---
name: explain-without-ai
description: Force a human-readable explanation of a plan, diff, algorithm, or incident without leaning on AI-generated phrasing. Use before merge, after large AI-generated changes, during learning tasks, or when the developer may not understand the code.
---

# Explain Without AI

The developer should be able to explain the work in plain language before shipping it.

## Process

1. Ask for or produce a concise explanation without rhetorical polish.
2. Include the actual mechanism, not just the outcome.
3. Explain why the selected approach is better than the obvious alternative.
4. Identify what would break if the explanation is wrong.

## Required Output

```md
Plain explanation:
Mechanism:
Rejected alternative:
Breakage test:
```

If the explanation is vague, ask one focused follow-up that forces a concrete mechanism.
