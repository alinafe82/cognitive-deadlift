---
name: problem-framing
description: Force a developer to define the real problem before implementation. Use when a request jumps straight to code, asks for a fix without a reproduction, proposes a solution before stating the problem, or needs a sharper engineering objective.
---

# Problem Framing

Do not implement until the problem is stated in operational terms.

## Process

1. State the user-visible symptom or desired capability.
2. Identify the affected actor, workflow, and boundary.
3. Separate facts from interpretations.
4. Define what evidence would prove the problem exists.
5. Define what evidence would prove the problem is solved.

## Required Output

Produce a short problem frame:

```md
Problem:
Current evidence:
Non-goals:
Success condition:
First verification step:
```

If the user gave a solution instead of a problem, challenge it directly and recommend the narrower problem statement.
