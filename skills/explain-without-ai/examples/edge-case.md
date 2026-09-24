# Edge Case Example

Input:

```text
AI generated a caching layer for permission checks.
```

Expected behavior:

- Do not explain the caching layer first.
- Ask the human engineer what the cache key means, what invalidates it, and
  which permission state can become stale.
- Reject generic answers like "it improves performance" until they name the
  code path and branch that controls access.
- Ask the harder follow-up: "What would break if a role update happens between
  cache fill and cache expiry?"
- Explain the rejected no-cache alternative.
- Name a breakage test around role updates.
