---
type: agent-instruction
status: implemented-gated
area: operations
owner: librarian-agent
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[97-Registries/Evidence Registry]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# Context Pack - Evidence

Use this pack for evidence, source of truth, and verification.

## Read First

- [[97-Registries/Evidence Registry]]
- [[97-Registries/Source of Truth Map]]

## Evidence Rules

- Do not claim implementation without repository or test evidence.
- Do not claim production without runtime evidence.
- Mark unverified AI output as `review_status: unreviewed`.

## Stop Conditions

Stop if the task needs a new architecture decision, production claim, or security severity change that is not supported by evidence.
