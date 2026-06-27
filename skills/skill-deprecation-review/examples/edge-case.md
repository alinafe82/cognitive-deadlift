# Edge Case Example

Input:

```text
Review a popular but broad skill that overlaps with five narrower skills.
```

Expected behavior:

- Consider migration path before deletion.
- Recommend splitting or redirecting if users rely on it.
- Avoid deleting solely because overlap exists.
