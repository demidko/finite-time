#!/usr/bin/env python3
"""Read the clock: the rate-limit window this agent is spending.

Claude Code: reads the OAuth token Claude Code keeps in ~/.claude/.credentials.json and asks
Anthropic's usage endpoint for the 5-hour and 7-day windows.
Codex: starts `codex app-server --listen stdio://` on the existing ChatGPT sign-in and calls
account/rateLimits/read (the documented app-server method; no model turn is spent).

Prints one line per window, in both notations, with time to reset. Never prints a token.
Exit code 1 with a one-line reason when no clock can be read; then ask the human.

    python3 usage.py            # try Claude Code, then Codex
    python3 usage.py --codex    # Codex only
    python3 usage.py --claude   # Claude Code only
"""
import datetime
import json
import os
import shutil
import subprocess
import sys
import urllib.request

CLAUDE_CREDENTIALS = os.environ.get("CLAUDE_CREDENTIALS", os.path.expanduser("~/.claude/.credentials.json"))
CLAUDE_URL = "https://api.anthropic.com/api/oauth/usage"
TIMEOUT = 20


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
            span = f"{minutes // 10080}-week" if minutes > 10080 else "weekly"
        elif minutes % 1440 == 0:
            span = f"{minutes // 1440}-day"
        elif minutes % 60 == 0:
            span = f"{minutes // 60}-hour"
        else:
            span = f"{minutes}-minute"
    else:
        span = slot
    name = limit_id if limit_id and limit_id != "codex" else "Codex"
    return f"{span} window ({name})"


def read_codex(now):
    binary = shutil.which("codex")
    if not binary:
        raise FileNotFoundError("no codex CLI on PATH")
    proc = subprocess.Popen(
        [binary, "app-server", "--listen", "stdio://"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
    )
    try:
        def send(message):
            proc.stdin.write(json.dumps(message) + "\n")
            proc.stdin.flush()

        def wait_for(request_id):
            deadline = datetime.datetime.now() + datetime.timedelta(seconds=TIMEOUT)
            while datetime.datetime.now() < deadline:
                raw = proc.stdout.readline()
                if not raw:
                    break
                try:
                    message = json.loads(raw)
                except ValueError:
                    continue
                if message.get("id") == request_id:
                    if "error" in message:
                        raise RuntimeError(message["error"].get("message", "app-server error"))
                    return message.get("result") or {}
            raise TimeoutError("no response from codex app-server")

        send({"id": 1, "method": "initialize", "params": {"clientInfo": {"name": "finite_time", "version": "1.0"}}})
        wait_for(1)
        send({"method": "initialized", "params": {}})
        send({"id": 2, "method": "account/rateLimits/read", "params": {}})
        result = wait_for(2)
    finally:
        proc.kill()
    limits = result.get("rateLimitsByLimitId") or ({"codex": result["rateLimits"]} if result.get("rateLimits") else {})
    out = []
    for limit_id, limit in limits.items():
        for slot in ("primary", "secondary"):
            window = limit.get(slot)
            if not window or window.get("usedPercent") is None:
                continue
            reset_at = None
            if window.get("resetsAt"):
                reset_at = datetime.datetime.fromtimestamp(window["resetsAt"], datetime.timezone.utc)
            out.append(line(window_label(limit_id, slot, window), window["usedPercent"], reset_at, now))
    return out


def main(argv):
    now = datetime.datetime.now(datetime.timezone.utc)
    want = {"--claude": ["claude"], "--codex": ["codex"]}.get(argv[0] if argv else "", ["claude", "codex"])
    readers = {"claude": read_claude, "codex": read_codex}
    reasons = []
    for name in want:
        try:
            lines = readers[name](now)
        except Exception as error:  # missing credentials or CLI, network, protocol
            reasons.append(f"{name}: {type(error).__name__}: {error}")
            continue
        if lines:
            print("\n".join(lines))
            return 0
        reasons.append(f"{name}: no windows in the response")
    print("clock unreadable (" + "; ".join(reasons) + "). Ask the human for the reading and the mark.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
