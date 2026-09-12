# -*- coding: utf-8 -*-
# Convert each web-pilot page into an editable Word "edit doc" (prose + embedded small figures + [bracketed] layout notes).
# Reconstructed 2026-07-23 after the scratchpad reset; kept here in the Source Library so it persists.
import os, re, subprocess, tempfile, html as H
from html.parser import HTMLParser
from docx import Document
from docx.shared import Pt, RGBColor, Inches

# Paths updated 2026-07-28. The pages moved out of Dropbox into their own repo, and
# Google Drive (the old BASE) is no longer used at all.
WP = '/Users/chaissn/Claude/hemosim-web'
BASE = '/Users/chaissn/Library/CloudStorage/Dropbox/Claude/CCM/Fellowship/Hemosim'
OUT = os.path.join(BASE, 'Module Edit Docs')
os.makedirs(OUT, exist_ok=True)


def as_png(path):
    """python-docx cannot embed SVG, so render a PNG copy via macOS QuickLook."""
    if not path.lower().endswith('.svg'):
        return path
    cache = os.path.join(tempfile.gettempdir(), 'hemosim_svg_png')
    os.makedirs(cache, exist_ok=True)
    out = os.path.join(cache, os.path.basename(path) + '.png')
    if not os.path.exists(out):
        subprocess.run(['qlmanage', '-t', '-s', '1400', '-o', cache, path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out if os.path.exists(out) else None


# Report a figure's real rendered width in the layout note.
#
# This used to be hardcoded as "capped at ~520px wide" regardless of the figure's
# actual class, so a figure sitting at w400 was described to Neal as 520. He then
# judged "make this bigger" against a number he had never actually been shown.
# Caught on the N1 pass, 2026-08-03. Keep this table in step with style.css.
FIG_WIDTHS = {
    'w400': 'capped at 400px wide',
    'w640': 'capped at 640px wide',
    'wfull': 'full column width, about 750px',
}


def fig_width(cls):
    for k, v in FIG_WIDTHS.items():
        if k in (cls or '').split():
            return v
    return 'capped at 520px wide, the default'


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.blocks = []; s.inmain = False
        s.collect = None; s.buf = ''; s.skip = 0
        s.fig = None; s.grid = None; s.row = None; s.bus = None; s.box = None; s.callout = None
        s.refs = None; s.cdepth = 0

    def handle_starttag(s, t, attrs):
        a = dict(attrs); c = a.get('class', '')
        if t == 'main': s.inmain = True; return
        if not s.inmain: return
        if t == 'br' and s.collect: s.buf += '\n'; return
        # `refs` used to be skipped here alongside the page furniture. It is not
        # furniture: skipping it left Neal with no way to see, prune or add a
        # reference while reviewing, and the only reason that went unnoticed is
        # that the older docs predate this script and still carry their lists.
        # See the emitter below for the split between which references appear
        # (this document decides) and how they read (PubMed decides).
        if t in ('div', 'p') and ('pager' in c or 'eyebrow' in c or 'attrib' in c):
            s.skip += 1; return
        if s.skip: return
        if t == 'div' and s.callout is not None: s.cdepth += 1; return
        if t == 'div' and 'refs' in c.split(): s.refs = []; return
        if t == 'li' and s.refs is not None: s.collect = 'refitem'; s.buf = ''; return
        # Body lists arrived on the site 2026-08-03 (N7-T1's balloon safety list).
        # Without this they parse to nothing and vanish from the review doc.
        if t == 'li': s.collect = 'listitem'; s.buf = ''; return
        if t == 'h1': s.collect = 'h1'; s.buf = ''
        elif t == 'h2': s.collect = 'h2'; s.buf = ''
        # Subheads arrived 2026-08-03 (N7-T2) and were silently dropped from every
        # edit doc until 2026-09-12, when the N7-T3 rewrite leaned on them.
        elif t == 'h3': s.collect = 'h3'; s.buf = ''
        elif t == 'p' and 'closing' in c: s.collect = 'closing'; s.buf = ''
        elif t == 'div' and 'eq' in c.split(): s.collect = 'eq'; s.buf = ''
        elif t == 'div' and 'figframe' in c: s.collect = 'figframe'; s.buf = ''
        elif t == 'figure': s.fig = {'img': None, 'cap': ''}
        elif t == 'img' and s.fig is not None: s.fig['img'] = a.get('src'); s.fig['cls'] = c
        elif t == 'figcaption': s.collect = 'figcap'; s.buf = ''
        elif t == 'div' and 'callout' in c: s.callout = {'txt': '', 'href': None, 'insight': 'insight' in c.split()}
        elif t == 'a' and s.callout is not None: s.callout['href'] = a.get('href')
        elif t == 'table' and 'grid' in c: s.grid = []
        elif t == 'tr' and s.grid is not None: s.row = []
        elif t in ('td', 'th') and s.row is not None: s.collect = 'cell'; s.buf = ''
        elif t == 'div' and 'bus' in c.split(): s.bus = []
        elif t == 'div' and 'box' in c and s.bus is not None: s.box = []
        elif t == 'div' and c in ('l', 't', 'd') and s.box is not None: s.collect = 'boxpart'; s.buf = ''
        elif t == 'p' and s.collect is None and s.callout is None: s.collect = 'p'; s.buf = ''

    def handle_data(s, d):
        if s.skip or not s.inmain: return
        if s.callout is not None and s.collect not in ('cell', 'boxpart') and s.fig is None:
            s.callout['txt'] += d
        if s.collect: s.buf += d

    def handle_endtag(s, t):
        if t == 'main': s.inmain = False; return
        if not s.inmain: return
        if t in ('div', 'p') and s.skip:
            s.skip -= 1; return
        if t == 'div' and s.callout is not None and s.cdepth:
            s.cdepth -= 1; return
        b = s.buf.strip()
        if t == 'li' and s.collect == 'refitem':
            s.refs.append(b); s.collect = None; return
        if t == 'li' and s.collect == 'listitem':
            s.blocks.append(('li', b)); s.collect = None; return
        if t == 'div' and s.refs is not None and s.collect != 'refitem':
            s.blocks.append(('refs', s.refs)); s.refs = None; return
        if t == 'h1' and s.collect == 'h1': s.blocks.append(('h1', b)); s.collect = None
        elif t == 'h2' and s.collect == 'h2': s.blocks.append(('h2', b)); s.collect = None
        elif t == 'h3' and s.collect == 'h3': s.blocks.append(('h3', b)); s.collect = None
        elif t == 'p' and s.collect == 'closing': s.blocks.append(('closing', b)); s.collect = None
        elif t == 'div' and s.collect == 'eq': s.blocks.append(('eq', b)); s.collect = None
        elif t == 'div' and s.collect == 'figframe': s.blocks.append(('figframe', b)); s.collect = None
        elif t == 'figcaption': s.fig['cap'] = b; s.collect = None
        elif t == 'figure': s.blocks.append(('figure', s.fig)); s.fig = None
        elif t in ('td', 'th') and s.collect == 'cell': s.row.append(b); s.collect = None
        elif t == 'tr' and s.row is not None: s.grid.append(s.row); s.row = None
        elif t == 'table' and s.grid is not None: s.blocks.append(('grid', s.grid)); s.grid = None
        elif t == 'div' and s.collect == 'boxpart': s.box.append(b); s.collect = None
        elif t == 'div' and s.box is not None and s.collect is None and len(s.box) >= 3:
            s.bus.append(s.box); s.box = None
        elif t == 'div' and s.bus is not None and s.box is None and s.collect is None:
            s.blocks.append(('bus', s.bus)); s.bus = None
        elif t == 'div' and s.callout is not None and s.collect is None:
            s.blocks.append(('callout', s.callout)); s.callout = None
        elif t == 'p' and s.collect == 'p': s.blocks.append(('p', b)); s.collect = None


def note(doc, t, color='C0392B'):
    p = doc.add_paragraph(); r = p.add_run(t); r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor.from_string(color)


# Per-module issue blocks, added 2026-08-16.
#
# A module's known problems used to live only in a separate document, which meant
# holding two files open during review. Now an optional plain-text file per module
# is rendered as a block at the top of its edit doc, so the issues travel with the
# prose they concern and get resolved in the same pass.
#
# One file per module at `Module Edit Docs/_issues/<LABEL>.md`, for example
# `_issues/I14.md`. One issue per line, wrapped lines continue if indented. A line
# starts with its class:
#
#   SOURCE:    a defect in a deck, Notion page, document or the index. Fixing the
#              module alone leaves the error in circulation.
#   DECISION:  a judgement Neal or Gustavo has to make before the page is final.
#   NOTE:      something done deliberately and worth knowing, needing no action.
#
# Blank lines and lines starting with # are ignored. **No file means no block**,
# so every module without one regenerates byte-for-byte as before. That is what
# makes this safe to add to a script the Novice docs also use.
ISSUE_DIR = os.path.join(OUT, '_issues')
ISSUE_COLORS = {'SOURCE': 'B00000', 'DECISION': '0050A0', 'NOTE': '5A5A5A'}


def read_issues(label):
    path = os.path.join(ISSUE_DIR, '%s.md' % label)
    if not os.path.exists(path):
        return []
    out = []
    for raw in open(path):
        ln = raw.rstrip()
        if not ln.strip() or ln.lstrip().startswith('#'):
            continue
        if ln[:1].isspace() and out:                      # continuation of the previous issue
            out[-1] = (out[-1][0], out[-1][1] + ' ' + ln.strip())
            continue
        cls, _, rest = ln.partition(':')
        cls = cls.strip().upper()
        if cls not in ISSUE_COLORS:
            cls, rest = 'NOTE', ln                        # unclassed lines still render
        out.append((cls, rest.strip()))
    return out


def issue_block(doc, label):
    issues = read_issues(label)
    if not issues:
        return
    p = doc.add_paragraph()
    r = p.add_run('ISSUES FLAGGED FOR THIS MODULE (%d)' % len(issues))
    r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = RGBColor.from_string('B00000')
    note(doc, 'These were found while the module was built and are not part of the prose. '
              'SOURCE means the defect is in a deck, a Notion page or the source index and has to be '
              'fixed there too. DECISION means it needs your call before the page is final. NOTE is '
              'for information. Answer them in [brackets] like any other instruction.', '5A5A5A')
    for cls, text in issues:
        note(doc, '[%s: %s]' % (cls, text), ISSUE_COLORS[cls])
    doc.add_paragraph()


def build(nfile, label):
    html = open(os.path.join(WP, nfile)).read()
    body = html[html.find('<main'):html.find('</main>') + 7]
    p = P(); p.feed(body)
    d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(11)
    d.add_heading('HemoSim edit doc - %s' % label, level=0)
    note(d, 'HOW TO USE: edit the wording directly (Track Changes if you like). For layout or a figure (size, position, wrong/missing image) write a short instruction in [brackets] right where it applies. Send it back and I apply the wording to the page and the layout notes to the styling, then regenerate. This is a content+notes doc, so it will not look exactly like the web page.')
    d.add_paragraph()
    issue_block(d, label)
    for kind, data in p.blocks:
        if kind == 'h1': d.add_heading(data, level=1)
        elif kind == 'h2': d.add_heading(data, level=2)
        elif kind == 'h3': d.add_heading(data, level=3)
        elif kind == 'p': d.add_paragraph(data)
        elif kind == 'closing':
            pp = d.add_paragraph(); r = pp.add_run(data); r.italic = True
        elif kind == 'eq':
            pp = d.add_paragraph()
            for i, ln in enumerate(data.split('\n')):
                ln = ln.strip()
                if not ln: continue
                r = pp.add_run(('' if i == 0 else '\n') + ln); r.font.name = 'Consolas'; r.font.size = Pt(10.5)
        elif kind == 'bus':
            for box in data:
                l = box[0] if len(box) > 0 else ''; tt = box[1] if len(box) > 1 else ''; dd = box[2] if len(box) > 2 else ''
                pp = d.add_paragraph(style='List Bullet'); r = pp.add_run((l + ' - ' if l else '') + tt + ': '); r.bold = True; pp.add_run(dd)
        elif kind == 'grid':
            rows = data
            if rows:
                tb = d.add_table(rows=len(rows), cols=len(rows[0])); tb.style = 'Light Grid Accent 1'
                for ri, row in enumerate(rows):
                    for ci, cell in enumerate(row):
                        if ci < len(tb.rows[ri].cells):
                            tb.rows[ri].cells[ci].paragraphs[0].add_run(cell).font.size = Pt(9)
        elif kind == 'figure':
            src = (data.get('img') or ''); cap = data.get('cap', '')
            path = os.path.join(WP, src) if src else ''
            try:
                embed = as_png(path) if path and os.path.exists(path) else None
                if embed: d.add_picture(embed, width=Inches(3.1))
                else: note(d, '[figure image not found: %s]' % src)
            except Exception:
                note(d, '[figure could not embed: %s]' % src)
            cp = d.add_paragraph(); r = cp.add_run(cap); r.font.size = Pt(9.5); r.font.color.rgb = RGBColor.from_string('777777')
            note(d, '[Layout note: figure shown small here. On the web it is currently %s. '
                    'Say if you want it smaller/larger, moved, cropped, or replaced.]' % fig_width(data.get('cls', '')))
        elif kind == 'li': d.add_paragraph(data, style='List Bullet')
        elif kind == 'refs':
            # The reference list is emitted so Neal can prune it, which he cannot
            # do if he cannot see it. He pruned N8 from seven entries to two on
            # 2026-08-04 purely because the list was in front of him.
            #
            # But the citation text here is NOT authoritative and must never be
            # applied verbatim. Two of the details he typed by hand that same day
            # were wrong: Funk part II was given as issue 1 when it is issue 2,
            # and Permutt 1962 as ending on page 269 when it ends on 260. Those
            # are the ordinary errors of retyping a citation, and a round trip
            # through this document would write them straight back into the page.
            #
            # So: this document decides WHICH references appear. PubMed decides
            # HOW they read. The note below travels with the doc so the rule does
            # not live only in a context file.
            d.add_paragraph()
            d.add_heading('References', level=2)
            note(d, 'To DROP a reference, strike it. To ADD one, write [add: author, year, journal, '
                    'roughly what it is] rather than typing the citation out. Do not correct the text '
                    'of an entry here: every author list, volume, issue, page range, year and DOI is '
                    'fetched from PubMed when the page is rebuilt, so an edit made here is discarded '
                    'and a typo made here is caught. This list is what the page currently carries.',
                 '6B7280')
            for i, ref in enumerate(data, 1):
                pp = d.add_paragraph()
                r = pp.add_run('%d. %s' % (i, ref)); r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor.from_string('444444')
            if not data:
                note(d, 'This page currently carries no references.', '6B7280')
        elif kind == 'figframe':
            note(d, '[FIGURE PLACEHOLDER - to import at build: ' + re.sub(r'\s+', ' ', data) + ']', '9A6B00')
        elif kind == 'callout':
            kind = 'Physiologic Insight box' if data.get('insight') else 'Offshoot / At-the-Bedside link'
            body = re.sub(r'^\s*(Physiologic insight|At the Bedside)[\s.:-]*', '', re.sub(r'\s+', ' ', data.get('txt', '')).strip(), flags=re.I)
            note(d, '[' + kind + ': ' + body + (' (target: ' + data['href'] + ')' if data.get('href') else '') + ']', '9A6B00')
    outp = os.path.join(OUT, '%s - Edit Doc.docx' % label); d.save(outp); return outp


mods = [('n1.html', 'N1'), ('n2.html', 'N2'), ('n3.html', 'N3'), ('n4.html', 'N4'), ('n5.html', 'N5'),
        ('n6.html', 'N6'), ('n7.html', 'N7'),
        ('n7-t1.html', 'N7-Topic1-Indications'), ('n7-t2.html', 'N7-Topic2-Insertion'),
        ('n7-t3.html', 'N7-Topic3-Waveforms'), ('n7-t4.html', 'N7-Topic4-CardiacOutput'), ('n8.html', 'N8')]

# The Informed pathway. All seventeen are listed so the file is the roster, but
# build() skips any page that does not exist yet, so running this before a module
# is written is harmless. Added 2026-08-05 with the first Informed slice.
mods += [('i%d.html' % n, 'I%d' % n) for n in range(1, 18)]
if __name__ == '__main__':
    # No args regenerates every module. Pass labels (e.g. "N1 N4") to regenerate just those,
    # so a single reviewed module can be refreshed without overwriting the others.
    import sys
    wanted = {a.upper() for a in sys.argv[1:]}
    missing = []
    for f, l in mods:
        if wanted and l.upper() not in wanted: continue
        if not os.path.exists(os.path.join(WP, f)):
            missing.append(l); continue
        print('made', build(f, l))
    if missing:
        print('skipped, page not built yet: ' + ', '.join(missing))
