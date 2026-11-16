"""Stretchable FAST ring (SAT): a ring of width 12 that adds 24 coils.   Needs python-sat.

Given a whirling tour T0 of the n x n board with c0 coils, find a tour T1 of the N x N board, N = n + 24, with
c0 + 24 coils:
  * Omega': the cells of T0 in rows 0..R-1 and in the last C columns (a block in the top right corner);
  * T1 keeps every arc of T0 (shifted by (12,12)) that does not touch Omega'; each piece of T0 through Omega' is
    replaced by a path with the same ends (labels as in splice_sat.py), and these paths cover Omega' and the ring;
  * on every side of the ring the move of a cell depends only on its depth, in the columns ZL .. N-ZL-1;
  * arcs that violate condition (W') of the paper are excluded;
  * the top right corner of T1 (rows 0..R+1, last C+2 columns) repeats that of T0, which gives condition (S').
  python fast_sat.py tours_max_coils.txt n --obox R C [--zl 16] --out file
In seeds_max_coils.txt the header of each seed carries fast=1 and obox=R,C, which half_family.py reads.
Not every inner tour admits such a ring; another tour with the same number of coils may.
"""
import argparse, math, json, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--zl", type=int, default=16); ap.add_argument("--zl2", type=int, default=None)
ap.add_argument("--zlen", type=int, default=7); ap.add_argument("--mid", type=int, default=3); ap.add_argument("--pad", type=int, default=1)
ap.add_argument("--rays", type=int, default=48); ap.add_argument("--maxiter", type=int, default=5000)
ap.add_argument("--zones", action="store_true"); ap.add_argument("--copy", type=int, default=0)
ap.add_argument("--clean", type=int, nargs=3, default=None, metavar=("ROWS", "FROM", "WIN"))
ap.add_argument("--win", type=int, nargs=2, default=[2, 6], help="Omega window: from tau0-L to tau0+R-1, tau0 = floor((n-1)/4)")
ap.add_argument("--orows", type=int, default=3, help="Omega uses rows 0..orows-1 of T0")
ap.add_argument("--copyrange", type=int, nargs=2, default=None)
ap.add_argument("--obox", type=int, nargs=2, default=[4, 8])
args = ap.parse_args()
n = args.n; W = 12; N = n + 2 * W; h = N // 2
T = None
for line in open(args.tours):
    if not line.strip(): continue
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n:
        T = [tuple(map(int, s.split(","))) for s in t.split()]; c = abs(int(head.split()[1][6:])) + 2 * W
assert T, "inner tour not found"
succ0 = dict(zip(T, T[1:] + T[:1])); pred0 = {w: u for u, w in succ0.items()}
d0 = lambda v: min(v[0], v[1], n - 1 - v[0], n - 1 - v[1])
sh = lambda v: (v[0] + W, v[1] + W)
tau0 = (n - 1) // 4
def in_omega(v):
    return v[0] < args.obox[0] and v[1] >= n - args.obox[1]
Omega = {v for v in succ0 if in_omega(v)}
alphas = [u for u in succ0 if u not in Omega and succ0[u] in Omega]
betas = []
for a_ in alphas:
    x = succ0[a_]
    while x in Omega: x = succ0[x]
    betas.append(x)
assert len(set(betas)) == len(betas)
p = q = (N - 1) / 2
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
centre = (N // 2, N // 2) if N % 2 else None
inboard = lambda v: 0 <= v[0] < N and 0 <= v[1] < N and v != centre
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
valid = lambda u, v: (u[0] - p) * (v[1] - q) > (v[0] - p) * (u[1] - q)
new = [(i, j) for i in range(N) for j in range(N) if depth((i, j)) < W]
inner = set(new) | {sh(v) for v in Omega}                    # cells whose both arcs are free
A1 = {sh(v): k for k, v in enumerate(alphas)}; B1 = {sh(v): k for k, v in enumerate(betas)}
fixed = {sh(u): sh(v) for u, v in succ0.items() if u not in Omega and v not in Omega}
src = list(inner) + list(A1); dstset = inner | set(B1)
arcs = [(u, (u[0] + d[0], u[1] + d[1])) for u in src for d in MOV]
arcs = [a for a in arcs if inboard(a[1]) and a[1] in dstset and valid(*a)]
arcs = [a for a in arcs if not (a[0] in A1 and a[1] in B1 and A1[a[0]] != B1[a[1]])]
pool = IDPool(); var = {a: pool.id(a) for a in arcs}
clauses = []
# condition (W) of the fast rings: the arc must stay counterclockwise when the right and lower halves move away
fbox = lambda t: (-12,) if t < h - 4 else (-12, 12) if t < h else (12,)
nW = 0
for a in arcs:
    (u, w_), m = a, (a[1][0] - a[0][0], a[1][1] - a[0][1])
    if any(d1 * m[1] - m[0] * d2 < 0 for d1 in fbox(u[0]) for d2 in fbox(u[1])): clauses.append([-var[a]]); nW += 1
def card(lits, k):
    if k < 0 or k > len(lits): clauses.append([]); return
    clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
outs, ins = {}, {}
for a in arcs: outs.setdefault(a[0], []).append(a); ins.setdefault(a[1], []).append(a)
for v in src: card([var[a] for a in outs.get(v, [])], 1)
for v in dstset: card([var[a] for a in ins.get(v, [])], 1)
ang = lambda v: math.atan2(v[1] - q, -(v[0] - p))
def crosses(a, th):
    t0, t1 = ang(a[0]), ang(a[1]); d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo_, hi_ = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    return 0 < (th - lo_) % (2 * math.pi) < hi_ - lo_
for r in range(args.rays):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    k0 = sum(1 for a in fixed.items() if crosses(a, th))
    card([var[a] for a in arcs if crosses(a, th)], c - k0)
# labels: every free cell carries the number of the piece whose replacement path visits it
nb = max(1, (len(alphas) - 1).bit_length())
bit = {(v, j): pool.id(("bit", v, j)) for v in inner for j in range(nb)}
lit = lambda v, j, val: bit[(v, j)] if val else -bit[(v, j)]
for a in arcs:
    u, w = a
    if u in A1 and w in B1: continue
    if u in A1:
        for j in range(nb): clauses.append([-var[a], lit(w, j, (A1[u] >> j) & 1)])
    elif w in B1:
        for j in range(nb): clauses.append([-var[a], lit(u, j, (B1[w] >> j) & 1)])
    else:
        for j in range(nb):
            clauses.append([-var[a], -bit[(u, j)], bit[(w, j)]]); clauses.append([-var[a], bit[(u, j)], -bit[(w, j)]])
rot = lambda v: (v[1], N - 1 - v[0])
def rotk(v, k):
    for _ in range(k): v = rot(v)
    return v
ZL = (args.zl, args.zl2 or args.zl + args.zlen); ZM = (h - args.mid, h + args.mid + N % 2); ZR = (N - ZL[1], N - ZL[0])
neq = 0
def same(A, B):
    global neq
    if A in var and B in var: clauses.append([-var[A], var[B]]); clauses.append([var[A], -var[B]]); neq += 1
    elif A in var: clauses.append([-var[A]])
    elif B in var: clauses.append([-var[B]])
def periodic(rows, ranges):
    for k in range(4):
        for (j0, j1) in ranges:
            for t in range(rows):
                for j in range(j0, j1 - 1):
                    for d in MOV:
                        same((rotk((t, j), k), rotk((t + d[0], j + d[1]), k)), (rotk((t, j + 1), k), rotk((t + d[0], j + 1 + d[1]), k)))
periodic(W, ((args.zl, N - args.zl),))
for i in range(args.obox[0] + 2):                       # the corner of T1 repeats the corner of T0
    for j in range(n - args.obox[1] - 2, n):
        if (i, j) not in succ0: continue
        mv = (succ0[(i, j)][0] - i, succ0[(i, j)][1] - j); a = ((i, j + 2 * W), (i + mv[0], j + 2 * W + mv[1]))
        clauses.append([var[a]] if a in var else [])
print(f"N={N}, {c} coils: Omega has {len(Omega)} cells, {len(alphas)} pieces of T0 to replace ({nb} label bits); "
      f"{len(inner)} free cells, {len(arcs)} variable arcs, {len(fixed)} kept arcs, {neq} zone equalities", flush=True)
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0
cells = [(i, j) for i in range(N) for j in range(N) if (i, j) != centre]
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
        for a_, k in A1.items():                      # each replacement path must end at its own beta
            x = succ[a_]
            while x in inner: x = succ[x]
            assert B1[x] == k
        print(f"FOUND at iteration {it} ({time.time()-t0:.0f}s)")
        if args.out:
            open(args.out, "a").write(f"n={N} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
            json.dump({"N": N, "win": args.win, "orows": args.orows, "omega": sorted(sh(v) for v in Omega),
                       "alphas": sorted(A1)}, open(args.out + f".{N}.json", "w"))
        break
    for cy in cyc:
        Sx = set(cy)
        cl = [var[a] for a in arcs if a[0] in Sx and a[1] not in Sx]
        if cl: S.add_clause(cl); cuts += 1
    if it % 100 == 0: print(f"  iter {it}: {len(cyc)} cycles, {cuts} cuts, {time.time()-t0:.0f}s", flush=True)
else:
    print("gave up")
