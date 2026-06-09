# Local Quality Gates

Local gates are the primary quality contract.

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/validate_canvas_json.py
python3 scripts/check_required_links.py
python3 scripts/check_no_secrets.py
python3 scripts/check_large_files.py
```

The frontmatter, Canvas, and link checks target `template/` and curated example notes by default. Secret and large-file checks scan the repository, excluding local `.context` workspace state.

For generated vaults, pass the vault path:

```bash
python3 scripts/validate_frontmatter.py startup-brain-vault
python3 scripts/validate_canvas_json.py startup-brain-vault
python3 scripts/check_required_links.py startup-brain-vault
```
