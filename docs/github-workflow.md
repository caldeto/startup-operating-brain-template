# GitHub Workflow

Use small branches and small PRs. Do not mix unrelated scopes.

## Branch Model

- `main`: accepted stable template.
- `agent/*` or descriptive branches: proposed work.
- PRs: review, evidence, local verification, and merge history.

## Required PR Body

```text
## Summary

## Local Verification
- Base SHA:
- Commands run:
- Results:
- Tests skipped and why:

## Architecture / Contract Impact

## Security Impact

## Docs Updated

## Remaining Risk
```

## Gates

Run local validators before review. Optional GitHub Actions should mirror local gates and not replace them.
