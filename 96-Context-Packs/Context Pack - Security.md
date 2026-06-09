---
type: registry
status: implemented-gated
area: security
owner: security-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
risk: high
confidence: high
links:
  - "[[06-Security/Security Index]]"
  - "[[06-Security/Threat Model]]"
  - "[[06-Security/IAM Matrix]]"
  - "[[06-Security/Data Classification]]"
---

# Context Pack - Security

## Usar Cuando

- revisar vulnerabilidades;
- actualizar threat model;
- analizar RLS/GUC;
- analizar SQL sandbox;
- revisar prompt injection/tool abuse;
- revisar IAM/secrets.

## Leer Primero

1. [[91-Agent-Instructions/GLOBAL_AGENT_RULES]]
2. [[06-Security/Security Index]]
3. [[06-Security/Threat Model]]
4. [[06-Security/Data Classification]]
5. [[06-Security/IAM Matrix]]
6. [[97-Registries/Evidence Registry]]

## Reglas

- No bajar severidad sin evidencia.
- No declarar seguridad resuelta sin test, codigo o config.
- Distinguir riesgo teorico, bug confirmado y blocker produccion.

## Outputs Permitidos

- security-finding;
- risk;
- update threat model;
- update IAM matrix;
- Agent Run.

