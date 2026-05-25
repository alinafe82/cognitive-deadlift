---
name: debugging-lab-notebook
description: "Debug hard failures with reproduction, hypotheses, instrumentation, experiments, and regression proof. Use when bugs are flaky, poorly understood, production-facing, performance-related, or AI starts guessing fixes. NOT for simple bugs that already have a deterministic failing test."
---

# Debugging Lab Notebook

## Purpose

Turn hard debugging into a recorded experiment loop instead of a sequence of guesses.

## When To Use

- A bug is hard, flaky, or poorly understood.
- The failure crosses services, time, state, or concurrency boundaries.
- AI starts proposing fixes without a hypothesis.
- Negative findings need to be preserved.

## When Not To Use

- Simple bugs that already have a failing test.
- Purely visual defects with an obvious screenshot reproduction.
- Incidents where immediate mitigation must happen before root-cause analysis.

## Inputs Expected

- Symptom and reproduction attempt.
- Logs, traces, metrics, failing command, or user report if available.
- Code area or workflow likely involved.
- Constraints on instrumentation or environment access.

## Output Expected

```md
Reproduction:
Hypotheses:
Experiment:
Result:
Next hypothesis:
Regression proof:
```

## Process

1. Build the smallest available reproduction or observation signal.
2. Write competing hypotheses.
3. Add instrumentation that distinguishes between hypotheses.
4. Run one experiment at a time.
5. Record negative findings.
6. Add regression proof after the fix.

## Quality Bar

A good notebook lets another engineer see what was tried, what was ruled out, and why the final fix is credible.

## Examples

Simple case: a CLI sometimes exits zero after failure. The skill should reproduce the command, list hypotheses around exception handling, and add a regression check.

Complex case: a worker drops messages under load. The skill should separate queue delivery, concurrency, retry, timeout, and persistence hypotheses before changing code.

See `examples/simple.md` and `examples/edge-case.md`.

## Failure Modes

- Reproduction unavailable: define the next best observation point and explain the uncertainty.
- Flaky signal: measure frequency before and after changes.
- Logs contain sensitive data: request redacted or synthetic traces.
- Permissions missing: ask for specific command output rather than broad access.

## Safety And Privacy

Do not expose raw production logs, tokens, customer data, internal hostnames, or private incident details. Remove exploratory instrumentation unless it is intentionally kept.

## Anti-Slop Rules

- Do not patch before naming a hypothesis.
- Do not keep only one favored hypothesis.
- Do not drop negative findings.
- Do not claim root cause until the experiment supports it.

