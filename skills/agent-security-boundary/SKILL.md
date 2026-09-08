---
name: agent-security-boundary
description: "Review agent workflows when trust boundaries, data access, tool permissions, or external side effects change."
---

# Agent Security Boundary

Prevent agent workflows from widening permissions, leaking data, or trusting hostile context.

## Scope

Use for the task in the description. For example: Review a tool that executes commands extracted from uploaded documents. Do not activate for: Rename a local helper without changing tool or data access.

## Workflow

1. Map every tool, file, network, and external-state boundary.
2. Classify data sensitivity and untrusted inputs.
3. Identify how prompt injection or misleading context could steer tool use.
4. Check approval gates for destructive, permission-widening, or external-send actions.
5. Recommend guardrails, rejection, or targeted validation before merge.

## Evidence

Tool, file, network, or permission surfaces touched. Data sensitivity and trust boundaries. User approvals or destructive action requirements. Prompt-injection and untrusted-content exposure. Report the outcome with relevant workflow, tools and data, trust boundaries, prompt-injection risks. Adapt the format to the task; omit empty fields. Never claim checks ran without observed results.

## Boundaries

Keep secrets and private records out of shared artifacts. Use redacted or synthetic evidence. External sends, publication, destructive operations and permission widening need explicit authorization; reuse authorization already given for the action. Continue authorized read-only and reversible local work through the requested outcome. If evidence is missing, inspect available sources before asking; report limits honestly.

## References

For worked examples, open [simple](examples/simple.md) or [edge case](examples/edge-case.md) only when useful. [Routing cases](tests/routing.json) record positive and negative activation examples for review; they are not a model benchmark.
