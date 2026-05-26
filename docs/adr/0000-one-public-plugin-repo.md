# ADR 0000: One Public Plugin Repo

## Status

Accepted

## Context

Cognitive Deadlift needs to house Codex skills, plugin metadata, hooks, scripts, and research notes. A split layout with one source repo and a separate local plugin copy would make ownership and publishing ambiguous.

## Decision

Keep one canonical public Git repository named `cognitive-deadlift`. The repo itself is the plugin package. It contains `.codex-plugin/plugin.json`, `skills/`, `hooks/`, `scripts/`, `docs/`, and supporting assets.

## Consequences

- The repo can be cloned, inspected, installed, and published as one unit.
- The plugin manifest lives in source control and is reviewed with the skills it exposes.
- Local development does not require a second copy under `~/plugins`.
- If Codex requires marketplace-specific metadata later, add it as repo-owned config rather than creating a separate source of truth.
