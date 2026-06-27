# Edge Case Example

Input:

```text
Review a broad skill named better-coding that overlaps with problem-framing, trace-the-code, and diff-interrogation.
```

Expected behavior:

- Reject the broad name and scope.
- Map each claimed behavior to existing skills.
- Recommend a narrower skill only if a distinct repeated problem remains.
