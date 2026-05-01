# Pre-Publish Submission Checklist

Run this before clicking **Publish** on Zenodo, **Submit** on arXiv, or **Publish release** on GitHub. Order matters — Zenodo first (mints DOI), then update the GitHub release notes and arXiv comments with the DOI, then publish those.

---

## 🔍 Paper integrity (5 min)

- [ ] Open `paper/ouroboros-thesis-v2-empirical.pdf` and skim every page.
- [ ] Title page shows: title, subtitle, "Stephen P. Lutar Jr. — SZL Holdings", "April 30, 2026"
- [ ] Epigraph (page 2) is the **ouroboros-chewing-through-its-own-body** quote (NOT the cracks quote — that one belongs to the blog).
- [ ] §3.7 Falsification ledger lists F1 through F9.
- [ ] §10 Reproducibility manifest shows the real commit SHAs (`e9fc4b8`, `69a5416`, `fe3217a`) and file blob SHAs.
- [ ] Acknowledgments section + "Author's note on the epigraph" paragraph present.
- [ ] No "TODO" or "[placeholder]" strings (search the markdown to confirm: `grep -i "todo\|placeholder\|XXXX" paper/ouroboros-thesis-v2-empirical.md` should return only the ORCID line and intentional XXXXXX DOI placeholders in template files).
- [ ] References section exists with all numbered citations resolved.

## 🧪 Replication harness (3 min)

- [ ] `experiments/analysis/pareto.ts` runs and outputs `cheap-bad, middle, good, expensive-best` on the verification fixtures.
- [ ] `study/randomization.ts` is deterministic across runs with the same seed.
- [ ] Each subdirectory has a README.
- [ ] LICENSE.txt at `experiments/` root says MIT.

## 🎓 Zenodo prep (5 min)

- [ ] Signed in to Zenodo as the v1 owner.
- [ ] `submission/zenodo-metadata.json` is finalized.
- [ ] Decided on license: **CC BY 4.0** (recommended).
- [ ] Have the v1 DOI handy: `10.5281/zenodo.19867281`
- [ ] Read `ZENODO_PLAYBOOK.md` and clicked "New version" (NOT "Edit") on the v1 record.

## 📝 arXiv prep (5 min)

- [ ] arXiv account verified.
- [ ] Endorsement secured for cs.SE OR plan to use cs.AI primary instead.
- [ ] Abstract (`arxiv-abstract.md`) is ≤250 words. *(Verified: 248 words.)*
- [ ] Read `ARXIV_PLAYBOOK.md`.

## 🚀 GitHub release prep (3 min)

- [ ] `release/RELEASE_NOTES.md` reviewed.
- [ ] `ouroboros-v2-payload.zip` is freshly built.
- [ ] Decided whether to commit `v2_build/` to the repo first (recommended) or attach as binaries only.
- [ ] Read `GITHUB_RELEASE_PLAYBOOK.md`.

---

## 🔁 Publish order

1. **Zenodo "New version"** → captures DOI (e.g. `10.5281/zenodo.19934129`)
2. **Replace `XXXXXXXX` in:**
   - `release/RELEASE_NOTES.md`
   - `submission/arxiv-abstract.md` (if referenced)
   - `blog/companion-post.md`
   - `CITATION.cff` (if pushing to repo)
3. **GitHub release `v2.0.0`** → tag, attach PDF + zip, paste release notes
4. **arXiv submit** → paste abstract, list Zenodo DOI in Comments field
5. **Wait 12-48h for arXiv accept**
6. **Update Zenodo record** → add arXiv ID as related identifier (`is identical to`)
7. **Update v1 record** → add v2 DOI as `is previous version of` (makes link bidirectional)
8. **Publish blog post** with both DOIs.

---

## 📡 Announcement copy (ready to use)

### Twitter/X

> v2 of the Ouroboros Thesis is up — empirical companion to the v1 position paper.
>
> 142/142 tests, three production case studies, a §3.7 falsification ledger, and a pre-registered audit study with a null commitment.
>
> 📄 Zenodo: https://doi.org/10.5281/zenodo.19934129
> 📝 arXiv: https://arxiv.org/abs/2604.XXXXX
> 🚀 Repo: https://github.com/szl-holdings/ouroboros-thesis/releases/tag/v2.0.0
> 📰 Why a companion, not a revision: [link to blog post]

### LinkedIn / longer post

> I shipped v2 of the Ouroboros Thesis today — an empirical companion to last week's position paper.
>
> The thesis is the same: bounded loops with measurable convergence should be a runtime primitive for AI systems, not an implementation detail. What's new is the receipt. v2 cites the actual TypeScript modules, names the 142 tests, pins commits with file blob SHAs, and runs three production case studies on the same kernel.
>
> The part I'm most willing to be wrong about: there's a §3.7 "falsification ledger" listing nine load-bearing claims paired with the specific observations that would refute each one — including a pre-registered commitment to publish a null result for the audit study.
>
> If you find a falsifier I missed, I want to know.
>
> Paper: https://doi.org/10.5281/zenodo.19934129
> Replication harness (MIT): https://github.com/szl-holdings/ouroboros-thesis

---

## 📚 Where everything lives after publish

| Asset | URL |
|---|---|
| Concept DOI (always latest) | `https://doi.org/10.5281/zenodo.19867281` (resolves to latest version) |
| v1 version DOI | `https://doi.org/10.5281/zenodo.19867281` |
| v2 version DOI | `https://doi.org/10.5281/zenodo.19934129` (mint after publish) |
| arXiv | `https://arxiv.org/abs/2604.XXXXX` |
| GitHub release | `https://github.com/szl-holdings/ouroboros-thesis/releases/tag/v2.0.0` |
| Replication harness | `https://github.com/szl-holdings/ouroboros-thesis/tree/v2.0.0/experiments` |
| Companion blog | wherever you host (Medium, Substack, personal site, or GitHub Pages) |

---

🎯 **Done means:** Zenodo v2 record live, GitHub `v2.0.0` release tagged, arXiv submission accepted, blog post published, Zenodo↔GitHub linked for future auto-archival.
