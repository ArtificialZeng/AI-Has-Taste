import sys, json, time
from template import build, solve
n = int(sys.argv[1]); mode = sys.argv[2]; tl = float(sys.argv[3]); states = sys.argv[4] if len(sys.argv) > 4 else "AABA"
pats = json.load(open("shallow4.json"))
for i in range(len(pats["patterns"])):
    for c in range(4):
        cr = (n - 1 - c) % 4
        presc = build(n, states, (i, c), (i, cr), pats)
        t0 = time.time(); name, val, bd, used = solve(n, presc, tl, 4, cover=(mode == "cover"))
        print(f"n={n} {states} pattern {i} phase {c} (right phase {cr}): {mode} {name} {val} ({time.time()-t0:.0f}s)", flush=True)
