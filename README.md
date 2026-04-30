# The Ouroboros Thesis

  > Bounded loops with measurable convergence as a first-class system primitive.

  [![Runtime tests](https://img.shields.io/badge/runtime%20tests-133%2F133-2da44e?style=flat-square)](https://github.com/szl-holdings/ouroboros)
  [![Contract](https://img.shields.io/badge/contract-v6.0.0-2b6cb0?style=flat-square)](./a11oy-ultimate-replit-payload.v6.json)
  [![NYSTEC](https://img.shields.io/badge/NYSTEC%20audit-2026--04--30-805ad5?style=flat-square)](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)

  This repository hosts the canonical text and operational contract for the **Ouroboros Thesis**, the architectural rationale that underpins the [SZL Holdings](https://github.com/szl-holdings) product portfolio.

  ## Contents

  | File | What it is |
  |---|---|
  | [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Full thesis — abstract, 11 sections, 3 appendices |
  | [`ouroboros-thesis-v2.docx`](./ouroboros-thesis-v2.docx) | Source manuscript (Word format) |
  | [`ouroboros-runtime-contract.v2.json`](./ouroboros-runtime-contract.v2.json) | v2 operational contract — interfaces, validators, proof routes, risk tiers, almanac cycles, deployment health checks |
  | [`a11oy-ultimate-replit-payload.v6.json`](./a11oy-ultimate-replit-payload.v6.json) | **v6 operational contract** — adds 16 shared runtime services, 10 halt conditions, 11-rule task routing, tool permission matrix, sandbox policy, secrets broker, agent registry contract |

  ## Reference implementation

  The runtime that implements the v2 and v6 contracts is published at [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros) — `@workspace/ouroboros`, **133/133 tests passing**. The seven domain products that consume the runtime — A11oy, Sentra, Amaru, Counsel, Terra, Vessels, Carlota Jo — are showcased under the [`szl-holdings`](https://github.com/szl-holdings) organization.

  ## Government readiness

  The thesis architecture has been formally audited for federal and New York State AI procurement (Empire APEX Accelerator, NYSTEC, 2026-04-30). Full report and structured data layer:

  - **Audit document**: [`docs/audit/szl-government-readiness.md`](https://github.com/szl-holdings/ouroboros/blob/main/docs/audit/szl-government-readiness.md)
  - **Per-platform scorecards**: A11oy 72/100, Sentra 68/100, Amaru 65/100
  - **NIST AI RMF**: full coverage across GOVERN / MAP / MEASURE / MANAGE
  - **DoD Responsible AI Tenets**: 4 of 5 covered (Equitable in 30-day roadmap)
  - **GSAR 552.239-7001**: 5 of 10 covered, 5 documented gaps (all documentation, no architectural rework needed)

  ## Citation

  The thesis draws on, and explicitly generalizes, the loop-language work in the literature (notably the *Ouro LoopLM* line of inquiry, arXiv:2510.25741) to the **system layer** — control planes, agent fabrics, data-sync engines — rather than the model layer. See §2 of the thesis for the full lineage.

  ---

  © 2026 SZL Holdings. The thesis text is published for reference; reuse requires written permission.
  