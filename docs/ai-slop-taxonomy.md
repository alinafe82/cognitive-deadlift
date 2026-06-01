# AI Slop Taxonomy

This taxonomy names review smells in AI-assisted work. Use it to repair the work,
not to score the author.

## S1: Unsupported Claim

- Signal: The docs or summary says something works without file, test, script, or command
  evidence.
- Example: "The validator covers every edge case" with no tests for those cases.
- Why it matters: Reviewers may accept confidence instead of proof.
- Repair: Cite the evidence or narrow the claim.

## S2: Fake Completeness

- Signal: The change presents itself as finished while known gaps remain hidden.
- Example: A README lists commands that are not wired into the Makefile.
- Why it matters: Users trust setup and validation paths that fail later.
- Repair: Implement the missing behavior or state the limitation plainly.

## S3: Placeholder Implementation

- Signal: Code or docs leave a stub, dummy branch, or vague future note in a live path.
- Example: A validator accepts any file because the real checks were deferred.
- Why it matters: The repo appears safer than it is.
- Repair: Replace the stub with real behavior or remove the claim.

## S4: Over-Abstraction

- Signal: The solution adds layers before the problem needs them.
- Example: A plugin framework replaces three small scripts with no second consumer.
- Why it matters: Maintenance cost rises before value is proven.
- Repair: Use the smallest local change and record what would justify a larger design.

## S5: Test Theater

- Signal: Tests exist but do not prove the risky behavior.
- Example: A bug fix adds only a happy-path test while the failure path remains untested.
- Why it matters: Reviewers get false confidence.
- Repair: Add a failing signal that matches the bug or state why no proper seam exists.

## S6: Diff Sprawl

- Signal: The diff touches unrelated files, formats, or names while solving a narrow task.
- Example: A docs fix also rewrites script structure without evidence.
- Why it matters: Reviewers must separate intent from churn.
- Repair: Split the work or remove unrelated changes.

## S7: Generic Documentation

- Signal: The README could describe many AI repos with only the project name changed.
- Example: Broad claims about better workflows without naming commands, files, or limits.
- Why it matters: Users cannot tell what exists or how to verify it.
- Repair: Name the concrete artifact, command, workflow, and limitation.

## S8: Silent Failure Handling

- Signal: Errors are swallowed, logged vaguely, or converted into success states.
- Example: A script exits zero after a validation failure.
- Why it matters: Automation reports health while behavior is broken.
- Repair: Fail loudly or return a clear degraded status with evidence.

## S9: Unjustified Dependency

- Signal: A dependency is added for work the standard library or existing tools can do.
- Example: A schema package is added for four simple YAML-like files.
- Why it matters: Supply-chain and maintenance cost grow without need.
- Repair: Use the existing toolchain unless a real limitation is shown.

## S10: Tool Permission Creep

- Signal: The assistant or script gets broader write, network, or destructive permissions
  than the task requires.
- Example: A cleanup task asks to reset the repo instead of reporting candidates first.
- Why it matters: Agent speed can amplify mistakes.
- Repair: Use least privilege, inspect first, and require human approval for high-risk
  actions.
