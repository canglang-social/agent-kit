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
