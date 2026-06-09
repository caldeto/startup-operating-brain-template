---
type: registry
status: implemented-gated
area: operations
owner: architecture-agent
layer: evidence
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Registries Index]]"
  - "[[01-Company/Vault Constitution]]"
---

# Source of Truth Map

## Objetivo

Definir que fuente manda para cada tipo de afirmacion.

## Mapa

| Tema | Fuente que manda | Fuente secundaria | Nota |
|---|---|---|---|
| Codigo monorepo | `caldeto/bibound` `origin/development` | branches de PR | main es produccion, development es base de trabajo |
| Codigo pipeline | `ecommerce-data-cleaning-pipeline` `origin/development` | branches de PR | development es base real |
| Produccion runtime | GCP | GitHub deploy configs | Obsidian no puede declarar produccion sin evidencia GCP |
| Contratos tecnicos | repo + tests + fixtures | PRD | Codigo/tests ganan sobre docs |
| Seguridad | codigo/config/tests + GCP/IAM | threat model | No bajar severidad sin evidencia |
| Roadmap tecnico | PRD vigente + repo state | Obsidian | Separar planned de implemented |
| Decisiones | `15-Decisions-ADR/` | conversaciones | Decision debe tener contexto y tradeoffs |
| Ideas CEO | `02-Strategy/CEO Idea Pipeline` | Inbox | Idea no es decision |
| Referencias externas | nota reference + source_url | resumen IA | Siempre explicar uso potencial |
| Estado del brain | este repo | Obsidian workspace local | workspace visual no manda sobre contenido |

## Regla De Ramas

Para monorepo y pipeline:

```text
origin/development = base verdadera de analisis
main = produccion o release estable cuando aplique
branch local = posible trabajo en curso
PR branch = candidato, no verdad aceptada hasta merge
```

## Regla De Conflictos

```text
codigo > tests > configs runtime > docs versionadas > Obsidian > output IA
```

