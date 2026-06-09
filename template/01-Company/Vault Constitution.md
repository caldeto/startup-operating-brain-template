---
type: vault-protocol
status: implemented-gated
area: company
owner: "{{FOUNDER_NAME}}"
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[00-Home/Startup Operating Brain]]"
  - "[[97-Registries/Schema Registry]]"
---

# Vault Constitution

This vault exists to preserve useful operating context without pretending to be the source of every truth.

## Source Of Truth

| Claim type | Primary source |
|---|---|
| Code behavior | `{{PRIMARY_REPO}}` and tests |
| Data pipeline behavior | `{{DATA_PIPELINE_REPO}}` and tests |
| Production status | `{{CLOUD_PROVIDER}}` runtime, deploys, logs, smoke tests |
| Decisions | `15-Decisions-ADR/` |
| Context and reasoning | This vault |
| AI output | Unverified until reviewed |

## Operating Rules

- Keep ideas, decisions, evidence, and production status separate.
- Do not mark a note `production` without evidence.
- Do not delete useful human context; mark it stale or archive it.
- Keep notes linked to an index or parent note.
- Keep startup-specific details out of reusable templates.
