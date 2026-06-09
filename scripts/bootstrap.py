#!/usr/bin/env python3
"""Create a customized startup operating brain vault from template/."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


DEFAULT_DEST = Path("startup-brain-vault")
TEXT_SUFFIXES = {
    ".md",
    ".canvas",
    ".json",
    ".yaml",
    ".yml",
    ".mmd",
    ".dbml",
    ".txt",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy template/ to a generated vault and replace startup placeholders."
    )
    parser.add_argument("--startup", required=True, help="Startup or project name")
    parser.add_argument("--founder", required=True, help="Founder or primary owner name")
    parser.add_argument("--primary-repo", default="{{PRIMARY_REPO}}", help="Primary app repository")
    parser.add_argument("--data-repo", default="{{DATA_PIPELINE_REPO}}", help="Data pipeline repository")
    parser.add_argument("--cloud", default="{{CLOUD_PROVIDER}}", help="Cloud/runtime provider")
    parser.add_argument("--dest", default=str(DEFAULT_DEST), help="Destination vault directory")
    parser.add_argument("--force", action="store_true", help="Replace destination if it already exists")
    return parser.parse_args()


def slugify(value: str) -> str:
    chars: list[str] = []
    previous_dash = False
    for char in value.lower():
        if char.isalnum():
            chars.append(char)
            previous_dash = False
        elif not previous_dash:
            chars.append("-")
            previous_dash = True
    return "".join(chars).strip("-") or "startup"


def copy_template(template: Path, dest: Path, force: bool) -> None:
    if not template.exists():
        raise SystemExit("template/ directory not found")
    if dest.exists():
        if not force:
            raise SystemExit(f"{dest} already exists. Re-run with --force to replace it.")
        shutil.rmtree(dest)
    shutil.copytree(template, dest)


def replace_placeholders(dest: Path, replacements: dict[str, str]) -> None:
    for path in sorted(dest.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    template = root / "template"
    requested_dest = Path(args.dest)
    dest = requested_dest
    if not dest.is_absolute():
        dest = root / dest
    dest_label = str(requested_dest)

    startup_slug = slugify(args.startup)
    cloud_lower = slugify(args.cloud).replace("-", "_")
    replacements = {
        "{{STARTUP_NAME}}": args.startup,
        "{{STARTUP_NAME_LOWER}}": startup_slug,
        "{{FOUNDER_NAME}}": args.founder,
        "{{PRIMARY_REPO}}": args.primary_repo,
        "{{DATA_PIPELINE_REPO}}": args.data_repo,
        "{{CLOUD_PROVIDER}}": args.cloud,
        "{{CLOUD_PROVIDER_LOWER}}": cloud_lower,
        "{{LOCAL_PRIMARY_REPO_PATH}}": f"~/repos/{args.primary_repo.split('/')[-1]}",
        "{{LOCAL_DATA_PIPELINE_REPO_PATH}}": f"~/repos/{args.data_repo.split('/')[-1]}",
        "{{LOCAL_OPERATING_BRAIN_PATH}}": dest_label,
        "{{LOCAL_PROJECT_PATH}}": str(requested_dest.parent) if str(requested_dest.parent) != "." else ".",
        "{{LOCAL_WORKSPACES_PATH}}": "~/conductor/workspaces",
        "{{LOCAL_USER_HOME}}": "~",
    }

    copy_template(template, dest, args.force)
    replace_placeholders(dest, replacements)
    print(f"Created startup operating brain vault at {dest}")
    print("Open this folder in Obsidian, then run:")
    print(f"  python3 scripts/validate_frontmatter.py {dest}")
    print(f"  python3 scripts/validate_canvas_json.py {dest}")
    print(f"  python3 scripts/check_required_links.py {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
