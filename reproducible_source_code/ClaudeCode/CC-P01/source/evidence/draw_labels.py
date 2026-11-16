"""Figure: the labelled wedges that give the lower bounds.   python draw_labels.py   (needs matplotlib)"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import lower_bounds as L

COL = {"B": "#1f1f1f", "N": "#ffffff", "O": "#f3c48b", "I": "#9cc5e6"}
def panel(ax, n, label, title, pad=1):
    odd = n % 2; m = n // 2
    cells = [(i, j) for i in range(n) for j in range(n) if not (odd and i == j == m)]
    key = (lambda v: (v[0] - m, v[1] - m)) if odd else (lambda v: v)
    lab = {v: label(key(v)) for v in cells}
    W = [v for v in cells if lab[v]]
    i0, i1 = min(v[0] for v in W) - pad, max(v[0] for v in W) + pad
    j0, j1 = min(v[1] for v in W) - pad, max(v[1] for v in W) + pad
    for (i, j) in cells:
        if i0 <= i <= i1 and j0 <= j <= j1:
            l = lab[(i, j)]
            ax.add_patch(Rectangle((j - 0.5, -i - 0.5), 1, 1, fc=COL[l] if l else "none",
                                   ec="#555555" if l else "#d0d0d0", lw=0.5 if l else 0.3))
            if l == "N": ax.plot([j], [-i], marker="o", ms=1.6, color="#1f1f1f")
    p = (n - 1) / 2
    if i0 <= p <= i1 and j0 <= p <= j1: ax.plot([p], [-p], marker="+", ms=9, color="#c0392b", mew=1.4)
    ax.set_xlim(j0 - 0.6, j1 + 0.6); ax.set_ylim(-i1 - 0.6, -i0 + 0.6); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title, fontsize=9)
fig, axs = plt.subplots(2, 2, figsize=(7.4, 7.6))
panel(axs[0][0], 20, L.even_label(20), "even $n$: $n=20$, bound $12$")
panel(axs[0][1], 23, L.axis_label, "odd $n$, axis wedge: $n=23$, bound $13$")
panel(axs[1][0], 29, L.diag_label(1), "odd $n$, diagonal wedge, pattern 1: $n=29$, bound $16$")
panel(axs[1][1], 27, L.diag_label(2), "odd $n$, diagonal wedge, pattern 2: $n=27$, bound $15$")
handles = [Rectangle((0, 0), 1, 1, fc=COL[k], ec="#555555", lw=0.5) for k in "BNOI"]
fig.legend(handles, ["B  (+1)", "N  (−1)", "O", "I"], loc="lower center", ncol=4, frameon=False, fontsize=9)
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.07, wspace=0.05, hspace=0.12)
fig.savefig("labels.pdf"); fig.savefig("labels.png", dpi=160)
