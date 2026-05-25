---
name: read-the-docs-first
description: Require source docs, ADRs, interfaces, schemas, and upstream references before guessing. Use when the task touches external APIs, framework behavior, repo conventions, architecture decisions, or policy.
---

# Read The Docs First

Guessing is allowed only after the relevant source of truth has been checked or shown to be absent.

## Process

1. Look for local `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`, README files, schemas, and interface definitions.
2. For third-party behavior, prefer official docs or primary sources.
3. Record the exact source that constrains the work.
4. Distinguish documented behavior from inference.

## Required Output

```md
Sources checked:
Relevant constraints:
Inference:
Docs gap:
```

If docs contradict the user's plan, call out the contradiction before changing code.
