---
name: assumption-audit
description: Surface and challenge hidden assumptions in a plan, prompt, bug report, design, or AI-generated answer. Use before committing to an approach or when the user claims something is obvious, simple, safe, or already decided.
---

# Assumption Audit

Treat confidence as a thing to inspect, not a thing to inherit.

## Process

1. Extract assumptions from the request, plan, and code context.
2. Classify each assumption as factual, technical, product, operational, or social.
3. Mark whether it is verified, likely, risky, or unknown.
4. Inspect code or docs for assumptions that can be checked locally.
5. Ask only for assumptions that cannot be checked and would change the work.

## Required Output

```md
Verified:
Likely but unproven:
Risky:
Unknown:
Recommended next check:
```

Challenge at least one assumption unless all assumptions are already verified by code or docs.
