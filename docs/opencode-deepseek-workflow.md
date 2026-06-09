# OpenCode And DeepSeek Workflow

Use lower-cost execution models for narrow, controlled tasks. Do not use them as the final authority for critical architecture, security, or production decisions without review.

## When To Use

- DeepSeek V4 Flash: small edits, mechanical changes, simple tests.
- DeepSeek V4 Pro: larger but bounded implementation tasks.
- Codex or Claude: architecture, ambiguous debugging, security review, final review.

## Scope Control

- Provide a task packet.
- Limit files and commands.
- Require evidence and tests.
- Stop on architectural uncertainty.

## Conceptual OpenCode Agent Config

```json
{
  "agent": {
    "build-fast": {
      "model": "deepseek/deepseek-v4-flash",
      "permission": { "edit": "ask", "bash": "ask" }
    },
    "build-pro": {
      "model": "deepseek/deepseek-v4-pro",
      "permission": { "edit": "ask", "bash": "ask" }
    },
    "review-readonly": {
      "permission": { "edit": "deny", "bash": "ask" }
    }
  }
}
```
