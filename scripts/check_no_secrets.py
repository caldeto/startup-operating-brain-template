#!/usr/bin/env python3
"""Detect likely secrets committed to the vault."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKIP_DIRS = {".git", ".trash"}
SKIP_FILES = {".obsidian/workspace.json", ".obsidian/workspace-mobile.json"}
MAX_TEXT_BYTES = 1024 * 1024

PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("aws access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,255}\b")),
    ("openai api key", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    ("slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("google api key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    (
        "generic assigned secret",
        re.compile(
            r"(?i)\b(?:api[_-]?key|secret|token|password|passwd|pwd)\b\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{24,}"
        ),
    ),
]


def is_binary(sample: bytes) -> bool:
    return b"\0" in sample


def should_skip(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    return path.as_posix().lstrip("./") in SKIP_FILES


def main() -> int:
    errors: list[str] = []

    for path in sorted(Path(".").rglob("*")):
        if not path.is_file() or should_skip(path):
            continue

        data = path.read_bytes()
        if is_binary(data[:4096]):
            continue
        if len(data) > MAX_TEXT_BYTES:
            continue

        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path}:{line_number}: possible {label}")

    if errors:
        print("Secret scan failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Secret scan passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
