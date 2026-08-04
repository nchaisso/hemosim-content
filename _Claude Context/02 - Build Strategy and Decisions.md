# 02 - Build Strategy and Decisions

The web-build plan and the decisions locked with Neal. Last updated: 2026-07-30.

Current status lives in `00 - START HERE.md`. The procedure for applying a
reviewed edit doc is `04 - Module Edit Workflow.md`.

## Locked decisions

1. **Build the real site natively in Wix** (Wix Editor pages), on top of the
   roughly 36 pages already on hemosim.org. Reason: Neal must be able to edit
   content himself.
2. **The HTML pages are a design blueprint, not the content store.** They live in
   the `hemosim-web` repo at `~/Claude/hemosim-web`. Their styling becomes a Wix
   theme; the published words live in Wix.
3. **Native content means Neal edits directly in the Wix Editor, anytime, with no
   Claude and no rebuild.** The anti-pattern to avoid is embedding content as
   custom HTML, which would make him dependent on Claude for wording changes. So
   content is native and only interactive components are code.
4. **Interactive knowledge checks are added on top later**, incrementally, as
   reviewable drop-in components, page by page. Adding a check does not disturb
   the native content around it.

## Content standards that govern any module work

- **Never rebuild a module from the V8 outline alone.** Open its sources in
  `_Source Library/INDEX.md`, including speaker notes and the published Wix page.
- **Source precedence when they disagree:** published Wix wording and citations,
  then Notion depth, then deck narration. Still mine the speaker notes and the
  Notion Clinical and Physiological Correlation subpages for depth the published
  Wix page compresses out.
- **Depth standard:** connected prose, several `<h2>` sections, `.eq` equations,
  `.grid` tables. Roughly 1200 to 2000 words per module.
- **Writing standard (locked):** connected prose, not bullet dumps. Carry the
  module-to-module thread naturally in the opening and closing prose. No boxed
  recap, no boxed bridge.
- **Embed real figures** from the library rather than leaving placeholders, where
  the asset exists. Original SVGs are the answer when it does not.
- **Figure sourcing:** deck figures come from the .pptx, Wix and Notion figures
  via browser, animations as an exported static frame. Default cap 520px wide;
  other sizes need a CSS class, not an inline style. There is no image generation
  available, so a requested "generated" figure means a hand-written SVG.
- **Attribution:** every source gets a link. Any graphic with an attribution in
  Notion, Wix, or the slides carries it. AI-generated Wix and Notion graphics need
  none. All pptx graphics need attribution if used. Open questions are logged in
  `HemoSim Graphics Follow-Up.md`.

### Page components and the variable colours, settled 2026-08-04

The stylesheet in `hemosim-web` carries the components a module page is built
from. Use the class, do not write an inline style.

| Class | Use |
|---|---|
| *(none)* | figure capped at 520px, the default |
| `.fig img.w400` / `.w640` / `.wfull` | smaller, larger, and full column width |
| `.figpair` | two figures side by side, stacking under 640px |
| `.callout` + `img.abicon` | the At the Bedside box |
| `.callout.insight` + `img.insighticon` | the Physiologic Insights box, new in N7 |
| `main ul` / `main h3` | body lists and subheads |
| `.v-map` `.v-co` `.v-rap` `.v-papm` `.v-lap` `.v-svr` | shock-grid table headers |

**The hemodynamic variable colours are Neal's, not a design choice.** They were
read out of the cell shading he applied himself in the N5 edit doc: MAP `#EE0000`,
CO `#FFC000`, RAP `#00B050`, PAPm `#000000`, LAP `#F058CD`, SVR `#00B0F0`. One
colour per variable, not per role. Each has a darkened `-ink` pair used for text,
because most fail contrast on white; the raw fill is used only for the underline
rule and figure strokes. Put the class on the `<th>` and the stylesheet does the
rest.

An earlier attempt inferred a three-role scheme from a figure and was wrong. When
a document and an assumption disagree, the document wins.

This section is the single home for these rules. Files 00 and 01 point here rather
than restating them.

## Build history

**N1 to N8 fresh rebuild, completed 2026-07-23.** Run as a background workflow
(8 agents): one agent per module read its full source set and returned a deep
body, Wix references, and figure filenames; `_Source Library/assemble_rebuild.py`
copied the figures in and spliced each body into the page, preserving the header,
stepper, and pager chrome. The twelve script-managed Module Edit Docs were
regenerated. Banner
Concept B (flowing ribbons) is locked into the landing hero, which closed out the
"header is too conservative" note.

**Module review pass, began 2026-07-27.** N1 applied and published. See
`00 - START HERE.md` for which modules remain and `04` for the procedure.

## Tooling

All build scripts live in `_Source Library/` so they survive scratchpad resets:
`extract_all.py`, `wix_capture.py`, `banner_gen.py`, `assemble_rebuild.py`,
`make_edit_docs.py`, and `read_edit_doc.py`. They are tracked in git as of
2026-07-28.

`make_edit_docs.py` was repaired on 2026-07-28: its paths pointed at Google Drive
and at the old `web-pilot` location, it could not embed SVG, and it had no way to
regenerate a single module. **Always pass it a module label.** A bare invocation
regenerates all twelve and will silently destroy tracked changes on any module
Neal has reviewed but not yet handed back.

Its module list holds twelve entries (N1 to N8 plus the four N7 topics), but
`Module Edit Docs/` holds fourteen documents. The two Novice offshoot docs,
`N2-Offshoot-BedsideDO2VO2` and `N5-Offshoot-RAPVolume`, are not in the list and
cannot be regenerated by the script. If either offshoot page changes, its edit doc
has to be added to the list first or it will silently drift out of date.

`build_pilot_v8.py` was lost with an old scratchpad and was never reconstructed.
It is not needed: pages exist and are edited by splice, and the page chrome lives
in the existing HTML if a page ever has to be built from scratch.

## Wix native tools versus Velo (reference)

- **Native tools** (Editor and Studio, CMS, Wix Forms, app market): no code,
  team-maintainable. Handles roughly 90 percent, including content pages, menus,
  the level selector, the modular flow, images and references, and opening a
  detour in a new tab. Cannot do branching or scored quizzes, per-answer capture
  with IP, or writing to an external spreadsheet.
- **Velo**, Wix's JavaScript platform: can read request IP, call external APIs,
  run scoring and branching, store to collections. Needs a developer and deepens
  Wix lock-in.
- **Recommendation: hybrid, stay on Wix.** Native for everything except the
  interactive checks. Reserve code for the checks, answer capture, targeted
  feedback, and the data export, isolated to those components.

## How interactivity gets added after the native build

Claude cannot reliably operate the live Wix Editor, and Neal's rule is that any
Wix change must be reviewable before it is made permanent. So Claude builds the
component and hands it over as a drop-in that Neal or a helper pastes once.

It is a one-time paste per component, not a rebuild. Quiz content (questions and
feedback) can live in a Wix collection so Neal edits the wording himself; only
the scoring and capture logic stays as code.

### Answer capture: decided 2026-07-30

**Capture into a Wix Data collection via Velo, and export to Dropbox.** The
original design posted to a Google Sheet via Apps Script, which predates the
decision to stop using Google.

Dropbox cannot take the writes directly, for three reasons worth remembering
before anyone proposes it again:

1. **No append operation.** Adding a row means download, modify, re-upload. Two
   concurrent submissions and one silently overwrites the other. A file in a
   folder is not a database; Apps Script only worked because it serialized writes.
2. **Credentials would be public.** Anything in an embedded widget is readable by
   view-source, so a Dropbox token there is a published password.
3. **IP and request data need a server.** Browser code cannot see them. Removing
   Google removed the server, not just the spreadsheet.

Wix Data is a real database on a platform Neal already pays for, Velo backend
functions can read request headers, and the dashboard exports CSV. Dropbox
remains the archive, receiving that export. Nothing leaves platforms he controls.

**Still open:** whether the checks need Velo at all. If they are simple, native
Wix Forms captures submissions with no code, no IP, and no scoring or branching.
Confirm what the checks actually require before committing to code that has to be
maintained until 2026 and beyond.

## Linking one learner's answers across modules

Neal wants a learner's answers connected across questions and modules, without
exposing anything protected. The design:

**Identify by an opaque participant ID, never by a person.**

- **Anonymous by default.** On first visit the widget generates a random ID
  (`crypto.randomUUID()`) and stores it in `localStorage`. Every answer carries
  it. That links a learner's whole path with no registration and no personal data
  anywhere. It is a random number, meaningless outside the dataset.
- **Upgraded by sign-up, which is already planned.** If a learner registers
  through the Wix Members Area, store the **member ID** on subsequent answers and
  write one row mapping the old anonymous ID to it, so earlier work carries
  forward. Their email stays inside Wix Members, which is access controlled, and
  never enters the answers collection.

Limits of the anonymous ID, worth stating plainly: it breaks if the learner
clears site data, switches browser or device, or uses private browsing. Same
person on a phone and a laptop counts as two participants. Sign-up is what fixes
that, which is a reason to keep the sign-up link prominent.

**What the answers collection holds:** participant ID, module, question ID,
answer, timestamp, and the score if any.

**What it never holds:** name, email, free-text identifying anything, or a raw
IP address.

**Two settings that do the actual protecting:**

1. **Collection permissions must be write-only for site visitors**, with read
   restricted to admin. Wix Data permissions can otherwise expose a collection
   through the public API, which would publish the entire answer set. This is the
   single most important configuration step and must be verified, not assumed.
2. **If IP is wanted** for abuse control or deduplication, store a salted hash
   with the salt held server-side, never the address itself. An IP is personal
   data under GDPR and the site will have European visitors. If the only purpose
   is telling learners apart, the participant ID already does that and IP should
   be dropped entirely.

The Dropbox export therefore contains opaque IDs only, so the archive is not
sensitive even as it syncs.

**One clinical risk specific to this course.** Free-text answer fields invite a
learner to paste real patient details into a public website. Keep knowledge
checks to multiple choice or other structured responses. If a free-text field is
ever genuinely needed, it carries an explicit warning not to enter patient
information, and the same PHI wall that governs this project applies to whatever
comes back.

## Next steps

1. Finish the module review pass, N2 through N8.
2. Turn the approved pages into a Wix design template and a page-by-page build
   spec.
3. Neal or a Wix helper assembles the native Wix pages on top of the existing
   hemosim.org pages, applying the theme.
4. Add interactive knowledge checks as reviewable drop-in components, one at a
   time.

## Completed

- Prototype look and flow approved; the N1 to N8 rebuild superseded it.
- Header and hero redesign, closed by Banner Concept B.
- Topic 4 Q5 source fix, verified applied 2026-07-30: the explanation computes
  6.3 L/min and the incorrect-answers line reads "A, B, D". Topic 2 Q5 and Q17
  insertion tables were deliberately left as they are.
- The N0 Global Edit Doc was deleted by Neal on 2026-07-28. Earlier instructions
  to ignore it are obsolete.

## Tabled

- The interactive quiz-and-capture prototype, deferred by Neal. Building it also
  settles native versus Velo for the capture piece.
