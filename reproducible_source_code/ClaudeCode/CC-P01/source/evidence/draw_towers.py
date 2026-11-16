"""Figure: three towers of two rings around the same base (side 48, 40 coils): slow+slow, fast+slow, fast+fast.
   python draw_towers.py  (needs matplotlib)"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
sys.path.insert(0, ".")
import half_family as hf, spectrum_family as sf

N0, c, k = 48, 40, 2
cmax, sc, omax = {}, {}, {}
tmax, smax = hf.load("tours_max_coils.txt", cmax), hf.load("seeds_max_coils.txt", sc, omax)
sslow, rslow = hf.load("seeds_slow_on_fast.txt"), hf.load("rings_slow.txt")
bases = [(cc, T) for n, cc, T in sf.load_all("bases_spectrum.txt") if n == N0]
cl = sf.Class(N0, tmax, cmax, smax, omax, sslow, rslow, bases)
BLUE, RED, GREY, INK = "#0072B2", "#D55E00", "#b0b0b0", "#222222"
N = N0 + 24 * k
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.55)); fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.085, wspace=0.03)
seg = lambda x, y: [(x[1], -x[0]), (y[1], -y[0])]
for ax, b in zip(axes, (0, 1, 2)):
    a = k - b; succ = cl.tower(c, a, b); coils = c + 12 * a + 24 * b
    assert hf.check_tour(N, hf.Family.as_list(succ), coils)
    kinds = ["fast"] * b + ["slow"] * a                      # ring 1 (inner) and ring 2 (outer)
    lines = {"base": [], "slow": [], "fast": []}
    for x, y in succ.items():
        d = min(x[0], x[1], N - 1 - x[0], N - 1 - x[1])
        lines["base" if d >= 24 else kinds[1] if d < 12 else kinds[0]].append(seg(x, y))
    ax.add_collection(LineCollection(lines["base"], colors=GREY, linewidths=0.3))
    ax.add_collection(LineCollection(lines["slow"], colors=BLUE, linewidths=0.3))
    ax.add_collection(LineCollection(lines["fast"], colors=RED, linewidths=0.3))
    ax.plot([(N - 1) / 2], [-(N - 1) / 2], marker="+", color=INK, ms=5, mew=0.6)
    ax.set_xlim(-1.5, N + 0.5); ax.set_ylim(-(N + 0.5), 1.5); ax.set_aspect("equal"); ax.axis("off")
    parts = " + ".join(["40"] + ["24" if t == "fast" else "12" for t in kinds])
    ax.text((N - 1) / 2, -(N + 3.2), f"{parts} = {coils} coils", ha="center", va="top", fontsize=9, color=INK)
for ext in ("pdf", "png"): fig.savefig(f"towers96.{ext}", dpi=220)
print("towers96 written")
