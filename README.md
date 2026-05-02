# The Ouroboros Thesis

> Bounded loops with measurable convergence as a first-class system primitive.

[![Runtime tests](https://img.shields.io/badge/runtime%20tests-150%2F150-2da44e?style=flat-square)](https://github.com/szl-holdings/ouroboros)
[![Contract](https://img.shields.io/badge/contract-v6.0.0-2b6cb0?style=flat-square)](./a11oy-ultimate-replit-payload.v6.json)
[![Paper v2 (empirical)](https://img.shields.io/badge/paper-v2.0.0%20empirical-805ad5?style=flat-square)](./v2/paper/ouroboros-thesis-v2-empirical.pdf)
[![DOI v1](https://img.shields.io/badge/DOI%20v1-10.5281%2Fzenodo.19867281-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19867281)
[![DOI v2](https://img.shields.io/badge/DOI%20v2-10.5281%2Fzenodo.19934129-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19934129)

This repository hosts the canonical text and operational contract for the **Ouroboros Thesis**, the architectural rationale that underpins the [SZL Holdings](https://github.com/szl-holdings) product portfolio.

> **Notice — May 2 2026.** v3 (Zenodo 19951520, "Ouroboros Thesis v3 — The Lutar Invariant") was retracted by the author on 2026-05-02 due to overstated implementation and commercial claims discovered in self-audit. The Zenodo record is tombstoned with reason "retracted." v1 and v2 are unaffected and remain the citable record.
>
> **Update — May 2 2026 (later same day).** The rewritten v3 has now landed at [`papers/v3/`](./papers/v3/). It contains only audit-supported claims; the full pre-publication audit is in [`papers/v3/AUDIT.md`](./papers/v3/AUDIT.md). A new DOI will be minted automatically by Zenodo on the GitHub Release.

---

## 📄 Papers

| Track | Paper | Status | DOI |
|---|---|---|---|
| **Empirical companion** (latest published) | [`v2/paper/ouroboros-thesis-v2-empirical.pdf`](./v2/paper/ouroboros-thesis-v2-empirical.pdf) | Published 2026-04-30 | [10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129) |
| Position paper (v1) | [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Published 2026-04-28 | [10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281) |
| v3 (Lutar Invariant) — original | — | **Retracted 2026-05-02** by author | [10.5281/zenodo.19951520](https://doi.org/10.5281/zenodo.19951520) (tombstone) |
| v3 (Lutar Invariant) — rewrite | [`papers/v3/ouroboros-thesis-v3.pdf`](./papers/v3/ouroboros-thesis-v3.pdf) | **Published 2026-05-02** (audit-supported rewrite) | Pending Zenodo (auto-mint on Release) |

> **Naming note:** the file `ouroboros-thesis-v2.md` in the repo root is the *v1 position paper text* (Zenodo 19867281). The empirical companion is the formal v2 publication and lives under [`v2/`](./v2/).

### v2 — The Loop Is the Product (Empirical Companion)

> *Subtitle:* An Empirical Companion to the Ouroboros Thesis.

The v1 paper was a position and systems-design preprint and made no empirical claims. v2 is the empirical companion: a shipped reference implementation, three case studies on the same kernel (A11oy, Sentra, Amaru), closure of the v1 experimental agenda, and a falsification ledger naming the observations that would refute each load-bearing claim — including a pre-registered commitment to publish a null result for the trace-aided audit study.

The narrow claim defended: **when convergence is measurable, the trace is not a log but a deliverable.**

> **v2 erratum.** The published v2 paper states "142/142 tests" at the release commit. The actual count at that commit was **150 tests** in the single `@szl-holdings/ouroboros` package. This is a counting error in the paper text, not a fabrication. A corrected version will be filed.

**Browse [`v2/`](./v2/) for:**
- 📄 [`v2/paper/`](./v2/paper/) — the typeset PDF and markdown source
- 🧪 [`v2/experiments/`](./v2/experiments/) — MIT-licensed replication harness (Pareto extractor, frontier sweep, trace loader)
- 📋 [`v2/study/`](./v2/study/) — pre-registered protocol, consent form, deterministic randomization
- 📰 [`v2/blog/`](./v2/blog/) — companion announcement post
- 🚀 [`v2/release/`](./v2/release/) — release notes and GitHub-release playbook
- 🎓 [`v2/submission/`](./v2/submission/) — Zenodo + arXiv playbooks and metadata
- 📦 [`v2/PAYLOAD.md`](./v2/PAYLOAD.md) — full index of the v2 build

---

## Contents (root)

| File | What it is |
|---|---|
| [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Original position paper text (v1 on Zenodo) |
| [`ouroboros-thesis-v2.docx`](./ouroboros-thesis-v2.docx) | Source manuscript (Word format) |
| [`ouroboros-runtime-contract.v2.json`](./ouroboros-runtime-contract.v2.json) | v2 operational contract — interfaces, validators, proof routes, risk tiers, almanac cycles, deployment health checks |
| [`a11oy-ultimate-replit-payload.v6.json`](./a11oy-ultimate-replit-payload.v6.json) | v6 operational contract — adds shared runtime services, halt conditions, task routing, tool permission matrix, sandbox policy, secrets broker, agent registry contract |
| [`CITATION.cff`](./CITATION.cff) | GitHub auto-renders this into the "Cite this repository" button |

---

## Reference implementation

The runtime that implements the v2 and v6 contracts is published at [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros) — `@szl-holdings/ouroboros`, **150 declared Vitest tests passing** at v6.1.0. The seven product surfaces (A11oy, Sentra, Amaru, Counsel, Terra, Vessels, Carlota Jo) are public README-stage repositories under the [`szl-holdings`](https://github.com/szl-holdings) organization. They are not yet shipped products.

## Government readiness

SZL Holdings has engaged the **Empire APEX Accelerator** (administered by NYSTEC) for procurement counseling and advisory support. Empire APEX is a counseling program, not a third-party audit body. The platform readiness scorecards (A11oy 72/100, Sentra 68/100, Amaru 65/100) are **founder self-assessments** prepared as input material for those counseling sessions, not third-party audit findings.

The architecture intends alignment with NIST AI RMF, the DoD Responsible AI Tenets, and GSAR 552.239-7001. Coverage at this stage is documented intent and roadmap, not certified compliance. See [`docs/audit/szl-government-readiness.md`](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md) in the runtime repository for the structured detail.

---

## Citation

If you use this work, please cite the empirical companion (v2):

```bibtex
@misc{lutar2026loop,
  author    = {Lutar, Stephen P.},
  title     = {The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI},
  subtitle  = {An Empirical Companion to the Ouroboros Thesis},
  year      = 2026,
  month     = apr,
  publisher = {Zenodo},
  version   = {2.0.0},
  doi       = {10.5281/zenodo.19934129},
  url       = {https://doi.org/10.5281/zenodo.19934129},
  note      = {Companion to Lutar 2026, Zenodo 10.5281/zenodo.19867281}
}
```

The thesis draws on, and explicitly generalizes to the system layer, prior work on adaptive computation and recursive depth in the language-model literature (Universal Transformers; PonderNet; Adaptive Computation Time). See §2 of the v2 paper for the full lineage.

---

© 2026 SZL Holdings. The paper text is published under CC BY 4.0. The replication harness under [`v2/experiments/`](./v2/experiments/) is MIT licensed. The runtime ([`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros)) remains proprietary.
