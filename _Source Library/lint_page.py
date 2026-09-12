# -*- coding: utf-8 -*-
# Lint one site page against the HemoSim writing rules. Usage: python3 lint_page.py i4.html [more.html]
# Written 2026-09-12 for the Informed application pass so every agent runs the same checks.
import html, os, re, sys
WEB = '/Users/chaissn/Claude/hemosim-web'
TERMS = ['Guyton curve', 'Starling curve', 'MSFP', ' Pra ', 'PRA', 'honest', 'coming soon', 'Phsyiology', '{+', '+}', '{-', '-}']
for name in sys.argv[1:]:
    path = name if os.path.isabs(name) else os.path.join(WEB, name)
    s = open(path).read(); problems = []
    for ch, label in (('—', 'em dash'), ('–', 'en dash')):
        if ch in s: problems.append('%s x%d' % (label, s.count(ch)))
    body = s[s.find('<main'):s.find('<div class="refs">')] if '<div class="refs">' in s else s[s.find('<main'):]
    prose = re.sub(r'<small>.*?</small>', '', body, flags=re.S)
    prose = re.sub(r'<!--.*?-->', '', prose, flags=re.S)
    text = html.unescape(re.sub(r'&[A-Za-z]+;|&#\d+;', '', re.sub(r'<[^>]+>', ' ', prose)))
    for m in re.finditer(r';', text):
        problems.append('semicolon: ...%s...' % re.sub(r'\s+', ' ', text[max(0, m.start()-50):m.end()+25]))
    for t in TERMS:
        for m in re.finditer(re.escape(t), text):
            problems.append('term %r: ...%s...' % (t.strip(), re.sub(r'\s+', ' ', text[max(0, m.start()-40):m.end()+30])))
    for m in re.finditer(r'\[(?:link|add:|replace|Layout|IMAGE|make this)[^\]]{0,80}\]', text, re.I):
        problems.append('unresolved bracket: %s' % m.group(0))
    for src in re.findall(r'src="([^"]+)"', s):
        if not src.startswith('http') and not os.path.exists(os.path.join(WEB, src)): problems.append('missing image: ' + src)
    for href in re.findall(r'href="([^"#]+\.html)"', s):
        if not os.path.exists(os.path.join(WEB, href)): problems.append('broken link: ' + href)
    if 'class="attrib"' in s: problems.append('attribution footer present, must be removed')
    if 'style="' in body: problems.append('inline style attribute in body')
    words = len(re.sub(r'<[^>]+>', ' ', body).split())
    print('%s: %d words, %d problems' % (name, words, len(problems)))
    for p in problems: print('   -', p)
