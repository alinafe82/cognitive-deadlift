# Edge Case Example

Input:

```text
A release changes AGENTS.md, GEMINI.md, and skills_index.json but not the Gemini extension manifest.
```

Expected behavior:

- Trace each runtime context file.
- Flag missing Gemini manifest change only if context routing changed.
- Recommend publish only after affected runtimes are checked.
