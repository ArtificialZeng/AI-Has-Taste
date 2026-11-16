"""Whirling knight's tours (Knuth, TAOCP Pre-Fascicle 8A, ex. 229/231): SAT search with lazy subtour elimination.

Board n x n, centre removed when n is odd, pivot ((n-1)/2, (n-1)/2). Arc (i,j)->(i',j') for knight moves with
(i-p)(j'-q) > (i'-p)(j-q). A Hamiltonian cycle with c coils crosses every ray from the pivot that avoids the cells
exactly c times, because its polar angle increases at every step; this is imposed for --rays generic rays.
Short cycles in a solution are forbidden together with their rotations, and the solver is called again.
Every tour written by this program should be re-checked with check_tour.py.

  python whirl_sat.py n c --out tours.txt      find one n x n tour with c coils and append it to tours.txt
  python whirl_sat.py n c --enumerate          count all tours with c coils (small n)
  python whirl_sat.py n --enumerate            count all tours (no coil constraint; small n)
"""
import argparse
import math
import sys
import time

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("n", type=int); ap.add_argument("c", type=int, nargs="?", default=-1)
ap.add_argument("--enumerate", action="store_true"); ap.add_argument("--rays", type=int, default=24)
ap.add_argument("--out", default=None); ap.add_argument("--covers", action="store_true"); ap.add_argument("--maxiter", type=int, default=100000)
args = ap.parse_args()
n, c = args.n, args.c
p = q = (n - 1) / 2
cells = [(i, j) for i in range(n) for j in range(n) if not (n % 2 == 1 and i == p and j == q)]
idx = {v: k for k, v in enumerate(cells)}
arcs = []
for (i, j) in cells:
    for di, dj in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)):
        i2, j2 = i + di, j + dj
        if (i2, j2) in idx and (i - p) * (j2 - q) > (i2 - p) * (j - q):
            arcs.append(((i, j), (i2, j2)))
pool = IDPool()
var = {a: pool.id(("a", a)) for a in arcs}
outs = {v: [] for v in cells}; ins = {v: [] for v in cells}
for a in arcs:
    outs[a[0]].append(a); ins[a[1]].append(a)
clauses = []
def add_card(lits, k):
    enc = CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter)
    clauses.extend(enc.clauses)
for v in cells:
    if not outs[v] or not ins[v]:
        print("vertex without in/out arcs:", v); sys.exit(0)
    add_card([var[a] for a in outs[v]], 1); add_card([var[a] for a in ins[v]], 1)
def ang(v):
    return math.atan2(v[1] - q, -(v[0] - p))   # angle measured from the 'up' direction (towards row 0)
def crosses(a, theta):
    t0, t1 = ang(a[0]), ang(a[1])
    # the polar angle increases or decreases monotonically along the arc; take the short sweep
    d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo, hi = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    x = (theta - lo) % (2 * math.pi)
    return 0 < x < (hi - lo)
if c >= 0:
    for r in range(args.rays):
        theta = 2 * math.pi * (r + 0.5137) / args.rays
        lits = [var[a] for a in arcs if crosses(a, theta)]
        add_card(lits, c)
def rot(v):
    return (v[1], n - 1 - v[0])
solver = Cadical153(bootstrap_with=clauses)
def cycles_of(model_set):
    succ = {a[0]: a[1] for a in arcs if var[a] in model_set}
    seen, cyc = set(), []
    for v in cells:
        if v in seen: continue
        cur, cy = v, []
        while cur not in seen:
            seen.add(cur); cy.append(cur); cur = succ[cur]
        cyc.append(cy)
    return cyc, succ
def coil_count(succ):
    tot = 0.0
    for v in cells:
        w = succ[v]; d = (ang(w) - ang(v) + math.pi) % (2 * math.pi) - math.pi; tot += d
    return round(tot / (2 * math.pi))
t0 = time.time(); found = 0; it = 0; cuts = 0
while it < args.maxiter:
    it += 1
    if not solver.solve():
        print(f"UNSAT after {it} iterations, {cuts} cuts, {time.time()-t0:.0f}s; tours found: {found}"); break
    ms = set(l for l in solver.get_model() if l > 0)
    cyc, succ = cycles_of(ms)
    if args.covers:   # enumerate every cycle cover (no subtour cuts), report its cycle structure
        print(f"cover #{it}: {len(cyc)} cycles, sizes {sorted(len(x) for x in cyc)}", flush=True)
        if it == 1:
            for x in cyc:
                if len(x) <= 12: print("   small cycle:", x)
        solver.add_clause([-var[(v, succ[v])] for v in cells])
        continue
    if len(cyc) == 1:
        found += 1
        cc = coil_count(succ)
        print(f"HAMILTONIAN #{found} at iteration {it} ({time.time()-t0:.0f}s), coils={cc}", flush=True)
        if args.out:
            with open(args.out, "a") as fh:
                fh.write(f"n={n} coils={cc} tour=" + " ".join(f"{i},{j}" for (i, j) in cyc[0]) + "\n")
        if not args.enumerate: break
        solver.add_clause([-var[(v, succ[v])] for v in cells])
        continue
    for cy in cyc:
        S = set(cy)
        for k in range(4):
            leave = [var[a] for a in arcs if a[0] in S and a[1] not in S]
            solver.add_clause(leave); cuts += 1
            S = {rot(v) for v in S}
    if it % 50 == 0:
        print(f"  iter {it}: {len(cyc)} cycles, sizes {sorted(len(x) for x in cyc)[:8]}, cuts {cuts}, {time.time()-t0:.0f}s", flush=True)
