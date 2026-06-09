---
type: metric
status: implemented-gated
area: metrics
owner: product-agent
created_at: 2026-06-08
last_verified: 2026-06-09
risk: high
confidence: high
links:
  - "[[07-Agents-AI/Copilot Action Policy]]"
  - "[[docs/model/history/2026-06-08]]"
  - "[[docs/model/README]]"
layer: knowledge
---

# Measurement Ledger

## Estado

El pipeline implemento el ledger BigQuery en Fase 7: DDL, `measurement-ingest`, outbox transaccional, exporter, infra/IAM y tests de consistencia. Sigue `implemented-gated` porque el Operating Brain no verifico runtime productivo.

## Leer

- [[docs/model/history/2026-06-08]]
- `docs/model/diagrams/data-lineage.mmd`
