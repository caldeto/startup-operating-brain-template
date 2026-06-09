#!/usr/bin/env python3
"""Validate that Obsidian Canvas files contain JSON."""

from __future__ import annotations

import json
import sys
from pathlib import Path


SKIP_DIRS = {".git", ".trash"}


def main() -> int:
    errors: list[str] = []

    for path in sorted(Path(".").rglob("*.canvas")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError as exc:
            errors.append(f"{path}: cannot read as UTF-8: {exc}")
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}")

    if errors:
        print("Canvas JSON validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Canvas JSON validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
