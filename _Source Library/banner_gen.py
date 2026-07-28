# -*- coding: utf-8 -*-
"""Generate flowing-waveform HemoSim banner concepts (SVG). Same palette: navy/red."""
import math

NAVY='#1f3a5f'; NAVY2='#2b4d7a'; RED='#c0392b'; REDL='#e0584a'; BG='#faf9f7'

def catmull_to_path(pts):
    """Smooth path through pts via Catmull-Rom -> cubic Bezier."""
    if len(pts)<2: return ''
    p=pts
    d='M %.1f,%.1f'%(p[0][0],p[0][1])
    for i in range(len(p)-1):
        p0=p[i-1] if i>0 else p[i]
        p1=p[i]; p2=p[i+1]
        p3=p[i+2] if i+2<len(p) else p[i+1]
        c1x=p1[0]+(p2[0]-p0[0])/6.0; c1y=p1[1]+(p2[1]-p0[1])/6.0
        c2x=p2[0]-(p3[0]-p1[0])/6.0; c2y=p2[1]-(p3[1]-p1[1])/6.0
        d+=' C %.1f,%.1f %.1f,%.1f %.1f,%.1f'%(c1x,c1y,c2x,c2y,p2[0],p2[1])
    return d

# --- one arterial beat: (fraction, amplitude 0..1, 1=systolic peak) ---
ART=[(0.00,0.14),(0.09,0.94),(0.15,1.00),(0.24,0.74),(0.34,0.55),(0.40,0.47),
     (0.44,0.44),(0.49,0.55),(0.55,0.50),(0.72,0.32),(1.00,0.14)]
# one venous beat: a, c, v waves
VEN=[(0.00,0.42),(0.09,0.66),(0.17,0.44),(0.24,0.56),(0.33,0.38),(0.55,0.30),
     (0.72,0.62),(0.82,0.40),(1.00,0.42)]

def wave_points(beat, x0, x1, beats, base_y, amp, phase=0.0):
    span=x1-x0; per=span/beats; pts=[]
    n=beats+2
    for k in range(-1,int(beats)+2):
        for (f,a) in beat:
            x=x0+(k+phase)*per+f*per
            y=base_y-a*amp
            if -80<=x<=x1+80: pts.append((x,y))
    return pts

def line(pts,stroke,w,op,glow=True,fill=None):
    d=catmull_to_path(pts)
    f=' filter="url(#glow)"' if glow else ''
    fillattr=' fill="%s"'%fill if fill else ' fill="none"'
    return '<path d="%s" stroke="%s" stroke-width="%.1f" stroke-opacity="%.2f"%s stroke-linecap="round"%s/>'%(d,stroke,w,op,fillattr,f)

W,H=1240,430

def defs():
    return ('<defs>'
      '<linearGradient id="bg" x1="0" y1="0" x2="0.35" y2="1">'
      '<stop offset="0" stop-color="#16293f"/><stop offset="0.55" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient>'%(NAVY,NAVY2)+
      '<radialGradient id="glowred" cx="0.82" cy="0.1" r="0.6">'
      '<stop offset="0" stop-color="%s" stop-opacity="0.55"/><stop offset="0.6" stop-color="%s" stop-opacity="0"/></radialGradient>'%(RED,RED)+
      '<linearGradient id="ribA" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="%s" stop-opacity="0"/><stop offset="0.5" stop-color="%s" stop-opacity="0.9"/><stop offset="1" stop-color="%s" stop-opacity="0"/></linearGradient>'%(REDL,REDL,REDL)+
      '<linearGradient id="ribB" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8fb8e6" stop-opacity="0"/><stop offset="0.5" stop-color="#8fb8e6" stop-opacity="0.8"/><stop offset="1" stop-color="#8fb8e6" stop-opacity="0"/></linearGradient>'+
      '<filter id="glow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'+
      '<filter id="softblur"><feGaussianBlur stdDeviation="7"/></filter>'
      '</defs>')

# ================= CONCEPT A: monitor flow =================
def concept_A():
    s=['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" style="width:100%%;height:100%%;display:block">'%(W,H)]
    s.append(defs())
    s.append('<rect width="%d" height="%d" fill="url(#bg)"/>'%(W,H))
    s.append('<rect width="%d" height="%d" fill="url(#glowred)"/>'%(W,H))
    # faint deep background streamlines
    for i,(by,amp,op) in enumerate([(150,26,0.10),(300,34,0.09),(230,30,0.08)]):
        pts=[]
        for x in range(-60,W+60,20):
            y=by+amp*math.sin(x/220.0+i*1.3)+amp*0.4*math.sin(x/90.0+i)
            pts.append((x,y))
        s.append(line(pts,'#9fb6d4',2,op,glow=False))
    # venous waveforms (light) - lower band, layered
    for by,amp,op,ph in [(322,70,0.20,0.0),(300,84,0.34,0.35),(340,60,0.14,0.7)]:
        s.append(line(wave_points(VEN,-60,W+60,5.2,by,amp,ph),'#a9c6ea',2.4,op))
    # arterial waveforms (red) - upper band, the hero trace
    for by,amp,op,ph,wd in [(232,120,0.22,0.1,2.2),(214,150,0.85,0.45,3.0),(250,96,0.30,0.8,2.0)]:
        col=REDL if op>0.5 else RED
        s.append(line(wave_points(ART,-60,W+60,4.0,by,amp,ph),col,wd,op))
    # wave-shaped bottom edge flowing into the page bg
    edge=[]
    for x in range(-20,W+40,40):
        edge.append((x,398+16*math.sin(x/150.0)))
    edge_path=catmull_to_path(edge)+' L %d,%d L 0,%d Z'%(W,H,H)
    s.append('<path d="%s" fill="%s"/>'%(edge_path,BG))
    # thin red flowing accent riding the edge
    s.append(line(edge,RED,3,0.9,glow=False))
    s.append('</svg>')
    return ''.join(s)

# ================= CONCEPT B: laminar ribbons =================
def concept_B():
    s=['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" style="width:100%%;height:100%%;display:block">'%(W,H)]
    s.append(defs())
    s.append('<rect width="%d" height="%d" fill="url(#bg)"/>'%(W,H))
    s.append('<rect width="%d" height="%d" fill="url(#glowred)"/>'%(W,H))
    # broad laminar ribbons (fluid streamlines) sweeping across
    ribs=[(120,54,'url(#ribB)',0.5,0.0),(190,70,'url(#ribA)',0.55,0.5),
          (250,60,'url(#ribB)',0.4,1.1),(300,86,'url(#ribA)',0.5,1.7),(350,50,'url(#ribB)',0.35,2.3)]
    for by,amp,grad,op,ph in ribs:
        pts=[]
        for x in range(-80,W+80,24):
            y=by+amp*math.sin(x/300.0+ph)+amp*0.35*math.sin(x/130.0+ph*1.6)
            pts.append((x,y))
        s.append(line(pts,grad,10,op,glow=False))
    # a crisp arterial pulse trace threading through the ribbons
    s.append(line(wave_points(ART,-60,W+60,4.2,232,140,0.4),REDL,3.0,0.9))
    # soft wave bottom edge
    edge=[]
    for x in range(-20,W+40,40):
        edge.append((x,402+14*math.sin(x/170.0+1)))
    edge_path=catmull_to_path(edge)+' L %d,%d L 0,%d Z'%(W,H,H)
    s.append('<path d="%s" fill="%s"/>'%(edge_path,BG))
    s.append(line(edge,RED,2.5,0.85,glow=False))
    s.append('</svg>')
    return ''.join(s)

A=concept_A(); B=concept_B()
open('bannerA.svg','w').write(A)
open('bannerB.svg','w').write(B)

# combined preview HTML with the wordmark overlaid (as it'll appear on the page)
def hero(svg,align):
    just='center' if align=='center' else 'flex-start'
    talign='center' if align=='center' else 'left'
    pad='0' if align=='center' else '0 0 0 60px'
    return ('<div style="position:relative;border-radius:14px;overflow:hidden;box-shadow:0 10px 30px rgba(31,58,95,.18);font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">'
      '<div style="position:absolute;inset:0">%s</div>'
      '<div style="position:relative;display:flex;flex-direction:column;justify-content:center;align-items:%s;text-align:%s;height:300px;padding:%s;color:#fff">'
      '<div style="font-size:52px;font-weight:800;letter-spacing:.5px;text-shadow:0 2px 16px rgba(0,0,0,.35)">Hemo<span style="color:#ff8a7a">Sim</span></div>'
      '<div style="font-size:18px;opacity:.9;max-width:560px;margin-top:8px;text-shadow:0 1px 8px rgba(0,0,0,.4)">Hemodynamics, brought to life. A modular, case-based approach to the patient in shock.</div>'
      '</div></div>'%(svg,just,talign,pad))

html=('<div style="display:flex;flex-direction:column;gap:26px;max-width:960px;margin:0 auto">'
  '<div><div style="font:600 13px/1 -apple-system,Segoe UI,sans-serif;color:#8a6b6b;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px">Concept A &middot; Monitor flow (layered arterial + venous tracings)</div>%s</div>'
  '<div><div style="font:600 13px/1 -apple-system,Segoe UI,sans-serif;color:#8a6b6b;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px">Concept B &middot; Laminar ribbons (fluid streamlines + one pulse trace)</div>%s</div>'
  '</div>')%(hero(A,'center'),hero(B,'left'))
open('banner_preview.html','w').write(html)
print('wrote bannerA.svg (%d bytes), bannerB.svg (%d bytes), banner_preview.html'%(len(A),len(B)))
