#!/usr/bin/env python3
"""Check the portable package and repository links with the Python standard library."""

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "finite-time"
SKIP = {".git", ".venv", "dist", "__pycache__", "comparison-2026-10-06"}


def files():
    return sorted(p for p in ROOT.rglob("*")
                  if p.is_file() and not any(part in SKIP for part in p.relative_to(ROOT).parts))


def check():
    errors = []
    source = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    parts = source.split("---\n", 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError("SKILL.md must begin with YAML frontmatter")

    # This project uses a deliberately small, scalar-only YAML subset. Reject
    # unsupported syntax rather than silently pretending to parse arbitrary YAML.
    metadata = {}
    in_metadata = False
    for line in parts[1].splitlines():
        if in_metadata and line.startswith("  "):
            key, separator, value = line.strip().partition(": ")
            if not separator or key not in {"author", "version"} or "metadata." + key in metadata:
                errors.append(f"Unexpected metadata line: {line}")
                continue
            metadata["metadata." + key] = json.loads(value) if value.startswith('"') else value
            continue
        in_metadata = line == "metadata:"
        if in_metadata:
            continue
        key, separator, value = line.partition(": ")
        if not separator or key not in {"name", "description", "license"} or key in metadata:
            errors.append(f"Unexpected frontmatter line: {line}")
            continue
        metadata[key] = json.loads(value) if value.startswith('"') else value
    name = metadata.get("name", "")
    if name != SKILL.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("Invalid skill name or directory name")
    if not 1 <= len(metadata.get("description", "")) <= 1024:
        errors.append("Description must contain 1–1024 characters")
    if metadata.get("license") != "MIT":
        errors.append("Expected MIT skill license")
    if (SKILL / "LICENSE").read_bytes() != (ROOT / "LICENSE").read_bytes():
        errors.append("Bundled license differs from root license")
    version = (ROOT / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:\.[2-9]\d*|\.1\d+)?", version):
        errors.append("VERSION must be YYYY-MM-DD, optionally followed by a same-day edition such as .2")
    else:
        date.fromisoformat(version.split(".", 1)[0])
    if metadata.get("metadata.version") != version:
        errors.append("SKILL.md metadata.version must equal VERSION")

    expected_files = {"SKILL.md", "TIME-LENS.md", "LICENSE", "usage.py"}
    actual_files = {str(p.relative_to(SKILL)) for p in SKILL.rglob("*") if p.is_file()}
    if actual_files != expected_files:
        errors.append(f"Runtime package must be flat: {sorted(expected_files)}")

    for path in files():
        data = path.read_text(encoding="utf-8")
        if re.search(r"[\u0400-\u04ff]", data):
            errors.append(f"Non-English Cyrillic text in {path.relative_to(ROOT)}")
        if re.search(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|glpat-[A-Za-z0-9_-]{16,})", data):
            errors.append(f"Possible credential in {path.relative_to(ROOT)}")
        if path.suffix == ".md":
            links = re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", data)
            links += re.findall(r'(?:href|src)="([^"]+)"', data)
            for link in links:
                parsed = urlsplit(link)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (path.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    errors.append(f"Broken local link in {path.relative_to(ROOT)}: {link}")
        if path.suffix == ".svg":
            ElementTree.fromstring(data)

    cases = json.loads((ROOT / "evals" / "cases.json").read_text())
    ids = [case["id"] for case in cases]
    if len(set(ids)) != len(ids) or not cases:
        errors.append("Behavioral cases must have unique IDs")
    for case in cases:
        if not case.get("messages") or not case.get("expected"):
            errors.append(f"Incomplete behavioral case: {case['id']}")

    if errors:
        raise ValueError("\n".join(errors))
    print(f"Package checks passed: {len(files())} files, {len(cases)} behavioral cases defined.")


if __name__ == "__main__":
    try:
        check()
    except (ValueError, OSError, KeyError, ElementTree.ParseError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
