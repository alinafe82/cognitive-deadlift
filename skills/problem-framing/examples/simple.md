# Simple Example

Input:

```text
Add retries to the webhook worker.
```

Expected output shape:

```md
Problem: Webhook processing may fail transiently, but the current failure mode has not been identified.
Current evidence: No logs, failure rate, or error class supplied.
Assumptions: Failures are transient; retrying is safe; webhook handling is idempotent.
Non-goals: Designing the retry implementation before proving the failure.
Success condition: A known transient failure is retried without duplicate side effects.
First verification step: Inspect worker logs or tests for the current failure path.
```
