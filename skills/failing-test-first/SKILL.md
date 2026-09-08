---
name: failing-test-first
description: "Reproduce a reported bug, fix it, and verify the regression with the narrowest useful test."
---

# Failing Test First

Turn a fix from a guess into a red-green feedback loop.

## Scope

Use for the task in the description. For example: Fix the parser accepting an empty required field and prove the regression. Do not activate for: Correct README punctuation.

## Workflow

1. Identify the smallest behavior that should fail before the fix.
2. Use an existing test harness when available.
3. If no harness exists, create a repeatable command or script.
4. Run the failing signal and capture the failure.
5. Implement the smallest fix.
6. Re-run the failing signal and nearby regression checks.

## Evidence

Bug description or desired behavior. Smallest failing signal available. Command or repeatable step that can prove the failure and the fix. Report the outcome with relevant failing signal, command, expected failure, fix boundary. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not use real credentials, payment data, medical records, customer records, or production-only endpoints in tests. Use fixtures or redacted examples. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
