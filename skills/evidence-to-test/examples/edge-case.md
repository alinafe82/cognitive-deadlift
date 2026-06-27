# Edge Case Example

Input:

```text
Agent transcripts often claim tests passed without command output.
```

Expected behavior:

- Choose a harness fixture or transcript-review rubric rather than a unit test.
- Define observable unsupported-test-confidence markers.
- Avoid claiming semantic truth beyond the fixture.
