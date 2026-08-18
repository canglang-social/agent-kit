# Agent Kit contributor instructions

Read `spec.md` before changing scope. This public repository ships Markdown,
JSON, and Codex YAML metadata; Python is allowed only for repository tests.
Do not add application/runtime code, private payloads, owner-specific machine
paths, or vault contents.

## Runtime map

- `plugins/core/skills/learn/SKILL.md` and
  `plugins/core/skills/prompt-engineer/SKILL.md` are the sole behavior bodies.
  Codex reaches them through fail-closed thin loaders under
  `plugins/core/codex/skills/`; Claude loads them directly. Preserve the Claude
  frontmatter and keep the shared bodies runtime-neutral.
- `plugins/core/capabilities/explain.md` is the canonical Explain behavior.
  Claude's adapter is `plugins/core/agents/explain.md`; Codex's adapter is
  `plugins/core/codex/skills/explain/SKILL.md`. Adapters load the canonical
  file and fail closed; they must not duplicate its procedure.
- Thin Codex adapter `SKILL.md` frontmatter intentionally contains only
  `name` and `description`. The referenced shared body or capability owns the
  behavior version; both Core manifests own the installed package version.
- `prompts/` and `snippets/` are explicit file assets. They are not installed
  or automatically activated by either plugin runtime.
- There is no MCP server in this repository.

## Safety and release rules

- Explain is one-shot and read-only. It never discovers a profile or vault.
- Learn accepts profile data only from the current session or governing
  `AGENTS.md` / `CLAUDE.md` instructions supplied to it. Vault access requires
  an exact owner-supplied path. Keep card selection/review human-gated, writes
  append-only, and production-code writes forbidden.
- Claude's `allowed-tools` frontmatter is a Claude adapter. Codex sandbox and
  approval prompts are the Codex enforcement boundary.
- Bump the canonical behavior asset SemVer for behavior changes; thin Codex
  adapter frontmatter carries no duplicate version. Keep
  `plugins/core/.claude-plugin/plugin.json` and
  `plugins/core/.codex-plugin/plugin.json` at the same Core version.
- `.codex/hooks.json` is reminder-only. Never make it edit, reinstall,
  refresh, cachebust, or deploy automatically.

## Checks

Run `python3 -m unittest discover -s tests -v`, both available runtime/plugin
validators, the Codex Explain skill validator, and `git diff --check`. Test
with synthetic content only; never inspect a private profile or vault.
