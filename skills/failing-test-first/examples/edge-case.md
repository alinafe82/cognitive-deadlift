# Edge Case Example

Input:

```text
Retry logic may double-submit payments.
```

Expected behavior:

- Create a failing test proving duplicate side effects can occur or are not guarded.
- Verify idempotency keys or dedupe logic.
- Run regression checks around payment submission and retry behavior.
