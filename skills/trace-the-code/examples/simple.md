# Simple Example

Input:

```text
The --dry-run CLI flag is ignored.
```

Expected behavior:

- Trace argument parsing.
- Trace config construction.
- Trace the branch that should consume `dry_run`.
- Summarize the path before proposing edits.
