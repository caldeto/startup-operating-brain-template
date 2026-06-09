---
type: roadmap
status: planned
area: operations
owner: ceo
layer: evidence
created_at: 2026-06-08
last_verified: 2026-06-08
risk: medium
confidence: high
links:
  - "[[97-Registries/Source of Truth Map]]"
  - "[[03-Product/PRD - Operating Brain 10-10 Execution]]"
---

# Repo Connection Plan

## Decision

El Operating Brain vivira como repositorio GitHub independiente.

## Modelo Recomendado

```text
main = conocimiento aceptado
development = cambios revisables
agent/<scope> = cambios generados por agentes
```

## Conexiones

| Conexion | Metodo inicial | Motivo |
|---|---|---|
| Monorepo BiBound | Evidence Registry + notas verificadas | evita submodulos y ruido |
| Pipeline | Evidence Registry + notas verificadas | mantiene independencia |
| GCP | Production Status + evidencia manual/automatizable | runtime no vive en Obsidian |
| Conductor/Codex | Agent Runs + prompts + context packs | trazabilidad |

## No Usar Todavia

- submodulos;
- sincronizacion automatica agresiva;
- agentes con write directo a main.

## Futuro

Cuando el repo este estable:

- GitHub Actions para lint de front matter;
- validacion de links;
- check de Canvas JSON;
- reportes de notas sin `type/status/layer`.

