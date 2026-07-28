# -*- coding: utf-8 -*-
"""Bulk-capture the published HemoSim Wix site: fetch each page, extract main text + image URLs."""
import urllib.request, re, os, html as H
from html.parser import HTMLParser

BASE = '/Users/chaissn/Library/CloudStorage/GoogleDrive-neal.chaisson@gmail.com/My Drive/Claude/CCM/Fellowship/Hemosim'
OUT = os.path.join(BASE, '_Source Library', 'wix')
os.makedirs(OUT, exist_ok=True)

SITEMAP = 'https://www.hemosim.org/pages-sitemap.xml'
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
# functional / non-curriculum pages to skip
SKIP = {'', 'blog', 'groups', 'file-share', 'blank', 'blank-1', 'interactive-course'}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8', 'replace')


class MainText(HTMLParser):
    """Extract readable text from within <main>, dropping script/style/svg, keeping headings/paras."""
    def __init__(s):
        super().__init__()
        s.depth_main = 0
        s.skip = 0
        s.parts = []
        s.cur = ''
        s.imgs = []
        s.in_block = False

    def handle_starttag(s, t, attrs):
        a = dict(attrs)
        if t == 'main':
            s.depth_main += 1
        if s.depth_main == 0:
            # still capture images even outside main (Wix wraps oddly), but only wix media
            if t == 'img':
                src = a.get('src', '')
                if 'wixstatic.com' in src or 'media' in src:
                    s.imgs.append(src.split('/v1/')[0] if '/v1/' in src else src)
            return
        if t in ('script', 'style', 'svg', 'noscript'):
            s.skip += 1
        if t == 'img':
            src = a.get('src', '') or a.get('data-src', '')
            alt = a.get('alt', '')
            if src:
                s.imgs.append((src, alt))
        if t in ('h1', 'h2', 'h3', 'h4', 'p', 'li', 'div', 'span'):
            pass

    def handle_endtag(s, t):
        if t in ('script', 'style', 'svg', 'noscript') and s.skip:
            s.skip -= 1
        if t in ('h1', 'h2', 'h3', 'h4', 'p', 'li', 'br', 'div'):
            if s.cur.strip():
                s.parts.append(s.cur.strip())
            s.cur = ''
        if t == 'main' and s.depth_main:
            s.depth_main -= 1

    def handle_data(s, d):
        if s.depth_main > 0 and not s.skip:
            s.cur += d


def clean(parts):
    out = []
    seen = set()
    for p in parts:
        p = re.sub(r'\s+', ' ', p).strip()
        if len(p) < 2:
            continue
        # drop obvious boilerplate
        if p.lower() in ('home', 'menu', 'log in', 'members', 'blog', 'search',
                         'top of page', 'bottom of page', 'previous', 'next'):
            continue
        if p.startswith('©') or 'Powered and secured by Wix' in p:
            continue
        key = p.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


def main():
    sm = fetch(SITEMAP)
    urls = re.findall(r'<loc>([^<]+)</loc>', sm)
    slugs = []
    for u in urls:
        slug = u.rstrip('/').split('/')[-1]
        if slug == 'hemosim.org' or u.rstrip('/') == 'https://www.hemosim.org':
            continue
        if slug in SKIP:
            continue
        slugs.append((slug, u))
    print('capturing %d pages' % len(slugs))
    manifest = []
    for slug, u in sorted(slugs):
        try:
            html = fetch(u)
        except Exception as e:
            print('FAIL', slug, e)
            continue
        title = ''
        m = re.search(r'<title>([^<]*)</title>', html)
        if m:
            title = H.unescape(m.group(1)).replace(' | HemoSim- Practical Hemodynamics', '').strip()
        pr = MainText()
        pr.feed(html)
        parts = clean(pr.parts)
        # image urls (dedup, base form)
        imgs = []
        seenimg = set()
        for it in pr.imgs:
            src = it[0] if isinstance(it, tuple) else it
            if 'wixstatic.com/media' not in src:
                continue
            base = src.split('/v1/')[0]
            if base in seenimg:
                continue
            seenimg.add(base)
            imgs.append(src)
        body = '\n\n'.join(parts)
        doc = ['# %s (Wix published page)' % (title or slug), '',
               'Source: %s (captured 2026-07-22)' % u, '',
               '---', '', body]
        if imgs:
            doc += ['', '## Images referenced', ''] + ['- ' + i for i in imgs[:40]]
        with open(os.path.join(OUT, slug + '.md'), 'w') as f:
            f.write('\n'.join(doc))
        manifest.append((slug, title, len(parts), len(imgs)))
        print('  %-42s %4d blocks  %2d imgs  | %s' % (slug, len(parts), len(imgs), title))
    # write a small capture index
    with open(os.path.join(OUT, '_captured.md'), 'w') as f:
        f.write('# Wix pages captured (2026-07-22)\n\n')
        f.write('| slug | title | text blocks | images |\n|---|---|---|---|\n')
        for slug, title, nb, ni in sorted(manifest):
            f.write('| %s | %s | %d | %d |\n' % (slug, title, nb, ni))
    print('DONE: %d pages captured' % len(manifest))


if __name__ == '__main__':
    main()
