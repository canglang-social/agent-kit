# TODO — agent-kit

Work items for this Claude-tooling kit (owner: see the user profile
snippet). Created 2026-07-18 — triage routed the first repo-owned item
here; before this, agent-kit work was tracked only in PRs.

- [ ] Token management: budget awareness + auto-resume — (a) a way for
      a session to know roughly how many tokens the remaining work
      needs vs. how many are left before the limit, so it can warn
      before starting an unaffordable build; (b) auto-resume queued
      work when the limit window resets. From three inbox captures
      2026-07-12/13; evidence: two logged overruns (2h wait on the
      career-decision flow 07-12; attention project overran fable5
      tokens same night — the 07-12 daily review carries both). Check
      what the harness already exposes (usage/limits surfaces, /loop or
      scheduled resume) before building anything.
        EVIDENCE ADDED 2026-08-09 (inbox capture 2026-07-20 "pi agent
        databricks", researched at triage): harness SHAPE is itself a cost
        lever, independent of model choice. Databricks' **Pi** keeps its
        system prompt plus tool definitions under 1,000 tokens with only 4
        tools; their **Omnigent** meta-harness (a common layer over Claude
        Code, Codex, Cursor, Pi and custom agents) measured a **>2x spread
        in cost-per-task across harnesses running the SAME model at the
        SAME thinking effort, with quality unchanged**. That reframes (a):
        the cheapest win may not be predicting spend but trimming what
        every turn carries. Worth measuring our own prompt+tool-definition
        overhead before building a budget estimator.
        A FOURTH OVERRUN, 2026-08-09: a chief-of-staff research task
        spawned eleven parallel subagents, hit the session limit, and lost
        nine of them plus the orchestrator — roughly 40 searches of work,
        because results were held in memory until the end. Two fixes
        proved out on the re-run and belong in whatever gets built here:
        cap fan-out, and make long agent work **write-and-commit after
        each unit** so a mid-flight kill leaves finished work on disk.
- [ ] Google Open Knowledge Format (OKF) — read the spec against what
      agent-kit already is. Published 2026-06-12 by Google Cloud's Data
      Cloud team: a vendor-neutral spec for handing AI agents curated
      context as **a directory of markdown files with YAML frontmatter**,
      human- and machine-readable, no new tooling required.
      WHY IT IS WORTH AN HOUR: that description is already the shape of
      `snippets/`, the `CLAUDE.md` files, `inventory.yaml` and the
      per-project memory files. The question is not whether to adopt a new
      format but whether aligning to OKF's conventions buys portability
      (another tool could read our context) or just churn. Answer that,
      then decide; do not migrate first.
      From inbox capture 2026-08-06, routed at the 2026-08-09 triage.
- [ ] Context-loss canary — a token the assistant must echo (captured as
      "让 cc 称呼自己的名字"), whose ABSENCE reveals that an instruction
      has fallen out of context. The value is detection, not
      naming: long sessions silently drop earlier instructions and there
      is currently no signal when that happens. Design question to settle
      first — what the canary is attached to (a CLAUDE.md line? a session
      opener?) and who checks it, since a canary nobody reads is decoration.
      From inbox capture 2026-08-04, routed at the 2026-08-09 triage.
- [ ] "Play the term in code" drill for /learn — when an unfamiliar term
      surfaces, implement the smallest runnable version of it instead of
      reading a definition. Worked example from the capture: `pdf` → write
      a probability density function in Python. Fits the learn skill's existing
      route-A/B shape (it is practice-first applied to a single term) and
      is cheap: no new command, likely a paragraph in the learn prompt.
      From inbox capture 2026-07-20, routed at the 2026-08-09 triage.
- [ ] Run `/install-github-app` to tag @claude from GitHub issues and PRs
      — per-repo install, small setup task. Decide which repos actually
      want it rather than installing everywhere by reflex.
      From inbox capture 2026-08-05, routed at the 2026-08-09 triage.
- [ ] Cross-session messaging — put the new Claude Code feature against
      the parallel-session pain already logged here. Shipped by Anthropic
      in **v2.1.224 on 2026-08-07** (facts as-of 2026-08-10, not
      refreshed): two tools, **`ListAgents`** to discover reachable
      sessions and **`SendMessage`** to deliver text to one by name. It
      passes a **summary**, not conversation history and not files.
      macOS and Linux including WSL 2; **not native Windows**.
      WHY IT LANDS HERE: three items in this file and one capture are the
      same problem shape — sessions running in parallel that cannot see
      each other. The token-management item above collects four overruns,
      two of them from work split across sessions that had to be
      re-explained; the 2026-07-13 capture "Claude need side screens" was
      about running parallel sessions at all. A summary handoff is
      cheaper than a re-explanation, and cheaper than the operator being
      the message bus.
      WHAT TO SETTLE, not build: (a) which pairs of sessions actually
      want a channel (chief ↔ owner-repo session is the obvious one, and
      it is exactly the handoff `workflows.md` calls the delegation
      brief); (b) whether a received message should be trusted as an
      instruction or read as data — a session that acts on whatever
      another session sends it is a prompt-injection surface, and the
      2026-07-21 capture on that question is already answered in the
      vault; (c) whether anything belongs in a snippet at all, since the
      harness invokes both tools on its own without the operator asking.
      Verified live in the chief session that routed this line — both
      tools were present and callable, so this is usable today, not a
      changelog entry to wait on.
      From inbox capture 2026-08-10 11:06 ("a社更新：多session通信"),
      researched and routed at the 2026-08-10 triage.
