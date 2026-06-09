#!/usr/bin/env python3
"""Validate required front matter for vault markdown notes."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_KEYS = {"type", "status", "area", "owner", "layer"}
SKIP_DIRS = {".git", ".obsidian", ".trash"}


def iter_markdown_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def parse_frontmatter(path: Path):
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as exc:
        return None, f"cannot read as UTF-8: {exc}"

    if not lines or lines[0].strip() != "---":
        return None, "missing YAML front matter"

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body = lines[1:index]
            break
    else:
        return None, "front matter is not closed with ---"

    keys: dict[str, str] = {}
    for line in body:
        if not line.strip() or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        keys[key.strip()] = value.strip()

    return keys, None


def main() -> int:
    root = Path(".")
    errors: list[str] = []

    for path in iter_markdown_files(root):
        fields, error = parse_frontmatter(path)
        if error:
            errors.append(f"{path}: {error}")
            continue

        assert fields is not None
        missing = sorted(key for key in REQUIRED_KEYS if key not in fields)
        empty = sorted(key for key in REQUIRED_KEYS if key in fields and not fields[key])

        if missing:
            errors.append(f"{path}: missing required key(s): {', '.join(missing)}")
        if empty:
            errors.append(f"{path}: empty required key(s): {', '.join(empty)}")

    if errors:
        print("Front matter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Front matter validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
