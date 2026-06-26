# Simple Example

Input:

```text
Review a skill that tells the agent to read local .env files for setup.
```

Expected behavior:

- Flag secret exposure risk.
- Require .env.example or environment-variable names instead.
- Reject reading raw secrets into context.
