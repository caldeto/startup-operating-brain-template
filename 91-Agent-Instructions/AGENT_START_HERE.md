---
type: agent-instruction
status: implemented-gated
area: agents
owner: librarian-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[GLOBAL_AGENT_RULES]]"
  - "[[96-Context-Packs/Context Packs Index]]"
  - "[[97-Registries/Schema Registry]]"
---

# AGENT START HERE

Lee esto antes de operar dentro del BiBound Operating Brain.

## No Leas Todo El Vault

El vault puede crecer mucho. Leer todo aumenta costo, ruido y riesgo de errores.

## Orden Obligatorio

1. Lee [[GLOBAL_AGENT_RULES]].
2. Identifica el area de la tarea.
3. Abre el context pack correspondiente en [[96-Context-Packs/Context Packs Index]].
4. Abre el indice del area.
5. Abre solo las notas objetivo.
6. Si necesitas afirmar estado real, revisa [[97-Registries/Evidence Registry]].
7. Si modificas contenido relevante, crea un Agent Run.

## Mapa Rapido

| Tarea | Context Pack |
|---|---|
| Produccion/GCP/dominio | [[96-Context-Packs/Context Pack - Production]] |
| Seguridad/RLS/IAM/SQL sandbox | [[96-Context-Packs/Context Pack - Security]] |
| Pipeline | [[96-Context-Packs/Context Pack - Pipeline]] |
| Monorepo | [[96-Context-Packs/Context Pack - Monorepo]] |
| Agentes/prompts/templates | [[96-Context-Packs/Context Pack - Agents]] |
| Estrategia/CEO/negocio | [[96-Context-Packs/Context Pack - CEO Strategy]] |
| Referencias externas | [[96-Context-Packs/Context Pack - References]] |
| Producto/PRD | [[96-Context-Packs/Context Pack - Product]] |
| Evidencia/verificacion | [[96-Context-Packs/Context Pack - Evidence]] |

## Prohibido

- declarar `production` sin evidencia;
- marcar implementado sin fuente;
- borrar contenido humano;
- crear notas duplicadas sin buscar;
- mezclar idea, decision y estado real;
- usar outputs IA como verdad verificada.

## Output Final De Todo Agente

Reporta:

- notas creadas;
- notas actualizadas;
- evidencia usada;
- contradicciones;
- riesgos;
- next actions.

