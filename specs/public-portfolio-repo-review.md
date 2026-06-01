# Public portfolio repo review

Date: 2026-05-31
Owner: Alinafe Matenda
Branch where this doc lives: `portfolio-public-repo-differentiation` on `cognitive-deadlift`.

This is a portfolio-wide planning document. It lives in this repo for convenience because cognitive-deadlift is the flagship and the review work was kicked off here. Per-repo code changes happen in their own repos and PRs.

## Scope honesty

The user asked for a full review and code-change pass on 11 public repos. This document is the source of truth.

**What ships in this `cognitive-deadlift` branch (only):**

- `specs/public-portfolio-repo-review.md` (this file).
- The thinking ledger that accompanies it.
- Registration of the new `specs/` directory in `ARCHITECTURE.md` and `repo-audit.md`.

**What ships as separate PRs in other repos (referenced here, not part of this branch):**

- mlops-factory: exception-leak fix.
- ticket-triage-agent: exception-leak fix.
- compliance-copilot: exception-leak fix.
- Each per-repo PR listed below under "Per-repo plans".

**What ships as GitHub metadata (no commit, no PR):**

- All 11 public repo descriptions updated via `gh repo edit`.

Everything else is documented here as planned follow-up. Do not assume a repo's README has been rewritten unless this doc explicitly lists it as shipped.

## Public repo inventory (2026-05-31)

| Repo | Pushed | LOC class | Tests dir | CI workflows | Initial read |
| --- | --- | --- | --- | --- | --- |
| cognitive-deadlift | 2026-06-01 | medium | yes | ci, codeql, dependency-review, security, validate | Flagship. Already iterated in #7 / #8. |
| infra-iac-refactor | 2026-05-30 | small | yes | terraform.yml, secret-scan.yml | Terraform refactor demo. README is honest. |
| zk-rolling-upgrade | 2026-05-30 | medium | yes | python-ci.yml, secret-scan.yml | Calls itself "simulator". README is grounded. |
| kafka-topic-auditor | 2026-05-30 | medium | yes | python-ci.yml, secret-scan.yml | Audits cleanup candidates. Same scaffold as ZK. |
| es-snapshot-migrator | 2026-05-30 | small | yes | python-ci.yml, secret-scan.yml | Manifest planner. Same scaffold as Kafka/ZK. |
| mlops-factory | 2026-05-30 | larger | yes | ci, docker, secret-scan | ML platform demo. GH description is sales pitch. README is grounded but long. |
| orbital-factory-mlops | 2026-05-30 | small | yes | ci, secret-scan | Drift API. Same template family as mlops-factory. |
| policy-rag-agent | 2026-05-30 | medium | yes | python-ci.yml, secret-scan.yml | RAG with citation refusal. |
| ticket-triage-agent | 2026-05-30 | medium | yes | python-ci.yml, secret-scan.yml | Routing API. Same scaffold as policy-rag-agent. |
| compliance-copilot | 2026-05-30 | medium | yes | python-ci.yml, secret-scan.yml | PR risk scoring. Same scaffold as triage. |
| persistent-cognitive-infrastructure | 2026-05-30 | large | yes | multiple | Ambitious systems-design repo. README sets the right "not a chatbot" boundary already. |

All non-cognitive-deadlift repos share suspiciously identical scaffolding sizes (CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, Dockerfile, repowave.toml, pre-commit-config.yaml). This is the "generated sameness" the user flagged.

### Repeated section structure (the real slop)

A grep across READMEs found these reused section titles:

- "Quickstart"
- "Architecture Overview"
- "Limitations"
- "What It Solves"
- "Repository Layout"
- "Testing"

Plus suspiciously identical docs/ trees: each repo has `docs/architecture.md`, `docs/runbook.md`, `docs/security-notes.md`, `docs/production-readiness.md`. The reviewer-eye smell is high: it reads as "ten repos generated from one template" even when the prose inside each section is fine.

## Pinning decisions

The user's recommended pin set is sound. After reviewing the actual repo state, I confirm:

**Pin these six** (final pin set):

1. `cognitive-deadlift` — flagship, anti-autopilot, EngProd judgment.
2. `infra-iac-refactor` — Terraform/platform refactor with module + test.
3. `zk-rolling-upgrade` — distributed systems orchestration shape (Python).
4. `kafka-topic-auditor` — Kafka operational hygiene.
5. `mlops-factory` — main ML/MLOps demo.
6. `ticket-triage-agent` — main internal-tooling/agent demo.

**Public but unpinned:**

- `es-snapshot-migrator` — secondary infra repo. Honest and small.
- `policy-rag-agent` — secondary agent repo, valuable as the RAG-with-refusal counterpart to ticket-triage-agent's routing-with-confidence story.

**Demote (recommend archive or private):**

- `orbital-factory-mlops` — overlaps with `mlops-factory`. Drift API alone is too thin to stand as its own pinned repo. **Recommendation: archive on GitHub** with a short README note pointing at mlops-factory. Keeping it public-unpinned is the second-best option.
- `compliance-copilot` — overlaps with `ticket-triage-agent`. The "PR risk scoring" core is good but "copilot" naming reads as marketing. **Recommendation: rename to `pr-risk-scorer` and demote to unpinned, OR archive and fold the redaction/scoring logic into ticket-triage-agent's roadmap.** Final call is the user's; I lean rename + demote because the code is real.

**Keep public, do not pin yet:**

- `persistent-cognitive-infrastructure` — too ambitious to be a portfolio "demo" without a working end-to-end flow. README is honest about implemented vs not implemented, which is the right move. Keep it as a serious-prototype signal. Do not pin until a 5-minute local demo runs and a reviewer can see something work.

## No-generated-sameness section

### Repeated patterns to break across infra repos

These four section headings appear in nearly every Python repo: "Quickstart", "Architecture Overview", "Limitations", "What It Solves". Reviewers spotting all four in a row on five repos in a row will discount the work.

Concrete differentiation plan:

| Repo | Replace "What It Solves" with | Replace "Architecture Overview" with | Replace "Limitations" with |
| --- | --- | --- | --- |
| zk-rolling-upgrade | "Why leader-last matters" | "Control flow" | "Adapter work left before a real cluster" |
| kafka-topic-auditor | "Topic hygiene as a platform risk" | "How the audit pass runs" | "What this does not do (no deletes, no compaction)" |
| es-snapshot-migrator | "Why planning is the safe public part" | "How the manifest is built" | "What's out of scope (no restore execution)" |
| infra-iac-refactor | "Why centralize, what I would not centralize" | "Module boundary" | "Not a full AWS foundation" |
| mlops-factory | "Service shape" (already there) | Keep the diagram, lose "Architecture Overview" label | "What's not deployed" |

### Repeated `docs/` subtree

Every Python repo carries `docs/architecture.md`, `docs/runbook.md`, `docs/security-notes.md`, `docs/production-readiness.md`. This is template residue. Each repo should keep the docs it actually needs:

- ZK: keep architecture.md + runbook.md. Drop production-readiness.md (the repo is honest about not being production).
- Kafka: keep architecture.md + runbook.md + security-notes.md (delete safety).
- ES migrator: keep architecture.md. Drop runbook/production-readiness (no execution).
- mlops-factory: keep all four because operations are part of the story.
- Agent repos: collapse production-readiness.md into security-notes.md.

### Repeated identical scaffolding files

Find and verify:

- `repowave.toml` is identical across 9 repos (170 bytes). Either keep one as the canonical, or remove and document the scan policy in CONTRIBUTING.
- `CODE_OF_CONDUCT.md` is 41 bytes on three agent repos — that is empty / placeholder. Either flesh out or remove.
- `Dockerfile` is exactly 371 bytes in compliance-copilot and ticket-triage-agent. Confirm same content (template). Differentiate after PR for each.

## Claims audit

Each public claim must be supported by code, tests, or explicit limitation language. Findings:

| Repo | Claim | Evidence | Verdict |
| --- | --- | --- | --- |
| mlops-factory | "production-ready platform for end-to-end machine learning operations" (GH description) | Repo is a public-safe example per the README. No deployment evidence. | **Slop. Fix description.** |
| mlops-factory | "Kubernetes manifests for deployment review" | `infra/` has manifests; README says "reviewable example, not a live cluster". | Honest. Keep. |
| mlops-factory | "MLflow tracking and model loading boundaries" | `app/model_registry.py` exists. Tests cover load/predict. | Supported. |
| mlops-factory | API returns `str(e)` to clients on line 82 of `app/main.py` | Code confirmed. | **Real bug. Fix.** |
| ticket-triage-agent | "deterministic routing, confidence, queues, optional LLM" | `src/` has these. Tests cover routing logic. | Supported. |
| ticket-triage-agent | API returns `f"Triage failed: {str(e)}"` on line 332 of `src/app.py` | Confirmed. | **Real bug. Fix.** |
| compliance-copilot | Multiple `str(exc)` exposures in `src/app.py` | 8 occurrences. | **Real bug. Fix worst offenders.** |
| policy-rag-agent | "refuses answers that do not include valid citations" | `src/app.py:103` references `str(exc)`. Tests need verification. | Tests partially exposed; recheck citation tests. |
| zk-rolling-upgrade | "Simulated Zookeeper rolling upgrade" | README says simulator. No real cluster connection. | Honest. Reframe to "local adapter boundary" per user instruction. |
| kafka-topic-auditor | "The current client is a local mock" | Same. | Honest. Reframe to "local deterministic adapter". |
| persistent-cognitive-infrastructure | "Persistent Cognitive Infrastructure: a distributed runtime for context graphs, semantic events, cognition scheduling, reconciliation, and governed memory" | README has clear "implemented vs not" sections. | Mostly supported. Tone down the GH description. |

## Security posture (quick pass)

Findings from a one-pass scan of each repo. Full scan is recommended as a follow-up with `gitleaks`/`trufflehog`.

| Check | Result |
| --- | --- |
| Secrets in tracked files (`AWS_ACCESS_KEY_ID`, `OPENAI_API_KEY`, `SECRET`, `TOKEN`, `PASSWORD`, private keys) | Not run yet. Follow-up: run `gitleaks detect` on each clone. |
| `str(e)` exposure to clients | Found in 3 repos (mlops-factory, ticket-triage-agent, compliance-copilot). Will fix this PR. |
| CORS defaults | Not checked yet across repos. Follow-up: check `allow_origins=["*"]` in all FastAPI apps. |
| CI permissions | Each repo has its own workflow set. `cognitive-deadlift` has the strongest (minimal permissions, pinned actions). Other repos need an audit pass. |
| Docker root user | Need to verify each Dockerfile. ticket-triage-agent and compliance-copilot have identical 371-byte Dockerfiles, suspicious. |
| Kubernetes manifests | Only `mlops-factory` and `persistent-cognitive-infrastructure` have these. PCI does Helm render in CI per the user's instruction. |
| LLM prompt injection surface | policy-rag-agent and compliance-copilot use LLM input. Need to verify input sanitization and refusal-pattern tests. |

## Final profile story

How the six pinned repos work together as a narrative for a senior platform/EngProd reviewer:

- **`cognitive-deadlift`** is the meta repo. It is the EngProd judgment showcase: how I structure skills, hooks, and validation around AI-assisted engineering. It signals "I think about how AI changes engineering, not just how to use it."

- **`infra-iac-refactor`** is the platform-conventions repo. It is small on purpose. It signals "I know how to put repeated infrastructure code behind a module and prove the conventions hold with `terraform test`."

- **`zk-rolling-upgrade`** is the distributed-systems-operations repo. It signals "I know what the control flow of a rolling upgrade looks like in a coordinated system, and I know how to make the upgrade plan testable before it touches a cluster."

- **`kafka-topic-auditor`** is the platform-hygiene repo. It signals "I know how to surface review evidence for risky platform actions like topic deletion, instead of automating them."

- **`mlops-factory`** is the practical-ML repo. It signals "I can design a training-to-serving boundary with FastAPI, MLflow, and Prometheus, and I know which parts of MLOps actually matter."

- **`ticket-triage-agent`** is the internal-developer-productivity repo. It signals "I can build deterministic, human-in-the-loop internal tooling with a sensible LLM fallback."

The six together say: "infrastructure automation + distributed systems + platform tooling + practical ML + EngProd thinking + a strong opinion about AI-assisted engineering."

## Per-repo plans

For each repo: skills used (Cognitive Deadlift), evidence inspected, what changed in this PR, what was intentionally not changed, what needs manual follow-up.

### 1. cognitive-deadlift

Skills used: problem-framing, assumption-audit, diff-interrogation, explain-without-ai, complexity-budget.

Evidence inspected: README, CATALOG.md, CONTEXT.md, ARCHITECTURE.md, AGENTS.md, CLAUDE.md, GEMINI.md, skills/, scripts/, tests/, Makefile, pyproject.toml.

Changed in #7 (already merged): repo contract enforcement, doc contract checker, skills-index drift check, generated-artifact tracking check, `make prod-gate`, doc reorganization.

Changed in #8 (already merged): em dashes, inline-colon prose lists, banned adverbs.

Intentionally not changed: skill bodies (graded A, no obvious problems). The paid-offer mention near the top of README has been re-evaluated; it stays high but follows engineering content. Acceptable.

Needs follow-up: add a sample `make prod-gate` output to the README so a reviewer can see what passes. Already noted in the user instructions.

### 2. infra-iac-refactor

Skills used: trace-the-code, read-the-docs-first, alternatives-before-code, complexity-budget.

Evidence inspected: `main.tf`, `variables.tf`, `providers.tf`, `modules/foundation/`, `tests/`, `.github/workflows/terraform.yml`, README.

What I found: README is clean and honest. CI runs `terraform fmt`, `validate`, `test`. Module has a foundation pattern. Tests exist.

What still needs manual follow-up (PR-sized):

- Add a second consumer example to `modules/` showing how to import `foundation`.
- Add at least one test that validates naming/tagging derivation under known inputs.
- Rename "What It Solves" → "Why centralize this" and add a "What I would not centralize" subsection.
- Replace "Limitations" framing with "Adapter work left before this could provision real AWS."

Not changed in this PR: Terraform code.

### 3. zk-rolling-upgrade

Skills used: trace-the-code, failing-test-first, assumption-audit, debugging-lab-notebook, explain-without-ai.

Evidence inspected: `zk_upgrade/models.py`, `zk_upgrade/orchestrator.py`, `zk_upgrade/cli.py`, `zk_upgrade/health.py`, `tests/`, `docs/runbook.md`, `.github/workflows/python-ci.yml`.

What I found: README explicitly calls it a simulator. Tests exist. CI runs ruff and pytest.

What still needs manual follow-up:

- Reframe "simulator" language as "local adapter boundary" per user instruction.
- Add a "Why leader-last matters" section explaining quorum risk.
- Verify the test set covers: follower-before-leader ordering, exactly-one-leader validation, failed health check stops rollout, dry-run does not mutate, invalid node list rejected.
- Document explicitly whether quorum-aware planning is implemented or an explicit non-goal.

Not changed in this PR: code.

### 4. kafka-topic-auditor

Skills used: trace-the-code, failing-test-first, assumption-audit, complexity-budget, explain-without-ai.

Evidence inspected: `auditor/client.py`, `auditor/report.py`, `auditor/models.py`, `auditor/cli.py`, `tests/`.

What I found: README is clean. Same template scaffold as ZK.

What still needs manual follow-up:

- Reframe "current client is a local mock" → "local deterministic adapter so the repo can be reviewed without a Kafka cluster."
- Differentiate from ZK README: use "topic hygiene as platform risk" framing, not "rolling upgrade orchestration".
- Add tests for: internal topics skipped, empty topic detection, stale topic detection, timezone-aware audit time, invalid offsets rejected, "candidate only, no delete" behavior, JSON output contract.
- Add an explicit "Delete safety" section (no deletion by default, output is review evidence, recommended approval workflow).

Not changed in this PR: code.

### 5. es-snapshot-migrator

Skills used: problem-framing, trace-the-code, assumption-audit, alternatives-before-code, complexity-budget.

Evidence inspected: `migrator/models.py`, `migrator/plan.py`, `migrator/cli.py`, `tests/`.

What I found: README is small and honest. Same template scaffold.

What still needs manual follow-up:

- Reframe "Elasticsearch APIs are simulated" → "Restore execution is out of scope; this repo focuses on the reviewable migration plan."
- Add tests for: included indices, excluded indices with reasons, size filters, age filters, invalid metadata, JSON manifest output.
- Differentiate the README opening so it doesn't read as the third entry in the same template family.

Not changed in this PR: code.

### 6. mlops-factory

Skills used: trace-the-code, failing-test-first, assumption-audit, complexity-budget, diff-interrogation, explain-without-ai.

Evidence inspected: `app/main.py`, `app/model_registry.py`, `app/monitoring/`, `infra/`, `ops/`, `Dockerfile`, `Makefile`, `tests/`, `.github/workflows/`.

**Real findings:**

- `app/main.py:82` returns `str(e)` to clients via `HTTPException(status_code=500, detail=str(e))`. This leaks Python exception detail to API clients.
- GitHub repo description is the worst slop in the portfolio: `production-ready platform... seamlessly deploy, monitor, and scale ML models`. Marketing voice the repo does not earn.
- README is grounded but long (7.6 KB). A reviewer skims; the README should be tightened.

What changes in this PR:

- Fix the `str(e)` leak in `app/main.py`. Log the full exception server-side, return a stable generic 500 detail to the client.
- Fix the GitHub repo description via `gh repo edit`.

What still needs manual follow-up:

- Trim the README. Replace "Architecture Overview" label, keep the ASCII diagram.
- Decide vs `orbital-factory-mlops`: archive orbital, keep mlops-factory.
- Add tests for: `/healthz`, `/infer`, `/metrics`, model-not-loaded behavior, `predict_proba` fallback behavior.
- Add a basic model card.
- Verify Docker workflow does not push on PRs.

### 7. orbital-factory-mlops

Skills used: alternatives-before-code, complexity-budget, trace-the-code, failing-test-first.

Evidence inspected: `app/main.py`, `app/drift/`, README, `tests/`, CI.

Decision: **archive on GitHub.** The drift logic is good but does not warrant a second pinned ML repo. Migrate the drift logic into `mlops-factory` as a follow-up if useful; otherwise let it stand as archived prior work.

Not changed in this PR: code. Archive action is in the user's "manual follow-up" list at the bottom.

### 8. policy-rag-agent

Skills used: assumption-audit, trace-the-code, failing-test-first, diff-interrogation, explain-without-ai.

Evidence inspected: `src/app.py`, `src/store/`, `tests/`, README.

What I found: README is clean and honest about being a public-safe demo. One `str(exc)` reference at `src/app.py:103` needs context (might be a logger call, not a client response).

What still needs manual follow-up:

- Verify line 103 of `src/app.py` is server-side logging only, not a client response.
- Add or strengthen tests for: citation validation, no-source refusal, low-confidence refusal, cache behavior, unsafe-answer pattern rejection.
- Add an access-control warning near the top of README: source-level authorization is not implemented; in-memory document store is local/demo only.
- Review CORS defaults.

Decision: keep public, unpinned. Different enough from `ticket-triage-agent` (RAG with refusal vs deterministic routing with confidence).

### 9. ticket-triage-agent

Skills used: problem-framing, trace-the-code, failing-test-first, assumption-audit, explain-without-ai, complexity-budget.

Evidence inspected: `src/app.py`, `src/middleware.py`, `tests/`, README, Makefile.

**Real findings:**

- `src/app.py:332` returns `f"Triage failed: {str(e)}"` to clients. Leaks Python exception detail.
- `src/middleware.py:63` logs `str(e)` — that is fine for logger context, but verify it never leaks into a response body.
- `src/app.py:203` returns `str(exc) if settings.debug else None` — that is correct (gated on debug flag). Leave.

What changes in this PR:

- Fix `src/app.py:332` to log internally and return a stable generic message.

What still needs manual follow-up:

- Verify tests for: /health, /ready, /queues, /triage, API-key enabled/disabled, low-confidence needs_review, correlation ID, validation errors, routing evaluation on local sample data.
- Add a routing-evaluation artifact (small confusion matrix or precision/recall by queue on local sample data).
- README should center the engineering case for routing-with-confidence + human-in-the-loop, not generic agent voice.

Decision: pin.

### 10. compliance-copilot

Skills used: alternatives-before-code, complexity-budget, assumption-audit, diff-interrogation.

Evidence inspected: `src/app.py`, README, `tests/`.

**Real findings:**

- 8 occurrences of `str(exc)` or `str(e)` in `src/app.py`. At least three of them are response-bound (`content={"error": "...", "detail": str(exc)}` at lines 139, 149, 245). These leak exception detail.
- Repo description on GitHub is empty.
- Name "copilot" reads as marketing if the mechanism is just PR risk scoring + redaction.

What changes in this PR:

- Fix the worst response-bound `str(exc)` leaks at lines 139, 149, 245.

What still needs manual follow-up:

- **Decision: rename to `pr-risk-scorer` (or similar) and demote to unpinned.** "Copilot" framing is generic. The redaction + scoring core is real engineering work and deserves a name that says what it does.
- Differentiate from ticket-triage-agent: this is about PR risk and redaction, not ticket routing.
- Add tests for: redaction patterns, secret-like values, XSS/input rejection, risk score categories, "no approval/rejection mutation".
- Add an honest "pattern-based redaction is not full DLP" disclaimer.

### 11. persistent-cognitive-infrastructure

Skills used: problem-framing, assumption-audit, complexity-budget, read-the-docs-first, trace-the-code, explain-without-ai.

Evidence inspected: README (6.2 KB), `services/`, `frontend/`, `deployments/`, `proto/`, CI workflows.

What I found: README has the right "what PCI is / what PCI is not" framing. Boundaries against chatbot/personal-assistant framing are explicit. README is long but earned.

What still needs manual follow-up:

- Verify the 5-minute local control-plane demo runs cleanly.
- Confirm CI passes: scaffold verification, service tests, frontend lint/build, npm audit, Helm render.
- Tone down the GitHub repo description (currently "Persistent Cognitive Infrastructure: a distributed runtime for context graphs, semantic events, cognition scheduling, reconciliation, and governed memory" — that sentence reads as a startup pitch).
- Keep "implemented" and "not implemented yet" sections accurate as the codebase grows.

Decision: keep public, do not pin yet. Pin only once a reviewer can clone and see the control-plane demo work end-to-end in five minutes.

## Recommended commit / PR shape (across repos)

Per-repo work is best as one PR per repo. The shape that minimizes review burden:

1. `cognitive-deadlift`: nothing new in this branch beyond the spec doc. Already in #7/#8.
2. `infra-iac-refactor`: one PR that adds the second consumer example + renames sections + adds a naming/tagging test.
3. `zk-rolling-upgrade`: one PR that reframes "simulator" language, adds "Why leader-last matters", and adds the five tests listed above.
4. `kafka-topic-auditor`: same shape as ZK but with topic-hygiene framing and delete-safety section.
5. `es-snapshot-migrator`: smaller PR with reframed limitations and the manifest tests.
6. `mlops-factory`: PR with the `str(e)` fix, README trim, and the additional API tests.
7. `orbital-factory-mlops`: archive PR with one final README commit pointing at mlops-factory.
8. `policy-rag-agent`: verify line 103, add refusal tests, CORS check.
9. `ticket-triage-agent`: `str(e)` fix + routing-evaluation artifact.
10. `compliance-copilot`: rename + demote PR (large), or just `str(exc)` fix + safety disclaimers if keeping the name.
11. `persistent-cognitive-infrastructure`: README description tweak + local demo verification.

## What ships in this branch

Code changes in this branch are limited to:

- `specs/public-portfolio-repo-review.md` (this file).

Code changes that ship in separate repos as part of this work:

- `mlops-factory` `app/main.py:82` — `str(e)` leak fix (PR opened against `mlops-factory`).
- `ticket-triage-agent` `src/app.py:332` — `str(e)` leak fix (PR opened against `ticket-triage-agent`).
- `compliance-copilot` `src/app.py` lines 139, 149, 245 — `str(exc)` leak fixes (PR opened against `compliance-copilot`).
- All 11 public repos: GitHub repo description updates via `gh repo edit` (no commit, just metadata).

## Manual follow-up the user must do in GitHub

I do not have access to change pinning, repo visibility, or branch protection through this session.

- Pin the six repos listed above (cognitive-deadlift, infra-iac-refactor, zk-rolling-upgrade, kafka-topic-auditor, mlops-factory, ticket-triage-agent).
- Archive `orbital-factory-mlops` if you agree with the recommendation.
- Decide on `compliance-copilot`: rename + demote, archive, or keep. The PR I open here fixes the security leak but does not rename.
- Run `gitleaks detect --no-banner` on each public repo locally and confirm no secrets in history.
- Verify branch protection on each pinned repo: at minimum, require status checks on `main` and disable force-push.
- Verify GitHub package visibility for any container packages that the docker workflows push.

## Loose ends and known gaps

- I did not run `terraform test` or `pytest` on every repo. Doing so requires per-repo setup. Recommended next-session pass.
- I did not run `gitleaks` or `trufflehog`. Recommended next-session pass.
- I did not verify the orbital-factory drift logic against mlops-factory's drift module. If orbital-factory has unique drift edge-case handling, fold it into mlops-factory before archiving.
- I did not run the PCI local demo. The CI workflows exist but I did not exercise them.

This document is the next state to refresh once each per-repo PR lands. Update the "Per-repo plans" sections in place as work ships.
