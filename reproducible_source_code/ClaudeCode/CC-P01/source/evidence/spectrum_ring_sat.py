"""A ring of width 12 around a given whirling tour, with no zones (not stretchable): SAT.   Needs python-sat.

Given a tour T0 of side n with c0 coils, find a tour T1 of side N = n + 24 with c0 + ADD coils that contains every arc
of T0 + (12,12) except exactly one arc u->v, both of whose ends have depth < 2 in the inner board.
  --force "i,j>k,l ..."   arcs (coordinates of the N x N board) that T1 must contain
  --drop  "i,j>k,l"       the arc of T0 + (12,12) that is dropped (default: the solver chooses)
  python spectrum_ring_sat.py tours.txt n [--add 12] [--force ...] [--drop ...] --out file
Used for the tours Y (rings_slow.txt) and for assembling the tours of sides 99..143 with n = 3 (mod 4).
"""
import argparse, math, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--add", type=int, default=12); ap.add_argument("--rays", type=int, default=48)
ap.add_argument("--maxiter", type=int, default=3000); ap.add_argument("--force", default=""); ap.add_argument("--drop", default="")
ap.add_argument("-c", type=int, default=None)
args = ap.parse_args()
parse = lambda s: tuple(tuple(map(int, e.split(","))) for e in s.split(">"))
n = args.n; W = 12; N = n + 2 * W
T = None
for line in open(args.tours):
    if not line.strip(): continue
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n and (args.c is None or int(head.split()[1][6:]) == args.c):
        T = [tuple(map(int, s.split(","))) for s in t.split()]; c = int(head.split()[1][6:]) + args.add
assert T, "inner tour not found"
inner_succ = {(a[0] + W, a[1] + W): (b[0] + W, b[1] + W) for a, b in zip(T, T[1:] + T[:1])}
p = q = (N - 1) / 2
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
inboard = lambda v: 0 <= v[0] < N and 0 <= v[1] < N
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
valid = lambda u, v: (u[0] - p) * (v[1] - q) > (v[0] - p) * (u[1] - q)
ring = [(i, j) for i in range(N) for j in range(N) if depth((i, j)) < W]
ringset = set(ring)
if args.drop:
    zone_tails = [parse(args.drop)[0]]; assert inner_succ[zone_tails[0]] == parse(args.drop)[1], "the arc to drop is not an arc of the inner tour"
else:
    zone_tails = [u for u, v in inner_succ.items() if depth(u) < W + 2 and depth(v) < W + 2]
zone_heads = {inner_succ[u] for u in zone_tails}
arcs = []
for u in ring:
    for d in MOV:
        v = (u[0] + d[0], u[1] + d[1])
        if inboard(v) and valid(u, v) and (v in ringset or v in zone_heads): arcs.append((u, v))
for u in zone_tails:
    arcs.append((u, inner_succ[u]))
    for d in MOV:
        v = (u[0] + d[0], u[1] + d[1])
        if v in ringset and valid(u, v): arcs.append((u, v))
zt = set(zone_tails)
fixed = [(u, v) for u, v in inner_succ.items() if u not in zt]
pool = IDPool(); var = {a: pool.id(a) for a in arcs}
clauses = []
def card(lits, k):
    if k < 0 or k > len(lits): clauses.append([]); return
    clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
outs, ins = {}, {}
for a in arcs: outs.setdefault(a[0], []).append(a); ins.setdefault(a[1], []).append(a)
fixed_heads = {v for _, v in fixed}
for v in ring + zone_tails: card([var[a] for a in outs[v]], 1)
for v in set(ring) | zone_heads:
    if v in fixed_heads: continue
    card([var[a] for a in ins.get(v, [])], 1)
ang = lambda v: math.atan2(v[1] - q, -(v[0] - p))
def crosses(a, th):
    t0, t1 = ang(a[0]), ang(a[1]); d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo_, hi_ = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    return 0 < (th - lo_) % (2 * math.pi) < hi_ - lo_
for r in range(args.rays):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    card([var[a] for a in arcs if crosses(a, th)], c - sum(1 for a in fixed if crosses(a, th)))
drops = []
for u in zone_tails:
    a = (u, inner_succ[u]); d = pool.id(("drop", u)); drops.append(d)
    clauses.append([var[a], d]); clauses.append([-var[a], -d])
clauses.extend(CardEnc.equals(lits=drops, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
for s in args.force.split():
    a = parse(s); assert a in var, f"forced arc {a} is not a possible arc of the ring"
    clauses.append([var[a]])
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0
cells = [(i, j) for i in range(N) for j in range(N) if (2 * i, 2 * j) != (N - 1, N - 1)]
for it in range(1, args.maxiter + 1):
    if not S.solve():
        print(f"UNSAT after {it} iterations, {cuts} cuts ({time.time()-t0:.0f}s)"); break
    ms = set(l for l in S.get_model() if l > 0)
    succ = dict(fixed)
    for a in arcs:
        if var[a] in ms: succ[a[0]] = a[1]
    seen, cyc = set(), []
    for v in cells:
        if v in seen: continue
        cur, cy = v, []
        while cur not in seen: seen.add(cur); cy.append(cur); cur = succ[cur]
        cyc.append(cy)
    if len(cyc) == 1:
        U = [u for u in zone_tails if succ[u] != inner_succ[u]][0]; V = inner_succ[U]
        print(f"FOUND at iteration {it} ({time.time()-t0:.0f}s): dropped {U[0]},{U[1]}>{V[0]},{V[1]}")
        if args.out:
            open(args.out, "a").write(f"n={N} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
        break
    for cy in cyc:
        Sx = set(cy)
        S.add_clause([var[a] for a in arcs if a[0] in Sx and a[1] not in Sx]); cuts += 1
else:
    print("gave up")
