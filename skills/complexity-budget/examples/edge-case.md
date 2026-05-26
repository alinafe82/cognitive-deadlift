# Edge Case Example

Input:

```text
Add a queue and retry worker for billing sync.
```

Expected behavior:

- List queue, worker, retry policy, idempotency, observability, and ownership as moving parts.
- Compare with scheduled retry or synchronous retry.
- Define the deletion path.
- Recommend only if the proven failure requires it.
