---
type: security-model
status: in-progress
area: security
owner: security-agent
layer: knowledge
created_at: 2026-06-09
last_verified: 2026-06-09
risk: high
confidence: medium
links:
  - "[[06-Security/IAM Matrix]]"
  - "[[docs/model/README]]"
---

# IAM Matrix

## GCP Roles By Runtime

| Principal | Owns/uses | Expected privileges | Status |
|---|---|---|---|
| GitHub deployer SA | CI/CD deploy | WIF, build/deploy, actAs limited SAs | implemented-gated |
| Pipeline runtime SA | pipeline-api | read GCS uploads, connect Cloud SQL as app role | implemented-gated |
| Pipeline migrate SA/job | migrations | owner/migrate DB secret, schema changes | implemented-gated |
| Measurement exporter SA | ledger exporter | BigQuery write dataset-scoped, drain outbox | implemented-gated |
| Data quality runner SA | data quality job | read-mostly DB role, LLM role config | implemented-gated |
| Monorepo runtime SAs | backend/agent/analytics/orchestrator/bk-cm | service-specific Cloud Run runtime access | planned |
| Human admin | GitHub/GCP admin | break-glass only | planned |

## DB Roles

| Role | Owner | Use | Risk |
|---|---|---|---|
| `pipeline` | pipeline | migrate/owner role | high if exposed to runtime |
| `pipeline_app` | pipeline | no-owner runtime DML | intended runtime role |
| `pipeline_data_quality` | pipeline | read-mostly data quality | intended job role |
| monorepo app roles | monorepo | app-owned schemas/read models | planned/partial |
| `agent_readonly` | monorepo agent | SQL sandbox read-only role | high, requires strict tests |

## Required Before Production

- Verify live IAM bindings with GCP, not just Terraform files.
- Confirm no long-lived JSON keys in runtime.
- Confirm Secret Manager access is per service, not broad project-wide.
- Confirm DB migrate secrets are unavailable to normal runtime services.

