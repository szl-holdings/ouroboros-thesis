# The Ouroboros Thesis

> Bounded loops with measurable convergence as a first-class system primitive.

[![CI](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/ci.yml/badge.svg)](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/ci.yml)
[![CodeQL](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/codeql.yml/badge.svg)](https://github.com/szl-holdings/ouroboros-thesis/actions/workflows/codeql.yml)
[![Runtime tests](https://img.shields.io/badge/runtime%20tests-142%2F142-2da44e?style=flat-square)](https://github.com/szl-holdings/ouroboros)
[![Contract](https://img.shields.io/badge/contract-v6.0.0-2b6cb0?style=flat-square)](./a11oy-ultimate-replit-payload.v6.json)
[![Paper v2 (empirical)](https://img.shields.io/badge/paper-v2.0.0%20empirical-805ad5?style=flat-square)](./v2/paper/ouroboros-thesis-v2-empirical.pdf)
[![Zenodo v2 (latest)](https://zenodo.org/badge/DOI/10.5281/zenodo.19934129.svg)](https://doi.org/10.5281/zenodo.19934129)
[![Zenodo v1](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.19867281-1f78b4?style=flat-square)](https://doi.org/10.5281/zenodo.19867281)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-1f78b4?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--0110--4173-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0009-0001-0110-4173)
[![NYSTEC](https://img.shields.io/badge/NYSTEC%20audit-2026--04--30-805ad5?style=flat-square)](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)

This repository hosts the canonical text and operational contract for the **Ouroboros Thesis**, the architectural rationale that underpins the [SZL Holdings](https://github.com/szl-holdings) product portfolio.

---

## 📄 Papers

| Track | Paper | Status | DOI |
|---|---|---|---|
| **Empirical companion** (latest) | [`v2/paper/ouroboros-thesis-v2-empirical.pdf`](./v2/paper/ouroboros-thesis-v2-empirical.pdf) | **Published 2026-04-30** | [10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129) |
| Position paper (v1) | [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Published 2026-04-28 | [10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281) |
| Auditable-governance revision (v3 internal draft) | [`papers/ouroboros-thesis-v3.md`](./papers/ouroboros-thesis-v3.md) | Internal — superseded by the empirical companion | — |

> **Naming note:** the file `ouroboros-thesis-v2.md` in the repo root is the *v1 position paper text* (Zenodo 19867281). The new **empirical companion** is the formal v2 publication and lives under [`v2/`](./v2/).

### v2 — The Loop Is the Product (Empirical Companion)

> *Subtitle:* An Empirical Companion to the Ouroboros Thesis.

The v1 paper was a position and systems-design preprint and made no empirical claims. v2 is the empirical companion: a shipped reference implementation (142/142 tests, deterministic replay), three production case studies on the same kernel (A11oy, Sentra, Amaru), closure of the v1 §9 experimental agenda, and a §3.7 falsification ledger naming the observations that would refute each load-bearing claim — including a pre-registered commitment to publish a null result for the trace-aided audit study.

The narrow claim defended: **when convergence is measurable, the trace is not a log but a deliverable.**

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

If you use this work, please cite the v2 empirical companion:

```bibtex
@article{lutar2026ouroboros_v2,
  author       = {Lutar, Stephen P.},
  author_orcid = {0009-0001-0110-4173},
  title        = {The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI},
  journal      = {Zenodo},
  year         = {2026},
  month        = apr,
  doi          = {10.5281/zenodo.19934129},
  url          = {https://doi.org/10.5281/zenodo.19934129},
  version      = {2.0.0},
  license      = {CC-BY-4.0}
}
```

GitHub also auto-renders a one-click citation generator from [`CITATION.cff`](./CITATION.cff) — look for the **"Cite this repository"** button in the right sidebar.

For reproducibility, every release on this repo auto-mints a versioned DOI on Zenodo, version-linked under the same concept DOI. To always cite the latest, use the [Zenodo concept DOI](https://doi.org/10.5281/zenodo.19934129).

---

## Contents (root)

| File | What it is |
|---|---|
| [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Original position paper text (v1 on Zenodo) |
| [`ouroboros-thesis-v2.docx`](./ouroboros-thesis-v2.docx) | Source manuscript (Word format) |
| [`ouroboros-runtime-contract.v2.json`](./ouroboros-runtime-contract.v2.json) | v2 operational contract — interfaces, validators, proof routes, risk tiers, almanac cycles, deployment health checks |
| [`a11oy-ultimate-replit-payload.v6.json`](./a11oy-ultimate-replit-payload.v6.json) | **v6 operational contract** — adds 16 shared runtime services, 10 halt conditions, 11-rule task routing, tool permission matrix, sandbox policy, secrets broker, agent registry contract |
| [`CITATION.cff`](./CITATION.cff) | GitHub auto-renders this into the "Cite this repository" button |

---

## Reference implementation

The runtime that implements the v2 and v6 contracts is published at [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros) — `@szl-holdings/ouroboros`, **142/142 tests passing**. The seven domain products that consume the runtime — A11oy, Sentra, Amaru, Counsel, Terra, Vessels, Carlota Jo — are showcased under the [`szl-holdings`](https://github.com/szl-holdings) organization.

## Government readiness

The thesis architecture has been formally audited for federal and New York State AI procurement (Empire APEX Accelerator, NYSTEC, 2026-04-30). Full report and structured data layer:

- **Audit document**: [`docs/audit/szl-government-readiness.md`](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)
- **Per-platform scorecards**: A11oy 72/100, Sentra 68/100, Amaru 65/100
- **NIST AI RMF**: full coverage across GOVERN / MAP / MEASURE / MANAGE
- **DoD Responsible AI Tenets**: 4 of 5 covered (Equitable in 30-day roadmap)
- **GSAR 552.239-7001**: 5 of 10 covered, 5 documented gaps (all documentation, no architectural rework needed)

---

## Citation

If you use this work, please cite the empirical companion (v2) once its DOI is minted:

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

The thesis draws on, and explicitly generalizes, the loop-language work in the literature (notably the *Ouro LoopLM* line of inquiry, arXiv:2510.25741, alongside Universal Transformers, PonderNet, ACT) to the **system layer** — control planes, agent fabrics, data-sync engines — rather than the model layer. See §2 of the v2 paper for the full lineage.

---

© 2026 SZL Holdings. The paper text is published under CC BY 4.0. The replication harness under [`v2/experiments/`](./v2/experiments/) is MIT licensed. The runtime ([`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros)) remains proprietary.
