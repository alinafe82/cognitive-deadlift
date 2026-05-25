# Edge Case Example

Input:

```text
We can cache permission checks because role changes are rare.
```

Expected behavior:

- Identify assumptions about role-change frequency, cache invalidation, stale access, and audit requirements.
- Mark security-sensitive assumptions as risky until verified.
- Recommend checking authorization code and role update paths before implementation.
