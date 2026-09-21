# Git and GitHub Setup

**Date set up:** July 28, 2026

A reference for what was done and how to use it. Written to be readable cold, months later.

## The one-paragraph version

This Hemosim folder is now tracked by git, which saves a complete snapshot every time you commit. A copy of those snapshots lives on GitHub at `github.com/nchaisso/hemosim-content` (private). Your files stay in Dropbox exactly where they were, nothing moved. Only the 40 working documents are tracked, about 7 MB. The 1.3 GB of reference material is deliberately excluded.

## The two commands you need

```
git add -A && git commit -m "describe what changed"
git push
```

The first saves a snapshot on this Mac. The second copies it to GitHub. Both are run from this Hemosim folder. Claude Code can run them for you: just say what you changed.

Write commit messages describing **why** something changed, not what file it was. Git already knows which files changed. "Rewrote N4 waveform section after Gustavo's feedback" is useful in a year. "Updated file" is not.

## Vocabulary

**Repository (repo).** One folder on your computer plus the complete history of everything in it. The history lives in a hidden `.git` folder inside. Git only tracks the folder it sits in and everything beneath it.

**Commit.** A saved snapshot of the whole folder at one moment, with a message you write. Each gets a unique ID like `2d107f0`.

**Push.** Uploads your commits to GitHub. Manual. Nothing goes to GitHub until you push.

**Private repo.** Only you and people you explicitly invite can see it. Both HemoSim repos are private.

## Where things actually live

Your version history is on **this Mac**, in the hidden `.git` folder inside the Hemosim folder. That is the original, and it works with no internet.

GitHub holds a **copy**, updated only when you push. It is an off-site backup and a way to browse things in a web browser. If you commit for three weeks without pushing, all three weeks are safe locally. GitHub simply shows the older state until you push.

## The two separate repos

**`nchaisso/hemosim-content`** is this repo, holding the course documents. Created July 28, 2026. Lives in Dropbox at `Dropbox/Claude/CCM/Fellowship/Hemosim`.

**`nchaisso/hemosim-web`** holds the code that runs the live website. Created July 24, 2026. Its working copy on this Mac is `~/Claude/hemosim-web`. It has its own `CLAUDE.md` covering the site build; the standing facts that apply everywhere live in `~/.claude/CLAUDE.md`, and each repo's own file covers only what is specific to it.

They are separate because a repo tracks one folder, and these are two different folders holding two different kinds of work. Keeping them apart means each has a clean, readable history instead of website changes and document edits interleaved. This also matches the rule in the web repo's `CLAUDE.md`: that repo is not the content library, and binaries do not belong in it.

## What is tracked: 40 files, about 7 MB

| Location | Contents |
|---|---|
| `Module Edit Docs/` | 14 Word files: N1 through N8, N7 topic breakouts, offshoots |
| `Hemosim COntent Outlines for Wix Build/` | 8 Word files: content outline v1 through v8 |
| `_Claude Context/` | Project notes in Markdown, including this file |
| root | `PAC Simulation Mastery Checklist - Student Handout.docx` |
| root | `.gitignore`, `CLAUDE.md`, `.claude/settings.local.json` |
| `_Source Library/` root only | `INDEX.md`, `INGESTION PLAN.md`, and the six `.py` build scripts |

The rule of thumb: **documents you write and revise** are tracked, plus anything
plain-text that is small, diffs readably, and would be expensive to lose.

## What is excluded, and why

Listed in the `.gitignore` file:

- `_Source Library/`, 1.0 GB, **except** the two Markdown files and six `.py`
  scripts at its root, which are tracked (see the table above)
- `HemoSim Base Files for Claude Learning/`, 238 MB
- `PA Catheter Topics/`, 60 MB
- `Salient articles for hemodynamics (not for course)/`
- `web-pilot (ARCHIVED 2026-07-25...)/`
- `.DS_Store` and `~$*`, which are macOS and Word junk files

These are reference material you consult rather than author. Committing 1.3 GB would make every commit slow and bloat the history permanently, and unlike deleting a file, you cannot easily remove something from git history later. Reference material is still backed up by Dropbox.

To change this, edit `.gitignore`.

## Word documents in git: an important limitation

Git shows line-by-line changes for plain-text files. `.docx` files are compressed archives, so git can only store a full copy of each version and reports them as `Bin 50576 bytes`.

**What you get:** restore any committed version of any document.

**What you do not get:** a readable comparison of what changed between two versions.

The Markdown files in `_Claude Context/` are plain text and do show readable diffs.

## A deferred decision: the eight outline versions

There are currently eight files named `HemoSim Content Outline by Expertise Level` through `(v8)`. Git will preserve all eight forever, because it sees eight unrelated documents.

Replacing manual version numbers is what git is *for*. The alternative workflow: keep one file, edit it, and commit after meaningful changes. Git remembers each committed state, so version numbers move from the filename into the history.

**The tradeoff, and it is real:** that only works if you actually commit. Today, forgetting to save-as-v9 still leaves v8 intact. Under the new workflow, forgetting to commit means that intermediate state is simply gone. The safety net changes from automatic to deliberate.

**Decision made July 28, 2026:** deferred. Keep v1 through v8, build the commit habit first, revisit later. Clutter costs nothing.

**Revised 2026-09-20:** ahead of making the repo public, Neal chose to track v8 only. The earlier versions stay on disk and are ignored by git, because eight near-identical outlines would confuse an outside reader.

## Notes and open items

- **One computer.** Git and Dropbox both version files and do not coordinate. On a single machine this is fine. If a second Mac ever enters the picture, revisit this, because Dropbox syncing the `.git` folder mid-operation across two machines can corrupt it.
- **Standing preference:** Claude confirms which folders to include before each commit, since what matters may change over time.
- A `CLAUDE.md` at a folder's root loads automatically at the start of every session, whereas the files in `_Claude Context/` do not. That is why the read order is stated in `CLAUDE.md` rather than only here.
