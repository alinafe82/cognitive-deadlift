---
name: thinking-ledger-review
description: "Review thinking ledgers for substantive reasoning evidence. Use when accepting a staged or submitted thinking ledger for non-trivial work to check problem, assumptions, alternatives, evidence, verification, tradeoffs, and risk. NOT for checking only whether a ledger file exists or for reviewing unrelated prose docs."
---

# Thinking Ledger Review

## Purpose

Make reasoning evidence reviewable instead of treating ledger presence as proof.

## Preserves

Evidence discipline and accountable decision-making.

## Required Evidence

- Ledger file or staged ledger content.
- Changed files or task summary.
- Risk level from the thinking budget.
- Verification commands or evidence cited by the ledger.

## Failure Signs

- The ledger repeats the final answer without showing evidence.
- Alternatives are named but not compared.
- Tests are claimed without command output or limitations.

## When To Use

- A non-trivial change includes a thinking ledger.
- A pre-commit hook passed because a ledger exists but substance is uncertain.
- A reviewer wants to check reasoning evidence before merge.
- A high-risk change needs approval evidence.

## When Not To Use

- No ledger exists and the task is to create one from scratch.
- The change is purely mechanical and explicitly low risk.
- The request is to review code behavior; use diff-interrogation.

## Inputs Expected

- Ledger path or text.
- Task summary and risk level.
- Related diff or file list.
- Commands run and outputs if available.

## Output Expected

```md
Ledger:
Risk level:
Required evidence:
Evidence present:
Evidence missing:
Unsupported claims:
Decision:
```

## Process

1. Map the task to low, medium, or high thinking budget requirements.
2. Check that the ledger names problem, assumptions, alternatives, evidence, verification, and tradeoffs when required.
3. Compare claims to available commands, diffs, or artifacts.
4. Flag vague confidence, copied summaries, and missing rollback or approval for high-risk work.
5. Recommend accept, revise, or block until missing evidence is supplied.

## Quality Bar

A good review makes clear whether the ledger proves the developer understood the change, not just that a file was staged.

## Examples

Simple case: Review a ledger for a medium-risk validator change. The skill should check trace evidence, failing or targeted test evidence, and diff review notes.

Complex case: Review a ledger for a permissions change that has tests but no rollback plan. The skill should classify as high risk.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Required files missing: state what could not be checked and ask for the smallest missing artifact.
- Context ambiguous: list the plausible interpretations and pick the one that affects the decision most.
- Permissions missing: name the command, file, or approval needed without inventing results.
- Tests or checks fail: report the failure and do not recommend acceptance until the failure is understood.
- Unsafe request: refuse the unsafe step and offer a safe review or evidence-gathering path.
- Claim cannot be verified: mark it as unsupported and require evidence or limitation language.

## Safety And Privacy

Do not request or expose secrets, tokens, private keys, customer records, private employer details, personal data, or production credentials. Use redacted examples and require approval before destructive, external-send, permission-widening, or publication actions.

## Anti-Slop Rules

- Do not approve a skill, claim, release, or workflow on confident wording alone.
- Do not treat file presence as evidence of substance.
- Do not invent command results, runtime behavior, usage evidence, or reviewer approval.
- Do not broaden scope to make the recommendation sound more useful.
- Do not hide missing evidence in a generic summary.
