"""Writes the Hockey Road Trip badge and icon SVGs (concept v2). PNGs are rendered with headless Chrome."""
NAVY, RED, CREAM, ICE = "#142B40", "#D6493E", "#F5EBDD", "#B9DEE8"
FONT = "'Barlow Condensed','Oswald',Impact,'Arial Narrow',sans-serif"

def _road():
    """Road ribbon along a bezier, wide at the bottom-left and narrow at the horizon (perspective)."""
    P = [(100, 282), (270, 296), (230, 170), (440, 84)]
    def pt(t):
        u = 1 - t
        return tuple(u**3*P[0][i] + 3*u*u*t*P[1][i] + 3*u*t*t*P[2][i] + t**3*P[3][i] for i in (0, 1))
    left, right, centre = [], [], []
    n = 48
    for k in range(n + 1):
        t = k / n
        x0, y0 = pt(max(t - .01, 0)); x1, y1 = pt(min(t + .01, 1))
        dx, dy = x1 - x0, y1 - y0
        L = (dx*dx + dy*dy) ** .5
        nx, ny = -dy / L, dx / L
        x, y = pt(t)
        w = (96 * (1 - t) ** 1.6 + 8) / 2
        left.append((x + nx*w, y + ny*w)); right.append((x - nx*w, y - ny*w)); centre.append((x, y))
    f = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f(left + right[::-1]), "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in centre)

ROAD, LANE = _road()

def art(ink, bg, accent, cid="rc"):
    """Road + puck, drawn in a 600x340 area. The puck has a keyline so it never merges with the road."""
    return f'''
  <clipPath id="{cid}"><polygon points="{ROAD}"/></clipPath>
  <polygon points="{ROAD}" fill="{ink}"/>
  <path d="{LANE}" clip-path="url(#{cid})" fill="none" stroke="{bg}" stroke-width="7" stroke-dasharray="26 20" stroke-linecap="butt"/>
  <ellipse cx="446" cy="262" rx="82" ry="28" fill="{ink}" stroke="{bg}" stroke-width="10"/>
  <path d="M364 262 v50 c0 17 36 30 82 30 s82-13 82-30 v-50" fill="{ink}" stroke="{bg}" stroke-width="10" stroke-linejoin="round"/>
  <ellipse cx="446" cy="256" rx="71" ry="22" fill="{ink}"/>
  <ellipse cx="446" cy="254" rx="57" ry="14" fill="none" stroke="{bg}" stroke-width="3" opacity=".55"/>'''

def leaf(cx, cy, s, fill):
    return f'<path transform="translate({cx} {cy}) scale({s})" d="M0-50 L11-28 L30-34 L24-8 L44-18 L36 8 L22 6 L26 24 L2 18 L2 52 L-2 52 L-2 18 L-26 24 L-22 6 L-36 8 L-44-18 L-24-8 L-30-34 L-11-28 Z" fill="{fill}"/>'

def badge(ink, bg, outline, word2, name, cid="rc"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="680" viewBox="0 0 600 680" role="img" aria-label="Hockey Road Trip badge">
  <title>Hockey Road Trip ({name})</title>
  <polygon points="300,14 574,128 574,548 300,666 26,548 26,128" fill="{outline}" stroke="{outline}" stroke-width="28" stroke-linejoin="round"/>
  <polygon points="300,44 546,146 546,530 300,636 54,530 54,146" fill="{bg}" stroke="{bg}" stroke-width="20" stroke-linejoin="round"/>
  <g transform="translate(0 16)">{art(ink, bg, ink, cid)}</g>
  <text x="300" y="470" text-anchor="middle" font-family="{FONT}" font-weight="900" font-size="124" fill="{ink}" textLength="440" lengthAdjust="spacingAndGlyphs">HOCKEY</text>
  <text x="300" y="552" text-anchor="middle" font-family="{FONT}" font-weight="900" font-size="72" letter-spacing="3" fill="{word2}" textLength="400" lengthAdjust="spacingAndGlyphs">ROAD TRIP</text>
  {leaf(300, 596, 0.6, word2)}
</svg>
'''

def icon():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img" aria-label="Hockey Road Trip icon">
  <title>Hockey Road Trip icon</title>
  <rect width="512" height="512" rx="72" fill="{NAVY}"/>
  <circle cx="256" cy="256" r="211" fill="{CREAM}"/>
  <g transform="translate(23 83) scale(.72)">{art(NAVY, CREAM, NAVY, "ri")}</g>
  <rect x="88" y="404" width="336" height="14" rx="7" fill="{RED}"/>
</svg>
'''

open("badge.svg", "w", encoding="utf-8").write(badge(NAVY, CREAM, NAVY, RED, "full colour"))
open("badge-one-colour.svg", "w", encoding="utf-8").write(badge(NAVY, "#FFFFFF", NAVY, NAVY, "one colour", "rc1"))
open("icon.svg", "w", encoding="utf-8").write(icon())
