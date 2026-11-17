import sys, json, time
from template import build, solve
from uniform import save
pats = json.load(open("shallow4.json"))
for n in map(int, sys.argv[1:]):
    best = None
    for c in range(4):
        cr = (n - 1 - c) % 4
        for mc, mm in ((8, 4), (7, 3), (6, 3)):
            if n // 2 - mm - mc < 2: continue
            presc = build(n, "AABA", (3, c), (3, cr), pats, mc, mm)
            name, val, bd, used = solve(n, presc, 60, 4)
            if val is not None and (best is None or val < best[0]): best = (val, c, mc, mm, name, used)
    if best:
        save(f"out/small{n}.txt", best[5]); print(f"n={n}: {best[0]} crossings (7.5n+13 = {7.5*n+13:.0f}); phase {best[1]}, margins {best[2]},{best[3]}, {best[4]}", flush=True)
    else: print(f"n={n}: none", flush=True)
