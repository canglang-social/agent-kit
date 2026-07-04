# CLAUDE.md — agent-kit

## Overview

This repo is a **Claude Code plugin marketplace** holding my reusable agent
assets (skills, subagents, MCP configs). It ships markdown/JSON config only —
no application code. Assets install into other projects via `/plugin`. We standardize on **skills** for invocable assets (no legacy `commands/`);
raw copy-paste prompts live in `prompts/`. See `spec.md` for scope.

## Ecosystem position

This repo is the tool layer of the owner's personal repo ecosystem
(full private map: ai-mission-control/ECOSYSTEM.md) — one line each:

- agent-kit (this repo) — HOW I work: reusable Claude Code assets,
  consumed everywhere via `/plugin install`, never file-copied into
  consumer repos.
- ai-mission-control — WHAT I've built: project registry, reuse
  extraction, scaffolding; indexes this repo like any other project.

Flow touching this repo: the `learn` skill is the deep-study stage of a
two-step learning pipeline — ai-mission-control's `/glossary` stages
terms upstream as a quick capture queue; both write to the same journal
at different depths. (No personal specifics here by design — this repo
is public; see Do NOT below.)

## Structure (map, not full tree)

- `.claude-plugin/marketplace.json` — marketplace manifest; lists `plugins/`.
- `plugins/<name>/.claude-plugin/plugin.json` — per-plugin manifest.
- `plugins/<name>/skills/<skill>/SKILL.md` — skills (prompts live here too).
- `plugins/<name>/agents/*.md` — subagents.
- `plugins/<name>/.mcp.json` — MCP configs (plugin root, NOT in .claude-plugin/).
- `prompts/` — raw chat prompts to copy-paste or share as text (not installed).
- `snippets/` — reusable CLAUDE.md fragments (reference library; not installed).

## Commands

- Add marketplace locally: `/plugin marketplace add ./` (trailing slash required;
  bare `.` resolves wrong and fails)
- Refresh after edits: `/plugin marketplace update agent-kit`
- Install a plugin: `/plugin install <plugin>@agent-kit`, then `/reload-plugins`
  to apply
- Reload after changes: `/reload-plugins`
- Validate JSON: `python3 -m json.tool <file>.json`

## Asset frontmatter (required on every asset)

    ---
    name: kebab-case-name
    description: one line
    version: 0.1.0
    tags: [tag1, tag2]
    last-tested: YYYY-MM-DD
    ---

## Conventions

- Kebab-case for all plugin/skill/agent names.
- Skill file is exactly `SKILL.md` (case-sensitive).
- Relative paths in manifests start with `./`.
- Quote YAML glob patterns: `"**/*.ts"`.
- SemVer for `version`; bump on any behavior change.

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
