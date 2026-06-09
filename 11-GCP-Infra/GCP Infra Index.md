---
type: architecture-model
status: in-progress
area: infra
owner: production-agent
created_at: 2026-06-08
last_verified: 2026-06-09
risk: high
confidence: medium
links:
  - "[[05-Production/Production Status]]"
  - "[[06-Security/IAM Matrix]]"
  - "[[docs/model/README]]"
  - "[[docs/model/security/iam-matrix]]"
layer: knowledge
---

# GCP Infra Index

## Estado

GCP esta modelado y parcialmente implementado en repos, pero no se marca produccion sin verificacion runtime.

## Componentes

- Cloud Run;
- Cloud SQL Postgres 16;
- BigQuery measurement;
- Secret Manager;
- Artifact Registry;
- Workload Identity Federation;
- service accounts/IAM;
- Cloud Scheduler jobs.

## Leer

- `docs/model/diagrams/gcp-infra.mmd`
- [[docs/model/security/iam-matrix]]
- [[docs/model/security/production-readiness]]
