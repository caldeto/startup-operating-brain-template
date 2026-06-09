---
type: decision
status: accepted
area: operations
owner: "{{FOUNDER_NAME}}"
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: knowledge
decision_critical: true
links:
  - "[[00-Home/Startup Operating Brain]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# ADR-0001 Use Obsidian As Startup Operating Brain

## Decision

Use an Obsidian vault versioned in GitHub as the operating brain for {{STARTUP_NAME}}.

## Context

Small teams lose context across chats, PRs, documents, meetings, and agent runs. The brain keeps decisions, evidence, and operating context together without replacing source repositories or runtime systems.

## Alternatives Considered

- GitHub-only docs: strong review, weaker daily navigation.
- Chat-only memory: fast capture, weak evidence and durability.
- Project-management-only workspace: useful tasks, weak architecture and evidence model.

## Consequences

- Notes require frontmatter and links.
- Agents must use context packs.
- Important technical and production claims require evidence.
