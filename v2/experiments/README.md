# `@szl-holdings/ouroboros` — experiments harness

Open-source replication harness for "Bounded Loops in Production: An Empirical Companion to the Ouroboros Thesis" (Lutar, 2026).

**License:** MIT (this directory only; the runtime in `../packages/ouroboros/src/` remains proprietary).

## Purpose

This harness implements the five experiments proposed in v1 §9 and reported in v2 §5:

| Directory | v1 § | v2 § | What it does |
|---|---|---|---|
| `frontier-sweep/` | 9.5 | 5.5 | Loop-budget Pareto frontier across `maxSteps × convergenceThreshold` |
| `rca-bench/` | 9.1 | 5.1 | Single-pass vs looped root-cause analysis on synthesized incidents |
| `triage-bench/` | 9.2 | 5.2 | EntropyDepthAllocator on Sentra alert-triage workload |
| `sync-bench/` | 9.3 | 5.3 | Amaru convergent-sync replay vs single-pass baseline |
| `audit-study/` | 9.4 | 5.4 | Stimuli, randomization, and analysis for the human study |

## Layout

```
experiments/
├── README.md                       (this file)
├── package.json
├── tsconfig.json
├── vitest.config.ts
├── frontier-sweep/
│   ├── README.md
│   ├── sweep.ts                    main runner
│   ├── workloads/
│   │   ├── a11oy-replay.ts
│   │   ├── sentra-replay.ts
│   │   └── amaru-replay.ts
│   ├── analysis/
│   │   ├── pareto.ts               quality-vs-compute Pareto extraction
│   │   └── plot.ts                 chart emit (svg + csv)
│   └── results/                    .gitignore-d output
├── rca-bench/
│   ├── README.md
│   ├── synthesize-incidents.ts     CVE → incident schema
│   ├── single-pass.ts
│   ├── looped.ts
│   └── score.ts
├── triage-bench/
│   ├── README.md
│   ├── alerts/                     anonymized alert fixtures
│   ├── runner.ts
│   └── score.ts
├── sync-bench/
│   ├── README.md
│   ├── workloads/
│   │   ├── small.json
│   │   ├── medium.json
│   │   └── adversarial.json
│   ├── single-pass.ts
│   ├── ouroboros.ts
│   └── score.ts
├── audit-study/
│   ├── README.md
│   ├── PROTOCOL.md                 IRB-style protocol (also in /study)
│   ├── stimuli/                    8 decision stimuli (4 per arm, crossover)
│   ├── randomization.ts
│   ├── consent-form.md
│   ├── analysis.ipynb              R or Python — Wilcoxon + bootstrap CIs
│   └── results/
└── shared/
    ├── trace-loader.ts             reads from aef-evidence-ledger
    ├── replay.ts                   deterministic re-runner
    └── metrics.ts                  shared accuracy / latency / step metrics
```

## Quickstart

```bash
cd experiments
pnpm install
pnpm exec vitest run --no-coverage   # validates harness against fixtures

# Run §5.5 frontier sweep on A11oy workload
pnpm sweep -- --workload a11oy --output results/

# Run §5.1 RCA bench
pnpm rca -- --incidents 200 --output results/rca.json

# Run §5.3 sync bench against medium workload
pnpm sync -- --workload medium --output results/sync.json
```

## What you need before running

- Node 20+, pnpm 9+
- `OUROBOROS_LEDGER_URI` env var pointing to a `aef-evidence-ledger` instance OR a file-store dump
- For `rca-bench`: a CVE dataset dump (we ship a 200-row fixture; replication uses the full NVD 2024 CVE feed)

## Reproducibility notes

- Every experiment writes a `manifest.json` with the runtime version, allocator config, threshold sweep, and a SHA-256 of the input fixture.
- The frontier sweep is deterministic: same inputs + same seeds + same allocator flag → bit-identical outputs (the Dresden Venus invariant).
- We do **not** ship production traces. The fixtures under each `workloads/` directory are anonymized or synthesized.

## Citing

If you use this harness:

```bibtex
@misc{lutar2026ouroborosv2,
  author = {Lutar, Stephen P.},
  title  = {Bounded Loops in Production: An Empirical Companion to the Ouroboros Thesis},
  year   = {2026},
  note   = {arXiv preprint},
}
```

---

© 2026 SZL Holdings. Harness code MIT; runtime proprietary.
