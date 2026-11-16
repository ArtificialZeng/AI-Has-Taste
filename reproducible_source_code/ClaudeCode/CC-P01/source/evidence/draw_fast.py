"""Figure: a fast seed (side 54, 53 coils), whose ring adds 24 coils.   python draw_fast.py  (needs matplotlib)"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection
sys.path.insert(0, ".")
from half_family import load, Family

N = 54; coils, sc, opts = {}, {}, {}
tours = load("tours_max_coils.txt", coils); seeds = load("seeds_max_coils.txt", sc, opts)
fam = Family(tours[N - 24], seeds[N], **opts[N]); h = fam.h; succ1 = fam.succ1
T0 = tours[N - 24]; succ0 = {(x[0] + 12, x[1] + 12): (y[0] + 12, y[1] + 12) for x, y in zip(T0, T0[1:] + T0[:1])}
R, C = map(int, opts[N]["obox"].split(",")); ZA, ZB = h - 6, h + 2 + N % 2
BLUE, RED, GREY, INK, GREEN = "#0072B2", "#D55E00", "#b8b8b8", "#222222", "#009E73"
seg = lambda x, y: [(x[1], -x[0]), (y[1], -y[0])]
def in_zone(v):
    top = v[0] < 12 or v[0] >= N - 12; left = v[1] < 12 or v[1] >= N - 12
    return (top and ZA <= v[1] < ZB) or (left and ZA <= v[0] < ZB)
inner, zone, other, new, gone = [], [], [], [], []
for x, y in succ1.items():
    if x in succ0 and succ0[x] == y: inner.append(seg(x, y))
    elif x in succ0 or y in succ0: new.append(seg(x, y))
    elif in_zone(x) and in_zone(y): zone.append(seg(x, y))
    else: other.append(seg(x, y))
for x, y in succ0.items():
    if succ1[x] != y: gone.append(seg(x, y))
fig = plt.figure(figsize=(6.6, 4.4)); ax = fig.add_axes([0.0, 0.02, 0.62, 0.96]); bx = fig.add_axes([0.63, 0.25, 0.36, 0.5])
TINT, WIN = "#dcebf7", "#f6e3b4"
for r0 in ((-0.5, 11.5), (N - 12.5, N - 0.5)):
    ax.add_patch(Rectangle((ZA - 0.5, -r0[1]), ZB - ZA, r0[1] - r0[0], fc=TINT, ec="none", zorder=0))
    ax.add_patch(Rectangle((r0[0], -(ZB - 0.5)), r0[1] - r0[0], ZB - ZA, fc=TINT, ec="none", zorder=0))
for a in (ax, bx): a.add_patch(Rectangle((N - 12 - C - 0.5, -(11 + R) - 0.5), C, R, fc=WIN, ec=INK, lw=0.5, zorder=0))
ax.add_collection(LineCollection(inner, colors=GREY, linewidths=0.35)); ax.add_collection(LineCollection(other, colors=RED, linewidths=0.5))
ax.add_collection(LineCollection(zone, colors=BLUE, linewidths=0.5)); ax.add_collection(LineCollection(new, colors=INK, linewidths=1.1))
ax.plot([h - 0.5, h - 0.5], [1.5, -(N + 0.5)], color=INK, lw=0.5, ls=(0, (4, 3))); ax.plot([-1.5, N + 0.5], [-(h - 0.5), -(h - 0.5)], color=INK, lw=0.5, ls=(0, (4, 3)))
ax.text(h - 0.5, 2.2, "$h$", ha="center", va="bottom", fontsize=10, color=INK); ax.text(-2.2, -(h - 0.5), "$h$", ha="right", va="center", fontsize=10, color=INK)
ax.plot([(N - 1) / 2], [-(N - 1) / 2], marker="+", color=INK, ms=8)
ax.set_xlim(-5, N + 1); ax.set_ylim(-(N + 1), 5); ax.set_aspect("equal"); ax.axis("off")
c0, r1 = N - 12 - C - 6, 12 + R + 3
box = lambda S: [q for q in S if min(q[0][1], q[1][1]) >= -r1 - 0.01 and min(q[0][0], q[1][0]) >= c0]
bx.add_collection(LineCollection(box(inner), colors=GREY, linewidths=0.9)); bx.add_collection(LineCollection(box(other), colors=RED, linewidths=0.9))
bx.add_collection(LineCollection(box(new), colors=INK, linewidths=1.5)); bx.add_collection(LineCollection(box(gone), colors=GREEN, linewidths=1.4, linestyles=(0, (2.2, 1.4)), zorder=4))
cells = [(i, j) for i in range(r1 + 1) for j in range(c0, N)]
bx.scatter([j for i, j in cells], [-i for i, j in cells], s=1.6, color=INK, zorder=3)
bx.set_xlim(c0 - 1, N); bx.set_ylim(-r1 - 1, 1); bx.set_aspect("equal"); bx.axis("off")
print(len(new), "new arcs at inner cells;", len(gone), "arcs of the inner tour dropped;", len(fam.pieces), "pieces; box", R, C)
fig.savefig("fast54.pdf"); fig.savefig("fast54.png", dpi=170)
