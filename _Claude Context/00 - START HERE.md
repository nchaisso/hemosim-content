# START HERE

Orientation and current status for HemoSim. Last updated: 2026-07-28.

This file holds **current state only**. Standing rules live in `CLAUDE.md` at the
folder root and load automatically every session. History and detail live in
files 01 and 02. Keep this one short: if it stops being scannable in a minute,
move the detail out.

## Read order

1. This file, for where things stand
2. `01 - Project State and Content.md`, people, sources, Notion hierarchy (stale, see below)
3. `02 - Build Strategy and Decisions.md`, build plan and locked decisions
4. `03 - Git and GitHub Setup.md`, how version control works here
5. `04 - Module Edit Workflow.md`, the procedure for applying a reviewed edit doc
   (read when a module comes back, not every session)

Before any module build, also read `_Source Library/INDEX.md` to know which
sources feed which module. Build rule: never rebuild a module from the V8 outline
alone. Open its sources, including speaker notes and the published Wix version.

## The project in one paragraph

Neal is building HemoSim, a free public tiered hemodynamics curriculum on Wix
(hemosim.org), due September 1, 2026. Content is captured in the V8 outline
(Novice, Informed, Expert). The real site gets built natively in Wix so Neal can
edit it himself. The HTML pilot is the design template and narrative standard,
not the content store. Interactive knowledge checks get added later as reviewable
drop-in components.

## Where things stand

**Content: the Novice spine is complete.** N1 through N8 were rebuilt deep on
2026-07-23 from the full Source Library (deck slides plus speaker notes, Notion,
Wix), with real figures embedded and Wix as the preferential source for final
wording and citations. Method and locked parameters are in file 02 under
"N1-N8 FRESH REBUILD". Site content has not changed since that date.

**Where the site code lives.** The pilot moved to its own private GitHub repo,
`hemosim-web`, on 2026-07-24, checked out at `~/Claude/hemosim-web`. It has its
own `CLAUDE.md`. The local `web-pilot` folder here was renamed ARCHIVED on
2026-07-25 and is a frozen copy, not the live version. To view the pages, open
`~/Claude/hemosim-web/index.html`.

**Edit docs.** All 13 Module Edit Docs were regenerated on 2026-07-25 from the
rebuilt pages. Neal edits wording directly in Word with track changes and writes
layout or figure requests in [brackets]. Claude then applies wording to the page
and layout notes to the CSS.

**Review pass: N1 applied, N2 to N8 awaiting review.** Neal edited
`N1 - Edit Doc.docx` on 2026-07-27. Those edits were applied to the page and
published on 2026-07-28 (`hemosim-web` commit `9a825a9`), which included two new
hand-drawn SVG figures, the B.U.S. graphic, and linked references. The N1 edit
doc was then regenerated from the updated page; Neal's annotated original is
recoverable at `hemosim-content` commit `2d107f0`.

The repeatable procedure for the remaining modules is
`04 - Module Edit Workflow.md`. Follow it rather than improvising.

**This folder is now under version control.** Set up 2026-07-28, pushed to the
private repo `hemosim-content`. Working documents are tracked, the large
reference folders are excluded. See file 03.

## Next step

Neal continues the review pass through the Module Edit Docs. As each is finished,
Claude applies the wording and layout edits to the corresponding page in
`hemosim-web`.

After the review pass, in rough order: enrich the four N7 topic subpages from
Notion and Wix, fill the remaining N2, N5, and N6 figure placeholders, then move
toward the native Wix build.

## Open items

- **File 01 is stale.** Last updated 2026-07-12, and still describes the v6
  outline as current when V8 is. Worth a rewrite when convenient.
- **Two V8 Appendix B items** ("Needs your attention") are Informed and Expert
  only: ANDROMEDA and Pinsky citations, and the level of the two new arterial
  modules. Neal is following up with Gustavo. Neither blocks the Novice build.
- **Graphics questions** are logged in `HemoSim Graphics Follow-Up.md`.
- **Notion and Wix were not re-crawled** during the N1 to N5 depth pass. If
  specific passages are still missing, point at them directly.

## Conventions worth restating

**Writing standard (locked):** connected prose, not bullet dumps. Carry the
module-to-module thread naturally in the opening and closing prose. No boxed
recap, no boxed bridge.

**Figures:** deck figures come from the .pptx, Wix and Notion figures via
browser, animations as an exported static frame. Default cap 520px wide.

**Build scripts are durable and now tracked.** Five live at the root of
`_Source Library/`: `make_edit_docs.py` (regenerates the Word edit docs from the
HTML), `assemble_rebuild.py`, `extract_all.py` (deck extraction),
`wix_capture.py`, and `banner_gen.py`. They are in git as of 2026-07-28.

The one script not preserved is `build_pilot_v8.py`, which generated the pilot
pages and was lost with an old scratchpad. If a full page rebuild is needed,
reconstruct it from the existing HTML structure in `hemosim-web`.
