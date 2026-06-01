# Harnesses

Harnesses are review fixtures for AI-assisted development failure modes. They are
not a full benchmark suite.

Each fixture has:

- `task.md`: the user-facing task
- `expected-behavior.md`: what a careful developer or agent should do
- `rubric.yaml`: review criteria

Use them to test whether a workflow preserves judgment:

- Does it ask for missing constraints when the request is ambiguous?
- Does it read relevant code or docs before editing?
- Does it avoid out-of-scope changes?
- Does it require a failing signal when behavior is being fixed?
- Does it avoid fake test confidence?
- Does it explain tradeoffs?
- Does it stop before unsafe action?

Validate harnesses with:

```bash
make harness-check
```
