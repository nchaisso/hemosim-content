# -*- coding: utf-8 -*-
# Generic edit-doc reader by path: inline tracked changes (tagged N: for Neal, G: for Gustavo), comments with anchors, images.
import re, sys, zipfile, html

def runs(frag, tag='w:t'):
    return ''.join(html.unescape(t) for t in re.findall(r'<' + tag + r'[^>]*>([^<]*)</' + tag + '>', frag))

def paragraphs(xml):
    return re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)

def style_of(para):
    m = re.search(r'w:val="(Heading\d|Title)"', para)
    return m.group(1) if m else ''

def inline(para, comments):
    out, pos = [], 0
    pat = r'<w:(ins|del) [^>]*>.*?</w:\1>|<w:commentRangeStart w:id="(\d+)"/>|<w:commentRangeEnd w:id="(\d+)"/>'
    for m in re.finditer(pat, para, re.S):
        plain = runs(para[pos:m.start()])
        if plain:
            out.append(plain)
        if m.group(1) in ('ins', 'del'):
            a = re.search(r'w:author="([^"]*)"', m.group(0))
            a = a.group(1) if a else ''
            who = 'N:' if 'neal' in a.lower() else ('G:' if 'gustavo' in a.lower() or 'GG ' in a else '')
            if m.group(1) == 'ins':
                t = runs(m.group(0))
                if t: out.append('{+' + who + t + '+}')
            else:
                t = runs(m.group(0), 'w:delText')
                if t: out.append('{-' + who + t + '-}')
        elif m.group(2):
            out.append('[[C%s>>' % m.group(2))
        elif m.group(3):
            out.append('<<C%s]]' % m.group(3))
        pos = m.end()
    tail = runs(para[pos:])
    if tail: out.append(tail)
    return ''.join(out)

def main():
    path = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'inline'
    z = zipfile.ZipFile(path)
    names = z.namelist()
    xml = z.read('word/document.xml').decode('utf8', errors='ignore')
    comments = {}
    if 'word/comments.xml' in names:
        cx = z.read('word/comments.xml').decode('utf8', errors='ignore')
        for m in re.finditer(r'<w:comment [^>]*w:id="(\d+)"[^>]*>(.*?)</w:comment>', cx, re.S):
            cid = m.group(1)
            author = re.search(r'w:author="([^"]*)"', m.group(0))
            date = re.search(r'w:date="([^"]*)"', m.group(0))
            text = ' / '.join(runs(p) for p in paragraphs(m.group(2)) if runs(p).strip())
            comments[cid] = (author.group(1) if author else '?', date.group(1) if date else '?', text)
    # authors of tracked changes
    authors = {}
    for m in re.finditer(r'<w:(ins|del) [^>]*w:author="([^"]*)"[^>]*w:date="([^"]*)"', xml):
        key = (m.group(1), m.group(2))
        authors.setdefault(key, []).append(m.group(3))
    if mode == 'summary':
        print('FILE:', path)
        print('has comments.xml:', 'word/comments.xml' in names, 'n comments:', len(comments))
        for k, v in sorted(authors.items()):
            print('  %s by %s: %d (dates %s .. %s)' % (k[0], k[1], len(v), min(v), max(v)))
        media = [n for n in names if n.startswith('word/media/')]
        print('media files:', len(media))
        return
    if mode == 'accepted':
        xml = re.sub(r'<w:del [^>]*>.*?</w:del>', '', xml, flags=re.S)
    for i, para in enumerate(paragraphs(xml)):
        text = runs(para) if mode == 'accepted' else inline(para, comments)
        has_img = '<w:drawing' in para or '<w:pict' in para
        if not text.strip() and not has_img:
            continue
        tag = ('[%s]' % style_of(para)) if style_of(para) else ''
        if has_img: tag += '[IMAGE]'
        print('--- para %d %s' % (i, tag))
        print(text)
    if comments:
        print('\n===== COMMENTS =====')
        for cid in sorted(comments, key=int):
            a, d, t = comments[cid]
            print('C%s [%s %s]: %s' % (cid, a, d, t))

main()
