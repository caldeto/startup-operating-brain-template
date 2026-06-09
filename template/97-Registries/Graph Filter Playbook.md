---
type: registry
status: implemented-gated
area: operations
owner: librarian-agent
layer: operation
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
links:
  - "[[97-Registries/Schema Registry]]"
---

# Graph Filter Playbook

## Objetivo

Evitar que el grafo global mezcle conocimiento real con prompts, templates, bases y Canvas.

## Filtro Ejecutivo

Usar para tomar decisiones generales:

```text
-path:92-Prompts -path:93-Templates -path:94-Views -path:95-Canvas -path:91-Agent-Instructions
```

## Filtro Tecnico

```text
path:04-Engineering OR path:05-Production OR path:06-Security OR path:07-Agents-AI OR path:08-Memory-Embeddings OR path:09-Data-Pipeline OR path:10-App-Monorepo OR path:11-Cloud-Infra
```

## Filtro Negocio

```text
path:01-Company OR path:02-Strategy OR path:03-Product OR path:12-Market-Research OR path:13-Competitors OR path:14-References OR path:16-Experiments OR path:17-Metrics OR path:18-Fundraising
```

## Filtro Operacion IA

```text
path:90-Agent-Runs OR path:91-Agent-Instructions OR path:92-Prompts OR path:93-Templates OR path:96-Context-Packs
```

## Filtro Evidencia

```text
path:97-Registries OR "Evidence Registry" OR "Source of Truth Map"
```

## Regla De Grafo

El grafo global es para humanos. Los agentes deben usar context packs, no el grafo global.

