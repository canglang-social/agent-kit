---
name: about-me-example
description: Template for the user profile fragment in ~/.claude/CLAUDE.md — identity, language preference, knowledge-base conventions. Skills reference the profile instead of embedding personal data.
version: 0.2.0
tags: [profile, claude-md-fragment, template]
last-tested: 2026-07-10
---

<!-- Copy to snippets/about-me.md (gitignored — personal data never publishes)
and fill it in. Your copy is UPSTREAM — every other copy mirrors it. Flows:
1. Claude Code: @import it from ~/.claude/CLAUDE.md with one line
   (@/path/to/agent-kit/snippets/about-me.md) — live at every session.
2. claude.ai project knowledge: keep ONE Google Doc mirror of the body and
   paste updates into it (Google-native Docs can't be updated from disk).
   Add the doc's URL to your copy's header so the paste is one click away.
3. Record any other mirror in your copy's header checklist as you add it.
4. Drifted? Ask Claude Code to "check profile drift" — it can read each mirror
   and diff it against this upstream copy. -->

## About me (user profile)

- I'm <name>. In learning contexts treat me as <experience level and learning
  goals, e.g. "a motivated beginner who wants to understand WHY">.
- Language — THE single source of truth; prompts/skills read this instead of
  hardcoding a language rule: <your language rule, e.g. "reply bilingually BY
  DEFAULT in all chats, including Claude Code — each English paragraph followed
  by its <language> equivalent, matched in detail; pair key terms as term
  (translation) on first use; refine my English first if it has errors">.
  Exceptions: code, shell commands, commit messages, and file contents stay
  English-only; a trivial one-line confirmation may be English-only; drop to
  plain English when I ask.
- My knowledge base is <tool, e.g. a Logseq vault> at:
  `<absolute path to vault/notes>`
  - <where daily notes live + their naming scheme + what they capture, e.g.
    "journals/ — daily pages named yyyy_MM_dd.md; the capture point for session
    logs and flashcards">
  - <where topic pages live + how they're named + any reuse rule, e.g. "pages/
    — topic pages; reuse existing pages before inventing new ones">
- Learning skills (learn, explain) read this profile for language and vault
  location instead of hardcoding them.
