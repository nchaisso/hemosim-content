Subject: HemoSim Core modules: what is applied, and the items to settle before the Wix build

Gustavo,

All of your reviewed edits on I1 through I17 are now applied to the pages, and the tier is called "Core" everywhere on the site (Novice, Core, Expert). Your full rewrite of I13 became the new page, with the SVV section and the four-part dynamic arterial elastance treatment. Your four I12 infographics are on the page with credit to you. Every page passes our style check and every reference resolves in PubMed. Before we start writing the code that moves this onto Wix, a few things need your input. Most are places where a number you typed could not be matched to the paper's abstract, so it was left out rather than published unverified. If you have the source, send the PMID or the page and I will put the number back.

Numbers left out pending a source

1. I9, coronary flow. The sentence giving the systolic-to-diastolic right coronary flow ratio "R = -0.83, P < 0.001" against RV systolic pressure, with the scatter plot you pasted, is not in the abstracts of Vlahakes 1981 or Lowensohn 1976. Which paper is it from?
2. I10, Guarracino, Bertini and Pinsky 2019. "49 of the 55 patients increased cardiac index by more than 15 percent" and the dynamic arterial elastance values 1.00 (S.D. +/- 0.13) versus 0.67 (S.D. +/- 0.14) are not in the abstract. The 35 of 55 reaching a MAP above 65 mmHg is, and is on the page. Are the other figures from the full text?
3. I2, Convertino 2006. The abstract supports pulse pressure tracking stroke volume (r squared 0.91) but not that this paper was a basis for the pulse pressure below 40 mmHg criterion in ANDROMEDA-SHOCK-2. The correlation is cited, the trial link is not.
4. I15, Magder 2018 (PMID 27872408). The recommendation to measure "before that expiratory pressure develops, generally near the beginning of expiration" and the phrase "including pulmonary artery occlusion pressure" are not in the abstract. The page keeps what the abstract supports.
5. I6, your comment C25 that Pinsky attributes central arterial stiffening in sepsis to vasa vasorum microangiopathy. No PubMed record supports this. Is it published, or a personal communication? If the latter, it stays off the page.
6. I12, Vieillard-Baron 2001. Your "26 (S.D. +/- 17) percent" was corrected to 25 per the abstract, and the patient descriptor was changed to what the abstract states.
7. I13, Zhou 2024. The Eadyn cutoff was written as "0.80 to 0.97"; the abstract gives a mean cutoff of 0.89 with a 95 percent confidence interval of 0.80 to 0.98, which is what the page now says.

Edits held because they conflict with something

8. I10, worked-example table, "Pump depressed alone" row. Your change of Pms from 8 to 16 and RAP from 3.2 to 8.0, with the resistances and flow unchanged, breaks the module's own equation: with those inputs Q would be 5.9 rather than 3.4. What inputs did you intend?
9. I6, table row 2. The insertion of "functionally" before "capillary density" conflicts with the page's distinction between anatomical and functional density, because that row's mechanism (haemodilution, anaemia) is anatomical and functional loss is row 1. Did you mean to move the row?
10. I15, wedge reading. Neal has fixed the site-wide convention: RAP at the z point (a-wave peak at end-expiration acceptable), the wedge at the a-wave peak, wedge normal 6 to 12 mmHg. Your "average the peak and trough of the a wave" was rendered as the a-wave peak for that reason. Your distinction between end-diastolic PAWP and mean PAWP is kept in full.
11. I14 and I16. Where your edit struck verified data (the Magder 119-patient active-expiration cohort, the cosine values for Doppler misalignment), the data were kept and folded into your new wording. Say if you want them out.
12. I17, Case 4. Your rewrite no longer uses Hayes 1994, ANDROMEDA-SHOCK or the Kattan post hoc. They are still in the reference list. Drop them, or keep for a future case?

Figures

13. I4. You asked for the Notion and Wix videos on time-varying elastance and for the Notion PVA versus MVO2 image. Videos are planned for the Wix build (see below), so tell me which files you mean. The PVA image has the same provenance problem as the two existing I4 figures that carry "Pagoulatou 2021" baked in: we need a citable source or a redraw.
14. I5, I6, I9, I12, I13, I16, I17. Several images you pasted were not used: some duplicate figures already on the page, some carry "Pra" or "Pmsf" in the pixels (the site uses RAP and Pms), and the I6 lactate and CO2-gap diagrams have no verifiable source. The I17 Case 3 abdominal pressure figure was redrawn as an SVG with site notation. If any of the unused ones is your own drawing, say so and I will credit and place it.

Open questions Neal is deciding, where your view helps

15. I13: one PPV threshold for the curriculum, 12.5 or 13 percent. Your text keeps both.
16. I3: your comment C8 asks which damping-coefficient cutoff to teach. Propose one.
17. I11: you said the PPV blunting in vasodilatory states and dynamic arterial elastance would wait for the Expert pathway, but Eadyn is now on I13 through your rewrite. Is I13 the right home, or should I13 carry the short version and Expert the full one?
18. I2: your C288 (perfusion pressure versus upstream pressure for patient 1) and C289 (patient 1 does not meet the ANDROMEDA-SHOCK-2 enrolment criteria). Both are with Neal.
19. I5: your C109 on the "Not all MAPs are equal" table. A hedging sentence, or leave it?

Source defects you may want to know about before anything is reused

20. The v2022 deck teaches tamponade as loss of the x and y descents (slides 308, 309); only the y is lost. The PAC deck's Module 8 answer grid pairs RV 45 with PA 30 without pulmonic stenosis and fails to equalise RAP and wedge in tamponade. Scenario 5 in the sim-day proposal has been recomputed (SV 35, CI 2.1, PVR 8.33, SVR 1089, SvO2 56 percent).

What happens next is a clean rebuild of hemosim.org on Wix from these pages, with cross-links, editable content, quizzes, progress tracking, a blog and an authors page in the design from the start. Nothing on the live site is touched until the new site is ready, and the existing site is archived first.

Thank you for the depth of this review. The pages are markedly better for it.

Neal
