#!/usr/bin/env python3
"""Reject accidentally large files in the vault."""

from __future__ import annotations

import os
import sys
from pathlib import Path


MAX_FILE_MB = int(os.environ.get("MAX_FILE_MB", "10"))
MAX_BYTES = MAX_FILE_MB * 1024 * 1024
SKIP_DIRS = {".git", ".trash"}


def main() -> int:
    errors: list[str] = []

    for path in sorted(Path(".").rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        size = path.stat().st_size
        if size > MAX_BYTES:
            size_mb = size / 1024 / 1024
            errors.append(f"{path}: {size_mb:.2f} MB exceeds {MAX_FILE_MB} MB limit")

    if errors:
        print("Large file check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Large file check passed. Limit: {MAX_FILE_MB} MB.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
