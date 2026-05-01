# Zenodo Publishing Play-by-Play — v2 Companion Paper

**Goal:** Publish v2 as a *new version* of the existing v1 record so the two share a concept DOI but each get their own version DOI. This is the same mechanism used for arXiv-style preprint succession.

**Existing v1 record:** [zenodo.org/records/19867281](https://zenodo.org/records/19867281)
**File you'll upload:** `v2_build/paper/ouroboros-thesis-v2-empirical.pdf` (20 pages, ~145 KB)
**Bundle you'll also upload (recommended):** `ouroboros-v2-payload.zip` (paper + harness + study + blog)

---

## Step 0 — Before you start (5 min)

- [ ] Sign in to Zenodo at [zenodo.org/login](https://zenodo.org/login) using the same account that owns v1 (the one tied to `stephenlutar2@gmail.com` / SZL Holdings).
- [ ] (Optional but recommended) Get an ORCID at [orcid.org/register](https://orcid.org/register) and link it under **Account → Settings → Linked accounts → ORCID** in Zenodo. ORCID makes you citeable forever even if your email changes.
- [ ] Decide license: **CC BY 4.0** is recommended (academic standard, lets people cite/build on it, you keep authorship). The alternative is CC0 (full public domain) if you want zero friction.

---

## Step 1 — Open the v1 record (2 min)

1. Go to [zenodo.org/records/19867281](https://zenodo.org/records/19867281).
2. Confirm you see an **"Edit"** or **"New version"** button on the right side. If you don't see it, you're not signed in as the owner — sign in first.
3. Click **"New version"**. (Not "Edit" — that would modify v1 itself, which you don't want.)

> Why "New version" and not a fresh upload?
> Zenodo creates a *concept DOI* the first time you publish, plus a *version DOI* per release. Using "New version" keeps v2 under the same concept DOI as v1, so anyone citing the concept DOI always gets the latest version, and anyone citing a specific version DOI gets exactly that snapshot. This is the cleanest scholarly record.

---

## Step 2 — Replace the file (3 min)

After clicking "New version" you'll land on an editing form pre-filled with v1's metadata.

1. **Files panel (top of page):** click the trash/X icon next to the v1 PDF to remove it.
2. Drag and drop **`ouroboros-thesis-v2-empirical.pdf`** into the upload area.
3. (Recommended) Also drag in **`ouroboros-v2-payload.zip`** as a supplementary file. Zenodo allows multiple files per record. The PDF stays the primary citable artifact; the zip is the replication bundle.

Do NOT click "Save" yet — keep editing the metadata below.

---

## Step 3 — Update the metadata (10 min)

Use the values from `v2_build/submission/zenodo-metadata.json` as your source of truth. Field-by-field:

| Field | Value |
|---|---|
| **Resource type** | Publication → **Preprint** |
| **Title** | `The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI` |
| **Subtitle** (if available) | `An Empirical Companion to the Ouroboros Thesis` |
| **Publication date** | `2026-04-30` |
| **Authors** | `Lutar, Stephen P.` — affiliation: `SZL Holdings` — paste your ORCID if you have one |
| **Description** | Paste from `zenodo-metadata.json` → `metadata.description` (already HTML-formatted) |
| **Version** | `2.0.0` |
| **Language** | English |
| **Keywords** | adaptive computation; recursive systems; AI governance; agent runtimes; decision receipts; auditable AI; loop budget; convergence traces; NIST AI RMF; EU AI Act; reproducibility |
| **License** | **Creative Commons Attribution 4.0 International (CC BY 4.0)** |
| **Access right** | Open Access |

### Related identifiers (this is the important one)

Click **"Add related identifier"** and add these three entries:

| Identifier | Relation | Resource type |
|---|---|---|
| `10.5281/zenodo.19867281` | **is new version of** | Publication / Preprint |
| `https://github.com/szl-holdings/ouroboros-thesis` | is supplement to | Software |
| `https://github.com/szl-holdings/ouroboros` | is supplement to | Software |

The first one is what tells Zenodo and Crossref this is the v2 of the v1 record.

### Notes (optional but useful)

Paste from `zenodo-metadata.json` → `metadata.notes`:

> Companion paper to Zenodo 19867281 (v1 position paper). v2 closes the v1 §9 experimental agenda with shipped, version-pinned implementations and pre-registered analyses. Falsification ledger (§3.7) and reproducibility manifest (§10) included. Replication harness is MIT-licensed; the runtime is proprietary.

---

## Step 4 — Save and preview (2 min)

1. Click **"Save"** at the bottom. Zenodo will validate the form.
2. Fix any red error markers (most common: missing license, missing description, empty author affiliation).
3. Click **"Preview"** to see the public-facing record. Check:
   - [ ] Title renders correctly
   - [ ] Author is `Lutar, Stephen P.` (not split weirdly)
   - [ ] Description paragraphs are formatted (not one wall of text)
   - [ ] PDF and zip both appear in Files
   - [ ] "Versions" sidebar shows both v1 (19867281) and v2 (your new draft)
   - [ ] Related identifiers show the v1 link

---

## Step 5 — Publish (1 min) — irreversible

> Once you click Publish, the version DOI is minted and **the record becomes immutable**. You can edit metadata later but you cannot replace files or change the DOI.

1. Click **"Publish"**.
2. Confirm in the modal.
3. Zenodo mints your version DOI (format: `10.5281/zenodo.19934129`).
4. Copy that DOI — you'll need it for arXiv, GitHub release notes, and the blog post.

---

## Step 6 — Right after publishing (10 min)

- [ ] **Update the GitHub release notes** (in `v2_build/release/RELEASE_NOTES.md`) — replace the `10.5281/zenodo.19934129` placeholder with your real DOI.
- [ ] **Cut the GitHub release**: follow `v2_build/release/GITHUB_RELEASE_PLAYBOOK.md`. Tag it `v2.0.0`.
- [ ] **Mint a Zenodo-GitHub link** (optional, but powerful): on Zenodo go to Account → GitHub, enable repo `szl-holdings/ouroboros-thesis`. Future releases auto-archive to Zenodo.
- [ ] **arXiv submission** (separate workflow): use `v2_build/submission/arxiv-abstract.md` and `v2_build/submission/ARXIV_PLAYBOOK.md`. Cross-reference the Zenodo DOI in your arXiv "Comments" field.
- [ ] **Update v1 record** (optional): go back to [zenodo.org/records/19867281](https://zenodo.org/records/19867281), click Edit, and add a related identifier `is previous version of: <new v2 DOI>`. This makes the link bidirectional.
- [ ] **Update the companion blog post** (`v2_build/blog/companion-post.md`) — replace any DOI placeholders.
- [ ] **Memory update for citation block:** the new "Cite as" should read approximately:
  > Lutar, S. P. (2026). *The Loop Is the Product: Measuring Bounded Recursion as a System Primitive for Auditable AI* (Version 2.0.0) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.19934129

---

## Common issues and fixes

| Symptom | Fix |
|---|---|
| "New version" button missing | You're not the v1 owner. Sign in with the right account. |
| Form blocks "Save" with red error | Scroll up — there's a missing required field (most often License or Description). |
| PDF rendered with wrong fonts | Re-render: `cd v2_build/paper && pandoc ouroboros-thesis-v2-empirical.md -o ouroboros-thesis-v2-empirical.html --standalone --toc --toc-depth=2 --metadata title="The Loop Is the Product" --metadata subtitle="An Empirical Companion to the Ouroboros Thesis" --metadata author="Stephen P. Lutar Jr. — SZL Holdings" --metadata date="April 30, 2026" --css paper.css --highlight-style=tango && weasyprint ouroboros-thesis-v2-empirical.html ouroboros-thesis-v2-empirical.pdf` |
| Want to add an author later (e.g., a collaborator) | Edit the published record's metadata — Zenodo allows author edits post-publish, just not file changes. |
| Need to fix a typo in the PDF after publish | Cut a v2.0.1 with "New version" again. Each version gets its own DOI; the concept DOI always resolves to the latest. |

---

## Why this matters (the 30-second version)

When you publish v2 on Zenodo with the "is new version of" relationship:
- The v1 → v2 lineage is machine-readable in Crossref, OpenAlex, Google Scholar, and Semantic Scholar within ~48 hours.
- Anyone who cited v1 will see "newer version available" via DOI resolvers.
- Your concept DOI becomes the durable canonical reference; people who cite it always get the freshest version.
- The §3.7 falsification ledger and §10 reproducibility manifest become permanently archived — the kind of thing a procurement officer can point to as "this work has staked claims and they are verifiable."
