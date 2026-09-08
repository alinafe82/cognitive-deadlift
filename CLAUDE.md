# Claude adapter

Follow [AGENTS.md](AGENTS.md) for repository work. `.claude-plugin/plugin.json` is the runtime manifest; [skills_index.json](skills_index.json) lists shared skill paths. Read a selected `skills/<name>/SKILL.md` only when that workflow applies. Do not copy skill bodies or force all tasks through the catalog.

Use the session's configured model unless the user requests a change. Static manifest checks establish path consistency, not proof that this runtime loaded or executed a skill. Report actual runtime smoke evidence separately.
