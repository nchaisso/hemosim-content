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
- Avoid overusing the word "honest". Avoid the semicolon; prefer a period, a
  comma, or a colon.
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

## The variable colours, and the open question

Sampled from Neal's own figure (N5 `img01.png`): the cardiac function curve is
**#A8034F** and the venous return curve is **#00B0F0**. Those two are settled.

`--filling-ink` (#0077A6) is the darkened form of #00B0F0 for text, which needs
the contrast. Use `--filling` itself only for swatches, rules, and figure strokes.

**Unresolved:** Neal asked for the shock-grid table headers to be colour-coded
"as they are coded in the figure above", but the figure defines two colours and
the tables carry up to six variables (MAP, CO, RAP, PAPm, LAP, SVR). The working
assumption is three semantic roles, matching the labels Neal himself used in N3:
flow (CO) takes `--flow`, filling (RAP and the other pressures) takes
`--filling`, tone (SVR) takes `--tone`, which is a placeholder amber that Neal
has not confirmed. Apply that mapping, and flag in your report that you did.

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

- **Attribution.** If Neal struck a `Source:` line and the figure is being
  replaced, that is right. If the figure is staying, say so, because every deck
  graphic in use requires attribution.
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
