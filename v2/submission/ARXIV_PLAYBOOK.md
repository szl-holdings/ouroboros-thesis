# arXiv Submission Play-by-Play

**Goal:** Cross-list the v2 paper to arXiv under cs.SE primary, cs.AI secondary, with the Zenodo DOI in the "Comments" field. arXiv is preferred-citation territory for the AI/SE community; Zenodo is your archival home with the DOI.

**File you'll upload:** `v2_build/paper/ouroboros-thesis-v2-empirical.pdf`
**Abstract you'll paste:** `v2_build/submission/arxiv-abstract.md` (≤250 words, already prepared)

---

## Step 0 — Account requirements (5 min, one-time)

- [ ] Create an arXiv account at [arxiv.org/user/register](https://arxiv.org/user/register) using `stephenlutar2@gmail.com` (or your preferred academic-facing email).
- [ ] **Endorsement check:** new submitters to cs.SE typically need an endorsement from someone who has already published in cs.SE. If you don't have one:
  - Option A: Ask a published cs.SE author you know to endorse you.
  - Option B: arXiv's `cs.AI` and `cs.LG` are open to most users after the first verified submission. You can submit primary as cs.AI instead and it will still appear in cs.SE if you list it as cross-list. This is allowed and common.
  - Option C: If endorsement is blocked, publish on Zenodo first (already done), wait, and try again with the Zenodo DOI as evidence.

---

## Step 1 — Start the submission (2 min)

1. Sign in at [arxiv.org/login](https://arxiv.org/login).
2. Click **"Start a new submission"** at [arxiv.org/submit](https://arxiv.org/submit).
3. Choose: **License** → CC BY 4.0 (matches Zenodo). Hit Continue.

---

## Step 2 — Upload (5 min)

arXiv accepts PDF directly OR LaTeX source. Since you have a clean weasyprint PDF and no LaTeX source, choose:

1. **Submission Format:** PDF
2. Upload `ouroboros-thesis-v2-empirical.pdf`
3. arXiv will run sanity checks (font embedding, page count, etc.). Address any warnings.

> If arXiv rejects the PDF for font/structure reasons (rare with weasyprint), you can convert to LaTeX via pandoc: `pandoc ouroboros-thesis-v2-empirical.md -o paper.tex --standalone` and submit `.tex` instead.

---

## Step 3 — Metadata (8 min)

| Field | Value |
|---|---|
| **Title** | `The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI` |
| **Authors** | `Stephen P. Lutar Jr. (SZL Holdings)` |
| **Abstract** | Paste the body of `arxiv-abstract.md` (the markdown headers + final word-count line removed; just the prose paragraphs) |
| **Comments** | `20 pages, 1 figure. Companion to Zenodo 10.5281/zenodo.19867281. v2 DOI: 10.5281/zenodo.19934129. Replication harness (MIT) at https://github.com/szl-holdings/ouroboros-thesis.` |
| **Primary Category** | `cs.SE` (Software Engineering) |
| **Cross-list** | `cs.AI` (Artificial Intelligence) |
| **MSC class** (optional) | leave empty |
| **ACM class** (optional) | `D.2.4 [Software/Program Verification]; I.2.0 [Artificial Intelligence: General]` |
| **Report number** | leave empty |
| **Journal reference** | leave empty (this is a preprint) |
| **DOI** | Paste your Zenodo v2 DOI here: `10.5281/zenodo.19934129` |

---

## Step 4 — Preview and submit (3 min)

1. Click **"Preview"**. arXiv generates a draft listing.
2. Verify: title, authors, abstract, categories, the Comments field showing the Zenodo cross-link.
3. Click **"Submit"**.

---

## Step 5 — Wait (12-48 hours)

arXiv has moderation. New submissions to cs.SE/cs.AI typically post in the next overnight cycle (10pm ET / 02:00 UTC). You'll get an email when:
- Submission is accepted → assigned an arxiv ID like `arXiv:2604.XXXXX`
- Submission is held for moderation → respond to moderator questions

If accepted, the paper is publicly listed by the next morning UTC.

---

## Step 6 — After it goes live

- [ ] Add the arXiv ID to your Zenodo record: edit metadata → Related identifiers → add `arXiv:2604.XXXXX` with relation "is identical to" or "is variant form of".
- [ ] Update GitHub release notes with the arXiv link.
- [ ] Update the companion blog post.
- [ ] Tweet/announce: "v2 of the Ouroboros Thesis is live: arXiv link + Zenodo DOI."

---

## Why both Zenodo *and* arXiv?

| Platform | Strength |
|---|---|
| **Zenodo** | Long-term archival. DOI. CC BY license enforcement. Bundles non-PDF artifacts (zip, datasets). Concept DOI for version succession. |
| **arXiv** | Discoverability in the AI/SE research community. Indexed by Google Scholar, Semantic Scholar, ConnectedPapers within hours. Citation conventions assume arXiv ID. |

You want both. Zenodo is the canonical archive; arXiv is the front door researchers actually walk through.
