---
type: registry
status: implemented-gated
area: monorepo
owner: architecture-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
risk: high
confidence: high
links:
  - "[[10-Monorepo/Monorepo Index]]"
  - "[[07-Agents-AI/Agent Runtime Index]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# Context Pack - Monorepo

## Usar Cuando

- auditar BiBound monorepo;
- analizar agents/analytics/orchestrator/BK-CM;
- revisar PRDs pendientes;
- actualizar production blockers;
- cruzar con pipeline.

## Leer Primero

1. [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
2. [[10-Monorepo/Monorepo Index]]
3. [[07-Agents-AI/Agent Runtime Index]]
4. [[08-Memory-Embeddings/Memory Embeddings Index]]
5. [[97-Registries/Source of Truth Map]]
6. [[97-Registries/Evidence Registry]]

## Fuentes Esperadas

- `/Users/fran/conductor/repos/bibound`
- branch base: `origin/development`
- main: produccion/release estable cuando aplique
- PR branches: candidatos, no verdad final hasta merge

## Reglas

- No asumir que `main` es estado de trabajo.
- Separar PRD pendiente de implementado.
- Verificar contra archivos, tests, commits o docs.

