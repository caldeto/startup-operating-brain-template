---
type: registry
status: implemented-gated
area: operations
owner: librarian-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Registries Index]]"
  - "[[91-Agent-Instructions/GLOBAL_AGENT_RULES]]"
---

# Schema Registry

## Objetivo

Definir vocabulario cerrado para que humanos y agentes mantengan el vault consistente.

## Propiedades Base

| Propiedad | Requerida | Descripcion |
|---|---:|---|
| `type` | si | Tipo de nota |
| `status` | si | Estado operativo |
| `area` | si | Area principal |
| `owner` | si | Responsable humano o agente |
| `layer` | si | Capa de grafo/contexto |
| `created_at` | recomendado | Fecha de creacion |
| `last_verified` | si para notas criticas | Fecha de ultima verificacion |
| `risk` | si para tecnico/produccion/seguridad | Riesgo |
| `confidence` | si | Confianza |
| `decision_critical` | recomendado | Si afecta decision importante |
| `links` | recomendado | Notas relacionadas |

## Valores Permitidos: `status`

```text
captured
triage
exploring
planned
in-progress
implemented-ungated
implemented-gated
production
blocked
stale
rejected
archived
accepted
proposed
```

## Valores Permitidos: `layer`

```text
knowledge
operation
template
prompt
canvas
evidence
archive
```

## Definicion De Layers

| Layer | Uso |
|---|---|
| `knowledge` | producto, negocio, tecnologia, estrategia, seguridad, arquitectura |
| `operation` | indices, instrucciones, workflows, reviews, bases |
| `template` | plantillas para crear notas |
| `prompt` | prompts reutilizables para agentes |
| `canvas` | mapas visuales y notas de Canvas |
| `evidence` | registros de fuente, verificacion, commits, outputs |
| `archive` | contenido historico o descartado |

## Valores Permitidos: `confidence`

```text
low
medium
high
```

## Valores Permitidos: `risk`

```text
low
medium
high
critical
```

## Tipos De Nota Permitidos

```text
agent-instruction
agent-run
architecture-model
base-spec
business-hypothesis
canvas-index
changelog
competitor
competitor-index
decision
decision-index
engineering-index
evidence
evidence-index
experiment
experiment-index
external-repo
home
idea
idea-index
inbox
market-research-index
meeting
meeting-index
metric
operating-brain
prd
product-index
prompt
reference
reference-index
registry
registry-index
risk
roadmap
security-finding
security-index
security-model
strategy
strategy-index
system-component
template
vault-protocol
```

## Regla Para Notas Nuevas

Si una nota nueva no puede clasificarse con este schema, crearla en `20-Inbox/` como:

```yaml
type: ai-output
status: captured
layer: operation
confidence: low
review_status: unreviewed
```

