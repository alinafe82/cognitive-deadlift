# Simple Example

Input:

```text
Explain this date parsing change before merge.
```

Expected behavior:

- Select the smallest date parsing branch or diff hunk.
- Ask the human engineer: "What does this code mean?"
- Require their own explanation of accepted input, rejected input, timezone
  behavior, and the state that reaches each branch.
- Ask a harder follow-up: "What would break if this parser accepted ambiguous
  local dates?"
- Identify the rejected alternative.
- Define a test that would fail if the explanation is wrong.
