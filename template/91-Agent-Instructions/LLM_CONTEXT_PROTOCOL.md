---
type: agent-instruction
status: implemented-gated
area: agents
owner: librarian-agent
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: operation
links:
  - "[[GLOBAL_AGENT_RULES]]"
  - "[[96-Context-Packs/Context Packs Index]]"
---

# LLM Context Protocol

Use context packs to reduce token load.

## Protocol

1. Read `AGENT_START_HERE`.
2. Read global rules.
3. Read one relevant context pack.
4. Read one area index.
5. Read target notes.
6. Pull evidence only when needed.

## Stop Conditions

Stop and ask for a decision when the task requires scope expansion, architectural tradeoffs, production claims without runtime evidence, or security severity changes without proof.
