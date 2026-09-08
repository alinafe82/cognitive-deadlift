# Skill Standard

A skill should add useful task-specific guidance. Keep its description short and its root focused; load worked examples only when needed.

## Package contract

- `SKILL.md` has frontmatter with a name matching the folder and a non-empty task-specific description. Descriptions have no mandatory wording or minimum length; the static grade budget is 240 characters.
- The body explains scope, workflow, evidence needed/produced, and relevant data/action boundaries. The compact format uses `Scope`, `Workflow`, `Evidence`, and `Boundaries`; legacy equivalent sections remain accepted. There is no required number of steps, output fields or warnings.
- Include two non-empty worked examples in `examples/` and link supporting resources from the root. Keep detailed teaching material outside the root; the static grade budget is 450 words.
- `tests/routing.json` records non-empty `use` and `skip` lists of objects with `request` and `reason`. Requests must be distinct, including across decisions. These are review cases, not a model benchmark.
- Add executable tests or fixtures only when they verify a real behavior. Existing legacy fixture packages remain valid; new compact skills need routing cases.

## Review

Check that a concrete request selects this skill rather than its nearest neighbor. Evaluate the workflow against its examples: can it produce a useful result without unnecessary questions or ceremony? Do not infer quality from section counts or repeated safety prose.

Preserve factual evidence, data boundaries and applicable authorization requirements. Reuse authorization already supplied for an action. Reversible preparation and read-only work should continue; sending, publication, destruction and widening permissions need authorization when absent.

## Verification

Run affected validators and tests during edits; `make prod-gate` is required before merge/release or changes to the validation contract. Keep metadata, links, examples, routing cases, adapter lists and the shared skills index consistent. Static checks cannot establish actual activation accuracy or model performance.
