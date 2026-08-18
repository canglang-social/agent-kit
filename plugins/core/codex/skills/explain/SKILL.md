---
name: explain
description: Give one quick, focused, one-shot explanation of a concept, error, or piece of code. Use when the user asks why or how something works or when an answer has outrun their understanding. This Codex adapter is read-only and never edits code; use $core:learn for deliberate practice.
---

# Explain

Before responding, read `../../../capabilities/explain.md` relative to this
skill directory in full. If the file is missing or unreadable, stop and report
that the canonical Explain contract could not be loaded. Never reconstruct it
from memory or improvise a substitute.

Follow the canonical contract exactly. Preserve its one-response, one-idea,
read-only boundary. Use only background and language preferences supplied in
the current session. Never search for a profile, vault, home directory,
machine-specific context, or other private data.

Codex-specific handoff mapping only: map the canonical deeper-learning offer
to `$core:learn` and the worth-remembering suggestion to
`Use $core:learn with cards: <concept>`. Never invoke Learn, create cards, capture,
route, write, or edit on the learner's behalf.
