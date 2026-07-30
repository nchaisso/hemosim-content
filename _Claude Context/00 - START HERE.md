# START HERE

Orientation and current status for HemoSim. Last updated: 2026-07-30.

This file holds **current state only**. Standing rules live in two files that load
automatically: `~/.claude/CLAUDE.md` for the global ones and `CLAUDE.md` at this
folder's root for the HemoSim ones. History and detail live in files 01 and 02.
Keep this one short: if it stops being scannable in a minute, move the detail out.

## Read order

1. This file, for where things stand
2. `01 - Project State and Content.md`, people, sources, Notion hierarchy
3. `02 - Build Strategy and Decisions.md`, build plan and locked decisions
4. `03 - Git and GitHub Setup.md`, how version control works here
5. `04 - Module Edit Workflow.md`, the procedure for applying a reviewed edit doc
   (read when a module comes back, not every session)

Before any module build, also read `_Source Library/INDEX.md` to know which
sources feed which module, and file 02 under "Content standards" for the rules
that govern the build itself.

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
"Build history". Since then the only content change is the N1 review pass below.

**Where the site code lives.** The pilot moved to its own private GitHub repo,
`hemosim-web`, on 2026-07-24, checked out at `~/Claude/hemosim-web`. It has its
own `CLAUDE.md`. The local `web-pilot` folder here was renamed ARCHIVED on
2026-07-25 and is a frozen copy, not the live version. To view the pages, open
`~/Claude/hemosim-web/index.html`.

**Edit docs.** There are 14 in `Module Edit Docs/`. All were regenerated on
2026-07-25 from the rebuilt pages. Neal edits wording directly in Word with track changes and writes
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

This is the single list of project-level open items. Figure-specific questions are
the one exception and live in `HemoSim Graphics Follow-Up.md`.

**Blocked on Neal or Gustavo**

- **Two V8 Appendix B items** ("Needs your attention") are Informed and Expert
  only: ANDROMEDA and Pinsky citations, and the level of the two new arterial
  modules. Neal is following up with Gustavo. Neither blocks the Novice build.
- Confirm exact citations for ANDROMEDA-PEGASUS, ANDROMEDA-SHOCK 2, and the
  Pinsky TPP figure. Do not fabricate.
- **N2 offshoot overlap.** The "At the Bedside: DO2/VO2 mismatch" detour overlaps
  N3 on recognizing shock. Keep both, or fold the detour into N3? Currently kept
  as an optional side path.
- **N8 teaching case.** The guided case (79-year-old woman, hypovolemic pattern)
  and its single test number (low RAP, flat IVC) are placeholder quality. Confirm
  or swap in a preferred case.
- **Where the PAC fingerprint content lives.** PAC Modules deck Module 8 has seven
  worked hemodynamic fingerprint cases with full number tables. Novice N7 teaches
  mechanics, so the pattern-reading layer probably belongs one tier up, in
  Informed or Expert, and also seeds the sim-day ACT scenarios. Not needed for the
  Novice build.

**Ours to do**

- **Six pages are still at 2026-07-13 depth**, predating the rebuild: both Novice
  offshoots (`bedside-do2-vo2.html`, `rap-volume.html`) and the four N7 topic
  pages. Bring them to the N1 to N8 standard when the review pass allows.
- **Cross-check each N7 topic page against its question bank** once content is
  final, so no tested item is missing from the teaching text (V7 C36).
- **Notion and Wix were not re-crawled** during the N1 to N5 depth pass. If
  specific passages are still missing, point at them directly.
- **Level selector behavior** for the Wix build: once a learner picks Novice, how
  locked in is that path versus free browsing? Decide during the build.
- **`index.html` oversells the placeholders.** It still says figures appear as
  labeled placeholders to import at build, which was true before 2026-07-23. Most
  figures are now embedded. Fix the landing copy.

## Conventions

The content and writing standards that govern module work (connected prose, the
depth standard, source precedence, figure rules) live in
`02 - Build Strategy and Decisions.md` under "Content standards". Do not keep a
second copy here.

**Build scripts are durable and now tracked.** Six live at the root of
`_Source Library/`: `make_edit_docs.py` (regenerates the Word edit docs from the
HTML), `read_edit_doc.py` (reads tracked changes out of a returned doc),
`assemble_rebuild.py`, `extract_all.py` (deck extraction), `wix_capture.py`, and
`banner_gen.py`. They are in git as of 2026-07-28.

The one script not preserved is `build_pilot_v8.py`, which generated the pilot
pages and was lost with an old scratchpad. If a full page rebuild is needed,
reconstruct it from the existing HTML structure in `hemosim-web`.
