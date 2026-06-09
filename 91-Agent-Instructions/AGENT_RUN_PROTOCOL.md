---
type: vault-protocol
status: implemented-gated
area: agents
owner: librarian-agent
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[90-Agent-Runs/Agent Runs Index]]"
  - "[[93-Templates/template-agent-run]]"
layer: operation
---

# AGENT RUN PROTOCOL

## Objetivo

Registrar cambios relevantes hechos por agentes para que el vault sea auditable.

## Cuando Crear Agent Run

Crear nota en `90-Agent-Runs/` cuando:

- se crean varias notas;
- se actualiza una decision;
- se cambia una regla;
- se importa evidencia;
- se actualiza produccion/seguridad;
- se ejecuta weekly/monthly review;
- se hace un upgrade estructural del vault.

## Nombre

```text
YYYY-MM-DD-agent-scope.md
```

Ejemplo:

```text
2026-06-08-codex-scaffold-10-10-upgrade.md
```

## Contenido Minimo

- agente;
- objetivo;
- archivos creados;
- archivos actualizados;
- verificaciones;
- riesgos;
- next actions.

## Regla

Agent Run no reemplaza commit ni PR. Es bitacora operativa dentro del brain.

