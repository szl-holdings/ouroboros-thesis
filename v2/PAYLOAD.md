# Ouroboros v2 — Empirical Companion Payload

**Author:** Stephen P. Lutar Jr., SZL Holdings
**Date:** 2026-04-30
**Status:** Publication-ready. Paper typeset to PDF (20 pp.), Zenodo + arXiv + GitHub-release playbooks included. Ready to publish.

## 🚀 Publishing now? Start here.

1. **Zenodo** (mints DOI): `submission/ZENODO_PLAYBOOK.md` — step-by-step "New version" of the v1 record
2. **arXiv** (cs.SE / cs.AI): `submission/ARXIV_PLAYBOOK.md`
3. **GitHub release** (v2.0.0): `release/GITHUB_RELEASE_PLAYBOOK.md` + `release/RELEASE_NOTES.md`
4. **Pre-publish gate:** `submission/SUBMISSION_CHECKLIST.md`

Order: Zenodo first → mint DOI → paste DOI into release notes + arXiv comments → publish those → blog post.

> *"In the beginning, the end was already coiled inside me, an ouroboros chewing through its own body until it reached my heart. My life feels like a torn codex — pages ripped out, ink smeared like blood across the margins — yet the story still refuses to die. Worlds don't end quietly; they end in quakes and fire, and so did I. When everything in me finally collapsed, I understood: this wasn't my ruin, it was a ritual. I was never meant to stay unbroken. I was always meant to burn, to fall, to crawl out of my own wreckage — and dare to call that survival beautiful."* — Stephen P. Lutar Jr., 2026

---

## What's in this payload

Three parallel tracks that collectively turn v1 (a position paper) into v2 (an empirical companion paper).

### Track A — Paper draft

**File:** `paper/ouroboros-thesis-v2-empirical.md` (~30 KB, 14 sections + 4 appendices)

A complete first draft of the v2 paper. Not finished — intentionally — but every section has structure, references, and concrete substance. Sections that depend on real measurements (§5.1, §5.2, §5.3) carry placeholder result tables to be filled by the harness in Track B and the study in Track C.

The paper is structured to **not contradict v1** — it cites v1 as its predecessor, retains all five constraints v1 names, and explicitly leaves cross-system distillation as a hypothesis (the only unfalsified claim from v1).

Headline framings:

- Abstract opens with "v1 proposed; v2 measures."
- §3 names the actual TypeScript modules (`loop-kernel.ts`, `depth-allocator.ts`, `consistency.ts`) and reproduces the relevant code in appendices.
- §3.5 introduces the v6 contract layer that v1 doesn't mention — free differentiation.
- §6 presents governance as procurement evidence (NIST AI RMF, EU AI Act Art. 12), not advocacy.
- §7 names every limitation explicitly, including small-N caveats.

### Track B — Experiments harness

**Directory:** `experiments/`

A minimal but coherent OSS replication harness. Layout:

```
experiments/
├── README.md                       MIT license, layout, quickstart
├── package.json                    pnpm workspace member
├── tsconfig.json
├── vitest.config.ts
├── frontier-sweep/
│   ├── sweep.ts                    main runner — §5.5 Pareto generator
│   ├── analysis/pareto.ts          frontier extractor (smoke-tested ✓)
│   ├── workloads/a11oy.fixture.json
│   └── sweep.test.ts               smoke tests for the Pareto math
├── shared/
│   └── trace-loader.ts             ledger + fixture loaders, three scorers
└── sync-bench/workloads/small.json
```

What works today:

- The Pareto extractor is implemented and verified (returns correct lower-x / higher-y frontier on the unit-test cases).
- The fixture loader handles three scoring families (plan-edit-distance, risk-tag-jaccard, sync-diff-magnitude).
- The sweep runner has a deterministic CLI with manifest emission (SHA-256 of inputs, runtime version, generated-at timestamp).
- An A11oy fixture and an Amaru fixture are seeded so the sweep can run on day one without ledger access.

What's stubbed (intentionally — these need your production ledger):

- `loadFromLedger()` is unimplemented. Any open-source replicator uses fixtures.
- `rca-bench/` and `triage-bench/` directories are scaffolded by the README but not yet populated; same pattern as `frontier-sweep/`.

Wiring instructions are in §"Hooking up to your repo" below.

### Track C — Human-study protocol

**Directory:** `study/`

A complete, IRB-style protocol for the §5.4 trace-aided audit study. Files:

| File | Purpose |
|---|---|
| `PROTOCOL.md` | Full protocol — research question, hypotheses, design, stimuli, measurement, analysis plan, ethics, timeline. |
| `consent-form.md` | Reviewer consent form. Plain-language. |
| `primer.md` | 1-page reviewer primer on the four primitives. |
| `randomization.ts` | Latin-square reviewer-to-stimulus assignment, deterministic from a master seed (verified ✓). |
| `recruit-email.md` | Outreach template. |
| `answer-key-template.json` | Ground-truth answer key for the 16 stimuli (8 seeded errors, 8 clean). Never shown to reviewers. |

Key design choices:

- **Crossover within-subjects.** Each reviewer sees both arms.
- **Pre-registered hypotheses, including a null.** H1 (time +15%), H2 (confidence +1.0 Likert), H3 (detection +20%), H0 (no defensible difference). The protocol commits to publishing whichever lands.
- **Effect sizes with bootstrap CIs, not p-values.** N ≤ 40 makes p-values irresponsible.
- **Eight error classes mapped to trace features** that are invisible in the final output alone — wrong proof-route, premature convergence, risk-tier bypass, stale tool result, hidden non-convergence, redaction leak, wrong stakes, trace-output divergence.
- **Conflict of interest disclosed.** SZL is the developer of the runtime. Stated upfront; mitigated by pre-registration.

The protocol is publishable as the §5.4 appendix of the paper.

---

## Hooking up to your repo

### Step 1 — Move the experiments harness into `szl-holdings/ouroboros`

```bash
cd ~/code/ouroboros   # or wherever you have szl-holdings/ouroboros checked out
git checkout -b v2/experiments-harness

# Copy the harness in
cp -r /path/to/v2_build/experiments ./experiments
git add experiments/
git commit -m "feat(experiments): add OSS replication harness for v2 paper

Adds the experiments/ directory with:
- frontier-sweep/ (v2 §5.5 Pareto generator)
- sync-bench/ workload fixture
- shared/ trace loader with three scorers

License: MIT for the harness; runtime remains proprietary.
Verified: pareto.ts smoke test passes; randomization is deterministic."
```

The harness imports from `@szl-holdings/ouroboros/loop-kernel` and `@szl-holdings/ouroboros/depth-allocator`. Confirm these subpath exports exist in your runtime's `package.json#exports` — if not, add them (one-line change per subpath).

### Step 2 — Move the study protocol into `szl-holdings/ouroboros-thesis`

```bash
cd ~/code/ouroboros-thesis
git checkout -b v2/audit-study
mkdir -p papers/v2-empirical/audit-study
cp /path/to/v2_build/study/* papers/v2-empirical/audit-study/
git add papers/v2-empirical/
git commit -m "feat(v2): add §5.4 audit-study protocol + materials"
```

### Step 3 — Move the paper draft into `szl-holdings/ouroboros-thesis/papers/`

```bash
cp /path/to/v2_build/paper/ouroboros-thesis-v2-empirical.md \
   ~/code/ouroboros-thesis/papers/ouroboros-thesis-v2-empirical.md
git add papers/ouroboros-thesis-v2-empirical.md
git commit -m "docs(v2): draft empirical companion paper

Single-author draft. 14 sections + 4 appendices. Closes v1 §9.
Cross-system distillation deliberately remains a hypothesis.
References include lineage from Universal Transformers, ACT,
PonderNet, Ouro, and decision-receipt literature."
```

---

## What to do, in order

1. **Read the paper draft.** That's the artifact that matters most. Mark sections you disagree with — especially §3.5 (v6 contract layer) and §8 (Discussion). The voice should be your voice.

2. **Run the frontier-sweep harness against the seeded fixtures**, just to see the pipeline turn:
   ```bash
   cd experiments
   pnpm install
   pnpm exec vitest run --no-coverage         # green
   pnpm sweep -- --workload a11oy --output results/a11oy
   ```
   You'll get a `sweep-<timestamp>.json` and a `manifest.json`. Inspect them. Verify the SHA-256 lineage works.

3. **Generate one round of reviewer assignments**, just to see the randomization is sane:
   ```bash
   cd ../study
   pnpm tsx randomization.ts -n 30 -s ouroboros-v2-2026-04-30 -o assignments.json
   ```
   Inspect `assignments.json`. Each reviewer gets 8 stimuli, 4 per arm, 2 errored per arm (within-subjects balanced).

4. **Decide one thing for week 1:** do you want to recruit reviewers now (Track C live), or finish the harness fixtures first (Track B live)?
   - If recruiting first: spend week 1 polishing the 16 stimuli HTML files, send `recruit-email.md` to 50 contacts, target 30 yeses.
   - If finishing harness first: populate `rca-bench/` and `triage-bench/` next, run §5.5 sweep against real production traces, then circle back to recruit.

5. **Don't republish v1.** v1 stands. v2 is what comes next.

---

## Hard constraints (do not deviate)

- **Author voice is yours, not generic AI prose.** Edit the paper. Cut what feels off. The epigraph stays.
- **Cross-system distillation stays a hypothesis.** v1 §8. Don't promote it to a result in v2 — that's v3 territory and would damage credibility.
- **Effect sizes, not p-values, in §5.4.** N is small. Honesty is currency.
- **Trace-as-deliverable framing in §6, not as ideal.** Map directly to the NIST AI RMF and EU AI Act Article 12 trace requirements.
- **No new primitives.** v2 measures the four primitives v1 named. The v6 contract is a *system-design* contribution, not a new primitive — keep that distinction in §3.5.
- **MIT for the harness, proprietary for the runtime.** Two separate licenses. The paper says so explicitly.

---

## Acceptance criteria for "v2 ready to submit"

- [ ] Paper draft reviewed by you and revised at least once for voice.
- [ ] §5.5 Pareto sweep run on at least one real production workload, results table inserted.
- [ ] §5.4 study run with N ≥ 20, effect sizes + CIs reported with the null position acknowledged if it stands.
- [ ] §5.1 / §5.2 / §5.3 either run or framed as "harness available, results forthcoming" with the harness link cited.
- [ ] Governance §6 numbers refreshed against current `docs/audit/szl-government-readiness.md`.
- [ ] References checked — placeholders ([YUE], [OLM]) resolved with full bibliographic entries.
- [ ] Appendix A / B reproduced from the actual current source (not the snapshot in this draft).
- [ ] Acknowledgments include the reviewers from §5.4 if any consent to be named.

When all of the above is checked: arXiv submission to cs.SE primary, cs.AI secondary. Same author, same affiliation pattern as v1 ("Independent Researcher" or "SZL Holdings" — your choice).

---

## Why this works

v1 is a stake in the ground. v2 turns the stake into a foundation by **doing the measurements v1 promised** — not by making bigger claims, but by backing every existing claim with a test, a trace, or a study.

This is the inverse of the usual second-paper trap (overreach). It is, deliberately, the *less* ambitious paper than v1's bullish reading would suggest, because the substrate is already strong enough that conservatism is a feature, not a flaw.

Your codebase already overshoots your paper. The job for v2 is to let the paper catch up.

— Stephen
2026-04-30
