# Expected Behavior

A careful response should reject test confidence that is not backed by command output.

It should:

- identify the behavior change
- require a failing signal for the parser bug
- inspect whether edge cases are covered
- run or request the exact test command
- avoid saying tests passed unless they were run
- recommend revision if proof is missing

Relevant skills:

- `failing-test-first`
- `diff-interrogation`
- `explain-without-ai`
