"""A whirling knight's tour of the n x n board with c coils that contains given arcs (SAT, lazy subtour cuts).
Needs python-sat.  Used for the listed tours and the bases of the theorem on all numbers of coils.
  python spectrum_base_sat.py n c [--force "i,j>k,l ..."] [--out file]
The arcs after --force (cell>cell, coordinates of the board) must belong to the tour.
"""
import argparse, math, sys, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("n", type=int); ap.add_argument("c", type=int); ap.add_argument("--rays", type=int, default=24)
ap.add_argument("--out", default=None); ap.add_argument("--maxiter", type=int, default=20000); ap.add_argument("--force", default="")
ap.add_argument("--tmax", type=float, default=1e9)
args = ap.parse_args()
n, c = args.n, args.c
p = q = (n - 1) / 2
cells = [(i, j) for i in range(n) for j in range(n) if (2 * i, 2 * j) != (n - 1, n - 1)]
cs = set(cells)
arcs = [((i, j), (i + di, j + dj)) for (i, j) in cells for di, dj in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
        if (i + di, j + dj) in cs and (i - p) * (j + dj - q) > (i + di - p) * (j - q)]
pool = IDPool(); var = {a: pool.id(a) for a in arcs}
outs = {v: [] for v in cells}; ins = {v: [] for v in cells}
for a in arcs: outs[a[0]].append(a); ins[a[1]].append(a)
clauses = []
card = lambda lits, k: clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
for v in cells: card([var[a] for a in outs[v]], 1); card([var[a] for a in ins[v]], 1)
ang = lambda v: math.atan2(v[1] - q, -(v[0] - p))
def crosses(a, th):
    t0, t1 = ang(a[0]), ang(a[1]); d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo, hi = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    return 0 < (th - lo) % (2 * math.pi) < hi - lo
for r in range(args.rays):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    card([var[a] for a in arcs if crosses(a, th)], c)
for s in args.force.split():
    a = tuple(tuple(map(int, e.split(","))) for e in s.split(">")); assert a in var, f"forced arc {a} is not an arc of the board"
    clauses.append([var[a]])
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0
for it in range(1, args.maxiter + 1):
    if time.time() - t0 > args.tmax: print(f"n={n} c={c}: TIMEOUT after {it} iterations"); sys.exit(2)
    if not S.solve(): print(f"n={n} c={c}: UNSAT after {it} iterations, {cuts} cuts ({time.time()-t0:.0f}s)"); sys.exit(1)
    ms = set(l for l in S.get_model() if l > 0)
    succ = {a[0]: a[1] for a in arcs if var[a] in ms}
    seen, cyc = set(), []
    for v in cells:
        if v in seen: continue
        cur, cy = v, []
        while cur not in seen: seen.add(cur); cy.append(cur); cur = succ[cur]
        cyc.append(cy)
    if len(cyc) == 1:
        print(f"n={n} c={c}: FOUND at iteration {it} ({time.time()-t0:.0f}s)")
        if args.out: open(args.out, "a").write(f"n={n} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
        sys.exit(0)
    for cy in cyc:
        Sx = set(cy)
        S.add_clause([var[a] for a in arcs if a[0] in Sx and a[1] not in Sx]); cuts += 1
print(f"n={n} c={c}: gave up"); sys.exit(2)
