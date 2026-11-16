"""Ring attached at several pieces (SAT): the seeds for n = 3 (mod 4).   Needs python-sat.

Given a tour T0 of the n x n board with c coils, find a tour T1 of the N x N board, N = n + 24, with c + 12 coils:
  * Omega: the cells of T0 of depth < 3 in a window of each of the eight places where the lanes of the ring change;
  * T1 keeps every arc of T0 (shifted by (12,12)) that does not touch Omega;
  * T0 passes through Omega in short pieces alpha_i -> ... -> beta_i; in T1 each piece is replaced by a path from
    alpha_i to beta_i (same i), and these paths cover Omega and the twelve new outer layers.  The pairing is enforced
    by a label of a few bits at every cell, which is constant along chosen arcs.
So T1 is T0 with some pieces replaced by longer paths with the same ends.

The six seeds of the paper were found with
  python splice_sat.py tours_odd3_coils.txt n --win 4 12 --zl 17 --zones --clean 5 8 6 --copy 5 --out file
for n = 123, 127, 131, 135, 139, 143:
  --win 4 12   Omega is the window [tau0 - 4, tau0 + 12) along each side, tau0 = floor((n-1)/4), from both ends
  --zones      in the zones (first zone [17, 24), i.e. shift 3) the move depends only on the depth of the cell
  --clean      the same in rows 0..4 outside the corners and the windows
  --copy 5     rows 0..4 of T1 are the stretched copy of rows 0..4 of T0; this gives condition (S)
In seeds_odd3_coils.txt the header of each seed carries shift=3 and omega=15,L0,L1 (the same Omega in the
coordinates of the N x N board), which half_family.py reads.
"""
import argparse, math, json, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--zl", type=int, default=14); ap.add_argument("--zl2", type=int, default=None)
ap.add_argument("--zlen", type=int, default=7); ap.add_argument("--mid", type=int, default=3); ap.add_argument("--pad", type=int, default=1)
ap.add_argument("--rays", type=int, default=48); ap.add_argument("--maxiter", type=int, default=5000)
ap.add_argument("--zones", action="store_true"); ap.add_argument("--copy", type=int, default=0)
ap.add_argument("--clean", type=int, nargs=3, default=None, metavar=("ROWS", "FROM", "WIN"))
ap.add_argument("--win", type=int, nargs=2, default=[2, 6], help="Omega window: from tau0-L to tau0+R-1, tau0 = floor((n-1)/4)")
ap.add_argument("--orows", type=int, default=3, help="Omega uses rows 0..orows-1 of T0")
ap.add_argument("--copyrange", type=int, nargs=2, default=None)
args = ap.parse_args()
n = args.n; W = 12; N = n + 2 * W; h = N // 2
T = None
for line in open(args.tours):
    if not line.strip(): continue
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n:
        T = [tuple(map(int, s.split(","))) for s in t.split()]; c = abs(int(head.split()[1][6:])) + W
assert T, "inner tour not found"
succ0 = dict(zip(T, T[1:] + T[:1])); pred0 = {w: u for u, w in succ0.items()}
d0 = lambda v: min(v[0], v[1], n - 1 - v[0], n - 1 - v[1])
sh = lambda v: (v[0] + W, v[1] + W)
tau0 = (n - 1) // 4
def in_omega(v):
    for _ in range(4):
        t, j = v
        if t < args.orows and (tau0 - args.win[0] <= j < tau0 + args.win[1] or tau0 - args.win[0] <= n - 1 - j < tau0 + args.win[1]): return True
        v = (n - 1 - v[1], v[0])
    return False
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
if args.zones: periodic(W, ((ZL[0] - args.pad, ZL[1] + args.pad), ZM, (ZR[0] - args.pad, ZR[1] + args.pad)))
if args.clean:
    R_, f_, w_ = args.clean; tau = (N - 1) // 4 - 1
    periodic(R_, ((f_, tau), (tau + w_, N - tau - w_), (N - tau, N - f_)))
if args.copy:
    a_, h0, b0 = args.zl + 5, n // 2, n - args.zl - 5
    def pull(t):
        if t < a_: return t
        if t < a_ + 6: return a_ - 3 + (t - a_) % 3
        if t < h0 + 6: return t - 6
        if t < h0 + 18: return h0 - 2 + (t - h0 - 6) % 2
        if t < b0 + 18: return t - 18
        if t < b0 + 24: return b0 + (t - b0 - 18) % 3
        return t - 24
    for v in new:
        along = max(min(v[0], N - 1 - v[0]), min(v[1], N - 1 - v[1]))
        if depth(v) < args.copy and (args.copyrange is None or args.copyrange[0] <= along < args.copyrange[1]):
            s0 = (pull(v[0]), pull(v[1])); mv = (succ0[s0][0] - s0[0], succ0[s0][1] - s0[1])
            a = (v, (v[0] + mv[0], v[1] + mv[1]))
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
