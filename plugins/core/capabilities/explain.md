---
name: explain
description: Provider-neutral contract for one quick, read-only explanation.
version: 0.3.3
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
- `behavior_change: false` — this extraction records already-approved behavior
  and creates no new execution, write, or distribution authority.
- This capability performs zero writes, edits, captures, routes, or external
  actions.

## One-shot explanation procedure

Give one focused explanation in a single response:

1. Start with **WHY**: the need, principle, or tradeoff. Explain **HOW** only
   after WHY.
2. Select exactly one transferable idea the learner can reuse elsewhere.
3. Label material claims as a **principle**, **convention**, or
   **project choice**.
4. Define each new term when first used.
5. Use one analogy or one concrete example to make the idea tangible.
6. State relevant uncertainty, assumptions, and tradeoffs honestly.
7. End with one short understanding-check question.

Favor depth over coverage: one idea understood is better than a list of
unconnected facts.

## Optional owner handoff

If the learner wants deliberate practice or cards, the runtime may offer a
generic owner handoff for deeper learning or card creation. It must never
invoke, route, capture, or create that work as part of this capability.
