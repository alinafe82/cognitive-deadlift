---
name: diff-interrogation
description: "Review a human or AI-generated diff as an untrusted claim. Use when merging, committing, or accepting changes that may hide regressions, missing tests, security risk, data loss, or unexplained behavior. NOT for formatting-only diffs or already-reviewed changes with no new code."
---

# Diff Interrogation

## Purpose

Force a diff to prove its behavior, test coverage, and risk profile before acceptance.

## When To Use

- A diff came from AI, heavy autocomplete, or an unfamiliar contributor.
- The change touches behavior, data, auth, permissions, persistence, or error handling.
- Tests are missing or only prove the happy path.
- The developer cannot explain every meaningful line.

## When Not To Use

- Formatting-only diffs.
- Lockfile or generated artifact updates with separate verification.
- Diffs already reviewed after the latest changes.

## Inputs Expected

- Diff or PR summary.
- Test output if available.
- Relevant files, issue, or expected behavior.
- Whether security-sensitive areas are touched.

## Output Expected

```md
Behavior change:
Highest-risk lines:
Missing proof:
Questions:
Recommendation:
```

## Process

1. Summarize the behavior change, not the file list.
2. Identify the highest-risk lines or decisions.
3. Check for missing tests, widened permissions, silent failures, data loss, and hidden coupling.
4. Ask explanation questions for unclear changes.
5. Recommend commit, revise, or reject.

## Quality Bar

A good interrogation leads with actionable findings. It does not praise style while missing behavior risk.

## Examples

Simple case: a diff changes a validation condition. The skill should identify new accepted and rejected inputs and ask for a test proving both.

Complex case: a diff adds retry logic around payment submission. The skill should inspect idempotency, duplicate side effects, logging, and failure handling before recommending merge.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Diff unavailable: ask for `git diff` or a patch before reviewing.
- Tests not run: say so directly and avoid claiming confidence.
- Security-sensitive change: escalate risk and request targeted review.
- Large diff: triage by highest-risk files and behavior first.

## Safety And Privacy

Do not paste secrets, tokens, customer records, private incident details, or proprietary code into public summaries. Use line references and redacted snippets.

## Anti-Slop Rules

- Do not review only the file list.
- Do not say "looks good" without proof.
- Do not bury missing tests.
- Do not claim security safety without checking the relevant paths.

