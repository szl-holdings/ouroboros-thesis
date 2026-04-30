# The Ouroboros Thesis (v2)

  > Bounded loops with measurable convergence as a first-class system primitive.

  This repository hosts the canonical text and operational contract for the **Ouroboros Thesis**, the architectural rationale that underpins the [SZL Holdings](https://github.com/szl-holdings) product portfolio.

  ## Contents

  | File | What it is |
  | --- | --- |
  | [`ouroboros-thesis-v2.md`](./ouroboros-thesis-v2.md) | Full thesis — abstract, 11 sections, 3 appendices |
  | [`ouroboros-thesis-v2.docx`](./ouroboros-thesis-v2.docx) | Source manuscript (Word format) |
  | [`ouroboros-runtime-contract.v2.json`](./ouroboros-runtime-contract.v2.json) | Operational contract — interfaces, validators, proof routes, risk tiers, almanac cycles, deployment health checks |

  ## Reference implementation

  The runtime that implements the contract is published at [`szl-holdings/ouroboros`](https://github.com/szl-holdings/ouroboros). The seven domain products that consume the runtime — Amaru, A11oy, Sentra, Counsel, Terra, Vessels, Carlota Jo — are showcased under the [`szl-holdings`](https://github.com/szl-holdings) organization.

  ## Citation

  The thesis draws on, and explicitly generalizes, the loop-language work in the literature (notably the *Ouro LoopLM* line of inquiry, arXiv:2510.25741) to the **system layer** — control planes, agent fabrics, data-sync engines — rather than the model layer. See §2 of the thesis for the full lineage.

  ---

  © 2026 SZL Holdings. The thesis text is published for reference; reuse requires written permission.
  