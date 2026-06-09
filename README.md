# Startup Operating Brain Template

An open-source Obsidian + GitHub operating system for solo founders and small AI-native startup teams.

It helps founders maintain one living workspace for CEO strategy, CTO decisions, product planning, engineering execution, security, fundraising, metrics, market research, and AI-agent workflows.

The template is designed for teams using tools like Codex, Claude Code, Conductor, OpenCode, GitHub, and local test gates. It prevents context loss by separating ideas, decisions, evidence, production truth, and AI-generated outputs.

## Who It Is For

- Solo founders who need a versioned CEO/CTO operating brain.
- Small AI-native teams that use coding agents heavily.
- OSS maintainers who want repeatable evidence and review workflows.
- Teams that need Obsidian for thinking and GitHub for review history.

## What It Includes

- CEO, CTO, product, engineering, production, security, fundraising, metric, and research areas.
- Agent instructions, prompts, task packets, context packs, and run logs.
- Evidence registry and source-of-truth model.
- Obsidian Canvas maps and reusable note templates.
- Local validators for frontmatter, Canvas JSON, links, secrets, and large files.
- Public docs for founder workflows, Conductor, OpenCode, GitHub, and local gates.

## Quickstart

```bash
git clone https://github.com/caldeto/startup-operating-brain-template.git my-startup-brain
cd my-startup-brain
python3 scripts/bootstrap.py --startup "Acme AI" --founder "Jane Doe" --primary-repo "acme/app" --data-repo "acme/data-pipeline" --cloud "GCP"
python3 scripts/validate_frontmatter.py
```

Open the generated `startup-brain-vault/` folder as an Obsidian vault.

## Core Model

```text
GitHub = technical truth
Cloud/runtime = production truth
Operating Brain = context and decision truth
AI agents = helpers, not source of truth
```

AI output is never verified truth by default. Technical or production claims need evidence from repositories, tests, runtime systems, or reviewed decisions.

## Main Paths

- `template/`: reusable Obsidian vault template.
- `docs/`: installation and workflow documentation.
- `examples/bibound/`: sanitized curated examples from the original BiBound operating brain.
- `scripts/`: bootstrap and validation scripts.
- `.github/`: issue templates, PR template, and optional validation workflow.

## Local Gates

```bash
python3 scripts/validate_frontmatter.py
python3 scripts/validate_canvas_json.py
python3 scripts/check_required_links.py
python3 scripts/check_no_secrets.py
python3 scripts/check_large_files.py
```

GitHub Actions are optional. Local gates are the primary quality contract.

## Documentation

Start with:

- [Installation](docs/installation.md)
- [Quickstart](docs/quickstart.md)
- [Founder Workflow](docs/founder-workflow.md)
- [Agent Workflow](docs/agent-workflow.md)
- [Security Model](docs/security-model.md)

## Project Status

This repository is a template conversion of a real operating brain. The `template/` directory is generic. The BiBound material is retained only as sanitized examples.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep changes small, run local validators, and avoid adding startup-specific secrets or private paths.
