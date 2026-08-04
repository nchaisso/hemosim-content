# -*- coding: utf-8 -*-
# Extract every embedded image from the returned Module Edit Docs and write a
# manifest that says where each one sits in the document.
#
# Usage:
#   python3 extract_edit_doc_images.py            # all labels below
#   python3 extract_edit_doc_images.py N4 N7-T2   # only these
#
# Why this exists: Neal's figure instructions are positional. "[Add the above
# graphic]" and "[I replaced the current figure with a new set of figures]" only
# make sense if you know which image sits where. Unzipping a .docx gives you
# media/image7.png with no idea what it is. This walks paragraphs in reading
# order, resolves each drawing's relationship ID to its media file, and records
# the text immediately before and after it.
#
# Output, per label:
#   edit-doc-images/<LABEL>/img01.png ...   images renumbered in reading order
#   edit-doc-images/<LABEL>/manifest.md     what each one is and what it sits next to
#
# The output folder is derived data and is gitignored; rerun this rather than
# committing it. Written 2026-08-03 for the N1-N8 + topic review pass.

import os, re, sys, zipfile

BASE = '/Users/chaissn/Library/CloudStorage/Dropbox/Claude/CCM/Fellowship/Hemosim'
DOCS = os.path.join(BASE, 'Module Edit Docs')
OUT = os.path.join(BASE, '_Source Library', 'edit-doc-images')

# label -> filename in Module Edit Docs
LABELS = {
    'N1': 'N1 - Edit Doc.docx',
    'N2': 'N2 - Edit Doc.docx',
    'N2-Offshoot': 'N2-Offshoot-BedsideDO2VO2 - Edit Doc.docx',
    'N3': 'N3 - Edit Doc.docx',
    'N4': 'N4 - Edit Doc.docx',
    'N5': 'N5 - Edit Doc.docx',
    'N5-Offshoot': 'N5-Offshoot-RAPVolume - Edit Doc.docx',
    'N6': 'N6 - Edit Doc.docx',
    'N7': 'N7 - Edit Doc.docx',
    'N7-T1': 'N7-Topic1-Indications - Edit Doc.docx',
    'N7-T2': 'N7-Topic2-Insertion - Edit Doc.docx',
    'N7-T3': 'N7-Topic3-Waveforms - Edit Doc.docx',
    'N7-T4': 'N7-Topic4-CardiacOutput - Edit Doc.docx',
    'N8': 'N8 - Edit Doc.docx',
}


def paragraphs(xml):
    return re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)


def text_of(para):
    """Visible text plus deleted text, so context reads the same as the diff."""
    keep = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', para))
    gone = ''.join(re.findall(r'<w:delText[^>]*>([^<]*)</w:delText>', para))
    return (keep + (' {-%s-}' % gone if gone.strip() else '')).strip()


def rels(z):
    """relationship id -> media path inside the zip."""
    try:
        xml = z.read('word/_rels/document.xml.rels').decode('utf8', errors='ignore')
    except KeyError:
        return {}
    out = {}
    for rid, target in re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"', xml):
        if 'media/' in target:
            out[rid] = 'word/' + target.lstrip('/')
    return out


def trim(s, n=220):
    s = ' '.join(s.split())
    return s if len(s) <= n else s[:n] + '...'


def run(label):
    path = os.path.join(DOCS, LABELS[label])
    if not os.path.exists(path):
        print('  SKIP %-12s no such file: %s' % (label, LABELS[label]))
        return
    z = zipfile.ZipFile(path)
    xml = z.read('word/document.xml').decode('utf8', errors='ignore')
    rel = rels(z)
    paras = paragraphs(xml)
    texts = [text_of(p) for p in paras]

    dest = os.path.join(OUT, label)
    os.makedirs(dest, exist_ok=True)
    # Clear previous output first. Images are renumbered in reading order every
    # run, so when Neal adds or removes one the numbering shifts and any stale
    # file left behind is silently wrong. On 2026-08-04 a leftover img01.png in
    # a folder whose document had zero images sent a search down the wrong path.
    for old in os.listdir(dest):
        if old.startswith('img') or old == 'manifest.md':
            os.remove(os.path.join(dest, old))

    rows, seq = [], 0
    for i, para in enumerate(paras):
        # r:embed is the normal case; r:link covers linked-not-embedded images.
        for rid in re.findall(r'r:(?:embed|link)="([^"]+)"', para):
            member = rel.get(rid)
            if not member or member not in z.namelist():
                continue
            seq += 1
            ext = os.path.splitext(member)[1].lower() or '.png'
            name = 'img%02d%s' % (seq, ext)
            with open(os.path.join(dest, name), 'wb') as f:
                f.write(z.read(member))

            # Context: nearest non-empty text before and after this paragraph.
            before = next((texts[j] for j in range(i - 1, -1, -1) if texts[j]), '')
            after = next((texts[j] for j in range(i + 1, len(texts)) if texts[j]), '')
            rows.append({
                'name': name,
                'para': i,
                'bytes': z.getinfo(member).file_size,
                'source': member,
                'self': texts[i],
                'before': before,
                'after': after,
            })

    with open(os.path.join(dest, 'manifest.md'), 'w') as f:
        f.write('# %s embedded images\n\n' % label)
        f.write('Extracted from `%s` in reading order.\n' % LABELS[label])
        f.write('`before` and `after` are the nearest non-empty paragraphs, which is\n')
        f.write('how you resolve a positional instruction like "add the above graphic".\n\n')
        if not rows:
            f.write('No embedded images in this document.\n')
        for r in rows:
            f.write('## %s\n\n' % r['name'])
            f.write('- paragraph %d, %s bytes, was `%s`\n' % (r['para'], format(r['bytes'], ','), r['source']))
            if r['self']:
                f.write('- same paragraph: %s\n' % trim(r['self']))
            f.write('- before: %s\n' % trim(r['before']))
            f.write('- after: %s\n\n' % trim(r['after']))

    print('  %-12s %2d image(s) -> %s' % (label, len(rows), os.path.relpath(dest, BASE)))


if __name__ == '__main__':
    wanted = sys.argv[1:] or list(LABELS)
    bad = [w for w in wanted if w not in LABELS]
    if bad:
        sys.exit('unknown label(s): %s\nknown: %s' % (', '.join(bad), ', '.join(LABELS)))
    os.makedirs(OUT, exist_ok=True)
    print('extracting to %s' % OUT)
    for label in wanted:
        run(label)
