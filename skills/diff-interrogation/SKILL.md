---
name: diff-interrogation
description: Review a generated or human diff as untrusted code. Use before merging, committing, or accepting AI-generated changes; focus on behavioral regressions, missing tests, security risk, and code that the developer cannot explain.
---

# Diff Interrogation

Treat every diff as a claim. Make it prove itself.

## Process

1. Summarize the behavior change, not the file list.
2. Identify the highest-risk lines.
3. Check for missing tests, widened permissions, silent failures, data loss, and hidden coupling.
4. Ask whether the developer can explain every changed line.
5. Recommend commit, revise, or reject.

## Required Output

```md
Behavior change:
Highest-risk lines:
Missing proof:
Questions:
Recommendation:
```

Lead with findings. Avoid praise unless there are no issues.
