# spec.md — agent-kit (Personal Agent Asset Marketplace)

## Problem / Goal

I accumulate reusable Claude Code and Codex assets — prompts, skills, subagents, MCP
configs — scattered across projects. I want one git-versioned repository,
structured as a Claude Code plugin marketplace, that stores these assets,
versions them, lets me install them into my own projects, and lets me
selectively share some publicly.

## Goals

- Central, git-versioned home for my reusable agent assets.
- Structured as Claude Code and Codex plugin marketplaces so assets install natively.
- Standardize on skills for invocable assets (no legacy commands).
- Keep a plain `prompts/` library for copy-paste chat prompts (versioned,
  shared as text, not installed).
- Canonical versioned-asset metadata (version, tags, last-tested) in frontmatter.
- Selective sharing: private by default, flip chosen plugins public.
- Approved provider-neutral canonical behavior contracts may document an asset's
  behavior beside thin runtime loaders. Portable content alone is not runtime
  support: each runtime needs a real manifest, loader, and invocation path.
- A canonical contract is the provider-neutral behavior and version-lineage
  authority for its loader; Core Explain is defined in
  `plugins/core/capabilities/explain.md`. It contains no provider-specific
  command, selects no runtime, and authorizes no distribution. Its thin loaders
  are `plugins/core/agents/explain.md` for Claude and
  `plugins/core/codex/skills/explain/SKILL.md` for Codex. Loaders own
  trigger/discovery metadata, fail-closed loading, and runtime handoff syntax.
  Thin Codex adapter frontmatter intentionally contains only `name` and
  `description`; the referenced shared body/capability owns behavior versioning,
  and the Core manifests own installed-package versioning.
  For Explain only, supplied-context mapping never discovers a profile or vault.

## Non-Goals (frozen scope)

- Not an application or runtime — ships config/markdown assets, no product code.
- No `commands/` — skills only.
- No automated CI / publishing pipeline in v1.
- No multi-user governance, access control, or web UI.
- Not a general document store — Claude Code / agent assets only.
- No unsupported runtime parity, acceptance, promotion, or write authority
  follows from a canonical contract.
- No MCP server or external-account integration in the current catalog.

## Users

- Primary: me, across my own coding projects.
- Secondary: people I choose to share specific plugins with.

## Requirements / User Stories

- As owner, I can add a new asset (skill / subagent / MCP config) in the right
  plugin location and commit it.
- As a user of my own projects, I can `/plugin marketplace add <this repo>`
  then `/plugin install <plugin>` to pull assets in.
- As a Codex user, I can add this repo with `codex plugin marketplace add`,
  install Core with `codex plugin add core@agent-kit`, and invoke its skills.
- Each canonical versioned asset carries frontmatter metadata; thin Codex
  adapters carry only `name` and `description`.
- I can mark a plugin shareable without exposing the whole repo.
- As owner, I can save a raw chat prompt as a markdown file in `prompts/` and
  share it as plain text, without turning it into a skill.

## Acceptance Criteria

- Repo validates as a marketplace: `.claude-plugin/marketplace.json` present and
  loads via `/plugin marketplace add .`.
- `.agents/plugins/marketplace.json` exposes a valid Codex Core package, whose
  manifest version stays in lockstep with the Claude Core manifest.
- At least one plugin installs cleanly; its skills/agents are invocable.
- README catalogs two shared skills, Explain, six prompts, three snippets, hook
  behavior, and the explicit absence of MCP.
- Every canonical versioned asset has full required frontmatter; thin Codex
  adapters have the intentional `name` + `description` exception.
- README documents how to add an asset and how to install.

## Constraints

- Follow current Claude Code and Codex plugin/marketplace schemas.
- Kebab-case names; `SKILL.md` exact casing; component dirs at plugin root
  (not under `.claude-plugin/`).
- Runtime assets remain Markdown, JSON, and Codex YAML metadata. Python is
  permitted only under `tests/`; no application/runtime code or build step.

## Open Questions

- One starter plugin (`core`) vs split by domain now? Default: start with one.
- Migration: convert existing old commands to skills as they're added.
