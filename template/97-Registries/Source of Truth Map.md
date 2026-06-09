---
type: registry
status: implemented-gated
area: operations
owner: architecture-agent
layer: evidence
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Registries Index]]"
  - "[[01-Company/Vault Constitution]]"
---

# Source of Truth Map

Use this map when notes, repos, runtime, and AI output conflict.

| Topic | Primary source | Secondary source | Notes |
|---|---|---|---|
| App code | `{{PRIMARY_REPO}}` | PR branches | Code and tests beat docs. |
| Data pipeline | `{{DATA_PIPELINE_REPO}}` | PR branches | Schema and contract tests beat plans. |
| Production runtime | `{{CLOUD_PROVIDER}}` | Deploy config | Do not mark production without runtime evidence. |
| Technical contracts | Repos and tests | PRDs | Tests and fixtures beat prose. |
| Security | Code, config, tests, runtime IAM | Threat model | Do not lower severity without evidence. |
| Roadmap | Current PRD and repo state | Strategy notes | Keep planned separate from implemented. |
| Decisions | `15-Decisions-ADR/` | Meetings | Decisions need alternatives and tradeoffs. |
| Ideas | `20-Inbox/` or strategy notes | AI summaries | Ideas are not decisions. |
| External references | Source URL and notes | AI summaries | Record why the reference matters. |

## Conflict Rule

```text
runtime > code > tests > config > versioned docs > operating brain > AI output
```
