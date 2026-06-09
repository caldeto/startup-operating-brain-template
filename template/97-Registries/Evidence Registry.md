---
type: evidence-index
status: implemented-gated
area: operations
owner: architecture-agent
layer: evidence
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Source of Truth Map]]"
  - "[[09-Data-Pipeline/Data Pipeline Index]]"
  - "[[10-App-Monorepo/App Monorepo Index]]"
---

# Evidence Registry

Record verifiable sources used for technical, production, security, roadmap, or decision claims.

## Source Inventory

| source_id | Type | Location | Expected branch | Status |
|---|---|---|---|---|
| operating-brain | vault | `{{LOCAL_OPERATING_BRAIN_PATH}}` | main | active |
| primary-app | github-repo | `{{PRIMARY_REPO}}` | main | pending-verification |
| data-pipeline | github-repo | `{{DATA_PIPELINE_REPO}}` | main | pending-verification |
| runtime | cloud-runtime | `{{CLOUD_PROVIDER}}` | n/a | pending-verification |

## Evidence Required For `implemented-gated`

- repository or system;
- branch or environment;
- commit, deployment, or timestamp;
- command or check result;
- verifier;
- linked note.

## Evidence Required For `production`

- runtime environment;
- service or domain;
- revision or deploy;
- IAM/secrets verification;
- health check or smoke test;
- rollback path.

## Verification Log

| Date | Source | Area | Verified by | Result | Note |
|---|---|---|---|---|---|
| YYYY-MM-DD | primary-app | engineering | owner | pending | Add first verification |
