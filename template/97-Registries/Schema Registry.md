---
type: registry
status: implemented-gated
area: operations
owner: librarian-agent
layer: operation
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Registries Index]]"
  - "[[91-Agent-Instructions/GLOBAL_AGENT_RULES]]"
---

# Schema Registry

Use this registry to keep humans and agents consistent.

## Required Properties

| Property | Required | Use |
|---|---:|---|
| `type` | yes | Note kind |
| `status` | yes | Operational state |
| `area` | yes | Primary area |
| `owner` | yes | Human role or agent |
| `layer` | yes | Graph/context layer |
| `created_at` | recommended | Creation date |
| `last_verified` | critical notes | Last verification date |
| `risk` | technical/security/production | Risk level |
| `confidence` | yes | Confidence level |
| `decision_critical` | recommended | Whether it affects decisions |
| `links` | recommended | Related notes |

## Status Values

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

## Layer Values

```text
knowledge
operation
template
prompt
canvas
evidence
archive
```

## Confidence Values

```text
low
medium
high
```

## Risk Values

```text
low
medium
high
critical
```

## Note Types

```text
agent-instruction
agent-run
architecture-model
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
view-spec
```
