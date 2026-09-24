# Edge Case Example

Input:

```text
A release changes runtime routing in skills_index.json but not the Gemini extension manifest.
```

Expected behavior:

- Trace each runtime manifest and the shared skills index.
- Flag missing Gemini manifest change only if public routing changed.
- Recommend publish only after affected runtimes are checked.
