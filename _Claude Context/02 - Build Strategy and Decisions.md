# 02 - Build Strategy and Decisions

Captures the web-build plan and the decisions locked with Neal (as of 2026-07-12).

## Locked decisions
1. **Build the real site NATIVELY in Wix** (Wix Editor pages), building on the ~36 pages already on hemosim.org. Reason: Neal must be able to edit content himself.
2. **The HTML prototype is a design blueprint only, not the content store.** It lives in the `web-pilot` subfolder. Its styling becomes a Wix theme; the actual words live in Wix.
3. **Native content = Neal edits it directly in the Wix Editor, anytime, no Claude and no rebuild.** The anti-pattern to avoid is embedding content as custom HTML, which would make Neal dependent on Claude for edits. So content is native; only interactive components are code.
4. **Interactive knowledge checks are added ON TOP later, incrementally, as reviewable drop-in components** - after the native content build, page by page. Adding a check does not disturb the native content on the page.

## N1-N8 FRESH REBUILD: DONE 2026-07-23
**STATUS: completed.** Ran as a background workflow (`hemosim-n1-n8-rebuild`, 8 agents, ~633k tokens): one agent per module read its full source set (deck slides + speaker notes, Notion, Wix) and returned a deep body + Wix references + real figure filenames; `_Source Library/assemble_rebuild.py` copied the chosen figures into `web-pilot/img/` and spliced each body + refs into the page (preserving header/stepper/pager chrome). N1-N8 rebuilt ~1200-2000 words each with real embedded figures (v2022 reservoir on N5, blood-volume on N1, ScvO2/CO2 on N2, CRT/mottling on N3, PAC anatomy on N7, 79yo case slides on N8), Wix wording/citations, same prose format. 12 Module Edit Docs regenerated. Banner Concept B (flowing ribbons) locked into the landing hero. A few `figframe` placeholders remain on N2/N5/N6 where no deck figure fit; the 4 N7 topic subpages still hold their earlier deck figures (enrich with Notion/Wix in a follow pass if wanted). **All build scripts now saved in `_Source Library/`** (extract_all, wix_capture, banner_gen, make_edit_docs, assemble_rebuild) so they survive scratchpad resets. Build method going forward: workflow generates content -> assemble_rebuild splices -> make_edit_docs regenerates the Word docs. `build_pilot_v8.py` was NOT reconstructed (not needed; pages exist and are edited by splice); the page chrome lives in the existing HTML if a from-scratch page is ever needed.

### Original locked parameters (for reference)
After the full Source Library was built (see `_Source Library/INDEX.md`), Neal directed a fresh rebuild of all 8 Novice sample modules (N1-N8, incl. N7 Topics 1-4) drawing on ALL captured sources. Locked parameters:
1. **Fresh pass from the full library.** Each module is rebuilt from its complete INDEX.md source set: deck slide text **AND speaker notes**, the Notion tree, and the Wix pages. NOTE: the earlier N1-N5 "deep rebuild" used deck *slide text only* - it did NOT use speaker notes, Notion, or Wix - so **N1-N5 must be re-enriched**, and N6-N8 brought up to the same depth. Depth standard = the N1-N5 exemplar level (connected prose, several `<h2>` sections, `.eq` equations, `.grid` tables), now deeper because of the new sources.
2. **Embed real figures.** Use the actual figures from the library (`decks/images/` = 374, `notion/extracted/` images = 336, Wix figure URLs) during this rebuild - replace the labeled placeholders wherever the library has the asset. This is no longer a "placeholder + import later" pass.
3. **Wix is the preferential resource for FINAL WORDING and REFERENCE LISTS** (the published, citation-bearing form). Precedence when sources differ: **Wix published wording/citations > Notion depth > deck narration**; but still mine the speaker notes and Notion "Clinical/Physiological Correlation" subpages for depth the published Wix page compresses out.
4. **Header/hero redesign.** Neal likes the clean look but the title is "too conservative." Make a **more active header** plus a **background graphic or accent** to complement the cleanliness. (Design direction only, not content.)
5. **Fold in Neal's edit-doc edits.** Neal put edits in the **first few Module Edit Docs** (N1-N3 range) in Google Drive - read those (tracked changes / comments / inline changes) and incorporate them into the fresh pass. (Watch for Drive-sync lag: the N0 doc showed a stale/unsynced local copy; verify each edit doc's edits are actually present before relying on them.)
6. **N0 doc: IGNORE.** Neal doesn't know what happened to its content (local copy is just an N1 duplicate); do not use it.
7. **Source cleanup:** fix Topic 4 Q5 explanation in the source docx (`PA Catheter Topics/Topic 4 - Cardiac Output Measurement.docx`): "≈ 4.8 L/min" → "≈ 6.3 L/min" and the "A, C, D" incorrect-answers line → "A, B, D" (answer key C/6.3 is already correct; only the explanation math was wrong). Re-run `extract_all.py` after. **Topic 2 Q5/Q17 insertion tables: LEAVE AS-IS** (Neal decided not to reconcile them).
8. **Tooling to reconstruct:** `build_pilot_v8.py` (page template/RAIL/CSS) and `make_edit_docs.py` (HTML→Word edit-doc converter) were WIPED when the scratchpad reset. Reconstruct them from the surviving `web-pilot/*.html`, and **save copies into `_Source Library/`** so they persist. `extract_all.py` and `wix_capture.py` are already saved there.
9. **After the HTML rebuild:** regenerate ALL Module Edit Docs in Google Drive (Neal edits wording there; layout in [brackets]).

Suggested execution shape: a workflow with one agent per module (each reads its INDEX §3 + §8 sources incl. speaker notes, drafts the deep page with embedded figures + Wix wording/citations, applies any Neal edit-doc edits), then assemble into web-pilot + regenerate edit docs. Header redesign done once, applied to all pages.

## The pilot (done)
- `web-pilot` folder: a clickable HTML prototype of the Novice spine (Modules N1-N6), content + navigation only (no quiz, per Neal). Open `index.html`.
- Demonstrates: level selector on entry, the modular "next/previous" flow with a step rail, one onion-layer detour that opens in a new tab and returns, academic styling with references + attribution note, a "PROTOTYPE" ribbon.
- Iterated per Neal's feedback: added red highlights into the navy header/hero, added original SVG figures (a DO2/VO2 curve on N2, the Guyton + Frank-Starling intersection on N4) plus a labeled "figure placeholder" frame on N5, and fixed the brand spacing.
- Purpose: lock the look and flow before the full build. Graphics were omitted in the first pass by scope choice, not a limitation; the build can carry PNG/JPG/SVG figures.

## Wix native tools vs Wix Velo (reference)
- **Native tools** (Editor/Studio, CMS, Wix Forms, app-market): no code, team-maintainable. Handles ~90% - content pages, menus, the level selector, the modular flow, images/references, and "open detour in a new tab" (a native link setting). Cannot do branching/scored quizzes, per-answer capture with IP, or writing to an external Google Sheet.
- **Velo** (Wix's JavaScript dev platform): custom front/back-end code; can read request IP, call the Google Sheets API, run scoring/branching, store to collections. Needs a developer; more Wix lock-in.
- **Lower-code middle option**: a native Wix Form + an automation (Wix Automations -> Make/Zapier -> Google Sheet). Good for simple logging; IP capture and branching still lean toward code.
- **Recommendation: hybrid, stay on Wix.** Native for everything except the interactive checks; reserve code only for the checks + answer capture + targeted feedback + the Google Sheet export, isolated to those components.

## How interactivity gets added after the native build
- Claude cannot reliably operate the live Wix Editor, and per Neal's rule any Wix change must be reviewable first. So Claude BUILDS the component and hands it over as a drop-in; Neal (or a helper) pastes it once.
- **Simplest route (no Velo): a self-contained HTML/JS quiz widget** dropped into a Wix "Embed HTML" element. For data capture, the widget POSTs each answer to a small Google Apps Script web-app endpoint that appends a row (timestamp + IP) to Neal's Google Sheet. This satisfies the section 1.9 data-capture requirement without Velo.
- **Tighter route: Velo** page/back-end code, pasted in with Dev Mode on.
- Either way it is a one-time paste per component, not a rebuild. Quiz **content** (questions + feedback) can be stored in a Wix collection so Neal edits wording himself; only the scoring/capture **logic** stays as code.

## Recommended build sequence / next steps
1. Approve the prototype look and flow (open web-pilot/index.html).
2. Claude turns the approved prototype into a Wix design template/theme + a page-by-page build spec.
3. Neal (or a Wix helper) assembles the native Wix pages on top of the existing hemosim.org pages, applying the theme.
4. Later, add interactive knowledge checks as reviewable drop-in components (Embed HTML widget + Apps Script, or Velo), one at a time.

## Tabled / deferred
- Building the interactive quiz-and-capture prototype (deferred by Neal; it also settles native-vs-Velo for the capture piece when we do it).
