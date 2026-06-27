# Edge Case Example

Input:

```text
Review a ledger for a permissions change that has tests but no rollback plan.
```

Expected behavior:

- Classify as high risk.
- Require rollback and approval evidence.
- Block acceptance until high-risk requirements are met.
