# CLAUDE.md — agent-kit

## Overview

This repo is a **Claude Code and Codex plugin marketplace** holding my reusable agent
assets (skills, subagents, MCP configs). Runtime assets are Markdown, JSON, and
Codex YAML metadata; Python is test-only. There is no application/runtime code.
Assets install through each runtime's plugin commands.
Provider-neutral Markdown is runtime support only when a real runtime manifest
and adapter expose it. We standardize on **skills** for invocable assets (no legacy `commands/`);
raw copy-paste prompts live in `prompts/`. See `spec.md` for scope.

## Ecosystem position

This repo is the tool layer of the owner's personal repo ecosystem
(full private map: forge/ECOSYSTEM.md) — one line each:

- agent-kit (this repo) — Claude installable components use `/plugin install`;
  Codex skills use `codex plugin marketplace add` plus `codex plugin add`;
  raw prompts/snippets remain explicit file assets and are not plugin-installed.
- forge — WHAT I've built: project registry, reuse
  extraction, scaffolding; indexes this repo like any other project.

`/glossary` is retired; it is not a current pipeline stage. Explain provides
quick, read-only explanations. Learn alone owns deliberate deeper practice and
cards. (No personal specifics here by design — this repo is public; see Do NOT
below.)

## Structure (map, not full tree)

- `.claude-plugin/marketplace.json` — marketplace manifest; lists `plugins/`.
- `.agents/plugins/marketplace.json` — Codex repo/team marketplace manifest.
- `plugins/<name>/.claude-plugin/plugin.json` — per-plugin manifest.
- `plugins/<name>/.codex-plugin/plugin.json` — Codex per-plugin manifest.
- `plugins/<name>/skills/<skill>/SKILL.md` — skills (prompts live here too).
- `plugins/<name>/agents/*.md` — subagents.
- `plugins/<name>/capabilities/*.md` — provider-neutral canonical behavior
  contracts loaded by an adapter; they do not themselves install or execute.
  For Core Explain, `plugins/core/capabilities/explain.md` is the sole behavior
  and version-lineage authority. Claude loads it through
  `plugins/core/agents/explain.md`; Codex loads it through
  `plugins/core/codex/skills/explain/SKILL.md`. Each adapter owns only runtime
  discovery, fail-closed loading, and handoff syntax. For Explain only, supplied
  context never discovers a profile or vault.
- `plugins/<name>/.mcp.json` — MCP configs when present. Core currently has no MCP.
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
- Add and install for Codex: `codex plugin marketplace add <path-or-git-url>`
  then `codex plugin add core@agent-kit`; start a new Codex task.
- Invoke Claude with `/learn <topic>`, `/prompt-engineer <idea>`, or
  `Use the core:explain agent to explain <concept>`.
- Invoke Codex with `Use $core:learn ...`, `Use $core:prompt-engineer ...`, or
  `Use $core:explain ...`.
- Raw prompts/snippets are not installed. From a clean clone,
  `ask Codex to read <path> and follow it`; file-inaccessible products require
  attaching or pasting that one selected asset.

## Asset frontmatter

Canonical versioned assets use the full frontmatter below. Thin Codex adapter
`SKILL.md` files intentionally use only `name` and `description`; their loaded
shared body/capability and the Core manifests are the version authorities.

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
- SemVer for each canonical versioned asset; bump on any behavior change.
- Also bump the enclosing plugin manifest once per release whenever that release
  changes installed contents. Keep Claude and Codex Core manifest versions in
  lockstep. Marketplace refresh and plugin update are separate operations.

## Do

- Read `spec.md` before adding scope.
- Author prompts as skills; component dirs at plugin root; keep only
  `plugin.json` inside `.claude-plugin/` or `.codex-plugin/`.
- Fill full frontmatter on canonical versioned assets; thin Codex adapters use
  only `name` and `description`.
- Decide per prompt: invocable by the agent → skill; copy-paste text → `prompts/`.

## Do NOT

- Do NOT add a `commands/` dir — skills only.
- Do NOT nest `skills/`, `agents/`, `.mcp.json` inside `.claude-plugin/`.
- Do NOT add application/runtime code — assets only.
- Do NOT invent manifest fields; `plugin.json` is strict-validated.
- Do NOT treat Claude `allowed-tools` as Codex enforcement; Codex sandbox and
  approvals are its permission boundary.
- Do NOT put personal data (names, emails, machine paths, vault locations) in
  tracked files — this repo is public and every asset must work verbatim for a
  stranger. Assets say "read the user profile" instead of embedding specifics;
  personal values live only in `~/.claude/CLAUDE.md` and the gitignored
  `snippets/about-me.md` (template: `snippets/about-me.example.md`).

## Gotchas

- New top-level component dir mid-session may not be watched — restart session.
- Codex loads newly installed or updated skills in a new task.
- Marketplace won't load a plugin missing `plugin.json` unless its entry sets
  `strict: false`.
