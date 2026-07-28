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


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.blocks = []; s.inmain = False
        s.collect = None; s.buf = ''; s.skip = 0
        s.fig = None; s.grid = None; s.row = None; s.bus = None; s.box = None; s.callout = None

    def handle_starttag(s, t, attrs):
        a = dict(attrs); c = a.get('class', '')
        if t == 'main': s.inmain = True; return
        if not s.inmain: return
        if t == 'br' and s.collect: s.buf += '\n'; return
        if t in ('div', 'p') and ('pager' in c or 'refs' in c or 'eyebrow' in c or 'attrib' in c):
            s.skip += 1; return
        if s.skip: return
        if t == 'h1': s.collect = 'h1'; s.buf = ''
        elif t == 'h2': s.collect = 'h2'; s.buf = ''
        elif t == 'p' and 'closing' in c: s.collect = 'closing'; s.buf = ''
        elif t == 'div' and 'eq' in c.split(): s.collect = 'eq'; s.buf = ''
        elif t == 'div' and 'figframe' in c: s.collect = 'figframe'; s.buf = ''
        elif t == 'figure': s.fig = {'img': None, 'cap': ''}
        elif t == 'img' and s.fig is not None: s.fig['img'] = a.get('src')
        elif t == 'figcaption': s.collect = 'figcap'; s.buf = ''
        elif t == 'div' and 'callout' in c: s.callout = {'txt': '', 'href': None}
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
        b = s.buf.strip()
        if t == 'h1' and s.collect == 'h1': s.blocks.append(('h1', b)); s.collect = None
        elif t == 'h2' and s.collect == 'h2': s.blocks.append(('h2', b)); s.collect = None
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


def build(nfile, label):
    html = open(os.path.join(WP, nfile)).read()
    body = html[html.find('<main'):html.find('</main>') + 7]
    p = P(); p.feed(body)
    d = Document(); d.styles['Normal'].font.name = 'Calibri'; d.styles['Normal'].font.size = Pt(11)
    d.add_heading('HemoSim edit doc - %s' % label, level=0)
    note(d, 'HOW TO USE: edit the wording directly (Track Changes if you like). For layout or a figure (size, position, wrong/missing image) write a short instruction in [brackets] right where it applies. Send it back and I apply the wording to the page and the layout notes to the styling, then regenerate. This is a content+notes doc, so it will not look exactly like the web page.')
    d.add_paragraph()
    for kind, data in p.blocks:
        if kind == 'h1': d.add_heading(data, level=1)
        elif kind == 'h2': d.add_heading(data, level=2)
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
            note(d, '[Layout note: figure shown small here; on the web it is capped at ~520px wide. Say if you want it smaller/larger, moved, cropped, or replaced.]')
        elif kind == 'figframe':
            note(d, '[FIGURE PLACEHOLDER - to import at build: ' + re.sub(r'\s+', ' ', data) + ']', '9A6B00')
        elif kind == 'callout':
            note(d, '[Offshoot / At-the-Bedside link: ' + re.sub(r'\s+', ' ', data.get('txt', '')).strip() + (' (target: ' + data['href'] + ')' if data.get('href') else '') + ']', '9A6B00')
    outp = os.path.join(OUT, '%s - Edit Doc.docx' % label); d.save(outp); return outp


mods = [('n1.html', 'N1'), ('n2.html', 'N2'), ('n3.html', 'N3'), ('n4.html', 'N4'), ('n5.html', 'N5'),
        ('n6.html', 'N6'), ('n7.html', 'N7'),
        ('n7-t1.html', 'N7-Topic1-Indications'), ('n7-t2.html', 'N7-Topic2-Insertion'),
        ('n7-t3.html', 'N7-Topic3-Waveforms'), ('n7-t4.html', 'N7-Topic4-CardiacOutput'), ('n8.html', 'N8')]
if __name__ == '__main__':
    # No args regenerates every module. Pass labels (e.g. "N1 N4") to regenerate just those,
    # so a single reviewed module can be refreshed without overwriting the others.
    import sys
    wanted = {a.upper() for a in sys.argv[1:]}
    for f, l in mods:
        if wanted and l.upper() not in wanted: continue
        print('made', build(f, l))
