# Edge Case Example

Input:

```text
Webhook requests return 200 but are not persisted.
```

Expected behavior:

- Trace request handler, validation, persistence, retry, and error logging.
- Identify where success response can happen before durable write.
- Mark unknowns if a generated or external boundary is reached.
