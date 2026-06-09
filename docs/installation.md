# Installation

Clone the template and generate your startup vault:

```bash
git clone https://github.com/caldeto/startup-operating-brain-template.git my-startup-brain
cd my-startup-brain
python3 scripts/bootstrap.py --startup "Acme AI" --founder "Jane Doe" --primary-repo "acme/app" --data-repo "acme/data-pipeline" --cloud "GCP"
python3 scripts/validate_frontmatter.py
```

The bootstrap command creates `startup-brain-vault/` by default. Open that folder as a vault in Obsidian.

## Optional Destination

```bash
python3 scripts/bootstrap.py --startup "Acme AI" --founder "Jane Doe" --dest ../acme-brain
```

Use `--force` only when you intend to replace an existing generated vault.

## First Checks

```bash
python3 scripts/validate_frontmatter.py startup-brain-vault
python3 scripts/validate_canvas_json.py startup-brain-vault
python3 scripts/check_required_links.py startup-brain-vault
```

Then create your first note in `20-Inbox/` or your first ADR in `15-Decisions-ADR/`.
