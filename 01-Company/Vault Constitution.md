---
type: decision
status: accepted
area: company
owner: ceo
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
risk: medium
confidence: high
decision_critical: true
links:
  - "[[00-Home/BiBound Operating Brain]]"
  - "[[15-Decisions-ADR/ADR-0001 Use Obsidian as BiBound Operating Brain]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# Vault Constitution

## Principio Central

```text
GitHub = verdad tecnica ejecutable
GCP = verdad de produccion/runtime
Obsidian = cerebro estrategico, operativo y contextual
Codex/Claude/Conductor = agentes que ayudan a mantener, verificar y conectar
```

## Reglas Constitucionales

1. Obsidian no reemplaza GitHub ni GCP.
2. Una nota puede orientar decisiones, pero debe citar evidencia si afirma estado tecnico.
3. Toda idea entra como idea, no como decision.
4. Toda referencia externa debe explicar para que podria servir en BiBound.
5. Todo output IA entra como no revisado hasta validarse.
6. Toda decision relevante vive en `15-Decisions-ADR/`.
7. Todo cambio relevante de agente deja `Agent Run`.
8. El vault debe mantenerse legible para humanos y barato en tokens para agentes.

## Politica De Conflictos

| Conflicto | Fuente que gana |
|---|---|
| Obsidian vs codigo | Codigo |
| Docs vs codigo | Codigo |
| Obsidian vs GCP runtime | GCP |
| branch local vs `origin/development` | `origin/development` |
| idea vs evidencia | evidencia |

