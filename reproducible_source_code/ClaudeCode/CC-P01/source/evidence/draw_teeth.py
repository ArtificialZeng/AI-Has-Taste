"""Figure: the seed tour of side 147 (n = 3 mod 4), whose ring is attached at many pieces of the inner tour.   python draw_teeth.py  (needs matplotlib)"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection
sys.path.insert(0, ".")
from half_family import load, Family

N = 147; coils, sc, opts = {}, {}, {}
tours = load("tours_odd3_coils.txt", coils); seeds = load("seeds_odd3_coils.txt", sc, opts)
fam = Family(tours[N - 24], seeds[N], **opts[N])
h, a, b, s = fam.h, fam.a, fam.b, fam.s
succ1 = fam.succ1
T0 = tours[N - 24]; succ0 = {(x[0] + 12, x[1] + 12): (y[0] + 12, y[1] + 12) for x, y in zip(T0, T0[1:] + T0[:1])}
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
along = lambda v: max(min(v[0], N - 1 - v[0]), min(v[1], N - 1 - v[1]))
D, L0, L1 = map(int, opts[N]["omega"].split(","))
zones = [(14 + s, 21 + s), (h - 3, h + 4), (N - 21 - s, N - 14 - s)]
def in_zone(v):
    top = v[0] < 12 or v[0] >= N - 12; left = v[1] < 12 or v[1] >= N - 12
    return (top and any(A <= v[1] < B for A, B in zones)) or (left and any(A <= v[0] < B for A, B in zones))
BLUE, RED, GREY, INK, GREEN = "#0072B2", "#D55E00", "#b8b8b8", "#222222", "#009E73"
seg = lambda x, y: [(x[1], -x[0]), (y[1], -y[0])]
inner, zone, other, new, gone = [], [], [], [], []
for x, y in succ1.items():
    if x in succ0 and succ0[x] == y: inner.append(seg(x, y))                 # an arc of the inner tour that is kept
    elif x in succ0 or y in succ0: new.append(seg(x, y))                      # a new arc at an inner cell
    elif in_zone(x) and in_zone(y): zone.append(seg(x, y))
    else: other.append(seg(x, y))
for x, y in succ0.items():
    if succ1[x] != y: gone.append(seg(x, y))                                  # an arc of the inner tour that is dropped
print(len(new), "new arcs at inner cells;", len(gone), "arcs of the inner tour dropped")
fig = plt.figure(figsize=(6.6, 8.9))
ax = fig.add_axes([0.05, 0.27, 0.90, 0.72]); bx = fig.add_axes([0.02, 0.005, 0.96, 0.255])
TINT, WIN = "#dcebf7", "#f6e3b4"
for A0, B0 in zones:
    for r0 in ((-0.5, 11.5), (N - 12.5, N - 0.5)):
        ax.add_patch(Rectangle((A0 - 0.5, -r0[1]), B0 - A0, r0[1] - r0[0], fc=TINT, ec="none", zorder=0))
        ax.add_patch(Rectangle((r0[0], -(B0 - 0.5)), r0[1] - r0[0], B0 - A0, fc=TINT, ec="none", zorder=0))
for w0, w1 in ((L0, L1), (N - L1, N - L0)):                                   # the eight windows of Omega
    for d0 in (12, N - D):
        ax.add_patch(Rectangle((w0 - 0.5, -(d0 + D - 12) + 0.5), w1 - w0, D - 12, fc=WIN, ec=INK, lw=0.4, zorder=0))
        ax.add_patch(Rectangle((d0 - 0.5, -w1 + 0.5), D - 12, w1 - w0, fc=WIN, ec=INK, lw=0.4, zorder=0))
ax.add_collection(LineCollection(inner, colors=GREY, linewidths=0.16))
ax.add_collection(LineCollection(other, colors=RED, linewidths=0.3))
ax.add_collection(LineCollection(zone, colors=BLUE, linewidths=0.3))
ax.add_collection(LineCollection(new, colors=INK, linewidths=0.9))
for c, name in ((a, "a"), (h, "h"), (b, "b")):
    ax.plot([c - 0.5, c - 0.5], [1.5, -(N + 0.5)], color=INK, lw=0.5, ls=(0, (4, 3)))
    ax.plot([-1.5, N + 0.5], [-(c - 0.5), -(c - 0.5)], color=INK, lw=0.5, ls=(0, (4, 3)))
    ax.text(c - 0.5, 3.5, f"${name}$", ha="center", va="bottom", fontsize=10, color=INK)
    ax.text(-3.5, -(c - 0.5), f"${name}$", ha="right", va="center", fontsize=10, color=INK)
ax.plot([(N - 1) / 2], [-(N - 1) / 2], marker="+", color=INK, ms=9)
ax.set_xlim(-8, N + 1); ax.set_ylim(-(N + 1), 8); ax.set_aspect("equal"); ax.axis("off")
# zoom: the second window of the top side
c0, c1, r1 = 76, 122, 18
box = lambda S: [q for q in S if min(q[0][1], q[1][1]) >= -r1 - 0.01 and c0 <= min(q[0][0], q[1][0]) and max(q[0][0], q[1][0]) <= c1]
bx.add_patch(Rectangle((N - L1 - 0.5, -(D - 1) - 0.5), L1 - L0, D - 12, fc=WIN, ec=INK, lw=0.5, zorder=0))
bx.add_collection(LineCollection(box(inner), colors=GREY, linewidths=0.8))
bx.add_collection(LineCollection(box(other), colors=RED, linewidths=0.8))
bx.add_collection(LineCollection(box(new), colors=INK, linewidths=1.5))
bx.add_collection(LineCollection(box(gone), colors=GREEN, linewidths=1.4, linestyles=(0, (2.2, 1.4)), zorder=4))
cells = [(i, j) for i in range(r1 + 1) for j in range(c0, c1 + 1)]
bx.scatter([j for i, j in cells], [-i for i, j in cells], s=1.4, color=INK, zorder=3)
bx.plot([c0 - 0.5, c1 + 0.5], [-11.5, -11.5], color=INK, lw=0.5, ls=(0, (4, 3)))
bx.text(c0 - 1.2, -5.5, "ring", ha="right", va="center", fontsize=8.5, color=INK, rotation=90)
bx.text(c0 - 1.2, -15, "inner", ha="right", va="center", fontsize=8.5, color=INK, rotation=90)
bx.text(N - (L0 + L1 + 1) / 2, -r1 - 1.0, r"window of $\Omega$", ha="center", va="top", fontsize=8.5, color=INK)
bx.set_xlim(c0 - 3, c1 + 1); bx.set_ylim(-r1 - 2.6, 1); bx.set_aspect("equal"); bx.axis("off")
fig.savefig("teeth147.pdf"); fig.savefig("teeth147.png", dpi=170)
