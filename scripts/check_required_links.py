#!/usr/bin/env python3
"""Validate required evidence links and report broken Obsidian wiki links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DEFAULT_ROOTS = (Path("template"), Path("examples/bibound"))
SKIP_DIRS = {".git", ".obsidian", ".trash", "archive"}
WIKILINK_RE = re.compile(r"!\[\[([^\]]+)\]\]|\[\[([^\]]+)\]\]")


def parse_roots(argv: list[str]) -> list[Path]:
    if argv:
        return [Path(arg) for arg in argv]
    return list(DEFAULT_ROOTS)


def iter_markdown_files(roots: list[Path]):
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


def parse_frontmatter(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body = lines[1:index]
            break
    else:
        return {}

    fields: dict[str, str] = {}
    for line in body:
        if not line.strip() or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def build_note_index(roots: list[Path]):
    by_stem: dict[str, list[Path]] = {}
    by_path: set[str] = set()

    for path in iter_markdown_files(roots):
        rel = path
        by_path.add(rel.with_suffix("").as_posix())
        by_path.add(rel.as_posix())
        by_stem.setdefault(path.stem, []).append(rel)

    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.canvas")):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            rel = path
            by_path.add(rel.with_suffix("").as_posix())
            by_path.add(rel.as_posix())
            by_stem.setdefault(path.stem, []).append(rel)

    return by_stem, by_path


def link_target_exists(target: str, by_stem: dict[str, list[Path]], by_path: set[str]) -> bool:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return True
    if target in by_path:
        return True
    if target.endswith((".md", ".canvas")) and target in by_path:
        return True
    return Path(target).stem in by_stem


def main() -> int:
    roots = parse_roots(sys.argv[1:])
    errors: list[str] = []
    warnings: list[str] = []
    by_stem, by_path = build_note_index(roots)

    for path in iter_markdown_files(roots):
        text = path.read_text(encoding="utf-8")
        fields = parse_frontmatter(path)

        if fields.get("status") == "production":
            has_evidence = "evidence" in fields and bool(fields["evidence"])
            has_source = "source_of_truth" in fields and bool(fields["source_of_truth"])
            if not has_evidence and not has_source:
                errors.append(f"{path}: status is production but evidence/source_of_truth is missing")

        for match in WIKILINK_RE.finditer(text):
            target = match.group(1) or match.group(2) or ""
            if not link_target_exists(target, by_stem, by_path):
                warnings.append(f"{path}: possible broken wiki link: [[{target}]]")

    if warnings:
        print("Non-blocking wiki link warnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("Required evidence link check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Required evidence link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
