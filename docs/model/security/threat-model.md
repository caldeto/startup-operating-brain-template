---
type: security-model
status: in-progress
area: security
owner: security-agent
layer: knowledge
created_at: 2026-06-09
last_verified: 2026-06-09
risk: high
confidence: high
decision_critical: true
links:
  - "[[06-Security/Threat Model]]"
  - "[[docs/model/README]]"
---

# Threat Model

## System Boundaries

| Boundary | Assets | Primary risk |
|---|---|---|
| User/browser to frontend | sessions, tenant context | auth bypass, tenant confusion |
| Frontend to backend | Bearer tokens, API payloads | broken authorization |
| Backend/agent/analytics to Cloud SQL | tenant data, PII, warehouse | cross-tenant read/write |
| Monorepo to pipeline HTTP | uploads, ingest reports | contract drift, SSRF, replay |
| Pipeline to GCS/Cloud SQL/BigQuery | raw artifacts, ledger | PII retention, bad measurement |
| LLM providers/Vertex | prompts, context, tool outputs | PII leakage, prompt injection |
| GitHub to GCP | deploy credentials | WIF/IAM overreach |

## Findings Table

| Topic | Current state | Severity | Required next step |
|---|---|---:|---|
| Tenant isolation | Pipeline has RLS runtime and `pipeline_app`; monorepo dual-writes GUCs | high | Finish cutover to `app.current_tenant` and test current-tenant-only path |
| SQL sandbox | Monorepo added tenant isolation suite and validator coverage | high | Keep tests blocking in local CI and later remote CI |
| BYOK | PR #37 prevents tenant key from falling to platform endpoint | high | Add ongoing review for per-tenant LLM routing |
| Rate limiting | PR #38 bounds fallback memory, uses Redis sliding window and rebuilds singleton on URL change | medium | Ensure Redis is configured in production; orchestrator RPM remains follow-up |
| SSRF | Pipeline blocks unsafe callback URLs | high | Keep callback contract documented and tested |
| Secrets | Secret Manager target; no repo secrets | high | Verify live Cloud Run env and secret bindings |
| IAM | WIF/deployer/service accounts exist in Terraform | high | Verify live IAM least privilege before production |
| PII to LLM | Pipeline policy says no PII to LLM; Vertex target | high | Audit prompts/tool outputs before production |
| Prompt injection | Prompt safety libs and tool scope gates exist | medium | Create adversarial evals for agent tools |
| Agent tool abuse | Copilot/agent tools have scopes and gates | high | Enforce approval gates for mutating actions |
| Supply chain | Local gates include audits in pipeline; monorepo uses local CI | medium | Enable remote scans when billing allows |
| Observability | Not production-ready | high | Add logs/metrics/alerts/runbooks |
| Incident response | Not formalized | medium | Create incident runbook and owner matrix |

## Do Not Mark Production Until

- GCP service URLs, service accounts, secrets and deploy revisions are verified.
- Smoke tests pass against target environment.
- Rollback path is documented.
- Backups and restore test are verified.
- Tenant isolation is tested in the deployed runtime.
