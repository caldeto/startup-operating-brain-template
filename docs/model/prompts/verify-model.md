---
type: prompt
status: implemented-gated
area: agents
owner: librarian-agent
layer: prompt
created_at: 2026-06-09
last_verified: 2026-06-09
risk: medium
confidence: high
links:
  - "[[docs/model/README]]"
---

# Verify Technical Model

Usa este prompt para que otro agente revalide el modelo tecnico.

```text
Actua como Staff Architect y auditor tecnico.

Objetivo:
Verificar si docs/model del BiBound Operating Brain sigue alineado con:
- caldeto/bibound origin/development
- caldeto/ecommerce-data-cleaning-pipeline origin/development
- GCP runtime solo cuando haya evidencia directa

Reglas:
1. No confies en checkout local; usa git ls-remote o gh api para SHAs.
2. No marques production sin evidencia GCP.
3. Compara sources.yaml con los SHAs remotos.
4. Verifica conteos de PR por dia contra gh pr list --state merged --base development.
5. Revisa contrato v3 monorepo y SCHEMA.md pipeline.
6. Revisa que cada diagrama represente un flujo real, no aspiracional.
7. Distingue implemented, implemented-gated, planned, risk y production-blocker.
8. Reporta divergencias con path, commit y motivo.
9. GitHub Actions no es gate canonico; verifica y reporta comandos locales robustos.
10. Revisa correlaciones: contrato pipeline-monorepo, schema drift, GUC/RLS, ledger, LLM roles, seguridad de agentes y produccion GCP.
11. Si propones cambios, crea Agent Run.

Entrega:
- resumen ejecutivo;
- divergencias;
- archivos a actualizar;
- riesgos;
- validaciones locales.
- correlaciones probadas.
```
