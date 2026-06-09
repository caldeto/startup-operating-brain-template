#!/usr/bin/env python3
"""Validate that Obsidian Canvas files contain JSON."""

from __future__ import annotations

import json
import sys
from pathlib import Path


DEFAULT_ROOTS = (Path("template"), Path("examples/bibound"))
SKIP_DIRS = {".git", ".trash", "archive"}


def parse_roots(argv: list[str]) -> list[Path]:
    if argv:
        return [Path(arg) for arg in argv]
    return list(DEFAULT_ROOTS)


def main() -> int:
    roots = parse_roots(sys.argv[1:])
    errors: list[str] = []

    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.canvas")):
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
