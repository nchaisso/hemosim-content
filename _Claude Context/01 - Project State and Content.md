# 01 - Project State and Content

## Project snapshot
- HemoSim = a free, public, tiered, case-based hemodynamics curriculum on Wix. Live site: **hemosim.org** (NOT .com). Deadline: **September 1, 2026**.
- It is Part 1 (web curriculum) of a 2-part fellowship course; Part 2 is an in-person simulation day (PA-catheter station, tools/LiDCO+PLR station, 4 ACT scenarios).
- Working deliverable: a Word "content outline by expertise level" mapping all source content into three learner levels.

## People and workflow
- **Neal Chaisson, MD** - owner; pulmonary/critical care, fellowship director, Cleveland Clinic. Style: direct, no sycophancy, no em/en dashes, ready-to-use deliverables. Rule: any change to the live Wix site must be reviewable before he makes it permanent.
- **Gustavo Garcia Chavez** - medical student writing/expanding the Notion content.
- Review loop: Neal (and Gustavo) annotate the .docx in Google Drive with tracked changes + comments, save as a NEW version. Claude reads BOTH the tracked changes AND the comments (python unzip: word/comments.xml + w:ins/w:del in document.xml), applies them, and saves the next version as a NEW file (never overwrite an annotated copy). No em/en dashes in deliverables.

## Document version history (all in the HemoSim folder)
- v1 (Jun 27): first per-level outline.
- v2 (Jun 29): + both PowerPoint decks, Proposal 2026, first Notion scrub.
- v3 (Jun 29): + fully recursive Notion crawl (~55-60 pages) + Appendix A inventory.
- v4 (Jun 30): applied Neal's v3 review (moved microcirculation + venous-return to Informed; Wix "What is shock" sourcing; 4th unifying equation; Novice PAC thermodilution/Fick how-to; built out Frontier; Appendix B).
- v5 (Jul 3): Neal + Gustavo's edited copy (their input) - added the Notion page hierarchy in Appendix A, attribution rules, sign-up link, ~33 comments.
- v6 (Jul 3): Claude built from the V5 review + a fresh Notion crawl. Reordered Novice N4-N6 (framework before ACT); added Informed "At the Bedside" module (normotensive shock, pulse pressure ~45-50 mmHg via ANDROMEDA-PEGASUS, etiology-vs-phenotype); added DSI (HR/DAP) to vasoplegia; folded in the 8 new heart-lung scenario pages; Appendix A rebuilt as Gustavo's hierarchy; Appendix B carries Neal's per-item dispositions.
- **v7 (Jul 12): EXISTS on disk, NOT reviewed in the thread that wrote these notes. Read it first on resume.** New PAC topic docs also appeared (see inventory).

## v6 outline structure (last version Claude fully built; v7 may supersede)
- **Novice N0-N9**: orientation; what shock is (oVO2/nVO2, not BP); oxygen delivery (DO2 = Hb x SaO2 x 1.34 x CO); recognize (B.U.S.); big-picture 3 principles; unifying equation + shock-type grid; ACT method; tools (AHE Tone/Filling/Flow); PA-catheter (8 modules + thermodilution/Fick how-to); put-it-together.
- **Informed I1-I15**: foundations; NEW I2 "At the Bedside" (normotensive shock / pulse pressure / phenotype); pressure measurement + damping; Interface I (+DSI, +"pressure is not perfusion" transition); Interface II; microcirculation/vascular waterfall (TPP = MAP - CrCP); Interface III; venous return depth; Interface IV (Wix-first per C169); tying the loop; tools (fluid-responsiveness intro + table); RA/CVP waveform (+ CVP page build task); PAC interpretation; CO measurement; apply.
- **Expert E1-E8**: arterial + ventricular-arterial coupling (Ea vs TAC); heart-lung (incl. 8 scenario pages); RV-PA coupling/pulmonary load; Interface IV bedside + venous congestion (VExUS, 60/60 sign); unifying/Forrester-Kenney; advanced CO + minimally invasive monitors; advanced echo; frontier (iCPET, manometry, iNO, occult PH, dysautonomia, bendopnea, liver/VExUS).
- Plus: Part 3 inventory table, Part 4 sim-day mapping, Part 5 source docs, Part 6 gaps, Part 7 sources of truth, Appendix A (Notion hierarchy), Appendix B (cleanup items + dispositions).

## Sources of truth and how they map
- **Assessing Shock - 2024 (with voice).pptx** (51 slides): primary Novice source. B.U.S., the unifying equation, the shock-type grid, ACT, RAP/volume-responsiveness. ACT storyline = slides 4-17.
- **Hemodynamics module - v2022 full.pptx** (413 slides): Informed/Expert backbone. Pressure-measurement physics + damping, tools (PLR, PPV/SPV, occlusion, fluid challenge, ScvO2, Pv-aCO2, CRT, mottling), minimally invasive CO monitors, arterial + RA/CVP waveform interpretation, IVC, thermodilution/Fick, echo (Simpson, LVOT VTI).
- **Hemodynamics Proposal 2026.docx**: goals/objectives, ABIM blueprint, sim-day design.
- **Notion workspace**: evolving conceptual source (see hierarchy below).
- **Wix (hemosim.org)**: the published, edited pages; Interface IV is fully built there (primary source for Interface IV).
- **Additional Reading** Drive folder: fact-checking source of truth.
- **NEW PAC topic docs (Jul 12, unreviewed)**: Topic 1 Indications, Topic 2 Insertion/Troubleshooting, Topic 3 Waveforms/Wedging, Topic 4 Cardiac Output, PAC Simulation Mastery Checklist - likely the PA-catheter source content; review and map to Novice N8 / Informed PAC modules.
- Attribution rule (Neal V5): reference every source with a link; attribute any graphic that has an attribution in Notion/Wix/slides; AI-generated Wix/Notion graphics need none; ALL pptx graphics need attribution if used.

## Notion structure and access
- Root: "HemoSim", id 23a0235473e8802f8281e97d0531b204. Organized by Foundations/Principles + the 4 Interfaces (each with Physiology-Correlation and At-the-Bedside children) + a Heart-Lung Interactions module. Authoritative hierarchy = Appendix A of v6 (Gustavo's map).
- **New since v4 (Jul 3 crawl): 8 heart-lung "At the Bedside" scenario pages, all with graphics** - spontaneous breathing (LV dysfunction, RV dysfunction, intra-abdominal hypertension, COPD/asthma, cardiac tamponade) and positive-pressure ventilation (ARDS, LV dysfunction, relative/absolute hypovolemia). Revised: Assessing Vasoplegia now has the Diastolic Shock Index (DSI = HR/DAP). Fluid Responsiveness page has a test-selection summary table. CVP Waveform Alterations is still empty (build task).
- ACCESS: pages are PUBLIC; read via the Claude-for-Chrome browser (navigate + javascript scrape of `.notion-page-content`; sanitize 22+char tokens to dodge the content filter). The Notion MCP connector 404s in-session (credential cached at start; only a fresh session picks up new auth). Crawl FULLY RECURSIVELY - Neal QC-checks by naming deep pages.

## Conventions and key decisions
- Three levels: Novice / Informed / Expert; onion-layer model; deeper branches tagged "Physiology Correlation" and "At the Bedside".
- Clinical method: B.U.S. -> ACT (Assess / Create hypothesis / Test) -> AHE (Tone/Filling/Flow). The Test step must name the measurable parameter that narrows the differential or proves an intervention worked.
- Unifying hydraulic model across ALL FOUR interfaces: I MAP-Pcrit=SVR*CO; II Pcrit-MSFP=arteriolar resistance*CO; III MSFP-RAP=VR*CO; IV mean PAP-LAP=PVR*CO. Introduced at Novice.
- Naming: Interface III = "Capillaries to Right Atrium"; Interface IV = "RV to LA".
- Normotensive shock / pulse pressure / etiology-vs-phenotype = Informed "At the Bedside" (kept out of the simple Novice grid).
- Website infra: capture every case-answer with timestamp + IP identifier (no name), export to a Google Drive Excel at web-build; add a user sign-up link.

## Open items to carry forward
- Read/reconcile v7 and the new PAC topic docs.
- Confirm exact citations for ANDROMEDA-PEGASUS and ANDROMEDA-SHOCK 2, and the Pinsky TPP-figure citation (do not fabricate).
- Build the CVP Waveform Alterations page; create the Clinical Markers clinical example; remaining Appendix B cleanup items.

## Access mechanics and gotchas
- PHI / Cleveland Clinic OneDrive / Desktop PHI folders are OFF-LIMITS.
- Node not installed; python-docx is (used to build the .docx). Build scripts live in the session scratchpad.
- The browser extension forces https, so it cannot open local file:// paths; preview the web-pilot by opening it locally, or via a local http server.

## Current file inventory (HemoSim folder, 2026-07-12)
- Outlines: v1 (base), v2, v3, v4, v5 (Neal/Gustavo edit), v6 (Claude), v7 (Jul 12, unreviewed).
- Decks: Assessing Shock - 2024 (with voice).pptx; Hemodynamics module- v2022 full.pptx.
- Proposal: Hemodynamics Proposal 2026.docx. Overview: HemoSim Revamp Overview Document for Claude.gdoc.
- NEW PAC docs (unreviewed): Topic 1-4 + PAC Simulation Mastery Checklist.
- Folders: Additional Reading; web-pilot (HTML design prototype); _Claude Context (this folder).
