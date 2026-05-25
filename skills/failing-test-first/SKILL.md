---
name: failing-test-first
description: Enforce a red-green loop before bug fixes or behavior changes. Use when fixing a bug, adding behavior, changing edge-case handling, or when AI proposes code without a failing test or reproducible check.
---

# Failing Test First

A fix without a failing signal is a guess with code attached.

## Process

1. Reproduce the failure manually or with an automated test.
2. Minimize the failing case.
3. Run the test or command and capture the failure.
4. Implement the smallest fix.
5. Re-run the failing check and a relevant regression set.

## Required Output

```md
Failing signal:
Command:
Expected failure:
Fix boundary:
Passing signal:
```

If no automated test framework exists, create the smallest repeatable command or script that fails before the fix.
