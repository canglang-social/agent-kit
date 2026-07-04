---
name: deployment-loaders
description: Thin-loader instruction blocks — a deployment references its prompt in this repo instead of containing a pasted copy, so repo edits update the deployment
version: 0.1.0
tags: [prompting, deployment, template]
last-tested: 2026-07-04
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

Use for: ai-strategist, skincare-consultant, workout-coach. Via the GitHub
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
  CANNOT deliver it. Deliver it via ONE Google Drive doc (titled "about-me
  profile — Claude project knowledge") added to each claude.ai project's
  knowledge through the Drive connector — one doc serves all projects. The
  Drive doc is a MIRROR: the repo snippet stays upstream; when it changes,
  update the Drive doc and bump its "Last synced" line. Manual paste is the
  fallback where the Drive connector isn't available.
- The "say so and stop" clause makes a broken loader fail loudly. Without it,
  the model improvises a plausible-but-unversioned ghost prompt and you may
  not notice for weeks.
- The user profile in `~/.claude/CLAUDE.md` uses a stronger mechanism: an
  @import (`@<absolute path to agent-kit>/snippets/about-me.md`) — live at
  every session start, no sync step at all.
- `last-tested` in a prompt's frontmatter still gets bumped after a real
  session on the deployed surface; loaders don't change that convention.
