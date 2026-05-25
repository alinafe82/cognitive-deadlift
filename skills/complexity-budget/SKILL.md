---
name: complexity-budget
description: Challenge unnecessary abstraction, architecture, dependencies, and cleverness. Use when a solution adds new modules, frameworks, queues, caches, state machines, agents, or indirection.
---

# Complexity Budget

Every moving part spends future attention. Make the spend explicit.

## Process

1. List the new concepts, dependencies, states, and failure modes.
2. Identify which complexity is essential versus optional.
3. Compare with the boring solution.
4. Define the deletion path if the abstraction fails to pay for itself.

## Required Output

```md
New moving parts:
Essential complexity:
Optional complexity:
Boring alternative:
Deletion path:
Recommendation:
```

Prefer the boring alternative unless the added complexity buys a named capability or removes larger existing complexity.
