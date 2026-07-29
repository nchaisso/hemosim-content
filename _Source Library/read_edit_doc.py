# -*- coding: utf-8 -*-
# Read a Module Edit Doc and print Neal's review markup.
#
# Usage:
#   python3 read_edit_doc.py N1            # inline view: {+insertions+} and {-deletions-} in context
#   python3 read_edit_doc.py N1 --accepted # the final text with all changes accepted
#
# Written 2026-07-28 during the N1 pass. Kept here rather than in a scratchpad because
# scratchpads are wiped between sessions, which is how build_pilot_v8.py was lost.
#
# Note: Neal's layout and figure instructions are written inline in [square brackets],
# not as Word comments. Older docs have no word/comments.xml at all. Both are handled.

import os, re, sys, zipfile

DOCS = '/Users/chaissn/Library/CloudStorage/Dropbox/Claude/CCM/Fellowship/Hemosim/Module Edit Docs'


def load(label):
    path = os.path.join(DOCS, '%s - Edit Doc.docx' % label)
    if not os.path.exists(path):
        sys.exit('no such edit doc: %s' % path)
    return zipfile.ZipFile(path)


def runs(frag, tag='w:t'):
    return ''.join(re.findall(r'<' + tag + r'[^>]*>([^<]*)</' + tag + '>', frag))


def paragraphs(xml):
    return re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)


def style_of(para):
    m = re.search(r'w:val="(Heading\d|Title)"', para)
    return m.group(1) if m else ''


def inline(para):
    """Render one paragraph with insertions and deletions marked in reading order."""
    out, pos = [], 0
    for m in re.finditer(r'<w:(ins|del) [^>]*>.*?</w:\1>', para, re.S):
        plain = runs(para[pos:m.start()])
        if plain:
            out.append(plain)
        if m.group(1) == 'ins':
            t = runs(m.group(0))
            if t:
                out.append('{+' + t + '+}')
        else:
            t = runs(m.group(0), 'w:delText')
            if t:
                out.append('{-' + t + '-}')
        pos = m.end()
    tail = runs(para[pos:])
    if tail:
        out.append(tail)
    return ''.join(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__ or 'usage: read_edit_doc.py <LABEL> [--accepted]')
    label = sys.argv[1]
    accepted = '--accepted' in sys.argv
    z = load(label)
    xml = z.read('word/document.xml').decode('utf8', errors='ignore')

    if accepted:
        xml = re.sub(r'<w:del [^>]*>.*?</w:del>', '', xml, flags=re.S)

    for i, para in enumerate(paragraphs(xml)):
        text = runs(para) if accepted else inline(para)
        has_img = '<w:drawing' in para or '<w:pict' in para
        if not text.strip() and not has_img:
            continue
        tag = ('[%s]' % style_of(para)) if style_of(para) else ''
        if has_img:
            tag += '[IMAGE]'
        print('--- para %d %s' % (i, tag))
        print(text)
        print()

    if not accepted:
        # Word comments, if this doc has any. Recent docs put notes inline in brackets instead.
        if 'word/comments.xml' in z.namelist():
            c = z.read('word/comments.xml').decode('utf8', errors='ignore')
            found = re.findall(r'<w:comment [^>]*w:author="([^"]*)"[^>]*>(.*?)</w:comment>', c, re.S)
            print('=== WORD COMMENTS: %d ===' % len(found))
            for who, body in found:
                print('  [%s] %s' % (who, runs(body)))
        else:
            print('=== WORD COMMENTS: none in this doc ===')

    # Embedded images, useful when an instruction says "redraw this" or "I used this one".
    media = [n for n in z.namelist() if 'media' in n]
    if media:
        print()
        print('=== EMBEDDED IMAGES: %d (extract with zipfile if an instruction refers to one) ===' % len(media))
        for n in media:
            print('  %s  %s bytes' % (n, format(z.getinfo(n).file_size, ',')))


if __name__ == '__main__':
    main()
