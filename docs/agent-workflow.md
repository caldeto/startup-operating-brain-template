# Agent Workflow

Agents do not read the whole vault by default.

Required reading order:

1. `91-Agent-Instructions/AGENT_START_HERE.md`
2. `91-Agent-Instructions/GLOBAL_AGENT_RULES.md`
3. Relevant context pack in `96-Context-Packs/`
4. Area index
5. Target notes
6. `97-Registries/Evidence Registry.md` only if evidence is needed

## Roles

- CTO Planner: architecture, task packets, risk, acceptance criteria.
- CEO Strategy Agent: positioning, market, narrative, fundraising.
- Product Agent: PRDs, roadmap, customer insights.
- Security Agent: threat model, prompt injection, tool abuse, data handling.
- Production Agent: runtime status, rollback, smoke tests, readiness.
- Research Agent: market and competitor synthesis.
- Librarian Agent: dedupe, schema, links, stale notes.
- Builder Agent: scoped implementation from a task packet.
- Reviewer Agent: review evidence, tests, risk, and scope control.

## Rule

AI output is `unreviewed` until a human or verification step records evidence.
