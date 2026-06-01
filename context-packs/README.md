# Context Packs

Context packs define the evidence an agent should receive before working on a
common AI-assisted development task.

They are not prompts. They are small checklists for useful context:

- what must be supplied
- what may help
- what should not be included
- how fresh the evidence should be
- what the output should contain
- which skills fit the workflow

Use the smallest pack that matches the task. Low-risk edits may not need a pack.

Validate context packs with:

```bash
make context-check
```
