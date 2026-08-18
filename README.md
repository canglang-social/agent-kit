# agent-kit

Personal Claude Code and Codex plugin marketplace: reusable agent assets,
git-versioned and installable into any project. Portable Markdown is runtime
support only where a real manifest and adapter expose it. See `spec.md` for
scope and `CLAUDE.md` for conventions.

## Layout

- `.claude-plugin/marketplace.json` — marketplace manifest.
- `.agents/plugins/marketplace.json` — Codex repo/team marketplace manifest.
- `plugins/<name>/` — one directory per plugin.
  - `.claude-plugin/plugin.json` — plugin manifest (only this file lives here).
  - `.codex-plugin/plugin.json` — Codex plugin manifest.
  - `skills/<skill>/SKILL.md` — shared invocable skills.
  - `codex/skills/<skill>/SKILL.md` — Codex-only skill adapters.
  - `agents/*.md` — subagents.
  - `capabilities/*.md` — provider-neutral behavior contracts consumed by a
    runtime adapter; they are not adapters or runtime support by themselves.
    For Core Explain, `plugins/core/capabilities/explain.md` is the behavior
    and version-lineage authority. Claude loads it through
    `plugins/core/agents/explain.md`; Codex loads it through
    `plugins/core/codex/skills/explain/SKILL.md`. Both fail closed. For Explain
    only, supplied context never discovers a profile or vault.
  - `.mcp.json` — MCP server configs when present. Core currently has no MCP.
- `prompts/` — raw copy-paste chat prompts (versioned, shared as text, not installed).
- `snippets/` — reusable CLAUDE.md fragments (reference library, not installed).
  `about-me.md` holds the user profile — it is gitignored (personal data
  never publishes); copy `about-me.example.md`, fill it in, and @import it
  from `~/.claude/CLAUDE.md` (one line:
  `@/path/to/agent-kit/snippets/about-me.md` — live at every session, no
  re-sync). Skills reference the profile (language, knowledge-base location)
  instead of embedding it.

## Install into a project

### Claude Code

```text
/plugin marketplace add <path-or-git-url-of-this-repo>
/plugin install core@agent-kit
/reload-plugins
```

Note: from a session inside this repo, use `/plugin marketplace add ./` — the
trailing slash is required (bare `.` resolves against the parent directory and
fails). `/reload-plugins` is needed to apply a fresh install.

### Codex

From a shell:

```sh
codex plugin marketplace add <path-or-git-url-of-this-repo>
codex plugin add core@agent-kit
```

The repo/team marketplace must be added explicitly. Start a new Codex task in
the target workspace after install so skill discovery starts cleanly.

Installed plugins are cached separately from the marketplace source. Updating
the marketplace alone does not replace the installed copy. After changing an
installed asset:

1. Bump the asset frontmatter `version` for a behavior change.
2. Bump both enclosing Core manifests in lockstep once per release whenever
   that release changes installed contents.
3. Validate, refresh the marketplace listing, and update the installed cache:

```text
claude plugin validate --strict plugins/core
claude plugin marketplace update agent-kit
claude plugin update core@agent-kit
```

Restart Claude Code after the update.

Verify that the enabled user installation is byte-for-byte equal to the source:

```sh
(
  set -eu
  installed_record=$(
    claude plugin list --json |
      jq -cer '[.[] | select(.id == "core@agent-kit" and .scope == "user" and .enabled)] |
        if length == 1 then .[0]
        else error("expected exactly one enabled user install of core@agent-kit")
        end'
  )
  source_version=$(jq -er '.version' plugins/core/.claude-plugin/plugin.json)
  installed_version=$(printf '%s' "$installed_record" | jq -er '.version')
  install_path=$(printf '%s' "$installed_record" | jq -er '.installPath')

  if [ "$source_version" != "$installed_version" ]; then
    printf 'Version mismatch: source=%s installed=%s\n' \
      "$source_version" "$installed_version" >&2
    exit 1
  fi

  diff -qr -x .DS_Store -x .in_use plugins/core "$install_path"
)
```

No output means both Claude's installed-version registry and cached files match
the source. Any error or listed path is release drift and must be resolved
before treating an edit as deployed.

## Complete catalog and invocation

Installed Core contains exactly two shared skill bodies plus Explain:

| Feature | Claude Code | Codex | Boundary |
| --- | --- | --- | --- |
| Learn | `/learn <topic>` or `/learn cards: <focus>` | `Use $core:learn to study <topic>` or `Use $core:learn with cards: <focus>` | Teaching only; production code is never edited. Vault access requires one exact owner-supplied path, human gates, and append-only writes. |
| Prompt Engineer | `/prompt-engineer <rough idea>` | `Use $core:prompt-engineer to improve <rough idea>` | Produces a prompt, not the underlying result; model-neutral by default. |
| Explain | `Use the core:explain agent to explain <concept>` | `Use $core:explain to explain <concept>` | One response, one transferable idea, read-only; adapters fail closed if the canonical contract is unavailable. |

The six files under `prompts/` are intentional file assets, not installed
skills. From a clean clone, use the exact pattern
`ask Codex to read <path> and follow it` with one of:

- `prompts/about-me.md`
- `prompts/hard-question.md`
- `prompts/life-talk.md`
- `prompts/prompt-engineer.md`
- `prompts/skincare-consultant.md`
- `prompts/workout-coach.md`

The three files under `snippets/` are also intentional file assets:

- `snippets/about-me.example.md` — public profile template; copy to the
  gitignored `snippets/about-me.md` and supply that private file explicitly.
  Explain never discovers it.
- `snippets/deployment-loaders.md` — Claude/Cowork loader guidance; it does not
  activate a Codex plugin.
- `snippets/prompt-preamble.md` — prompt-authoring fragment.

For any tracked snippet, `ask Codex to read <path> and follow it`. If a product
cannot read the clone, attach or paste the one selected prompt/snippet; no
automatic parity is claimed for file-inaccessible products.

`.codex/hooks.json` is a non-mutating `PostToolUse` contributor reminder: it
never edits, refreshes, reinstalls, or cachebusts. `.claude/settings.json`
retains the existing Claude marketplace-source refresh hook, which does not
update installed caches. MCP: none — Core has no `.mcp.json`, `mcpServers`
entry, or external-account dependency.

## Learning-card contract

New cards created by the `learn` skill carry `#card`, a broad topic tag, a
namespaced concept tag, and exactly one question-type tag: `#q/why`, `#q/how`,
or `#q/apply`. The skill does not retroactively alter historical vault cards to
normalize those tags.

## Add a new asset

1. Decide the destination:
    - Invocable by the agent → a skill: `plugins/<plugin>/skills/<name>/SKILL.md`.
    - Subagent → `plugins/<plugin>/agents/<name>.md`.
    - Provider-neutral behavior → a canonical capability:
      `plugins/<plugin>/capabilities/<name>.md`; pair it with the approved
      provider-specific adapter. The capability owns behavior, while the adapter
      owns only provider syntax and loading.
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

4. New dual-runtime plugin? Add both runtime manifests and register it in both
   marketplace files.
5. Validate the plugin (`claude plugin validate --strict plugins/<plugin>`),
   bump the asset `version` on behavior changes, and also bump the enclosing
   Core manifests in lockstep when that release changes installed contents.

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
