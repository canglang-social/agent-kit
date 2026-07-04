# agent-kit

Personal Claude Code plugin marketplace: reusable agent assets (skills,
subagents, MCP configs), git-versioned, installable into any of my projects.
See `spec.md` for scope and `CLAUDE.md` for conventions.

## Layout

- `.claude-plugin/marketplace.json` — marketplace manifest.
- `plugins/<name>/` — one directory per plugin.
  - `.claude-plugin/plugin.json` — plugin manifest (only this file lives here).
  - `skills/<skill>/SKILL.md` — invocable skills.
  - `agents/*.md` — subagents.
  - `.mcp.json` — MCP server configs (at plugin root).
- `prompts/` — raw copy-paste chat prompts (versioned, shared as text, not installed).
- `snippets/` — reusable CLAUDE.md fragments (reference library, not installed).
  `about-me.md` holds the user profile — it is gitignored (personal data
  never publishes); copy `about-me.example.md`, fill it in, and @import it
  from `~/.claude/CLAUDE.md` (one line:
  `@/path/to/agent-kit/snippets/about-me.md` — live at every session, no
  re-sync). Skills reference the profile (language, knowledge-base location)
  instead of embedding it.

## Install into a project

```text
/plugin marketplace add <path-or-git-url-of-this-repo>
/plugin install core@agent-kit
/reload-plugins
```

Note: from a session inside this repo, use `/plugin marketplace add ./` — the
trailing slash is required (bare `.` resolves against the parent directory and
fails). `/reload-plugins` is needed to apply a fresh install.

After editing assets locally:

```text
/plugin marketplace update agent-kit
/reload-plugins
```

## Add a new asset

1. Decide the destination:
   - Invocable by the agent → a skill: `plugins/<plugin>/skills/<name>/SKILL.md`.
   - Subagent → `plugins/<plugin>/agents/<name>.md`.
   - Copy-paste chat prompt → `prompts/<name>.md`.
2. Use kebab-case names; skill file is exactly `SKILL.md`.
3. Every asset carries required frontmatter:

   ```yaml
   ---
   name: kebab-case-name
   description: one line
   version: 0.1.0
   tags: [tag1, tag2]
   last-tested: YYYY-MM-DD
   ---
   ```

4. New plugin? Add `plugins/<name>/.claude-plugin/plugin.json` and register it
   in `.claude-plugin/marketplace.json`.
5. Validate JSON (`python3 -m json.tool <file>.json`), bump `version` on any
   behavior change, and commit.

## Deployed prompts — the repo is upstream

Chat prompts in `prompts/` are used by Claude Projects / Cowork projects.
Prefer the loader pattern (`snippets/deployment-loaders.md`): the deployed
instruction is a short pointer at the repo file, so editing here updates the
deployment (Cowork: next session; claude.ai: one knowledge re-sync click)
and the instruction itself never changes. If a surface can't reference the
repo and needs a pasted copy: **edit here first, bump `version`, re-paste**
— never tweak only the deployed copy; if a live session forces a quick fix,
port it back the same day. Either way, update `last-tested` after a real
session. Settings a prompt "confirms and remembers" (e.g. daily-review's
SETTINGS block) must be baked back into the deployed project instructions,
not left in chat memory. New prompts start from
`snippets/prompt-preamble.md`, the canonical language + profile block.

## Sharing

Private by default. To share a plugin, publish it (or this repo) to a location
of your choice; the marketplace entry's `source` decides what consumers pull.
No CI/publishing pipeline in v1.
