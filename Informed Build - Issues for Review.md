# Informed pathway build: issues for review

**Date:** 2026-08-15
**Scope:** the fourteen Informed modules written on 2026-08-15 (I2 to I7, I9, I10,
I12 to I17), plus what building them turned up in the source material.

## What this is

Each module was built by a separate agent working from the Source Library, then
checked. Three modules (I4, I9, I15) were additionally put through a read-only
adversarial audit. Every citation on every page was verified against PubMed in a
single central pass: **300 references, three formatting problems, no wrong
citations.**

The source material did not fare as well. Most of what follows is not a problem
with the new pages. It is a problem the new pages found, in decks, in Notion, in
the Source Library index, in the proposal document, and on the live site. Several
items are wrong physiology currently being taught.

Items are marked:

- **FIX AT SOURCE.** The defect is in a deck, document, Notion page or the index,
  and correcting the module alone leaves the error in circulation.
- **REVIEW.** A judgement call on a module, for the edit phase.
- **LIVE SITE.** Currently published on hemosim.org.

---

# Part 1. Things that are wrong and are being taught

## 1.1 FIX AT SOURCE. The v2022 deck teaches cardiac tamponade incorrectly

Slide 308: "one can detect this by noting a loss of x and y descent."
Slide 309: "Tamponade causes loss of x and y descents."

In tamponade the **x descent is preserved and is usually the dominant one**,
because ejection is the only moment at which total cardiac volume can fall. It is
the **y descent that is lost**. Confirmed against Zhang, Kerins and Byrd,
*Echocardiography* 1994;11(5):507-521 (PMID 10150627), which describes tamponade
as showing "a predominant X descent with little or no Y descent", the prominent Y
belonging to constriction.

Two things make this worse than a single slide error:

1. **Slide 308 contradicts itself.** Its own question is "Why doesn't tamponade
   have a prominent y descent?", and its annotated figure marks loss of the y
   alone. Only the prose says both.
2. **The correct version is already in the library.**
   `pac-modules-patrick-lindsay-v1` slide 121 gets it right: "the x descent
   occurs during systole, therefore this is relatively preserved", and "the right
   atrial y descent is lost". So the fix is a copy, not a rewrite.

These slides feed the N7 topic 3 question bank and the sim-day cognitive items,
so the error propagates beyond the deck. **I14 teaches it correctly and says on
the page that the deck disagrees.**

## 1.2 FIX AT SOURCE. Scenario 5's PA catheter panel does not compute

**Corrected 2026-09-12** in the Word proposal and the markdown extract: derived
values recomputed from CO 3.6, HR 103 and BSA 1.70 m2, mixed venous saturation set
to 56 percent so indirect Fick agrees with thermodilution, debrief CI aligned.
The table below is the record of the defect as found.

`docs/hemodynamics-proposal-2026.md`, the decompensated RV failure case. This was
found independently by two agents that agreed on every number.

| Value | Proposal says | Recomputes to |
|---|---|---|
| Stroke volume | 39.34 mL | **35.0 mL** (CO 3.6 at HR 103) |
| PVR | 12.50 Wood units | **8.33** (TPG 30 ÷ CO 3.6) |
| RVSWI | 11.51 | **7.78** |
| PA capacitance | 1.16 | **1.03** with the corrected stroke volume |
| SVR | 1007 | **1089** |
| Indirect Fick CO 3.42 | implies VO2 ≈ 133 mL/min, about half the expected value |

TPG 30 and DPG 17 are correct. Separately, **the debrief text contradicts its own
panel**, quoting CI 1.68 and ScvO2 58 percent against the panel's 2.0 and 68
percent. SVI 22.87 implies a BSA of 1.72 while CI 2.0 implies 1.80.

The clinical shape of the case and its drug sequencing (perfuse before you
inotrope) are sound and worth keeping. The numbers need rebuilding. **I17 rebuilt
every number rather than reproducing them, and I9 recomputed PVR.** This is a
sim-day teaching case, so it should be fixed at source.

## 1.3 FIX AT SOURCE. The PAC deck's Module 8 answer grid is internally inconsistent

`pac-modules-patrick-lindsay-v1`, slides 109 to 124. The same answer options are
reused across seven cases, and option B reads:

> CVP 15 mmHg · RV 45/15 · PA 30/15 · PCWP 10 · CI 1.9 · SvO2 55 percent

**RV systolic 45 against PA systolic 30 is a 15 mmHg gradient across the pulmonic
valve.** None of these cases has pulmonic stenosis, and absent it the two systolic
pressures are the same number. The option offered for tamponade and constriction
also fails to equalise RAP and PAOP, which is the defining feature of both.

I17 did not reproduce the grid and built its cases from scratch.

## 1.4 FIX AT SOURCE. Wix general-8-10 teaches the RV descending limb wrongly

> "Once the chamber becomes excessively distended, increased pericardial
> constraint causes septal flattening and **stretches myofibrils beyond their
> optimal sarcomere length (actin-myosin overlap)**."

Sarcomeres do not overstretch in the intact heart. The descending limb is
pericardial constraint, septal shift and ventricular interdependence, all of
which the same paragraph already names. The fix is to delete the sarcomere
clause. The page also carries three typos: "ventricular ventricular", "it is
often requires", and "mulitfaceted". **This page is live.**

I9's Physiologic Insight box explicitly denies the sarcomere account.

## 1.5 FIX AT SOURCE. INDEX.md orphan O9 preserves an incorrect formula

O9 instructs that "PWV = Zc/blood density", from v2022 slide 139, be carried
forward so the numeric method is not lost. The formula is dimensionally
incoherent and causally backwards. The water-hammer relation is
Zc = ρ·PWV/A, so PWV = Zc·A/ρ, and characteristic impedance is *derived from*
wave speed rather than its cause. Wix `general-8-1` carries the correct
Moens-Korteweg form, PWV = √(Eh/2ρR), inverse **square root** of density, and Wix
outranks the deck.

I4 followed the deck and has been corrected to Moens-Korteweg.

## 1.6 FIX AT SOURCE. INDEX.md orphan O11 inverts its own paper's finding

O11 files *Am J Respir Crit Care Med* 1999;160:535 as the "Fick versus
thermodilution poor-agreement literature". That paper is Hoeper 1999
(PMID 10430725) and it found the **opposite**: mean difference between
thermodilution and Fick of +0.01 ± 1.1 L/min, explicitly **unaffected** by low
cardiac output or severe tricuspid regurgitation.

The genuine poor-agreement result is Opotowsky 2017 (PMID 28877293), and it holds
only against **estimated** Fick: in over 12,000 patients the two methods differed
by more than 20 percent in 38 percent of cases, limits of agreement -50 to +49
percent.

Anyone building from O11 would have taught the reverse of what the cited paper
says. I16 is built on the direct-versus-estimated distinction instead, which is
the more useful teaching.

---

# Part 2. Source material that is unusable or unreliable

## 2.1 FIX AT SOURCE. Notion citation strings are not trustworthy

Three wrong citations found while building three different modules:

| Notion says | Actually |
|---|---|
| Magder 2018, *Ann Transl Med* 6:272 | 6(18):**348** |
| Xu 2017, *Int J COPD* 12:**3323-3332** | 12:**3123-3131** |
| Ltaief 2021, *Crit Care* 25:318 | does not resolve |

**Consequence for the build standard:** Notion is second in source precedence, so
its prose may be followed, but its **citation strings must be re-verified against
PubMed, never copied.** This is worth stating in the build rules.

## 2.2 The Gallardo and Pinsky TPP figure cannot be sourced

INDEX.md gap G8 asks for it and G17 warns the citation is unconfirmed. A PubMed
author search for Gallardo and Pinsky together returns **zero results**. I6
dropped the figure and drew its own rather than cite something unverifiable.

## 2.3 Appendix B's citation item is now largely closed

- **ANDROMEDA-SHOCK-2 is real and published.** *JAMA* 2025;334(22):1988-1999,
  PMID 41159835, PMC12573117. I2 read the PMC full text to verify its tier-1
  algorithm directly rather than trusting the Notion summary.
- **ANDROMEDA-PEGASUS returns zero PubMed hits** under every query tried,
  including the bare name and PEGASUS with septic shock. Not a results paper, not
  a protocol, not indexed. I2 wrote the page without it.
- **The Pinsky TPP figure** cannot be sourced, as above.

That resolves all three items. Appendix B should be updated.

## 2.4 FIX AT SOURCE. INDEX.md mislabels

- Section 4 calls v2022 slide022 the strain gauge and Wheatstone bridge. The
  extracted image is the transducer assembly.
- Section 8b lists Wix `general-8-6` as "Critical Closing Pressure". The captured
  page is Starling's heart-lung preparation and carries nothing on Pcrit.
- Section 4 lists slide177 and slide180 as two figures for I13. They are the same
  image.
- Section 3 lists v2022 slides 289 to 310 as sources for I9. That range is
  entirely RA and CVP waveform material, which belongs to I14.

## 2.5 Figures catalogued but unusable

Four of the seven figures INDEX.md lists for I3: slide009 is a trivial labelled
sine, slide017's extracted PNG is a 9 KB thumbnail rather than the resonance
figure, slide020 is a text flow chart, slide026 is a static frame of an animation
with everything at rest. The genuine Wheatstone figure survives only as an EMF
that macOS cannot render.

Also unusable: slide393 and slide399 (LVOT column and diameter) are EMF;
slide319 (Guyton slope) is EMF and hung the renderer. The five abnormal CVP
tracings are TIFF, which browsers do not display, and had to be converted.

## 2.6 Two more deck defects

- **Slide 29 contradicts itself on the damping coefficient.** The text says
  A1/A2; the figure's own column header says A2/A1 and the worked example
  computes 2.5 ÷ 8 = 0.31. I3 follows the figure and the arithmetic and warns the
  reader about the inverted notation.
- **Slide 401** gives fallback LVOT diameters as "1.8 cm² for females, 2.0 cm² for
  males". Those are centimetres, not square centimetres. I16 omitted the fallback
  rather than reproduce the unit error.
- **Slide 411** gives 5.96 L/min where its own inputs give 5.97.
- **Slide 341** and Funk say positive pressure depresses the cardiac function
  curve through RV afterload. Marini 1981 found function curves plotted against
  **transmural** pressure indistinguishable on and off 15 cmH2O PEEP. I10
  follows Marini and reconciles the two explicitly.
- **Slides 32 and 33** state that mean arterial pressure is unaffected by
  damping. Romagnoli 2014 measured a 7.4 ± 11.2 mmHg mean discrepancy in resonant
  systems. I3 teaches mean as the most robust of the three, not invariant.

---

# Part 3. LIVE SITE. Five defects currently published on hemosim.org

All confirmed against the live site on 2026-08-15, not just the July capture.
These are Wix edits, so they are Neal's to make.

1. **`/general-8-9`, "RAP Assessment".** The entire "Preload Responsiveness"
   section is published as the placeholder text `asdfasdfasdf`. The rest of the
   page is finished and genuinely good.
2. **`/general-8-7`, "PPV Effect on Venous Return".** Headed literally "Page
   Title". The body is a raw `notion.so` URL and the words "Click Here", which
   exposes an internal Notion link publicly.
3. **`/general-8-11`, "Pulmonary Arterial Physiology".** Publishes the editing
   note "Add the afterload physiology section here." between a diagram and the
   PVR paragraph.
4. **`/general-8-10`, "RV Function".** The sarcomere error and three typos, in
   1.4 above.
5. **The site header tagline** reads "Bringing Hemodynamic **Phsyiology** to
   Life". The header appears on every page of the site.

Three further Wix pages are unedited templates reading "This is a Paragraph.
Click on Edit Text.": `general-8`, `general-8-2`, `general-8-4`. `bringing-in`
and `autoregulation-and-tissue-perfusion` are graphic-only stubs under 30 words.
Wix-first source precedence cannot apply where the page carries no prose, which
is worth knowing before the next build.

---

# Part 3b. Two things we need from Gustavo

## 3b.1 The two rewrites offered on 2026-08-09, still outstanding

Gustavo offered on 2026-08-09 to finish two pieces by the end of that week if
told they were needed. He has had no answer, and both are now overtaken by the
build in ways worth knowing before he starts:

1. **The transmural versus intravascular CVP/RAP passage**, which Neal flagged as
   awkwardly written. Still wanted. Note that **I3 now teaches transmural
   pressure properly as the concept the monitoring modules stand on**, and I12,
   I13, I14 and I15 all refer back to it rather than restating it. A rewrite
   should fit that structure rather than duplicate I3.
2. **The full section on CVP waveform, measurement and alterations.** **This one
   is no longer needed.** I14 is written and complete, built from the v2022 RA
   module, and it covers the normal waveform, how to measure, and the pathological
   series. The empty Notion page is not being backfilled. What would help instead
   is a review of I14 itself, which has its own issue block.

**So the answer on the two rewrites is: the transmural passage is still wanted,
the CVP waveform section is not.**

## 3b.2 The 2026-08-09 edits, not yet incorporated

Two items from the same email are still outstanding on our side, not his:

- A minor proposal for the fluid responsiveness section in the Expert pathway.
  Expert has not been built yet, so this needs holding until E-tier work starts.
- A correction to the Master Content Inventory and Level Mapping, where some
  perfusion assessment tools were not referenced to Notion.

---

# Part 3c. One question that needs a curriculum-level answer

## Where do we read a right atrial pressure?

This is the only issue in the build that cannot be fixed module by module,
because our sources give three different answers and the pages have inherited
all three. They diverge by several mmHg in exactly the patients where the reading
changes management, so this needs one answer applied everywhere.

**The three conventions in our own material:**

| Source | Says |
|---|---|
| v2022 slide 293, and Magder | The **z point**, the base of the c wave |
| v2022 slide 277 | The **peak of the a wave** |
| `pulmonary-artery-catheter-1` slide 11 | The **a wave averaged** top to bottom |

**Where each has landed on the site:**

| Page | Currently teaches |
|---|---|
| `i14.html` | The z point / base of the c wave, and argues explicitly that reading the a wave peak overstates filling pressure in a stiff ventricle |
| `i15.html` | "The peak of the a wave is what should be measured", then "read the a wave, averaging its top and its bottom", which are two different instructions |
| `i17.html` | The z point, in two worked cases |
| `n7-t3.html` | "Read the RA pressure at the a wave, averaging its top and bottom" |

**i14 and i15 directly contradict each other**, and i14 gives the argument
against what i15 instructs.

Every one of these four locations is marked in the HTML with the comment
`TODO-CVPREAD`, so they can be found with a single search once the answer is
settled, and corrected together. The same question is flagged in the edit docs
for I14, I15, I17 and N7-Topic3, so whichever module is reviewed first surfaces
it.

Nothing has been changed on any of the four pages pending that decision.

---

# Part 4. Per-module review items

## I1 (already written, not rebuilt)

**REVIEW.** i1 states: "Because cardiac output is common to all three terms, the
total systemic resistance is the sum of the three interface resistances." True as
algebra inside the model, misleading as physiology, because the Interface II
gradient is a waterfall rather than a resistive drop. Maas 2012 (PMID 22344243)
measured arterial resistance 8.27 and venous 2.75, summing to 11.01, against a
conventionally calculated total SVR of 16.56, P = 0.005. The 26.8 mmHg waterfall
gap is the difference, and conventional SVR books it silently as resistance.

**I5 carries the caveat and i1 does not.** i1.html was deliberately left
unchanged because its edit doc is out for review, and editing the page would
desync it from the copy under review.

## I2, phenotype

The DSI > 2.2 threshold appears only in Notion, as an unpublished exploratory
analysis by the investigators. The page says so explicitly and calls it a
landmark rather than a threshold. Confirm that framing. The ANDROMEDA-SHOCK-2
supplementary eTable-3 capillary refill numbers quoted in Notion were **not**
used, because the supplement could not be verified.

## I3, waveform fundamentals

Sources disagree on the acceptable oscillation count in a square wave test: deck
slide 33 says fewer than 2, topic-2 Q12 says fewer than 1.5. The page says "fewer
than one full oscillation" and resolves the wider tension through Gardner's joint
natural-frequency and damping adequacy region. Confirm.

## I4, Interface I

- Karatzas and Lee's 67 percent figure for pulsatile capillary flow traces only
  to deck slide 137, and the paper has no PubMed abstract.
- Avolio 2009 carries an erratum (*Hypertension* 2011;58(4):e30) the page does
  not note.
- Lamia 2005 and Kelly 1992 are in the reference list but never cited in the text.
- **Attribution problem.** `i4-pv-loop-ees-ea.png` and `i4-pva-stroke-work.png`
  are Notion assets renamed as though hand-drawn. The first has "Pagoulatou 2021"
  baked into the image, and that citation is absent from the reference list. The
  Ees 2 to 4 and Ea 1 to 2 mmHg/mL values in the equation legend come from that
  graphic rather than from a verified paper.
- One sentence, copied from Wix, says an elevated systolic peak is "a statement
  about arterial buffering capacity rather than about the heart", which
  contradicts the page's own three determinants, the first of which is
  contractility.
- **Corrected during the build:** the PWV formula (1.5 above) and a figure caption
  claiming blood pressure is identical between a coupled and an uncoupled
  ventricle, when only end-systolic pressure is.

## I5, Interface II

Burton 1951, Nichol 1951 and Girling 1952 have no PubMed abstracts, so they are
cited only for the origin of the concept and no claim is made about their results.

## I6, microcirculation

One unsourced textbook constant remains: CO2 is "roughly twenty times more
diffusible" than O2. No real-image sublingual videomicroscopy figure exists in
the library, so that figure gap is open.

## I7, Interface III

**REVIEW, worth a decision.** Wix-first precedence could not apply to this
module. The Wix page, the entire Notion Interface III subtree and deck slides
49-62 and 311-323 are all I8 material: the Guyton curve, Pms, resistance to
venous return. None of them covers the capillary boundary, the Starling forces,
the revised Starling principle, compliance versus capacitance, or the splanchnic
reservoir. **The module is therefore built from primary literature** (Levick and
Michel 2010, Woodcock 2012, Greenway 1974, Starling 1896). It fills a real hole,
nothing on the site previously explained where a fluid bolus goes, but confirm
the scope is what was wanted.

Gelman and Mushlin 2004 (PMID 14739821) was dropped, no PubMed abstract to verify
against.

## I9, Interface IV

- Six references are uncited in prose: Sanz, Haddad (twice), Vonk Noordegraaf,
  Rudski, Lang. Rudski and Lang underpin the threshold table.
- RV stroke work is given as roughly a sixth of the left ventricle's. Haddad
  gives a quarter to a fifth.
- RV free wall thickness given as 2 to 5 mm, usually quoted 3 to 5.
- Three figures are renamed Notion assets rather than keeping source filenames.
- **Corrected during the build:** "a sixth of the systemic resistance" was the
  pressure ratio, not the resistance ratio, which is an order of magnitude lower
  again. Left coronary flow was attributed to LV systolic pressure exceeding
  aortic pressure during ejection, when the mechanism is intramyocardial
  compression. Tello's TAPSE/PASP result was reported as an independent predictor
  without noting the multivariate odds ratio of 18.6 has a confidence interval of
  0.8 to 96.1, P = 0.08.

## I10, tying the loop together

Added beyond the brief, deliberately: Kenny's geometric model, which introduces a
pericardial-pressure term and a "cardiac resistance" term no other module uses,
and Uemura's two-atrium venous return surface as the honest limit of the one-loop
treatment. Confirm both belong at Informed rather than Expert.

The Funk intubation passage quoted in the proposal reads "VR increases (a
shallower slope of the VR curve)", which is self-contradictory. Written correctly
as a fall.

## I12, heart-lung interactions

- The deck's mechanism ordering implies venous effects dominate the loss of RV
  stroke volume. Vieillard-Baron 1999 and Jellinek 2000 show afterload and venous
  resistance dominate rather than gradient loss. The page keeps Michard's
  five-mechanism framework and adds "Which of the five actually dominates".
- The page gives the conventional > 10 mmHg definition of pulsus paradoxus. The
  brief said no numeric thresholds, but that instruction was about SPV and PPV,
  which belong to I13, and the sign cannot be taught without the number.

## I13, SPV and PPV

- The deck's summary slide 203 gives the threshold as 12.5 percent while
  ANDROMEDA-SHOCK-2 uses 13 percent. The page publishes the provenance of both
  rather than picking one. **Decide whether the curriculum should state a single
  number.**
- No human study of PPV validity in intra-abdominal hypertension exists, so only
  porcine data is given (Renner, Jacques), and the page says the human thresholds
  are unestablished.

## I14, CVP waveform

- **Three reading conventions disagree across our own sources**: v2022 slide 293
  says the z point, `pulmonary-artery-catheter-1` slide 11 says average the top
  and bottom of the a wave, Magder 2015 says the base of the c wave. The page
  follows the z point and puts the disagreement in a Physiologic Insight box,
  because the answers diverge exactly in the patients where the reading changes
  management. **This needs a curriculum-level decision.**
- Two claims dropped for want of support: the deck's claim that a femoral CVP
  tracks RA pressure within about 1 mmHg (no PubMed source found, retained as the
  curriculum's own practical guidance rather than attributed to literature), and
  any percentage for the atrial contribution to RV filling, where only LV data
  exists.
- The Notion "CVP Waveform Alterations" page is empty, title line only, so the
  module was built from the v2022 RA module instead and is complete without it.
  **Decided 2026-08-17: the Notion page is not being backfilled.** I14 is the
  curriculum's treatment of this material.

## I15, PA catheter interpretation

- The Halpern insight callout draws an inference the abstract does not state.
- Al-Kharrat's "twice the disagreement" belongs to a substudy, not the 147
  tracings.
- Komadina's agreement figure drops its "within 4 mmHg" qualifier.
- The Z-point section says "the peak of the a wave is what should be measured"
  and then "averaging its top and its bottom". Pick one.
- Swan and Nadeau are in the reference list but uncited.
- Topic-3 Q12, the catheter whip artifact, is covered only in I3. Q13's normal
  ranges (mPAP < 20, PAWP 6 to 12) appear nowhere in I15.
- **Corrected during the build:** the page asserted that a wedge above the
  pulmonary artery diastolic pressure "is not a physiological finding" and could
  only mean overwedging or a tip outside zone 3. A giant v wave in acute mitral
  regurgitation routinely lifts the mean wedge above PADP with the measurement
  working correctly, and our own topic-3 Q4 says the relation holds only "without
  tall v-waves". Also corrected: a claim that the overwedging mechanism is the
  rupture mechanism, and Cope 1986's postcapillary result, which is dog data.

## I16, cardiac output

The Q5 defect in `topic-4` that the brief warned about **was already fixed** on
2026-07-30; the brief was out of date. The correct answer is 6.2 L/min and the
page states it.

## I17, apply

Two claims softened to match their abstracts: Fincke is now the strongest
independent correlate on multivariable analysis only, and the Kattan post hoc is
normal capillary refill **at two hours**, not at baseline. Every case's arithmetic
was verified by script: twelve SVR values, five PVR values, six mean PA pressures,
both LVOT stroke volume calculations and the full Fick set all compute from the
stated inputs.

---

# Part 5. The length question

Every new module is longer than the three that set the contract. This is
systematic rather than three agents overrunning, and every agent that flagged it
gave the same reason: the briefs mandated more distinct topics than i1, i8 and
i11 carried, and further cuts would have removed verified content.

Word counts below include figure captions and alt text, so the prose figure is
roughly 10 to 20 percent lower. I9's audit measured its actual prose at 6,626
against the 8,397 shown here.

| Contract pages | | New modules | |
|---|---|---|---|
| I1 | 4,981 | I2 | 6,682 |
| I8 | 5,429 | I3 | 6,413 |
| I11 | 6,047 | I4 | 7,026 |
| | | I5 | 7,472 |
| | | I6 | 6,733 |
| | | I7 | 6,359 |
| | | I9 | 8,397 |
| | | I10 | 7,844 |
| | | I12 | 6,539 |
| | | I13 | 7,751 |
| | | I14 | 7,463 |
| | | I15 | 7,662 |
| | | I16 | 7,045 |
| | | I17 | 7,702 |

**The decision is whether the contract ceiling moves or the modules get trimmed
in review.** For I9 specifically, the audit identified about 480 words of genuine
redundancy and named each passage, which would land it near 6,150 prose words
without losing required teaching.
