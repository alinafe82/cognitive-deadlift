---
name: evidence-to-test
description: "Turn a specific recurring review failure or validator gap into a repeatable regression check."
---

# Evidence To Test

Turn review concerns into repeatable proof instead of recurring discussion.

## Scope

Use for the task in the description. For example: Our validator repeatedly misses unsupported test-pass claims; design a regression check. Do not activate for: Implement the fix for this existing precise failing unit test.

## Workflow

1. Restate the gap as an invariant that can fail.
2. Choose the narrowest test surface: unit test, validator fixture, harness case, slop scan, or command check.
3. Define the red signal before proposing the fix.
4. Name fixture data needed to prove the behavior without private data.
5. Keep the check deterministic, fast, and aligned with the repo contract.

## Evidence

Gap or repeated failure described in concrete terms. Observable bad behavior or missing invariant. Existing test or validator surface. Expected failing signal before the fix. Report the outcome with relevant gap, observable failure, best test surface, fixture needed. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
