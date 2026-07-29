# HemoSim content library

## Standing facts

Home base: Claude is the cockpit, Dropbox is the file backbone, Notion is notes
and knowledge, GitHub is for versioned and code work.

PHI wall: this is a personal consumer Claude account with no BAA. Work OneDrive,
work SharePoint, work email, and anything containing PHI stay walled off and are
never connected. Never write PHI into this folder or either repo.

Google Drive is not used. Do not read from or write to Google Drive. Everything
was migrated to Dropbox under /Claude. If a task seems to require Drive, ask first.

Writing style: never use em dashes or en dashes. Use commas, colons, periods, or
parentheses. Graduate and professional level language. Direct and structured.
This applies to chat replies and to every file written here.

## Read this before any content work

`_Claude Context/` holds the project state. Read it in order at the start of a
session that touches content:

1. `00 - START HERE.md`, orientation and current status
2. `01 - Project State and Content.md`, people, version history, outline structure, sources
3. `02 - Build Strategy and Decisions.md`, the web build plan and locked decisions
4. `03 - Git and GitHub Setup.md`, how version control here works

**When Neal hands back a reviewed Module Edit Doc**, stop and read
`_Claude Context/04 - Module Edit Workflow.md` first, then follow it in order.
It is a procedure, not background, and it records several traps that cost time
on the N1 pass. Do not improvise this from scratch.

Then `_Source Library/INDEX.md` before any module build, to know which sources
feed which module.

## What this folder is

The content library for the HemoSim hemodynamics curriculum (hemosim.org, due
September 1, 2026). Source decks, primary literature, outline versions, and the
Word module edit docs Neal revises directly.

It is not the website. The site code lives in a separate repo, `hemosim-web`,
checked out at `~/Claude/hemosim-web`, which has its own CLAUDE.md governing that
work. Do not copy binaries into that repo. When content is needed there, read it
from here and bring the text over.

## The two repos

`hemosim-content` is this folder, private on GitHub. It tracks working documents
only, about 7 MB. The large reference folders (`_Source Library`, `HemoSim Base
Files`, `PA Catheter Topics`, archived `web-pilot`) are excluded by `.gitignore`
and backed up by Dropbox instead.

`hemosim-web` is the site code, private on GitHub, checked out at `~/Claude/hemosim-web`.

## Source of truth

Physiology claims trace to primary sources. The named authorities for this
curriculum are Jon Emile Kenny, Eduardo Kattan, Sheldon Magder, and Michael
Pinsky. Never invent a citation, a value, or a waveform. If a claim cannot be
sourced, flag it rather than asserting it.

## Working agreement

Commit in small, described increments. Before any change that touches more than
three files, say what you intend to do and wait for confirmation.

Before every commit, show which folders have changes and ask which to include.
Do not assume the scope carries over from last time.

Explain what a command does and why before running it, especially anything that
reaches outside this folder.
