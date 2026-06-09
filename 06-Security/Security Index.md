---
type: security-index
status: in-progress
area: security
owner: security-agent
created_at: 2026-06-08
last_verified: 2026-06-09
risk: high
confidence: high
layer: knowledge
---

# Security Index

## Modelo Principal

- [[docs/model/security/threat-model]]
- [[docs/model/security/iam-matrix]]
- [[docs/model/security/production-readiness]]
- `docs/model/diagrams/security-boundaries.mmd`

## Areas Criticas

- tenant isolation, RLS y GUC;
- SQL sandbox;
- BYOK y LLM provider routing;
- secrets e IAM;
- PII, embeddings y prompt injection;
- approval gates y tool abuse;
- observabilidad e incident response.
