# Edge Case Example

Input:

```text
Review a long session where the agent used problem-framing but still implemented before tracing code.
```

Expected behavior:

- Separate problem-framing compliance from trace-the-code failure.
- Identify the missed trigger sequence.
- Recommend a rubric or skill example update if the miss is repeatable.
