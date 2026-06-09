# Security Policy

## Reporting Security Issues

Open a private report with the maintainers if the issue could expose secrets, private startup data, credentials, or unsafe agent behavior. For normal template hygiene issues, open a GitHub issue.

## Public Repo Hygiene

Do not commit:

- API keys, credentials, tokens, private keys, or session material.
- Personal local paths or machine-specific secrets.
- Customer data, private deal data, or internal vendor data.
- Unreviewed AI outputs that claim verified production or security status.

## Template Security Model

The template assumes:

- GitHub is technical truth.
- Cloud/runtime systems are production truth.
- The operating brain is context and decision truth.
- AI agents help, but do not become a source of truth.

Run `python3 scripts/check_no_secrets.py` before publishing changes.
