# -*- coding: utf-8 -*-
# Draw the two patient illustrations for Module C2 (i2.html) as hand-written SVG.
# Neal asked for SVGs in place of the AI-image placeholders (C2 review, 2026-11-05).
#
#   python3 make_i2_patient_figures.py
#
# Writes img/i2-opening-patient.svg and img/i2-two-patients.svg into the web repo.
import os
import sys

WEB = '/Users/chaissn/Claude/hemosim-web/img'
FONT = '-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif'
NAVY, MUTED, LINE = '#1f3a5f', '#5a626b', '#8d949c'
SKIN, SKIN_EDGE, MOTTLE = '#e9c4a6', '#b98d6d', '#7d4e8c'
SHEET, BLANKET, BLANKET_EDGE = '#f4f6f8', '#9fb3c8', '#6f86a0'


def ecg(x0, y0, width, beats):
    """A tachycardic sinus trace: flat baseline, P, QRS, T, repeated."""
    step = width / beats
    pts = []
    for b in range(beats):
        x = x0 + b * step
        s = step / 30.0
        seq = [(0, 0), (3, 0), (4, -2), (5, 0), (8, 0), (9, 2), (10, -15), (11, 5), (12, 0),
               (16, 0), (18, -4), (20, 0), (30, 0)]
        pts += ['%.1f,%.1f' % (x + dx * s, y0 + dy) for dx, dy in seq]
    return '<polyline points="%s" fill="none" stroke="#3ddc84" stroke-width="1.4"/>' % ' '.join(pts)


def mottling(cx, cy):
    """Reticular violaceous patches over the patella."""
    out = []
    blots = [(-9, -3, 4, 2.4), (-3, -5, 3.2, 2), (4, -3, 4.2, 2.6), (10, -4, 3, 1.8),
             (-6, 2, 3.4, 2), (1, 1, 4.4, 2.2), (8, 2, 3.2, 1.8), (-12, 0, 2.4, 1.6)]
    for dx, dy, rx, ry in blots:
        out.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" fill-opacity="0.55"/>'
                   % (cx + dx, cy + dy, rx, ry, MOTTLE))
    out.append('<path d="M%.1f %.1f q4 -4 8 0 t8 0 t8 0" fill="none" stroke="%s" stroke-width="0.9" '
               'stroke-opacity="0.7"/>' % (cx - 12, cy - 1, MOTTLE))
    return ''.join(out)


def abp_trace(x0, base, beats, pp):
    """Arterial pressure trace whose height is scaled to the pulse pressure, so a
    wide and a narrow pulse pressure look different on the two monitors."""
    h = pp * 0.3                      # 70 mmHg draws about 21 px, 26 mmHg about 8 px
    d = 'M%.1f %.1f' % (x0, base)
    for b in range(beats):
        x = x0 + b * 30
        d += (' C%.1f %.1f %.1f %.1f %.1f %.1f' % (x + 3, base - h, x + 6, base - h, x + 9, base - 0.72 * h) +
              ' L%.1f %.1f' % (x + 11, base - 0.6 * h) +
              ' C%.1f %.1f %.1f %.1f %.1f %.1f' % (x + 18, base - 0.45 * h, x + 25, base - 0.1 * h, x + 30, base))
    return '<path d="%s" fill="none" stroke="#ff5c5c" stroke-width="1.3"/>' % d


def scene(ox, oy, hr, abp, label, sub, long_hair=False):
    sys_, dia = (int(v) for v in abp.split()[0].split('/'))
    pp = sys_ - dia
    g = ['<g transform="translate(%d,%d)">' % (ox, oy)]
    # floor
    g.append('<line x1="0" y1="232" x2="340" y2="232" stroke="%s" stroke-width="1"/>' % LINE)
    # monitor on a pole at the head of the bed
    g.append('<line x1="62" y1="96" x2="62" y2="232" stroke="%s" stroke-width="3"/>' % LINE)
    g.append('<line x1="44" y1="232" x2="80" y2="232" stroke="%s" stroke-width="4"/>' % LINE)
    g.append('<rect x="4" y="6" width="128" height="92" rx="7" fill="#2a2f36"/>')
    g.append('<rect x="10" y="12" width="116" height="80" rx="3" fill="#0d1117"/>')
    g.append(ecg(14, 34, 70, 4))
    g.append('<text x="90" y="30" font-size="9" fill="#3ddc84">HR</text>')
    g.append('<text x="122" y="44" font-size="17" font-weight="700" fill="#3ddc84" text-anchor="end">%s</text>' % hr)
    g.append(abp_trace(14, 66, 2, pp))
    g.append('<text x="90" y="58" font-size="9" fill="#ff5c5c">ABP</text>')
    g.append('<text x="122" y="86" font-size="13" font-weight="700" fill="#ff5c5c" text-anchor="end">%s</text>' % abp)
    # bed: frame, legs, mattress, raised backrest
    g.append('<rect x="96" y="186" width="232" height="8" rx="2" fill="#b7bec6"/>')
    for x in (108, 312):
        g.append('<line x1="%d" y1="194" x2="%d" y2="226" stroke="#b7bec6" stroke-width="4"/>' % (x, x))
        g.append('<circle cx="%d" cy="228" r="4" fill="#8d949c"/>' % x)
    g.append('<rect x="150" y="170" width="176" height="17" rx="4" fill="%s" stroke="#c9d0d7"/>' % SHEET)
    g.append('<polygon points="150,170 150,187 106,187 98,128 112,124" fill="%s" stroke="#c9d0d7"/>' % SHEET)
    # pillow and head
    g.append('<ellipse cx="114" cy="124" rx="13" ry="7" transform="rotate(-62 114 124)" fill="#ffffff" stroke="#c9d0d7"/>')
    g.append('<circle cx="124" cy="116" r="12" fill="%s" stroke="%s"/>' % (SKIN, SKIN_EDGE))
    if long_hair:
        g.append('<path d="M113 112 q2 -14 14 -12 q8 2 9 8 q-8 -4 -14 0 q-4 6 -2 22 q-8 -4 -7 -18z" fill="#6b5a4e"/>')
    else:
        g.append('<path d="M113 112 q2 -13 13 -12 q9 1 10 8 q-9 -4 -16 -1 q-4 2 -7 5z" fill="#8a8580"/>')
    # torso under the blanket, from the shoulders to mid-thigh
    g.append('<path d="M118 134 q8 -6 20 -2 l38 32 l70 2 q8 1 8 9 l-2 3 l-126 0 q-8 -2 -12 -18 z" '
             'fill="%s" stroke="%s"/>' % (BLANKET, BLANKET_EDGE))
    # arm resting on the blanket
    g.append('<path d="M140 140 q16 14 34 20 q6 2 10 0" fill="none" stroke="%s" stroke-width="7" stroke-linecap="round"/>' % SKIN)
    # exposed lower legs, knees, feet
    g.append('<path d="M252 160 l58 2 q6 0 6 6 l0 2 l-64 1 z" fill="%s" stroke="%s"/>' % (SKIN, SKIN_EDGE))
    g.append('<path d="M310 162 q4 -16 10 -14 q3 2 1 16 z" fill="%s" stroke="%s"/>' % (SKIN, SKIN_EDGE))
    g.append(mottling(268, 163))
    g.append('<line x1="268" y1="150" x2="268" y2="140" stroke="%s" stroke-width="0.8"/>' % MUTED)
    g.append('<text x="268" y="136" font-size="10" fill="%s" text-anchor="middle">mottled knees</text>' % MUTED)
    # labels
    g.append('<text x="170" y="252" font-size="13.5" font-weight="700" fill="%s" text-anchor="middle">%s</text>' % (NAVY, label))
    g.append('<text x="170" y="268" font-size="11.5" fill="%s" text-anchor="middle">%s</text>' % (MUTED, sub))
    g.append('</g>')
    return ''.join(g)


def svg(w, h, body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="%s">'
            '<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>%s</svg>\n' % (w, h, w, h, FONT, w, h, body))


def main():
    one = scene(10, 8, '118', '112/52 (72)', '61-year-old man, pyelonephritis',
                'after 2 L of crystalloid, no vasopressor')
    open(os.path.join(WEB, 'i2-opening-patient.svg'), 'w').write(svg(360, 288, one))
    a = scene(10, 8, '128', '118/48 (71)', 'A. 68-year-old woman', 'pneumonia, treated hypertension',
              long_hair=True)
    b = scene(360, 8, '112', '104/78 (87)', 'B. 58-year-old man', 'pneumonia, previously well')
    open(os.path.join(WEB, 'i2-two-patients.svg'), 'w').write(svg(710, 288, a + b))
    print('wrote i2-opening-patient.svg and i2-two-patients.svg')


if __name__ == '__main__':
    main()
