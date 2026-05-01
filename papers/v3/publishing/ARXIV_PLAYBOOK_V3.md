# arXiv Submission Playbook — Ouroboros Thesis v3

**Target:** arXiv cs.CR primary, cs.AI + math.HO cross-list
**Window:** Mon 2026-05-04 18:00 ET → Tue 2026-05-05 14:00 ET (US announce window opens at this time)
**Author:** Stephen P. Lutar (ORCID 0009-0001-0110-4173)

## Pre-submission checklist

- [ ] PDF generated from `OUROBOROS_THESIS_V3.md` via Pandoc with proper math + bibliography
- [ ] PDF size under 10 MB (arXiv limit is 50 MB but tighter is faster review)
- [ ] All math compiles (no broken \( \), \[ \] expressions)
- [ ] No markdown italics in source (CC BY 4.0 typesetting)
- [ ] Both predecessor DOIs cited inline AND in references
- [ ] Reproducibility manifest references commit `e9fc4b86eae18bb7401b14cb0e53900ba8e47ad8`
- [ ] All 30+ references resolve to valid arXiv / DOI / journal URLs
- [ ] No personal contact info in the paper body (move to acknowledgments)
- [ ] Author affiliation: SZL Holdings (no street address)

## Endorsement requirement

cs.CR requires endorsement for first-time submitters. Stephen has prior arXiv submissions for v1 and v2 (verify on arxiv.org/a/lutar_s_1.html). If endorsement is still needed:
- Reach out to a published cs.CR author (security/cryptography researcher)
- Use the v1 + v2 DOIs as evidence of standing
- Endorsement email template:
  > Subject: Endorsement request for cs.CR submission
  >
  > Dr. [Name],
  >
  > I am submitting a paper to arXiv cs.CR titled "Ouroboros Thesis v3 — The Lutar Invariant: A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems." The paper has two predecessors already deposited: DOI 10.5281/zenodo.19867281 (position paper, Apr 28 2026) and DOI 10.5281/zenodo.19934129 (empirical companion, Apr 30 2026). I would be grateful for an endorsement.
  >
  > The paper proves uniqueness of a closed-form scalar trust aggregator under four axioms, including a novel inspectability axiom from Egyptian arithmetic. An open-source reference implementation passes 1,372 tests across 24 packages.
  >
  > arXiv endorsement code: [insert]
  >
  > Thank you,
  > Stephen P. Lutar (ORCID 0009-0001-0110-4173)

## Submission steps

1. **Generate the PDF** — see `BUILD_PDF.md` in this directory.
2. **Login to arXiv.org** with the same account used for v1 / v2.
3. **Start new submission**:
   - Primary archive: `cs.CR` (Cryptography and Security)
   - Cross-lists: `cs.AI` (Artificial Intelligence), `math.HO` (History and Overview)
   - License: CC BY 4.0
4. **Upload** the PDF. arXiv will TeX-process it; let it complete.
5. **Title:** Ouroboros Thesis v3 — The Lutar Invariant: A Nine-Axis Closed-Form Scalar Law for Runtime Trust in Agentic AI Systems
6. **Authors:** Stephen P. Lutar
7. **Abstract:** copy from §Abstract of the paper (cap at 1920 chars for arXiv).
8. **Comments field:** "v3 of the Ouroboros series. Companion runtime: github.com/szl-holdings/ouroboros (v6.1.0). 1,372 open-source tests. Compounds Zenodo DOIs 10.5281/zenodo.19867281 and 10.5281/zenodo.19934129."
9. **MSC class** (math.HO cross-list requirement): 11A67 (Other representations), 68P25 (Data encryption)
10. **ACM class** (cs.CR requirement): D.4.6 (Security and Protection), I.2.0 (General AI)
11. **Submit for moderation.** Hold a copy of the assigned arXiv ID.

## Post-submission

- arXiv replaces the live paper PDF when announced. Update the SZL Holdings org `.github` README with the arXiv ID + the v3 DOI within 6 hours.
- Tweet thread (see `companion/X_THREAD_V3.md`) goes live the morning after announcement.
- Substack + Medium long-form posts go live same morning.
- LinkedIn announcement same morning.

## Zenodo + arXiv coordination

The convention used in v1/v2: Zenodo DOI is minted on the day arXiv accepts the paper. The Zenodo upload includes the arXiv ID as a related identifier. The Zenodo concept-DOI for the Ouroboros thesis line bridges all three paper versions.

- Zenodo upload should happen within 24 hours of arXiv acceptance.
- Zenodo metadata file: `ZENODO_METADATA_V3.json` (in this directory).
- Files attached to Zenodo: PDF, markdown source, BibTeX file, full reproducibility manifest.

## Failure modes and recovery

| Failure | Action |
| --- | --- |
| arXiv rejects for "no novelty" | The novelty is the **uniqueness theorem** under axioms A1–A4 plus the **Egyptian inspectability** axiom. Resubmit with abstract sharpened to lead with the uniqueness claim. |
| arXiv requests cs.CR endorsement | Send endorsement request emails (template above) to 3 cs.CR authors in parallel. |
| arXiv flags math.HO cross-list | Drop math.HO; keep cs.CR + cs.AI. The Egyptian arithmetic content stays in the paper but the primary contribution is computational. |
| Pandoc PDF build fails on math | Use the LaTeX fallback path in `BUILD_PDF.md`. |
| Citations don't resolve | All references must have a DOI, arXiv ID, or journal URL. Verify each one before submission. |

## Embargo discipline

- Do not publicly post the paper until arXiv announces it.
- Substack/Medium drafts can be staged but not published before arXiv goes live.
- The first public mention should reference the arXiv ID directly.
