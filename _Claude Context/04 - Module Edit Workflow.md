# 04 - Module Edit Workflow

How to apply a reviewed Module Edit Doc to its web page. Written from the N1 pass
on 2026-07-28, the first module taken end to end. Follow it in order.

This is a procedure, not project state. Read it when a module comes back from
review, not every session.

## What Neal hands back

A file in `Module Edit Docs/`, for example `N4 - Edit Doc.docx`, containing two
different kinds of change:

- **Wording**, as Word tracked changes. Apply these to the page.
- **Layout, figure, and reference instructions**, written inline in
  **[square brackets]**.  
  **Scan the Word files for any comments as well and apply them to the page.  

Never edit the returned .docx. It is the record of what he asked for.

## Step 1. Read the markup

```
cd "_Source Library"
python3 read_edit_doc.py N4              # insertions and deletions in context
python3 read_edit_doc.py N4 --accepted   # the final text, changes accepted
```

Run both. The inline view shows intent (what replaced what). The accepted view
shows the target text. The script also lists embedded images, which matters when
an instruction says "redraw this" or "I used this one in Wix".

## Step 2. Sort the changes before touching anything

Split what you found into:

1. **Wording** you can apply immediately and unambiguously.
2. **Asset work**: figures to redraw, replace, resize, or source.
3. **Questions** where his intent is genuinely unclear.

Apply group 1 now. Do not block the whole module on group 3.

## Step 3. Apply the wording

The page lives in `~/Claude/hemosim-web/`, one file per module. Edit the HTML
directly, matching existing markup and class names.

**Watch for dashes.** Neal's locked rule is no em dashes and no en dashes, and it
applies to his own typed text too. He typed "So - " in the N1 closing; it was
rendered as a comma and flagged rather than published as a dash. Normalize and
tell him.

**Links to modules that do not exist yet.** Several instructions ask for a link
to an intermediate module. Render the sentence as plain text with no anchor and
mark the spot so it is greppable later:

    <!-- TODO-LINK: intermediate module on the vascular waterfall (I8) -->

Never a live href to a page that does not exist, and no visible "coming soon".

**Semicolons.** Convert them in prose to a period, a comma or a colon, including
ones that predate the pass. Leave them inside `<small>` equation legends, where
they separate list items (`Hb, hemoglobin (g/dL); SaO2, arterial saturation`)
rather than joining sentences. Neal confirmed this split on 2026-08-03.

**Watch for attribution.** He struck the `Source:` line under both N1 figures. If
a figure is being replaced, that is obviously right. If the figure is staying,
say so, because file 01 requires attribution for every deck graphic in use.

## Step 4. Figures

Assets are usually already local. Check before going to the internet:

- **Deck figures**: `_Source Library/decks/images/`, named by deck and slide.
- **Notion figures**: `_Source Library/notion/extracted/`, with the page folders.
  The B.U.S. bus came from here.
- **Wix**: `_Source Library/wix/` is **text only**. Images are recorded as URLs,
  so anything from Wix needs fetching or sourcing elsewhere.
- **Images embedded in the edit doc itself**, extractable with `zipfile`. Neal
  sometimes pastes the exact image he means.

**There is no image generation available.** When he asks for a drawn or generated
figure, the answer is a hand-written SVG. Two are in `img/` as worked examples:
`cain-vo2-do2-dependency.svg` (a data plot) and `circulatory-loop-volume.svg`
(a diagram encoding blood volume as channel width). SVG is a good outcome here:
crisp at any size, small, and hand-editable text that diffs properly in git.

Render an SVG to check it before wiring it in:

```
qlmanage -t -s 900 -o . img/whatever.svg
```

Sizes other than the 520px default need a CSS class, not an inline style. See
`.fig img.w400` in `style.css`.

## Step 5. References

Verify every citation through **PubMed at pubmed.ncbi.nlm.nih.gov**, the US
source. Do not use Europe PMC.

Find the PMID from a DOI:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<doi>[doi]&retmode=json
```

Or from a title, when there is no DOI:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<title+words>[title]&retmode=json
```

Get the authoritative citation details from the PMID:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<pmid>&retmode=json
```

Check whether a free full text exists, which means a PMC record:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pmc&id=<pmid>&retmode=json&linkname=pubmed_pmc
```

A returned PMC id means free full text at
`https://pmc.ncbi.nlm.nih.gov/articles/PMC<id>/`. An empty linkset means there is
no free version, and the DOI is the only link to give.

The human-readable equivalent, useful for a quick check, is
`https://pubmed.ncbi.nlm.nih.gov/?term=<doi>`.

Link every reference to its DOI, and add a free-full-text link only where a PMC
record genuinely exists. Of N1's five, only Secomb 2016 had one
(PMID 27065172, PMC4958049).

**Never invent a DOI or a citation.**  Report back
which references have no free version; he asks for this explicitly.

### Recall is not a source

Inventing a citation is the obvious failure and it is easy to avoid. The failure
that actually happens is subtler: writing down something you already "know" about
a trial without checking it. It reads as confident, it is often nearly right, and
nothing about the sentence signals that it was never verified.

**Every factual claim about a trial goes through PubMed before it is written to a
page.** Not just the citation string, the claim itself. That covers which trial
was largest, how many patients were enrolled, what the primary outcome was,
whether the result was positive, neutral or harmful, the year, the journal, and
the PMID. If you did not fetch it in this session, you do not know it.

The relevant field is in the `esummary` JSON already fetched above. For
enrollment and findings, pull the abstract:

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=<pmid>&rettype=abstract&retmode=text
```

Two failures from 2026-08-04, both caught only because Neal questioned them:

- A page was written saying randomized trials had not shown benefit from PA
  catheters, "the largest of which is PAC-Man". PAC-Man randomized 1041. Sandham
  2003 randomized 1994, nearly twice as many. The ranking was fabricated by
  recall. Neal also remembered an ARDS Network trial showing harm, which is FACTT
  (2006, 1000 patients, more complications in the catheter arm). It was missing
  from the page entirely.
- A PMID recalled for the ESCAPE trial returned an unrelated review on dyspnoea
  in the emergency department. Searching by author and title found the real paper.
  A wrong PMID produces a citation that looks correct and points somewhere else,
  which is worse than no citation because it survives review.

**A search costs seconds. A wrong trial fact on a teaching site outlives the
session that wrote it.** When a claim cannot be verified, write the page without
it and say so, rather than softening it into something vague that is still
unsourced.

## Step 6. Look at the page

Do not skip this. Serve it and read it in a browser:

```
cd ~/Claude/hemosim-web && python3 -m http.server 8731
```

Then open `http://localhost:8731/n4.html`. Kill the server afterwards.

## Step 7. Fix anything the edits invalidated

Changing figures can falsify surrounding text. The N1 attribution footer still
claimed every figure came from a source deck after two became original diagrams.
Reread the captions, the footer, and any prose that references a figure.

## Step 8. Regenerate the edit doc

```
cd "_Source Library"
python3 make_edit_docs.py N4
```

**Pass the label.** With no arguments it regenerates all twelve modules and will
silently destroy tracked changes on any module Neal has reviewed but not yet
handed back.

**Confirm his annotated copy is committed first:**

```
git log --oneline -- "Module Edit Docs/N4 - Edit Doc.docx"
```

Regenerating overwrites it. Committed means recoverable with
`git checkout <commit> -- "Module Edit Docs/N4 - Edit Doc.docx"`. Tell him the
commit hash.

Known gap: images inside a `callout` div are rendered as a bracketed text note,
not embedded, so they appear on the page but not as pictures in the edit doc.

## Step 9. Commit both repos

The work spans two repos and needs two commits.

- `hemosim-web`: the page, `style.css`, new files in `img/`.
- `hemosim-content`: the regenerated edit doc, plus any script changes.

Confirm commit scope with Neal first, every time. Write the message about why the
change was made, and use `git commit -F <file>` when the message contains quotes,
because inline quoting breaks the shell.

## Step 10. Update the record

Update `00 - START HERE.md` with which modules are applied and which remain.
Propose it rather than waiting to be asked.

## Things that cost time on N1

- `make_edit_docs.py` pointed at Google Drive and was unrunnable. Fixed, but
  check the other scripts in `_Source Library` before trusting them.
- `python-docx` cannot embed SVG. `make_edit_docs.py` now renders a PNG first.
- Six pages still date from 2026-07-13 and were not part of the July 23 rebuild:
  both Novice offshoots and the four N7 topic pages. Expect them to be thinner
  than N1 through N8.

## Running more than one module at once

The 2026-08-03 pass applied ten modules with one agent per module. What made it
work, and what would break it:

- **One agent owns one page.** Ten agents on ten pages never collide. Ten agents
  on one shared stylesheet would, and a broken rule there breaks every page at
  once. So agents may not edit `style.css`: define every class up front, and have
  them report a missing one instead. Both real gaps this pass, body lists and
  `h3`, surfaced that way and cost nothing.
- **Agents do not run git and do not regenerate edit docs.** Commits need scope
  confirmed with Neal each time, and a bare `make_edit_docs.py` destroys tracked
  changes. Both stay central.
- **References are one pass, not ten.** Per-module citation work drifts in format
  and cannot see a citation orphaned on another page.
- **The orchestrator reads reports, not pages.** That is what keeps the whole
  thing inside one context.
- **Tell agents that the document beats the instructions they were given.** The
  colour scheme in this pass was wrong in the brief and right in Neal's file, and
  an agent caught it only because it was told to check.
- **A read-only verification pass at the end earns its keep.** It found a false
  physiology claim created by a blanket find-and-replace, two duplicated
  sentences, and an invalid HTML entity. It also produced one confident finding
  that was wrong, so verify its claims before acting on them.
