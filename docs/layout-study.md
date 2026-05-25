# Layout Study

The repo layout is adapted from public AI-agent skill/plugin repositories inspected on May 25, 2026.

## Repos Inspected

- `mattpocock/skills`
- `addyosmani/agent-skills`
- `obra/superpowers`
- `anthropics/claude-plugins-official`
- `ComposioHQ/awesome-claude-skills`
- `hesreallyhim/awesome-claude-code`
- `sickn33/antigravity-awesome-skills`
- `VoltAgent/awesome-agent-skills`
- `wshobson/agents`
- `ciembor/agent-rules-books`

## Layout Decisions

- Use a root `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, and `CHANGELOG.md`.
- Keep shared skills under `skills/*/SKILL.md`.
- Include runtime-specific root context files: `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`.
- Include plugin/extension manifests: `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `gemini-extension.json`.
- Include repo hygiene under `.github/`, including issue templates, pull request template, CODEOWNERS, dependabot, and validation workflow.
- Include local enforcement under `hooks/` and `scripts/`.
- Avoid package-manager files until the repo needs package-manager behavior.

## Dotfiles Included

- `.codex-plugin/`
- `.claude-plugin/`
- `.gemini/`
- `.github/`
- `.gitattributes`
- `.gitignore`
- `.markdownlint.json`
- `.pre-commit-config.yaml`
- `.python-version`
