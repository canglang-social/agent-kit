# CLAUDE.md — agent-kit

## Overview

This repo is a **Claude Code plugin marketplace** holding my reusable agent
assets (skills, subagents, MCP configs). It ships markdown/JSON config only —
no application code. Assets install into other projects via `/plugin`. Approved
provider-neutral canonical contracts may document behavior, but portable content
is not runtime support: Claude `/plugin` remains the sole current distribution
and runtime unless separately approved. We standardize on **skills** for invocable assets (no legacy `commands/`);
raw copy-paste prompts live in `prompts/`. See `spec.md` for scope.

## Ecosystem position

This repo is the tool layer of the owner's personal repo ecosystem
(full private map: forge/ECOSYSTEM.md) — one line each:

- agent-kit (this repo) — Claude Code plugin marketplace: holds my
  reusable agent assets (skills, subagents, chat prompts), consumed
  everywhere via `/plugin install`, never file-copied into consumer repos.
- forge — WHAT I've built: project registry, reuse
  extraction, scaffolding; indexes this repo like any other project.

`/glossary` is retired; it is not a current pipeline stage. Explain provides
quick, read-only explanations. Learn alone owns deliberate deeper practice and
cards. (No personal specifics here by design — this repo is public; see Do NOT
below.)

## Structure (map, not full tree)

- `.claude-plugin/marketplace.json` — marketplace manifest; lists `plugins/`.
- `plugins/<name>/.claude-plugin/plugin.json` — per-plugin manifest.
- `plugins/<name>/skills/<skill>/SKILL.md` — skills (prompts live here too).
- `plugins/<name>/agents/*.md` — subagents.
- `plugins/<name>/capabilities/*.md` — provider-neutral canonical behavior
  contracts loaded by an adapter; they do not themselves install or execute.
  For Core Explain, `plugins/core/capabilities/explain.md` is the sole behavior
  and version-lineage authority; `plugins/core/agents/explain.md` is the sole
  current Claude runtime loader. The canonical contract does not select a
  runtime or name Claude commands. The loader owns Claude trigger/discovery
  metadata, mirrored version metadata, model/tools, fail-closed loading,
  supplied-context mapping, and `/learn` syntax. For Explain only, that mapping
  uses only session-supplied context and never discovers a profile or vault.
- `plugins/<name>/.mcp.json` — MCP configs (plugin root, NOT in .claude-plugin/).
- `prompts/` — raw chat prompts to copy-paste or share as text (not installed).
- `snippets/` — reusable CLAUDE.md fragments (reference library; not installed).

## Commands

- Add marketplace locally: `/plugin marketplace add ./` (trailing slash required;
  bare `.` resolves wrong and fails)
- Refresh the marketplace listing after edits: `claude plugin marketplace update agent-kit`
- After bumping the manifest, update the installed cache:
  `claude plugin update core@agent-kit`, then restart Claude Code
- Install a plugin: `/plugin install <plugin>@agent-kit`, then `/reload-plugins`
  to apply
- Verify source matches the installed cache with the parity command in README.
- Validate the plugin and marketplace: `claude plugin validate --strict plugins/core`
  and `claude plugin validate --strict .`

## Asset frontmatter (required on every asset)

    ---
    name: kebab-case-name
    description: one line
    version: 0.1.0
    tags: [tag1, tag2]
    last-tested: YYYY-MM-DD   # only where a real session can be said to have
                              # happened: prompts with a cadence, role
                              # doctrines. Audited by ai-chief-of-staff, which
                              # warns when the newest commit postdates it.
                              # Omit on always-live files (an @imported
                              # snippet can never honestly go stale).
    ---

## Conventions

- Kebab-case for all plugin/skill/agent names.
- Skill file is exactly `SKILL.md` (case-sensitive).
- Relative paths in manifests start with `./`.
- Quote YAML glob patterns: `"**/*.ts"`.
- SemVer for each asset `version`; bump on any behavior change.
- Also bump the enclosing plugin manifest once per release whenever that release
  changes installed contents. Marketplace refresh and plugin update are separate
  operations.

## Do

- Read `spec.md` before adding scope.
- Author prompts as skills; component dirs at plugin root; keep only
  `plugin.json` inside `.claude-plugin/`.
- Fill frontmatter metadata on every new asset.
- Decide per prompt: invocable by the agent → skill; copy-paste text → `prompts/`.

## Do NOT

- Do NOT add a `commands/` dir — skills only.
- Do NOT nest `skills/`, `agents/`, `.mcp.json` inside `.claude-plugin/`.
- Do NOT add application/runtime code — assets only.
- Do NOT invent manifest fields; `plugin.json` is strict-validated.
- Do NOT put personal data (names, emails, machine paths, vault locations) in
  tracked files — this repo is public and every asset must work verbatim for a
  stranger. Assets say "read the user profile" instead of embedding specifics;
  personal values live only in `~/.claude/CLAUDE.md` and the gitignored
  `snippets/about-me.md` (template: `snippets/about-me.example.md`).

## Gotchas

- New top-level component dir mid-session may not be watched — restart session.
- Marketplace won't load a plugin missing `plugin.json` unless its entry sets
  `strict: false`.
