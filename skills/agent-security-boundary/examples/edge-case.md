# Edge Case Example

Input:

```text
Review an agent workflow that reads user-uploaded docs and runs shell commands based on extracted instructions.
```

Expected behavior:

- Treat uploaded docs as untrusted content.
- Block document-sourced tool instructions.
- Require explicit user approval for shell actions.
