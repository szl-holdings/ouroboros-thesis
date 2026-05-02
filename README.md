# The Ouroboros Thesis

> Bounded loops with measurable convergence as a first-class system primitive.

[![CI](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/ci.yml/badge.svg)](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/ci.yml)
[![CodeQL](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/codeql.yml/badge.svg)](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/codeql.yml)
[![Runtime tests](https://img.shields.io/badge/runtime%20tests-150%20declared-2da44e?style=flat-square)](https://github.com/szl-holdings/ouroboros)
[![Contract](https://img.shields.io/badge/contract-v6.1.0-2b6cb0?style=flat-square)](./a11oy-ultimate-replit-payload.v6.json)
[![Paper v3 (latest)](https://img.shields.io/badge/paper-v3.0.0%20Lutar%20Invariant-c4356b?style=flat-square)](./papers/v3/OUROBOROS_THESIS_V3.md)
[![Zenodo v3 (latest)](https://zenodo.org/badge/DOI/10.5281/zenodo.19951520.svg)](https://doi.org/10.5281/zenodo.19951520)
[![Zenodo concept (always-latest)](https://img.shields.io/badge/Zenodo%20concept-10.5281%2Fzenodo.19944926-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19944926)
[![Zenodo v2](https://img.shields.io/badge/Zenodo%20v2-10.5281%2Fzenodo.19934129-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19934129)
[![Zenodo v1](https://img.shields.io/badge/Zenodo%20v1-10.5281%2Fzenodo.19867281-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19867281)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-1f78b4?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--0110--4173-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0001-0110-4173)

This repository hosts the canonical text and operational contracts for the **Ouroboros Thesis**, the architectural rationale that underpins the [SZL Holdings](https://github.com/szl-holdings) product portfolio.

---

## 📄 Papers

| Track | Paper | Status | DOI |
|---|---|---|---|
| **v3 — The Lutar Invariant** (latest) | [`papers/v3/OUROBOROS_THESIS_V3.md`](./papers/v3/OUROBOROS_THESIS_V3.md) · [PDF](./papers/v3/OUROBOROS_THESIS_V3.pdf) | **Published 2026-05-01** | [10.5281/zenodo.19951520](https://doi.org/10.5281/zenodo.19951520) |
| v2 — Empirical companion | [`v2/paper/ouroboros-thesis-v2-empirical.pdf`](./v2/paper/ouroboros-thesis-v2-empirical.pdf) | Published 2026-04-30 | [10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129) |
| v1 — Position paper | [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Published 2026-04-28 | [10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281) |
| Concept DOI (always-latest) | — | — | [10.5281/zenodo.19944926](https://doi.org/10.5281/zenodo.19944926) |

> **Naming note:** the file `ouroboros-thesis-v2.md` in the repo root is the *v1 position paper text* (Zenodo 19867281). v2 is under [`v2/`](./v2/). v3 is under [`papers/v3/`](./papers/v3/).

### v3 — The Lutar Invariant

> *Subtitle:* A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems.

v3 introduces the **Lutar Invariant Λ**, a closed-form scalar in [0, 1] that aggregates nine independent runtime-trust axes — Cleanliness, Horizon, Resonance, Frustum, Geometry, Invariance, Moral, Being, Non-measurability — into a single auditable number. The invariant is derived from first principles and instrumented in a reference runtime (`@szl-holdings/ouroboros` v6.1.0). The shipped test surface at the v6.1.0 release is **150 declared Vitest tests** in the single `@szl-holdings/ouroboros` package. Earlier copies of this README claimed 1,372 tests across 24 packages with a 925 TypeScript / 447 Python split; that surface was roadmap, not shipped, and the claim is retracted. Where v1 was a position paper and v2 was empirical, v3 is the formal scalar law.

**Browse [`papers/v3/`](./papers/v3/) for:**
- 📄 [`OUROBOROS_THESIS_V3.md`](./papers/v3/OUROBOROS_THESIS_V3.md) — markdown source
- 📑 [`OUROBOROS_THESIS_V3.pdf`](./papers/v3/OUROBOROS_THESIS_V3.pdf) — typeset 40-page PDF

### v2 — The Loop Is the Product (Empirical Companion)

The v1 paper was a position and systems-design preprint. v2 is the empirical companion: a shipped reference implementation (150 declared Vitest tests at the v6.1.0 release commit; the original v2 release reported 142 due to a counting error), three case studies on the same kernel (A11oy, Sentra, Amaru), closure of the v1 §9 experimental agenda, and a §3.7 falsification ledger.

**Browse [`v2/`](./v2/) for:**
- 📄 [`v2/paper/`](./v2/paper/) — the typeset PDF and markdown source
- 🧪 [`v2/experiments/`](./v2/experiments/) — MIT-licensed replication harness (Pareto extractor, frontier sweep, trace loader)
- 📋 [`v2/study/`](./v2/study/) — pre-registered protocol, consent form, deterministic randomization
- 📰 [`v2/blog/`](./v2/blog/) — companion announcement post
- 🚀 [`v2/release/`](./v2/release/) — release notes and GitHub-release playbook
- 🎓 [`v2/submission/`](./v2/submission/) — Zenodo + arXiv playbooks and metadata
- 📦 [`v2/PAYLOAD.md`](./v2/PAYLOAD.md) — full index of the v2 build

---

## How to cite

Cite v3 (the current latest):

```bibtex
@misc{lutar2026lutar_invariant,
  author    = {Lutar, Stephen P.},
  author_orcid = {0009-0001-0110-4173},
  title     = {Ouroboros Thesis v3 — The Lutar Invariant: A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems},
  year      = 2026,
  month     = may,
  publisher = {Zenodo},
  version   = {3.0.0},
  doi       = {10.5281/zenodo.19951520},
  url       = {https://doi.org/10.5281/zenodo.19951520},
  license   = {CC-BY-4.0}
}
```

To always cite the latest version regardless of revision, use the **concept DOI** [10.5281/zenodo.19944926](https://doi.org/10.5281/zenodo.19944926).

GitHub auto-renders a one-click citation generator from [`CITATION.cff`](./CITATION.cff) — look for the **"Cite this repository"** button in the right sidebar.

---

## Contents (root)

| File | What it is |
|---|---|
| [`papers/v3/`](./papers/v3/) | **v3 — The Lutar Invariant** (markdown + PDF) |
| [`v2/`](./v2/) | v2 empirical companion build |
| [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Original v1 position paper text |
| [`ouroboros-thesis-v2.docx`](./ouroboros-thesis-v2.docx) | v1 source manuscript (Word) |
| [`ouroboros-runtime-contract.v2.json`](./ouroboros-runtime-contract.v2.json) | v2 operational contract |
| [`a11oy-ultimate-replit-payload.v6.json`](./a11oy-ultimate-replit-payload.v6.json) | v6 operational contract — 16 shared runtime services, 10 halt conditions, 11-rule task routing, tool permission matrix, sandbox policy, secrets broker, agent registry |
| [`CITATION.cff`](./CITATION.cff) | GitHub "Cite this repository" metadata |

---

## Reference implementation

The reference runtime is published at [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros) — `@szl-holdings/ouroboros` v6.1.0 with **150 declared Vitest tests** at the release commit. The seven domain products listed under the [`szl-holdings`](https://github.com/szl-holdings) organization (A11oy, Sentra, Amaru, Counsel, Terra, Vessels, Carlota Jo) are at varying stages: some have shipped code in private repositories, others are README-only placeholders. Earlier copies of this README listed all seven as products consuming the runtime; the public availability and integration status of each is being clarified separately and will be reflected in the per-product README.

## Government readiness

The 2026-04-30 NYSTEC engagement was an **Empire APEX Accelerator counseling session**, not a third-party audit. The scorecards below were prepared by the founder using the Empire APEX readiness checklist as a self-assessment instrument; they are not external audit findings.

- **Self-assessment document:** [`docs/audit/szl-government-readiness.md`](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)
- **Per-platform self-scored readiness:** A11oy 72/100, Sentra 68/100, Amaru 65/100
- **NIST AI RMF:** mapped across GOVERN / MAP / MEASURE / MANAGE in the self-assessment
- **DoD Responsible AI Tenets:** 4 of 5 mapped (Equitable in 30-day roadmap)
- **GSAR 552.239-7001:** 5 of 10 mapped, 5 documented gaps (all documentation, no architectural rework expected)

A formal third-party audit has not been performed.

---

The thesis draws on, and explicitly generalizes, the loop-language work in the literature (notably the *Ouro LoopLM* line of inquiry, arXiv:2510.25741, alongside Universal Transformers, PonderNet, ACT) to the **system layer** — control planes, agent fabrics, data-sync engines — rather than the model layer. See §2 of the v2 paper and §1–§2 of the v3 paper for the full lineage.

---

© 2026 SZL Holdings. The paper text is published under CC BY 4.0. The replication harness under [`v2/experiments/`](./v2/experiments/) is MIT licensed. The runtime ([`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros)) remains proprietary.
