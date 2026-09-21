# HemoSim content

The working library behind [HemoSim](https://github.com/nchaisso/hemosim-web), a
modular, case-based curriculum in bedside hemodynamics for clinicians who care
for patients in shock.

If you want to read the curriculum, go to
[hemosim-web](https://github.com/nchaisso/hemosim-web). This repository is the
workshop: the review documents, the curriculum outline, the project notes, and
the scripts that move content between them and the web pages. It is public so
that the process is visible, not because it is the best way to read the material.

> **Status: work in progress.** The content is under active physician review. It
> is an educational resource, not medical advice.

## Who HemoSim is for

Healthcare providers, pitched at the level of a physician who manages shock.
Medical students, physician assistants, and nurse practitioners should find it
usable, although it is not written specifically for those groups.

## The three tiers

| Tier | Modules | Purpose |
| --- | --- | --- |
| **Novice** | N1 to N8, with four pulmonary artery catheter topics under N7 | A systematic bedside approach to shock |
| **Core** | I1 to I17 | The physiology behind the bedside approach, in depth |
| **Expert** | not yet built | Edge cases, controversies, and the primary literature |

The Core tier was originally called "Informed." The visible label changed on the
site, but file names, script names, and the internal notes in this repository
still use the old word. Wherever you see "Informed" or an `I` prefix here, read
"Core."

## What is in this repository

| Path | Contents |
| --- | --- |
| `Module Edit Docs/` | One Word document per module. Each is generated from the finished web page so that a physician reviewer can mark it up with tracked changes and comments. These reflect the current state of the site. |
| `Module Edit Docs/_issues/` | One short Markdown file per module listing what is still open: source defects, decisions awaiting a physician's judgement, and notes. Its own README explains the format. |
| `Informed Build - Issues for Review` | The open questions from the Core tier build, collected in one place (Markdown, with a Word copy for reviewers). |
| `Hemosim COntent Outlines for Wix Build/` | The curriculum outline by expertise level: which concept is taught at which tier. Only the current version (v8) is kept here. |
| `_Source Library/` | The index of source material, the plan used to ingest it, and the Python scripts described below. The source material itself is not in the repository. |
| `_Claude Context/` | Project notes written for the AI assistant used during the build: project state, build decisions, the edit workflow, and setup notes. Start with `00 - START HERE.md`. |
| `CLAUDE.md` | The standing instruction file for that assistant. |

### What is deliberately not here

The slide decks, journal PDFs, and other reference material that originally
guided the build are not tracked. They are large, they rarely change, and much
of the material is under third-party copyright. Superseded drafts, including
earlier outline versions and reviewers' marked-up originals whose edits have
already been applied, are also kept out so that what you see here matches the
current site.

## How a module moves from draft to page

1. A module page is drafted in HTML in the
   [hemosim-web](https://github.com/nchaisso/hemosim-web) repository.
2. `make_edit_docs.py` generates a Word edit doc from that page, with the
   module's open issues printed at the top.
3. A physician reviewer marks up the Word document: tracked changes for wording,
   bracketed instructions and comments for layout, figures, and references.
4. `read_edit_doc.py` extracts the markup, and the changes are applied to the
   HTML page. The returned document is never edited. It is the record of what
   the reviewer asked for.
5. The page is linted (`lint_page.py`) and its references are rebuilt and checked
   against PubMed (`build_refs.py`, `verify_refs.py`).
6. The edit doc is regenerated from the finished page, which keeps the two in
   step for the next review pass.

The full procedure is `_Claude Context/04 - Module Edit Workflow.md`.

## Scripts

All scripts are in `_Source Library/` and use Python 3.

| Script | Purpose |
| --- | --- |
| `make_edit_docs.py` | Generate the Word edit docs from the web pages |
| `read_edit_doc.py`, `read_any_edit_doc.py` | Read tracked changes, comments, and embedded images out of a returned edit doc |
| `extract_edit_doc_images.py` | Pull the figures a reviewer pasted into an edit doc |
| `lint_page.py` | Check a page against the site's conventions |
| `build_refs.py`, `verify_refs.py` | Build a page's reference list and verify each entry against PubMed |
| `make_pac_tracings.py` | Draw the pulmonary artery catheter waveform figures as SVG |
| `make_informed_shell.py`, `assemble_rebuild.py` | Scaffold and assemble module pages |
| `md2docx.py` | Convert Markdown to Word for reviewers |
| `banner_gen.py` | Generate the site banner artwork |
| `wix_capture.py` | Capture the text and image links of an earlier published version of the site, for comparison |
| `extract_all.py` | Extract text and figures from the source material (requires the source library, which is not included) |

Several scripts assume the web repository is checked out alongside this one and
contain paths specific to the authors' setup. They are shared as a record of
method and will need adjustment to run elsewhere.

## Evidence standard

Physiology claims are traced to primary literature rather than to secondary
summaries. Every page carries a numbered reference list checked against PubMed,
and figures taken or adapted from published work are credited in their captions.
Where a claim could not be sourced, the intent is to flag it instead of asserting
it.

## How it was built

The pages and tooling were produced with the help of Claude, an AI assistant
from Anthropic, working under physician direction, followed by line-by-line
review from critical care physicians. `CLAUDE.md` and `_Claude Context/` are that
assistant's working instructions and notes. They are left in place for
transparency about the process, and they are written for the assistant, so
expect shorthand and references to the authors' own working environment.

## Feedback

Corrections to the curriculum are best raised as issues on
[hemosim-web](https://github.com/nchaisso/hemosim-web), naming the page and the
passage. Issues about the scripts or the workflow belong here.

## Copyright

Copyright 2026, the HemoSim authors. All rights reserved. Figures reproduced or
adapted from published work remain the property of their original publishers.
