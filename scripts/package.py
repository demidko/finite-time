#!/usr/bin/env python3
"""Build a reproducible, single-folder Agent Skills ZIP and its checksum."""

import hashlib
import zipfile
from datetime import date

from check import ROOT, SKILL, check


def main():
    check()
    version = (ROOT / "VERSION").read_text().strip()
    released = date.fromisoformat(version.split(".", 1)[0])
    destination = ROOT / "dist"
    destination.mkdir(exist_ok=True)
    archive = destination / f"finite-time-{version}.zip"
    package_files = [
        "SKILL.md",
        "LICENSE",
        "TIME-LENS.md",
        "usage.py",
    ]
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for relative in sorted(package_files):
            info = zipfile.ZipInfo("finite-time/" + relative,
                                   date_time=(released.year, released.month, released.day, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (0o100755 if relative.endswith(".py") else 0o100644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, (SKILL / relative).read_bytes())
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (destination / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n")
    print(f"Built {archive.name} ({archive.stat().st_size} bytes), SHA-256 {digest}")


if __name__ == "__main__":
    main()
