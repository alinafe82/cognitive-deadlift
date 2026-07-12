# Simple Example

Input:

```text
Go god mode and clean this repo.
```

Expected output shape:

```md
Goal: Clean the repo without adding unsupported claims or broad rewrites.
Risk: Medium, because repo cleanup can change docs, validation, and behavior.
Available skills checked: problem-framing, trace-the-code, complexity-budget, docs-claim-audit, diff-interrogation, explain-without-ai.
Skill sequence: problem-framing -> trace-the-code -> docs-claim-audit -> complexity-budget -> diff-interrogation -> explain-without-ai.
Skipped skills: failing-test-first, because no specific bug has been reported yet.
Evidence needed: repo contract docs, current status, relevant files, validation commands.
Actions: inspect before editing, remove unsupported claims, keep changes small.
Checks: run the configured repo gate.
Limits: no claim that every possible cleanup path was covered.
```
