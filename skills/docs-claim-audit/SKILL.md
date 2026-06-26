---
name: docs-claim-audit
description: "Audit README, docs, comments, examples, and public copy against repository evidence. Use when merging documentation changes or public claims to ensure claims are backed by files, tests, scripts, examples, or explicit limitation language. NOT for typo-only edits or private notes that make no factual claims."
---

# Docs Claim Audit

## Purpose

Keep public documentation factual, bounded, and backed by repo evidence.

## Preserves

Source-based reasoning and documentation honesty.

## Required Evidence

- Changed docs or claim text.
- Files, tests, scripts, examples, or commands that support each claim.
- Known limitations or unsupported surfaces.
- Target audience if relevant.

## Failure Signs

- Docs claim a feature exists without a backing file or command.
- Limitations are hidden behind polished wording.
- Examples imply behavior that tests or scripts do not support.

## When To Use

- README, docs, comments, examples, or public copy change.
- A claim describes support, readiness, security, compatibility, or behavior.
- Docs mention tests, checks, integrations, or runtime support.
- A reviewer suspects marketing filler or unsupported scope.

## When Not To Use

- Typo-only edits with no factual claim change.
- Private local notes that are not public docs.
- The task is to check external docs before coding; use read-the-docs-first.

## Inputs Expected

- Changed documentation or claim list.
- Relevant source files, validators, tests, scripts, examples, and command output.
- Known limitations or out-of-scope behavior.
- Diff if available.

## Output Expected

```md
Claim:
Evidence found:
Unsupported part:
Required edit:
Verification:
Decision:
```

## Process

1. Extract each factual claim from the changed text.
2. Trace each claim to a repo artifact or command output.
3. Mark claims as supported, unsupported, overstated, or explicitly limited.
4. Replace unsupported claims with factual wording or limitation language.
5. Run the relevant doc or slop checks when changing public docs.

## Quality Bar

A good audit leaves no public claim stronger than the evidence available in the repository.

## Examples

Simple case: README says make prod-gate runs all meaningful checks. The skill should verify Makefile prod-gate target.

Complex case: Docs claim runtime compatibility with Codex, Claude, and Gemini after only manifest validation. The skill should separate manifest consistency from actual runtime smoke testing.

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
