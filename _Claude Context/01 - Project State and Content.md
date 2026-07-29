# 01 - Project State and Content

Detail and history. Current status lives in `00 - START HERE.md`. Standing rules
live in `CLAUDE.md` at the folder root. Last updated: 2026-07-28.

## Project snapshot

- HemoSim is a free, public, tiered, case-based hemodynamics curriculum on Wix.
  Live site: **hemosim.org** (not .com). Deadline: **September 1, 2026**.
- It is Part 1 (web curriculum) of a two-part fellowship course. Part 2 is an
  in-person simulation day: PA-catheter station, tools station (LiDCO plus PLR),
  and four ACT scenarios.
- The working deliverable is a Word content outline by expertise level, mapping
  all source content into three learner levels. Current version: **V8**.

## People and workflow

- **Neal Chaisson, MD**, owner. Pulmonary and critical care, fellowship director,
  Cleveland Clinic. Style: direct, no sycophancy, ready-to-use deliverables. See
  `CLAUDE.md` for the locked writing rules. Any change to the live Wix site must
  be reviewable before he makes it permanent.
- **Gustavo Garcia Chavez**, medical student writing and expanding the Notion
  content.

**Review loop (current, locked 2026-07-12).** Per module there is a Word edit doc
in `Module Edit Docs/`. Neal edits wording directly with track changes and writes
any layout or figure request in [brackets]. Claude then applies the wording to
the corresponding page and the layout notes to the CSS, and regenerates. Wording
is edited natively in the doc. Styling is described in brackets, because a Word
file cannot set web formatting.

To read an annotated doc, unzip it and parse both `word/comments.xml` and the
`w:ins` and `w:del` elements in `word/document.xml`. Never overwrite an annotated
copy.

*(Superseded: an earlier loop used tracked-changes .docx files in Google Drive.
Google Drive is no longer used at all. Everything is in Dropbox under /Claude.)*

## Outline version history

All versions live in `Hemosim COntent Outlines for Wix Build/`.

- **v1** (Jun 27): first per-level outline.
- **v2** (Jun 29): added both PowerPoint decks, Proposal 2026, first Notion scrub.
- **v3** (Jun 29): added a fully recursive Notion crawl (roughly 55 to 60 pages)
  plus the Appendix A inventory.
- **v4** (Jun 30): applied Neal's v3 review. Moved microcirculation and venous
  return to Informed, added Wix "What is shock" sourcing, the fourth unifying
  equation, the Novice PAC thermodilution and Fick how-to, built out Frontier,
  added Appendix B.
- **v5** (Jul 3): Neal and Gustavo's edited copy. Added the Notion page hierarchy
  to Appendix A, attribution rules, sign-up link, roughly 33 comments.
- **v6** (Jul 3): built from the V5 review plus a fresh Notion crawl. Reordered
  Novice N4 to N6 (framework before ACT), added the Informed "At the Bedside"
  module, added DSI (HR/DAP) to vasoplegia, folded in the eight heart-lung
  scenario pages.
- **v7** (Jul 12): Neal's review version. The PAC topic docs appeared alongside it.
- **v8** (current): built from Neal's V7 review plus the PAC topic docs. Appendix B
  was split per V7 request C46 into "Needs your attention" and "Resolved".

## V8 outline structure

**Part 1, design architecture and conventions.** Defining shock; the three
expertise levels; the onion-layer model; the clinical method (B.U.S. and ACT,
with AHE inside the Test step); the three principles and the unifying equation;
the shock-type diagnostic grid explained by curve physiology; how the web
curriculum maps to the simulation day; navigation, graphics, and sources; website
infrastructure notes.

**Part 2, the three expertise pathways.**

*Novice, N0 to N8.* N0 orientation; N1 what shock is and why hemodynamics
matters; N2 oxygen delivery as the organizing principle, with an At the Bedside
offshoot on recognizing a low DO2/VO2 mismatch; N3 recognizing shock at the
bedside; N4 the big-picture circulatory map; N5 connecting the physiology to the
shock-type grid (the key integration), with an At the Bedside offshoot on RAP and
volume status; N6 the ACT method; N7 PA catheter across four mastery topics; N8
put it together.

Both Novice offshoots are optional side paths that open in a new tab so the
reader does not lose their place in the main flow.

*Informed, I1 to I17.* I1 physiologic foundations; I2 At the Bedside (normotensive
shock, pulse pressure, hemodynamic phenotype); I3 pressure measurement and
waveform fundamentals; I4 Interface I, LV to arterial system; I5 Interface II,
arterioles to capillaries; I6 microcirculation and the vascular waterfall; I7
Interface III, capillaries to right atrium; I8 venous return in depth; I9
Interface IV, RV to LA; I10 tying the loop together; I11 hemodynamic monitoring
tools; I12 heart-lung interactions in arterial pressure monitoring; I13
evaluating arterial systolic and pulse-pressure variation; I14 right-atrial and
CVP waveform interpretation; I15 PA catheter interpretation beyond the Novice
basics; I16 measuring cardiac output; I17 apply.

*Expert, E1 to E8.* E1 arterial system and ventricular-arterial coupling; E2
heart-lung interactions (the integrating module); E3 RV-PA coupling and pulmonary
load; E4 Interface IV at the bedside and venous congestion; E5 unifying and
advanced shock models; E6 advanced cardiac output and minimally invasive
monitoring; E7 advanced echo-based cardiac output; E8 frontier topics.

**Parts 4 to 6 and appendices.** Part 4 the simulation day (PA-catheter
mastery station, ACT plus Guyton and Starling scenarios); Part 5 source
documents; Part 6 sources of truth for fact-checking; Appendix A the Notion page
hierarchy (baseline July 3 recursive crawl); Appendix B open items, split into
"Needs your attention" and "Resolved".

*Note: V8 has no Part 3. Earlier versions carried a Part 3 inventory table.*

## Sources

**`_Source Library/INDEX.md` is the authoritative source map.** It carries the
per-module source manifest, the figure catalogue, the orphan list, and the gap
report. Read it before any module build rather than relying on the summary here.

**Build rule:** never rebuild a module from the V8 outline alone. Open its
sources in INDEX.md, including the speaker notes and the published Wix version.

Principal sources:

- **`Assessing Shock - 2024 (with voice).pptx`**, 51 slides. The canonical Novice
  spine: DO2, B.U.S., the four-interface unifying equation, the shock grid, ACT,
  the 79-year-old case, RAP and volume responsiveness. Speaker notes on 49 of 51
  slides.
- **`Hemodynamics module - v2022 full.pptx`**, 412 slides. The Informed and Expert
  backbone. "Regulation of Circulatory Flow" (slides 43 to 67) is the deep N4 and
  N5 physiology. "Tools" (slides 69 to 107) covers perfusion markers, mottling,
  ScvO2, CO2 gap, and preload-responsiveness logic. Speaker notes on 213 slides.
- **`PAC Modules Patrick Lindsay V1.pptx`**, 124 slides. **The authoritative PAC
  teaching source**, a seven-module PAC course that maps cleanly onto the four N7
  topics. Supporting PAC decks are also in the library.
- **PAC Topic 1 to 4 .docx files.** These are **not** teaching prose. They are
  board-style multiple-choice question banks, roughly 20 questions each with
  correct answer and explanation. They are the sim-day cognitive-test content
  (V7 C36: LMS test, 10 of 20, 90 percent threshold). Every item must be covered
  by the N7 module pages.
- **`Hemodynamics Proposal 2026.docx`**: goals, objectives, ABIM blueprint,
  sim-day design.
- **Notion workspace**: the evolving conceptual source. Fully exported into the
  library (93 markdown pages, 336 images, 2 CSV).
- **Wix (hemosim.org)**: the published, edited pages. 29 captured. **Preferential
  source for final wording and reference lists.** Interface IV is fully built
  there and is the primary source for it.

**Attribution rule (Neal, V5):** reference every source with a link. Attribute any
graphic that has an attribution in Notion, Wix, or the slides. AI-generated Wix
and Notion graphics need none. All pptx graphics need attribution if used.

## Notion structure and access

Root page "HemoSim", id `23a0235473e8802f8281e97d0531b204`. Organized by
Foundations and Principles plus the four Interfaces (each with
Physiology-Correlation and At-the-Bedside children), plus a Heart-Lung
Interactions module. The authoritative hierarchy is Appendix A of the outline,
which is Gustavo's map.

Eight heart-lung "At the Bedside" scenario pages exist, all with graphics: five
spontaneous breathing (LV dysfunction, RV dysfunction, intra-abdominal
hypertension, COPD and asthma, cardiac tamponade) and three positive-pressure
ventilation (ARDS, LV dysfunction, relative and absolute hypovolemia). Assessing
Vasoplegia carries the Diastolic Shock Index (DSI = HR/DAP). Fluid Responsiveness
has a test-selection summary table. CVP Waveform Alterations is still empty and
remains a build task.

**Access:** pages are public. Read via the Claude-in-Chrome browser (navigate,
then scrape `.notion-page-content`; sanitize tokens over 22 characters to avoid
the content filter). The Notion MCP connector has 404'd in-session, because the
credential is cached at session start and only a fresh session picks up new auth.
Crawl fully recursively. Neal QC-checks by naming deep pages.

A full Notion export already lives in `_Source Library/notion/extracted/`, so
re-crawling is usually unnecessary.

## Conventions and key decisions

- Three levels: Novice, Informed, Expert. Onion-layer model, with deeper branches
  tagged "Physiology Correlation" and "At the Bedside".
- Clinical method: B.U.S., then ACT (Assess, Create hypothesis, Test), with AHE
  (Tone, Filling, Flow) inside the Test step. The Test step must name the
  measurable parameter that narrows the differential or proves an intervention
  worked.
- **Unifying hydraulic model across all four interfaces**, introduced at Novice:
  I, MAP minus Pcrit = SVR times CO; II, Pcrit minus MSFP = arteriolar resistance
  times CO; III, MSFP minus RAP = VR times CO; IV, mean PAP minus LAP = PVR times
  CO.
- Naming: Interface III is "Capillaries to Right Atrium". Interface IV is "RV to LA".
- Normotensive shock, pulse pressure, and etiology-versus-phenotype belong to the
  Informed "At the Bedside" module, deliberately kept out of the simple Novice grid.
- **Writing standard (locked):** connected prose, not bullet dumps. Carry the
  module-to-module thread naturally in the opening and closing prose. No boxed
  recap, no boxed bridge.
- **Figures:** deck figures from the .pptx, Wix and Notion figures via browser,
  animations as an exported static frame. Default cap 520px wide.
- Website infrastructure: capture every case answer with a timestamp and an
  opaque participant ID so one learner's answers link across modules, export to
  Dropbox, and keep a user sign-up link prominent (signing up is what carries
  progress across devices). Raw IP capture was dropped on 2026-07-30 in favour of
  the participant ID. Full design in file 02 under "Linking one learner's answers
  across modules".

## Open items

- **Six pages predate the 2026-07-23 rebuild** and are still at the original
  2026-07-13 depth: both Novice offshoots (`bedside-do2-vo2.html`,
  `rap-volume.html`) and the four N7 topic pages. Bring them to the N1 to N8
  depth standard when the review pass allows.
- Confirm exact citations for ANDROMEDA-PEGASUS, ANDROMEDA-SHOCK 2, and the
  Pinsky TPP figure. Do not fabricate.
- Build the CVP Waveform Alterations page in Notion.
- Create the Clinical Markers clinical example.
- Remaining Appendix B cleanup items. The two under "Needs your attention" are
  Informed and Expert only (the ANDROMEDA and Pinsky citations, and the level of
  the two new arterial modules). Neal is following up with Gustavo. Neither
  blocks the Novice build.
- Notion and Wix were not re-crawled during the N1 to N5 depth pass. If specific
  passages are still missing, point at them directly.

## Access mechanics and gotchas

- PHI, Cleveland Clinic OneDrive, work SharePoint, and work email are off limits.
  See `CLAUDE.md`.
- Google Drive is not used. Everything is in Dropbox under /Claude.
- Node is not installed. python-docx is, and is used to build the .docx files.
- The browser extension forces https and cannot open local `file://` paths. To
  preview the site, open the HTML directly or serve it over local http.

## Current file inventory (2026-07-28)

**In this folder** (`Dropbox/Claude/CCM/Fellowship/Hemosim`):

- `CLAUDE.md`, standing rules, loads automatically.
- `_Claude Context/`, files 00 to 03 plus `HemoSim Graphics Follow-Up.md`.
- `_Source Library/` (1.0 GB), the durable capture: `INDEX.md`,
  `INGESTION PLAN.md`, `decks/` (9 decks as markdown with speaker notes, plus
  374 figures in `decks/images/`), `docs/` (6 source .docx), `notion/extracted/`,
  `wix/` (29 published pages), and five build scripts.
  The two Markdown files and the five `.py` scripts **are tracked in git**
  (roughly 98 KB, they diff readably and are expensive to lose). Everything else
  in the folder is excluded. The scripts are `make_edit_docs.py` (regenerates the
  Word edit docs from the HTML), `assemble_rebuild.py`, `extract_all.py`,
  `wix_capture.py`, and `banner_gen.py`. `build_pilot_v8.py`, which generated the
  pilot pages, was lost with an old scratchpad and is not recoverable.
- `Hemosim COntent Outlines for Wix Build/`, outline v1 through v8.
- `Module Edit Docs/`, 13 Word edit docs (N1 to N8, the four N7 topics, and the
  two offshoots).
- `HemoSim Base Files for Claude Learning/` (238 MB), decks and proposal.
- `PA Catheter Topics/` (60 MB), Topic 1 to 4 .docx plus the "Additional PA
  Catheter Data" pptx decks.
- `PAC Simulation Mastery Checklist - Student Handout.docx`.
- `web-pilot (ARCHIVED 2026-07-25...)`, a frozen copy. Not the live version.

**Outside this folder:** `~/Claude/hemosim-web`, the live site code, its own
private GitHub repo with its own `CLAUDE.md`.

**Version control:** this folder is the private GitHub repo `hemosim-content`,
tracking working documents only. See `03 - Git and GitHub Setup.md`.
