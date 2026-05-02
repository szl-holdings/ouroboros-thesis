> **RETRACTED — May 1 2026.** This file contains numbers and partner attributions that were not true at the time of writing. Specifically: claims of "1,372 tests passing (925 TypeScript + 447 Python) across 24 packages" should be read as "150 declared Vitest tests in the single `@szl-holdings/ouroboros` package." Pricing tables, the federal lighthouse $360K figure, AWS Marketplace product, Lambda-as-a-Service product, and named vendor partners (Booz Allen Hamilton, Truist Financial, Northwell Health) were aspirational and never executed. Empire APEX (administered by NYSTEC) is a counseling resource the founder engaged with on 2026-04-30, not an audit, not a customer, not a funder. The mathematical content of the paper (the four axioms, the uniqueness proof, the bound theorem, the nine axes, the falsification ledger) is unchanged and correct. The published paper at [DOI 10.5281/zenodo.19951520](https://doi.org/10.5281/zenodo.19951520) carries the same correction notice. This announcement/playbook draft is preserved for history; the corrected ground truth lives in [`papers/v3/OUROBOROS_THESIS_V3.md`](../OUROBOROS_THESIS_V3.md) and [`README.md`](../../../README.md).

---

# Zenodo Submission Playbook — Ouroboros Thesis v3

**Concept DOI line:** Ouroboros Thesis (v1 → v2 → v3) — Zenodo concept-DOI bridges all three.
**v3 target window:** Same day as arXiv acceptance, or within 24 hours.
**Author:** Stephen P. Lutar (ORCID 0009-0001-0110-4173)
**Predecessor v1 DOI:** [10.5281/zenodo.19867281](https://doi.org/10.5281/zenodo.19867281)
**Predecessor v2 DOI:** [10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129)

## What you're uploading

The Zenodo v3 record is the **canonical, versioned, citable** form of the paper. arXiv is the open-access pre-print; Zenodo is the long-term archival record with a real DOI that doesn't break.

Files to attach to the Zenodo record:

1. `OUROBOROS_THESIS_V3.pdf` — typeset paper
2. `OUROBOROS_THESIS_V3.md` — markdown source (CC BY 4.0 mirror)
3. `ZENODO_METADATA_V3.json` — the metadata used for upload (for reproducibility)
4. `THESIS_PROOF_BUNDLE.json` — signed proof anchor (DOIs, commit SHAs, test counts)
5. `OUROBOROS_THESIS_V3.bib` — BibTeX file for citing v3

Total upload size: under 5 MB.

## Steps

1. **Login to zenodo.org** with the same account that holds v1 + v2.
2. **Open the v2 record:** [zenodo.org/records/19934129](https://zenodo.org/records/19934129).
3. **Click "New version"** — Zenodo will pre-populate metadata from v2 and assign a fresh version DOI under the same concept DOI.
4. **Replace the metadata** using `ZENODO_METADATA_V3.json` as the canonical reference. Specifically:
   - Title: as in JSON
   - Version: `3.0.0`
   - Publication date: 2026-05-01 (or actual upload date)
   - Description: as in JSON (HTML allowed)
   - Keywords: copy 15-keyword list from JSON
   - License: CC BY 4.0
   - Related identifiers:
     - `10.5281/zenodo.19867281` — `isNewVersionOf`
     - `10.5281/zenodo.19934129` — `isNewVersionOf`
     - GitHub repo URL — `isSupplementTo`
     - arXiv ID (once assigned) — `isIdenticalTo`
   - References list: copy from JSON
   - Subjects: cs.CR, cs.AI, math.HO
5. **Upload the 5 files.** Confirm checksums.
6. **Save draft** — review everything before publishing.
7. **Publish.** Zenodo mints the v3 DOI immediately. Save it.

## After publishing

| Action | Where |
| --- | --- |
| Update org `.github` README with v3 DOI badge | github.com/szl-holdings/.github |
| Update personal profile README with v3 DOI badge | github.com/stephenlutar2-hash |
| Update `ouroboros-thesis` repo description with all three DOIs | github.com/szl-holdings/ouroboros-thesis |
| Cut a GitHub release on `ouroboros-thesis` tagged `paper-v3-1.0.0` | (release notes already drafted) |
| Add v3 DOI to LETTER_TO_MOM.md and UNIFIED_PAYLOAD_INDEX.md | local payload |
| Post Substack + Medium long-form announcements | szlholdings.substack.com / @stephen_38454 |
| Post LinkedIn announcement | linkedin.com/in/stephen-l-279315240 |
| Post X thread | (handle TBD) |

## Concept DOI hygiene

Zenodo gives you two DOIs per published record:
- **Version DOI** — points to v3 specifically
- **Concept DOI** — points to "the latest version" of the Ouroboros Thesis line

For citations going forward, use the **version DOI** (10.5281/zenodo.[v3 ID]). For "always cite the latest" links (e.g., a permalink in the org README), use the concept DOI.

The concept DOI was already established at v1; v3 inherits it automatically when published as a new version of v2 (which itself was a new version of v1).

## Failure modes

| Failure | Action |
| --- | --- |
| Zenodo upload fails with "file too large" | Compress the PDF; the source MD is plain text and small. |
| Zenodo metadata validation rejects a related identifier | Verify the predecessor DOIs are spelled exactly as `10.5281/zenodo.19867281` (no `https://doi.org/` prefix in the identifier field). |
| Concept DOI doesn't link to v3 | Wait 60 minutes; Zenodo's concept-DOI propagation is async. If still broken after 24h, contact info@zenodo.org with both record IDs. |
| arXiv ID hasn't been assigned yet at Zenodo upload time | Publish the Zenodo record without the arXiv `isIdenticalTo` identifier, then add it via "Edit" → "Save" once arXiv is live. |

## Citation forms

After publication, the paper should be cited in three forms:

**APA:**
> Lutar, S. P. (2026). Ouroboros Thesis v3 — The Lutar Invariant: A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems. Zenodo. https://doi.org/10.5281/zenodo.[v3 ID]

**BibTeX:**
```bibtex
@article{lutar2026ouroborosv3,
  title   = {Ouroboros Thesis v3 — The Lutar Invariant: A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems},
  author  = {Lutar, Stephen P.},
  year    = {2026},
  publisher = {Zenodo},
  version = {3.0.0},
  doi     = {10.5281/zenodo.[v3 ID]},
  url     = {https://doi.org/10.5281/zenodo.[v3 ID]},
  orcid   = {0009-0001-0110-4173}
}
```

**Markdown (for org README):**
```markdown
[![DOI v3](https://img.shields.io/badge/DOI%20v3-10.5281%2Fzenodo.%5Bv3%20ID%5D-blue?style=flat-square)](https://doi.org/10.5281/zenodo.[v3 ID])
```
