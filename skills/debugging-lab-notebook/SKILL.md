---
name: debugging-lab-notebook
description: "Run debugging as a lab notebook: reproduce, minimize, hypothesize, instrument, test, and record what changed. Use for hard bugs, flaky behavior, performance regressions, production incidents, or when AI starts guessing fixes."
---

# Debugging Lab Notebook

Do not patch symptoms until the failure has a feedback loop.

## Process

1. Reproduce the issue with the smallest deterministic signal available.
2. Write competing hypotheses.
3. Add instrumentation that can distinguish between hypotheses.
4. Run one experiment at a time.
5. Record negative findings; they are part of the search space.

## Required Output

```md
Reproduction:
Hypotheses:
Experiment:
Result:
Next hypothesis:
```

If reproduction is impossible, define the next best observation point and explain the loss of certainty.
