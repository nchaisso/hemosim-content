# Wix Build Plan

Written 2026-09-13 from Neal's brief. The first priority is a working site. The
other capabilities are designed in from the start so nothing has to be rebuilt
to add them later. Read after files 00 to 04.

## Neal's requirements, in his order

0. Preserve the existing hemosim.org material somewhere it can be referred to or
   reverted to.
1. A clean rewrite of the entire site on Wix from the existing Novice and Core
   pages (Neal wrote "Intermediate" in the brief and confirmed "Core" on
   2026-09-13).
2. Hyperlinks between modules and concepts that connect to each other.
3. Neal can edit the wording of a module later, inside Wix.
4. Questions can be added later so a reader can check progress.
5. User identifiers can eventually be captured, to track progress and to see
   how the site is used and whether readers understand the concepts.
6. A blog and a comments section, eventually.
7. An authors page with Neal and Gustavo.
8. Video can be added to modules, with the insertion points flagged in advance.

## Architecture decision

Build the modules as **data, not as hand-placed Wix pages**. One CMS collection
holds every module; one dynamic page template renders them. This is the only
arrangement that satisfies 1, 2, 3, 4, 5 and 8 at once:

- The migration is a script, so the site can be regenerated from the HTML pages
  in this repo whenever the content changes, and the pilot stays the source of
  truth until Neal starts editing in Wix (at which point Wix becomes it, and the
  script is retired or run one way only).
- Neal edits a module's rich content field in the Wix CMS, in an editor that
  looks like a document, without touching layout.
- Cross-links are ordinary links to stable module URLs, `/modules/<slug>`, with
  anchors for concepts, so they survive edits.
- Questions, progress, videos and comments attach to a module by its slug in
  further collections, so adding them later needs no change to the modules.

Wix pieces this relies on, each to be confirmed against Neal's plan tier at the
start of Phase 1 (the free and lower plans lack some): the CMS (Content Manager)
with a rich content field type, dynamic pages, Velo for page code and backend
data hooks, the Wix Data and Media REST APIs with an API key for the migration
script, the Members Area, Wix Blog, Wix Comments, and Wix Video or a YouTube
embed. If the rich content field cannot carry our figures, equations, tables and
callouts with fidelity, the fallback is a plain HTML field rendered by Velo into
a rich text element, which loses in-Wix WYSIWYG editing but keeps everything
else. Test that on one page (I8 is the hardest: tables, equations, callouts,
SVG) before committing.

## Content model

Collections, all keyed by `slug`:

- `Modules`: slug, tier (novice, core, expert), order, title, eyebrow, lead,
  body (rich content), references (rich content or a repeater of items),
  prev and next slugs, status (draft, published).
- `Figures`: slug of module, figure id, media item, caption, alt, width class.
  Uploaded to the Media Manager by the script; SVGs go up as SVG (confirm SVG is
  accepted in rich content, otherwise render to PNG at 2x).
- `Questions` (Phase 4): module slug, position anchor, stem, options, answer,
  explanation, concept tag.
- `Progress` (Phase 5): member id, module slug, opened at, completed at,
  question results. Written only by backend code, never by the page.
- `Videos` (Phase 8): module slug, anchor, provider and id or media item,
  caption, status (placeholder, live).
- `Authors` (Phase 7): name, role, bio, photo, links.

## The migration script

Lives in `_Source Library/wix_push.py` (to be written). It reads each page of
`hemosim-web`, splits `<main>` into lead, body and references, converts the body
to the CMS rich content format (paragraphs, h2, h3, lists, tables, the `.eq`
blocks, the two callout types as styled containers, figures as media nodes),
uploads figures, and upserts the `Modules` and `Figures` rows through the REST
API. It is idempotent: running it twice changes nothing. It never deletes. A
`--dry-run` prints what would change. The API key is read from the environment,
never stored in the repo.

Link rewriting happens here: every `href="iN.html"` or `nN.html` becomes
`/modules/<slug>`, `#anchor` fragments are preserved, and the `.newtab` pattern
becomes `target="_blank"` on the link. Unresolved `<!-- TODO-LINK -->` comments
become entries in a link report, not links.

## Video flagging convention

Insertion points are marked in the HTML now, before the build, as
`<!-- VIDEO: <what the clip should show> | <source if known> -->` at the exact
spot, and the script turns each into a placeholder block in the module body and
a `placeholder` row in `Videos`. Known candidates on 2026-09-13: N3's capillary
refill demonstration (already a YouTube link, `youtu.be/aO3mqie46hQ`, becomes an
embed), I4's time-varying elastance videos on Notion and Wix (Gustavo's C213,
files to be identified), and the PAC insertion and waveform material in N7-T3
and N7-T4 if Neal has bedside footage. The inventory of every video on the
current Wix site and in Notion is a Phase 0 task, so the list is complete before
Phase 1 ends.

## Phases

**Phase 0, archive (before anything else).** Duplicate the site inside the Wix
dashboard so a full editable copy exists under Neal's account, named with the
date. Mirror the published site to
`_Source Library/wix-archive-2026-09/` with `wget --mirror` (HTML, images,
PDFs), commit it if under the repo's size rule, otherwise keep it in Dropbox
only. Export the Wix Media Manager. Record the site map (every URL) and the
video inventory in `_Source Library/wix/_captured.md`, which already holds the
29 page texts. Nothing on the live site changes.

**Phase 1, working site.** Confirm plan tier and enable Velo. Create the
collections and the dynamic page template in the house design (style.css is the
spec: type, colours, `.callout`, `.callout.insight`, `table.grid`, `.eq`, the
grouped stepper). Write and run the migration for N1 to N8, N7-T1 to T4 and I1
to I17. Build the static pages: home with the three tier cards, a pathway page
per tier listing its modules in order (Expert modules as "coming soon" rows), and the stepper as a component driven by
the `Modules` collection. Set up SEO titles and descriptions from the page data.
Publish to a staging URL, read every module against the pilot, then point
hemosim.org at the new site. Definition of done: every pilot page renders on Wix
with its figures, tables, equations and references, every internal link works,
and Neal can edit one module's wording in the CMS and see it live.

**Phase 2, cross-links.** Mostly done by the script in Phase 1. What remains is
concept-level linking: a `Concepts` list (Pms, venous return curve, z point,
wedge, PPV and so on) mapping each concept to the module and anchor that owns it,
and a pass that adds the link at the first mention in each module. Keep to the
rule from the I1 review: link only where an explicit nod is needed, in a new
tab, without narrating what the other module covers.

**Phase 3, editability.** Confirmed in Phase 1's definition of done. Add a
short written guide for Neal on editing in the CMS, what not to touch (slugs,
order, anchors) and how figures are swapped. Decide the direction of truth:
after Neal's first edit in Wix, the migration script is run only with
`--dry-run` to report drift, and edits flow from Wix outward.

**Phase 4, questions.** Add the `Questions` collection and a question block on
the dynamic page that renders any questions attached to the module, at the
anchor given, with immediate feedback and an explanation. No account needed to
answer. Authoring happens in the CMS. Seed from the existing N7 topic banks and
the assess, hypothesize, test prompts already in the Novice pages.

**Phase 5, identifiers and progress.** Turn on the Members Area with optional
sign-in (the site stays fully readable without an account). Backend code writes
`Progress` rows on module open, on completion and on each question answered.
Dashboards: per module, how many opened, how many completed, question accuracy
by concept tag. This is where "do people understand the concepts" is answered.
Privacy: state on the sign-in page what is stored and why, collect only email
and display name, and keep the data in Wix. No PHI is involved, but the PHI wall
still means no work systems are connected.

**Phase 6, blog and comments.** Install Wix Blog for posts and Wix Comments on
the module dynamic page and on posts. Comments require sign-in (uses Phase 5),
moderation on. Decide whether comments open on every module or only on a
discussion page.

**Phase 7, authors.** An `Authors` collection and a page with Neal and Gustavo,
and an author line on each module drawn from it. Names, roles, affiliations and
photos from Neal.

**Phase 8, video.** Replace each placeholder in `Videos` with the clip: Wix Video
for files Neal owns, YouTube embed for public clips. The module page renders the
embed at the anchor. The flagging convention above means no module text changes
when a video lands.

## Decisions taken 2026-09-13

- The middle tier is "Core" on the site.
- The Expert pathway exists on the site from day one as its tier card and
  pathway page, with each module shown as "coming soon" and no module pages
  published until written.
- Figures Gustavo pasted into an edit doc go on the page even where their
  labels read Pra or Pmsf; the caption states the notation.
- Domain cutover only after Neal has read the staging site end to end.

## Still to settle before Phase 1

- Which Wix plan the site is on, and that the CMS and Velo are usable on it.
- An API key for the migration script, created by Neal.

## How to check the plan, the CMS and Velo (for Neal)

1. Plan. Sign in at manage.wix.com, open the account menu (your avatar or
   name, top right) and choose "Premium Subscriptions", or go straight to
   manage.wix.com/account/premium-subscriptions. The page lists every paid
   item: the site plan for hemosim.org with its name (for example Light, Core,
   Business, Business Elite, or a Studio plan), the domain, and any apps. Tell
   Claude the plan name as printed. If the page is empty, you are in a
   different Wix account from the one that owns the site.
2. Which editor. Open the site from "My Sites" and click "Edit Site". If the
   editor's top bar has a "Dev Mode" menu, it is the classic Wix Editor. If it
   shows a code icon (a `< >` symbol) in the left toolbar and the word Studio
   in the corner, it is Wix Studio. Both support what the plan needs.
3. Velo. Classic Editor: top bar, "Dev Mode", then "Turn on Dev Mode". A code
   panel appears at the bottom and a "Velo Sidebar" on the left. Wix Studio:
   click the code icon in the left toolbar, then "Start coding" if prompted.
   Velo is free; no plan is required.
4. CMS. In the site dashboard (manage.wix.com/dashboard/<site id>), the left
   menu has a "CMS" entry (older accounts say "Content Manager"). Open it and
   click "Create Collection" once to confirm it works, then delete the empty
   collection or leave it. The CMS is free; the limit on free sites is 1,000
   collection items on a classic account, far more than this site needs
   (about 60 modules, a few hundred questions). A connected domain such as
   hemosim.org already implies a paid plan.
5. Site ID. It is the string after `/dashboard/` in the dashboard URL,
   for example `manage.wix.com/dashboard/1a2b3c4d-.../home`. Copy it.

## How to create the API key (for Neal)

1. Go to manage.wix.com/account/api-keys (account menu, "API Keys"). Only
   the account owner or a co-owner can do this.
2. Click "+ Generate API Key" (top right).
3. Under "Key details", name it `hemosim-migration 2026-09`.
4. Under permissions, choose the two the script needs and nothing else: the
   CMS or Wix Data permission (read and write collection items and manage
   collections) and the Site Media permission (upload files). The exact
   labels are grouped by product; if the list is confusing, choose "All site
   permissions" for now and we replace the key with a narrower one once the
   migration is done. The default permission that lists your sites cannot be
   removed.
5. Under site access, choose the hemosim.org site only, not all sites.
6. Click "Generate Key". Wix emails a six-digit code; click "Send Code",
   enter it, then "Verify & Generate Key".
7. The token is shown once. Copy it into your password manager immediately.
   Do not paste it into chat, email, a file in Dropbox, or the repo. When the
   script runs, it reads the key from an environment variable that you set
   in the terminal for that session only.
8. On the same page, copy the "Account ID" ("Copy ID"). The script needs the
   account ID, the site ID and the token.
9. When the migration is finished and verified, delete the key on the same
   page.

## Order of work for the next session

1. Phase 0 archive, in full.
2. Plan-tier check and a one-page fidelity test of the rich content field with I8.
3. Write `wix_push.py` and run it for N1 to N8 in dry run, then live to staging.
4. The rest of Phase 1.
