---
type: prd
status: in-progress
area: operations
owner: ceo
layer: knowledge
created_at: 2026-06-08
last_reviewed: 2026-06-08
risk: medium
confidence: high
decision_critical: true
links:
  - "[[00-Home/BiBound Operating Brain]]"
  - "[[00-Home/Execution Plan]]"
  - "[[97-Registries/Schema Registry]]"
  - "[[96-Context-Packs/Context Packs Index]]"
---

# PRD - Operating Brain 10/10 Execution

## Resumen Ejecutivo

Llevar el BiBound Operating Brain a 10/10 en dos dimensiones:

```text
Scaffold 10/10 = estructura, reglas, filtros, plantillas, navegacion y mantenibilidad impecables.
Cerebro operativo 10/10 = contenido real, verificado, vivo, util para decidir y conectado con evidencia.
```

Este proyecto debe ejecutarse sin romper lo actual. Se agregan capas de control, no se reescribe el vault.

## Contexto

El vault inicial ya tiene Home, carpetas, notas base, prompts, templates y Canvas. En la vista grafica se ve una arquitectura sana, pero tambien aparece ruido operativo: templates, prompts, bases y Canvas compiten visualmente con conocimiento real.

Ademas, el brain todavia no contiene suficiente evidencia viva desde:

- monorepo BiBound;
- pipeline;
- PRDs pendientes;
- GCP/produccion;
- seguridad;
- roadmap;
- negocio/CEO;
- referencias externas.

## Objetivo

Convertir el vault en un repositorio GitHub independiente que se abre visualmente en Obsidian y sirve como cerebro de decision para BiBound.

El sistema debe responder en menos de 5 minutos:

```text
que esta hecho,
que esta en development,
que esta pendiente,
que bloquea produccion,
que decision sigue,
que evidencia existe,
que agente lo verifico,
y que accion toca ahora.
```

## Decisiones De Arquitectura

### Repo Independiente

El vault vivira como repo GitHub independiente.

```text
bibound-operating-brain = conocimiento, decisiones, contexto, evidencia, Canvas
caldeto/bibound = verdad tecnica del producto/monorepo
ecommerce-data-cleaning-pipeline = verdad tecnica del pipeline
GCP = verdad runtime/produccion
```

No se usaran submodulos al inicio. La conexion se hara con registries, links, evidence notes y snapshots verificados.

### Branching

Modelo recomendado:

```text
main = conocimiento aceptado
development = cambios preparados
agent/* = ramas de agentes
```

Los agentes pueden proponer cambios en ramas. Los cambios grandes deben quedar en PR.

## Alcance

### Fase 1 - Scaffold 10/10

Agregar:

- Schema Registry;
- Source of Truth Map;
- Evidence Registry;
- Agent Start Here;
- Context Packs;
- indices faltantes;
- Graph Filter Playbook;
- Changelog;
- protocolo anti-token;
- protocolo de Agent Runs.

### Fase 2 - Cerebro Tecnico 10/10

Importar y verificar:

- pipeline `origin/development`;
- monorepo `origin/development`;
- PRDs pendientes;
- production readiness;
- seguridad;
- roadmap.

### Fase 3 - Cerebro CEO/Negocio 10/10

Completar:

- Vision;
- ICP;
- Wedge;
- Positioning;
- Pricing;
- GTM;
- Competitive Narrative;
- Fundraising Story;
- North Star;
- Business Hypotheses;
- Experiments;
- References.

### Fase 4 - Gobernanza

Activar:

- weekly review;
- monthly CTO review;
- stale notes;
- dedupe;
- agent ops;
- repo PR workflow.

## Requisitos Funcionales

### RF1 - Taxonomia Cerrada

Cada nota nueva debe usar propiedades normalizadas:

```yaml
type: TBD
status: TBD
area: TBD
owner: TBD
layer: knowledge | operation | template | prompt | canvas | evidence | archive
risk: low | medium | high | critical
confidence: low | medium | high
last_verified: YYYY-MM-DD
decision_critical: true | false
```

### RF2 - Context Packs Anti-Token

Ningun agente debe leer todo el vault por defecto.

Orden de lectura obligatorio:

```text
1. 91-Agent-Instructions/AGENT_START_HERE.md
2. 91-Agent-Instructions/GLOBAL_AGENT_RULES.md
3. 96-Context-Packs/<area>.md
4. indice del area
5. notas objetivo
6. 97-Registries/Evidence Registry.md si necesita verificar
```

### RF3 - Evidencia

Toda afirmacion tecnica critica debe tener:

- repo;
- branch;
- path;
- commit o fecha;
- metodo de verificacion;
- confidence.

### RF4 - Grafos Filtrables

El vault debe soportar vistas:

- Executive Graph;
- Technical Graph;
- Business Graph;
- Agent Ops Graph;
- Evidence Graph.

### RF5 - Agent Runs

Todo cambio relevante hecho por IA debe dejar nota en `90-Agent-Runs/`.

## No Objetivos

- No convertir Obsidian en fuente unica de verdad tecnica.
- No borrar ni renombrar masivamente notas existentes.
- No importar todo BuyerKind/BiBound sin triage.
- No usar submodulos en esta fase.
- No marcar nada como produccion sin evidencia GCP/GitHub.

## Riesgos

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| Vault lleno de ruido IA | Alto | ai-output + review_status |
| Agentes leen demasiado | Alto | Context Packs |
| Docs stale | Alto | last_verified + weekly review |
| Grafo ilegible | Medio | layer + filtros |
| Confundir Obsidian con verdad tecnica | Critico | Source of Truth Map |
| PRDs pendientes mezcladas con implementado | Alto | status + Evidence Registry |

## Definition Of Done - Fase 1

- Existe Schema Registry.
- Existe Source of Truth Map.
- Existe Evidence Registry.
- Existen Context Packs por dominio.
- Existen indices de Agents, Prompts, Templates, Canvas y Registries.
- Existe Agent Start Here.
- Existe Graph Filter Playbook.
- Existe Changelog.
- GLOBAL_AGENT_RULES incluye protocolo anti-token.
- Home enlaza la nueva capa.
- No se borro ni rompio contenido existente.

## Definition Of Done - Fase 2

- Pipeline tiene nota verificada desde `origin/development`.
- Monorepo tiene nota verificada desde `origin/development`.
- PRDs pendientes se separan de implementado.
- Production Readiness tiene blockers accionables.
- Security tiene riesgos con severidad/evidencia.
- Roadmap muestra fase real.

## Criterio De Exito Final

El vault es 10/10 cuando un humano o agente puede entender, decidir y ejecutar sin perderse:

- donde mirar;
- que esta verificado;
- que esta pendiente;
- que fuente manda;
- que accion sigue.

