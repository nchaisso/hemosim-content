# -*- coding: utf-8 -*-
# Draw the PA catheter pressure tracings for N7 Topics 3 and 4 as SVG.
#
#   python3 make_pac_tracings.py            # writes every figure into hemosim-web/img/
#
# Written 2026-09-12 for the N7-T3 and N7-T4 rewrite. Neal asked for an ECG aligned
# to each chamber tracing (right atrium, right ventricle, pulmonary artery, wedge),
# all formatted the same way, plus one tracing for each concept the Topic 3 question
# bank tests: overwedging, giant v waves, cannon a waves, tricuspid regurgitation,
# catheter whip, end-expiration timing, and the zone 1 or 2 pseudo-wedge. The
# thermodilution washout curves and the indirect calorimetry diagram for Topic 4
# come from the same file so the whole set shares one style.
#
# There is no image generation available, so everything is drawn from equations.
# Every waveform is a list of (time, mmHg) keypoints joined by cosine interpolation,
# which gives rounded peaks and troughs without a spline library. The ECG is a sum
# of Gaussians. Keep the landmark timings shared between the ECG and the pressure
# traces: the alignment is the whole point of the figures.
#
# Style follows img/n7-t2-ra-waveform-ecg.svg: ECG in near-black, pressure in the
# site red, labels in the site navy, systole and diastole shaded.

import math, os, random

OUT = '/Users/chaissn/Claude/hemosim-web/img'
FONT = '-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif'
INK, RED, NAVY, MUTED, LINE, TEAL = '#1a1d21', '#c0392b', '#1f3a5f', '#5a626b', '#e4e1db', '#16706B'
SYS, DIA = '#e6ecf3', '#f2f5f8'

T = 0.85                     # beat period, seconds (about 70 per minute)
QRS_ON, QRS_OFF, T_END, P_PEAK = 0.215, 0.255, 0.52, 0.11


# ---------- waveform maths ----------

def cosinterp(points, dt=0.002):
    """Cosine interpolation between (t, v) keypoints. Returns [(t, v), ...]."""
    out = []
    for (t0, v0), (t1, v1) in zip(points, points[1:]):
        n = max(2, int((t1 - t0) / dt))
        for i in range(n):
            u = i / n
            out.append((t0 + (t1 - t0) * u, v0 + (v1 - v0) * (1 - math.cos(math.pi * u)) / 2))
    out.append(points[-1])
    return out


def periodic(shape, beats, period=T, offset=0.0):
    """Repeat a one-beat keypoint list (fractions of the period) over several beats."""
    pts = []
    for b in range(beats):
        for i, (f, v) in enumerate(shape):
            if b and i == 0:
                continue                      # the first point of a beat is the last of the previous
            pts.append((offset + (b + f) * period, v))
    return cosinterp(pts)


def gauss(t, mu, sig, amp):
    return amp * math.exp(-0.5 * ((t - mu) / sig) ** 2)


def ecg(t, qrs_times, p_times=None):
    """ECG voltage at time t, given the times of each QRS onset (and P waves if dissociated)."""
    v = 0.0
    for q in qrs_times:
        v += gauss(t, q + 0.000, 0.006, -0.06)          # q
        v += gauss(t, q + 0.015, 0.007, 1.00)           # R
        v += gauss(t, q + 0.030, 0.007, -0.18)          # s
        v += gauss(t, q + 0.225, 0.040, 0.24)           # T
    for p in (p_times if p_times is not None else [q - QRS_ON + P_PEAK for q in qrs_times]):
        v += gauss(t, p, 0.028, 0.13)                   # P
    return v


# one-beat shapes, as (fraction of the period, mmHg)
RA = [(0.00, 4.0), (0.10, 4.6), (0.175, 8.2), (0.25, 4.9), (0.31, 6.3), (0.42, 2.4), (0.58, 7.2), (0.71, 2.9), (0.85 / T, 4.0)]
RV = [(0.00, 4.8), (0.19, 6.0), (0.235, 7.0), (0.30, 25.0), (0.40, 26.0), (0.47, 22.5), (0.53, 8.0), (0.59, 2.4), (0.70, 3.4), (0.85 / T, 4.8)]
PA = [(0.00, 11.6), (0.245, 10.0), (0.34, 25.0), (0.45, 20.5), (0.545, 14.0), (0.58, 15.6), (0.85 / T, 11.6)]
WEDGE = [(0.00, 9.0), (0.20, 9.4), (0.29, 12.2), (0.41, 8.4), (0.61, 12.6), (0.75, 7.9), (0.85 / T, 9.0)]
WEDGE_BIG_V = [(0.00, 12.0), (0.20, 12.4), (0.29, 16.0), (0.41, 11.0), (0.61, 34.0), (0.77, 12.0), (0.85 / T, 12.0)]
RA_TR = [(0.00, 7.0), (0.17, 10.0), (0.25, 8.2), (0.31, 9.6), (0.45, 15.5), (0.57, 17.0), (0.72, 4.6), (0.85 / T, 7.0)]

# fix the last fraction: the shapes above use 0.85/T (=1.0) to mean "one full period"
for _s in (RA, RV, PA, WEDGE, WEDGE_BIG_V, RA_TR):
    _s[-1] = (1.0, _s[-1][1])


# ---------- SVG helpers ----------

def wrap(text, width=104):
    """Greedy word wrap. Notes under a figure must not run past the 700px canvas."""
    words, lines, cur = text.split(), [], ''
    for w in words:
        if len(cur) + len(w) + 1 > width and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    return lines


class Fig:
    def __init__(self, w, h, title, desc, comment=''):
        self.w, self.h, self.parts = w, h, []
        self.title, self.desc, self.comment = title, desc, comment

    def notes(self, x, y, lines, size=11.5, fill='#4a5568', lead=15, width=104):
        """Wrapped explanatory lines under a figure. Grows the canvas if they run past it."""
        for para in lines:
            for ln in wrap(para, width):
                self.text(x, y, ln, size, fill); y += lead
            y += 3
        self.h = max(self.h, int(y + 6))
        return y

    def add(self, s):
        self.parts.append('    ' + s + '\n')

    def text(self, x, y, s, size=13, fill=INK, anchor='start', weight='normal', style=''):
        self.add('<text x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s" font-weight="%s"%s>%s</text>'
                 % (x, y, size, fill, anchor, weight, (' font-style="%s"' % style) if style else '', esc(s)))

    def path(self, pts, stroke, width=2.2, dash=''):
        d = 'M' + ' L'.join('%.1f %.1f' % p for p in pts)
        self.add('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s/>'
                 % (d, stroke, width, (' stroke-dasharray="%s"' % dash) if dash else ''))

    def line(self, x1, y1, x2, y2, stroke=MUTED, width=1, dash=''):
        self.add('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s/>'
                 % (x1, y1, x2, y2, stroke, width, (' stroke-dasharray="%s"' % dash) if dash else ''))

    def rect(self, x, y, w, h, fill, stroke='none', rx=0, opacity=1.0):
        self.add('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" rx="%s"%s/>'
                 % (x, y, w, h, fill, stroke, rx, (' opacity="%s"' % opacity) if opacity < 1 else ''))

    def dot(self, x, y, r=4, fill=TEAL):
        self.add('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s"/>' % (x, y, r, fill))

    def save(self, name):
        head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" '
                'aria-labelledby="t d">\n  <title id="t">%s</title>\n  <desc id="d">%s</desc>\n' % (self.w, self.h, self.w, self.h, esc(self.title), esc(self.desc)))
        if self.comment:
            head += '  <!-- %s -->\n' % self.comment
        head += '  <rect width="%d" height="%d" fill="#ffffff"/>\n' % (self.w, self.h)
        head += '  <g font-family="%s" font-size="13" fill="%s">\n' % (FONT, INK)
        s = head + ''.join(self.parts) + '  </g>\n</svg>\n'
        with open(os.path.join(OUT, name), 'w') as f:
            f.write(s)
        print('wrote', name)


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Panel:
    """A strip chart: x is time, with an optional ECG lane above a pressure lane."""

    def __init__(self, fig, x0, x1, t0, t1, ecg_y=None, ecg_h=48, p_top=None, p_bot=None, pmax=30, pmin=0):
        self.f, self.x0, self.x1, self.t0, self.t1 = fig, x0, x1, t0, t1
        self.ecg_y, self.ecg_h, self.p_top, self.p_bot, self.pmax, self.pmin = ecg_y, ecg_h, p_top, p_bot, pmax, pmin

    def X(self, t):
        return self.x0 + (t - self.t0) / (self.t1 - self.t0) * (self.x1 - self.x0)

    def Y(self, v):
        return self.p_bot - (v - self.pmin) / (self.pmax - self.pmin) * (self.p_bot - self.p_top)

    def axis(self, ticks, label='mmHg'):
        self.f.line(self.x0, self.p_top, self.x0, self.p_bot, MUTED, 1)
        for v in ticks:
            self.f.line(self.x0 - 4, self.Y(v), self.x0, self.Y(v), MUTED, 1)
            self.f.line(self.x0, self.Y(v), self.x1, self.Y(v), LINE, 0.6)
            self.f.text(self.x0 - 8, self.Y(v) + 4, str(v), 11, MUTED, 'end')
        self.f.text(self.x0 - 30, self.p_top - 8, label, 11, MUTED)

    def bands(self, qrs_times, label=True):
        """Shade ventricular systole (QRS onset to end of T) and diastole."""
        for i, q in enumerate(qrs_times):
            s0, s1 = self.X(q), self.X(q + (T_END - QRS_ON))
            d1 = self.X(qrs_times[i + 1]) if i + 1 < len(qrs_times) else self.X(self.t1)
            top = self.ecg_y - self.ecg_h if self.ecg_y else self.p_top
            self.f.rect(s0, top, s1 - s0, self.p_bot - top, SYS)
            self.f.rect(s1, top, max(0, d1 - s1), self.p_bot - top, DIA)
            if label and i == 0:
                self.f.text((s0 + s1) / 2, top + 13, 'Ventricular systole', 11, NAVY, 'middle')
                self.f.text((s1 + d1) / 2, top + 13, 'Diastole', 11, NAVY, 'middle')

    def draw_ecg(self, qrs_times, p_times=None, label=True, dt=0.002):
        pts = []
        t = self.t0
        while t <= self.t1:
            pts.append((self.X(t), self.ecg_y - ecg(t, qrs_times, p_times) * self.ecg_h * 0.9))
            t += dt
        self.f.path(pts, INK, 1.5)
        if label:
            self.f.text(self.x0 - 8, self.ecg_y + 4, 'ECG', 12, NAVY, 'end', 'bold')

    def ecg_labels(self, q):
        y = self.ecg_y - self.ecg_h * 0.9 - 4
        self.f.text(self.X(q - QRS_ON + P_PEAK), self.ecg_y - 14, 'P', 11, MUTED, 'middle')
        self.f.text(self.X(q + 0.015), y, 'R', 11, MUTED, 'middle')
        self.f.text(self.X(q + 0.225), self.ecg_y - 26, 'T', 11, MUTED, 'middle')

    def draw_pressure(self, series, stroke=RED, width=2.2, dash=''):
        self.f.path([(self.X(t), self.Y(v)) for t, v in series if self.t0 <= t <= self.t1], stroke, width, dash)

    def vline(self, t, y0=None, y1=None, stroke=NAVY, dash='3 3'):
        self.f.line(self.X(t), y0 if y0 is not None else self.ecg_y - self.ecg_h, self.X(t), y1 if y1 is not None else self.p_bot, stroke, 1, dash)

    def mark(self, t, v, s, dx=0, dy=-8, size=12, fill=NAVY, anchor='middle', weight='bold'):
        self.f.text(self.X(t) + dx, self.Y(v) + dy, s, size, fill, anchor, weight)


def chamber_figure(name, title, desc, shape, pmax, lane_label, marks, notes, vlines=(), footer=None, comment=''):
    """The standard one-chamber figure: ECG on top, three beats of the pressure below."""
    fig = Fig(700, 330, title, desc, comment)
    beats, q = 3, [QRS_ON + b * T for b in range(3)]
    p = Panel(fig, 70, 680, 0.0, 3 * T, ecg_y=84, ecg_h=48, p_top=118, p_bot=258, pmax=pmax)
    p.bands(q)
    p.draw_ecg(q)
    p.ecg_labels(q[1])
    p.axis(list(range(0, pmax + 1, 10 if pmax > 15 else 5)))
    p.draw_pressure(periodic(shape, beats))
    fig.text(22, p.Y(pmax / 2) + 4, lane_label, 12, NAVY, 'start', 'bold')
    for t in vlines:
        p.vline(t)
    for m in marks:
        p.mark(*m[:3], **m[3])
    y = fig.notes(70, 284, notes)
    if footer:
        fig.text(70, y + 4, footer, 11, MUTED, 'start', 'normal', 'italic'); fig.h = max(fig.h, int(y + 14))
    fig.save(name)


# ---------- Topic 3: the four chamber tracings ----------

def fig_ra():
    q = QRS_ON + T
    chamber_figure(
        'n7-t3-ra-ecg.svg',
        'Right atrial pressure tracing aligned with the ECG',
        'A right atrial pressure tracing beneath a simultaneous ECG over three beats. The a wave rises after the P wave and peaks inside the PR interval. The trace then falls to the z point at the end of the QRS, immediately before the c wave, which is the small bump as the tricuspid valve closes and bulges into the atrium. The x descent follows through ventricular systole, the v wave builds after the T wave as the atrium fills against the closed valve, and the y descent follows tricuspid opening in early diastole. Two dashed lines drop from the ECG: one from the end of the PR interval to the a wave, one from the end of the QRS to the z point.',
        RA, 15, 'RA',
        [(T + 0.175, 8.2, 'a', {}), (T + 0.31, 6.3, 'c', {}), (T + 0.42, 2.4, 'x', {'dy': 16}), (T + 0.58, 7.2, 'v', {}), (T + 0.71, 2.9, 'y', {'dy': 16}),
         (T + 0.25, 4.9, 'z', {'dx': 9, 'dy': 14, 'fill': TEAL})],
        ['a, atrial contraction, after the P wave  |  c, the closing tricuspid valve bulging into the atrium, at the end of the QRS  |  x, atrial relaxation and descent of the valve plane',
         'v, filling against a closed tricuspid valve, after the T wave  |  y, early diastolic emptying once the valve opens',
         'z, the trough between a and c at the end of the QRS. Right atrial and right ventricular pressure are equal here, so this is the most precise place to read the RAP.'],
        vlines=(T + 0.175, T + 0.255),
        comment='Drop lines: end of the PR interval to the a wave, end of the QRS to the z point. Values are illustrative, normal range 2 to 6 mmHg.')
    # extra: dot on the z point and the a-wave peak
    fig = None


def fig_rv():
    chamber_figure(
        'n7-t3-rv-ecg.svg',
        'Right ventricular pressure tracing aligned with the ECG',
        'A right ventricular pressure tracing beneath a simultaneous ECG over three beats. Pressure rises steeply just after the QRS to a rounded systolic peak near 25 mmHg, falls steeply after the T wave to an early diastolic minimum near 2 mmHg, then climbs slowly through diastole as the ventricle fills, with a small upward step from atrial contraction just before the next QRS. There is no dicrotic notch. Systolic pressure is read at the peak, and end-diastolic pressure at the R wave.',
        RV, 30, 'RV',
        [(T + 0.40, 26.0, 'systolic peak, just after the QRS', {'dy': -10, 'size': 11}), (T + 0.59, 2.4, 'early diastolic minimum', {'dy': 16, 'size': 11, 'dx': 30}),
         (T + 0.235, 7.0, 'end-diastole, at the R wave', {'dy': -14, 'size': 11, 'dx': -6, 'anchor': 'end'}),
         (T + 0.85 - 0.06, 5.6, 'slow filling', {'dy': -10, 'size': 11, 'anchor': 'end', 'fill': MUTED, 'weight': 'normal'})],
        ['Read systolic pressure at the peak, which follows the QRS, and end-diastolic pressure at the R wave, not at the lowest point of the trace.',
         'Pressure is still rising at the end of diastole because the ventricle is filling. That rising tail, and the absence of a dicrotic notch, separate this trace from the pulmonary artery.',
         'Normal range 15 to 25 mmHg systolic, 2 to 6 mmHg diastolic.'],
        vlines=(T + 0.23,),
        comment='The RV trace is drawn with a genuinely rising end-diastolic segment because that is the discriminator against the PA trace taught in the text.')


def fig_pa():
    chamber_figure(
        'n7-t3-pa-ecg.svg',
        'Pulmonary artery pressure tracing aligned with the ECG',
        'A pulmonary artery pressure tracing beneath a simultaneous ECG over three beats. Pressure rises steeply after the QRS to a systolic peak near 25 mmHg that sits within the T wave, falls with a dicrotic notch just after the T wave as the pulmonic valve closes, then runs off gradually through diastole to an end-diastolic pressure near 10 mmHg at the end of the next QRS. The diastolic pressure is higher than in the right ventricle and the trace is still falling, not rising, when the next QRS arrives.',
        PA, 30, 'PA',
        [(T + 0.34, 25.0, 'systolic peak, within the T wave', {'dy': -10, 'size': 11}), (T + 0.56, 15.6, 'dicrotic notch, pulmonic valve closure', {'dy': -12, 'size': 11, 'dx': 44}),
         (T + 0.85 - 0.05, 12.0, 'diastolic runoff, still falling', {'dy': 24, 'size': 11, 'anchor': 'end', 'fill': MUTED, 'weight': 'normal'}),
         (2 * T + 0.245, 10.0, 'end-diastole, end of the QRS', {'dy': 26, 'size': 11, 'dx': 6, 'anchor': 'start'})],
        ['Three things change on crossing the pulmonic valve: the diastolic pressure steps up, a dicrotic notch appears on the downslope, and the diastolic segment runs downhill to the next QRS.',
         'Read systolic pressure at the peak within the T wave and end-diastolic pressure at the end of the QRS.',
         'Normal range 15 to 25 mmHg systolic, 8 to 15 mmHg diastolic, mean 10 to 20 mmHg.'],
        vlines=(2 * T + 0.255,),
        comment='The dicrotic notch is placed just after the end of the T wave. The runoff slope is exaggerated slightly so the downhill end-diastole reads at figure size.')


def fig_wedge():
    chamber_figure(
        'n7-t3-wedge-ecg.svg',
        'Pulmonary artery wedge pressure tracing aligned with the ECG',
        'A wedge pressure tracing beneath a simultaneous ECG over three beats. It looks like a damped atrial tracing with two peaks per beat. The a wave peaks at the end of the QRS, later than the right atrial a wave, because the left atrial pressure wave has to travel back through the pulmonary veins and capillaries to reach the catheter. The v wave peaks after the T wave. There is no c wave, and the whole trace has a smaller amplitude than the right atrial tracing. A dashed line drops from the end of the QRS to the a wave.',
        WEDGE, 20, 'Wedge',
        [(T + 0.29, 12.2, 'a', {}), (T + 0.61, 12.6, 'v', {}), (T + 0.41, 8.4, 'x', {'dy': 16}), (T + 0.75, 7.9, 'y', {'dy': 16})],
        ['Two peaks per beat, no c wave, and a smaller amplitude than the right atrial tracing: the c wave and the fine detail are damped out on the way back through the capillaries.',
         'The a wave sits at the end of the QRS rather than inside the PR interval, delayed by the distance the left atrial pressure wave has to travel to reach the catheter.',
         'Read at the peak of the a wave at end-expiration. Normal range 6 to 12 mmHg.'],
        vlines=(T + 0.29,),
        comment='The a wave is deliberately placed at the end of the QRS: Topic 3 questions 15 and 20 test exactly this delay against the RA tracing.')


def fig_ra_vs_wedge():
    fig = Fig(700, 360,
              'Right atrial and wedge a waves against the same ECG',
              'One ECG with a right atrial tracing and a wedge tracing drawn beneath it over two beats. Dashed lines drop from the end of the PR interval and from the end of the QRS. The right atrial a wave peaks on the first line, inside the PR interval. The wedge a wave peaks on the second line, at the end of the QRS. Both a waves are the same atrial contraction. The wedge version arrives later because the pressure wave travels back from the left atrium through the pulmonary veins and capillaries before the catheter sees it.',
              'The two traces share a time axis so the delay is visible as a horizontal offset rather than described in words.')
    q = [QRS_ON + b * T for b in range(2)]
    top = Panel(fig, 90, 680, 0.0, 2 * T, ecg_y=78, ecg_h=44, p_top=104, p_bot=194, pmax=15)
    bot = Panel(fig, 90, 680, 0.0, 2 * T, ecg_y=None, p_top=214, p_bot=304, pmax=20)
    for pnl in (top, bot):
        for i, qq in enumerate(q):
            s0, s1 = pnl.X(qq), pnl.X(qq + (T_END - QRS_ON))
            d1 = pnl.X(q[i + 1]) if i + 1 < len(q) else pnl.X(pnl.t1)
            t0 = (top.ecg_y - top.ecg_h) if pnl is top else pnl.p_top
            fig.rect(s0, t0, s1 - s0, pnl.p_bot - t0, SYS); fig.rect(s1, t0, max(0, d1 - s1), pnl.p_bot - t0, DIA)
    top.draw_ecg(q); top.ecg_labels(q[0]); top.ecg_labels(q[1])
    top.axis([0, 5, 10, 15]); bot.axis([0, 10, 20])
    top.draw_pressure(periodic(RA, 2)); bot.draw_pressure(periodic(WEDGE, 2))
    fig.text(22, top.Y(7.5) + 4, 'RA', 12, NAVY, 'start', 'bold'); fig.text(22, bot.Y(10) + 4, 'Wedge', 12, NAVY, 'start', 'bold')
    for b in range(2):
        fig.line(top.X(b * T + 0.175), top.ecg_y - top.ecg_h, top.X(b * T + 0.175), bot.p_bot, TEAL, 1, '3 3')
        fig.line(top.X(b * T + 0.29), top.ecg_y - top.ecg_h, top.X(b * T + 0.29), bot.p_bot, NAVY, 1, '3 3')
        top.mark(b * T + 0.175, 8.2, 'a', dx=-8, fill=TEAL); bot.mark(b * T + 0.29, 12.2, 'a', dx=8)
        top.mark(b * T + 0.58, 7.2, 'v', fill=MUTED, weight='normal'); bot.mark(b * T + 0.61, 12.6, 'v', fill=MUTED, weight='normal')
    fig.text(90, 330, 'RA a wave: inside the PR interval, before the QRS.', 11.5, TEAL, 'start', 'bold')
    fig.text(90, 347, 'Wedge a wave: at the end of the QRS, delayed by the trip back from the left atrium. Same contraction, later arrival.', 11.5, NAVY, 'start', 'bold')
    fig.save('n7-t3-ra-vs-wedge-timing.svg')


def fig_rv_vs_pa():
    fig = Fig(700, 380,
              'Right ventricular and pulmonary artery traces: the end of diastole tells them apart',
              'A single ECG with a right ventricular tracing and a pulmonary artery tracing beneath it over two beats. The systolic peaks are the same height. A shaded box covers the last part of diastole before each QRS. Inside the box the right ventricular trace is rising, because the ventricle is filling, and the pulmonary artery trace is falling, because blood is running off into the lungs. The pulmonary artery trace also carries a dicrotic notch and a higher diastolic pressure.',
              'Topic 3 questions 1 and 6. The discriminator is the direction of the trace immediately before the QRS, which survives even when the RV diastolic pressure is high and the notch is ambiguous.')
    q = [QRS_ON + b * T for b in range(2)]
    top = Panel(fig, 90, 680, 0.0, 2 * T, ecg_y=78, ecg_h=44, p_top=104, p_bot=204, pmax=30)
    bot = Panel(fig, 90, 680, 0.0, 2 * T, ecg_y=None, p_top=224, p_bot=324, pmax=30)
    for pnl in (top, bot):
        for b in range(2):
            x0, x1 = pnl.X(b * T + 0.68 + (T - 0.85) ), pnl.X(b * T + QRS_ON + T - T) if False else pnl.X(b * T + 1.0 * T + 0.0)
        # the shaded "last part of diastole" boxes, one before each QRS after the first
    for pnl in (top, bot):
        for b in range(1, 3):
            xa, xb = pnl.X(b * T - 0.20), pnl.X(min(b * T + QRS_ON, 2 * T))
            if xa < pnl.X(2 * T):
                fig.rect(xa, pnl.p_top, xb - xa, pnl.p_bot - pnl.p_top, '#fdf2e6')
    top.draw_ecg(q); top.ecg_labels(q[1])
    top.axis([0, 10, 20, 30]); bot.axis([0, 10, 20, 30])
    top.draw_pressure(periodic(RV, 2)); bot.draw_pressure(periodic(PA, 2))
    fig.text(22, top.Y(15) + 4, 'RV', 12, NAVY, 'start', 'bold'); fig.text(22, bot.Y(15) + 4, 'PA', 12, NAVY, 'start', 'bold')
    top.mark(T - 0.07, 6.8, 'rising into the QRS', dx=-4, dy=-12, size=11, anchor='end')
    bot.mark(T - 0.07, 11.9, 'falling into the QRS', dx=-4, dy=24, size=11, anchor='end')
    bot.mark(T + 0.565, 15.6, 'dicrotic notch', dx=40, dy=-10, size=11, fill=MUTED, weight='normal')
    top.mark(T + 0.59, 2.4, 'no notch, low diastolic', dx=0, dy=16, size=11, fill=MUTED, weight='normal')
    fig.notes(90, 350, ['Same systolic pressure, opposite behaviour at the end of diastole. RV pressure climbs as the chamber fills. PA pressure falls as blood runs off.',
                        'Shaded: the last 200 ms before the QRS. Look there first when a notch is hard to see or the RV diastolic pressure is high.'], width=98)
    fig.save('n7-t3-rv-vs-pa-enddiastole.svg')


# ---------- Topic 3: the gallery ----------

def fig_overwedge():
    fig = Fig(700, 330,
              'Overwedging: a pulmonary artery trace that loses its pulse and keeps climbing',
              'A pulmonary artery pressure tracing over about seven seconds. For the first two seconds it shows normal pulsatile beats with a diastolic pressure near 12 mmHg. At the point marked balloon inflated the pulsations disappear and the trace rises steadily and smoothly to nearly 40 mmHg, well above the pulmonary artery diastolic pressure, with no a or v waves. At the point marked balloon deflated the trace drops back to the pulsatile pulmonary artery pattern.',
              'Topic 3 questions 2 and 16, Topic 2 questions 3 and 8. The rising non-pulsatile line is the continuous flush building pressure behind a tip pinned against the vessel wall.')
    t_inf, t_def = 2.0, 5.3
    p = Panel(fig, 70, 680, 0.0, 7.2, ecg_y=None, p_top=60, p_bot=240, pmax=40)
    p.axis([0, 10, 20, 30, 40])
    fig.line(p.X(0), p.Y(12), p.X(7.2), p.Y(12), NAVY, 1, '5 4'); fig.text(p.X(7.15), p.Y(12) + 14, 'PA diastolic 12 mmHg', 11, NAVY, 'end')
    pre = [(t, v) for t, v in periodic(PA, 3) if t <= t_inf]
    post = [(t + t_def, v) for t, v in periodic(PA, 3) if t + t_def <= 7.2]
    rise = [(t_inf + u * (t_def - t_inf), 14 + (38 - 14) * (u ** 0.85) + 0.6 * math.sin(14 * u)) for u in [i / 200 for i in range(201)]]
    p.draw_pressure(pre); p.draw_pressure(rise); p.draw_pressure(post)
    p.draw_pressure([(t_inf - 0.001, pre[-1][1]), (t_inf, 14)]); p.draw_pressure([(t_def, 38), (t_def + 0.02, post[0][1])])
    fig.rect(p.X(t_inf), 60, p.X(t_def) - p.X(t_inf), 180, '#fdf2e6', opacity=0.7)
    for t, s in ((t_inf, 'balloon inflated'), (t_def, 'balloon deflated')):
        p.vline(t, 48, 240, NAVY, '3 3'); fig.text(p.X(t) + 4, 52, s, 11, NAVY, 'start', 'bold')
    fig.text(p.X(3.6), p.Y(26) - 10, 'no a or v waves, pressure keeps rising', 11.5, RED, 'middle', 'bold')
    fig.notes(70, 268, ['The trace should never be read. Deflate, withdraw the catheter 1 to 2 cm, and re-inflate slowly to the smallest volume that gives a wedge.',
                        'Three signatures: a wedge at a low balloon volume, a value above the PA diastolic pressure, and a line that climbs instead of settling.',
                        'The flush behind the pinned tip is what drives the rise, which is also why a wedged catheter must never be flushed.'])
    fig.save('n7-t3-overwedge.svg')


def fig_big_v():
    fig = Fig(700, 340,
              'A wedge tracing with a giant v wave',
              'An ECG above a wedge pressure tracing over three beats. Each beat shows a modest a wave near 16 mmHg at the end of the QRS and then a tall v wave peaking near 34 mmHg after the T wave, followed by a steep y descent. The v wave is more than 10 mmHg taller than the a wave. There is no dicrotic notch and the trace is rising, not falling, as the next QRS approaches, which is how it is told apart from a pulmonary artery trace of similar height.',
              'Topic 3 questions 7, 8 and 19. The v wave peaks after the T wave; a PA systolic peak sits inside the T wave. Report the a wave, or the trough of the x descent, when the v dominates the mean.')
    q = [QRS_ON + b * T for b in range(3)]
    p = Panel(fig, 70, 680, 0.0, 3 * T, ecg_y=84, ecg_h=48, p_top=118, p_bot=258, pmax=40)
    p.bands(q); p.draw_ecg(q); p.ecg_labels(q[1]); p.axis([0, 10, 20, 30, 40])
    p.draw_pressure(periodic(WEDGE_BIG_V, 3))
    fig.text(22, p.Y(20) + 4, 'Wedge', 12, NAVY, 'start', 'bold')
    p.vline(T + 0.61); p.vline(T + 0.29, stroke=TEAL)
    p.mark(T + 0.29, 16.0, 'a', dx=-8, fill=TEAL); p.mark(T + 0.61, 34.0, 'v', dy=-9); p.mark(T + 0.41, 11.0, 'x', dy=16); p.mark(T + 0.77, 12.0, 'y', dy=16, dx=6)
    fig.text(p.X(T + 0.61) + 8, p.Y(30), 'peaks after the T wave', 11, NAVY)
    fig.notes(70, 284, ['Mean wedge here is near 18 mmHg and the a wave near 16, but the v wave dominates the mean. Haskell and French found the mean overestimates LVEDP by about 30% in this situation.',
                        'Giant v waves are classically acute mitral regurgitation but are neither sensitive nor specific for it: a stiff, small left atrium, a ventricular septal defect, or heart failure can produce them.',
                        'Report the a wave. Say which point you read, because the number changes with the choice.'])
    fig.save('n7-t3-wedge-large-v.svg')


def fig_cannon_a():
    fig = Fig(700, 340,
              'Cannon a waves on a right atrial tracing during atrioventricular dissociation',
              'An ECG in which the P waves march at their own rate, independent of slower, wide QRS complexes, above a right atrial pressure tracing. Most a waves are small. Whenever a P wave falls during ventricular systole the atrium contracts against a closed tricuspid valve and the tracing shows a single very tall a wave, near 22 mmHg, called a cannon a wave. Two such waves are marked. The v waves and y descents between them are normal.',
              'Topic 3 question 5. P times are generated independently of the QRS so the cannon waves land wherever atrial systole meets a closed valve.')
    dur = 4.2
    qrs = [0.25 + i * 1.15 for i in range(4)]
    ps = [0.06 + i * 0.62 for i in range(7)]
    p = Panel(fig, 70, 680, 0.0, dur, ecg_y=84, ecg_h=48, p_top=118, p_bot=258, pmax=25)
    p.bands(qrs, label=False); p.draw_ecg(qrs, ps); p.axis([0, 5, 10, 15, 20, 25])
    # base trace driven by QRS: c, x, v, y
    pts = []
    t = 0.0
    while t <= dur:
        v = 4.0
        for qq in qrs:
            u = t - qq
            v += gauss(u, 0.09, 0.05, 2.2) - gauss(u, 0.20, 0.09, 1.8) + gauss(u, 0.36, 0.08, 3.2) - gauss(u, 0.50, 0.08, 1.4)
        for pp in ps:
            in_sys = any(qq - 0.02 <= pp <= qq + 0.30 for qq in qrs)
            v += gauss(t, pp + 0.07, 0.045, 18.0 if in_sys else 4.0)
        pts.append((t, v)); t += 0.003
    p.draw_pressure(pts)
    fig.text(22, p.Y(12.5) + 4, 'RA', 12, NAVY, 'start', 'bold')
    for pp in ps:
        if any(qq - 0.02 <= pp <= qq + 0.30 for qq in qrs):
            p.mark(pp + 0.07, 22.5, 'cannon a', dy=-8, fill=RED)
        else:
            p.mark(pp + 0.07, 8.3, 'a', dy=-8, fill=MUTED, weight='normal')
    fig.text(p.X(ps[0]), p.ecg_y - 40, 'P waves at their own rate', 11, MUTED)
    fig.notes(70, 284, ['The atrium contracts against a closed tricuspid valve and the whole force of that contraction appears in the atrial pressure. Seen in complete heart block, ventricular tachycardia with dissociation, ventricular pacing, and other rhythms where atrial and ventricular systole coincide.',
                        'Tricuspid stenosis gives tall but regular a waves. Atrial fibrillation abolishes the a wave altogether, and tamponade blunts the y descent rather than raising the a wave.'])
    fig.save('n7-t3-ra-cannon-a.svg')


def fig_tr():
    fig = Fig(700, 340,
              'Right atrial tracing in tricuspid regurgitation',
              'An ECG above a right atrial pressure tracing over three beats. Instead of a small c wave, an x descent and a separate v wave, each beat shows one broad tall wave that begins at the QRS and peaks late in systole near 17 mmHg, followed by a steep y descent. The x descent has disappeared and the c and v waves have fused. The a wave is preserved but small by comparison. The tracing looks like a damped version of a ventricular pressure trace.',
              'Topic 3 question 17. The v wave begins at the QRS because regurgitant flow starts with ventricular contraction, which is what separates it from a normal v wave that builds after the T wave.')
    q = [QRS_ON + b * T for b in range(3)]
    p = Panel(fig, 70, 680, 0.0, 3 * T, ecg_y=84, ecg_h=48, p_top=118, p_bot=258, pmax=20)
    p.bands(q); p.draw_ecg(q); p.ecg_labels(q[1]); p.axis([0, 5, 10, 15, 20])
    p.draw_pressure(periodic(RA_TR, 3))
    fig.text(22, p.Y(10) + 4, 'RA', 12, NAVY, 'start', 'bold')
    p.mark(T + 0.17, 10.0, 'a', dx=-6); p.mark(T + 0.55, 17.0, 'c-v, fused', dy=-9); p.mark(T + 0.72, 4.6, 'y', dy=16)
    p.vline(T + QRS_ON, stroke=TEAL); fig.text(p.X(T + QRS_ON) - 6, p.Y(1.6), 'the wave starts with the QRS', 11, TEAL, 'end')
    fig.text(p.X(T + 0.38), p.Y(6.2), 'no x descent', 11, MUTED, 'middle', 'normal', 'italic')
    fig.notes(70, 284, ['During ventricular systole part of the stroke volume is driven backward through the incompetent valve, so the atrium fills from two directions and its pressure rises through systole rather than falling. The x descent is lost, the c and v waves merge into one systolic wave, and the y descent is steep because the atrium is overfilled.',
                        'A wedge tracing in the same patient can be entirely normal: a giant wedge v wave points to the mitral valve, a giant right atrial v wave to the tricuspid.'])
    fig.save('n7-t3-ra-tr-v.svg')


def fig_whip():
    fig = Fig(700, 300,
              'Catheter whip artifact on a pulmonary artery tracing',
              'An ECG above a pulmonary artery pressure tracing over four beats. The underlying pulmonary artery waveform is visible but is overlaid by rapid, spiky, high-frequency oscillations of several mmHg that are unrelated to the cardiac cycle, giving the trace a fuzzy, jagged look with false peaks and troughs. The systolic and diastolic values cannot be read reliably.',
              'Topic 3 question 12. The oscillations are the tip flicking with each contraction or in high flow, usually because it sits too proximally. Advancing slightly into a more distal, better supported branch usually settles it.')
    random.seed(7)
    q = [QRS_ON + b * T for b in range(4)]
    p = Panel(fig, 70, 680, 0.0, 4 * T, ecg_y=76, ecg_h=44, p_top=100, p_bot=230, pmax=40)
    p.draw_ecg(q); p.axis([0, 10, 20, 30, 40])
    base = periodic(PA, 4, )
    noisy = []
    for t, v in base:
        env = 1.0 + 0.8 * max(0.0, math.sin(2 * math.pi * (t % T) / T))
        noisy.append((t, v + env * (4.5 * math.sin(2 * math.pi * 19 * t) + 2.5 * math.sin(2 * math.pi * 31 * t + 1.1) + random.uniform(-1.6, 1.6))))
    p.draw_pressure(noisy, RED, 1.6)
    fig.text(22, p.Y(20) + 4, 'PA', 12, NAVY, 'start', 'bold')
    fig.notes(70, 256, ['High-frequency spikes riding on the pressure wave, out of step with the ECG: the tip is whipping in the flow, not reading pressure. Do not report the peaks.',
                        'Advance the catheter slightly (balloon inflated, watching for the wedge) so the tip sits in a more distal branch, and re-check the flush test in case the system is underdamped.'])
    fig.save('n7-t3-pa-whip.svg')


def fig_resp():
    fig = Fig(700, 430,
              'Where to read the wedge across the respiratory cycle: spontaneous breathing and positive pressure ventilation',
              'Two panels of a wedge pressure tracing over ten seconds, each with the inspiratory phases shaded. In the upper panel, spontaneous breathing, the tracing dips during each inspiration and end-expiration is the highest plateau of the swing; a marker sits on each end-expiratory beat. In the lower panel, positive pressure ventilation, the tracing rises during each inspiration and end-expiration is the lowest plateau, the valley; markers sit there. Both marked points sit at the same pressure because both are read where pleural pressure has returned toward atmospheric.',
              'Topic 3 questions 10, 11 and 13, and Lindsay module 3 question 2. Vent equals valley. Mirrors the CVP version on I14 so the two pages agree.')
    dur, per, insp = 10.0, 4.0, 1.4
    for k, (label, sign, y0) in enumerate((('Spontaneous breathing', -1, 60), ('Positive pressure ventilation', +1, 240))):
        p = Panel(fig, 70, 680, 0.0, dur, ecg_y=None, p_top=y0 + 22, p_bot=y0 + 142, pmax=30)
        fig.text(70, y0 + 10, label, 13, NAVY, 'start', 'bold')
        for c in range(3):
            t0 = 0.8 + c * per
            fig.rect(p.X(t0), p.p_top, p.X(t0 + insp) - p.X(t0), p.p_bot - p.p_top, '#e6ecf3')
            fig.text(p.X(t0 + insp / 2), p.p_top + 12, 'insp', 10.5, MUTED, 'middle')
        p.axis([0, 10, 20, 30])
        base = periodic(WEDGE, int(dur / T) + 1)
        pts = []
        for t, v in base:
            if t > dur: break
            ph = ((t - 0.8) % per)
            resp = 0.0
            if ph < insp:
                resp = math.sin(math.pi * ph / insp) ** 1.2 * 7.0
            elif ph < insp + 0.5:
                resp = 0.0
            pts.append((t, v + 2 + sign * resp))
        p.draw_pressure(pts)
        for c in range(3):
            te = 0.8 + c * per - 0.35 if c else 0.45
            # the beat closest to end-expiration
            tb = min(pts, key=lambda pv: abs(pv[0] - te))
            fig.dot(p.X(tb[0]), p.Y(tb[1]) - (10 if sign < 0 else -12), 4.5)
        fig.text(p.X(dur) - 4, p.p_bot + 16, 'read at end-expiration: the ' + ('peak' if sign < 0 else 'valley') + ' of the swing', 11.5, TEAL, 'end', 'bold')
        fig.text(22, p.Y(15) + 4, 'Wedge', 12, NAVY, 'start', 'bold')
    fig.notes(70, 412, ['Pleural pressure falls with a spontaneous breath and rises with a delivered one, so the swing moves in opposite directions and the end-expiratory read point moves with it.',
                        'Do not average across the cycle. In a spontaneous patient the average is pulled down by inspiration, and on the ventilator it is pushed up.'])
    fig.save('n7-t3-wedge-respiratory-timing.svg')


def fig_pseudo_wedge():
    fig = Fig(700, 320,
              'A pseudo-wedge from a catheter tip in West zone 1 or 2 on positive pressure ventilation',
              'A wedge pressure tracing over ten seconds in a ventilated patient with the inspiratory phases shaded. The trace is unnaturally smooth with no a or v waves and swings by more than 10 mmHg with each delivered breath, rising during inspiration. A dashed line marks the pulmonary artery diastolic pressure at 14 mmHg; the wedge trace sits above it for most of the cycle. The value tracks airway pressure rather than left atrial pressure.',
              'Topic 3 questions 4 and 18. Compare with the respiratory timing figure: a true zone 3 wedge keeps its a and v waves and swings far less.')
    dur, per, insp = 10.0, 4.0, 1.5
    p = Panel(fig, 70, 680, 0.0, dur, ecg_y=None, p_top=50, p_bot=200, pmax=40)
    for c in range(3):
        t0 = 0.8 + c * per
        fig.rect(p.X(t0), p.p_top, p.X(t0 + insp) - p.X(t0), p.p_bot - p.p_top, '#e6ecf3')
        fig.text(p.X(t0 + insp / 2), p.p_top + 12, 'ventilator breath', 10.5, MUTED, 'middle')
    p.axis([0, 10, 20, 30, 40])
    fig.line(p.X(0), p.Y(14), p.X(dur), p.Y(14), NAVY, 1, '5 4'); fig.text(p.X(0.1), p.Y(14) + 14, 'PA diastolic 14 mmHg', 11, NAVY)
    pts = []
    t = 0.0
    while t <= dur:
        ph = ((t - 0.8) % per)
        resp = math.sin(math.pi * ph / insp) ** 1.1 * 14.0 if ph < insp else 0.0
        pts.append((t, 17.5 + resp + 0.35 * math.sin(2 * math.pi * t / T))); t += 0.01
    p.draw_pressure(pts)
    fig.text(22, p.Y(20) + 4, 'Wedge', 12, NAVY, 'start', 'bold')
    fig.text(p.X(3.55), p.Y(9.5), 'smooth: no a wave, no v wave', 11.5, RED, 'middle', 'bold')
    fig.notes(70, 228, ['Alveolar pressure exceeds pulmonary venous pressure in that region, the capillary is squeezed shut, and the static column no longer reaches the left atrium. The tip is reading lung.',
                        'Clues: loss of a and v waves, an exaggerated respiratory swing, and a wedge above the PA diastolic pressure. High PEEP, diuresis and bleeding all convert zone 3 into zone 2 without the catheter moving.',
                        'Reposition to a dependent branch, or read the PA diastolic pressure instead.'])
    fig.save('n7-t3-zone-pseudo-wedge.svg')


def fig_static_column():
    fig = Fig(700, 330,
              'What the wedge measures: a static column of blood from the balloon to the left atrium',
              'A schematic of a pulmonary artery branch narrowing from left to right into arterioles, capillaries, venules and a pulmonary vein that enters the left atrium. A pulmonary artery catheter enters from the left with its balloon inflated in the branch, blocking forward flow. Beyond the balloon the column of blood is shaded as static, with no flow, all the way to the left atrium. Arrows travel backward along that column from the left atrium to the catheter tip, showing that pressure waves from the atrium reach the catheter through the motionless blood, and then continue up the fluid-filled catheter to the transducer.',
              'Neal asked for the conceptual framework to be explained explicitly: the balloon stops flow, the static column acts as an extension of the catheter, and the transducer reads the left atrial pressure wave that travelled backward through it.')
    # vessel outline: artery on the left tapering to capillaries and widening to the vein on the right
    fig.text(70, 30, 'Pulmonary artery branch', 11.5, NAVY, 'start', 'bold'); fig.text(330, 30, 'Capillaries', 11.5, NAVY, 'middle', 'bold'); fig.text(590, 30, 'Pulmonary vein', 11.5, NAVY, 'middle', 'bold')
    fig.add('<path d="M70 100 C 230 100, 280 140, 330 140 C 380 140, 430 100, 560 100 L 560 200 C 430 200, 380 160, 330 160 C 280 160, 230 200, 70 200 Z" fill="#fbe9e7" stroke="#c0392b" stroke-width="1.5"/>')
    # static column shading beyond the balloon
    fig.add('<path d="M190 104 C 260 108, 290 143, 330 143 C 380 143, 430 104, 556 104 L 556 196 C 430 196, 380 157, 330 157 C 290 157, 260 192, 190 192 Z" fill="#dfe6ee"/>')
    # left atrium
    fig.add('<path d="M560 80 C 640 80, 660 110, 660 150 C 660 190, 640 220, 560 220 Z" fill="#f3d9d6" stroke="#c0392b" stroke-width="1.5"/>')
    fig.text(612, 155, 'Left atrium', 12, NAVY, 'middle', 'bold')
    # catheter and balloon
    fig.rect(40, 143, 150, 14, '#f4f1ea', '#5a626b', 3)
    fig.add('<ellipse cx="190" cy="150" rx="22" ry="44" fill="#fff8e1" stroke="#c9862b" stroke-width="2"/>')
    fig.text(190, 154, 'balloon', 10.5, '#8a5a12', 'middle', 'bold')
    fig.text(42, 218, 'catheter lumen, saline filled, to the transducer', 10.5, MUTED)
    # flow arrows upstream of balloon (blocked)
    fig.add('<path d="M90 120 L 130 120" stroke="#c0392b" stroke-width="2" marker-end="url(#a)"/>')
    fig.add('<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#c0392b"/></marker><marker id="b" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#1f3a5f"/></marker></defs>')
    fig.text(110, 112, 'flow stops here', 10.5, RED, 'middle')
    # backward pressure-wave arrows through the static column
    for x0 in (540, 470, 400, 330, 270):
        fig.add('<path d="M%d 150 L %d 150" stroke="#1f3a5f" stroke-width="2" marker-end="url(#b)"/>' % (x0, x0 - 40))
    fig.text(400, 178, 'no flow: a static column of blood', 11, NAVY, 'middle', 'bold')
    fig.text(400, 122, 'left atrial pressure waves travel backward through it', 11, NAVY, 'middle')
    y = fig.notes(70, 250, ['Inflating the balloon stops flow in that branch. Without flow there is no pressure drop along the vessels beyond the tip, so the pressure at the tip equals the pressure where the column rejoins moving blood, in the pulmonary veins at the left atrium.',
                            'The motionless blood behaves like an extension of the saline inside the catheter: each left atrial pulse pushes on the column, the column pushes on the catheter fluid, and the transducer converts that movement into the wedge tracing.',
                            'Anything that lets the column move, or squeezes it shut, breaks the chain: a leaking balloon, a tip outside zone 3, or a flushed catheter.'])
    fig.text(70, y + 4, 'Right ventricle to the left, left atrium to the right. Not to scale.', 11, MUTED, 'start', 'normal', 'italic'); fig.h = max(fig.h, int(y + 16))
    fig.save('n7-t3-wedge-static-column.svg')


# ---------- Topic 4 ----------

def gamma_curve(a, b, area, t):
    # gamma variate with the requested area under the curve
    g = math.gamma(a + 1) * b ** (a + 1)
    return area / g * t ** a * math.exp(-t / b) if t > 0 else 0.0


def fig_thermodilution():
    fig = Fig(700, 430,
              'Thermodilution washout curves',
              'Two panels plotting the fall in pulmonary artery blood temperature against time after a cold injection. In the upper panel three curves for three cardiac outputs: a high output gives an early, sharp, small curve; a normal output a medium curve; a low output a late, broad, tall curve with a much larger area. The area under the curve is inversely proportional to the flow. In the lower panel a normal curve is compared with the curve produced when only 7 mL is injected although the monitor is set for 10 mL, which is smaller and is reported as a falsely high output, and with the curve of severe tricuspid regurgitation, which is low, prolonged and has a long tail that the monitor may cut off.',
              'Stewart-Hamilton: output = cold delivered divided by the integral of the temperature change. Gamma-variate curves; areas scale as 1/CO in the upper panel.')
    for k, (y0, title) in enumerate(((40, 'Area under the curve falls as cardiac output rises'), (245, 'Same output, different curves: technique and tricuspid regurgitation'))):
        p = Panel(fig, 70, 680, 0.0, 18.0, ecg_y=None, p_top=y0 + 20, p_bot=y0 + 140, pmax=1.0)
        fig.text(70, y0 + 8, title, 13, NAVY, 'start', 'bold')
        fig.line(p.X(0), p.p_bot, p.X(18), p.p_bot, MUTED, 1)
        for s in range(0, 19, 3):
            fig.line(p.X(s), p.p_bot, p.X(s), p.p_bot + 4, MUTED, 1); fig.text(p.X(s), p.p_bot + 16, str(s), 10.5, MUTED, 'middle')
        fig.text(p.X(18), p.p_bot + 30, 'seconds after injection', 11, MUTED, 'end')
        fig.line(p.X(0), p.p_top, p.X(0), p.p_bot, MUTED, 1)
        fig.text(p.X(0) - 6, p.p_top + 6, 'fall in', 10.5, MUTED, 'end'); fig.text(p.X(0) - 6, p.p_top + 18, 'blood', 10.5, MUTED, 'end'); fig.text(p.X(0) - 6, p.p_top + 30, 'temp.', 10.5, MUTED, 'end')
        if k == 0:
            curves = [('high output, 8 L/min', 2.0, 0.9, 0.62, RED, ''), ('normal, 5 L/min', 2.0, 1.5, 1.0, NAVY, ''), ('low output, 2.5 L/min', 2.0, 2.9, 2.0, TEAL, '')]
        else:
            curves = [('10 mL injected, 5 L/min', 2.0, 1.5, 1.0, NAVY, ''), ('7 mL injected, monitor set to 10 mL', 2.0, 1.5, 0.7, RED, '6 4'), ('severe tricuspid regurgitation', 1.3, 4.2, 1.0, TEAL, '')]
        peak_ref = max(gamma_curve(2.0, 1.5, 1.0, t / 100) for t in range(1, 1800))
        for i, (label, a, b, area, col, dash) in enumerate(curves):
            pts = [(t / 100, gamma_curve(a, b, area, t / 100) / peak_ref * 0.85) for t in range(0, 1800, 4)]
            p.draw_pressure(pts, col, 2.2, dash)
            ly = p.p_top + 6 + 16 * i
            fig.line(p.X(11.2), ly - 4, p.X(12.2), ly - 4, col, 2.5, dash); fig.text(p.X(12.4), ly, label, 11, col, 'start', 'bold')
        if k == 1:
            fig.text(p.X(6.2), p.Y(0.42), 'long, low tail: cold recirculates through the atrium', 10.5, TEAL, 'start', 'normal', 'italic')
    fig.notes(70, 432, ['The monitor integrates the curve and divides the cold it assumes was injected by that area. Less cold than assumed, or a truncated tail, both shrink the area and raise the reported output.',
                        'Faster flow sweeps the bolus past the thermistor sooner, so the peak comes earlier and the curve is smaller. Slower flow spreads the same cold over a longer time.'])
    fig.save('n7-t4-thermodilution-curves.svg')


def fig_calorimetry():
    fig = Fig(700, 330,
              'Measuring oxygen consumption at the bedside by indirect calorimetry',
              'A schematic of a ventilated patient in bed. The ventilator delivers gas through an inspiratory limb and receives it back through an expiratory limb. A metabolic cart sits in the circuit: a flow sensor and gas analysers measure inspired and expired oxygen and carbon dioxide breath by breath, and a display reports oxygen consumption, carbon dioxide production and the respiratory quotient. Notes list the conditions the measurement needs: a steady state of twenty to thirty minutes, no circuit leaks, an inspired oxygen fraction below about 0.6, and a calibrated analyser.',
              'Drawn for the Topic 4 section on why direct Fick is the reference standard and why most bedside cardiac outputs skip it.')
    # bed and patient
    fig.rect(60, 190, 250, 40, '#eef2f7', '#5a626b', 4)
    fig.add('<circle cx="95" cy="178" r="16" fill="#f3d9d6" stroke="#5a626b" stroke-width="1.5"/>')
    fig.add('<path d="M112 186 C 150 176, 220 178, 300 186 L 300 196 L 112 196 Z" fill="#f3d9d6" stroke="#5a626b" stroke-width="1.5"/>')
    fig.text(185, 250, 'patient, sedated and ventilated, at rest', 11, MUTED, 'middle')
    # ventilator
    fig.rect(400, 150, 110, 80, '#ffffff', '#1f3a5f', 6); fig.text(455, 175, 'Ventilator', 12, NAVY, 'middle', 'bold'); fig.text(455, 195, 'FiO2 0.40', 11, MUTED, 'middle'); fig.text(455, 212, 'no leaks', 11, MUTED, 'middle')
    # limbs
    fig.add('<path d="M400 170 L 360 170 L 360 150 L 120 150 L 120 168" fill="none" stroke="#1f3a5f" stroke-width="3"/>')
    fig.add('<path d="M108 168 L 108 120 L 250 120" fill="none" stroke="#c0392b" stroke-width="3"/>')
    fig.text(240, 164, 'inspiratory limb', 10.5, NAVY, 'middle'); fig.text(180, 113, 'expiratory limb', 10.5, RED, 'middle')
    # metabolic cart in the expiratory limb
    fig.rect(250, 90, 120, 60, '#ffffff', '#16706B', 6)
    fig.text(310, 110, 'Metabolic cart', 12, TEAL, 'middle', 'bold'); fig.text(310, 126, 'flow sensor', 10.5, MUTED, 'middle'); fig.text(310, 140, 'O2 and CO2 analysers', 10.5, MUTED, 'middle')
    fig.add('<path d="M370 120 L 420 120 L 420 150" fill="none" stroke="#c0392b" stroke-width="3"/>')
    # display
    fig.rect(540, 70, 130, 100, '#1a1d21', '#1a1d21', 6)
    for i, s in enumerate(('VO2   245 mL/min', 'VCO2  201 mL/min', 'RQ    0.82', 'steady state 24 min')):
        fig.text(552, 94 + 20 * i, s, 11.5, '#9be7c4' if i < 3 else '#ffd27a', 'start', 'bold')
    fig.add('<path d="M370 100 L 540 100" fill="none" stroke="#16706B" stroke-width="1.5" stroke-dasharray="4 3"/>')
    fig.text(60, 40, 'VO2 = inspired oxygen per minute minus expired oxygen per minute, measured breath by breath at the airway', 12, NAVY, 'start', 'bold')
    fig.text(60, 58, 'Cardiac output by direct Fick then follows from VO2 divided by the arteriovenous oxygen content difference.', 11.5, '#4a5568')
    fig.notes(60, 282, ['Requirements: 15 to 30 minutes at a steady state with no change in ventilation or agitation, a leak-free circuit (cuff, chest tubes, bronchopleural fistula), an FiO2 below about 0.6 so the small inspired-to-expired oxygen difference is measurable, a warmed-up and calibrated analyser, and a trained operator.',
                        'That cost, in time and equipment, is why most bedside Fick outputs estimate VO2 instead of measuring it, and why the estimate is the weak link.'])
    fig.save('n7-t4-indirect-calorimetry.svg')


if __name__ == '__main__':
    fig_ra(); fig_rv(); fig_pa(); fig_wedge(); fig_ra_vs_wedge(); fig_rv_vs_pa()
    fig_overwedge(); fig_big_v(); fig_cannon_a(); fig_tr(); fig_whip(); fig_resp(); fig_pseudo_wedge(); fig_static_column()
    fig_thermodilution(); fig_calorimetry()
