# Repo Governance

This repository ships a public operating-brain template. The root contains OSS docs, scripts, GitHub metadata, and examples. The active reusable vault lives in `template/`.

## Rules

- Keep `template/` generic.
- Keep company-specific examples under `examples/`.
- Do not commit secrets, private paths, or sensitive data.
- Use local validators as the main quality gate.
- Record PR evidence in the PR body.

## Source Of Truth

- GitHub is technical truth for this repository.
- Generated vaults are user-specific outputs.
- Examples are references, not template defaults.
