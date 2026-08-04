# 05 - Review Pass Contract

The shared rules for the N1 to N8 plus topic-page review pass that began
2026-08-03. Every agent working a module reads this file before touching a page,
alongside `04 - Module Edit Workflow.md`, which is the procedure.

File 04 tells you *how* to apply a returned edit doc. This file tells you what is
already decided, what is off limits, and what to do when the instruction is
ambiguous. Where the two disagree, this file wins for the duration of this pass.

## Your scope

You own exactly one page in `~/Claude/hemosim-web/`. Do not open, read, or edit
any other module's page. If your edit doc references another module, note it in
your report rather than reaching across.

## Four things you must not do

1. **Do not run git.** Not `add`, not `commit`, not `checkout`, not `stash`.
   Commits are made centrally after review, and the working agreement requires
   confirming commit scope with Neal every time. Leave your changes in the
   working tree.
2. **Do not edit `style.css`.** Every class this pass needs already exists (see
   below). If you need one that does not, stop and report it; do not add it. Ten
   agents editing one shared file is the only real collision risk in this pass.
3. **Do not edit the returned `.docx`.** It is the record of what Neal asked for.
4. **Do not run `make_edit_docs.py`.** With no argument it regenerates all twelve
   modules and silently destroys tracked changes on anything Neal has reviewed
   but not handed back. Regeneration happens centrally, one label at a time.

## Terminology, locked

These come from Neal and are not stylistic preferences to weigh:

- **venous return curve**, never Guyton curve.
- **cardiac function curve**, never Starling curve. Naming the Frank-Starling
  curve once, parenthetically, where the concept is first introduced is fine.
- **Pms**, not MSFP, wherever the change does not break a quoted equation.
- Avoid overusing the word "honest".
- **Semicolons.** Convert them in prose to a period, a comma, or a colon,
  including ones Neal did not mark and ones that predate this pass. **Leave them
  alone inside equation legends**, the `<small>` text under an `.eq` block, where
  they separate list items (`Hb, hemoglobin (g/dL); SaO2, arterial saturation`)
  rather than joining sentences. Neal confirmed this split on 2026-08-03.
- **No em dashes and no en dashes anywhere**, including in text Neal typed
  himself. He typed "So - " in the N1 closing and it was rendered as a comma.
  Normalize silently and note it in your report.

Several pages still say "Guyton curve" or "MSFP" in prose that Neal did not mark
up. Fix those too. The convention is global, not per-instruction.

## Figures are already extracted

Do not unzip a `.docx`. Every embedded image from every returned edit doc is
already extracted to:

    _Source Library/edit-doc-images/<LABEL>/

Each folder has the images numbered in reading order (`img01.png`, `img02.png`)
and a `manifest.md` giving, for each one, its paragraph index and the nearest
non-empty paragraph before and after it. That is how you resolve a positional
instruction: "[Insert the graphic above]" means the image whose `after` context
is that instruction.

To use one, copy it into `~/Claude/hemosim-web/img/` with a descriptive,
module-prefixed name (`n5-vr-cf-overlap.png`, not `img02.png`). The prefix is
what keeps ten agents from colliding in one directory.

Check the existing library before importing anything: `_Source Library/decks/images/`
for deck figures, `_Source Library/notion/extracted/` for Notion figures. There is
no image generation. A requested "drawn" or "generated" figure means a
hand-written SVG.

## CSS classes available to you

Already in `style.css`. Use these rather than inline styles.

| Class | Use |
|---|---|
| `.fig img.w400` | figure capped at 400px |
| *(no class)* | figure capped at 520px, the default |
| `.fig img.w640` | "make this bigger" |
| `.fig img.wfull` | "as large as possible" |
| `.figpair` | two figures side by side, stacking on narrow screens |
| `.callout` | the At-the-Bedside box, with `img.abicon` |
| `.callout.insight` | the Physiologic Insights box, with `img.insighticon` |
| `.v-flow` `.v-filling` `.v-tone` | colour-coded table headers |

The Physiologic Insights box is new in this pass and its icon is
`img/physiologic-insights-icon.svg`. Structure it exactly like an existing
`.callout`, with a `<div class="tag">Physiologic insight</div>` where the
At-the-Bedside box puts its bolded lead-in.

## The variable colours, settled

One colour per variable, not per role. These are read straight out of the cell
shading Neal applied himself in the N5 edit doc, which is the table he means when
he writes "the same colors I used for parameters in N5". Do not derive them from
a figure and do not invent one for a variable not listed here.

| Variable | Class | Fill | Text |
|---|---|---|---|
| MAP | `.v-map` | `#EE0000` | `#C00000` |
| CO | `.v-co` | `#FFC000` | `#8F6400` |
| RAP | `.v-rap` | `#00B050` | `#00753A` |
| PAPm | `.v-papm` | `#000000` | `#000000` |
| LAP | `.v-lap` | `#F058CD` | `#B01E90` |
| SVR | `.v-svr` | `#00B0F0` | `#006B96` |

Put the class on the `<th>`. The stylesheet then sets the text in the darkened
form and the underline rule in Neal's exact fill, so the document's colour survives
where it is visible and the header stays readable. You do not need to think about
which is which. N3 and N5 carry the shading in their own docs; N6 and N8 do not,
which is why they point back at N5.

An earlier draft of this file inferred a three-role scheme from a figure. That was
wrong, and it was caught by an agent checking the document rather than trusting
the contract. If something here contradicts what is actually in Neal's file, the
file wins. Say so in your report.

## Links to modules that do not exist yet

Several edit docs ask for a link to an intermediate module (I8, I11, "the
appropriate module in the intermediate level modules"). None are built. Render
the sentence as plain text with no anchor, and mark the spot with an HTML
comment so it is greppable later:

    <!-- TODO-LINK: intermediate module on the vascular waterfall (I8) -->

Do not create a live href, and do not add visible "coming soon" text.

## References

Verify every citation through PubMed at pubmed.ncbi.nlm.nih.gov, the US source.
Do not use Europe PMC. The eutils recipes are in file 04, step 5.

**In this pass, do not verify references yourself.** A single agent handles every
citation across all ten modules in one pass, so that the formatting and the
free-full-text reporting stay consistent. Put any citation you need into your
report as a request, in whatever form the edit doc gave it, and leave the
reference list alone. Never invent a DOI, a PMID, or a citation.

## When the instruction is ambiguous

Sort what you find into three groups, exactly as file 04 says: wording you can
apply unambiguously, asset work, and genuine questions. Apply the first group.
Do the asset work you can. **Log the third group. Do not guess and do not
silently pick an interpretation.** An unresolved item that is clearly flagged
costs Neal a sentence. A wrong guess that reads plausibly costs him a review pass
to find.

Watch for two traps recorded from the N1 pass:

- **Attribution.** If Neal struck a `Source:` line, it stays struck. Do not
  restore it and do not raise it, even when the figure is staying and file 01
  would otherwise require attribution for a deck graphic. He ruled on this on
  2026-08-03: a deletion he made himself is deliberate. This overrides step 3 of
  file 04, which still tells you to flag it.
- **Edits that invalidate their surroundings.** Changing a figure can falsify the
  caption, the attribution footer, and any prose that refers to it. Reread those
  after you edit.

## What to return

Do not paste the page back. Return a short report:

1. What you applied, grouped as wording, figures, structure.
2. Every item you could not resolve, with the exact bracketed instruction and
   what you would need to proceed.
3. Citations requested, passed through for the references agent.
4. Anything you noticed that the edit doc did not mention: a stale claim, a
   broken caption, a dash you normalized, a Guyton or MSFP you fixed.
5. Any CSS class you needed and did not have.

Keep it under 400 words. The orchestrator reads reports, not pages, and that is
what keeps this pass from collapsing under its own context.
