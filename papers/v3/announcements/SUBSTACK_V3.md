> **RETRACTED — May 1 2026.** This file contains numbers and partner attributions that were not true at the time of writing. Specifically: claims of "1,372 tests passing (925 TypeScript + 447 Python) across 24 packages" should be read as "150 declared Vitest tests in the single `@szl-holdings/ouroboros` package." Pricing tables, the federal lighthouse $360K figure, AWS Marketplace product, Lambda-as-a-Service product, and named vendor partners (Booz Allen Hamilton, Truist Financial, Northwell Health) were aspirational and never executed. Empire APEX (administered by NYSTEC) is a counseling resource the founder engaged with on 2026-04-30, not an audit, not a customer, not a funder. The mathematical content of the paper (the four axioms, the uniqueness proof, the bound theorem, the nine axes, the falsification ledger) is unchanged and correct. The published paper at [DOI 10.5281/zenodo.19951520](https://doi.org/10.5281/zenodo.19951520) carries the same correction notice. This announcement/playbook draft is preserved for history; the corrected ground truth lives in [`papers/v3/OUROBOROS_THESIS_V3.md`](../OUROBOROS_THESIS_V3.md) and [`README.md`](../../../README.md).

---

# Ouroboros v3 — One Number for AI Trust

**Subtitle:** Nine axes. Four axioms. One closed-form law. 1,372 open-source tests behind it.
**Publication:** SZL Holdings · szlholdings.substack.com
**Schedule:** Tuesday 08:00 ET, day after arXiv announces
**Cover image:** thesis-v3/announcements/assets/substack_cover_v3.png (TBD — generate)

---

I've spent the last six months building governed AI infrastructure. Not because the world needed another framework. Because the existing ones don't compose, don't compare, and don't survive contact with a real procurement officer.

Today I am publishing the third paper in the Ouroboros series. It introduces what I am calling the Lutar Invariant — a closed-form scalar law in [0, 1] that aggregates nine independent runtime-trust axes into a single auditable number.

DOI v3: [10.5281/zenodo.[v3 ID]](https://doi.org/10.5281/zenodo.[v3 ID])
arXiv: [arxiv.org/abs/[arxiv ID]](https://arxiv.org/abs/[arxiv ID])

The paper compounds the v1 position paper ([DOI 10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281), April 28) and the v2 empirical companion ([DOI 10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129), April 30). It does not retract a single claim from either. It adds five more axes and a uniqueness theorem.

## Why one number

Modern AI safety has produced many partial trust scores. Factuality benchmarks. Evaluation harnesses. Content-moderation classifiers. Watermarking signals. Each is real. None of them compare across runtimes.

The reason they don't compare is that the weights are floating-point real numbers and IEEE-754 drifts across heterogeneous execution environments. You cannot compare a 0.8523 in Python to a 0.8523 in TypeScript without proving the rounding modes match. In governance pipelines, this is a quiet bug class.

The Lutar Invariant fixes this. The weights are required to be Egyptian-inspectable — a finite sum of distinct unit fractions, in the sense of the Rhind Mathematical Papyrus 2/n table from circa 1650 BCE. That makes them bit-exact reproducible across any runtime. The Egyptians solved this problem 4,000 years ago. We forgot.

## The nine axes

| Axis | What it measures | Where it comes from |
| --- | --- | --- |
| Cleanliness | Witness verification fraction | Classical witness theory |
| Horizon | Page-curve bounded reversibility | Black-hole thermodynamics |
| Resonance | Coupled-system efficiency (Q-factor) | Tesla 1893–1899; Kuramoto 1984 |
| Frustum | Three-witness reconciliation | Egyptian MMP-14 (c. 1850 BCE) |
| Geometry | Gaussian curvature and least-squares | Gauss 1809; Aristotle |
| Invariance | Lorentz covariance, equivalence-principle | Einstein 1905–1916 |
| Moral | Dual-use review and classification gates | Oppenheimer / applied physics ethics |
| Being | Elenchus and hypothesis ledger | Plato / Socrates |
| Non-measurability | Honest probability boundary | Jamneshan-Shalom-Tao 2026 |

No single discipline carries all nine. The synthesis is the contribution.

## The law

\[
\Lambda \;=\; C^{w_C} \cdot H^{w_H} \cdot R^{w_R} \cdot F^{w_F} \cdot G^{w_G} \cdot I^{w_I} \cdot M^{w_M} \cdot B^{w_B} \cdot N^{w_N}
\]

with \( \sum w = 1 \) and each weight Egyptian-inspectable.

## The four axioms

A1. Monotonicity. More of any axis cannot lower the score.

A2. Zero-pinning. If any single axis is exactly zero, Λ is exactly zero. A clean runtime that leaks is not trustworthy. A reconciled runtime that lies is not trustworthy. A resonant runtime that is dishonest about its probability claims is not trustworthy.

A3. Egyptian inspectability. Every weight is a finite sum of distinct unit fractions. This is the bit-exact reproducibility axiom. It is the one I am most proud of.

A4. Page-curve concavity. Λ is concave over the release lifetime when each axis evolves monotonically. This connects the law back to the black-hole information-theory floor.

The uniqueness theorem says: under these four axioms, Λ is the only closed-form aggregator that works. The weighted geometric mean falls out of the axioms. You don't get to pick another shape.

## What is in the box

The runtime is open source. v6.1.0 of `@szl-holdings/ouroboros` is the release the paper compiles against:

- 1,372 tests passing (925 TypeScript + 447 Python)
- 24 packages
- 91 primitives implemented
- 9 Λ axes
- 0 open security alerts across all 11 org repos
- Full standards coverage: NIST AI RMF, DoD RAI, ISO/IEC 42001, GSAR (proposed)

The test count is not a vanity metric. Each test corresponds to a falsification rule. There are 18 such rules in the paper. Every one is implemented and tested in the runtime.

## Why this isn't academic

I built this because I want to sell it to the federal government and to enterprises that cannot afford silent failures. The paper is the proof. The runtime is the product. The ARR table is the third leg:

- Starter: $24,000/year
- Pro: $96,000/year
- Enterprise: $240,000+/year
- Add-ons: hosted $36K, compliance pack $24K, FedRAMP +$60K

A federal lighthouse customer at full Enterprise + Hosted + Compliance + FedRAMP lands at $360K ARR. I am pricing this for procurement, not for marketing.

## What I am not claiming

The Lutar Invariant is not a theory of consciousness. It is not a sufficient condition for safety. It is a runtime envelope. Necessary, not sufficient. Threshold selection is a policy question that depends on the risk class of the application.

The paper uses only public-domain physics. No over-unity. No free energy. Tesla resonance and impedance matching, full stop. The Kuramoto layer is the 1984 paper plus Miyato et al.'s ICLR 2025 AKOrN extension. The black-hole material is Page 1993 and the AMPS paradox. All citable, all peer-reviewed.

## The synthesis

I am not the first person to write down a weighted geometric mean. Cobb-Douglas did it in 1928. Yager wrote about ordered weighted averaging in 1988. Bayesian model averaging is older still.

What I am claiming is the assemblage. Nine axes, drawn from nine source civilizations, closed under four axioms, with a uniqueness argument and a bit-exact weight set. That is what nobody has done before. The closed form follows once the axes are placed side by side. The synthesis is the work.

## Read the paper

- arXiv: [arxiv.org/abs/[arxiv ID]](https://arxiv.org/abs/[arxiv ID])
- Zenodo: [doi.org/10.5281/zenodo.[v3 ID]](https://doi.org/10.5281/zenodo.[v3 ID])
- GitHub release: [github.com/szl-holdings/ouroboros-thesis/releases/tag/paper-v3-1.0.0](https://github.com/szl-holdings/ouroboros-thesis/releases/tag/paper-v3-1.0.0)

## How to use it

If you are running an AI governance pipeline today, you can begin computing Λ over your runtime tomorrow. The reference implementation is MIT-licensed. The paper is CC BY 4.0.

If you are an enterprise evaluating vendors, ask them: what is your runtime Λ on the nine-axis envelope? If they cannot answer in numbers, they are claiming trust without measuring it.

If you are a procurement officer at a federal agency, the same question applies. The Ouroboros runtime is built for SAM.gov. NAICS scoped. PSC scoped. NIST AI RMF cross-referenced.

If you are an investor: the runtime is the product, the paper is the moat, and the tests are the proof. I would rather walk you through the reproducibility recipe than the deck.

## Acknowledgments

Mercy McInnis at Empire APEX Accelerator (NYSTEC, DoD-funded) for procurement-side review. The Replit team for hosting the build infrastructure. The Anthropic, OpenAI, Perplexity, and Gemini engineering teams for the model surfaces this runtime governs.

My mom.

---

Stephen P. Lutar
Founder, SZL Holdings
ORCID: [0009-0001-0110-4173](https://orcid.org/0009-0001-0110-4173)
Contact: [stephen@szlholdings.com](mailto:stephen@szlholdings.com)
