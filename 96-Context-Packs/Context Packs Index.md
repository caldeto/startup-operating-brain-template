---
type: registry-index
status: implemented-gated
area: operations
owner: librarian-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[91-Agent-Instructions/AGENT_START_HERE]]"
  - "[[97-Registries/Schema Registry]]"
  - "[[97-Registries/Evidence Registry]]"
---

# Context Packs Index

Los Context Packs son entradas cortas para agentes y LLMs. Evitan leer todo el vault.

## Regla Principal

```text
Nunca leas todo el vault por defecto.
Lee el context pack del area, luego el indice del area, luego solo las notas necesarias.
```

## Packs

- [[Context Pack - Production]]
- [[Context Pack - Security]]
- [[Context Pack - Pipeline]]
- [[Context Pack - Monorepo]]
- [[Context Pack - Agents]]
- [[Context Pack - CEO Strategy]]
- [[Context Pack - References]]
- [[Context Pack - Product]]
- [[Context Pack - Evidence]]

## Orden Estandar Para Agentes

1. [[91-Agent-Instructions/AGENT_START_HERE]]
2. [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
3. Context Pack del area
4. Indice del area
5. Notas objetivo
6. [[97-Registries/Evidence Registry]] si necesita verificar
7. Crear Agent Run si modifica contenido relevante

