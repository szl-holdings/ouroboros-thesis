# v2.0.0 — The Loop Is the Product

**Empirical companion to [The Ouroboros Thesis (v1)](https://zenodo.org/records/19867281).**

📄 **Paper (PDF):** attached to this release as `ouroboros-thesis-v2-empirical.pdf`
🎓 **Zenodo DOI:** [10.5281/zenodo.19934129](https://doi.org/10.5281/zenodo.19934129) *(replace after Zenodo publish)*
📝 **arXiv:** [arXiv:2604.XXXXX](https://arxiv.org/abs/2604.XXXXX) *(replace after arXiv accept)*
📰 **Companion blog post:** `blog/companion-post.md`

---

## TL;DR

v1 was a position paper. It said bounded loops with measurable convergence should be a runtime primitive, not an implementation detail, and it made no benchmark claims.

v2 is the empirical companion. It cites the actual TypeScript modules. It names the 142 passing tests. It enumerates the five trajectory classes and the stakes-modulated budget fractions the shipped allocator uses. It pins commits and publishes file blob SHAs. It pre-registers a small-N audit study and commits to publishing the null result.

If v1 was the design, v2 is the receipt.

## What's in this release

### 📄 Paper (`paper/`)
- `ouroboros-thesis-v2-empirical.md` — source markdown (~550 lines, ~40 KB)
- `ouroboros-thesis-v2-empirical.pdf` — typeset 20-page PDF (CC BY 4.0)
- `paper.css` — typesetting stylesheet (used by weasyprint)

### 🧪 Replication harness (`experiments/`) — MIT licensed
- `frontier-sweep/sweep.ts` — Pareto frontier extractor for §5.5
- `analysis/pareto.ts` — independent test-case-verified extractor (output: `cheap-bad, middle, good, expensive-best`)
- `shared/trace-loader.ts` — loads `OuroborosTrace` JSON from `aef-evidence-ledger`
- `fixtures/` — synthetic A11oy / Amaru small + medium fixtures

### 📋 Study protocol (`study/`) — pre-registered
- `PROTOCOL.md` — IRB-shaped protocol for §5.4 (trace-aided audit review)
- `consent-form.md` — informed consent
- `primer.md` — participant onboarding doc
- `randomization.ts` — deterministic mulberry32 + SHA-256 seeded randomization (verified)
- `answer-key-template.json` — schema for grading
- `recruit-email.md` — participant outreach template

### 🚀 Submission kit (`submission/`)
- `zenodo-metadata.json` — full Zenodo metadata (paste-ready for the upload form)
- `ZENODO_PLAYBOOK.md` — step-by-step Zenodo "New version" workflow
- `arxiv-abstract.md` — ≤250-word abstract for arXiv
- `ARXIV_PLAYBOOK.md` — arXiv submission walkthrough
- `SUBMISSION_CHECKLIST.md` — final pre-publish verification

### 📰 Blog (`blog/`)
- `companion-post.md` — same-day-as-Zenodo announcement, ~700 words

---

## Reproducibility manifest

Pinned commits as of release:

| Repo | Commit | Date |
|---|---|---|
| `szl-holdings/ouroboros` (runtime) | [`e9fc4b8`](https://github.com/szl-holdings/ouroboros/commit/e9fc4b8) | 2026-04-30T20:22:26Z |
| `szl-holdings/ouroboros-thesis` (this paper) | [`69a5416`](https://github.com/szl-holdings/ouroboros-thesis/commit/69a5416) | 2026-04-30T20:22:25Z |
| `szl-holdings/szl-holdings-platform` | [`fe3217a`](https://github.com/szl-holdings/szl-holdings-platform/commit/fe3217a) | 2026-04-30T19:16:43Z |

Tests passing at release: **142/142**

File blob SHAs (first 12 hex) for the four kernel modules and the runtime contract test:

| File | Blob SHA | Bytes |
|---|---|---|
| `loop-kernel.ts` | `45c8ec05365f` | 5428 |
| `depth-allocator.ts` | `53bff43d612d` | 3922 |
| `consistency.ts` | `50ffb14763f7` | 2992 |
| `types.ts` | `2405571bc7af` | 5199 |
| `runtime-contract.test.ts` | `6ea059910acd` | 5768 |

---

## What v2 deliberately does NOT claim

- **Cross-system distillation** (v1 §8) remains a hypothesis. Promoting it to a result would be premature and against the spirit of an empirical companion.
- **Learned depth allocation.** The `EntropyDepthAllocator` is a heuristic pure-function controller. A learned policy is future work.
- **§5.4 positive result.** The trace-aided audit study is pre-registered with explicit commitment to publish the null if the data supports it.

See §3.7 (Falsification ledger F1–F9) for the full list of load-bearing claims paired with the observations that would refute them.

---

## License

- **Paper, blog, study materials:** CC BY 4.0
- **Replication harness (`experiments/`):** MIT
- **Runtime (`@szl-holdings/ouroboros`):** proprietary (separate repo)

---

## Citation

```bibtex
@misc{lutar2026loop,
  author       = {Lutar, Stephen P.},
  title        = {The Loop Is the Product: Measuring Bounded Recursion
                  as a System Primitive for Auditable AI},
  subtitle     = {An Empirical Companion to the Ouroboros Thesis},
  year         = 2026,
  month        = apr,
  publisher    = {Zenodo},
  version      = {2.0.0},
  doi          = {10.5281/zenodo.19934129},
  url          = {https://doi.org/10.5281/zenodo.19934129},
  note         = {Companion to \textit{The Ouroboros Thesis} (Zenodo: 10.5281/zenodo.19867281)}
}
```

## Credits & acknowledgments

Thanks to the Ouroboros runtime contributors, the `aef-evidence-ledger` schema reviewers, the NYSTEC pre-briefing reviewers (2026-04-30), and the readers who pushed for falsification conditions to be made explicit. Errors are mine.

— Stephen P. Lutar Jr., SZL Holdings
