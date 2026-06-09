---
type: agent-instruction
status: implemented-gated
area: production
owner: librarian-agent
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[05-Production/Production Status]]"
  - "[[05-Production/Production Readiness Checklist]]"
---

# Context Pack - Production

Use this pack for runtime readiness, deploy evidence, rollback, and smoke tests.

## Read First

- [[05-Production/Production Status]]
- [[05-Production/Production Readiness Checklist]]

## Evidence Rules

- Do not claim implementation without repository or test evidence.
- Do not claim production without runtime evidence.
- Mark unverified AI output as `review_status: unreviewed`.

## Stop Conditions

Stop if the task needs a new architecture decision, production claim, or security severity change that is not supported by evidence.
