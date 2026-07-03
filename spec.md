# spec.md — agent-kit (Personal Agent Asset Marketplace)

## Problem / Goal

I accumulate reusable Claude Code assets — prompts, skills, subagents, MCP
configs — scattered across projects. I want one git-versioned repository,
structured as a Claude Code plugin marketplace, that stores these assets,
versions them, lets me install them into my own projects, and lets me
selectively share some publicly.

## Goals

- Central, git-versioned home for my reusable agent assets.
- Structured as a Claude Code plugin marketplace so assets install natively.
- Standardize on skills for invocable assets (no legacy commands).
- Keep a plain `prompts/` library for copy-paste chat prompts (versioned,
  shared as text, not installed).
- Per-asset metadata (version, tags, last-tested) in frontmatter.
- Selective sharing: private by default, flip chosen plugins public.

## Non-Goals (frozen scope)

- Not an application or runtime — ships config/markdown assets, no product code.
- No `commands/` — skills only.
- No automated CI / publishing pipeline in v1.
- No multi-user governance, access control, or web UI.
- Not a general document store — Claude Code / agent assets only.

## Users

- Primary: me, across my own coding projects.
- Secondary: people I choose to share specific plugins with.

## Requirements / User Stories

- As owner, I can add a new asset (skill / subagent / MCP config) in the right
  plugin location and commit it.
- As a user of my own projects, I can `/plugin marketplace add <this repo>`
  then `/plugin install <plugin>` to pull assets in.
- Each asset carries frontmatter metadata (version, purpose, tags, last-tested).
- I can mark a plugin shareable without exposing the whole repo.
- As owner, I can save a raw chat prompt as a markdown file in `prompts/` and
  share it as plain text, without turning it into a skill.

## Acceptance Criteria

- Repo validates as a marketplace: `.claude-plugin/marketplace.json` present and
  loads via `/plugin marketplace add .`.
- At least one plugin installs cleanly; its skills/agents are invocable.
- Every committed asset has required frontmatter.
- README documents how to add an asset and how to install.

## Constraints

- Follow current Claude Code plugin/marketplace schema (verified vs
  docs.claude.com, Jul 2026).
- Kebab-case names; `SKILL.md` exact casing; component dirs at plugin root
  (not under `.claude-plugin/`).
- Markdown + JSON only; no build step.

## Open Questions

- One starter plugin (`core`) vs split by domain now? Default: start with one.
- Migration: convert existing old commands to skills as they're added.
