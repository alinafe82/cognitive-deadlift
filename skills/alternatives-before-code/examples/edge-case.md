# Edge Case Example

Input:

```text
Failed billing sync might need a queue.
```

Expected behavior:

- Compare synchronous retry, scheduled retry, queue-based retry, and operational mitigation.
- Include idempotency, observability, ownership, and rollback cost.
- Recommend the smallest option that handles the proven failure mode.
