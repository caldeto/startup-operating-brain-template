# Quickstart

This path takes about 15 minutes.

1. Clone the repo.
2. Run `python3 scripts/bootstrap.py --startup "Acme AI" --founder "Jane Doe"`.
3. Open `startup-brain-vault/` in Obsidian.
4. Open `00-Home/Startup Operating Brain.md`.
5. Fill `02-Strategy/Vision.md`.
6. Update `97-Registries/Source of Truth Map.md` with your real repos and runtime.
7. Create your first ADR in `15-Decisions-ADR/`.
8. Create your first task packet from `93-Templates/template-prd.md` or a custom note.
9. Register your first agent run in `90-Agent-Runs/`.
10. Run the validators.

Local gates:

```bash
python3 scripts/validate_frontmatter.py startup-brain-vault
python3 scripts/validate_canvas_json.py startup-brain-vault
python3 scripts/check_required_links.py startup-brain-vault
```
