---
type: evidence-index
status: implemented-ungated
area: operations
owner: architecture-agent
layer: evidence
created_at: 2026-06-08
last_verified: 2026-06-09
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Source of Truth Map]]"
  - "[[09-Pipeline/Pipeline Index]]"
  - "[[10-Monorepo/Monorepo Index]]"
---

# Evidence Registry

## Objetivo

Registrar fuentes verificables usadas para afirmar estado tecnico, produccion, seguridad o roadmap.

## Fuentes Locales Iniciales

| source_id | Tipo | Ruta / Repo | Branch esperada | Estado |
|---|---|---|---|---|
| local-brain | vault | `<local operating brain path removed>` | pendiente repo | active |
| local-project-folder | local-folder | `<local project path removed>` | n/a | active |
| monorepo-bibound | github-repo | `<local monorepo path removed>` | `origin/development` | pending-verification |
| pipeline | github-repo | `<local pipeline path removed>` | `origin/development` | pending-verification |
| conductor-workspaces | local-folder | `<local workspace path removed>` | varies | pending-verification |
| monorepo-dev-2026-06-09 | github-repo | `caldeto/bibound` | `development@0c5c08ca` | verified |
| pipeline-dev-2026-06-09 | github-repo | `caldeto/ecommerce-data-cleaning-pipeline` | `development@d1b74e5` | verified |

## Evidencia Requerida Para Marcar `implemented-gated`

- archivo o test;
- rama;
- commit o fecha;
- resultado de verificacion;
- agente/humano que verifico;
- link a nota destino.

## Evidencia Requerida Para Marcar `production`

- entorno GCP verificado;
- servicio o dominio;
- revision/deploy;
- secrets/IAM verificados;
- smoke test o health check;
- rollback conocido.

## Registro De Verificaciones

| Fecha | Fuente | Area | Verificado por | Resultado | Nota |
|---|---|---|---|---|---|
| 2026-06-08 | local-brain | scaffold | codex | vault creado y canvas JSON validos | [[90-Agent-Runs/2026-06-08-codex-scaffold-10-10-upgrade]] |
| 2026-06-09 | monorepo-dev-2026-06-09 | monorepo | codex | `development` remoto verificado en `0c5c08ca`; PRs #1-#38 revisados por fecha de merge UTC; fuente en `docs/model/sources.yaml` | [[docs/model/README]] |
| 2026-06-09 | pipeline-dev-2026-06-09 | pipeline | codex | `development` remoto verificado en `d1b74e5`; PRs #1-#65 revisados por fecha de merge UTC; fuente en `docs/model/sources.yaml` | [[docs/model/README]] |
| 2026-06-09 | local-brain | technical-model | codex | creado `docs/model/` con historia diaria, arquitectura, contrato, seguridad, DBML y diagramas | [[docs/model/README]] |

## Snapshots Tecnicos

| snapshot_id | Fecha | Fuente | Commit | Cobertura | Nota |
|---|---|---|---|---|---|
| brain-model-2026-06-04 | 2026-06-04 | pipeline | `34754a89`-`c71b7193` | PR #1-#5 foundation, secrets, GCS, medicion, Terraform | [[docs/model/history/2026-06-04]] |
| brain-model-2026-06-05 | 2026-06-05 | pipeline | `f1ee84ff`-`0f6d34ca` | PR #6-#15 Cloud SQL, Cloud Run, ingest, CI, DB segura | [[docs/model/history/2026-06-05]] |
| brain-model-2026-06-06 | 2026-06-06 | pipeline | `64c9ee58`-`2aff7c0b` | PR #16-#19 CLV neto, CLP, qcut, roadmap | [[docs/model/history/2026-06-06]] |
| brain-model-2026-06-07 | 2026-06-07 | pipeline + monorepo | `2e72d68e`-`8ca6072f`, `412d6a89`-`a47a76ee` | hardening pipeline, WIF/IAM, truth/rebrand monorepo | [[docs/model/history/2026-06-07]] |
| brain-model-2026-06-08 | 2026-06-08 | pipeline + monorepo | `89e2d36e`-`d1b74e5`, `096afef6`-`e6e768f5` | ledger, data quality, LLM core, contract v3 | [[docs/model/history/2026-06-08]] |
| brain-model-2026-06-09 | 2026-06-09 | monorepo | `8b23af6e`-`0c5c08ca` | CI unblock, ADC, SQL sandbox, SSE, BYOK, rate limiter | [[docs/model/history/2026-06-09]] |
