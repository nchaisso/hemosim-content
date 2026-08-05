# -*- coding: utf-8 -*-
# Generate the Informed pathway navigation chrome, and skeleton pages for modules
# that have not been written yet.
#
# The site has no build step, so the stepper is duplicated into every page exactly
# as the Novice one is. That means this script is the only sane way to keep
# seventeen copies of it in step: run it again whenever a module is built, or the
# grouping changes, and it rewrites the chrome on every Informed page in place.
#
# Written 2026-08-04. Lives here rather than in a scratchpad because scratchpads
# are wiped between sessions, which is how build_pilot_v8.py was lost.
#
# Usage:
#   python3 make_informed_shell.py            # rewrite chrome on all built pages
#   python3 make_informed_shell.py --list     # show build state, write nothing

import os, re, sys

WEB = '/Users/chaissn/Claude/hemosim-web'

# Phase groups shown in the stepper. Chosen 2026-08-04 over a single scrolling
# row: seventeen pills do not fit the viewport, and scrolling hides both the
# length of the pathway and which modules exist. Novice keeps the single row,
# where eight steps fit.
GROUPS = [
    ('Foundations', [
        ('I1',  'Foundations',      'i1.html',  'Physiologic foundations'),
        ('I2',  'Phenotype',        None,       'At the bedside: normotensive shock, pulse pressure, and hemodynamic phenotype'),
        ('I3',  'Waveforms',        None,       'Pressure measurement and waveform fundamentals'),
    ]),
    ('The four interfaces', [
        ('I4',  'Interface I',      None,       'Interface I: LV to arterial system'),
        ('I5',  'Interface II',     None,       'Interface II: arterioles to capillaries'),
        ('I6',  'Microcirculation', None,       'Microcirculation and the vascular waterfall'),
        ('I7',  'Interface III',    None,       'Interface III: capillaries to right atrium'),
        ('I8',  'Venous return',    'i8.html',  'Venous return, in depth'),
        ('I9',  'Interface IV',     None,       'Interface IV: RV to LA'),
        ('I10', 'The loop',         None,       'Tying the loop together'),
    ]),
    ('Monitoring and measurement', [
        ('I11', 'Monitoring tools', 'i11.html', 'Hemodynamic monitoring tools'),
        ('I12', 'Heart-lung',       None,       'Heart-lung interactions in arterial pressure monitoring'),
        ('I13', 'SPV and PPV',      None,       'Evaluating arterial systolic and pulse-pressure variation'),
        ('I14', 'CVP waveform',     None,       'Right atrial and CVP waveform interpretation'),
        ('I15', 'PA catheter',      None,       'PA catheter interpretation beyond the Novice basics'),
        ('I16', 'Cardiac output',   None,       'Measuring cardiac output'),
    ]),
    ('Apply', [
        ('I17', 'Apply',            None,       'Apply'),
    ]),
]

FLAT = [m for _, mods in GROUPS for m in mods]


def stepper(current_file):
    rows = []
    for name, mods in GROUPS:
        pills = []
        for code, short, f, _ in mods:
            lab = '%s %s' % (code, short)
            if f and f == current_file:
                pills.append('<a class="step active" href="%s">%s</a>' % (f, lab))
            elif f:
                pills.append('<a class="step" href="%s">%s</a>' % (f, lab))
            else:
                pills.append('<span class="step off">%s</span>' % lab)
        rows.append('<div class="stepgroup"><div class="glabel">%s</div>'
                    '<div class="gsteps">%s</div></div>' % (name, ''.join(pills)))
    return ('<div class="stepper grouped"><div class="wrap">%s</div></div>'
            % ''.join(rows))


def pager(idx):
    """Neighbours that do not exist render disabled and named, never as dead links."""
    def side(i, cls, kind):
        if i < 0 or i >= len(FLAT):
            return ('<span class="pg %s disabled"><div class="k">%s</div>'
                    '<div class="v">&mdash;</div></span>' % (cls, kind))
        code, _, f, title = FLAT[i]
        if f:
            return ('<a class="pg %s" href="%s"><div class="k">%s</div>'
                    '<div class="v">%s</div></a>' % (cls, f, kind, title))
        return ('<span class="pg %s disabled"><div class="k">%s</div>'
                '<div class="v">%s, not built yet</div></span>' % (cls, kind, code))
    if idx == 0:
        prev = ('<a class="pg" href="index.html"><div class="k">Previous</div>'
                '<div class="v">Choose your level</div></a>')
    else:
        prev = side(idx - 1, '', 'Previous')
    return '<div class="pager">%s%s</div>' % (prev, side(idx + 1, 'next', 'Next concept'))


SKELETON = (
    '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>{title} | HemoSim (prototype)</title>'
    '<link rel="stylesheet" href="style.css"></head><body>'
    '<header class="top"><div class="wrap"><div class="brand">HemoSim'
    '<span>Practical Hemodynamics</span></div>'
    '<div class="levelchip informed">Informed pathway</div></div></header>'
    '{stepper}<main><div class="wrap"><p class="eyebrow">Module {code}</p>'
    '<h1>{title}</h1>'
    '<div class="pilotbar"><b>Shell only.</b> The navigation for the Informed '
    'pathway is built; this module\'s content has not been written yet. Informed '
    'modules assume the Novice pathway has been read and go considerably deeper.'
    '</div>{pager}</div></main><div class="ribbon">PROTOTYPE</div></body></html>\n')


def refresh(path, idx, code, title):
    """Rewrite the stepper and pager in place, leaving written content alone."""
    html = open(path).read()
    html = re.sub(r'<div class="stepper[^"]*"><div class="wrap">.*?</div></div>',
                  stepper(FLAT[idx][2]), html, count=1, flags=re.S)
    html = re.sub(r'<div class="pager">.*?</div>\s*</div>\s*</main>',
                  pager(idx) + '</div></main>', html, count=1, flags=re.S)
    open(path, 'w').write(html)


if __name__ == '__main__':
    if '--list' in sys.argv:
        for code, short, f, title in FLAT:
            print('  %-4s %-18s %s' % (code, short, f or 'not built'))
        raise SystemExit

    touched = []
    for i, (code, short, f, title) in enumerate(FLAT):
        if not f:
            continue
        path = os.path.join(WEB, f)
        if os.path.exists(path) and 'Shell only.' not in open(path).read():
            refresh(path, i, code, title)          # written page: chrome only
            touched.append(f + ' (chrome refreshed)')
        else:
            open(path, 'w').write(SKELETON.format(
                title=title, code=code, stepper=stepper(f), pager=pager(i)))
            touched.append(f + ' (skeleton)')
    print('updated: ' + ', '.join(touched))
