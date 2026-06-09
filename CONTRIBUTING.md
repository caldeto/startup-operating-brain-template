# Contributing

Thanks for improving Startup Operating Brain Template.

## Principles

- Keep the template generic and reusable.
- Keep startup-specific material in `examples/`, never in `template/`.
- Treat AI-generated content as unverified until evidence is recorded.
- Do not add secrets, private paths, customer data, or personal credentials.
- Prefer small PRs with clear evidence and local verification.

## Adding Or Changing Template Notes

1. Use the existing frontmatter schema in `template/97-Registries/Schema Registry.md`.
2. Link new notes to a parent index or context pack.
3. Keep agent instructions short and operational.
4. Update Canvas files only when the JSON remains valid.
5. Run the local validators before opening a PR.

## Adding Context Packs

A context pack should tell an agent what to read, what not to read, and what evidence is required. It should reduce tokens, not become another full manual.

## Local Validation

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/validate_canvas_json.py
python3 scripts/check_required_links.py
python3 scripts/check_no_secrets.py
python3 scripts/check_large_files.py
```

## Pull Requests

Use the PR template. Include commands run, results, skipped tests, architecture impact, security impact, docs updated, and remaining risk.
