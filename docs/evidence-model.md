# Evidence Model

The brain is useful only when important claims have evidence.

## Evidence For Technical Claims

Record repository, branch, commit, path, test, and verification date.

## Evidence For Production Claims

Record runtime, service, revision, deployment, health check, logs, rollback, and owner.

## Evidence For Security Claims

Record finding, severity, source, mitigation, verification command, and residual risk.

## Evidence Entry Shape

```yaml
evidence_id: repo-shortsha-path
repo: owner/repo
branch: main
commit: short_sha
path: file
claim: verifiable claim
status: implemented-gated
verified_at: YYYY-MM-DD
```
