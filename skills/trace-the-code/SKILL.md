---
name: trace-the-code
description: Make the developer trace existing execution paths before inventing new behavior. Use when changing unfamiliar code, debugging, reviewing AI-generated edits, or when a plan depends on how the code currently works.
---

# Trace The Code

Do not reason about the system from memory when the code is available.

## Process

1. Locate the public entry point.
2. Follow calls to the state change or external effect.
3. Identify the data shape at each boundary.
4. Note where errors are swallowed, transformed, retried, or surfaced.
5. Summarize the path before proposing edits.

## Required Output

```md
Entry point:
Call path:
State/external effects:
Error path:
Unknowns:
```

Use `rg` first for code search. Prefer file and line references over vague module names.
