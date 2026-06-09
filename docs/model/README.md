---
type: architecture-model
status: implemented-gated
area: engineering
owner: architecture-agent
layer: knowledge
created_at: 2026-06-09
last_verified: 2026-06-09
risk: high
confidence: high
decision_critical: true
links:
  - "[[97-Registries/Source of Truth Map]]"
  - "[[97-Registries/Evidence Registry]]"
  - "[[09-Pipeline/Pipeline Index]]"
  - "[[10-Monorepo/Monorepo Index]]"
---

# BiBound Technical Model

Este directorio es el modelo tecnico principal del Operating Brain. No reemplaza a los repos; resume lo verificado desde `development`, con evidencia por commit, PR, archivo y fecha.

## Estado Ejecutivo

| Area | Estado | Lectura honesta |
|---|---|---|
| Pipeline | implemented-gated | Fases 0-8 completas en `caldeto/ecommerce-data-cleaning-pipeline@d1b74e5`; fuerte en seguridad, ledger, data quality y contrato. |
| Monorepo | implemented-ungated | `caldeto/bibound@0c5c08ca` tiene LLM core, contrato v3, SQL sandbox tests, BYOK safety y rate limiter hardening; aun faltan bordes de produccion. |
| GCP/infra | implemented-gated | Hay Terraform/WIF/Cloud Run/Cloud SQL/BigQuery/Secret Manager modelados; no se marca `production` sin verificacion runtime. |
| Seguridad | in-progress | Mejoro mucho: RLS/GUC, BYOK, SSRF, SQL sandbox, IAM. Pendientes: cutover GUC, observabilidad, dominio, backups, rollback. |
| Operating Brain | in-progress | Antes habia placeholders; este modelo agrega historia, arquitectura, contratos, DBML, amenazas y evidencias. |

## Como Leer

1. `sources.yaml` - snapshot deterministico de fuentes y SHAs.
2. `ownership.yaml` - que manda pipeline, monorepo, GCP y brain.
3. `history/` - avance diario con tabla PR/commit/evidencia.
4. `diagrams/` - vista visual versionable.
5. `contracts/pipeline-consumer-v3.md` - contrato real pipeline-monorepo.
6. `security/` - threat model, IAM y readiness.
7. `testing/local-quality-gates.md` - regla canonica de pruebas locales.
8. `db/` - modelo conceptual Cloud SQL y contrato pipeline.

## Reglas De Verdad

| Pregunta | Fuente que manda |
|---|---|
| Que schema produce el pipeline | `db/migrations/*.sql` y `SCHEMA.md` del pipeline |
| Que consume el monorepo | `apps/backend/tests/fixtures/pipeline_schema_contract.yaml` del monorepo |
| Que corre en desarrollo | `origin/development` remoto de cada repo |
| Que esta en produccion | GCP runtime, deploys, logs, smoke tests |
| Que decision esta aceptada | ADRs y PRs mergeados |
| Que sabe el brain | Esta documentacion mas Evidence Registry |
| Que valida calidad | Gates locales robustos y documentados, no GitHub Actions |

## Hallazgos Principales

- El pipeline va adelante del monorepo: ya cerro Fases 0-8, ledger BigQuery y data quality IA.
- El monorepo cerro riesgos importantes el 2026-06-09 UTC: CI local, ADC wrap, SQL sandbox tests, SSE timeout, BYOK endpoint safety y rate limiter hardening.
- La integracion cross-repo esta cerca pero no terminada: contrato v3 existe, gate existe, falta operar el cutover final de GUC y consumos netos.
- GCP esta modelado y parcialmente materializado, pero produccion end-to-end aun requiere dominio, observabilidad, alerts, backups, rollback y smoke tests.
- GitHub Actions no se usa como gate de calidad; los cambios deben probarse localmente en todos los frentes relevantes y registrar correlaciones.
