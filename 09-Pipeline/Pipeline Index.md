---
type: system-component
status: implemented-gated
area: pipeline
owner: engineering
source_of_truth:
  - github
created_at: 2026-06-08
last_verified: 2026-06-09
verified_by: codex
risk: medium
confidence: high
links:
  - "[[10-Monorepo/Monorepo Index]]"
  - "[[17-Metrics/Measurement Ledger]]"
  - "[[docs/model/README]]"
  - "[[docs/model/contracts/pipeline-consumer-v3]]"
layer: knowledge
---

# Pipeline Index

## Fuente Verificada

- Repo: `caldeto/ecommerce-data-cleaning-pipeline`
- Branch: `development`
- Snapshot verificado: `d1b74e5`
- Estado: `implemented-gated`

## Que Manda El Pipeline

- ingestion xlsx;
- limpieza y normalizacion;
- identity resolution;
- features, freshness, CLV/RFM;
- tablas warehouse pipeline-owned;
- ledger BigQuery `measurement`;
- data quality detector/triage;
- roles DB pipeline/runtime/migrate;
- jobs/schedulers del pipeline.

## Modelo

- [[docs/model/history/2026-06-04]]
- [[docs/model/history/2026-06-05]]
- [[docs/model/history/2026-06-06]]
- [[docs/model/history/2026-06-07]]
- [[docs/model/history/2026-06-08]]
- [[docs/model/contracts/pipeline-consumer-v3]]
