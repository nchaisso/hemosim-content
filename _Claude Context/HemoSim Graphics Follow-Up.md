# HemoSim Graphics Follow-Up

A tracker for the figures in use on the live pages, their source, and any
attribution or copyright question to resolve before launch. Per Neal: prioritize
getting figures in, and where a source is questionable, log it here rather than
block the build.

The rules for sourcing and attributing figures are in
`02 - Build Strategy and Decisions.md` under "Content standards". This file holds
only the per-figure record and the open questions.

Last updated: 2026-07-30, rebuilt against the live pages in `~/Claude/hemosim-web`.
The previous version dated from 2026-07-12 and still described the pre-rebuild
pilot, including file paths under the archived `web-pilot/img/`.

Status key: EMBEDDED = on the live page; PLACEHOLDER = labeled placeholder on the
page, asset still to be produced; OK = free to use (author or AI generated);
CHECK = attribution or copyright to confirm.

## Figures in use

All filenames are relative to `~/Claude/hemosim-web/img/`. Every deck figure below
carries "Attribution to confirm" in its caption, and each page's reference block
repeats it in a footer, so the CHECK items are disclosed on the page rather than
silently assumed.

| Page | Figure | File | Source | Status |
|---|---|---|---|---|
| N1 | Oxygen dependency plot | `cain-vo2-do2-dependency.svg` | Original SVG drawn for the course, adapted from Cain 1965 (PMID 5837745) | OK |
| N1 | Circulatory loop with volume distribution | `circulatory-loop-volume.svg` | Original SVG drawn for the course | OK |
| N1, N3 | ICU monitor photo (HR 122, 76/61, mean 69, SpO2 94) | `assessing-shock-2024-version-with-voice_slide005_4b593e1a.png` | Assessing Shock deck, slide 5 | CHECK |
| N1 | B.U.S. graphic | `notion_clinical-markers_bus.png` | HemoSim Notion, Clinical Markers page | OK |
| N2 | Perfusion marker figure | `hemodynamics-module-v2022-full_slide102_3e007b70.png` | Hemodynamics v2022 deck, slide 102 | CHECK |
| N2 | De Backer marker framework | `hemodynamics-module-v2022-full_slide104_f6bee4da.jpeg` | v2022 deck, slide 104 (De Backer, Crit Care 2017) | CHECK |
| N3 | Mottling score, 0 to 5 | `hemodynamics-module-v2022-full_slide107_9837bd58.png` | v2022 deck, slide 107 (Galbois et al. J Hepatol 2015;62:549-55) | CHECK |
| N3, N8 | Venous return crossing cardiac function curves | `assessing-shock-2024-version-with-voice_slide039_1c666b0f.png` | Assessing Shock deck, slide 39 | CHECK |
| N4 | Closed loop labeled by interface | `assessing-shock-2024-version-with-voice_slide001_6c238a7c.png` | Assessing Shock deck. Caption cites slide 9, filename says slide 1: reconcile | CHECK |
| N4, N5 | Venous reservoir, stressed and unstressed volume | `hemodynamics-module-v2022-full_slide046_eb6b300b.png` | v2022 deck, slide 46 (N5 caption also cites slide 314) | CHECK |
| N5 | Second curve figure | `hemodynamics-module-v2022-full_slide052_bd9bca8f.png` | v2022 deck, slide 52 | CHECK |
| N6, N8 | ACT method figure | `assessing-shock-2024-version-with-voice_slide018_b24b9ada.png` | Assessing Shock deck, slide 18 | CHECK |
| N8 | Third case figure | `assessing-shock-2024-version-with-voice_slide040_6224cd40.png` | Assessing Shock deck, slide 40 | CHECK |
| N7 overview | PAC components | `pac-modules-patrick-lindsay-v1_slide025_25ef4d6a.png` | PAC Modules (Lindsay) deck, slide 25 | CHECK |
| N7 overview | PAC waveform | `pac-modules-patrick-lindsay-v1_slide041_c740e5c3.png` | PAC Modules deck, slide 41 | CHECK |
| N5 | Shock-type grid | none, HTML table | Built as a styled `.grid` table | OK |

## Placeholders still to produce

Each of these is a labeled placeholder on the live page whose caption points a
reader here, so leaving one unresolved is visible on the site.

| Page | Figure needed | Where it comes from |
|---|---|---|
| N2 | DO2 and VO2 relationship curve, supply-independent to supply-dependent with lactate | Wix "What is shock" graphic. Animated build in the deck, so it needs a static export. Note the N1 original SVG `cain-vo2-do2-dependency.svg` covers adjacent ground and may be adaptable instead. |
| N5 | Guyton venous return and Frank-Starling curves intersecting at the operating point | Drawn as vector shapes in the v2022 deck, slides 63 to 67 and 320 to 323. Export a static raster. |
| N6 | ACT or assessment graphic | Built as an `.emf` vector in the Assessing Shock deck, slides 17 and 26. Export a static raster. |
| N7-T1 | PA catheter components, ports, thermistor, balloon, plus zero and level | PAC Modules deck, slides 21 to 28. |
| N7-T2 | Insertion waveform sequence, RA to RV to PA to wedge, plus an over-wedge tracing | PAC Modules deck, slides 40 to 51 and 81. |
| N7-T3 | RA, RV, PA and wedge tracings side by side, aligned to ECG | PAC Modules deck, slides 40 to 66, West zones on slide 63. Overlaps the "Right Heart Catheter Video Graphics" pptx. |
| N7-T4 | Thermodilution washout curves, high versus low CO, plus the Fick equation | "PAC-based Cardiac Output" deck plus PAC Modules slides 91 to 101. |

The four N7 topic pages carry no figures at all today. They are among the six
pages still at 2026-07-13 depth, so their figures land with the depth pass rather
than separately.

## Open attribution and copyright checks

- **ICU monitor photo** (Assessing Shock slide 5, on N1 and N3). Is this a clinical
  photograph taken by the authors, needing no attribution, or sourced elsewhere?
  Confirm before public launch. This is the one Neal asked about first.
- **Venous reservoir diagram** (v2022 slide 46, on N4 and N5). Author-generated
  diagram, which likely needs no attribution, or adapted from a published source?
  Confirm origin.
- **Every other deck figure in the table above** is marked CHECK and carries the
  disclosure in its caption. The two figures with a printed citation in the source
  slide, Galbois on slide 107 and De Backer on slide 104, need that citation
  verified through PubMed and turned into a proper reference rather than a caption
  note.
- **N4 slide-number mismatch.** The interface loop figure is filed as slide 1 and
  captioned as slide 9. One of the two is wrong, and the caption is what a reader
  sees.

Resolved, kept as a record: N1's per-figure `Source:` lines were struck at Neal's
request on 2026-07-27. The page still credits the monitor photograph and the B.U.S.
graphic in its attribution footer, so nothing is uncredited. No action needed.

## Orphaned files

`img/AS_image18.png` and `img/v22_circ_reservoir.png` are pre-rebuild extracts of
the monitor photo and the reservoir diagram. No page references either one. The
2026-07-23 rebuild replaced them with the differently named extracts in the table
above. They can be deleted, but confirm with Neal first in case he wants the
cleaner filenames back.
