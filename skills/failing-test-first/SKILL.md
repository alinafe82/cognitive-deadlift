---
name: failing-test-first
description: "Require a failing signal before bug fixes or behavior changes. Use when fixing a bug, adding behavior, changing edge cases, or reviewing AI code that lacks proof. NOT for docs-only edits, generated snapshots, or emergency hotfixes with a tracked follow-up test."
---

# Failing Test First

## Purpose

Turn a fix from a guess into a red-green feedback loop.

## Preserves

Behavioral proof and test design.

## Required Evidence

- Bug description or desired behavior.
- Smallest failing signal available.
- Command or repeatable step that can prove the failure and the fix.

## Failure Signs

- The fix is written before the failing signal is defined.
- Test results are claimed without command output.
- The test covers only the happy path while the bug is an edge case.

## When To Use

- A bug fix is requested.
- New behavior needs acceptance proof.
- AI proposes a code change without showing a failing signal.
- A regression could return silently.

## When Not To Use

- Documentation-only edits.
- Snapshot or lockfile churn with separate validation.
- Emergency hotfixes where restoration is more urgent and a follow-up test is tracked.

## Inputs Expected

- Bug description or desired behavior.
- Existing test command if known.
- Relevant files, reproduction steps, logs, or failing user workflow.

## Output Expected

```md
Failing signal:
Command:
Expected failure:
Fix boundary:
Passing signal:
Regression checks:
```

## Process

1. Identify the smallest behavior that should fail before the fix.
2. Use an existing test harness when available.
3. If no harness exists, create a repeatable command or script.
4. Run the failing signal and capture the failure.
5. Implement the smallest fix.
6. Re-run the failing signal and nearby regression checks.

## Quality Bar

A good result includes a command that failed before the change and passed after the change, plus a clear explanation of what behavior the test proves.

## Examples

Simple case: a parser accepts invalid empty input. The skill should create or identify a test that fails on empty input before changing parser code.

Complex case: a retry loop double-submits payments. The skill should create a failing integration or boundary test proving only one payment side effect occurs.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- No test framework: create the smallest repeatable script or manual command and state its limits.
- Flaky failure: isolate the smallest deterministic signal before changing code.
- Tests fail for unrelated reasons: record the baseline failure and avoid claiming the fix passed.
- Permissions missing: ask for the command or log output needed to reproduce.

## Safety And Privacy

Do not use real credentials, payment data, medical records, customer records, or production-only endpoints in tests. Use fixtures or redacted examples.

## Anti-Slop Rules

- Do not write the fix before defining the failing signal.
- Do not claim a test failed or passed unless it was run.
- Do not test private internals when public behavior can prove the fix.
- Do not stop at the happy path if the risk is an edge case.
