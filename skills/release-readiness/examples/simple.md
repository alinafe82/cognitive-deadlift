# Simple Example

Input:

```text
Prepare a patch release after adding one skill.
```

Expected behavior:

- Check skill index, catalog, adapter manifests, changelog need, and prod-gate result.
- Flag missing release notes only if a public tag is planned.
- Recommend release or block with exact fixes.
