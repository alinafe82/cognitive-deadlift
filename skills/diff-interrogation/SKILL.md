---
name: diff-interrogation
description: "Review a code diff for behavioral regressions, missing evidence, and security or data risks."
---

# Diff Interrogation

Force a diff to prove its behavior, test coverage, and risk profile before acceptance.

## Scope

Use for the task in the description. For example: Review this retry diff for duplicate payment side effects. Do not activate for: Reformat these comments without changing behavior.

## Workflow

1. Summarize the behavior change, not the file list.
2. Identify the highest-risk lines or decisions.
3. Check for missing tests, widened permissions, silent failures, data loss, and hidden coupling.
4. Ask explanation questions for unclear changes.
5. Recommend commit, revise, or reject.

## Evidence

Diff or PR summary. Test output if available. Relevant files, issue, expected behavior, and security-sensitive areas. Report the outcome with relevant behavior change, highest-risk lines, missing proof, questions. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not paste secrets, tokens, customer records, private incident details, or proprietary code into public summaries. Use line references and redacted snippets. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
