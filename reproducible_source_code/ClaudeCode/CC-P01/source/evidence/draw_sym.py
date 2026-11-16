"""Figure: three whirling knight's tours that are invariant under the quarter turn.   python draw_sym.py  (needs matplotlib)"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
sys.path.insert(0, ".")
from half_family import load
coils = {}; T = load("tours_sym_coils.txt", coils)
COL = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"]
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))
for ax, n in zip(axes, (14, 18, 22)):
    t = T[n]; L = len(t); q = L // 4
    for k in range(4):                                  # the four quarters of the tour are rotations of one another
        seg = [[(t[i][1], -t[i][0]), (t[(i + 1) % L][1], -t[(i + 1) % L][0])] for i in range(k * q, (k + 1) * q)]
        ax.add_collection(LineCollection(seg, colors=COL[k], linewidths=0.9))
    ax.scatter([v[1] for v in t], [-v[0] for v in t], s=2.2, color="#222222", zorder=3)
    ax.plot([(n - 1) / 2], [-(n - 1) / 2], marker="+", color="#222222", ms=8)
    ax.set_title(f"${n}\\times{n}$, {coils[n]} coils", fontsize=10)
    ax.set_xlim(-1, n); ax.set_ylim(-n, 1); ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout(); fig.savefig("sym_tours.pdf"); fig.savefig("sym_tours.png", dpi=170)
