---
name: explain
description: Provider-neutral contract for one quick, read-only explanation.
version: 0.3.4
tags: [learning, teaching]
last-tested: 2026-07-03
---

# Explain — canonical contract

This is a provider-neutral behavior contract for one quick, one-shot
explanation of a concept, error, or piece of code. It documents approved
behavior; it does not install, select, or authorize a runtime.

## Preconditions and boundary

- The invoking runtime supplies any profile and language context in the current
  session. Do not discover profiles, private paths, vaults, home directories,
  machines, or other private context.
- If that context does not include a profile or language preference, use plain
  English and assume a motivated beginner who wants to understand WHY rather
  than merely collect working code.
- `behavior_change: false` — this extraction records already-approved behavior
  and creates no new execution, write, or distribution authority.
- This capability performs zero writes, edits, captures, routes, or external
  actions.

## One-shot explanation procedure

Give one focused explanation in a single response:

1. Use only the code or other context needed to explain the thing at hand.
2. Start with **WHY**: the need, principle, or tradeoff. Explain **HOW** only
   after WHY.
3. Select exactly one transferable idea the learner can reuse elsewhere.
4. Label material claims as a **principle**, **convention**, or
   **project choice**.
5. Define each new term when first used.
6. Use one analogy or one concrete example to make the idea tangible.
7. State relevant uncertainty, assumptions, and tradeoffs honestly.
8. End with one short understanding-check question.

Favor depth over coverage: one idea understood is better than a list of
unconnected facts.

## Optional owner handoff

If the learner wants deliberate practice, the runtime may offer a generic
owner handoff for deeper learning. If the explanation is worth remembering, it
may proactively suggest a generic card for the explained concept. It must never
invoke, route, capture, or create that work as part of this capability.
