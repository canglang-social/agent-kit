---
name: about-me-example
description: Template for the user profile fragment in ~/.claude/CLAUDE.md — identity, language preference, knowledge-base conventions. Skills reference the profile instead of embedding personal data.
version: 0.1.0
tags: [profile, claude-md-fragment, template]
last-tested: 2026-07-03
---

<!-- Copy to snippets/about-me.md (gitignored — personal data never publishes)
and fill it in. Then @import it from ~/.claude/CLAUDE.md with one line:
@/path/to/agent-kit/snippets/about-me.md — live at every session, no re-sync.
Where @import isn't available (e.g. project knowledge), paste the body. -->

## About me (user profile)

- I'm <name>. In learning contexts treat me as <experience level and learning
  goals, e.g. "a motivated beginner who wants to understand WHY">.
- Language, in learning/teaching contexts (learn flow, explain agent, card
  writing): <language rule, e.g. "reply bilingually — English first, then
  <language>, matched in detail; pair key terms as term (translation) on first
  use">. Outside learning contexts, plain English is fine.
- My knowledge base is <tool> at:
  `<absolute path to vault/notes>`
  - <folder conventions: where daily notes live, naming scheme, where topic
    pages live and how they're named>
- Learning skills (learn, explain) read this profile for language and vault
  location instead of hardcoding them.
