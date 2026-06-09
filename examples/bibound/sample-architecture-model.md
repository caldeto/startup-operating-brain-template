---
type: architecture-model
status: implemented-gated
area: examples
owner: maintainer
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: knowledge
---

# Sample Architecture Model

## System Boundaries

| Boundary | Source Of Truth | Notes |
|---|---|---|
| App monorepo | GitHub repository | Code and tests are technical truth. |
| Data pipeline | GitHub repository | Pipeline contracts and schema are technical truth. |
| Runtime | Cloud provider | Runtime evidence is production truth. |
| Operating brain | Obsidian + GitHub | Context, decisions, evidence, and review history. |

## Lesson

The operating brain is strongest when it records what each system owns and refuses to turn aspirational notes into verified status.
