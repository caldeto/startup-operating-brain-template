---
type: agent-run
status: implemented-gated
area: operations
owner: codex
layer: operation
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
risk: medium
decision_critical: true
links:
  - "[[docs/model/testing/local-quality-gates]]"
  - "[[docs/repo-governance]]"
  - "[[91-Agent-Instructions/AGENT_RUN_PROTOCOL]]"
---

# 2026-06-09 Codex Local Quality Gates Policy

## Objetivo

Persistir la regla operativa: GitHub Actions no es gate canonico de calidad. Las validaciones reales son locales, robustas y deben cubrir frentes y correlaciones entre vault, monorepo, pipeline, seguridad y runtime modelado.

## Archivos Creados

- `docs/model/testing/local-quality-gates.md`
- `90-Agent-Runs/2026-06-09-codex-local-quality-gates-policy.md`

## Archivos Actualizados

- `.github/workflows/validate-vault.yml`
- `.github/pull_request_template.md`
- `docs/repo-governance.md`
- `docs/model/README.md`
- `docs/model/sources.yaml`
- `docs/model/prompts/verify-model.md`
- `docs/model/security/production-readiness.md`

## Decision

El workflow remoto queda solo como `workflow_dispatch` manual. Los PRs y Agent Runs deben registrar comandos locales ejecutados, SHAs verificados y correlaciones cubiertas.

## Verificaciones

- Validadores locales del vault.
- Revision de scope para no incluir cambios visuales de Obsidian.

## Riesgos

- Si alguien mira solo GitHub checks, puede interpretar erroneamente que no hay gate. La fuente correcta es `docs/model/testing/local-quality-gates.md`.
