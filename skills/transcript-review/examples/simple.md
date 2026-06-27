# Simple Example

Input:

```text
Review a transcript where the agent used diff-interrogation before merging a small validator change.
```

Expected behavior:

- Check whether behavior change, risk lines, missing proof, and recommendation were covered.
- Flag any test claims without command output.
- Recommend no skill change if the behavior matched the contract.
