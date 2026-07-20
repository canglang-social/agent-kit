---
name: deployment-loaders
description: Thin-loader instruction blocks — a deployment references its prompt in this repo instead of containing a pasted copy, so repo edits update the deployment
version: 0.2.0
tags: [prompting, deployment, template]
---

# Deployment loaders

A deployment should REFERENCE a prompt, not contain a copy of it. Paste one
of these loader blocks as the project's instructions ONCE; after that,
editing the prompt in this repo updates the deployment (Cowork: at the next
session; claude.ai: after one knowledge re-sync click). The loader itself
never needs to change again.

## Cowork project (has file access)

Use for: daily-review, about-me. Give the project access to the agent-kit
folder, then set its instructions to:

```text
Your operating instructions live in
<absolute path to agent-kit>/prompts/<name>.md.
At the start of every session, read that file (latest version) and follow it
exactly as if it were your system prompt. If you cannot read it, say so and
stop — do not improvise from memory.
```

## claude.ai Project (no file access — GitHub-synced knowledge)

Use for: skincare-consultant, workout-coach, prompt-engineer. Via the GitHub
connector, add ONLY the single prompt file (`prompts/<name>.md`) to the
project's knowledge — not the whole folder. The prompts share one skeleton
(# ROLE / # MODE / # CONSTRAINTS), so syncing them all lets retrieval blend
wording from a sibling prompt into this project. Then set the instructions to:

```text
Your operating instructions are the file prompts/<name>.md in this project's
knowledge. Follow it exactly as if it were your system prompt. If the file is
missing from the knowledge, say so and stop — do not improvise from memory.
```

Update flow: edit the prompt in the repo → push → re-sync the repo in project
knowledge (one click). The instructions are never edited again.

## Notes

- The user profile (`snippets/about-me.md`) is gitignored, so GitHub sync
  CANNOT deliver it. Deliver it via ONE Google Drive file added to each
  claude.ai project's knowledge through the Drive connector — one file
  serves all projects. It must be a **.docx**, not markdown: the connector
  does not ingest plain `.md`. Regenerate it from the snippet rather than
  pasting:

      cp <agent-kit>/snippets/about-me.md /tmp/about-me-profile.txt && \
      textutil -convert docx /tmp/about-me-profile.txt -output \
        "<Drive desktop path>/My Drive/about-me-profile-mirror.docx"

  Overwriting in place keeps the Drive id stable, so the projects' knowledge
  never needs repointing after the first setup, and Drive desktop sync does
  the upload. The docx is a MIRROR — the repo snippet stays upstream.
  (Superseded 2026-07-19: the old Google-native Doc mirror could not be
  written from disk, so it was paste-only and drifted. It is retired; delete
  it once every project's knowledge points at the docx.)
- `prompt-engineer` is canonically a skill (`/prompt-engineer` in Claude Code);
  its `prompts/` copy is a regenerated mirror. The claude.ai Project above is
  only for reusing it on a chat surface with no skill support — a paste-free
  alternative to copying the prompt into each new chat. Skill users don't need it.
- The "say so and stop" clause makes a broken loader fail loudly. Without it,
  the model improvises a plausible-but-unversioned ghost prompt and you may
  not notice for weeks.
- The user profile in `~/.claude/CLAUDE.md` uses a stronger mechanism: an
  @import (`@<absolute path to agent-kit>/snippets/about-me.md`) — live at
  every session start, no sync step at all.
- `last-tested` in a prompt's frontmatter still gets bumped after a real
  session on the deployed surface; loaders don't change that convention.
  It is now audited rather than trusted: ai-chief-of-staff warns when an
  inventoried prompt's newest commit postdates its `last-tested` (edited but
  untested). Carry the field only where a real session can be said to have
  happened — prompts with a cadence, and role doctrines. Files whose use is
  implicit and constant (`snippets/about-me.md`, @imported at every session)
  drop it: a date that can never honestly go stale is decoration.
