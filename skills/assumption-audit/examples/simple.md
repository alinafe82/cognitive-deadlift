# Simple Example

Input:

```text
This endpoint is idempotent, so retries are safe.
```

Expected output shape:

```md
Verified: None yet.
Likely but unproven: The endpoint can receive duplicate requests.
Risky: Idempotency is assumed but not verified.
Unknown: Whether request IDs or dedupe keys exist.
Recommended next check: Trace endpoint handling and persistence for duplicate submissions.
```
