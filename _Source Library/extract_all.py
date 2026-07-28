# -*- coding: utf-8 -*-
"""HemoSim full source extraction.

For every source .pptx: slide text + SPEAKER NOTES + per-slide images (deduped).
For every source .docx: full paragraph text.
Writes a durable Source Library into the project folder.
"""
import zipfile, re, os, hashlib, posixpath, json
from xml.etree import ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

BASE = '/Users/chaissn/Library/CloudStorage/GoogleDrive-neal.chaisson@gmail.com/My Drive/Claude/CCM/Fellowship/Hemosim'
LIB = os.path.join(BASE, '_Source Library')
DECKS = os.path.join(LIB, 'decks')
DOCS = os.path.join(LIB, 'docs')
IMGS = os.path.join(DECKS, 'images')

# folders that hold OUR deliverables or explicitly-excluded material, not source
SKIP_DIRS = {'_Source Library', 'Module Edit Docs', 'web-pilot', '_Claude Context',
             'Hemosim COntent Outlines for Wix Build',
             'Salient articles for hemodynamics (not for course)'}

MIN_IMG = 8000  # bytes; below this is almost always an icon/bullet/logo


def slug(name):
    s = re.sub(r'\.(pptx|docx)$', '', name, flags=re.I)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-').lower()
    return re.sub(r'-+', '-', s)[:70]


def drawing_text(root):
    return ' '.join(t.text for t in root.iter(A + 't') if t.text and t.text.strip()).strip()


def rels_for(z, part):
    d, b = posixpath.split(part)
    rp = posixpath.join(d, '_rels', b + '.rels')
    out = {}
    if rp in z.namelist():
        try:
            for rel in ET.fromstring(z.read(rp)):
                out[rel.get('Id')] = {'type': rel.get('Type', ''), 'target': rel.get('Target', '')}
        except Exception:
            pass
    return out, d


def extract_pptx(path):
    name = os.path.basename(path)
    sg = slug(name)
    imgdir = os.path.join(IMGS, sg)
    out = ['# %s' % name, '',
           'Source file: `%s`' % os.path.relpath(path, BASE), '',
           'Extracted: slide text + speaker notes + per-slide images.', '', '---', '']
    seen = {}
    n_img = 0
    n_notes = 0
    n_slides = 0
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        slides = sorted([n for n in names if re.match(r'ppt/slides/slide\d+\.xml$', n)],
                        key=lambda n: int(re.search(r'slide(\d+)', n).group(1)))
        for sp in slides:
            num = int(re.search(r'slide(\d+)', sp).group(1))
            try:
                root = ET.fromstring(z.read(sp))
            except Exception:
                continue
            body = drawing_text(root)
            rels, basedir = rels_for(z, sp)

            notes = ''
            for r in rels.values():
                if r['type'].endswith('notesSlide'):
                    tgt = posixpath.normpath(posixpath.join(basedir, r['target']))
                    if tgt in names:
                        try:
                            nt = drawing_text(ET.fromstring(z.read(tgt)))
                            nt = re.sub(r'^\s*%d\s+' % num, '', nt).strip()
                            if nt:
                                notes = nt
                        except Exception:
                            pass

            imgs = []
            for r in rels.values():
                if not r['type'].endswith('/image'):
                    continue
                tgt = posixpath.normpath(posixpath.join(basedir, r['target']))
                if tgt not in names:
                    continue
                try:
                    data = z.read(tgt)
                except Exception:
                    continue
                if len(data) < MIN_IMG:
                    continue
                h = hashlib.md5(data).hexdigest()
                if h in seen:
                    imgs.append(seen[h])
                    continue
                ext = os.path.splitext(tgt)[1] or '.png'
                fn = '%s_slide%03d_%s%s' % (sg, num, h[:8], ext)
                os.makedirs(imgdir, exist_ok=True)
                with open(os.path.join(imgdir, fn), 'wb') as f:
                    f.write(data)
                seen[h] = fn
                imgs.append(fn)
                n_img += 1

            if not (body or notes or imgs):
                continue
            n_slides += 1
            out.append('## Slide %d' % num)
            if body:
                out.append('')
                out.append(body)
            if notes:
                n_notes += 1
                out.append('')
                out.append('**SPEAKER NOTES:** ' + notes)
            if imgs:
                out.append('')
                out.append('*Images on this slide:* ' + ', '.join('`%s`' % i for i in imgs))
            out.append('')
    os.makedirs(DECKS, exist_ok=True)
    with open(os.path.join(DECKS, sg + '.md'), 'w') as f:
        f.write('\n'.join(out))
    return {'file': name, 'slug': sg, 'slides': n_slides, 'notes': n_notes, 'images': n_img}


def extract_docx(path):
    name = os.path.basename(path)
    sg = slug(name)
    out = ['# %s' % name, '', 'Source file: `%s`' % os.path.relpath(path, BASE), '', '---', '']
    n_par = 0
    with zipfile.ZipFile(path) as z:
        if 'word/document.xml' not in z.namelist():
            return None
        root = ET.fromstring(z.read('word/document.xml'))
        for p in root.iter(W + 'p'):
            t = ''.join(n.text for n in p.iter(W + 't') if n.text)
            t = t.strip()
            if t:
                out.append(t)
                out.append('')
                n_par += 1
    os.makedirs(DOCS, exist_ok=True)
    with open(os.path.join(DOCS, sg + '.md'), 'w') as f:
        f.write('\n'.join(out))
    return {'file': name, 'slug': sg, 'paragraphs': n_par}


def main():
    ppt_stats, doc_stats = [], []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in files:
            if fn.startswith('~$') or fn.startswith('.'):
                continue
            p = os.path.join(root, fn)
            try:
                if fn.lower().endswith('.pptx'):
                    ppt_stats.append(extract_pptx(p))
                elif fn.lower().endswith('.docx'):
                    r = extract_docx(p)
                    if r:
                        doc_stats.append(r)
            except Exception as e:
                print('ERROR %s: %s' % (fn, e))
    print(json.dumps({'decks': ppt_stats, 'docs': doc_stats}, indent=1))


if __name__ == '__main__':
    main()
