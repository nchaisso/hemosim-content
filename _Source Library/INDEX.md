# HemoSim Source Library — Master INDEX

**Last updated:** 2026-07-23 — **ALL sources captured** (9 decks + 6 docs + full Notion export + 29 Wix pages). Notion/Wix per-module map is in **§8**.
**Companion files:** `INGESTION PLAN.md` (capture method + status), `_Claude Context/00 - START HERE.md`

---

## 0. Purpose and how to use this file

This INDEX is the mechanism that guarantees **every** captured source is drawn on when a module is
built. It is the second thing a build session reads (after `INGESTION PLAN.md`) and before writing any
module. For a module you are building:

1. Go to **§3 Per-module source manifest** and open exactly the files + slide ranges listed there.
2. Read the **speaker notes**, not just slide text — for the two lecture decks the notes carry the
   majority of the teaching (see §1).
3. Pull figures from `decks/images/<deck-slug>/` using the filenames in **§4 Figure catalogue**
   (the filename encodes deck + slide, which is your attribution).
4. Then open the module's rows in **§8** (its Notion pages and Wix page(s)) — that is where the
   Informed/Expert physiology and the published wording/citations live. Finally re-check the
   **§5 Orphan list** so nothing relevant is skipped.

**Do not** rebuild a module from the V8 outline alone. The outline is a spec; this library is the content.

### What is captured vs pending

| Source | Status | Notes |
|---|---|---|
| **9 PowerPoint decks** | ✅ CAPTURED | slide text + speaker notes + per-slide images, in `decks/` |
| **6 source .docx** | ✅ CAPTURED | full text, in `docs/` |
| **Notion workspace** | ✅ CAPTURED 2026-07-22 | 93 md pages, 2 CSV, 336 images in `notion/extracted/` — the richest Informed/Expert + deep-physiology layer. **Per-module map in §8a.** |
| **Wix (hemosim.org)** | ✅ CAPTURED 2026-07-23 | 29 published pages in `wix/` (17 with substantial prose) + `wix/_captured.md` index — the polished, referenced form of the curriculum. **Per-module map in §8b.** |

> **Scope note.** §1–§6 below were built from the 9 decks + 6 docs (the first catalogued corpus).
> **Notion (2026-07-22) and Wix (2026-07-23) were captured afterward and are folded into §8**, whose
> per-module maps close the §6 gaps: Notion fills the Informed/Expert physiology, and Wix supplies the
> published Novice/Interface wording + citations. When building any module, read its **§3 entry AND its
> §8 rows** together. Nothing is pending — all four source types are captured.

---

## 1. Source inventory

### 1a. Decks (`decks/*.md`, images in `decks/images/<slug>/`)

| File (`decks/…`) | Slides | Speaker notes? | Imgs | What it is good for (one line) |
|---|---|---|---|---|
| `assessing-shock-2024-version-with-voice.md` | 51 | **YES — 49/51, PRIMARY teaching (~70% of substance in notes)** | 25 | Flagship Novice spine: DO2 goal, MAP-is-a-poor-surrogate, unifying equation across 4 interfaces, shock-type grid, Frank-Starling/Guyton curves, A.C.T., the Magder volume-responsiveness argument, and the fully worked 79 yo guided case. Feeds N2–N8. |
| `hemodynamics-module-v2022-full.md` | 413 | **YES — 213/413** (rich in heart-lung, SPV/PPV, RA-waveform, CO sections; sparse/citation-only elsewhere) | 187 | The Informed/Expert backbone: waveform physics, Guyton/Starling derivation, PLR/PPV/EEO/fluid-challenge, ScvO2/CO2-gap/CRT/mottling, arterial-waveform interpretation, heart-lung interactions, SPV/PPV, minimally-invasive CO devices, full PA-catheter + RA/CVP-waveform + thermodilution/Fick + echo-CO. Feeds N3–N7 and nearly every I/E module. |
| `pac-modules-patrick-lindsay-v1.md` | 124 | NO (only a page-number artifact) — content is in slide text | 48 | The most complete standalone PAC course (8 modules → N7 T1–T4). Best for procedural detail, ~35 ready MCQs, and a reusable 5-column shock-type answer grid across 7 cases (RV failure, PAH, LV failure, hypovolemic, septic, tamponade, constriction) → N5/N8. |
| `pulmonary-artery-catheter-1.md` | 31 | **YES — 7 slides (10,12,14,16 PRIMARY on waveforms)** | 32 | Near-complete PAC tutorial (Arunachalam). RA/RV/PA/wedge waveforms with EKG timing, West-zone-III, Fick + thermodilution, and a derived-parameters table. Feeds N7 T1–T4. |
| `pulmonary-artery-catheter-1-1.md` | 33 | **YES — 11 slides (3,8,10,12,14 PRIMARY)** | 35 | Richest for the physical catheter (110 cm, 7-Fr, 1.5 mL balloon) and the RA→RV→PA→wedge walk-through with pressures. Feeds N7. |
| `pulmonary-artery-catheters.md` | 16 | **YES — 4 (slides 6–9 PRIMARY)** | 12 | Compact PAC insertion + waveform deck; strong indications/contraindications. **T4 (CO) is a gap** here (named only). |
| `pulmonary-artery-catheters-2.md` | 16 | **YES — 4 (slides 6–9 PRIMARY)** | 12 | Near-duplicate of the above; insertion depths by access site in the notes. |
| `pulmonary-artery-cather-based-cardiac-output.md` | 16 | NO | 12 | The single most concentrated N7-T4 source: thermodilution mechanics + Stewart-Hamilton curve intuition + Fick + derived-parameter table. |
| `right-heart-catheter-video-graphics-docx.md` | 16 | NO (all 16 "notes" are production placeholders, no narration) | 11 | Video storyboard: ordered assembly→time-out→level/zero→RA→RV→PA→wedge→CO→removal animation set; unique for the **pre-procedure time-out** and **catheter-removal** checklists → Sim Day psychomotor. |

### 1b. Docs (`docs/*.md`)

| File (`docs/…`) | Size | Speaker notes? | Media | What it is good for (one line) |
|---|---|---|---|---|
| `hemodynamics-proposal-2026.md` | ~894 para | NO (but case-debrief prose IS the facilitator narration) | none | Master curriculum design + **Sim Day (Part 2) facilitator guide**: goals/ABIM mapping, PAC + Tools hands-on stations, and **6 worked case scenarios** with debrief scripts (hypovolemic; septic + intubation; cardiogenic w/ worked Fick; severe MR; RV-failure w/ full PAC panel; cirrhotic). Feeds N5/N6/N8 + Sim Day + Informed. Names the missing-module roadmap. |
| `pac-simulation-mastery-checklist-student-handout.md` | ~314 para | NO | none | The instructor-graded **PAC psychomotor checklist** (T1–T4): exact pass/fail criteria — correct-port zeroing, phlebostatic-axis leveling, flush test, chamber depths (RA 20–25 / RV 25–35 / PA 35–45 cm), J-loop 9-o'clock, wedge-cursor at a-wave/end-expiration, thermodilution triplicate <10%. Sim Day Part 2 source of truth. |
| `topic-1-indications-for-pac-placement.md` | ~268 para / 30 Q | NO (answer explanations = teaching) | 1 video (`4-Flushing Proximal ports.mp4`); 2 referenced-but-not-extracted images (Q17 cable, Q19 GE screen) | N7-T1 cognitive bank: indications/contraindications, ports/anatomy, balloon handling, zeroing-vs-leveling physics, thermodilution setup. Sim Day cognitive items. |
| `topic-2-pa-catheter-insertion-and-troubleshooting.md` | ~253 para / 21 Q | NO | none (waveform/CXR tracings referenced inline, not extracted) | N7-T2 cognitive bank: advancement, ectopy, coiling, overwedge, damping/square-wave, CXR position, maintenance. |
| `topic-3-pa-waveforms-and-wedging.md` | ~200 para / 20 Q | NO | none (≈13/20 depend on inline tracings, not extracted) | N7-T3 cognitive bank: RA/RV/PA/wedge morphology, dicrotic notch, overwedge/whip, end-expiration ("Vent = Valley"), West zones/PEEP, a/v/c-waves, wedge-a-wave = LVEDP, cannon a-waves, TR/MR signatures. |
| `topic-4-cardiac-output-measurement.md` | ~243 para / 20 Q | NO | none | N7-T4 cognitive bank: thermodilution error/bias (shunt, TR, AF, PPV), Fick direct/indirect, method selection, high-SvO2-with-shock, validate-before-you-treat. **Contains a source defect: Q5 answer key (6.3 L/min) contradicts its own worked math (4.8 L/min) — fix before reuse.** |

**Totals (decks + docs):** 9 decks (716 slides: 51+413+124+31+33+16+16+16+16), 6 docs; **374 images**; ~123 MB. Two decks carry the teaching
narration in speaker notes (Assessing Shock, v2022) — the richest prose in the project.
**Plus (mapped in §8):** full **Notion export** = 93 markdown pages + 336 images + 2 CSV (`notion/extracted/`);
**29 Wix pages** = the published, referenced curriculum (`wix/`). **Library total ~726 MB.**

---

## 2. Module → primary-source at-a-glance

| Module | Primary captured source(s) | Coverage from decks/docs |
|---|---|---|
| N0 Orientation | Assessing Shock 1–2; v2022 1–5; Proposal logistics | thin, adequate |
| N1 What shock is | Assessing Shock 3–5; v2022 43; pac-modules M1; **Wix what-is-shock + Notion (§8)** | strong (Wix = published oVO₂/dVO₂/ERO₂ framing + refs) |
| N2 Oxygen delivery | Assessing Shock 3–4, 50; v2022 100–107; PAC Fick slides | **strong** |
| N3 Bedside / B.U.S. | Assessing Shock 4–7, 33–39; v2022 100–107, 344–354 | **strong** (Notion "Clinical Markers" adds worked example) |
| N4 Circulatory map | Assessing Shock 8–14; v2022 43–48; **Wix the-four-interface-model + Notion Principle 1/2 (§8)** | strong (4-interface graphics from Wix/Notion) |
| **N5 Curves→grid (KEY)** | **Assessing Shock 8–15, 19–23, 30–32, 36–45; v2022 45–67, 311–323** | **strong** |
| N5 offshoot RAP/volume | Assessing Shock 33–45; v2022 344–364 | **strong** |
| N6 A.C.T. | Assessing Shock 16–17, 24–27, 51; Proposal scenario framework | **strong** |
| N7 T1–T4 PA catheter | all PAC decks + Topic 1–4 docs + Mastery Checklist + Proposal Station 1 | **over-covered** |
| N8 Put it together | Assessing Shock 18–50 (full case); Proposal 6 scenarios | **strong** |
| I1–I17 Informed | v2022 (backbone) + Proposal scenarios; **Notion primary (§8a) + Wix Interface pages (§8b)** | now filled — see §8 (closes §6 gaps) |
| E1–E8 Expert | v2022 (arterial/heart-lung/CO/RA-waveform) + Proposal; **Notion primary (§8a) + Wix (§8b)** | now filled — see §8 (closes §6 gaps) |
| Sim Day (Part 4) | Proposal (stations + scenarios); Mastery Checklist; Topic 1–4 Q-banks; RHC video | **strong** |

---

## 3. PER-MODULE SOURCE MANIFEST

> Format per module: **files + slide ranges → what's there**, with 🎙️ marking where speaker notes are
> the richest content, and 🖼️ pointing at the figures (full filenames in §4).

### NOVICE

#### N0 — Orientation
- `assessing-shock-2024-version-with-voice.md` **slides 1–2, 51** — course thesis "bringing theory to the bedside"; conscious-competence framing (🎙️ slide 51 is a good capstone).
- `hemodynamics-module-v2022-full.md` **slides 1–5** — provenance, CC BY-NC-SA 4.0, original module map.
- `docs/hemodynamics-proposal-2026.md` (lines 1–207) — two-part structure, "what the sim day looks like."

#### N1 — What shock is and why hemodynamics matters
- `assessing-shock-2024-version-with-voice.md` **slides 3–5** 🎙️ — shock as an oxygen-utilization/delivery problem; DO2 = Hb × SaO2 × 1.34 × CO.
- `hemodynamics-module-v2022-full.md` **slide 43** 🎙️(placeholder) — shock = inadequate cellular O2 utilization.
- `pac-modules-patrick-lindsay-v1.md` **slides 5–8** — PAC framing of shock-as-relative (no universal CO target).
- **Deeper sources (captured — see §8):** Wix `introduction-to-hemodynamics`, `What is shock` (the crisp oVO2/nVO2<1, oDO2/nDO2, oERO2/nERO2, critical-DO2 framing) — see §6.

#### N2 — Oxygen delivery as the organizing principle
- `assessing-shock-2024-version-with-voice.md` **slides 3–4** 🎙️(PRIMARY) — DO2 equation, DO2 heterogeneous/hard to measure, lactate & MvO2 as rough surrogates, CO & Hb dominate; **slide 50** — improving Hb raises DO2.
- `hemodynamics-module-v2022-full.md` **slides 100–107** 🎙️(combined ScvO2 × CO2-gap logic in notes) — Fick/ScvO2 ~70%, Pv-aCO2 gap >6, CRT/ANDROMEDA-SHOCK, mottling. 🖼️ slide102, slide104, slide107.
- `pulmonary-artery-catheter-1.md` **slide 23**; `pulmonary-artery-cather-based-cardiac-output.md` **slides 12–14** — Fick, C(a-v)O2 = 13.4 × Hb × (SaO2–SvO2), VO2 250 mL/min.
- `pac-modules-patrick-lindsay-v1.md` **slides 99–101** — SvO2 physiology, high/low causes, high-SvO2-despite-hypoxia triad.

#### N2 offshoot — "At the Bedside: Recognizing a low DO2 / VO2 mismatch"
Optional side path off N2, opens in a new tab. Covers the bedside surrogates for DO2/VO2 mismatch, since neither can be measured directly.
- `hemodynamics-module-v2022-full.md` **slides 100–107** 🎙️(PRIMARY for the surrogates; combined ScvO2 × CO2-gap logic in notes) — Fick/ScvO2 ~70%, Pv-aCO2 gap >6, CRT/ANDROMEDA-SHOCK, mottling. 🖼️ slide102, slide104, slide107.
- `assessing-shock-2024-version-with-voice.md` **slides 4–7** 🎙️ — B.U.S. organ-perfusion signs (altered mentation, urine <30, cap-refill >3s, mottled knees) as the clinical half of the surrogate set.
- `pac-modules-patrick-lindsay-v1.md` **slides 99–101** — SvO2 physiology, high/low causes (shared with N2 proper).
- Built page cites Polanco PM, Pinsky MR. Surg Clin North Am. 2006;86(6):1431-56.
- **Build note:** `bedside-do2-vo2.html` dates from 2026-07-13 and was NOT regenerated in the 2026-07-23 fresh rebuild. Same is true of `rap-volume.html` and the four N7 topic pages. Enrich when those are brought to the N1-N8 depth standard.

#### N3 — Recognizing shock at the bedside (B.U.S. and the problem with MAP)
- `assessing-shock-2024-version-with-voice.md` **slides 4–7** 🎙️(PRIMARY) — B.U.S. (Brain/Urine<30/Skin cap-refill>3s, mottled knees; MAP<65, lactate>3, tachy); MAP = CO×SVR+Pcrit and the 3 ICU reasons the MAP-surrogate breaks. **slides 33–39** 🎙️ — RAP tools, "static CVP = PCO2 without pH," Rivers EGDT. 🖼️ slide005, slide038.
- `hemodynamics-module-v2022-full.md` **slides 100–107** (perfusion markers/mottling/CRT); **slides 344–354** 🎙️ — IVC collapse, IVC→RAP rule-of-thumb table, poor echo-vs-catheter correlation. 🖼️ slide107, slide346, slide349, slide353.
- **Deeper sources (captured — see §8):** Notion "Clinical Markers of Shock" (needs a worked clinical example — Appendix B item, Claude to draft).

#### N4 — The big-picture circulatory map (three principles, briefly)
- `assessing-shock-2024-version-with-voice.md` **slides 8–14** 🎙️(PRIMARY) — closed loop; four interfaces (MAP−Pcrit=SVR·CO; MSFP−RAP=VR·CO; mPAP−LAP=PVR·CO); venous-reservoir concept. 🖼️ slide014 loop diagram.
- `hemodynamics-module-v2022-full.md` **slides 43–48** — reservoir model, stressed/unstressed volume, Pms ~8–10, Hagen-Poiseuille. 🖼️ slide046 (reused widely).
- **Deeper sources (captured — see §8):** Wix `the-four-interface-model` + Principle 1 graphics; Notion Principle 1/2 — the four-interface **graphics** (§6).

#### N5 — Connecting the physiology to the shock-type grid (**THE KEY INTEGRATION**)
This is the module the whole V8 restructure hinges on. Source coverage is strong.
- `assessing-shock-2024-version-with-voice.md`:
  - **slides 8–15** 🎙️(PRIMARY) — unifying equation across 4 interfaces; **slide 15** = the canonical shock-type grid (MAP/CO/RAP/PAPm/LAP/SVR by type; recurs slides 22,23,29,32,47).
  - **slides 19–23** 🎙️ — sepsis walked across the curves (stressed→unstressed shift, catecholamine augmentation, Rv drop); choosing a discriminating parameter.
  - **slides 30–32** 🎙️ — cardiogenic vs hypovolemic on the curves; RAP as discriminator.
  - **slides 36–37, 39** 🎙️ — length-tension/Starling ascending limb and its limits; RAP↑ narrows MSFP−RAP gradient. 🖼️ slide036, slide039.
- `hemodynamics-module-v2022-full.md`:
  - **slides 49–62** 🎙️(slide 58 note defines Pcrit) — Guyton curve, Bayliss-Starling experiment, Pms determinants, maximal venous return / vascular waterfall. 🖼️ slide051, slide052, slide059.
  - **slides 63–67** — Frank-Starling curve, pleural-pressure shifts, **Guyton+Starling overlap = operating point** (this is the v8 "slides 45–67" flagged content).
  - **slides 311–323** — re-derivation of Pms/stressed-unstressed/Guyton/Starling and their intersection. 🖼️ slide319.
- `pac-modules-patrick-lindsay-v1.md` **slides 108–124** — the 5-column shock-type answer grid across 7 cases; **tamponade & constriction** waveforms (🖼️ slide121, slide123, slide124).
- `docs/hemodynamics-proposal-2026.md` scenarios 1–6 — the Funk 2013 curve transitions (A→B→C→D) in prose (figures must be rebuilt — §4/§6).

#### N5 offshoot — "At the Bedside: RAP and volume status"
- `assessing-shock-2024-version-with-voice.md` **slides 40–45** 🎙️(PRIMARY, the deck's single richest teaching point) — Magder J Intensive Care Med 2007;22:44-51; high CVP→non-responsive, low CVP = coin flip; **rule of thumb >10 mmHg high RAP (cardiogenic), <5 low (hypovolemic/distributive)**; confounders PEEP/obesity/PH/intra-abdominal pressure; 20 cc/kg challenge. 🖼️ slide040.
- `hemodynamics-module-v2022-full.md` **slides 324–364** — dynamic CVP across respiration; IVC collapse (spontaneous) → static RAP only; IVC distensibility (>18%) under PPV → volume responsiveness; IVC→RAP table. 🖼️ slide328, slide331, slide346, slide349, slide351, slide353, slide363.
- `docs/hemodynamics-proposal-2026.md` Scenario 6 — Magder fluid-adequacy technique (CVP rise >2 mmHg at end-expiration).

#### N6 — The A.C.T. method (AHE / Tone-Filling-Flow lives inside Test)
- `assessing-shock-2024-version-with-voice.md` **slides 16–17** (A.C.T. defined) 🎙️; **slides 24–25** 🎙️ — Advanced Hemodynamic Evaluation trigger, Tone(SVR)/Filling(RAP)/Flow(CO), trimmed 3-column grid, CO-measurement methods & Fick-vs-thermo disagreement; **slides 26–27** (iterative loop); **slide 51** (B.U.S.→AHE workflow). 🖼️ slide017, slide024, slide026.
- `hemodynamics-module-v2022-full.md` **slides 69–99** — the "Test" toolkit (PLR >10%, PPV 12.5%, EEO/EIO, fluid challenge) with thresholds. 🖼️ slide076, slide088, slide090.
- `docs/hemodynamics-proposal-2026.md` (lines 453–467) — A.C.T. framework, B.U.S. two-question gate. **Reconcile:** Proposal places Tone/Filling/Flow under **Assess**; V8 places it inside **Test** — build to V8.

#### N7 — PA catheter (four mastery topics). Web modules must cover every cognitive + psychomotor element.
Sources are abundant and overlapping; **build primarily from `pac-modules-patrick-lindsay-v1` + `hemodynamics-module-v2022-full` (246–288, 365–413) + the four Topic docs + the Mastery Checklist**, using the smaller PAC decks for figures and the RHC video for procedural sequencing.

**N7-T1 — Indications, Anatomy, Setup**
- `pac-modules-patrick-lindsay-v1.md` **slides 5–33** — indications/contraindications/complications, PA-rupture (0.2%/30%), 4-lumen anatomy (white 31 cm/blue 30 cm/thermistor 4 cm/balloon 1.5 cc), setup, zeroing vs leveling, normal-value table, Q-banks. 🖼️ slide021, slide023, slide025, slide026, slide027, slide028.
- `hemodynamics-module-v2022-full.md` **slides 19–24, 35–40, 246–253** — pressure-monitor system, zeroing/leveling to phlebostatic axis (4th ICS/mid-ax), insertion-distance guide. 🖼️ slide020, slide022, slide038, slide248, slide250, slide253.
- `docs/topic-1-indications-for-pac-placement.md` (30 Q) — indications, contraindications (absolute vs relative), ports, balloon handling, thermodilution setup, GE-monitor knobology; video `4-Flushing Proximal ports.mp4`.
- `docs/pac-simulation-mastery-checklist-student-handout.md` Topic 1 — zeroing (5-step), leveling, monitor manipulation (PA channel, 0–50 scale, sweep speed for respirophasic variation), component ID.
- `right-heart-catheter-video-graphics-docx.md` **slides 1–7** — assembly, cross-section, **pre-procedure time-out** + level/zero.
- `pulmonary-artery-catheter-1.md/-1-1` (specs 110 cm/7-Fr, 🎙️).
- `pulmonary-artery-catheters.md` **slides 3, 12** — indications (CO measurement, complex hemodynamic instability, PH-vasodilator titration, cardiogenic-vs-non-cardiogenic pulmonary edema, RH-failure cause/response) and a clean **absolute-contraindication** list (tricuspid/pulmonary valve prosthesis or vegetation, RV/RA mass, endocarditis); Swan-Ganz specs (110 cm, 7-Fr). `pulmonary-artery-catheters-2.md` is a near-duplicate — use as confirmatory only.

**N7-T2 — Insertion and Troubleshooting**
- `pac-modules-patrick-lindsay-v1.md` **slides 34–39, 77–89** — insertion sequence, distance-by-site table, **troubleshooting** (TR/Chiari network/LSVC, coronary-sinus miscannulation, coiling, overwedge, spontaneous wedge, ruptured balloon), overdamped/underdamped fixes. 🖼️ slide037, slide081, slide083, slide084, slide088.
- `hemodynamics-module-v2022-full.md` **slides 254–265, 25–34** — RA→RV→PA advancement with pressures; damping & square-wave test. 🖼️ slide026, slide029, slide031, slide032, slide033.
- `docs/topic-2-pa-catheter-insertion-and-troubleshooting.md` (21 Q, PRIMARY for T2) — ectopy (withdraw), RA coiling (clockwise rotate), depth+waveform congruency, CXR malposition, damping, J-tip 9-o'clock, inadvertent arterial cannulation, maintenance. **Reconcile the two RIJ depth tables** (Q5 vs Q17).
- `docs/pac-simulation-mastery-checklist-student-handout.md` Topic 2 — balloon at 20 cm, chamber depths, >10 cm mismatch = coiling, two-attempt→fluoroscopy escalation, over-wedge <1 cc → withdraw 1–2 cm.
- `right-heart-catheter-video-graphics-docx.md` **slides 8–12, 16** — insertion animation + **catheter-removal** checklist.
- `pulmonary-artery-catheters.md` **slides 4, 6–9** 🎙️(PRIMARY — teaching is in the notes) — distal-lumen-transduced, waveform-guided insertion; **insertion depths by access site** (subclavian 10–15 cm, jugular 15–20 cm, femoral 30–40 cm; +10 cm to RV, +10 cm to PA); AF as tip tickles atrium; RV pulsatile waveform (SBP 15–30, DBP = RAP); inflate balloon (1.5 mL) once in RV; PADP↔PAWP relationship (within ~5 mmHg, stable for hours → follow PADP, avoid repeat wedging); **"deflate passively, DO NOT keep inflated"** caution. `pulmonary-artery-catheters-2.md` **slides 4, 6–9** is a near-duplicate — confirmatory only.

**N7-T3 — Waveforms and Wedging**
- `hemodynamics-module-v2022-full.md` **slides 254–310** (PRIMARY) 🎙️ — RA a/c/v + x/y descents mapped to EKG, RV (no dicrotic notch), PA (diastolic step-up), PAOP mechanism, West zones, PAOP-vs-LVEDP (Halpern Chest 2009, Z-point), overwedging, **large v waves of MR**, and the full **abnormal-CVP case series** (prominent/cannon a, TR v-waves, prominent y, tamponade vs constriction). 🖼️ slide257, slide262, slide264, slide267, slide268, slide269, slide272, slide274, slide276, slide277, slide279, slide299, slide301, slide303, slide305, slide308.
- `pac-modules-patrick-lindsay-v1.md` **slides 40–76** — chamber waveforms with EKG-timed calculation, PADP>PAOP rule, West zones, CVP-vs-PAOP (2 vs 3 peaks), pathologic waveforms + image-based MCQs. 🖼️ slide040, slide043–050, slide062, slide063.
- `docs/topic-3-pa-waveforms-and-wedging.md` (20 Q, PRIMARY for T3) — RV-vs-PA discriminator (end-diastolic direction), "Vent = Valley," West-zone/PEEP pseudo-wedge, wedge a-wave=LVEDP, cannon a / TR / MR signatures, PADP-as-LAP-surrogate.
- `pulmonary-artery-catheter-1.md` **slides 10–22** 🎙️(PRIMARY) — a/c/v physiology, wedge Q=0 static-column, zone-3, PAOP-invalidating conditions.
- `docs/pac-simulation-mastery-checklist-student-handout.md` Topic 3 — wedge cursor at a-wave peak / end-expiration (ventilated vs spontaneous).

**N7-T4 — Cardiac Output Measurement**
- `pulmonary-artery-cather-based-cardiac-output.md` (16 slides, PRIMARY concentrated source) — thermodilution mechanics, Stewart-Hamilton AUC intuition (high CO = small tight curve), Fick, accuracy rules (expiration, mean of 3, discard >15%, 10% variability, invalid with shunt/TR). 🖼️ slide005, slide008, slide009, slide012.
- `hemodynamics-module-v2022-full.md` **slides 365–382** — thermodilution technique (10 mL D5W, computation constant, repeat 3×), Fick (CO=VO2/(CaO2−CvO2)), VO2 estimation. 🖼️ slide369, slide372, slide373, slide378.
- `docs/topic-4-cardiac-output-measurement.md` (20 Q, PRIMARY for T4) — directional bias (shunt overest., TR controversy, AF, PPV cycle), direct vs indirect Fick, method selection, CCO thermal filament, validate-before-you-treat. **Fix Q5 key defect.**
- `docs/pac-simulation-mastery-checklist-student-handout.md` Topic 4 — CO screen, injectate 10 mL, triplicate <10%, outlier rejection.
- `pac-modules-patrick-lindsay-v1.md` **slides 90–107** — thermodilution error tables (falsely high/low), worked Fick VO2 example, SvO2.

#### N8 — Put it together (guided case with A.C.T. + the curves)
- `assessing-shock-2024-version-with-voice.md` **slides 18, 28, 46–50** 🎙️(PRIMARY) — the 79 yo woman case end-to-end (Assess → distributive hypothesis → measured low CO refutes it → cardiogenic-vs-hypovolemic → RAP → hemorrhagic resolution → therapeutic A.C.T. on the curves → measure response). 🖼️ slide018.
- `docs/hemodynamics-proposal-2026.md` scenarios 1–6 (de novo starter cases spanning the grid).
- Curves must connect to the shock-type table and management (V8 C37).

### INFORMED (assumes the Novice spine)

> **Source precedence, confirmed by Neal 2026-08-05: Wix first where it has
> content, then Notion, then the v2022 deck.** Wix is stronger wherever it
> actually carries prose, because it is the published, citation-bearing form.
> Where a Wix page is thin, and several are, defer to Notion and then to the
> deck. Supplement from the named authorities (Kenny, Kattan, Magder, Pinsky)
> where extra depth genuinely helps.
>
> Earlier revisions of this file said Notion was primary for all Informed and
> Expert physiology. That was wrong and it misdirected the first three module
> agents. Corrected here.

#### I1 — Physiologic foundations (three principles in full)
- `hemodynamics-module-v2022-full.md` 43–67 (physiology backbone). **Deeper sources (captured — see §8): Wix; Notion** (primary).

#### I2 — At the Bedside: normotensive shock, pulse pressure, phenotype
- `hemodynamics-module-v2022-full.md` **slides 141–148** (pulse-pressure determinants, wide/narrow PP correlates). **Deeper sources (captured — see §8): normotensive shock, ANDROMEDA-PEGASUS/-SHOCK-2, DSI — Notion/Wix + Kattan literature** (§6).

#### I3 — Pressure measurement and waveform fundamentals
- `hemodynamics-module-v2022-full.md` **slides 8–40** (PRIMARY) — Fourier/harmonics, natural frequency/resonance (>20 Hz / ≥8×), transducer/strain-gauge/Wheatstone bridge, damping + square-wave (A1/A2 coefficient), zeroing vs leveling, end-expiration. 🖼️ slide009, slide012, slide017, slide020, slide022, slide026, slide029.
- `docs/topic-1…` block 2 (transduction physics), `docs/topic-2…` Q12 (square-wave).

#### I4 — Interface I: LV → Arterial System (Frank-Starling, VAC, Windkessel, DSI)
- `hemodynamics-module-v2022-full.md` **slides 63–67, 108–148** (arterial waveform components, Windkessel, SBP/DBP determinants, EKG-arterial delay). 🖼️ slide112, slide114, slide117, slide136, slide138, slide140. **Deeper sources (captured — see §8): VAC Ees/Ea, dicrotic-notch shift, DSI=HR/DAP — Notion/Wix.**

#### I5 — Interface II: Arterioles → Capillaries
- `hemodynamics-module-v2022-full.md` (critical closing pressure within 49–62). **Deeper sources (captured — see §8): Wix `interface-2`; Notion Interface II** (primary).

#### I6 — Microcirculation and the vascular waterfall
- `hemodynamics-module-v2022-full.md` **slides 100–107** (CRT/ANDROMEDA-SHOCK, mottling score, ScvO2/CO2-gap), **344–345** (transmural/critical closing). 🖼️ slide104, slide107. **Deeper sources (captured — see §8): Gallardo/Pinsky TPP graphic; Notion Interface II subtree** (§6).

#### I7 — Interface III: Capillaries → Right Atrium
- `hemodynamics-module-v2022-full.md` **slides 49–62, 311–323** (venous return, Guyton, stressed/unstressed, Pms, CVP as equilibrium point). **Deeper sources (captured — see §8): Wix `interface-3`; Notion.**

#### I8 — Venous return, in depth
- `hemodynamics-module-v2022-full.md` **slides 49–62** (flow limitation/max VR, Rv determinants, manipulating Pms; Bayliss-Starling). **Deeper sources (captured — see §8): Wix Interface III VR; Notion.**

#### I9 — Interface IV: RV → LA (**Wix is the primary, edited source; Notion for gaps — V8 C169**)
- `hemodynamics-module-v2022-full.md` (RA-waveform/RV context 289–310). `docs/hemodynamics-proposal-2026.md` **Scenario 5** — decompensated RV failure with the **full PAC admission panel** (DPG 17, TPG 30, PA capacitance 1.16, PVR 12.5 WU, RVSWI 11.51). **Deeper sources (captured — see §8): Wix `interface-4-rv-to-la`, general-8-10/11; Notion** (TAPSE, S′, FAC, TAPSE/PASP, VExUS).

#### I10 — Tying the loop together
- `hemodynamics-module-v2022-full.md` **slides 63–67, 323** (Guyton/Starling intersection). **Deeper sources (captured — see §8): Wix; Notion.**

#### I11 — Hemodynamic monitoring tools (preload/volume responsiveness + perfusion)
- `hemodynamics-module-v2022-full.md` **slides 69–107** (PLR, PPV, EEO/EIO, fluid challenge; ScvO2, Pv-aCO2, CRT, mottling, lactate). 🖼️ slide076, slide088, slide090, slide104, slide107.
- `docs/hemodynamics-proposal-2026.md` **Hands-On Station 2** (LiDCO/PLR/EEOT — note the sim "Tools" station was *removed* in V8, so this content now lives here in the web layer).
- **Deeper sources (captured — see §8): Notion "Fluid Responsiveness Assessment Tests" page + test-selection table** (the simple treatment I12/I13 deepen).

#### I12 — Heart-lung interactions in arterial pressure monitoring
- `hemodynamics-module-v2022-full.md` **slides 149–172** (PRIMARY — the complete Michard walk-through; 5 numbered mechanisms; 2–4 beat phase delay; transmural = true afterload). 🖼️ slide152, slide154 (reused ~8×), slide162, slide169, slide171.

#### I13 — Evaluating arterial systolic and pulse-pressure variation
- `hemodynamics-module-v2022-full.md` **slides 173–205** (PRIMARY — SPV dUp/dDown, PPV, 12.5% threshold/2009 meta-analysis, every situation that breaks the test). 🖼️ slide177, slide180.

#### I14 — Right-atrial / CVP waveform interpretation (**Notion "CVP Waveform Alterations" is EMPTY — build from v2022 RA module, C130**)
- `hemodynamics-module-v2022-full.md` **slides 289–310** (PRIMARY — normal a/c/v/x/y, z-point, and the Magder abnormal-waveform case series). 🖼️ slide257, slide299, slide301, slide303, slide305, slide308.
- `pulmonary-artery-catheter-1.md` slides 10–11 🎙️ (cannon a, TR CV fusion).

#### I15 — PA catheter interpretation beyond the Novice basics
- `hemodynamics-module-v2022-full.md` **slides 266–288** (PAOP vs LAP/LVEDP, Z-point, West zones, large v/MR, overwedging). 🖼️ slide268, slide276, slide277.
- `pac-modules-patrick-lindsay-v1.md` slides 59–71 (5-assumption chain PAOP=LAP=LVEDP…, zone conversion with management).

#### I16 — Measuring cardiac output (thermo/Fick + echo LVOT VTI)
- `hemodynamics-module-v2022-full.md` **slides 365–413** (thermodilution, Fick, Simpson biplane, LVOT VTI with worked example CO 5.96 L/min). 🖼️ slide388, slide393, slide399, slide405, slide408, slide411.

#### I17 — Apply (intermediate case library)
- `docs/hemodynamics-proposal-2026.md` scenarios (hypotension w/ high CVP; septic w/ SVV). **Deeper sources (captured — see §8): Notion.**

### EXPERT (assumes the Informed mainline; **Notion primary**)

#### E1 — Arterial system & ventricular-arterial coupling, in depth
- `hemodynamics-module-v2022-full.md` **slides 124–148** (arterial time constant, Windkessel, Ea vs TAC, PWV, wave reflection; **bizarre waveforms**: aortic stenosis, dynamic LVOT-obstruction midsystolic dip, chronic HTN/PVD; peripheral vascular decoupling in sepsis). 🖼️ slide124, slide126, slide128, slide136, slide140, slide141, slide142. **Deeper sources (captured — see §8): Wix general-8-x; Notion.**

#### E2 — Heart-lung interactions (the integrating module; **the 8 Notion "At the Bedside" scenario pages are captured — see §8a Heart-Lung subtree**)
- `hemodynamics-module-v2022-full.md` **slides 149–172, 336–343** (transmural pressure, West zones, PPV effects on VR & Starling at intubation). 🖼️ slide154, slide169. **Deeper sources (captured — see §8): Notion Heart-Lung subtree — the 8 "At the Bedside" scenario pages** (spontaneous: LV/RV dysfunction, IAH, COPD/asthma, tamponade; PPV: ARDS, LV dysfunction, hypovolemia) (§6).

#### E3 — RV-PA coupling and pulmonary load, in depth
- `docs/hemodynamics-proposal-2026.md` Scenario 5 (RV pressure-overload physiology, perfuse-before-inotrope). **Deeper sources (captured — see §8): Notion Interface IV subtree** (input impedance, why PVR misleads).

#### E4 — Interface IV at the bedside and venous congestion
- `hemodynamics-module-v2022-full.md` slides 299–310 (CVP waveform alterations). **Deeper sources (captured — see §8): Notion — TAPSE/PASP, 60/60 sign, VExUS, Castro venous waterfall.**

#### E5 — Unifying and advanced shock models
- `assessing-shock-2024-version-with-voice.md` slides 8–15 (Principle 3 full derivation). **Deeper sources (captured — see §8): Notion — Forrester-Kenney four-quadrant.**

#### E6 — Advanced cardiac-output and minimally-invasive monitoring
- `hemodynamics-module-v2022-full.md` **slides 206–245** (PRIMARY — FloTrac chi/kurtosis/skewness; LiDCO PulseCO 250 mL saturation eqn; PiCCO SV=P(t)/SVR+C(p)dP/dt; CNAP; bioreactance Starling/NICOM; indirect-Fick NICO/NM3) + **365–382** (thermodilution error, direct/indirect Fick). 🖼️ slide211, slide216, slide221, slide223, slide224, slide233, slide240. *(This is the "orphaned minimally-invasive-CO" block; its home is E6.)*

#### E7 — Advanced echo-based cardiac output
- `hemodynamics-module-v2022-full.md` **slides 383–413** (Simpson biplane, Doppler LVOT VTI, error sources). 🖼️ slide388, slide389, slide399, slide405, slide408, slide411.

#### E8 — Frontier topics (developing content)
- `docs/hemodynamics-proposal-2026.md` "Improvements for 2025" (obstructive shock, tamponade, constrictive/restrictive pericarditis; AJRCCM 2019 volume module). **Deeper sources (captured — see §8): Notion + new content + figures at web-build** (iCPET, manometry, VExUS/liver congestion, dysautonomia, bendopnea).

### SIM DAY (Part 4) — PA-catheter mastery + ACT scenarios
- `docs/hemodynamics-proposal-2026.md` — Station 1 (PAC), Station 2 (Tools — content redistributed; **station itself removed in V8**), 6 scenarios with debrief scripts, worked Fick handout, full PAC panel.
- `docs/pac-simulation-mastery-checklist-student-handout.md` — the graded psychomotor checklist (T1–T4) + mastery rubric (independent-without-prompting).
- `docs/topic-1…/2…/3…/4….md` — the 4 cognitive question banks (draw 10 of 20 per topic, pass ≥90%).
- `right-heart-catheter-video-graphics-docx.md` — time-out, level/zero, insertion animation, removal.
- Waveform/CXR tracings referenced in the Topic docs are **not extracted** — generate/source at build; use PAC-deck figures (§4) as the base.

---

## 4. FIGURE CATALOGUE (notable, by module)

Files live at `decks/images/<deck-slug>/<filename>`. Filename encodes deck + slide = attribution.
Slug key: **AS** = `assessing-shock-2024-version-with-voice`, **V22** = `hemodynamics-module-v2022-full`,
**PL** = `pac-modules-patrick-lindsay-v1`, **PAC1** = `pulmonary-artery-catheter-1`,
**PAC1-1** = `pulmonary-artery-catheter-1-1`, **PACCO** = `pulmonary-artery-cather-based-cardiac-output`.

### N2 / N3 — DO2, perfusion markers
- `V22/hemodynamics-module-v2022-full_slide102_3e007b70.png` — factors affecting ScvO2.
- `V22/hemodynamics-module-v2022-full_slide104_f6bee4da.jpeg` — combined ScvO2 × ΔCO2-gap interpretation.
- `V22/hemodynamics-module-v2022-full_slide107_9837bd58.png` — mottling score over the knee.
- `AS/assessing-shock-2024-version-with-voice_slide005_4b593e1a.png` — MAP-monitor "how ICU assesses DO2."
- `AS/…_slide038_42a78e3e.png` — Rivers/CVP-to-etiology figure.

### N4 / N5 — closed loop, curves, grid
- `V22/…_slide046_eb6b300b.png` — reservoir/Pms/VR model (reused slides 46–48, 63, 314–322).
- `V22/…_slide051_3511bae3.png` — Bayliss & Starling stopped-heart experiment.
- `V22/…_slide052_6984f62b.png` — two mechanisms that change Pms (volume vs compliance).
- `V22/…_slide059_05956dc2.emf` — vascular waterfall / Starling resistor.
- `V22/…_slide319_4dc547a8.emf` — Guyton slope = 1/venous resistance.
- `AS/…_slide036_d716b2c4.png` — Frank-Starling curve.
- `AS/…_slide039_1c666b0f.png` (+ `_a5ef3bd1.emf`) — hypovolemic vs cardiogenic curve contrast.
- `PL/pac-modules-patrick-lindsay-v1_slide121_a20d894c.png` — tamponade RA (loss of y).
- `PL/…_slide123_ad0563ae.png`, `…_slide124_03752e22.png` — constriction dip-and-plateau / brisk y.

### N5 offshoot / I11 / N6 — volume responsiveness, IVC, PLR
- `AS/…_slide040_6224cd40.png` — Magder volume-responsiveness (CVP vs response).
- `V22/…_slide328_98071a4e.png` / `…_slide331_fd330d5e.png` — CVP inspiratory drop (responsive) vs flat.
- `V22/…_slide346_d3d927d0.png` — IVC transmural-pressure abdomen/chest diagram.
- `V22/…_slide349_40342577.png` / `…_slide351_07e57f07.jpg` — M-mode IVC collapse vs no-variation.
- `V22/…_slide353_991284d6.png` — poor echo-vs-catheter RAP correlation.
- `V22/…_slide076_1ef5bc7a.png` — passive leg raise maneuver.
- `V22/…_slide088_8ebc646a.png`, `…_slide090_5c15834b.png` — EEO/EIO tracing + ≥13% calc.
- `AS/…_slide017_d211dbfe.emf`, `…_slide024_5a09f816.emf`, `…_slide026_f2789d40.emf` — A.C.T. schematic, Tone/Filling/Flow, iterative loop.

### N7 — PA catheter (T1 anatomy/setup)
- `PL/…_slide021_f1769180.png` — labeled catheter components; `…_slide023_4843d67a.jpeg` — 4 lumens.
- `PL/…_slide026_7060ce2f.png`, `…_slide027_b23b2ce4.png`, `…_slide028_faa1d6f2.jpeg` — setup, zeroing, phlebostatic-axis leveling.
- `V22/…_slide248_4843d67a.jpeg`, `…_slide250_7060ce2f.png`, `…_slide253_cd12eeeb.png` — 4-lumen, supplies, insertion distances.
- `V22/…_slide020_1c128d74.png`, `…_slide022_b2cf2d54.png` — pressure-monitor system, strain-gauge/Wheatstone bridge.

### N7 — (T2 insertion/troubleshooting; T3 waveforms/wedging)
- `V22/…_slide026_ed8c5f27.png`, `…_slide029_5708093e.png`, `…_slide031/032/033` — damping / square-wave (optimal/under/over).
- `PAC1-1/…_slide015_c71a0775.jpeg` — **best single composite RA→RV→PA→wedge sequence image.**
- `V22/…_slide257_597ff84c.png` — RA a/c/v + x/y mapped to EKG; `…_slide262_cd0dcf3e.png` — RV no dicrotic notch.
- `V22/…_slide264_4cf6b494.jpeg` — PA; `…_slide267_f35479c0.jpeg` / `…_slide268_1a2cf049.png` — wedge + static-column anatomy.
- `V22/…_slide272_d24477c4.jpg` — West zones; `…_slide274_ec1b05fc.jpeg` — wedge(2-peak) vs CVP(3-peak).
- `V22/…_slide279_86f69734.png` (= `PL/…_slide081_86f69734.png`) — overwedging tracing.
- `PL/…_slide053_*` (3 CXRs) — incorrect placements; `PL/…_slide083/084` — over/underdamped square-wave.
- Abnormal CVP series: `V22/…_slide299_53821f11.tiff` (prominent a), `…_slide301_51755b2a.tiff` (cannon a), `…_slide303_53d32d40.tiff` (TR v/CV fusion), `…_slide305_95dde5dc.tiff` (prominent y / chronic PH), `…_slide308_a7b93ee7.tiff` (tamponade).
- LVEDP/PAOP: `V22/…_slide276_926b5a2c.png` (Halpern), `…_slide277_aa9132dc.jpeg` (Z-point).

### N7 — (T4 cardiac output)
- `PACCO/…_slide009_55ded5e4.png` — thermodilution washout (high vs low CO AUC).
- `V22/…_slide372_4ab25765.jpg`, `…_slide373_55ded5e4.png` — Stewart-Hamilton curve, high vs low CO.
- `V22/…_slide378_14476654.jpg` — Fick principle + O2-content equation.

### I3 / I4 / E1 — arterial waveform & VAC
- `V22/…_slide009_dfb2627f.png` (sine), `…_slide012_1e294b15.png` (harmonic reconstruction), `…_slide017_1c1d84f2.png` (resonance).
- `V22/…_slide112_8ad4571c.jpg` (EKG-arterial 120–200 ms delay), `…_slide114_6e3fe716.png` (labeled waveform), `…_slide117_c5c89f71.tiff` (compliance morphology), `…_slide123_5980079f.png` (PP amplification).
- `V22/…_slide124_150301eb.tiff` (AS), `…_slide126_1b3c78f0.tiff` (LVOT-obstruction midsystolic dip), `…_slide128_218166d4.tiff` (HTN/PVD) — **the arterial-waveform case set / Sim cognitive.**
- `V22/…_slide136_9ada6248.png` (Windkessel), `…_slide138_221fe981.png` (time constant τ=Rp·C), `…_slide140_607cb513.png` (aging wave reflection / systolic augmentation).

### I12 / I13 — heart-lung & SPV/PPV
- `V22/…_slide154_68dd6535.png` — the workhorse Michard respirophasic figure (reused ~8×).
- `V22/…_slide162_e1063534.png`, `…_slide169_7f714482.png` — PPV RV-then-LV review; RV/LV SV phase relationship.
- `V22/…_slide177_6241b2ad.png` (SPV dUp/dDown), `…_slide180_171cfaff.png` (PPV vs SPV).

### E6 / E7 / I16 — minimally-invasive & echo CO
- `V22/…_slide211_c26d64c6.png` (FloTrac), `…_slide216_0f46a824.png` (PulseCO curves), `…_slide224_d1dad59b.png` (PiCCO), `…_slide233_9bef4457.png` (bioreactance), `…_slide240_9e1e8e9e.png` (indirect Fick).
- `V22/…_slide388_acbf988d.jpeg` (Simpson discs), `…_slide393_13e2cc07.emf` (LVOT column), `…_slide399_3cea4bd5.emf` (LVOT diameter), `…_slide408_69446017.png` (Doppler angle), `…_slide411_3ad9797f.png` (worked VTI CO).

### Figures that must be **rebuilt/sourced** (no extracted asset)
- **Funk 2013 Guyton/Starling curve transitions** (A→B→C→D) for hypovolemic, septic, cardiogenic, RV-failure, pressor, and intubation scenarios — described in prose only in `hemodynamics-proposal-2026.md`; rebuild for N5/N6/N8/I.
- Waveform/CXR tracings referenced inline in Topic-2/-3 Q-banks (RV+PVC, overwedge, square-wave, RV-coil CXR, ideal-vs-distal tip) — generate or borrow from PAC-deck figures.
- `right-heart-catheter-video-graphics` figures are **unlabeled placeholders** — pair with real RA/RV/PA/PCWP morphologies from V22/PL before use.

---

## 5. ORPHAN LIST (captured content that maps to no V8 module — the material most at risk)

> **True orphans** (no V8 node at all) are marked ⛔; **at-risk depth** items (a node exists but the
> detail is easily lost) are marked ⚠️. Each has a recommended home.

**⛔ O1 — Valvular/shunt derived parameters.** Gorlin mitral/aortic valve area, modified Hakki, LV/RV
Stroke Work Index, shunt fraction (Qp/Qs), Wood-units conversion. Source: `pulmonary-artery-catheter-1`
slide 29, `pulmonary-artery-catheter-1-1` slide 31, `pulmonary-artery-cather-based-cardiac-output` slide 15,
`topic-4` Q1/Q6. → **Drop from Novice/Informed; keep at most as an Expert "advanced PAC interpretation"
appendix under E6.** Not shock-focused.

**⛔ O2 — Obstructive shock / cardiac tamponade / constrictive & restrictive pericarditis as *teaching*.**
The authors' own "Improvements for 2025" list (`hemodynamics-proposal-2026.md` lines 1783–1793) names these
as **missing**. Rich source exists: `pac-modules-patrick-lindsay-v1` slides 108–124 (cases 6–7, transmural
physiology, square-root sign), `hemodynamics-module-v2022-full` slides 299–310 (tamponade vs constriction on
CVP), `topic-3` distractors. → **Create a dedicated Expert edge-case module (or fold into E8).** This is
simultaneously the strongest orphan and a gap.

**⛔ O3 — Minimally-invasive CO device physics at equation depth** (FloTrac chi/kurtosis/skewness; LiDCO
PulseCO 250 mL saturation eqn; PiCCO SV=P(t)/SVR+C(p)dP/dt; CNAP; bioreactance; indirect-Fick NICO) +
comparative device literature (Hadian/Pinsky Crit Care 2010). Source: `hemodynamics-module-v2022-full`
slides 206–245. → **This is the source for E6** (which V8 lists only as a one-line title). Not truly lost,
but E6 must be expanded to hold it, or it will be dropped as "no module." Recommend **→ E6**.

**⛔ O4 — Peripheral vascular decoupling in sepsis** (differential NO cycling; central > peripheral PP
inversion; degrades APCO/FloTrac). Source: `hemodynamics-module-v2022-full` slides 130–131, 231.
→ **Fold into I6 (microcirculation) or E1 (bizarre waveforms).**

**⛔ O5 — Cirrhosis-specific distributive physiology & PAH pharmacology.** Splanchnic/peripheral vasodilation
from uncleared NO → relative central hypovolemia (fluids before pressors); prostacyclin/treprostinil dosing
(14–18 ng/kg/min, t½ 4–6 h) and RV-afterload consequences; RV perfusion sequencing (norepinephrine **before**
dobutamine). Source: `hemodynamics-proposal-2026.md` Scenarios 5–6. → **Physiology → E3/E4/E8; drug dosing →
drop or a management appendix.**

**⛔ O6 — Procedural safety/complications outside the 4 mastery topics.** Pre-procedure time-out + lab screen
(plt/PTT/INR/BUN), catheter **removal** (steady pull, stop on resistance, 5–10 min pressure), PA-rupture
emergency management (rupture-side-down, double-lumen tube, PEEP tamponade), coronary-sinus miscannulation
(SvO2 ~20), Chiari network, persistent LSVC, catheter knotting, 72 h dwell, guidewire caveat, heparin-flush
not superior to saline. Sources: `right-heart-catheter-video-graphics` slides 5,16; `pac-modules-patrick-lindsay`
slides 12–14, 77–82; `topic-1`/`topic-2`. → **Sim Day psychomotor checklist + N7-T2 troubleshooting sidebars;
literature points → E-tier.**

**⛔ O7 — Sim Day "Tools" station content is now homeless.** V8 removed the LiDCO/PPV/SPV/PLR station
(Proposal Hands-On Station 2). The *concepts* survive in I11–I13, but the **hands-on station + LiDCO-Unity
knobology + finger-plethysmography demo** do not. → **Redirect the teaching to the web I11 module; drop the
device knobology or keep as an optional psychomotor elective.**

**⚠️ O8 — Pcrit / critical closing pressure as the downstream term** in `MAP = CO·SVR + Pcrit` (Magder "Highs
and Lows"). Recurs across `assessing-shock` slides 5–14 and a `v2022` slide-58 note but is treated as a given.
→ **Name it explicitly in N5 (equation) and I6 (CrCP/vascular waterfall)** or the depth is lost.

**⚠️ O9 — Waveform-generation physics depth.** Quantitative damping coefficient (A1/A2 table, worked
0.31→0.36), natural-frequency numeric rules ((180×8)/60 = 24 Hz), Wheatstone-bridge mechanics, PWV = Zc/blood
density, storage-volume-vs-stroke-volume distinction, Tacoma-Narrows/swing analogies. Source: `v2022` slides
8–40, 132–148. → **Home is I3 (+ E1); flag so the numeric method survives, not just the qualitative version.**

**⚠️ O10 — Bayliss & Starling stopped-heart experiment** (historical proof Pms independent of LV function).
`v2022` slide 51. → **Optional historical inset in I8/N5.**

**⚠️ O11 — Fick-vs-thermodilution poor-agreement literature** (Am J Respir Crit Care Med 1999;160:535) and
the electromechanical R-to-upstroke delay (120–200 ms). → **N7-T4 / E6 footnote; I4 for the delay.**

**⚠️ O12 — "Static CVP is like a PCO2 without a pH" and "clarify your goal first (measure RAP vs predict
responsiveness)"** — memorable metacognitive teaching devices from `assessing-shock` slides 33–35. → **Preserve
verbatim in the N5 offshoot / N6.**

**⚠️ O13 — Advanced arterial-waveform edge cases** (dynamic LVOT-obstruction midsystolic dip; AS; HTN/PVD).
`v2022` slides 124–129. → **E1 "bizarre/characteristic waveforms" + Sim Day cognitive.**

**⚠️ O14 — Detailed RA/CVP waveform pathology atlas** (prominent/cannon a, TR v-fusion, prominent y, TS/MS).
`v2022` 299–310; `topic-3` Q5/Q17. → **I14 (build the empty Notion "CVP Waveform Alterations" page from it) +
E4.**

**⚠️ O15 — Continuous CO (thermal filament), Qp/Qs step-up sampling, computation-constant physics, TR-vs-
thermodilution controversy.** `topic-4` Q6/Q7/Q19; `v2022`. → **E6 / N7-T4 advanced footnotes.**

**Orphan count: 15 (7 true ⛔, 8 at-risk-depth ⚠️).**

---

## 6. GAP LIST (V8 nodes thin in the decks/docs — now supplied by Notion/Wix, mapped in §8)

> "Captured coverage" = from the 9 decks + 6 docs (§1–§5). The **"Expected fill" column below is now
> captured**: Notion (`notion/extracted/`) and Wix (`wix/`) are both in hand and mapped in **§8**, so
> every gap here has a real source in the library. Nothing in this list is still uncaptured — what
> remains is drafting/figure work at build time, not missing sources.

| # | V8 node | What's missing from decks/docs | Expected fill |
|---|---|---|---|
| G1 | **N1** | The crisp "What is shock" framing (oVO2/nVO2<1, oDO2/nDO2, oERO2/nERO2, critical-DO2 threshold) | **Wix** `introduction-to-hemodynamics`, `What is shock` |
| G2 | **N3** | A worked clinical example for "Clinical Markers of Shock" (Appendix B open item) | **Notion** "Clinical Markers of Shock" (Claude to draft) |
| G3 | **N4** | The four-interface **graphics** (text is in decks; images are not) | **Wix** `the-four-interface-model` + Principle 1 graphics; **Notion** Principle 1/2 |
| G4 | **I1** | Three principles "in full" as an Informed module | **Notion**; **Wix** |
| G5 | **I2** | Normotensive shock, ANDROMEDA-PEGASUS/-SHOCK-2, etiology-vs-phenotype, DSI=HR/DAP | **Notion/Wix** + Kattan/Hernandez/Messina literature |
| G6 | **I4** | VAC (Ees/Ea), dicrotic-notch shift, DSI, "pressure is not perfusion" bedside | **Wix** `interface-1-*`, general-8-2; **Notion** |
| G7 | **I5** | Interface II proper (macro-to-micro, "not all MAPs are equal") | **Wix** `interface-2`; **Notion** Interface II |
| G8 | **I6** | Gallardo/Pinsky **TPP graphic**; CrCP/vascular-waterfall two-circuit depth; 0–5 mottling/ScvO2/PCO2-gap caveats | **Notion** Interface II subtree (cite Pinsky) |
| G9 | **I9** | Interface IV RV→LA — RV-PA coupling, TAPSE/S′/FAC/RVOT Doppler, TAPSE/PASP, VExUS (**Wix-primary, C169**) | **Wix** `interface-4-rv-to-la`, general-8-10/11; **Notion** for gaps |
| G10 | **I11** | The "Fluid Responsiveness Assessment Tests" test-selection table (the simple treatment I12/I13 deepen) | **Notion** Fluid Responsiveness page |
| G11 | **I14** | Notion "CVP Waveform Alterations" page is **empty** — must be built normal→measure→pathological (C130) | build from `v2022` RA module (deck covers it) + **Notion** |
| G12 | **E2** | The **8 heart-lung "At the Bedside" scenario pages** (spont: LV/RV dysfx, IAH, COPD/asthma, tamponade; PPV: ARDS, LV dysfx, hypovolemia), with graphics | **Notion** Heart-Lung subtree |
| G13 | **E3** | RV-specific input impedance, steady-vs-pulsatile load, "why PVR misleads" | **Notion** Interface IV subtree |
| G14 | **E4** | VExUS in depth, Castro venous vascular waterfall, 60/60 sign | **Notion** |
| G15 | **E5** | Forrester-Kenney four-quadrant model | **Notion**; Deck |
| G16 | **E8** | Frontier topics (iCPET, esophageal/pleural manometry, inhaled NO, occult PH, dysautonomia, bendopnea, liver/VExUS) + **obstructive/tamponade/pericarditis** (see O2) | **Notion** + NEW content + figures at web-build |
| G17 | **cross-cutting** | Confirm full citations for ANDROMEDA-PEGASUS, ANDROMEDA-SHOCK-2, and the Pinsky TPP-figure (do not fabricate) | literature / **Wix/Notion** references |
| G18 | **figures cross-cutting** | Funk-2013 curve figures are prose-only (rebuild); Topic-2/-3 tracings & CXRs not extracted; RHC-video figures unlabeled | rebuild/source at build |

**Gap count: 18** (11 Informed/Expert content nodes + N1/N3/N4 + 4 cross-cutting/figure gaps). All source
gaps are now filled: **Notion (captured, §8a) supplies G4–G16; Wix (captured, §8b) supplies G1, G3, G6,
G7, G9** and the Interface IV set. The only residual items are figure rebuilds (G18) and the two
"to draft / new content" notes (G2 worked example, G11/G16) — those are build-time tasks, not missing sources.

---

## 7. QC gate before the Wix build (from INGESTION PLAN)

Confirm (a) every V8 node maps to ≥1 source — **met for all Novice + most Informed/Expert from decks; the
Notion fold-in + Wix capture close G1–G18**; and (b) every Sim-Day cognitive question and psychomotor checklist
item maps to teaching content in a module (Topic 1–4 banks + Mastery Checklist → N7 T1–T4 web modules; verified
present). **Done:** Notion + Wix are captured and mapped in **§8**; read each module's §3 entry together with its §8 rows.

---

## 8. NOTION + WIX SOURCE MANIFEST (folded in 2026-07-22)

The §3 manifest above was built from the decks/docs only (Notion + Wix were captured afterward).
This section maps the now-captured **Notion tree** (`notion/extracted/`, 93 pages + 336 images) and
**Wix published pages** (`wix/`, 29 pages) to the modules. Together these **close gaps G1–G18** in
§6. **Precedence is Wix, then Notion, then the deck** (Neal, 2026-08-05). Wix is the polished,
citation-bearing form of the Novice + Interface pages.

### 8a. Notion → module map (paths under `notion/extracted/HemoSim/Hemosim Curriculum Template/`)
| Notion page (tree) | Feeds |
|---|---|
| Introduction to Hemodynamics | N1 |
| Shock Physiology and the Link with Hemodynamics | N1, N2 |
| Overview of Shock Assessment | N3, N6 |
| Clinical Markers of Shock (+ Clinical Example #1) | N3 |
| Assessing Shock (Forrester-Kenney Model) | N6, N8 |
| Hemodynamic Monitoring Tools | N6, Informed |
| Principle 1: The Four Interfaces of the Circulatory System | N4 |
| Principle 2: What goes in must come out (closed loop) | N4 |
| Principle 3: A unifying model for understanding hemodynamics | N5 |
| The Four-Interface Conceptual Model for Personalized… | N4 |
| **Interface I: Cardiac Function & Arterial Vascular** → Frank-Starling Curve; RAP – From Starling to Guyton | N4, N5 |
|  → The Arterial Windkessel; Stroke vs Storage Volume; On afterload; The Meaning of Blood Pressure | I (arterial), N5 |
|  → The Concept of Ventricular-to-Arterial Coupling; **Ea vs TAC**; Pulse Wave Propagation | I3/I4, E1 |
|  → Components of an Arterial Pressure Waveform (systolic upstroke, wave reflection, vasoplegia) | I3, I4 |
| **Interface II: Arteriolar function, CrCP & the Vascular Waterfall** | I (microcirc), N2 |
|  → Bringing Interface II to the bedside: Capillary Refill Time (+6 reasons for CRT); Mottling Score | N3 |
|  → Lactate "patho"physiology; Role of microcirc in PCO₂ gap; in ScvO₂; Other ScvO2 scenarios | N3, I |
|  → Autoregulation, Tissue Perfusion (Physiological Insight) | I (microcirc) |
| **Interface III: The Physiology of Venous Return** → Resistance to VR; Manipulating the Pmsf; PPV clinical correlation | N4, N5, I |
| **Interface IV: RV Physiology & Ventricular-arterial coupling** → Right Ventricular Function | I (RV), E |
|  → Physiologic Correlation: Pulmonary Circulation; determinants of PVR; PPV effect; **60/60 sign** | I (RV/PA), N7 |
|  → At the bedside: Clinical Tools for interface IV (TAPSE/VExUS/etc.); **CVP Waveform Alterations**; How Congestion Impairs…; venous vascular waterfall | I (RV), E |
| **Heart-Lung Interactions as an integration of the Interfaces** → Spontaneous Breathing (+ At the bedside ×5); Under Mechanical Ventilation (+ At the bedside ×3); Fluid Responsiveness Assessment | I12/I13 (heart-lung), E |
| Physiological Perspective: Flow Limitation | I, E |
| Articles (+ CSV) | reference list (citations only) |

*Onion-layer convention preserved in the export:* pages titled "Clinical Correlation…",
"Physiological Correlation…", "At the bedside…", "Physiological Insight…" are the deeper branches —
use them for the Informed/Expert layers and the "Physiology Correlation / At the Bedside" tabs.

### 8b. Wix → module map (`wix/<slug>.md`; the published, referenced version)
| Wix page(s) | Feeds |
|---|---|
| what-is-shock, copy-of-what-is-shock | N1 (published oVO₂/dVO₂/ERO₂ framing + refs) |
| introduction-to-hemodynamics | N1 (definition + 4 refs) |
| manipulating-do2 | N2 |
| practical-evaluation-of-shock | N3, N6 |
| the-four-interface-model | N4 |
| circulation-as-a-closed-loop-system *(graphic-only)* | N4 |
| a-unifying-hemodynamic-equation *(graphic-only)* | N5 |
| interface-1-cardiac-function | N5 (Frank-Starling, pleural shifts, 5 refs) |
| interface-1-arterial-vascular-function; general-8 (Windkessel); general-8-1 (waveform reflection); general-8-2 (vasoplegia); general-8-3 (bizarre waveforms); general-8-4 (systolic/diastolic BP determinants); general-8-5 (Interface 1: LV→Arterial); general-8-6 (Critical Closing Pressure); general-7 (systolic upstroke) | I3/I4 (arterial), N5 |
| interface-2-arteries-to-capillaries; autoregulation-and-tissue-perfusion; general-8-8 (Flow Limitation Primer); bringing-in (Macro→Micro Coupling) | N2, I (microcirc) |
| interface-3-capillaries-to-rv; general-8-7 (PPV effect on venous return); general-8-9 (RAP Assessment) | N4, N5, I |
| interface-4-rv-to-la; general-8-10 (RV Function); general-8-11 (Pulmonary Artery Physiology) | I (RV), N7 |
| pa-catheter-education | N7 |

### 8c. Effect on the gap list (§6)
The Informed/Expert gaps (G-series: VAC/Ea/TAC, microcirculation, venous-return depth, RV/RV-PA,
heart-lung, VExUS/congestion) are now **filled by the Notion tree**; the Novice published wording and
citations are **filled by Wix**. Remaining true gaps are only where a figure must be rebuilt (see §4
"Figures that must be rebuilt/sourced") — no remaining *content* gap across N1–N8.

### 8d. Note on redundancy / precedence
Wix is downstream of Notion, which is downstream of the decks. For any module: **decks (incl. speaker
notes) = origin of the teaching narrative; Notion = the organized deep-physiology layer; Wix = the
final published wording + citations.** When they conflict, prefer the most recent (Wix published
> Notion > deck), but mine the speaker notes and Notion "Correlation" subpages for depth the published
Wix page compresses out.
