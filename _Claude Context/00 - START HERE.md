# START HERE

Orientation and current status for HemoSim. Last updated: 2026-08-04.

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

**Edit docs.** Twelve are script-managed and were regenerated from the current
pages on 2026-08-04. Neal edits wording directly in Word with track changes and
writes layout or figure requests in [brackets]. Claude then applies wording to the
page and layout notes to the CSS.

As of 2026-08-04 the generated doc also carries the page's **reference list**, so
it can be pruned during review. The split matters: the document decides *which*
references appear, and PubMed decides *how* they read. See file 04, step 5.

Two further docs, `N2-Offshoot-BedsideDO2VO2` and `N5-Offshoot-RAPVolume`, are not
script-managed and are now **orphaned**: both offshoot pages were deleted on
Neal's instruction during the review pass. They are kept only as the record of
that instruction.

**Review pass: complete for the Novice spine.** N1 through N8 plus N7 topics 1
and 2 were all applied on 2026-08-03 and 2026-08-04, run as one module per agent
with a shared contract, then a references pass and a read-only verification pass.
Neal's annotated originals are recoverable at `hemosim-content` commits `c6f1bf1`
and `2a4192b`.

What changed beyond wording: the N2 and N5 offshoot pages were deleted, N4 gained
five new sections, N7 gained the first Physiologic Insights box, and four figures
were drawn from scratch as SVG (the insights icon, the West lung zones, an RV
pressure waveform, and a redrawn right atrial tracing). Every citation on the site
now resolves in PubMed.

`N7-T3` and `N7-T4` have not been reviewed. They still sit at 2026-07-13 depth.

The repeatable procedure is `04 - Module Edit Workflow.md`. Follow it rather than
improvising.

**This folder is now under version control.** Set up 2026-07-28, pushed to the
private repo `hemosim-content`. Working documents are tracked, the large
reference folders are excluded. See file 03.

## Next step

The Novice review pass is done. Next is Neal's read-through of the regenerated
edit docs, which now include reference lists for the first time, followed by the
two unreviewed topic pages (N7-T3, N7-T4).

After the review pass, in rough order: enrich the four N7 topic subpages from
Notion and Wix, fill the remaining N2, N5, and N6 figure placeholders, then move
toward the native Wix build.

## Open items

This is the single list of project-level open items. Figure-specific questions are
the one exception and live in `HemoSim Graphics Follow-Up.md`.

**Blocked on Neal or Gustavo**

- **V8 Appendix B, remaining items.** The ANDROMEDA and Pinsky citations still
  need confirming with Gustavo. The arterial-module question is **resolved**: I12
  and I13 sit at Informed and E2 becomes the integrating module, decided
  2026-08-04. See file 02, locked decision 5. The outline itself still lists it
  as open and should be updated at the next revision.
- Confirm exact citations for ANDROMEDA-PEGASUS, ANDROMEDA-SHOCK 2, and the
  Pinsky TPP figure. Do not fabricate.
- **N8 teaching case.** The guided case (79-year-old woman, hypovolemic pattern)
  and its single test number (low RAP, flat IVC) are placeholder quality. Confirm
  or swap in a preferred case.
- **Where the PAC fingerprint content lives.** PAC Modules deck Module 8 has seven
  worked hemodynamic fingerprint cases with full number tables. Novice N7 teaches
  mechanics, so the pattern-reading layer probably belongs one tier up, in
  Informed or Expert, and also seeds the sim-day ACT scenarios. Not needed for the
  Novice build.

**Ours to do**

- **The Wix build has to reproduce four hand-drawn SVGs**: the Physiologic
  Insights icon, the West lung zones diagram, an RV pressure waveform and a
  redrawn right atrial tracing. They exist only as vector files in `hemosim-web`,
  Neal approved the RV pressure waveform to ship on 2026-08-04; the other three
  have not been formally signed off.
- **Five figures carry stale text baked into the pixels** and cannot be fixed in
  HTML: MSFP on the N4 interface diagrams, "Starling curve" on the pleural
  pressure figure, and P_RA on the venous return series. Neal has said to ignore
  these for now. They need redrawing before launch.
- **Unanswered bracketed requests: none left.** The last one, a capillary refill
  demonstration for N3, turned out to be a YouTube link rather than a Dropbox
  file and is now live on the page (`youtu.be/aO3mqie46hQ`). The Wix build can
  embed it natively rather than linking out, if Neal prefers that there.
- **Links to intermediate modules** are marked in the HTML as
  `<!-- TODO-LINK: ... -->` on N4 and N8. They become real hrefs when those
  modules exist.

- **Two pages are still at 2026-07-13 depth**: `n7-t3.html` and `n7-t4.html`. The
  two Novice offshoots that shared this problem were deleted rather than
  deepened, and N7 topics 1 and 2 were brought up to standard in the review pass.
- **Cross-check each N7 topic page against its question bank** once content is
  final, so no tested item is missing from the teaching text (V7 C36).
- **Notion and Wix were not re-crawled** during the N1 to N5 depth pass. If
  specific passages are still missing, point at them directly.
- **Level selector behavior** for the Wix build: once a learner picks Novice, how
  locked in is that path versus free browsing? Decide during the build.

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
