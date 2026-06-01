# Skill Atrophy Taxonomy

This taxonomy names developer skills that can weaken when AI output is accepted
passively. It is a review aid, not a diagnosis of the developer.

## A1: Problem Outsourcing

- Definition: Letting the model define the problem from a vague request.
- What it looks like: The answer jumps straight to a solution without naming the
  actor, workflow, symptom, boundary, or success condition.
- Why it is harmful: The fix may solve the assistant's guessed problem instead of the
  real one.
- Which skill catches it: `problem-framing`.
- Minimal repair: Restate the problem, evidence, assumptions, non-goals, success
  condition, and first verification step.

## A2: Codepath Blindness

- Definition: Editing code without reading the path that already handles the behavior.
- What it looks like: New branches or helpers appear without file references to callers,
  state changes, or error paths.
- Why it is harmful: The change may bypass existing behavior or duplicate hidden logic.
- Which skill catches it: `trace-the-code`.
- Minimal repair: Trace entry point, call path, data shape, state effects, and error path.

## A3: Test Theater

- Definition: Adding tests that create confidence without proving the risky behavior.
- What it looks like: Only happy-path tests, shallow mocks, or claims that tests passed
  without command output.
- Why it is harmful: Reviewers accept proof that does not cover the failure mode.
- Which skill catches it: `failing-test-first`.
- Minimal repair: Define the failing signal, run it, fix the behavior, then rerun it.

## A4: Diff Trust

- Definition: Treating an AI-generated diff as if it is already reviewed.
- What it looks like: The review summarizes files changed but does not inspect behavior,
  risk, tests, or permissions.
- Why it is harmful: Regressions, widened access, and silent failures can hide in tidy
  patches.
- Which skill catches it: `diff-interrogation`.
- Minimal repair: Lead with behavior change, highest-risk lines, missing proof,
  questions, and recommendation.

## A5: Debugging Avoidance

- Definition: Asking AI for fixes before building a reproduction or hypothesis.
- What it looks like: Several patches are tried without a stable signal or recorded
  negative findings.
- Why it is harmful: The team learns less with every attempted fix.
- Which skill catches it: `debugging-lab-notebook`.
- Minimal repair: Record reproduction, hypotheses, one experiment, result, next
  hypothesis, and regression proof.

## A6: Abstraction Inflation

- Definition: Accepting a larger abstraction because it sounds cleaner than the local
  change.
- What it looks like: New modules, configuration layers, frameworks, or state machines
  appear before there are real call sites.
- Why it is harmful: Future maintainers inherit concepts that do not pay for themselves.
- Which skill catches it: `complexity-budget`.
- Minimal repair: List new moving parts, essential complexity, optional complexity,
  boring alternative, deletion path, and recommendation.

## A7: Context Laundering

- Definition: Turning weak or stale context into confident output.
- What it looks like: The model cites requirements, docs, APIs, or policies that were not
  opened or verified.
- Why it is harmful: The final answer sounds sourced even when it is inference.
- Which skill catches it: `read-the-docs-first`.
- Minimal repair: List sources checked, relevant constraints, inference, docs gap, and
  next action.

## A8: Tool Autopilot

- Definition: Letting an agent use tools before the risk of the action is understood.
- What it looks like: Broad edits, deletes, permission changes, or network actions happen
  before scope and approval are clear.
- Why it is harmful: Tool speed can discard work or widen access faster than review can
  catch it.
- Which skill catches it: `assumption-audit`.
- Minimal repair: Classify assumptions, inspect local state, and require approval for
  destructive or high-risk actions.

## A9: Explanation Collapse

- Definition: Being unable to explain how the change works without restating the model's
  summary.
- What it looks like: The developer can name the outcome but not the mechanism, breakage
  test, or rejected alternative.
- Why it is harmful: Ownership is weak, so debugging and review depend on the assistant.
- Which skill catches it: `explain-without-ai`.
- Minimal repair: Explain mechanism, code path, rejected alternative, breakage test, and
  confidence gap.

## A10: Review Fatigue

- Definition: Letting volume or fluency lower review standards.
- What it looks like: Large diffs are accepted because they appear consistent, not because
  risky behavior was checked.
- Why it is harmful: The easiest review path becomes trusting the generated shape.
- Which skill catches it: `diff-interrogation`.
- Minimal repair: Triage highest-risk behavior first and reject or split the diff when
  proof is missing.
