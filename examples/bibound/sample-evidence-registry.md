---
type: evidence-index
status: implemented-gated
area: examples
owner: maintainer
created_at: 2026-06-09
last_verified: 2026-06-09
confidence: high
layer: evidence
---

# Sample Evidence Registry

| source_id | Type | Location | Status | Notes |
|---|---|---|---|---|
| bibound-app-dev | github-repo | `caldeto/bibound@0c5c08ca` | verified | App repository snapshot used for technical model review. |
| bibound-pipeline-dev | github-repo | `caldeto/ecommerce-data-cleaning-pipeline@d1b74e5` | verified | Pipeline snapshot used for contract and data-quality review. |
| runtime | cloud-runtime | GCP runtime | pending | Production was not marked verified without runtime evidence. |

## Pattern Demonstrated

Technical implementation claims point to repository commits. Production claims remain pending until runtime evidence exists.
