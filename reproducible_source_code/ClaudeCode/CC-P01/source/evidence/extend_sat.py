"""Extension step for exercise 231(a): find a whirling tour of the N x N board with N/2 coils that contains a given
tour of the central n x n board (n = N - 2w) with n/2 coils, except for exactly one of its arcs.
  python extend_sat.py tours_half_coils.txt n 12 --out new_tours.txt      (needs python-sat)
The outer ring (width w) is then a Hamiltonian path of the ring spliced into the removed arc."""
import argparse, math, sys, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("w", type=int)
ap.add_argument("--out", default=None); ap.add_argument("--rays", type=int, default=32)
ap.add_argument("--maxiter", type=int, default=5000)
args = ap.parse_args()
n, w = args.n, args.w; N = n + 2 * w; c = N // 2
T = None
for line in open(args.tours):
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n:
        T = [tuple(map(int, s.split(","))) for s in t.split()]
assert T, "inner tour not found"
inner_succ = {(a[0] + w, a[1] + w): (b[0] + w, b[1] + w) for a, b in zip(T, T[1:] + T[:1])}
p = q = (N - 1) / 2
cells = [(i, j) for i in range(N) for j in range(N)]
cs = set(cells)
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
arcs = [((i, j), (i + di, j + dj)) for (i, j) in cells for di, dj in MOV
        if (i + di, j + dj) in cs and (i - p) * (j + dj - q) > (i + di - p) * (j - q)]
arcset = set(arcs)
pool = IDPool(); var = {a: pool.id(a) for a in arcs}
clauses = []
def card(lits, k): clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
outs = {v: [] for v in cells}; ins = {v: [] for v in cells}
for a in arcs: outs[a[0]].append(a); ins[a[1]].append(a)
for v in cells:
    card([var[a] for a in outs[v]], 1); card([var[a] for a in ins[v]], 1)
ang = lambda v: math.atan2(v[1] - q, -(v[0] - p))
def crosses(a, th):
    t0, t1 = ang(a[0]), ang(a[1]); d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo, hi = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    return 0 < (th - lo) % (2 * math.pi) < hi - lo
for r in range(args.rays):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    card([var[a] for a in arcs if crosses(a, th)], c)
# keep every inner arc except exactly one
drops = []
for u, wv in inner_succ.items():
    assert (u, wv) in arcset
    d = pool.id(("drop", u)); drops.append(d)
    clauses.append([var[(u, wv)], d]); clauses.append([-var[(u, wv)], -d])
clauses.extend(CardEnc.equals(lits=drops, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0
for it in range(1, args.maxiter + 1):
    if not S.solve():
        print(f"N={N} from n={n}: UNSAT after {it} iterations, {cuts} cuts ({time.time()-t0:.0f}s)"); break
    ms = set(l for l in S.get_model() if l > 0)
    succ = {a[0]: a[1] for a in arcs if var[a] in ms}
    seen, cyc = set(), []
    for v in cells:
        if v in seen: continue
        cur, cy = v, []
        while cur not in seen: seen.add(cur); cy.append(cur); cur = succ[cur]
        cyc.append(cy)
    if len(cyc) == 1:
        dropped = [u for u, wv in inner_succ.items() if succ[u] != wv]
        u = dropped[0]
        print(f"N={N} from n={n}: FOUND at iteration {it} ({time.time()-t0:.0f}s). removed inner arc "
              f"{u}->{inner_succ[u]} (board coords); new arcs {u}->{succ[u]} and "
              f"{[x for x in cells if succ[x] == inner_succ[u]][0]}->{inner_succ[u]}")
        if args.out: open(args.out, "a").write(f"n={N} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
        break
    for cy in cyc:
        Sx = set(cy)
        S.add_clause([var[a] for a in arcs if a[0] in Sx and a[1] not in Sx]); cuts += 1
    if it % 200 == 0: print(f"  iter {it}: {len(cyc)} cycles, {cuts} cuts, {time.time()-t0:.0f}s", flush=True)
else:
    print("gave up")
