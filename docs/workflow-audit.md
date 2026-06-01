# Workflow Audit

Some teams want help applying Cognitive Deadlift to their own AI-assisted
development workflow. This page describes that support without making it part of
the repo's core identity.

The repository is useful without this audit. The audit is for teams that want an
outside review of where AI-assisted work is losing judgment, evidence, or review
quality.

## Best Fit

- A small engineering team already using AI coding assistants.
- A team that sees faster code generation but weaker problem framing, diff review,
  debugging notes, or test discipline.
- A lead who wants concrete reasoning evidence in AI-assisted work, not a generic AI
  adoption workshop.

## Scope

The audit reviews workflow evidence and maps gaps to the repo's existing skill-retention
tools.

Typical inputs:

- Recent AI-assisted pull requests, tickets, or change writeups.
- Current review, debugging, or handoff practices.
- Existing gates such as tests, CI, checklists, or agent instructions.

Typical outputs:

- Reasoning evidence gap analysis.
- Recommended skill workflow for the team.
- Suggested thinking budget by task risk.
- Context-pack and harness recommendations.
- Short adoption plan for adding useful friction at review, debugging, or planning points.

## Not Included

- Security penetration testing.
- Production incident response.
- Private codebase implementation work.
- A guarantee that an AI assistant will follow every instruction perfectly.
- Commercial relicensing of repository content.

Commercial licensing or custom implementation can be scoped separately.

## First Contact

Contact the maintainer through the GitHub profile listed in `.codex-plugin/plugin.json`
with the subject `Cognitive Deadlift Workflow Audit`.

Include:

- Team size and primary AI coding assistants.
- The workflow you most want to improve: planning, debugging, code review, tests, or
  handoff.
- Whether sample pull requests or change writeups can be shared after an agreement is in
  place.

Do not send private source code, secrets, customer data, or proprietary incident details
in the first message.
