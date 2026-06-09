---
type: agent-instruction
status: implemented-gated
area: security
owner: librarian-agent
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[06-Security/Security Index]]"
  - "[[06-Security/Threat Model]]"
---

# Context Pack - Security

Use this pack for threat model, data classification, prompt injection, and tool abuse.

## Read First

- [[06-Security/Security Index]]
- [[06-Security/Threat Model]]

## Evidence Rules

- Do not claim implementation without repository or test evidence.
- Do not claim production without runtime evidence.
- Mark unverified AI output as `review_status: unreviewed`.

## Stop Conditions

Stop if the task needs a new architecture decision, production claim, or security severity change that is not supported by evidence.
