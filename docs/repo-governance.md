---
type: vault-protocol
status: implemented-gated
area: operations
owner: librarian-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
decision_critical: true
links:
  - "[[91-Agent-Instructions/AGENT_RUN_PROTOCOL]]"
  - "[[97-Registries/Evidence Registry]]"
  - "[[97-Registries/Source of Truth Map]]"
  - "[[97-Registries/Schema Registry]]"
---

# Repo Governance

## Objetivo

Este repositorio versiona el vault Obsidian `BiBound Operating Brain`.

GitHub mantiene historial, revision, PRs y CI. Obsidian mantiene escritura humana, navegacion visual, Canvas y grafo. El monorepo BiBound y el pipeline siguen siendo fuentes de verdad tecnica ejecutable; este vault registra contexto, decisiones, evidencia, estrategia, negocio, seguridad, produccion y referencias.

## Branches

- `main`: conocimiento aceptado, estable y revisado.
- `development`: trabajo normal antes de promover a `main`.
- `agent/*`: ramas creadas por Codex, Claude, Conductor u otros agentes.

Los cambios normales deben entrar por PR. Evitar commits directos a `main` salvo bootstrap, reparaciones urgentes o mantenimiento administrativo explicito.

## Como Nutrir El Vault

1. Capturar informacion nueva en `20-Inbox/` cuando todavia no esta clasificada.
2. Promover contenido a su area cuando tenga tipo, estado, owner, layer y confianza claros.
3. Registrar decisiones en `15-Decisions-ADR/`.
4. Registrar evidencia y fuentes en `97-Registries/Evidence Registry` y `97-Registries/Source of Truth Map`.
5. Mantener produccion y seguridad conectadas a evidencia verificable.

## Trabajo De Agentes

Los agentes deben leer primero `91-Agent-Instructions/AGENT_START_HERE`, `91-Agent-Instructions/GLOBAL_AGENT_RULES` y el protocolo especifico del area. Deben trabajar en ramas `agent/*` cuando preparan cambios para revision.

Los agentes no deben:

- borrar contenido humano sin permiso explicito;
- marcar `status: production` sin `evidence` o `source_of_truth`;
- presentar output IA como verdad verificada;
- duplicar conceptos ya existentes en registries, protocolos o context packs;
- conectar automatizaciones agresivas contra monorepo o pipeline sin una decision aprobada.

## Cuando Crear Agent Run

Crear un Agent Run en `90-Agent-Runs/` cuando un agente haga cambios estructurales, actualice decisiones, importe evidencia, cambie reglas, toque produccion/seguridad o ejecute una revision periodica. El Agent Run debe resumir objetivo, archivos creados o actualizados, verificaciones, riesgos y siguientes acciones.

## Conexion Con Monorepo Y Pipeline

La conexion inicial con monorepo y pipeline es documental, no automatica.

- `Evidence Registry`: apunta a commits, PRs, resultados, documentos y fuentes.
- `Source of Truth Map`: declara donde vive la verdad tecnica o runtime.
- `Agent Runs`: dejan bitacora de cambios hechos por agentes.
- PRs: revisan y promueven conocimiento del vault.

No usar submodulos ni sync automatico agresivo hasta que exista una decision revisada.

## GitHub Vs Obsidian

GitHub contiene:

- historial;
- ramas;
- PRs;
- revision;
- CI;
- protecciones.

Obsidian contiene:

- escritura humana;
- navegacion visual;
- Canvas;
- grafo;
- lectura y edicion diaria.

Los archivos de workspace visual de Obsidian no son parte del contrato de conocimiento estable.

## Revision De PRs

Cada PR debe explicar tipo de cambio, areas tocadas, impacto en produccion/seguridad/decisiones, evidencia usada y si corresponde Agent Run.

Antes de mergear:

1. Revisar que la evidencia soporte afirmaciones criticas.
2. Revisar que las notas nuevas sigan `97-Registries/Schema Registry`.
3. Confirmar que Canvas JSON sigue valido.
4. Confirmar que no hay secretos ni archivos enormes.
5. Confirmar que el CI `Validate Vault` pasa.
