"""Draw four of the tours (the figure in the manuscript).   python draw_tours.py   -> new_tours.pdf"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

want = [("tours_n_coils.txt", 16), ("tours_n_coils.txt", 20), ("tours_half_coils.txt", 24), ("tours_half_coils.txt", 26)]
fig, axs = plt.subplots(1, 4, figsize=(16, 4.3))
for ax, (fn, n) in zip(axs, want):
    for line in open(fn):
        head, t = line.strip().split(" tour=")
        if int(head.split()[0][2:]) == n:
            c = int(head.split()[1][6:])
            T = [tuple(map(int, s.split(","))) for s in t.split()]
    ax.plot([j for (i, j) in T] + [T[0][1]], [-i for (i, j) in T] + [-T[0][0]], color="#1f4e79", lw=0.7)
    ax.plot([(n - 1) / 2], [-(n - 1) / 2], marker="+", color="#c55a11", ms=8)
    ax.set_title(f"{n}x{n}, {c} coils", fontsize=11)
    ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout(); fig.savefig("new_tours.pdf")
