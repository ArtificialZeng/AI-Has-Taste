"""Figures of the paper (needs matplotlib).   python draw_figures.py outdir"""
import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crossing_tours import tour, prescribed
def cross_points(edges):
    def orient(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]); return (v > 0) - (v < 0)
    box = {}; pts = []
    for k, (a, b) in enumerate(edges): box.setdefault((min(a[0], b[0]), min(a[1], b[1])), []).append(k)
    for k, (a, b) in enumerate(edges):
        x0, y0 = min(a[0], b[0]), min(a[1], b[1])
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                for k2 in box.get((x0 + dx, y0 + dy), ()):
                    if k2 <= k: continue
                    c, d = edges[k2]
                    if a in (c, d) or b in (c, d): continue
                    if orient(a, b, c) * orient(a, b, d) < 0 and orient(c, d, a) * orient(c, d, b) < 0:
                        den = (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])
                        t = ((c[0] - a[0]) * (d[1] - c[1]) - (c[1] - a[1]) * (d[0] - c[0])) / den
                        pts.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return pts
def is_field(e): return (e[1][0] - e[0][0], e[1][1] - e[0][1]) in ((1, 2), (-1, -2))
def draw(ax, edges, n, window=None, lw=0.5, dots=3.0, cells=True):
    if window:
        x0, x1, y0, y1 = window
        edges = [e for e in edges if all(x0 - 2 <= c[0] <= x1 + 2 and y0 - 2 <= c[1] <= y1 + 2 for c in e)]
    f = [e for e in edges if is_field(e)]; g = [e for e in edges if not is_field(e)]
    ax.add_collection(LineCollection(f, colors="#8a8a8a", linewidths=lw * 0.8))
    ax.add_collection(LineCollection(g, colors="#111111", linewidths=lw * 1.3))
    pts = cross_points(edges)
    if window: pts = [p for p in pts if x0 - 0.5 <= p[0] <= x1 + 0.5 and y0 - 0.5 <= p[1] <= y1 + 0.5]
    if pts: ax.scatter([p[0] for p in pts], [p[1] for p in pts], s=dots, c="#d62728", zorder=3, linewidths=0)
    if cells:
        cs = {c for e in edges for c in e}
        if window: cs = {c for c in cs if x0 <= c[0] <= x1 and y0 <= c[1] <= y1}
        ax.scatter([c[0] for c in cs], [c[1] for c in cs], s=dots * 0.5, c="#111111", zorder=2, linewidths=0)
    if window: ax.set_xlim(x0 - 0.6, x1 + 0.6); ax.set_ylim(y0 - 0.6, y1 + 0.6)
    else: ax.set_xlim(-0.8, n - 0.2); ax.set_ylim(-0.8, n - 0.2)
    ax.set_aspect("equal"); ax.axis("off")
    return len(pts)
if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    n = 40; e = tour(n)
    fig, ax = plt.subplots(figsize=(7.2, 7.2)); k = draw(ax, e, n, lw=0.45, dots=2.6, cells=False)
    ax.plot([-0.5, n - 0.5, n - 0.5, -0.5, -0.5], [-0.5, -0.5, n - 0.5, n - 0.5, -0.5], color="#444444", lw=0.6)
    fig.savefig(os.path.join(out, "fig_tour40.pdf"), bbox_inches="tight", pad_inches=0.02); plt.close(fig); print("tour40:", k, "crossings drawn")
    n = 64; e = tour(n)
    fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.9), gridspec_kw={"width_ratios": [1.25, 1.25, 1.0]})
    draw(axs[0], e, n, window=(42, 53, n - 7, n - 1), lw=0.9, dots=14); axs[0].set_title("top wall: pattern A", fontsize=8)
    draw(axs[1], e, n, window=(14, 25, 0, 6), lw=0.9, dots=14); axs[1].set_title("bottom wall, left half: pattern B", fontsize=8)
    draw(axs[2], e, n, window=(0, 8, 26, 37), lw=0.9, dots=14); axs[2].set_title("left wall: pattern of period 2", fontsize=8)
    for ax, w in zip(axs, ((42, 53, n - 7, n - 1), (14, 25, 0, 6), (0, 8, 26, 37))):
        x0, x1, y0, y1 = w
        if y1 == n - 1: ax.plot([x0 - 0.6, x1 + 0.6], [n - 0.5, n - 0.5], color="#444444", lw=1.0)
        if y0 == 0: ax.plot([x0 - 0.6, x1 + 0.6], [-0.5, -0.5], color="#444444", lw=1.0)
        if x0 == 0: ax.plot([-0.5, -0.5], [y0 - 0.6, y1 + 0.6], color="#444444", lw=1.0)
    fig.savefig(os.path.join(out, "fig_patterns.pdf"), bbox_inches="tight", pad_inches=0.03); plt.close(fig); print("patterns done")
    n = 40; e = tour(n); pr = prescribed(n)
    fig = plt.figure(figsize=(7.2, 8.6))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 0.42], hspace=0.08, wspace=0.05)
    wins = [((0, 12, n - 13, n - 1), gs[0, 0]), ((n - 13, n - 1, n - 13, n - 1), gs[0, 1]), ((0, 12, 0, 12), gs[1, 0]),
            ((n - 13, n - 1, 0, 12), gs[1, 1]), ((n // 2 - 14, n // 2 + 9, 0, 5), gs[2, :])]
    for w, g in wins:
        ax = fig.add_subplot(g); x0, x1, y0, y1 = w
        pc = [(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1) if (x, y) not in pr]
        ax.scatter([c[0] for c in pc], [c[1] for c in pc], s=95, marker="s", c="#f3d9a4", zorder=0, linewidths=0)
        draw(ax, e, n, window=w, lw=0.9, dots=12)
        if y1 == n - 1: ax.plot([x0 - 0.6, x1 + 0.6], [n - 0.5, n - 0.5], color="#444444", lw=1.0)
        if y0 == 0: ax.plot([x0 - 0.6, x1 + 0.6], [-0.5, -0.5], color="#444444", lw=1.0)
        if x0 == 0: ax.plot([-0.5, -0.5], [y0 - 0.6, y1 + 0.6], color="#444444", lw=1.0)
        if x1 == n - 1: ax.plot([n - 0.5, n - 0.5], [y0 - 0.6, y1 + 0.6], color="#444444", lw=1.0)
    fig.savefig(os.path.join(out, "fig_patches.pdf"), bbox_inches="tight", pad_inches=0.03); plt.close(fig); print("patches done")
