# Release Workflow

1. Keep PRs small.
2. Run all local gates.
3. Confirm `template/` has no startup-specific identity leaks.
4. Confirm examples are sanitized.
5. Update `CHANGELOG.md`.
6. Merge to `main` after review.
7. Tag releases when template behavior or public docs materially change.

Optional GitHub Actions can run the same validators, but local evidence remains required in the PR body.
