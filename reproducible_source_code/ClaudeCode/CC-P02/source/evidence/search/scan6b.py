import sys, json, time
from template import build, solve
from uniform import save
pats = json.load(open("shallow6.json")); n = int(sys.argv[1]); states = sys.argv[2]; tl = float(sys.argv[3])
best = None
for i in range(6):
    for c in range(6):
        pass
        presc = build(n, states, (i, c), (i, (n - 1 - c) % 6), pats, 8, 6, 5)
        t0 = time.time(); name, val, bd, used = solve(n, presc, tl, 6)
        print(f"n={n} {states} pattern {i} phase {c}: tour {name} {val} ({time.time()-t0:.0f}s)", flush=True)
        if val is not None and (best is None or val < best[0]): best = (val, i, c, used); save(f"out/p6_{n}_{states}.txt", used)
if best: print("best", best[:3], " 43n/6 =", 43 * n / 6, " 7.5n+13 =", 7.5 * n + 13)
