# Edge Case Example

Input:

```text
The worker drops messages under load.
```

Expected behavior:

- Separate queue delivery, concurrency, retry, timeout, and persistence hypotheses.
- Add instrumentation that distinguishes between them.
- Preserve negative findings.
- Avoid pasting sensitive production logs.
