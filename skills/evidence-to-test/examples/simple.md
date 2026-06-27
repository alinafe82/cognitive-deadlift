# Simple Example

Input:

```text
A validator misses stale PR template wording.
```

Expected behavior:

- Define a fake PR template fixture with the stale command.
- Expect the validator to report the missing gate.
- Limit the fix to repo-contract validation.
