---
type: agent-instruction
status: implemented-gated
area: data-pipeline
owner: librarian-agent
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[09-Data-Pipeline/Data Pipeline Index]]"
  - "[[97-Registries/Evidence Registry]]"
---

# Context Pack - Data Pipeline

Use this pack for data ingestion, contracts, freshness, and data quality.

## Read First

- [[09-Data-Pipeline/Data Pipeline Index]]
- [[97-Registries/Evidence Registry]]

## Evidence Rules

- Do not claim implementation without repository or test evidence.
- Do not claim production without runtime evidence.
- Mark unverified AI output as `review_status: unreviewed`.

## Stop Conditions

Stop if the task needs a new architecture decision, production claim, or security severity change that is not supported by evidence.
