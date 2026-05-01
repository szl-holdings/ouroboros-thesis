# Ouroboros Thesis v4 — Paper Scope (one page)

**Working title.** *Time-Varying Λ, Compositionality, and Independence: Extensions to the Lutar Invariant.*

**Status.** Pre-draft. This document defines the boundary of the v4 paper. It is paired with — and posterior to — the v4 Certification Packet (`papers/v4/CERTIFICATION_PACKET.md`), which is the commercial artifact and ships first.

**Why the paper comes second.** The certification packet is the procurement-side instrument. It enables the Mercy Corps procurement conversation on May 6, 2026, and any other federal-adjacent acquisition discussion in Q2 2026. Writing the paper before that conversation closes the field on what reviewers actually ask for. Writing it after means the v4 paper extends Λ in directions procurement demand has named, not directions the founder guessed at.

---

## What v4 is

A theoretical extension of the v3 result. v3 proved that Λ is the unique closed-form aggregator over nine axes that satisfies four axioms (Monotonicity, Zero-pinning, Egyptian inspectability, Page-curve concavity). v4 takes that result and pushes it forward in four directions.

### 1. Time-varying Λ — Λ(t)

v3 treats Λ as a per-decision scalar. v4 treats Λ as a stochastic process indexed by deployment lifetime. The contribution is a formal account of how trust degrades and recovers — drift, calibration loss, falsification rule additions, and the dual recovery dynamics from runtime upgrades, ledger refinement, and replay-based remediation.

The deliverable is a Λ(t) trajectory equation, a recovery-half-life metric, and a falsification rule that fires when the observed trajectory diverges from the expected one beyond a stated bound.

### 2. Page-curve dynamics, formalized

v3 uses Page-curve concavity as an axiom on the aggregator shape. v4 lifts the Page curve into a dynamic statement about how the runtime's information-theoretic budget evolves over a workload. The contribution is a mapping between black-hole evaporation Page time and runtime trust-budget exhaustion. This is the technical bridge to the Mercy partnership thesis, the v2 black holes synthesis, and the public-facing narrative.

### 3. Compositionality under tenant isolation

v3 is silent on what Λ does when systems compose. v4 proves a compositionality theorem: under stated tenant-isolation conditions, the Λ of a composed system is bounded above by the minimum of the Λ values of the components, with a known correction term for cross-tenant information flow. This matters operationally — Pro and Enterprise tier customers run multi-tenant deployments. The theorem says something procurement-grade about the upper bound on aggregate trust.

### 4. Axiom independence and minimality

v3 proved uniqueness given the four axioms. v4 proves that no proper subset of the four axioms is sufficient — every axiom is independent of the others. The deliverable is four counterexamples, one per axiom, each showing a distinct closed-form aggregator that satisfies the other three axioms but not the named one. This closes the foundational question of whether the axiom set could be smaller.

---

## What v4 is not

- Not a retraction of v1, v2, or v3. The Zenodo concept-DOI series compounds.
- Not a packet update. The certification packet is versioned independently and refers to v3 as the canonical paper. v4 supersedes the canonical paper only when it reaches Zenodo.
- Not a replacement of the runtime. The runtime version that pairs with v4 will be stated at release time, not pre-announced here.

---

## New falsification rules anticipated

The full ledger in v4 will be at least 18 + N rules, where N is set by the four contributions above. Provisional additions:

- **F-T-1 (time-varying):** Λ(t) trajectory deviates from expected envelope without flag.
- **F-T-2 (time-varying):** recovery half-life exceeds stated bound after stated remediation.
- **F-K-1 (compositionality):** composed-system Λ exceeds minimum of component Λ values without explicit cross-tenant audit receipt.
- **F-A-1 (axiom independence):** runtime claims an aggregator with strictly fewer axioms than four without producing the counterexample family.

These are provisional. The final ledger emerges from the proofs, not the other way around.

---

## Dependencies on community feedback

The four directions above are the founder's pre-Mercy guess at what v4 should contain. They will be tightened or replaced based on:

1. Mercy Corps procurement-side input (May 6, 2026 meeting).
2. ATO reviewer feedback after the certification packet circulates.
3. Any peer-review-style commentary on v3 received between v3 publication (Apr 30, 2026) and v4 draft start.
4. Any falsification rule submissions from the public process invited by GOVERN-5 in the certification packet.

This dependency is intentional. Theoretical work that does not respond to procurement-side reality is theory that does not deploy.

---

## Target timeline

- v4 packet (this directory): **shipped May 1, 2026.**
- Mercy Corps meeting: **May 6, 2026 — 10:00 ET.**
- v4 paper draft start: **after Mercy meeting.**
- v4 paper Zenodo deposit: **target window — late Q2 2026, contingent on (3) above.**

---

## Identifiers

- Issuer: SZL Holdings LLC.
- Author: Stephen P. Lutar — ORCID 0009-0001-0110-4173.
- Concept DOI (always-latest): doi.org/10.5281/zenodo.19944926.
- v3 paper (canonical until v4 deposits): doi.org/10.5281/zenodo.19951520.
- Repository: github.com/szl-holdings/ouroboros-thesis.

---

End of scope.
