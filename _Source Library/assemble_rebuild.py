# -*- coding: utf-8 -*-
"""Assemble the N1-N8 rebuild: copy chosen figures, splice deep body + refs into each page."""
import json, os, re, html, glob, shutil

B = '/Users/chaissn/Library/CloudStorage/GoogleDrive-neal.chaisson@gmail.com/My Drive/Claude/CCM/Fellowship/Hemosim'
LIB = B + '/_Source Library'
WP = B + '/web-pilot'
IMG = WP + '/img'
os.makedirs(IMG, exist_ok=True)
OUT = '/private/tmp/claude-503/-Users-chaissn-Library-CloudStorage-GoogleDrive-neal-chaisson-gmail-com-My-Drive-Claude-CCM-Fellowship-Hemosim/2ec2940c-f953-4a4f-a8e3-0dec7f4afe46/tasks/w2zf3lcue.output'

wrap = json.loads(open(OUT).read())
res = wrap['result']
if isinstance(res, str):
    res = json.loads(res)
mods = res['modules']


def find_image(imgfile, deckslug):
    # try the named folder, else search all image folders
    cand = os.path.join(LIB, 'decks', 'images', deckslug or '', imgfile)
    if os.path.exists(cand):
        return cand
    hits = glob.glob(os.path.join(LIB, 'decks', 'images', '*', imgfile))
    return hits[0] if hits else None


def build_refs(refs):
    if not refs:
        return ''
    lis = ''.join('<li>%s</li>' % r for r in refs)
    return ('<div class="refs"><h4>References</h4><ol>%s</ol>'
            '<div class="attrib">Figures imported from the source decks (slide cited on each caption); '
            'attribution to confirm before publication.</div></div>' % lis)


report = []
for m in mods:
    mid = m['module'].strip()
    fn = mid.lower() + '.html'
    path = os.path.join(WP, fn)
    if not os.path.exists(path):
        report.append('%s: PAGE NOT FOUND (%s)' % (mid, fn)); continue

    body = m['bodyHtml']
    if body.lstrip().startswith('&lt;'):
        body = html.unescape(body)

    # copy figures
    copied, missing = [], []
    for f in m.get('figures', []):
        imgfile = f.get('imgFile', '').strip()
        if not imgfile:
            continue
        srcp = find_image(imgfile, f.get('deckSlug', ''))
        if srcp:
            shutil.copy2(srcp, os.path.join(IMG, imgfile))
            copied.append(imgfile)
        else:
            missing.append(imgfile)

    page = open(path).read()

    # splice body: everything between </h1> and <div class="pager">
    pat_body = re.compile(r'(</h1>).*?(<div class="pager">)', re.DOTALL)
    if not pat_body.search(page):
        report.append('%s: could not find body splice boundaries' % mid); continue
    page = pat_body.sub(lambda mm: mm.group(1) + body + mm.group(2), page, count=1)

    # splice refs: from <div class="refs"> to final </div></main>
    newrefs = build_refs(m.get('refs', []))
    if '<div class="refs">' in page:
        page = re.sub(r'<div class="refs">.*</div></main>',
                      lambda mm: newrefs + '</div></main>', page, count=1, flags=re.DOTALL)
    else:
        # insert before closing wrap/main
        page = page.replace('</div></main>', newrefs + '</div></main>', 1)

    open(path, 'w').write(page)
    report.append('%s: spliced body (%d chars), %d refs, figs copied=%s%s'
                  % (mid, len(body), len(m.get('refs', [])), copied,
                     (' MISSING=' + str(missing)) if missing else ''))

print('\n'.join(report))
print('\nImages now in web-pilot/img:', len(os.listdir(IMG)))
