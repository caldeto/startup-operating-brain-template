---
type: vault-protocol
status: implemented-gated
area: engineering
owner: architecture-agent
layer: operation
created_at: 2026-06-09
last_verified: 2026-06-09
risk: high
confidence: high
decision_critical: true
links:
  - "[[docs/model/README]]"
  - "[[97-Registries/Evidence Registry]]"
  - "[[docs/repo-governance]]"
---

# Local Quality Gates

## Regla

No usamos GitHub Actions como senal canonica de calidad. Los cambios se validan localmente, con comandos reproducibles y evidencia registrada.

## Vault

Para cambios del Operating Brain:

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/validate_canvas_json.py
python3 scripts/check_large_files.py
python3 scripts/check_required_links.py
python3 scripts/check_no_secrets.py
```

## Monorepo BiBound

Cuando el brain afirme estado tecnico del monorepo, verificar localmente contra `development` remoto actualizado.

Checks esperados segun area:

```bash
make ci
pnpm nx run-many --target=typecheck --all --exclude=backend
cd apps/backend && uv run mypy app
```

Para agent/analytics/security, agregar los tests especificos que cubran:

- SQL sandbox;
- tenant isolation;
- GUC/RLS;
- BYOK/provider routing;
- SSE timeout;
- rate limiter;
- prompt safety y tool scopes.

## Pipeline

Cuando el brain afirme estado tecnico del pipeline, verificar localmente contra `development` remoto actualizado.

Checks esperados segun area:

```bash
make ci
uv run pytest
```

Agregar segun el cambio:

- schema contract;
- migration/schema generated drift;
- gitleaks;
- pip-audit;
- Terraform/tflint/trivy config;
- ledger consistency;
- data quality evals;
- RLS app-role tests.

## Correlaciones Obligatorias

Cuando un cambio cruza repos o cambia estado tecnico del brain, probar y documentar:

| Correlacion | Que verificar |
|---|---|
| Pipeline schema -> monorepo consumer | `SCHEMA.md` y `pipeline_schema_contract.yaml` no divergen |
| GUC/RLS | `app.current_tenant` / `app.tenant_id` siguen alineados durante la ventana |
| Ledger/outcomes | medicion pipeline y productores monorepo no contradicen ownership |
| LLM roles | roles y provider routing son config-driven y no filtran secretos |
| Seguridad agentes | tool scopes, approval gates y SQL sandbox bloquean fugas cross-tenant |
| GCP runtime | solo se marca `production` con evidencia live |

## Registro

Cada PR o Agent Run debe indicar:

- SHA de cada repo verificado;
- comandos locales ejecutados;
- resultado;
- areas/correlaciones cubiertas;
- gaps no cubiertos.

