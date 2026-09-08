---
name: assumption-audit
description: "Audit consequential unverified assumptions in a plan or proposed explanation."
---

# Assumption Audit

Make unverified claims visible before they become implementation decisions.

## Scope

Use for the task in the description. For example: Check whether caching permission checks is safe when roles change. Do not activate for: Apply these already-verified mechanical formatting rules.

## Workflow

1. Extract concrete assumptions from the plan.
2. Classify each as factual, technical, product, operational, or social.
3. Check locally verifiable assumptions in code or docs before asking the user.
4. Mark each assumption as verified, likely, risky, or unknown.
5. Recommend the next check that would most change the decision.

## Evidence

Proposed plan, answer, or design. Claims the plan depends on. Available code, docs, logs, tests, metrics, or constraints. Report the outcome with relevant verified, likely but unproven, risky, unknown. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not request raw secrets, customer data, private contracts, or internal incident details. Ask for redacted evidence or aggregate behavior. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
