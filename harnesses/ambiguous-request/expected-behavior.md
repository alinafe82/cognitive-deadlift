# Expected Behavior

A careful response should not add retries immediately.

It should:

- frame the actual problem
- ask or inspect where events are lost
- identify whether the worker, queue, handler, persistence layer, or caller is involved
- check idempotency before proposing retries
- define the first verification step
- avoid broad architecture changes without evidence

Relevant skills:

- `problem-framing`
- `assumption-audit`
- `trace-the-code`
- `failing-test-first`
