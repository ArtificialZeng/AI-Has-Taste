"""Figure: the seed tour of side 96 and its stretchable ring.   python draw_ring.py  (needs matplotlib)"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection
sys.path.insert(0, ".")
from half_family import load

N = 96; h = N // 2; a, b = 19, N - 19
T = load("seeds_half_coils.txt")[N]
succ = dict(zip(T, T[1:] + T[:1]))
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
zones = [(14, 21), (h - 3, h + 3), (N - 21, N - 14)]
def in_zone(v):
    side_cols = v[0] < 12 or v[0] >= N - 12
    side_rows = v[1] < 12 or v[1] >= N - 12
    return (side_cols and any(A <= v[1] < B for A, B in zones)) or (side_rows and any(A <= v[0] < B for A, B in zones))
BLUE, RED, GREY, INK = "#0072B2", "#D55E00", "#b8b8b8", "#222222"
seg = lambda x, y: [(x[1], -x[0]), (y[1], -y[0])]
inner, zone, other, splice = [], [], [], []
for x, y in succ.items():
    dx, dy = depth(x) < 12, depth(y) < 12
    if not dx and not dy: inner.append(seg(x, y))
    elif dx != dy: splice.append(seg(x, y))
    elif in_zone(x) and in_zone(y): zone.append(seg(x, y))
    else: other.append(seg(x, y))
fig = plt.figure(figsize=(6.6, 8.6))
ax = fig.add_axes([0.06, 0.27, 0.88, 0.70]); bx = fig.add_axes([0.06, 0.03, 0.88, 0.19])
for A0, B0 in zones:
    for r0 in ((-0.5, 11.5), (N - 12.5, N - 0.5)):
        ax.add_patch(Rectangle((A0 - 0.5, -r0[1]), B0 - A0, r0[1] - r0[0], fc="#dcebf7", ec="none", zorder=0))
        ax.add_patch(Rectangle((r0[0], -(B0 - 0.5)), r0[1] - r0[0], B0 - A0, fc="#dcebf7", ec="none", zorder=0))
    bx.add_patch(Rectangle((A0 - 0.5, -11.5), B0 - A0, 12, fc="#dcebf7", ec="none", zorder=0))
ax.add_collection(LineCollection(inner, colors=GREY, linewidths=0.25))
ax.add_collection(LineCollection(other, colors=RED, linewidths=0.45))
ax.add_collection(LineCollection(zone, colors=BLUE, linewidths=0.45))
ax.add_collection(LineCollection(splice, colors=INK, linewidths=1.3))
for c, name in ((a, "a"), (h, "h"), (b, "b")):
    ax.plot([c - 0.5, c - 0.5], [1.5, -(N + 0.5)], color=INK, lw=0.5, ls=(0, (4, 3)))
    ax.plot([-1.5, N + 0.5], [-(c - 0.5), -(c - 0.5)], color=INK, lw=0.5, ls=(0, (4, 3)))
    ax.text(c - 0.5, 3.0, f"${name}$", ha="center", va="bottom", fontsize=10, color=INK)
    ax.text(-3.0, -(c - 0.5), f"${name}$", ha="right", va="center", fontsize=10, color=INK)
ax.plot([(N - 1) / 2], [-(N - 1) / 2], marker="+", color=INK, ms=9)
us = [x for x in succ if depth(x) >= 12 and depth(succ[x]) < 12][0]
ax.annotate("$u,v$", xy=(us[1] + 0.5, -us[0] - 1), xytext=(us[1] + 9, -us[0] - 1), fontsize=10, color=INK, va="center",
            arrowprops=dict(arrowstyle="-", color=INK, lw=0.6))
ax.set_xlim(-6, N + 1); ax.set_ylim(-(N + 1), 6); ax.set_aspect("equal"); ax.axis("off")
# zoom: left half of the top side
bx.add_collection(LineCollection([s for s in other if min(s[0][1], s[1][1]) > -12 and max(s[0][0], s[1][0]) < 52], colors=RED, linewidths=0.9))
bx.add_collection(LineCollection([s for s in zone if min(s[0][1], s[1][1]) > -12 and max(s[0][0], s[1][0]) < 52], colors=BLUE, linewidths=0.9))
cells = [(i, j) for i in range(12) for j in range(52)]
bx.scatter([j for i, j in cells], [-i for i, j in cells], s=1.2, color=INK, zorder=3)
for c, name in ((a, "a"), (h, "h")):
    bx.plot([c - 0.5, c - 0.5], [1.2, -12.2], color=INK, lw=0.5, ls=(0, (4, 3)))
    bx.text(c - 0.5, 1.5, f"${name}$", ha="center", va="bottom", fontsize=10, color=INK)
bx.text(17.5, -13.2, "zone, period 3", ha="center", va="top", fontsize=8.5, color=INK)
bx.text(48, -13.2, "zone, period 2", ha="center", va="top", fontsize=8.5, color=INK)
bx.text(5.5, -13.2, "corner", ha="center", va="top", fontsize=8.5, color=INK)
bx.text(33, -13.2, "transition", ha="center", va="top", fontsize=8.5, color=INK)
bx.set_xlim(-1, 52); bx.set_ylim(-15, 3.2); bx.set_aspect("equal"); bx.axis("off")
fig.savefig("ring96.pdf"); fig.savefig("ring96.png", dpi=170)
