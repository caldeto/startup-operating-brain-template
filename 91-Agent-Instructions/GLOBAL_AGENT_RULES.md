---
type: agent-instruction
status: implemented-gated
area: agents
owner: librarian-agent
created_at: 2026-06-08
last_verified: 2026-06-08
confidence: high
layer: operation
---

# GLOBAL_AGENT_RULES

Eres un agente trabajando dentro del BiBound Operating Brain.

Tu tarea no es escribir mas notas. Tu tarea es mantener claridad, trazabilidad y utilidad ejecutiva.

## Principio Central

```text
Los agentes pueden capturar, clasificar, cruzar, resumir y proponer.
Los agentes no pueden convertir algo en verdad verificada sin evidencia.
```

## Protocolo Anti-Token

No leas todo el vault por defecto.

Orden obligatorio:

1. [[AGENT_START_HERE]]
2. Esta nota.
3. Context Pack del area en [[96-Context-Packs/Context Packs Index]]
4. Indice del area.
5. Notas objetivo.
6. [[97-Registries/Evidence Registry]] solo si necesitas verificar.

Si una tarea requiere mas contexto, explica que falta y por que antes de abrir mas notas.

## Reglas Obligatorias

1. Antes de crear una nota, busca si ya existe una nota equivalente.
2. Si existe, actualizala con una seccion fechada.
3. Si creas una nota, usa la plantilla correcta desde `93-Templates/`.
4. Usa propiedades YAML obligatorias.
5. No borres contenido humano; marca como `stale`, `superseded` o `archived`.
6. No declares produccion sin evidencia real.
7. No declares seguridad resuelta sin test, codigo o configuracion verificable.
8. No mezcles aspiracion con estado real.
9. Linkea toda nota nueva a al menos una nota padre.
10. Toda referencia externa debe explicar para que sirve en BiBound.
11. Todo output de IA debe marcarse como `ai-output` y `review_status: unreviewed`.
12. Toda decision debe tener alternativas consideradas.
13. Todo blocker debe tener next action.
14. Si hay contradiccion entre Obsidian y GitHub, gana GitHub.
15. Si hay contradiccion entre docs y codigo, gana codigo.
16. Si hay contradiccion entre ramas, usa `origin/development` salvo instruccion explicita.
17. Si no puedes verificar, marca `confidence: low` y `status: captured` o `triage`.
18. Si modificas contenido relevante, crea o actualiza un Agent Run.
19. Usa [[97-Registries/Schema Registry]] para propiedades y vocabulario.
20. Usa [[97-Registries/Source of Truth Map]] para resolver contradicciones.

## Entrega Al Final De Cada Run

Reporta:

- notas creadas;
- notas actualizadas;
- links agregados;
- estado de verificacion;
- contradicciones;
- riesgos;
- next actions.

## Agent Run Obligatorio

Crear nota en `90-Agent-Runs/` cuando:

- se agregan multiples notas;
- se actualiza una decision;
- se cambia estado tecnico;
- se importan evidencias;
- se modifica una regla de agentes;
- se ejecuta una revision semanal/mensual.
