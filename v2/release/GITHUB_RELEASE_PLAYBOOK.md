# GitHub Release Play-by-Play — v2.0.0

**Goal:** Cut a tagged GitHub release on `szl-holdings/ouroboros-thesis` so the v2 paper has a permanent versioned home with downloadable PDF, zip bundle, and signed source archive — and (if you connect Zenodo↔GitHub) auto-archives there too.

**Repo:** `szl-holdings/ouroboros-thesis`
**Tag:** `v2.0.0`
**Title:** `v2.0.0 — The Loop Is the Product`

---

## Path A — Use the GitHub web UI (easiest, 8 min)

### Step 1 — Push the v2_build folder to the repo (3 min)

If `v2_build/` isn't in the repo yet, get it there. Two options:

**Option 1 — Copy into a clone of the repo:**
```bash
cd /tmp
git clone https://github.com/szl-holdings/ouroboros-thesis.git
cp -r /home/user/workspace/v2_build /tmp/ouroboros-thesis/v2/
cd /tmp/ouroboros-thesis
git checkout -b v2-empirical-companion
git add v2/
git commit -m "feat(v2): empirical companion paper + harness + study + submission kit"
git push -u origin v2-empirical-companion
```

Then open a PR on GitHub, merge to `main`. Or if you prefer to ship straight to main, use `git checkout main` and skip the branch step.

**Option 2 — Just attach files to the release without committing them.** Releases can ship binaries that aren't in the repo. This is fine for the PDF + zip but means the markdown sources won't be browseable on github.com.

### Step 2 — Create the release (4 min)

1. Go to [github.com/szl-holdings/ouroboros-thesis/releases/new](https://github.com/szl-holdings/ouroboros-thesis/releases/new).
2. **Choose a tag:** type `v2.0.0` → "Create new tag: v2.0.0 on publish"
3. **Target:** `main` (or whatever branch has the v2 content)
4. **Release title:** `v2.0.0 — The Loop Is the Product`
5. **Description:** paste the entire contents of `v2_build/release/RELEASE_NOTES.md` (replace the `10.5281/zenodo.19934129` placeholder with your real Zenodo DOI once minted).
6. **Attach binaries:** drag in:
   - `ouroboros-thesis-v2-empirical.pdf` (the typeset paper)
   - `ouroboros-v2-payload.zip` (the full bundle)
   - Optionally: `companion-post.md`, `arxiv-abstract.md`, `zenodo-metadata.json`
7. **Set as the latest release:** ✅ check this
8. **Pre-release?** ❌ leave unchecked (this is a real release)
9. Click **"Publish release"**.

### Step 3 — Verify (1 min)

- [ ] [github.com/szl-holdings/ouroboros-thesis/releases/tag/v2.0.0](https://github.com/szl-holdings/ouroboros-thesis/releases/tag/v2.0.0) loads
- [ ] PDF opens when clicked
- [ ] Zip downloads and extracts cleanly
- [ ] Release notes render with proper headings/links

---

## Path B — Use the `gh` CLI (faster if you're comfortable with terminal, 4 min)

```bash
# From a clone of the repo with v2/ already committed:
cd /path/to/ouroboros-thesis

# Tag the release commit
git tag -a v2.0.0 -m "v2.0.0 — The Loop Is the Product (empirical companion)"
git push origin v2.0.0

# Cut the release with attached files
gh release create v2.0.0 \
  --title "v2.0.0 — The Loop Is the Product" \
  --notes-file /home/user/workspace/v2_build/release/RELEASE_NOTES.md \
  /home/user/workspace/v2_build/paper/ouroboros-thesis-v2-empirical.pdf \
  /home/user/workspace/ouroboros-v2-payload.zip
```

That single `gh release create` command does what Path A's web-UI Step 2 does.

---

## Step 4 — (Recommended) Connect GitHub ↔ Zenodo for auto-archival

Do this once and every future release auto-archives to Zenodo with a fresh DOI. Most ML/SE projects use this — it's the "GitHub release → Zenodo DOI" pattern.

1. Sign in to [zenodo.org](https://zenodo.org) (same account that owns v1).
2. Go to **Account → GitHub** ([zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)).
3. Authorize Zenodo to read your repos.
4. Find `szl-holdings/ouroboros-thesis` in the list → flip the toggle ON.
5. From now on, any GitHub release with a tag (like `v2.0.0`) automatically creates a Zenodo deposit linked back to that release.

> ⚠️ **For v2.0.0 specifically:** because you're publishing the v2 PDF as a *new version* of the existing v1 record (DOI 10.5281/zenodo.19867281), you should publish via the **manual Zenodo "New version" flow** (see `ZENODO_PLAYBOOK.md`), NOT via the GitHub auto-archive — the auto-archive creates a fresh top-level deposit with no version link to v1. Use the GitHub auto-archive for v2.0.1 and beyond.

---

## Step 5 — After release is live

- [ ] Pin the release on the repo home page: go to repo → Releases → click "v2.0.0" → it's the latest, so it shows in the sidebar automatically.
- [ ] Update the repo README:
  - Add a "📄 Read the paper" badge linking to the Zenodo DOI
  - Add an "🚀 Latest release" badge linking to `v2.0.0`
- [ ] Update the repo's "About" sidebar (gear icon top right of repo home) → set the website to your Zenodo concept-DOI URL.
- [ ] Cross-reference: in `CITATION.cff` (create if missing) point at the v2 DOI.

### Suggested `CITATION.cff` to add to the repo root

```yaml
cff-version: 1.2.0
message: "If you use this work, please cite it as below."
title: "The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI"
authors:
  - family-names: Lutar
    given-names: Stephen P.
    affiliation: SZL Holdings
date-released: 2026-04-30
version: 2.0.0
doi: 10.5281/zenodo.19934129  # replace with v2 DOI after minting
url: https://github.com/szl-holdings/ouroboros-thesis
license: CC-BY-4.0
type: article
identifiers:
  - type: doi
    value: 10.5281/zenodo.19867281
    description: v1 (concept DOI / position paper)
keywords:
  - adaptive computation
  - recursive systems
  - AI governance
  - auditable AI
  - decision receipts
```

GitHub auto-renders `CITATION.cff` into the "Cite this repository" button on the repo sidebar. That button is how most researchers will copy-paste your citation.

---

## What this gives you

After all steps:
- **Zenodo v2 record** with its own DOI, linked to v1 via "is new version of"
- **arXiv listing** in cs.SE / cs.AI with the Zenodo DOI in Comments
- **GitHub `v2.0.0` release** with the PDF + zip attached and full release notes
- **Companion blog post** with the cracks-as-openings quote
- **`CITATION.cff`** so anyone clicking "Cite this repository" gets a proper bibtex
- **Future auto-archival** for v2.0.1, v2.1, etc.

The whole stack — paper + harness + protocol + DOIs + tagged release — becomes one citeable, reproducible bundle.
