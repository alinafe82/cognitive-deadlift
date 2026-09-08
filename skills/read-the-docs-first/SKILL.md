---
name: read-the-docs-first
description: "Verify version-sensitive API behavior or a documented repository constraint needed for the current task."
---

# Read The Docs First

Prevent unsupported claims about tools, APIs, frameworks, and repo decisions.

## Scope

Use for the task in the description. For example: Verify which webhook API version supports the requested event. Do not activate for: Refactor a local pure function whose behavior is fully covered by tests.

## Workflow

1. Read only local docs, schemas or interfaces relevant to the disputed behavior; reuse sources already inspected.
2. Check primary upstream docs when external behavior matters.
3. Record what each source actually constrains.
4. Separate documented facts from inference.
5. Flag contradictions before changing code.

## Evidence

Claim, plan, or task that depends on documented behavior. Local docs, ADRs, schemas, interfaces, or primary upstream sources. Version or date when external behavior may have changed. Report the outcome with relevant sources checked, relevant constraints, inference, docs gap. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Do not send private code, customer data, internal URLs, or confidential employer details to external sites. Use official public docs when browsing is required. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
