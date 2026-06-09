---
type: operating-brain
status: implemented-gated
area: company
owner: "{{FOUNDER_NAME}}"
created_at: 2026-06-09
last_verified: 2026-06-09
source_of_truth:
  - obsidian
  - github
  - "{{CLOUD_PROVIDER}}"
confidence: high
layer: operation
links:
  - "[[01-Company/Vault Constitution]]"
  - "[[91-Agent-Instructions/AGENT_START_HERE]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# Startup Operating Brain

This vault is the operating brain for {{STARTUP_NAME}}.

It keeps strategy, decisions, product work, engineering context, production status, security, metrics, fundraising, research, agent workflows, and PR evidence in one versioned workspace.

## Constitution

```text
GitHub = technical truth
{{CLOUD_PROVIDER}}/runtime = production truth
Operating Brain = context and decision truth
AI agents = helpers, not source of truth
```

## Rules

1. The brain does not replace GitHub or runtime systems.
2. Critical technical claims need evidence.
3. New unclassified input starts in `20-Inbox/`.
4. Decisions go in `15-Decisions-ADR/`.
5. AI output stays unverified until reviewed.
6. Production status requires runtime evidence.
7. Agents read context packs, not the whole vault.

## Start Here

- [[01-Company/Vault Constitution]]
- [[02-Strategy/Vision]]
- [[97-Registries/Source of Truth Map]]
- [[97-Registries/Evidence Registry]]
- [[91-Agent-Instructions/AGENT_START_HERE]]
- [[96-Context-Packs/Context Packs Index]]
- [[15-Decisions-ADR/Decision Index]]
- [[20-Inbox/Inbox Index]]
