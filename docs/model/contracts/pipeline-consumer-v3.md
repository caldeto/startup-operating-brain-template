---
type: system-component
status: implemented-gated
area: pipeline
owner: architecture-agent
layer: knowledge
created_at: 2026-06-09
last_verified: 2026-06-09
risk: high
confidence: high
decision_critical: true
links:
  - "[[docs/model/README]]"
  - "[[97-Registries/Source of Truth Map]]"
---

# Pipeline Consumer Contract V3

## Estado

El monorepo declara contrato consumidor v3 en `apps/backend/tests/fixtures/pipeline_schema_contract.yaml` y el pipeline declara `SCHEMA.md` v1.14 como superficie canonica. El contrato esta en `implemented-gated`: existe y se valida localmente, pero no es prueba de produccion.

## Boundary

| Lado | Responsabilidad |
|---|---|
| Pipeline | Produce tablas/matviews, endpoints `/ingest`, `/freshness`, ledger y data quality. |
| Monorepo | Consume contrato, emite headers, lee scoped/read surfaces, no migra tablas pipeline. |
| GCP | Ejecuta Cloud SQL, Cloud Run, BigQuery, Secret Manager e IAM. |

## Cambios V3

| Tema | Estado |
|---|---|
| GUC transition | Monorepo dual-escribe `app.tenant_id` y `app.current_tenant`; pipeline canonico es `app.current_tenant`. |
| Net CLV fields | `m_score_net` y `clv_percentile_net` son consumer-interest columns. |
| Measurement ledger | Ledger vive en BigQuery/measurement; monorepo no lo lee como tabla Cloud SQL directa. |
| Header rebrand | Monorepo emite `X-BiBound-Pipeline-Secret` y legacy durante ventana de cutover. |
| Cross-repo gate | Workflows existen, pero Actions no es senal confiable por billing/runner; usar local gates. |

## Superficie Consumida

| Objeto | Fuente | Uso |
|---|---|---|
| `orders` | pipeline Cloud SQL | conversion matching, analytics, region inference, catalog, BK-CM |
| `order_items` | pipeline Cloud SQL | SKU/category rollups, product attribution |
| `customer_features` / scoped | pipeline + monorepo scoped view | segmentation, suggestions, analytics, agent |
| `identity_clusters` | pipeline | identity joins |
| `identity_events` | pipeline | as-of membership and audit |
| `ingest_reports` | pipeline | ingest audit and report status |
| `measurement` BigQuery | pipeline | append-only outcome and data quality ledger |

## Reglas

- Las migraciones del pipeline ganan sobre docs.
- `SCHEMA.generated.sql` debe coincidir con migraciones.
- El monorepo no debe crear/alterar tablas pipeline-owned.
- Cambios breaking requieren ventana expand/contract.
- No activar FORCE RLS/cutover final si el consumidor no esta listo.

## Riesgos

| Riesgo | Severidad | Estado |
|---|---|---|
| Cutover GUC incompleto | high | residual, coordinado |
| Legacy header todavia en ventana | medium | aceptado temporalmente |
| CI remoto no ejecuta | high | mitigado por `make ci` local |
| Contrato no prueba runtime GCP | medium | requiere smoke tests |

