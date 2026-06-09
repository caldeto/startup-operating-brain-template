---
type: operating-brain
status: in-progress
area: company
owner: ceo
created_at: 2026-06-08
last_verified: 2026-06-08
source_of_truth:
  - obsidian
  - github
  - gcp
confidence: high
layer: operation
---

# BiBound Operating Brain

Este vault es el cerebro operativo de BiBound.

Su objetivo no es guardar mas notas. Su objetivo es mantener claridad, trazabilidad y utilidad para tomar decisiones sobre producto, tecnologia, negocio, seguridad y produccion.

## Constitucion

```text
GitHub = verdad tecnica ejecutable
GCP = verdad de produccion/runtime
Obsidian = cerebro estrategico, operativo y contextual
Codex/Claude/Conductor = agentes que ayudan a mantener, verificar y conectar
```

## Reglas Principales

1. Obsidian no reemplaza GitHub ni GCP.
2. Ninguna afirmacion tecnica critica se marca como verdad sin evidencia.
3. Todo input nuevo entra por `20-Inbox/` antes de convertirse en decision, PRD, riesgo o roadmap.
4. Toda nota importante debe tener `type`, `status`, `area`, `owner`, `risk`, `confidence` y `last_verified` cuando aplique.
5. Todo output de IA entra como `ai-output` y `review_status: unreviewed`.
6. Las decisiones se registran en `15-Decisions-ADR/`.
7. Los riesgos se registran en `06-Security/` o en el area afectada, pero deben aparecer en los indices.
8. El estado de produccion debe ser verificado con evidencia real.

## Estados Permitidos

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
```

## Tipos De Nota Permitidos

```text
system-component
production-status
prd
roadmap
decision
risk
reference
competitor
idea
experiment
metric
customer-insight
security-finding
architecture-model
agent-behavior
business-hypothesis
ai-output
meeting
external-repo
agent-run
```

## Entradas Principales

- [[00-Home/BiBound Operating Brain]]
- [[01-Company/Vault Constitution]]
- [[00-Home/Operating Principles]]
- [[03-Product/PRD - Operating Brain 10-10 Execution]]
- [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
- [[91-Agent-Instructions/AGENT_START_HERE]]
- [[96-Context-Packs/Context Packs Index]]
- [[97-Registries/Registries Index]]
- [[05-Production/Production Status]]
- [[06-Security/Security Index]]
- [[09-Pipeline/Pipeline Index]]
- [[10-Monorepo/Monorepo Index]]
- [[15-Decisions-ADR/Decision Index]]
- [[20-Inbox/Inbox Index]]
