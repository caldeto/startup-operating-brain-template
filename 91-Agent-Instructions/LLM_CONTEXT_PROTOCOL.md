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
  - "[[AGENT_START_HERE]]"
  - "[[96-Context-Packs/Context Packs Index]]"
  - "[[97-Registries/Evidence Registry]]"
layer: operation
---

# LLM Context Protocol

## Objetivo

Evitar que Codex, Claude o cualquier agente consuman demasiado contexto, mezclen capas o actualicen el vault con informacion no verificada.

## Regla Principal

```text
El agente debe leer lo minimo suficiente para ejecutar bien.
```

## Context Budget

| Tipo De Tarea | Archivos maximos recomendados antes de actuar |
|---|---:|
| Capturar referencia | 3-5 |
| Crear idea/hipotesis | 4-6 |
| Actualizar nota existente | 4-8 |
| Auditar area tecnica | 8-15 |
| PRD grande | 10-20 |
| Revision mensual CTO | 15-25 |

## Orden De Lectura

1. [[AGENT_START_HERE]]
2. [[GLOBAL_AGENT_RULES]]
3. Context Pack del area.
4. Indice del area.
5. Nota objetivo.
6. Evidence Registry si hay claims tecnicos.
7. Repos/GCP solo si la tarea requiere verificacion.

## Cuando Abrir Mas Contexto

Abrir mas notas solo si:

- hay contradiccion;
- falta evidencia;
- el usuario pide comparacion;
- una decision afecta varias areas;
- la nota objetivo linkea una dependencia critica.

## Prohibido

- leer todo el vault por comodidad;
- usar el grafo global como fuente para afirmar estado;
- mezclar templates/prompts con conocimiento real;
- presentar output IA como evidencia.

## Output Esperado

Todo agente debe cerrar con:

- que leyo;
- que cambio;
- que no pudo verificar;
- que recomienda hacer despues.
