---
type: registry
status: implemented-gated
area: production
owner: production-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
risk: high
confidence: high
links:
  - "[[05-Production/Production Status]]"
  - "[[05-Production/Production Readiness Checklist]]"
  - "[[11-GCP-Infra/GCP Infra Index]]"
  - "[[97-Registries/Evidence Registry]]"
---

# Context Pack - Production

## Usar Cuando

- actualizar estado de produccion;
- revisar dominio;
- revisar Cloud Run/GCP;
- evaluar si BiBound puede salir a produccion;
- preparar deploy checklist.

## Leer Primero

1. [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
2. [[05-Production/Production Status]]
3. [[05-Production/Production Readiness Checklist]]
4. [[11-GCP-Infra/GCP Infra Index]]
5. [[97-Registries/Source of Truth Map]]
6. [[97-Registries/Evidence Registry]]

## Reglas

- No marcar `production` sin evidencia GCP/runtime.
- Si no se puede verificar, usar `planned`, `blocked` o `unverified`.
- Todo blocker debe tener next action y owner.

## Outputs Permitidos

- actualizar Production Status;
- actualizar checklist;
- crear riesgo;
- crear Agent Run;
- proponer PRD o roadmap.

