---
name: alternatives-before-code
description: Require multiple viable approaches before implementation. Use for architecture, refactors, data model changes, workflow changes, tool choices, or any request where the first idea could be local optimum thinking.
---

# Alternatives Before Code

Do not let the first plausible plan become the plan by default.

## Process

1. Name the decision being made.
2. Present three options: minimal, structural, and conservative/no-build.
3. Compare cost, reversibility, blast radius, testability, and cognitive load.
4. Recommend one option and say what would make you change your mind.

## Required Output

```md
Decision:
Option A:
Option B:
Option C:
Recommendation:
Change-my-mind evidence:
```

If only one option seems viable, explain which constraint eliminated the others.
