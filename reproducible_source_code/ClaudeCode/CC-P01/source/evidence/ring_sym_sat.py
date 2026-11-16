"""Stretchable ring with rotational symmetry (SAT search).   Needs python-sat.

Given a symmetric whirling tour T0 of the n x n board with c0 coils, find a symmetric whirling tour T1 of the N x N
board, N = n + 24, with c0 + 12 coils, such that
  * T1 contains every arc of T0 (shifted by (12,12)) except the rotations of one arc u->v on the left edge of the
    inner board: four arcs for the quarter turn (--order 4, default), two for the half turn (--order 2);
  * on each side of the ring the move of a cell depends only on its depth inside three zones;
  * the ring contains the arc (u-(6,12)) -> (v-(6,12)), so that the same splice can be repeated one level up.
One Boolean variable per orbit of arcs under the rotation.
  python ring_sym_sat.py tours_sym_coils.txt n --out file                          n = 73, ..., 94, n not 3 (mod 4)
  python ring_sym_sat.py tours_half_turn_coils.txt n --order 2 --out file          n = 72, 76, ..., 92
"""
import argparse, math, json, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("tours"); ap.add_argument("n", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--zl", type=int, default=14); ap.add_argument("--zlen", type=int, default=7)
ap.add_argument("--mid", type=int, default=3); ap.add_argument("--rays", type=int, default=48)
ap.add_argument("--maxiter", type=int, default=3000); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--order", type=int, default=4, choices=(2, 4), help="4: quarter turn (default); 2: half turn")
ap.add_argument("--pad", type=int, default=1, help="extra columns on each side of the two outer zones")
args = ap.parse_args()
n = args.n; W = 12; N = n + 2 * W; h = N // 2
T = None
for line in open(args.tours):
    if not line.strip(): continue
    head, t = line.strip().split(" tour=")
    if int(head.split()[0][2:]) == n:
        T = [tuple(map(int, s.split(","))) for s in t.split()]; c = abs(int(head.split()[1][6:])) + W
assert T, "inner tour not found"
inner_succ = {(a[0] + W, a[1] + W): (b[0] + W, b[1] + W) for a, b in zip(T, T[1:] + T[:1])}
p = q = (N - 1) / 2
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
inboard = lambda v: 0 <= v[0] < N and 0 <= v[1] < N
depth = lambda v: min(v[0], v[1], N - 1 - v[0], N - 1 - v[1])
valid = lambda u, v: (u[0] - p) * (v[1] - q) > (v[0] - p) * (u[1] - q)
ring = [(i, j) for i in range(N) for j in range(N) if depth((i, j)) < W]
ringset = set(ring)
ZL = (args.zl, args.zl + args.zlen); ZM = (h - args.mid, h + args.mid + N % 2); ZR = (N - args.zl - args.zlen, N - args.zl)
cL = args.zl + 5                       # cut used by the stretching map (see family.py)
lo, hi = max(ZL[1] + 2, cL + 6), ZM[0] - 3
# droppable inner arcs: both ends in columns 12, 13 (depth 0, 1 of the inner board), rows between the zones
zone_tails = [u for u, v in inner_succ.items() if u[1] in (12, 13) and v[1] in (12, 13)
              and lo <= u[0] <= hi and lo <= v[0] <= hi]
rot = (lambda v: (N - 1 - v[1], v[0])) if args.order == 4 else (lambda v: (N - 1 - v[0], N - 1 - v[1]))   # quarter or half turn
def orbit(v):
    o = [v]
    for _ in range(args.order - 1): o.append(rot(o[-1]))
    return o
left_tails = list(zone_tails)
zone_tails = [w for u in left_tails for w in orbit(u)]
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
def arep(a):
    best = a
    for _ in range(args.order - 1):
        a = (rot(a[0]), rot(a[1])); best = min(best, a)
    return best
pool = IDPool(); var = {a: pool.id(arep(a)) for a in arcs}
seen_cards = set()
clauses = []
def card(lits, k):
    lits = sorted(set(lits)); key = (tuple(lits), k)
    if key in seen_cards: return
    seen_cards.add(key)
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
for r in range(args.rays // args.order):
    th = 2 * math.pi * (r + 0.5137) / args.rays
    k0 = sum(1 for a in fixed if crosses(a, th))
    card([var[a] for a in arcs if crosses(a, th)], c - k0)
drops = []
for u in left_tails:
    a = (u, inner_succ[u]); d = pool.id(("drop", u)); drops.append(d)
    clauses.append([var[a], d]); clauses.append([-var[a], -d])
    t = ((u[0] - 6, u[1] - 12), (inner_succ[u][0] - 6, inner_succ[u][1] - 12))
    clauses.append([-d, var[t]] if t in var else [-d])
clauses.extend(CardEnc.equals(lits=drops, bound=1, vpool=pool, encoding=EncType.seqcounter).clauses)
rot4 = lambda v: (N - 1 - v[1], v[0])                      # the zones are imposed on all four sides
def rotk(v, k):
    for _ in range(k): v = rot4(v)
    return v
neq = 0
def same(A, B):
    global neq
    if A in var and B in var: clauses.append([-var[A], var[B]]); clauses.append([var[A], -var[B]]); neq += 1
    elif A in var: clauses.append([-var[A]])
    elif B in var: clauses.append([-var[B]])
for k in range(4):
    for (j0, j1) in ((ZL[0] - args.pad, ZL[1] + args.pad), ZM, (ZR[0] - args.pad, ZR[1] + args.pad)):
        for t in range(W):
            for j in range(j0, j1 - 1):
                for d in MOV:
                    A = (rotk((t, j), k), rotk((t + d[0], j + d[1]), k))
                    B = (rotk((t, j + 1), k), rotk((t + d[0], j + 1 + d[1]), k))
                    same(A, B)
print(f"N={N}: zones {ZL} {ZM} {ZR}, splice rows {lo}..{hi}; {len(ring)} ring cells, {len(arcs)} variable arcs, "
      f"{len(zone_tails)} droppable inner arcs, {neq} zone equalities, {len(clauses)} clauses", flush=True)
S = Cadical153(bootstrap_with=clauses); t0 = time.time(); cuts = 0
full_cells = [(i, j) for i in range(N) for j in range(N) if not (N % 2 and i == j == N // 2)]
for it in range(1, args.maxiter + 1):
    if not S.solve():
        print(f"UNSAT after {it} iterations, {cuts} cuts ({time.time()-t0:.0f}s)"); break
    ms = set(l for l in S.get_model() if l > 0)
    succ = dict(fixed)
    for a in arcs:
        if var[a] in ms: succ[a[0]] = a[1]
    seen, cyc = set(), []
    for v in full_cells:
        if v in seen: continue
        cur, cy = v, []
        while cur not in seen: seen.add(cur); cy.append(cur); cur = succ[cur]
        cyc.append(cy)
    if len(cyc) == 1:
        U = [u for u in left_tails if succ[u] != inner_succ[u]][0]
        x = succ[U]
        while x in ringset: x = succ[x]
        sym = all(succ[rot(v)] == rot(w) for v, w in succ.items())
        print(f"FOUND at iteration {it} ({time.time()-t0:.0f}s): dropped the {args.order} rotations of {U}->{inner_succ[U]}; "
              f"the path from u ends at v: {x == inner_succ[U]}; symmetric: {sym}")
        if args.out:
            open(args.out, "a").write(f"n={N} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in cyc[0]) + "\n")
            json.dump({"N": N, "zl": args.zl, "zlen": args.zlen, "mid": args.mid, "u": U, "v": inner_succ[U]},
                      open(args.out + f".{N}.json", "w"))
        break
    cyc.sort(key=len)
    for cy in cyc[:max(4, len(cyc) // 2)]:
        Sx = set(cy)
        S.add_clause(sorted({var[a] for a in arcs if a[0] in Sx and a[1] not in Sx})); cuts += 1
    if it % 100 == 0: print(f"  iter {it}: {len(cyc)} cycles, {cuts} cuts, {time.time()-t0:.0f}s", flush=True)
else:
    print("gave up")
