"""Frame extension with a regular boundary (SAT), for n = 3 (mod 4).   Needs python-sat.

Given a tour T0 of the n x n board with c coils, find a tour T1 of the N x N board, N = n + 24, with c + 12 coils such
that every cell of T0 of depth >= 1 keeps its move (as a vector, at its new position), and only the 13 outer layers of
the new board (depth <= 12: twelve new layers and the positions of the old boundary cells) get new moves.
Options: in three zones of each side the moves of the 13 outer rows depend only on the depth (--zones); the moves of
rows 0..R-1 depend only on the depth outside the corners and outside a window at each place where the lanes change
(--clean R FROM WIN); the moves of rows 0..Q-1 are the stretched copies of the same rows of T0 (--copy Q).

The tours of sides 123 to 143 in tours_odd3_coils.txt were found with
  python frame_clean_sat.py tours_odd3_coils.txt n --clean 5 8 6 --out file          (n = 99, 103, 115)
  python frame_clean_sat.py tours_odd3_coils.txt n --clean 5 5 6 --out file          (n = 111)
  python frame_clean_sat.py tours_odd3_coils.txt n --clean 5 8 6 --zones --zl 17 --out file      (n = 107, 119)
Their regular boundary is what splice_sat.py needs.  For the plain extension (sides 51 to 119) see frame_sat.py.
"""
import argparse, math, json, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--zl", type=int, default=14); ap.add_argument("--zlen", type=int, default=7)
ap.add_argument("--mid", type=int, default=3); ap.add_argument("--pad", type=int, default=1)
ap.add_argument("--rays", type=int, default=48); ap.add_argument("--maxiter", type=int, default=3000)
ap.add_argument("--zones", action="store_true"); ap.add_argument("--copy", type=int, default=0)
ap.add_argument("--zrows", type=int, default=13, help="the zone rule applies to rows 0..zrows-1")
ap.add_argument("--pair", action="store_true",
                help="the paths of the new tour inside depth >= 3 must join the same (stretched) end cells as in the inner tour")
ap.add_argument("--clean", type=int, nargs=3, default=None, metavar=("ROWS", "FROM", "WIN"),
                help="rows 0..ROWS-1 depend only on the depth except in a window of WIN columns that starts at "
                     "floor((N-1)/4)-1 from each end of the side, and except in the first FROM columns at each end")
ap.add_argument("--copyrange", type=int, nargs=2, default=None, help="copy only where the distance to the nearer corner along the side is in [lo, hi)")
ap.add_argument("--zl2", type=int, default=None, help="zone 1 is [zl, zl2) instead of [zl, zl+zlen)")
ap.add_argument("--top", type=int, nargs=3, default=None, metavar=("ROWS", "FROM", "TO"),
                help="rows 0..ROWS-1 of each side depend only on the depth for columns FROM..TO-1 (and mirrored)")
args = ap.parse_args()
n = args.n; W = 12; N = n + 2 * W; h = N // 2; D = W + 1
T = None
for line in open(args.tours):
    if not line.strip(): continue
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n:
        T = [tuple(map(int, s.split(","))) for s in t.split()]; c = abs(int(head.split()[1][6:])) + W
assert T, "inner tour not found"
succ0 = dict(zip(T, T[1:] + T[:1]))
d0 = lambda v: min(v[0], v[1], n - 1 - v[0], n - 1 - v[1])
sh = lambda v: (v[0] + W, v[1] + W)
p = q = (N - 1) / 2
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
centre = (N // 2, N // 2) if N % 2 else None
inboard = lambda v: 0 <= v[0] < N and 0 <= v[1] < N and v != centre
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
valid = lambda u, v: (u[0] - p) * (v[1] - q) > (v[0] - p) * (u[1] - q)
frame = [(i, j) for i in range(N) for j in range(N) if depth((i, j)) < D]
fset = set(frame)
fixed = {sh(u): sh(v) for u, v in succ0.items() if d0(u) >= 1 and d0(v) >= 1}   # kept arcs between old cells of depth >= 1
released = [sh(u) for u, v in succ0.items() if d0(u) >= 1 and d0(v) == 0]          # old cells whose move went to the old boundary
need_in = {sh(v) for u, v in succ0.items() if d0(u) == 0 and d0(v) >= 1}  # old cells that lose their predecessor
fixed_heads = set(fixed.values())
arcs = [(u, (u[0] + d[0], u[1] + d[1])) for u in frame + released for d in MOV]
arcs = [a for a in arcs if inboard(a[1]) and valid(*a) and (a[1] in fset or a[1] in need_in)]
pool = IDPool(); var = {a: pool.id(a) for a in arcs}
clauses = []
def card(lits, k):
    if k < 0 or k > len(lits): clauses.append([]); return
    clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
outs, ins = {}, {}
for a in arcs: outs.setdefault(a[0], []).append(a); ins.setdefault(a[1], []).append(a)
for v in frame:
    card([var[a] for a in outs.get(v, [])], 1)
    card([var[a] for a in ins.get(v, [])], 0 if v in fixed_heads else 1)
for v in need_in: card([var[a] for a in ins.get(v, [])], 1)
for v in released: card([var[a] for a in outs.get(v, [])], 1)
ang = lambda v: math.atan2(v[1] - q, -(v[0] - p))
def crosses(a, th):
    t0, t1 = ang(a[0]), ang(a[1]); d = (t1 - t0 + math.pi) % (2 * math.pi) - math.pi
    lo_, hi_ = (t0, t0 + d) if d > 0 else (t0 + d, t0)
    return 0 < (th - lo_) % (2 * math.pi) < hi_ - lo_
for r in range(args.rays):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    k0 = sum(1 for a in fixed.items() if crosses(a, th))
    card([var[a] for a in arcs if crosses(a, th)], c - k0)
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
if args.zones:
    for k in range(4):
        for (j0, j1) in ((ZL[0] - args.pad, ZL[1] + args.pad), ZM, (ZR[0] - args.pad, ZR[1] + args.pad)):
            for t in range(args.zrows):
                for j in range(j0, j1 - 1):
                    for d in MOV:
                        same((rotk((t, j), k), rotk((t + d[0], j + d[1]), k)), (rotk((t, j + 1), k), rotk((t + d[0], j + 1 + d[1]), k)))
if args.top:
    R_, f_, t_ = args.top
    for k in range(4):
        for (j0, j1) in ((f_, t_), (N - t_, N - f_)):
            for t in range(R_):
                for j in range(j0, j1 - 1):
                    for d in MOV:
                        same((rotk((t, j), k), rotk((t + d[0], j + d[1]), k)), (rotk((t, j + 1), k), rotk((t + d[0], j + 1 + d[1]), k)))
if args.clean:
    R_, f_, w_ = args.clean; tau = (N - 1) // 4 - 1
    for k in range(4):
        for (j0, j1) in ((f_, tau), (tau + w_, N - tau - w_), (N - tau, N - f_)):
            for t in range(R_):
                for j in range(j0, j1 - 1):
                    for d in MOV:
                        same((rotk((t, j), k), rotk((t + d[0], j + d[1]), k)), (rotk((t, j + 1), k), rotk((t + d[0], j + 1 + d[1]), k)))
if args.copy:
    # rows 0..Q-1 of the new frame copy the same rows of T0, stretched: columns < a as they are, then 6 inserted
    # columns (period 3), columns a..h0-1 shifted by 6, 12 inserted (period 2), shifted by 18, 6 inserted, shifted by 24
    a_, h0, b0 = args.zl + 5, n // 2, n - args.zl - 5
    def pull(t):
        if t < a_: return t
        if t < a_ + 6: return a_ - 3 + (t - a_) % 3
        if t < h0 + 6: return t - 6
        if t < h0 + 18: return h0 - 2 + (t - h0 - 6) % 2
        if t < b0 + 18: return t - 18
        if t < b0 + 24: return b0 + (t - b0 - 18) % 3
        return t - 24
    nfix = 0
    for v in frame:
        along = max(min(v[0], N - 1 - v[0]), min(v[1], N - 1 - v[1]))
        if depth(v) < args.copy and (args.copyrange is None or args.copyrange[0] <= along < args.copyrange[1]):
            src = (pull(v[0]), pull(v[1]))
            mv = (succ0[src][0] - src[0], succ0[src][1] - src[1])
            a = (v, (v[0] + mv[0], v[1] + mv[1]))
            if a not in var: print("  copied move is not an allowed arc:", v, "<- inner", src, "move", mv, "target depth", depth(a[1]) if inboard(a[1]) else None, "valid", inboard(a[1]) and valid(*a), flush=True)
            clauses.append([var[a]] if a in var else []); nfix += 1
    print(f"copied the moves of {nfix} cells in rows 0..{args.copy - 1} from the inner tour", flush=True)
print(f"N={N}, {c} coils: {len(frame)} frame cells, {len(released)} released cells, {len(arcs)} variable arcs, {len(fixed)} kept arcs, "
      f"{len(need_in)} old cells to re-enter, {neq} zone equalities", flush=True)
pairs = {}
if args.pair:
    a_, h0, b0 = args.zl + 5, n // 2, n - args.zl - 5
    fw = lambda t: t if t < a_ else t + 6 if t < h0 else t + 18 if t < b0 else t + 24
    pred0 = {w: u for u, w in succ0.items()}
    for x in succ0:
        if d0(x) >= 3 and d0(pred0[x]) <= 2:
            y = x
            while d0(succ0[y]) >= 3: y = succ0[y]
            if y != x: pairs[(fw(x[0]), fw(x[1]))] = (fw(y[0]), fw(y[1]))
    print(f"{len(pairs)} long paths inside depth >= 3 of the inner tour must be reproduced", flush=True)
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0; pcuts = 0
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
    bad = 0
    if len(cyc) == 1 and pairs:
        for x, y in pairs.items():
            assert depth(x) >= 3, x
            A = [x]
            while depth(succ[A[-1]]) >= 3: A.append(succ[A[-1]])
            if A[-1] != y:
                As = set(A)
                S.add_clause([var[a] for u in A[:-1] for a in outs.get(u, []) if a[1] not in As and depth(a[1]) >= 3]); bad += 1; pcuts += 1
        if bad:
            if it % 20 == 0: print(f"  iter {it}: single cycle but {bad} of {len(pairs)} paths end at the wrong cell, {pcuts} path cuts, {time.time()-t0:.0f}s", flush=True)
            continue
    if len(cyc) == 1:
        print(f"FOUND at iteration {it} ({time.time()-t0:.0f}s), {pcuts} path cuts")
        if args.out: open(args.out, "a").write(f"n={N} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
        break
    for cy in cyc:
        Sx = set(cy)
        cl = [var[a] for a in arcs if a[0] in Sx and a[1] not in Sx]
        S.add_clause(cl); cuts += 1
    if it % 100 == 0: print(f"  iter {it}: {len(cyc)} cycles, {cuts} cuts, {time.time()-t0:.0f}s", flush=True)
else:
    print("gave up")
