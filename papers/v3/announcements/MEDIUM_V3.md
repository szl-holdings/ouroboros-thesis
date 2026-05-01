# The Lutar Invariant: One Number for AI Trust

**Subtitle:** A nine-axis closed-form scalar law with 1,372 open-source tests behind it
**Publication:** Medium · @stephen_38454
**Tags:** AI safety, AI governance, runtime trust, machine learning, mathematics, open source
**Read time:** ~10 minutes
**Schedule:** Tuesday 09:00 ET, day after arXiv announces

---

I publish the third paper in the Ouroboros series today.

It introduces a closed-form scalar law that aggregates nine independent runtime-trust axes into a single auditable number. I am calling it the Lutar Invariant, after the family that built it.

DOI: [10.5281/zenodo.[v3 ID]](https://doi.org/10.5281/zenodo.[v3 ID])
arXiv: [arxiv.org/abs/[arxiv ID]](https://arxiv.org/abs/[arxiv ID])

This post is the long-form story of how it came to exist.

## The accountability gap

I started SZL Holdings because I could not buy what I wanted to buy.

I wanted an AI infrastructure layer that would let me run a real business without lying to my customers. Something where every decision the system made was attributable to an artifact, every artifact was anchored to a witness root, every witness root was anchored to a tamper-evident ledger. Standard governance plumbing. Nothing exotic.

It did not exist as a product. There were partial answers. NIST AI RMF gave me the categories. DoD Responsible AI Tenets gave me the principles. ISO/IEC 42001 gave me a management system. None of them gave me a runtime number I could put on a page and defend in front of a procurement officer.

So I built one.

## v1 — the position paper

In April 2026 I published the v1 paper ([DOI 10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281)). It said one thing: an AI runtime is clean if and only if every released bit is reproducible from a witness root, and every witness root is anchored to a tamper-evident ledger.

That is the Cleanliness Theorem. It has not been retracted. It is the C in the v3 invariant.

## v2 — the empirical companion

Two days later I published the v2 paper ([DOI 10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129)). v2 added the empirical layer: a falsification ledger with four rules, a reproducibility manifest, and the first 142 tests of what would become the Ouroboros runtime.

v2 also added three more axes: Horizon (information release rate, bounded by Page-curve concavity), Resonance (coupled-system efficiency, bounded by Tesla impedance matching and Kuramoto coherence), and Frustum (three-witness reconciliation in the sense of the Egyptian Moscow Mathematical Papyrus problem 14, c. 1850 BCE).

Four axes. Necessary. Not sufficient.

## v3 — the synthesis

The synthesis claim of v3 is that there are nine axes, not four, and that under four axioms there is exactly one closed-form scalar law that aggregates them.

| Axis | What it measures |
| --- | --- |
| Cleanliness (C) | Witness verification fraction |
| Horizon (H) | Page-curve bounded reversibility |
| Resonance (R) | Coupled-system efficiency |
| Frustum (F) | Three-witness Jaccard reconciliation |
| Geometry (G) | Gaussian curvature, least-squares discipline |
| Invariance (I) | Lorentz covariance, equivalence-principle |
| Moral (M) | Dual-use review, classification gates |
| Being (B) | Elenchus, hypothesis ledger |
| Non-measurability (N) | Honest probability boundary |

These come from nine different source civilizations: classical witness theory, black-hole thermodynamics, Tesla-era resonance physics, Egyptian arithmetic, Gaussian geometry, Einstein's analytic physics, Oppenheimer's applied-physics ethics, the Plato-Socrates philosophical tradition, and 21st-century ergodic theory (specifically Jamneshan-Shalom-Tao 2026).

No single discipline carries all nine. The synthesis is what is new.

## The law

\[
\Lambda \;=\; C^{w_C} \cdot H^{w_H} \cdot R^{w_R} \cdot F^{w_F} \cdot G^{w_G} \cdot I^{w_I} \cdot M^{w_M} \cdot B^{w_B} \cdot N^{w_N}
\]

with \( \sum w = 1 \) and each weight a finite sum of distinct unit fractions.

That last constraint is the novel one. It is the Egyptian inspectability axiom. It says weights cannot be arbitrary IEEE-754 reals; they must be representable in the form the Rhind Mathematical Papyrus 2/n table established 4,000 years ago. The reason is bit-exact reproducibility: a weight that is `1/2 + 1/4 + 1/8` evaluates to the same value across Python, TypeScript, Rust, C++, and Lean. A weight that is `0.875` does not.

## The four axioms

A1. Monotonicity. More of any axis cannot lower the score.

A2. Zero-pinning. If any single axis is exactly zero, Λ is exactly zero. This is the axiom that does the most work. It says a clean system that leaks is not trustworthy. A resonant system that is dishonest about its probability claims is not trustworthy. The compound score collapses if any single dimension fails.

A3. Egyptian inspectability. Bit-exact weights, bit-exact comparison.

A4. Page-curve concavity. Λ is concave over the release lifetime when each axis evolves monotonically. This is the connection back to the information-thermodynamic floor.

## The uniqueness theorem

Under A1–A4, the unique closed-form aggregator over the nine axes is the weighted geometric mean with sum-to-one Egyptian-inspectable weights.

The proof is short. Additive forms fail A2 (zero-pinning) — you cannot have a sum hit exactly zero unless every term is zero. Multiplicative forms with monotonicity and the boundary condition Λ(1,1,1,1,1,1,1,1,1) = 1 force fᵢ(x) = x^wᵢ. Concavity (A4) forces sum-of-weights ≤ 1. The boundary forces sum-of-weights = 1. A3 restricts the rationals admissible as weights to the Egyptian set.

There are no other admissible aggregators. The closed form is unique.

## What v3 ships

The paper ships with a complete open-source reference implementation:

- 1,372 tests passing (925 TypeScript + 447 Python)
- 24 packages
- 91 primitives across 9 Λ axes
- Runtime release [`@szl-holdings/ouroboros` v6.1.0](https://github.com/szl-holdings/ouroboros/releases/tag/v6.1.0)
- 0 open security alerts across all 11 org repos
- Full security posture (secret scanning, push protection, dependabot, branch protection) on every active repo

The reproducibility recipe is in the paper. Three commands. Anyone can verify the test count.

## Why this matters now

We are entering a window where AI infrastructure is going to be procured by federal agencies, healthcare systems, and financial institutions at meaningful scale. These buyers cannot make the bet without a number they can defend.

The Lutar Invariant is the number. It is a position inside a measurable envelope. It is auditable, reproducible, and grounded in mathematics that has held up for between thirty years (Page 1993) and four thousand years (RMP).

I am not claiming Λ solves AI safety. I am claiming Λ gives you a measuring stick that does not break across runtimes. That is enough to start a real procurement conversation.

## What is next

The roadmap:

- v3.1: Lean / Coq formal proofs of the uniqueness theorem
- v3.2: OTel collector and Grafana dashboard shipping all nine axes as first-class metrics
- v3.3: Sigstore Rekor anchoring of witness roots in production
- v4: extension to multi-runtime federations — the Kuramoto layer becomes the federation layer
- v5: industry consortium / standards body work (ISO, NIST, IEEE)

## Read it

- arXiv: [arxiv.org/abs/[arxiv ID]](https://arxiv.org/abs/[arxiv ID])
- Zenodo (v3): [doi.org/10.5281/zenodo.[v3 ID]](https://doi.org/10.5281/zenodo.[v3 ID])
- Zenodo (v2 empirical): [doi.org/10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129)
- Zenodo (v1 position): [doi.org/10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281)
- GitHub: [github.com/szl-holdings/ouroboros-thesis](https://github.com/szl-holdings/ouroboros-thesis)
- Runtime: [github.com/szl-holdings/ouroboros](https://github.com/szl-holdings/ouroboros)

## Talk to me

- Email: [stephen@szlholdings.com](mailto:stephen@szlholdings.com)
- LinkedIn: [linkedin.com/in/stephen-l-279315240](https://linkedin.com/in/stephen-l-279315240)
- ORCID: [0009-0001-0110-4173](https://orcid.org/0009-0001-0110-4173)

If you are an enterprise evaluating governed-AI vendors, a federal procurement officer, an academic working on aggregation theory, or an investor who can read a reproducibility manifest before reading a deck, I want to hear from you.

The runtime is the product. The paper is the moat. The 1,372 tests are the proof.
