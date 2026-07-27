# HemoSim Graphics Follow-Up

A running tracker of the figures used in the build, their source, their status, and any attribution or copyright question to resolve together while building each page. Per Neal: prioritize getting figures in; where a source is questionable, log it here rather than block the build. Last updated: 2026-07-12.

Status key: EMBEDDED = pulled into the demo/build; NEEDS EXPORT = exists as a video/animation and needs a static image; NEEDS SOURCING = right figure not yet located; OK = free to use (AI-generated or author-generated); CHECK = attribution/copyright to confirm.

## Novice demo slice (N1-N3)

| Page | Figure | Source | Status | Note / question to resolve |
|---|---|---|---|---|
| N1 | (none needed) | - | - | Conceptual page; no figure planned. Could add the DO2 equation as styled text (done) rather than an image. |
| N2 | DO2 / VO2 relationship curve (supply-independent -> supply-dependent, with lactate) | Assessing Shock deck (animated build/video) | NEEDS EXPORT | The curve is animated in the deck (Neal noted it was uploaded to Notion as a video). Export a clean static frame, or rebuild as a simple chart, during the N2 build. Currently a labeled placeholder. |
| N3 | ICU monitor photo (HR 122, art 76/61 / MAP 69, SpO2 94) | Assessing Shock deck, image on the "how ICU caretakers assess DO2" slide (extracted to web-pilot/img/AS_image18.png) | EMBEDDED | CHECK: is this a clinical photo taken by the authors (no attribution needed) or sourced elsewhere? Confirm before public launch. |
| N4 | Circulatory closed-loop / venous-reservoir schematic (stressed/unstressed volume, Pms, Rv, P_RA) | Hemodynamics v2022 deck, slide 63 (extracted to web-pilot/img/v22_circ_reservoir.png) | EMBEDDED | CHECK: author-generated diagram (likely no attribution) vs adapted from a source. Confirm origin. |
| N5 | Guyton venous-return + Frank-Starling curves intersecting at the operating point | v2022 deck, slides ~63-67 (built as shapes, not a flat image) | NEEDS EXPORT | The centerpiece figure for N5. Export a static image of the intersecting curves during the N5 build; currently a labeled placeholder. |
| N5 | Shock-type grid | Built directly as an HTML table (no image) | OK | Rendered as a styled table, so no figure import needed. |

## Novice N7 sub-topics + N8

| Page | Figure | Source | Status | Note / question to resolve |
|---|---|---|---|---|
| N7-T1 | PA catheter components + setup steps (ports, thermistor, balloon; zero/level) | PAC Modules (Patrick Lindsay) deck slides 21-28 | NEEDS EXPORT | Deck now synced. Pull the components diagram + zero/level figures from those slides at build. |
| N7-T2 | Insertion waveform sequence (RA -> RV -> PA -> wedge) + over-wedge tracing | PAC Modules deck slides 40-51, 81 | NEEDS EXPORT | Deck now synced. The classic advance-the-catheter waveform strip lives across these slides. |
| N7-T3 | RA / RV / PA / wedge tracings side by side, aligned to ECG | PAC Modules deck slides 40-66 (+ West-zone slide 63) | NEEDS EXPORT | Deck now synced. Core waveform-ID figure. Also overlaps "Right Heart Catheter Video Graphics" pptx (2.97MB). |
| N7-T4 | Thermodilution washout curves (high vs low CO) + Fick equation | "PAC-based Cardiac Output" deck + PAC Modules slides 91-101 | NEEDS EXPORT | Deck now synced. The CO-based deck has clean thermodilution curve graphics. |
| N8 | Guyton venous-return + Frank-Starling curves (with the shift per shock hypothesis) | v2022 deck (same as N5 centerpiece) | NEEDS EXPORT | Same curve graphic as N5; export once and reuse on both pages. N8 also reuses the N5 shock-type grid table (no image). |

## How figures get imported (working method)
- Deck figures: they are image files inside the .pptx (a zip); extract from ppt/media and drop into the page (as done for N3).
- Wix/Notion figures: pull the image from the live page via the browser; AI-generated ones are free to use with no attribution.
- If a figure is an animation/video (like the DO2/VO2 curve), export a static frame or rebuild it as a clean chart.
- Attribution: slide figures that came from journals or textbooks need a citation and a copyright check (Neal removed one before for this reason); AI-generated site graphics need none. Anything uncertain gets logged here.

## Open attribution/copyright checks to walk through together
- N3 monitor photo (AS_image18.png): confirm origin (author photo vs external).
- (Add rows here as we build each page and hit a questionable figure.)

---

# Non-graphics follow-up (issues and questions during the build)

Anything that comes up while building a page that is not about a figure - content questions, wording to confirm with an author, links/navigation decisions, physiology points to double-check, LMS/data-capture questions, etc. Log it here so it does not get lost, and we resolve it together.

Status key: OPEN = needs a decision/answer; ANSWERED = resolved (keep a short note); WATCH = fine for now, revisit before launch.

| Page / area | Issue or question | Status | Note |
|---|---|---|---|
| N2 | The "At the Bedside: DO2/VO2 mismatch" detour overlaps somewhat with N3 (recognizing shock). Confirm we want both, or fold the detour content into N3. | OPEN | Currently kept as an optional side path from N2; N3 is the core method. |
| N3 -> N4 | The bridge promises the Guyton/Frank-Starling curves connect to the shock-type grid in the next module. Confirm N4/N5 delivers that link cleanly (this is the "key task" from your V7 C23). | OPEN | Flagged so the payoff the demo promises actually lands. |
| Novice PAC (N7) | Confirm whether the four PA-catheter topics are four separate pages/sub-modules or one long module (your V7 C35). | ANSWERED | Built as four sub-pages (n7-t1..t4) linked in sequence from the N7 overview, mirroring the sim-day mastery flow. |
| Novice PAC (N7) | The Topic 1-4 source docs are multiple-choice QUIZ BANKS (the sim-day cognitive test), not teaching prose. The N7 submodule pages were written to teach every concept those questions test (per C36 "all cognitive/psychomotor elements must be covered in the modules"). | WATCH | Cross-check each topic page against its question bank once content is final, so no tested item is missing from the teaching text. |
| Novice (N8) | N8 guided case reuses the shock-type grid and references the Guyton/Starling curves to deliver the physiology-to-grid payoff (C37). Confirm the case (79yo woman, hypovolemic pattern) and the single "test" number (low RAP / flat IVC) read the way you want. | OPEN | Case is a placeholder-quality draft; swap in your preferred teaching case if you have one. |
| PAC interpretation (Informed/Expert + sim day) | The PAC Modules deck Module 8 has 7 worked "hemodynamic fingerprint" cases (RV failure, PAH, LV failure, hypovolemia, septic shock, tamponade, constrictive pericarditis) each with a CVP/RV/PA/PCWP/CI/SvO2 answer table. These are ideal seed material for (a) an Informed/Expert PAC-number-interpretation module and (b) the sim-day ACT scenarios. Novice N7 teaches the mechanics; the pattern-reading layer likely belongs one tier up. | OPEN | Decide where the fingerprint-interpretation content lives. Not needed for the Novice build. |
| Site-wide | Level selector behavior: once a learner picks Novice, how "locked in" is the path vs free browsing? | WATCH | Decide during the Wix build. |
| N7-T4 cognitive bank (source defect) | Topic 4 Q5: explanation math was wrong. **FIXED 2026-07-23** in the source docx + library copy: "≈ 4.8 L/min" → "≈ 6.3 L/min" and the incorrect-answers line "A, C, D" → "A, B, D" (answer key C/6.3 was already correct; option B stays 4.8 as a distractor). | RESOLVED | - |
| N7-T2 cognitive bank (two depth tables) | Topic 2 Q5 (PA 35-45) vs Q17 (PA 45-55) insertion-depth tables differ. **Neal decided to LEAVE BOTH AS-IS (2026-07-23)** - do not reconcile. | ANSWERED | Kept per Neal; no change. |
| Source Library (complete) | ALL sources now captured durably in `_Source Library/` (9 decks w/ speaker notes + 374 images, 6 docs, full 93-page Notion export + 336 images, 29 Wix pages). `INDEX.md` maps every source to its module(s) + lists 15 orphans and remaining gaps. | ANSWERED | Read `_Source Library/INDEX.md` before building any module; §5 orphan list = content with no current module home (decide where each goes). |

