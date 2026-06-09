# Conductor Builder Workflow

Use Conductor as a planning and control tower for parallel local agents.

Recommended roles:

- Conductor: workspace orchestration and review surface.
- Codex: architecture, planning, implementation, and review.
- Claude: second opinion, debugging, and review.
- DeepSeek/OpenCode: controlled execution for narrow task packets.

## Codex Planner Prompt

```text
Act as CTO Planner. Do not edit files.

Goal:
...

Deliver:
1. current-state diagnosis;
2. relevant files;
3. risks;
4. small PR plan;
5. exact tests;
6. acceptance criteria;
7. TASK_PACKET for builder;
8. final review checklist.
```

## Builder Handoff Prompt

```text
You are a builder, not an architect.
Execute only this TASK_PACKET.
Do not expand scope.
Stop if you need architectural decisions.
```

Record important Conductor runs in `90-Agent-Runs/`.
