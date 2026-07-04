---
name: prompt-preamble
description: Canonical language + user-profile block for deployed chat prompts — the single source for wording that prompts otherwise re-state and drift apart
version: 0.1.0
tags: [prompting, profile, template]
last-tested: 2026-07-04
---

# Prompt preamble (canonical)

Every deployed chat prompt (Claude Project / Cowork project) needs the same
two rules: read the user profile before asking anything, and follow the
profile's language preference everywhere. Four prompts currently embed their
own near-copies of this wording; THIS file is the canonical version. When
writing a new prompt, paste the block below near the end (house style:
an `# INTERACTION & LANGUAGE` section). When editing an existing prompt,
sync its embedded copy to this wording rather than tweaking it in place.

## The block

```markdown
# INTERACTION & LANGUAGE

Read my user profile (project knowledge / account preferences) for who I am,
my context, and my language preference before doing anything else; do not
re-ask what it already answers.

Reply in my stated language preference; default to English if none is set.
If the preference is bilingual, apply it to the ENTIRE response — every
section, paragraph, and table — each unit in the first language immediately
followed by its translation, matched in tone and detail.
```

## Notes

- The profile this block points at is `snippets/about-me.md` (gitignored),
  pasted into `~/.claude/CLAUDE.md` and/or the deployment's project
  knowledge. The `about-me` interview prompt generates and maintains it.
- Prompts with domain-specific language settings (e.g. daily-review's
  JOURNAL_LANG vs CHAT_LANG split) keep those settings; this block only
  replaces the generic "what language do we talk in" wording.
