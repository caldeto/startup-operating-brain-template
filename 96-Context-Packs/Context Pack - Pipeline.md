---
type: registry
status: implemented-gated
area: pipeline
owner: architecture-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
risk: medium
confidence: high
links:
  - "[[09-Pipeline/Pipeline Index]]"
  - "[[97-Registries/Source of Truth Map]]"
  - "[[97-Registries/Evidence Registry]]"
---

# Context Pack - Pipeline

## Usar Cuando

- auditar pipeline;
- actualizar estado del pipeline;
- cruzar contrato pipeline-monorepo;
- analizar ledger/data quality/freshness.

## Leer Primero

1. [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
2. [[09-Pipeline/Pipeline Index]]
3. [[97-Registries/Source of Truth Map]]
4. [[97-Registries/Evidence Registry]]

## Fuentes Esperadas

- `/Users/fran/conductor/repos/ecommerce-data-cleaning-pipeline`
- branch base: `origin/development`
- docs clave: `ROADMAP.md`, `docs/HANDOFF.md`, `docs/KNOWN_ISSUES.md`

## Reglas

- Pipeline manda en ingestion, limpieza, freshness, quality y medicion operacional.
- Separar implementado de planeado.
- Si una doc contradice codigo/tests, gana codigo/tests.

