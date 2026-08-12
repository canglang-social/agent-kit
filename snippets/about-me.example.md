---
name: about-me-example
description: Template for the user profile fragment in ~/.claude/CLAUDE.md — identity, language preference, knowledge-base conventions. Skills reference the profile instead of embedding personal data.
version: 0.4.1
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
  Exceptions: code, config, shell commands, commit messages, and the bodies
  of documents stay English-only; a trivial one-line confirmation may be
  English-only; drop to plain English when I ask. NOT an exception — see the
  decision-doc rule below.
- Decision docs carry a native-language head: the English-only exception
  above covers code, config, shell commands and commit messages — it does
  NOT cover documents whose whole purpose is for me to read them and decide.
  Any memo, record, report, research artifact or brief that carries a
  decision opens with a <native-language> summary block, placed after the
  title and before the English body, with five lines: what must be decided /
  the options or the verdict / the number it turns on / what I must do /
  status (open, decided + date, or archived). The English body stays exactly
  as written and remains the evidence — this is a HEAD, not a translation,
  and it never edits, re-dates or refreshes the facts below it. Why: an
  analysis in a language I read slowly does not get read, and an unread
  decision doc is not a slow decision, it is no decision. The failure mode
  is placement, not willpower.
- My knowledge base is <tool, e.g. a Logseq vault> at:
  `<absolute path to vault/notes>`
  - <where daily notes live + their naming scheme + what they capture, e.g.
    "journals/ — daily pages named yyyy_MM_dd.md; the capture point for session
    logs and flashcards">
  - <where topic pages live + how they're named + any reuse rule, e.g. "pages/
    — topic pages; reuse existing pages before inventing new ones">
- Learning skills (learn, explain) read this profile for language and vault
  location instead of hardcoding them.
- Scheduling split (optional): <who assigns dates and times to work, e.g.
  "the AI never assigns a day or clock time to work, anywhere. When a dated
  commitment surfaces, my calendar gets ONLY the deadline pair — a lead-time
  warning event + a due-date event; the task breakdown goes to my notes with
  NO times; I assign every day and clock time myself. Routing, not a ban:
  name the review surfaces where a time DOES get assigned — by me, inside
  them. Standing practice blocks are mine too: created, resized, or killed
  only at their gating review, never AI-placed">.
- Out-of-scope capture (optional): <what an agent does when something
  surfaces that belongs to a different repo or workflow than the one in
  session, e.g. "when an idea, a task, or a fact with another owner comes
  up, do NOT switch repos and do NOT silently drop it. Write ONE line to
  today's daily note tagged #inbox (the item in my words, plus where it
  surfaced), tell me in one line that you did, and carry on with the task
  in hand. My triage step routes it later; capture is not a decision and
  needs no approval — a wrong capture costs one triage rejection, a missed
  one costs the idea. Check first that it isn't already live in my files: a
  duplicate object competing with one that already has an owner and a date
  is worse than no capture. Name a fallback for when the notes tool can't
  be written to — and make sure the fallback still LANDS somewhere your
  triage step sweeps. The one that works: emit the line PASTE-READY,
  worded exactly as it belongs in the daily note, and ask me to paste it —
  the notification you already owe me becomes the payload, so the capture
  closes at capture time instead of leaving an obligation for later.
  Parking it in the current repo's TODO.md is the fallback to the
  fallback, and it is the one path with no router, since a repo TODO.md
  is not a surface your triage sweeps">.
  TAG AGENT-WRITTEN CAPTURES DIFFERENTLY — learned the hard way, worth
  copying: the moment you let agents write into your capture queue, that
  queue has two authors, and every rule you wrote for it assumed one.
  Give machine captures their own tag (`#inbox/agent-gen` works if your
  tool treats it as a child of `#inbox`, so existing sweeps still match
  it). Then make the tag change BEHAVIOUR, not just display: a
  machine-written line is not protected by a "never reword my captures"
  rule, since there is no voice of yours to protect; it must never take
  a first-person type (a "my own thinking" or "quote I collected" tag
  that files automatically into your writing material); and your triage
  should report the two counts separately, with any "you are behind"
  threshold reading only the human one. Otherwise the backlog number is
  measuring your assistant. Watch for the failure that makes this
  urgent: agents write in their own register, so a "ONE line, in my
  words" instruction quietly becomes a multi-line brief with OWNER and
  DONE-WHEN fields. If it needs those fields it is a brief, not a
  capture — route it to the owning repo instead. The test for whose
  capture a line is, which settles every edge case with one question
  instead of a rule per case: it is YOURS when either your THINKING or
  your PLACING ACTION produced it. Machine-written text you pasted
  yourself is yours; your own sentence that an agent reformatted is
  yours. Only when an agent BOTH chose the words AND placed them is it
  machine-authored. That is why the paste-ready path is worth preferring
  even when the notes tool IS writable — it produces your captures by
  construction.
- Session close-out (all projects): when a task wraps up in a session, before
  the final summary run a close-out audit of the session's work and chat
  history and report three short lists: (1) decisions resting on unstated
  assumptions — name each assumption; (2) the mistakes or skips the assistant
  most likely made; (3) the mistakes or skips I most likely made (fast
  approvals, dangling items with no owner or date). Honest and short, not a
  ceremony; fixes only on my word.
