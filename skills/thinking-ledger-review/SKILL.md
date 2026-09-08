---
name: thinking-ledger-review
description: "Review an existing thinking ledger against its cited evidence and applicable risk requirements."
---

# Thinking Ledger Review

Make reasoning evidence reviewable instead of treating ledger presence as proof.

## Scope

Use for the task in the description. For example: Review this submitted thinking ledger against its cited test output. Do not activate for: Review a code diff with no ledger attached.

## Workflow

1. Apply the relevant evidence policy to the supplied ledger, without requiring a new ledger for unrelated work.
2. Check that the ledger names problem, assumptions, alternatives, evidence, verification, and tradeoffs when required.
3. Compare claims to available commands, diffs, or artifacts.
4. Flag vague confidence, copied summaries, and missing rollback evidence or missing authorization for a consequential action.
5. Recommend accept, revise, or block until missing evidence is supplied.

## Evidence

Ledger file or staged ledger content. Changed files or task summary. Risk level from the thinking budget. Verification commands or evidence cited by the ledger. Report the outcome with relevant ledger, risk level, required evidence, evidence present. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
