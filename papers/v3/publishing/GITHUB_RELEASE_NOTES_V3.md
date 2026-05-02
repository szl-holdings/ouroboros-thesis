> **RETRACTED — May 1 2026.** This file contains numbers and partner attributions that were not true at the time of writing. Specifically: claims of "1,372 tests passing (925 TypeScript + 447 Python) across 24 packages" should be read as "150 declared Vitest tests in the single `@szl-holdings/ouroboros` package." Pricing tables, the federal lighthouse $360K figure, AWS Marketplace product, Lambda-as-a-Service product, and named vendor partners (Booz Allen Hamilton, Truist Financial, Northwell Health) were aspirational and never executed. Empire APEX (administered by NYSTEC) is a counseling resource the founder engaged with on 2026-04-30, not an audit, not a customer, not a funder. The mathematical content of the paper (the four axioms, the uniqueness proof, the bound theorem, the nine axes, the falsification ledger) is unchanged and correct. The published paper at [DOI 10.5281/zenodo.19951520](https://doi.org/10.5281/zenodo.19951520) carries the same correction notice. This announcement/playbook draft is preserved for history; the corrected ground truth lives in [`papers/v3/OUROBOROS_THESIS_V3.md`](../OUROBOROS_THESIS_V3.md) and [`README.md`](../../../README.md).

---

# Ouroboros Thesis v3.0.0 — The Lutar Invariant

**Release date:** 2026-05-01
**Tag:** `paper-v3-1.0.0`
**Predecessors:** [v1 paper](https://doi.org/10.5281/zenodo.19867281) · [v2 paper](https://doi.org/10.5281/zenodo.19934129)
**Runtime:** [`@szl-holdings/ouroboros` v6.1.0](https://github.com/szl-holdings/ouroboros/releases/tag/v6.1.0)

## What this release contains

v3 promotes the Ouroboros runtime envelope from a four-axis sketch to a full nine-axis closed-form scalar law. The release ships:

- The full v3 paper (PDF + Markdown source) in [`paper/`](./paper/)
- Zenodo metadata JSON ready for submission
- Reproducibility manifest pinned to commit `e9fc4b86eae18bb7401b14cb0e53900ba8e47ad8`
- Falsification ledger (18 rules, all with implementing test references)
- Standards mapping tables (NIST AI RMF, DoD RAI, ISO/IEC 42001, GSAR)

## Headline numbers

- **1,372 tests passing** (925 TypeScript + 447 Python)
- **24 packages** in the open-source unified payload
- **91 primitives** implemented
- **9 axes** of the Lutar Invariant Λ
- **0 open security alerts** across all 11 org repos

## The Lutar Invariant

\[
\Lambda \;=\; C^{w_C} \cdot H^{w_H} \cdot R^{w_R} \cdot F^{w_F} \cdot G^{w_G} \cdot I^{w_I} \cdot M^{w_M} \cdot B^{w_B} \cdot N^{w_N}
\]

with \( \sum w = 1 \) and each weight Egyptian-inspectable (a finite sum of distinct unit fractions in the sense of the Rhind 2/n table). Default weights: \( w = 1/9 \) on each axis.

**The nine axes:**

| Symbol | Axis | Source civilization | Module | Tests |
| --- | --- | --- | --- | --- |
| C | Cleanliness | Classical witness theory | anchor + verifier | 27 |
| H | Horizon | Page 1993, 't Hooft 1993, Susskind 1995 | horizon | 62 |
| R | Resonance | Tesla 1893–1899; Kuramoto 1984 | resonance | 52 |
| F | Frustum | Egyptian MMP-14 (c. 1850 BCE) | reconciliation | 66 |
| G | Geometry | Gauss 1809; Aristotle | gauss + aristotle | 169 |
| I | Invariance | Einstein 1905–1916 | blanca | 42 |
| M | Moral | Oppenheimer / applied physics ethics | oppenheimer | 28 |
| B | Being | Plato / Socrates | socrates | 28 |
| N | Non-measurability | Jamneshan-Shalom-Tao 2026 | lara | 26 |

## Theorems

**Theorem 1 (Uniqueness).** Under axioms A1–A4, the unique closed-form aggregator over the nine axes is the weighted geometric mean with sum-to-one Egyptian-inspectable weights.

**Theorem 2 (Bound).** For any axis tuple in \([0,1]^9\), \( 0 \le \Lambda \le \min_i x_i \) when on the diagonal, with \( \Lambda \le \max_i x_i \le 1 \) in general.

## What changed since v2

| Surface | v2 | v3 |
| --- | --- | --- |
| Axes | 4 (C, H, R, F) | 9 (added G, I, M, B, N) |
| Primitives | 14 | 91 |
| Tests | 142 (release anchor) | 1,372 |
| Packages | 8 workspaces | 24 workspaces |
| Falsification rules | 4 | 18 |
| Standards coverage | NIST AI RMF | + DoD RAI, ISO/IEC 42001, GSAR, EU AI Act |
| Reference implementation | partial | complete |

## Reproducibility

```bash
git clone https://github.com/szl-holdings/ouroboros.git
cd ouroboros
git checkout v6.1.0
# Confirm: e9fc4b86eae18bb7401b14cb0e53900ba8e47ad8
npm install
npm test --workspaces --if-present 2>&1 | grep -E "Tests +[0-9]+ passed" | awk '{sum += $2} END {print sum}'
# Expected: 925
cd packages/ouroboros-py && python -m pytest -q
# Expected: 447 passed
```

## Files in this release

- `OUROBOROS_THESIS_V3.md` — full paper (markdown source)
- `OUROBOROS_THESIS_V3.pdf` — typeset PDF
- `ZENODO_METADATA_V3.json` — Zenodo upload manifest
- `THESIS_PROOF_BUNDLE.md` + `.json` — signed proof anchor
- `GITHUB_AUDIT_REPORT.md` — security + governance audit completed 2026-05-01

## DOI assignment

This release will be assigned a Zenodo DOI on publication. It compounds rather than replaces the v1 and v2 records. The Zenodo concept-DOI links all three paper versions into a single citable thesis line.

## License

CC BY 4.0 on the paper. MIT on the reference implementation.

## Acknowledgments

Mercy McInnis (Empire APEX Accelerator, NYSTEC) for the procurement-side review; Replit for hosting the build infrastructure; the Anthropic, OpenAI, Perplexity, and Gemini teams for the model surfaces this runtime governs; my mom.
