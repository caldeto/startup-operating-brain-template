# Security Model

## Rules

- Do not store secrets in the brain.
- AI output is unverified until reviewed.
- Production status requires runtime evidence.
- Security status requires code, config, tests, or runtime evidence.
- Prompt injection and tool abuse are first-class risks.
- Public repos require private-path and sensitive-data hygiene.

## Topics To Track

- Threat model.
- Data classification.
- Tenant isolation.
- Secrets handling.
- Prompt injection.
- Tool permissions.
- Runtime IAM.
- Evidence registry.

Run `python3 scripts/check_no_secrets.py` before publishing.
