#!/usr/bin/env python3
"""Read the clock: the rate-limit window this agent is spending.

Claude Code (--claude): reads the OAuth token Claude Code keeps in ~/.claude/.credentials.json and
asks Anthropic's usage endpoint for the 5-hour and 7-day windows.
Codex (--codex): starts `codex app-server --listen stdio://` on the existing ChatGPT sign-in and
calls account/rateLimits/read, the documented app-server method; no model turn is spent.

Pass the flag for the harness you run in. Without a flag the script detects the harness from the
environment (CLAUDECODE, CODEX_*) and refuses to guess when it cannot: one provider's quota is never
substituted for another's. Prints one line per window, in both notations, with time to reset.
Never prints a token. Exit 1 with a one-line reason when the clock cannot be read; then ask the
human. Exit 2 when the harness is unknown.
"""
import datetime
import json
import os
import queue
import shutil
import subprocess
import sys
import threading
import urllib.request

CLAUDE_CREDENTIALS = os.environ.get("CLAUDE_CREDENTIALS", os.path.expanduser("~/.claude/.credentials.json"))
CLAUDE_URL = "https://api.anthropic.com/api/oauth/usage"
TIMEOUT = float(os.environ.get("FINITE_TIME_TIMEOUT", "20"))


def countdown(reset_at, now):
    seconds = max(int((reset_at - now).total_seconds()), 0)
    hours, minutes = divmod(seconds // 60, 60)
    if hours >= 48:
        return f"{hours // 24}d {hours % 24}h"
    return f"{hours}h {minutes:02d}m"


def line(label, used, reset_at, now):
    used = max(0.0, min(100.0, float(used)))
    text = f"{label}: {used:.0f}% used, {100 - used:.0f}% left"
    if reset_at is not None:
        text += f", resets in {countdown(reset_at, now)}"
    return text


def read_claude(now):
    with open(CLAUDE_CREDENTIALS) as f:
        token = json.load(f)["claudeAiOauth"]["accessToken"]
    request = urllib.request.Request(
        CLAUDE_URL,
        headers={"Authorization": "Bearer " + token, "anthropic-beta": "oauth-2025-04-20", "User-Agent": "claude-code"},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        data = json.load(response)
    out = []
    for key, label in (("five_hour", "5-hour window (Claude)"), ("seven_day", "7-day window (Claude)")):
        window = data.get(key) or {}
        if window.get("utilization") is None:
            continue
        reset_at = None
        if window.get("resets_at"):
            reset_at = datetime.datetime.fromisoformat(window["resets_at"].replace("Z", "+00:00"))
        out.append(line(label, window["utilization"], reset_at, now))
    return out


def window_label(limit_id, slot, window):
    minutes = window.get("windowDurationMins")
    if minutes:
        if minutes % 10080 == 0:
            span = "weekly" if minutes == 10080 else f"{minutes // 10080}-week"
        elif minutes % 1440 == 0:
            span = f"{minutes // 1440}-day"
        elif minutes % 60 == 0:
            span = f"{minutes // 60}-hour"
        else:
            span = f"{minutes}-minute"
    else:
        span = slot
    name = "Codex" if not limit_id or limit_id == "codex" else limit_id
    return f"{span} window ({name})"


def read_codex(now):
    binary = shutil.which("codex")
    if not binary:
        raise FileNotFoundError("no codex CLI on PATH")
    proc = subprocess.Popen(
        [binary, "app-server", "--listen", "stdio://"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
    )
    lines = queue.Queue()
    threading.Thread(target=lambda: [lines.put(raw) for raw in iter(proc.stdout.readline, "")], daemon=True).start()
    deadline = datetime.datetime.now() + datetime.timedelta(seconds=TIMEOUT)
    try:
        def send(message):
            proc.stdin.write(json.dumps(message) + "\n")
            proc.stdin.flush()

        def wait_for(request_id):
            while True:
                remaining = (deadline - datetime.datetime.now()).total_seconds()
                if remaining <= 0:
                    raise TimeoutError(f"no response from codex app-server within {TIMEOUT:g}s")
                try:
                    raw = lines.get(timeout=remaining)
                except queue.Empty:
                    raise TimeoutError(f"no response from codex app-server within {TIMEOUT:g}s")
                try:
                    message = json.loads(raw)
                except ValueError:
                    continue
                if message.get("id") == request_id:
                    if "error" in message:
                        raise RuntimeError(message["error"].get("message", "app-server error"))
                    return message.get("result") or {}

        send({"id": 1, "method": "initialize", "params": {"clientInfo": {"name": "finite_time", "title": "finite-time", "version": "1.0"}}})
        wait_for(1)
        send({"method": "initialized", "params": {}})
        send({"id": 2, "method": "account/rateLimits/read", "params": {}})
        result = wait_for(2)
    finally:
        proc.kill()
        proc.wait()
    limits = result.get("rateLimitsByLimitId") or ({"codex": result["rateLimits"]} if result.get("rateLimits") else {})
    out = []
    for limit_id, limit in limits.items():
        for slot in ("primary", "secondary"):
            window = (limit or {}).get(slot)
            if not window or window.get("usedPercent") is None:
                continue
            reset_at = None
            if window.get("resetsAt"):
                reset_at = datetime.datetime.fromtimestamp(window["resetsAt"], datetime.timezone.utc)
            out.append(line(window_label(limit_id, slot, window), window["usedPercent"], reset_at, now))
    return out


def detect_harness():
    if os.environ.get("CLAUDECODE") or os.environ.get("CLAUDE_CODE_ENTRYPOINT"):
        return "claude"
    if any(key.startswith("CODEX_") for key in os.environ):
        return "codex"
    return None


def main(argv):
    flags = {"--claude": "claude", "--codex": "codex"}
    harness = flags.get(argv[0]) if argv else detect_harness()
    if harness is None:
        print("harness unknown: pass --claude or --codex. One provider's quota is never read in place of another's.", file=sys.stderr)
        return 2
    now = datetime.datetime.now(datetime.timezone.utc)
    try:
        lines = {"claude": read_claude, "codex": read_codex}[harness](now)
    except Exception as error:  # missing credentials or CLI, network, protocol, timeout
        print(f"clock unreadable ({harness}: {type(error).__name__}: {error}). Ask the human for the reading and the mark.", file=sys.stderr)
        return 1
    if not lines:
        print(f"clock unreadable ({harness}: no windows in the response). Ask the human for the reading and the mark.", file=sys.stderr)
        return 1
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
