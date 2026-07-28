# HemoSim Source Library - Ingestion Plan

**Purpose.** Capture EVERY source (PowerPoints, Notion, Wix, source docs) once, into a durable,
indexed library that lives in this project folder, so that every future build session can draw on
all of it. This exists because no single chat session can hold the whole corpus in memory
(~660 slides + ~55 Notion pages + Wix), and because the scratchpad where extractions are made is
CLEARED between sessions. If it is not written here, it is lost.

**The risk this removes (Neal, 2026-07-12):** "before we write the actual web site, I need claude to
ensure that we have ALL of the data from Wix, Notion and all the powerpoints... Not doing so risks
losing important build elements."

---

## Library structure

```
_Source Library/
  INGESTION PLAN.md      <- this file
  INDEX.md               <- master index + per-module source manifest + coverage/gap report
  decks/
    <deck-slug>.md       <- slide text + SPEAKER NOTES + image references, per slide
    images/<deck-slug>/  <- every embedded figure, named <deck>_slideNNN_<hash>.<ext>
  docs/
    <doc-slug>.md        <- full text of source .docx
  notion/                <- Notion workspace export (Markdown + CSV + images), extracted
  wix/                   <- per-page capture of the live site + figures
```

---

## STATUS

| Step | Source | Method | Status |
|---|---|---|---|
| 1 | All PowerPoints (9) | Local extraction: slide text + speaker notes + per-slide images | **DONE** 2026-07-12 |
| 2 | Source .docx (6) | Local extraction: full paragraph text | **DONE** 2026-07-12 |
| 3 | Notion workspace | Full page export of HemoSim root (Markdown+CSV, subpages ON) -> extracted from disk | **DONE** 2026-07-22 |
| 4 | Wix live site | Bulk fetch of every published page (server-rendered HTML) + figure URLs | **DONE** 2026-07-22 |
| 5 | INDEX + coverage matrix | Analyze all captured sources, map to modules, list gaps | **DONE for decks/docs; Notion + Wix manifests appended** 2026-07-22 |

### Step 4 result (completed 2026-07-22)
Wix content is server-rendered for SEO, so `wix_capture.py` bulk-fetched every page in
`pages-sitemap.xml` via curl (no browser needed) and extracted the main text + figure URLs.
**29 curriculum pages captured** into `wix/` (17 with substantial prose), including the published,
REFERENCED versions of: What is Shock, Introduction to Hemodynamics, the four Interface pages
(I cardiac + arterial, II, III, IV) and their sub-pages (Windkessel, CrCP, RAP assessment, RV
function, pulmonary artery physiology, waveform reflection, vasoplegia), the Four-Interface Model,
Manipulating DO2, Autoregulation, PA Catheter Education, Practical Evaluation of Shock. Note: the
`general-8-N` URLs are NOT stubs; they are real content pages (Wix internal names). Two pages
(a-unifying-hemodynamic-equation, circulation-as-a-closed-loop-system) are GRAPHIC-ONLY (figure URL
captured, no prose). `wix/_captured.md` indexes all pages with block/image counts.
**Wix's unique value: it is the most polished, published, and citation-bearing form of the
curriculum** - use it as the reference for final wording and references, even though the underlying
content originates in Notion.

### Step 3 result (completed 2026-07-22)
Exported the HemoSim root page with "Include subpages" ON (Markdown & CSV) via Neal's logged-in
browser; the ~310 MB zip downloaded directly and was moved into `notion/`. Extracted the nested
Part-1 zip. Captured: **93 markdown pages, 2 CSV databases, 336 images, ~307 MB**, preserving the
full tree (Curriculum Template -> Principle 1 four interfaces I-IV, Heart-Lung Interactions,
Principles 2-3, plus all the "Clinical Correlation" / "Physiological Correlation" onion-layer
subpages: Ea/Ees/TAC coupling, Windkessel, CrCP/vascular waterfall, venous return + Pmsf,
RV function + RV-PA coupling + 60/60 sign, VExUS/congestion, lactate & ScvO2 & PCO2-gap
pathophysiology, arterial waveform components). This is the richest Informed/Expert source and the
deep-physiology layer for Novice. Archive zip kept at `notion/HemoSim-Notion-export-2026-07-22.zip`;
working copy at `notion/extracted/`.

### Step 1-2 result (completed)
9 decks and 6 docs extracted. The two gaps that made earlier builds shallow are now closed:

| Deck | Slides | **Slides w/ speaker notes** | Images |
|---|---|---|---|
| Assessing Shock 2024 with voice | 51 | **49** | 25 |
| Hemodynamics module v2022 full | 413 | **213** | 187 |
| PAC Modules Patrick Lindsay V1 | 124 | 1 | 48 |
| Pulmonary Artery Catheter- 1 (1) | 33 | 11 | 35 |
| Pulmonary Artery Catheter- 1 | 31 | 7 | 32 |
| Right Heart Catheter Video Graphics | 16 | 16 | 11 |
| Pulmonary Artery Catheters | 16 | 4 | 12 |
| Pulmonary Artery Catheters 2 | 16 | 4 | 12 |
| PAC-based Cardiac Output | 16 | 0 | 12 |

Docs: PAC Simulation Mastery Checklist (314 para), Hemodynamics Proposal 2026 (894),
PAC Topic 1-4 question banks (268/253/200/243).
Total: **374 images**, ~123 MB library.

> **Why this mattered.** Prior builds used slide text ONLY. The "Assessing Shock ... with voice"
> deck carries its actual teaching narration in the speaker notes (49 of 51 slides), and v2022
> carries 213 more. That narration is the richest prose source in the project and was invisible
> until now. Any module written before 2026-07-12 was built without it.

---

## Method, source by source (repeatable)

### PowerPoints and docx (no dependencies, re-runnable)
`extract_all.py` walks the project, skipping our own deliverables
(`Module Edit Docs`, `web-pilot`, `_Claude Context`, outline versions, "Salient articles ... (not for course)").
For each .pptx it reads `ppt/slides/slideN.xml` for text, follows that slide's `.rels` to its
`notesSlide` for speaker notes, and follows image relationships to dump every figure (deduped by
md5, skipping anything under 8 KB, which filters icons/bullets). Images are named by slide so a
figure can always be traced to its source slide for attribution.
**Re-run this whenever a deck is added or updated.** A copy of the script is kept at
`_Source Library/extract_all.py`.

### Notion (needs a one-time action from Neal)
The Notion MCP connector is **not authorized** in these sessions (OAuth cannot be completed from a
non-interactive session), so programmatic access is unavailable. A manual page-by-page browser crawl
is the fallback but is slow, fragile, misses images, and has previously missed deep subpages.

**Preferred route - full workspace export:**
1. In Notion, open **Settings** -> **Workspace** -> **General**, then **Export all workspace content**
   (for a single space: open the HemoSim page -> `...` menu -> **Export**).
2. Format **Markdown & CSV**; toggle **Include subpages** ON; toggle **Include images/files** ON;
   "Everything" for content.
3. Notion emails a download link (large workspaces are processed asynchronously).
4. Drop the resulting **.zip into this project folder**, e.g. `_Source Library/notion/`.
5. Claude then extracts it from disk exhaustively (same pattern as the decks) - no browser needed,
   images included, structure preserved.

*Alternative:* grant the Notion integration page access (HemoSim page -> `...` -> **Connections** ->
add the integration), which makes the MCP `notion-fetch`/`notion-search` tools work for the whole
subtree.

### Wix
Browser capture of the published pages plus their figures. Note Wix is largely **downstream of
Notion** (Notion is the drafting source; Wix lags), so the unique value is the pages Neal built
directly in Wix (the **Interface IV** set is fully built per Neal) and any site-only graphics.
Bounded: capture the built pages, save text per page to `wix/`, and record figure URLs/sources.

### Reference PDFs (catalogued, not extracted)
`HemoSim Base Files/` and its `Additional Reading/` hold journal PDFs (Kenny Heart-Lung 1st Ed,
Lloyd-Donald, RHC, jpm-15-00207, mechanical ventilation text, etc.). These are **reference/citation**
material rather than teaching prose, and are copyrighted, so they are listed in INDEX.md but not
bulk-extracted. Pull specific passages on demand when a module needs a citation.
The "Salient articles for hemodynamics (**not for course**)" folder is excluded by Neal's own label.

---

## The mechanism that guarantees nothing is dropped

Capturing files is only half. `INDEX.md` carries two views:

1. **Per-module source manifest** - for each module (N1-N8, I1-I17, E1-E8): the exact source files,
   slide ranges, Notion/Wix pages that feed it, and whether its figures are captured.
2. **Reverse coverage / orphan list** - every captured source chunk tagged with the module(s) it
   feeds. Anything unclaimed surfaces as an **orphan**, which is precisely the "important build
   element" that would otherwise be lost.

**Final QC gate before the Wix build:** confirm that (a) every V8 outline node maps to >=1 source,
and (b) every sim-day cognitive question and psychomotor checklist item maps to teaching content in
a module (V7 C36). This replaces Neal spot-checking deep pages by hand.

---

## How build sessions must use this

1. Read `_Claude Context/00 - START HERE.md`, then this file, then `INDEX.md`.
2. For the module being built, open the source files named in its manifest - including the
   **speaker notes**, which carry the teaching narration.
3. Pull figures from `decks/images/` (filename encodes deck + slide for attribution).
4. After drafting, re-check the orphan list so nothing relevant was skipped.

**Do not** rebuild a module from the V8 outline alone. The outline is a spec/summary; the Source
Library is the content.
