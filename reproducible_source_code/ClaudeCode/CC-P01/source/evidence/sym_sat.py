"""Whirling knight's tours with rotational symmetry (SAT with lazy subtour elimination).   Needs python-sat.

A tour is symmetric if the quarter turn of the board about the pivot maps it to itself (--order 4, the default), and
centrally symmetric if the half turn does (--order 2).  In both cases the number of coils c is odd.  One Boolean
variable per orbit of arcs under the rotation.
  python sym_sat.py n c [--order 2] [--out file] [--maxiter M]        prints SAT (and writes the tour) or UNSAT

The listed tours were found with the least odd c that is at least the least number of coils of all tours:
  python sym_sat.py n c --out tours_sym_coils.txt                              4 does not divide n
  python sym_sat.py n c --order 2 --rays 12 --out tours_half_turn_coils.txt    4 divides n
  python sym_sat.py n c --clean 5 5 6 --lanes --out file                       n = 123, 127, 131, 135, 139
  python sym_sat.py n c --clean 5 8 6 --lanes --out file                       n = 143
With --clean R FROM WIN the moves in rows 0..R-1 depend only on the row, outside the corners (FROM columns) and
outside a window of WIN columns at each place where the lanes change; --lanes fixes these moves to the lane rule
of the rings.  The seeds for n = 3 (mod 4) need inner tours of this kind (see splice_sym_sat.py).
"""
import argparse, math, sys, time
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153

ap = argparse.ArgumentParser()
ap.add_argument("n", type=int); ap.add_argument("c", type=int); ap.add_argument("--out", default=None)
ap.add_argument("--maxiter", type=int, default=20000); ap.add_argument("--rays", type=int, default=6)
ap.add_argument("--order", type=int, default=4, choices=(2, 4), help="4: quarter turn (default); 2: half turn")
ap.add_argument("--lanes", action="store_true", help="with --clean: the rows follow the lane rule of the rings")
ap.add_argument("--clean", type=int, nargs=3, default=None, metavar=("ROWS", "FROM", "WIN"),
                help="in rows 0..ROWS-1 the move depends only on the row, outside the corners and two windows per side")
args = ap.parse_args()
n, c = args.n, args.c
P = (n - 1) / 2
centre = (n // 2, n // 2) if n % 2 else None
cells = [(i, j) for i in range(n) for j in range(n) if (i, j) != centre]
cs = set(cells)
rot = (lambda v: (n - 1 - v[1], v[0])) if args.order == 4 else (lambda v: (n - 1 - v[0], n - 1 - v[1]))   # quarter or half turn
valid = lambda u, v: (u[0] - P) * (v[1] - P) > (v[0] - P) * (u[1] - P)
MOV = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
arcs = [(u, (u[0] + d[0], u[1] + d[1])) for u in cells for d in MOV]
arcs = [a for a in arcs if a[1] in cs and valid(*a)]
def rep(a):                                                 # canonical representative of the orbit of an arc
    best = a
    for _ in range(args.order - 1):
        a = (rot(a[0]), rot(a[1])); best = min(best, a)
    return best
pool = IDPool(); var = {a: pool.id(rep(a)) for a in arcs}
out, inn = {}, {}
for a in arcs: out.setdefault(a[0], []).append(a); inn.setdefault(a[1], []).append(a)
clauses = []
seen_cards = set()
def exactly(lits, k):
    lits = sorted(set(lits)); key = (tuple(lits), k)
    if key in seen_cards: return
    seen_cards.add(key)
    if k < 0 or k > len(lits): clauses.append([]); return
    clauses.extend(CardEnc.equals(lits=lits, bound=k, vpool=pool, encoding=EncType.seqcounter).clauses)
for v in cells:                                             # equal constraints of rotated cells are added once
    exactly([var[a] for a in out.get(v, [])], 1); exactly([var[a] for a in inn.get(v, [])], 1)
def crosses(a, th):
    (u, v) = a; d = (math.cos(th), math.sin(th))
    x1, y1, x2, y2 = u[0] - P, u[1] - P, v[0] - P, v[1] - P
    return x1 * d[1] - d[0] * y1 > 0 and d[0] * y2 - x2 * d[1] > 0
for k in range(args.rays):                                  # rays within one sector; the others follow by symmetry
    th = 0.0137 + k * (2 * math.pi / args.order) / args.rays
    lits = [var[a] for a in arcs if crosses(a, th)]
    exactly(lits, c)
if args.clean:
    R_, f_, w_ = args.clean; tau = (n - 1) // 4 - 1
    def same(A, B):
        if A in var and B in var: clauses.append([-var[A], var[B]]); clauses.append([var[A], -var[B]])
        elif A in var: clauses.append([-var[A]])
        elif B in var: clauses.append([-var[B]])
    rules = (lambda i: (2, 1) if i % 3 == 0 else (-1, -2), lambda i: (2, -1) if i % 4 in (0, 1) else (-2, -1), lambda i: (1, -2) if i % 3 in (0, 1) else (-2, 1))
    for (j0, j1), rule in zip(((f_, tau), (tau + w_, n - tau - w_), (n - tau, n - f_)), rules):
        for t in range(R_):
            for j in range(j0, j1 - 1):
                for d in MOV:
                    same(((t, j), (t + d[0], j + d[1])), ((t, j + 1), (t + d[0], j + 1 + d[1])))
            if args.lanes:
                for j in range(j0, j1):
                    m = rule(t); a = ((t, j), (t + m[0], j + m[1]))
                    clauses.append([var[a]] if a in var else [])
s = Cadical153(bootstrap_with=clauses); t0 = time.time()
for it in range(args.maxiter):
    if not s.solve(): print(f"n={n} c={c}: UNSAT after {it} iterations ({time.time() - t0:.0f}s)"); sys.exit(0)
    m = set(x for x in s.get_model() if x > 0)
    succ = {a[0]: a[1] for a in arcs if var[a] in m}
    seen, cycles = set(), []
    for v in cells:
        if v in seen: continue
        cyc, x = [], v
        while x not in seen: seen.add(x); cyc.append(x); x = succ[x]
        cycles.append(cyc)
    if len(cycles) == 1:
        T = cycles[0]; i0 = T.index(min(T)); T = T[i0:] + T[:i0]
        shift = T.index(rot(T[0])) * args.order // len(T)
        print(f"n={n} c={c}: SAT at iteration {it} ({time.time() - t0:.0f}s); the rotation shifts the tour by {shift}/{args.order} of its length")
        if args.out: open(args.out, "a").write(f"n={n} coils={c} tour=" + " ".join(f"{i},{j}" for i, j in T) + "\n")
        sys.exit(0)
    cycles.sort(key=len)
    for cyc in cycles[:max(4, len(cycles) // 2)]:           # forbid each short cycle (its rotations share the variables)
        cl = sorted({-var[(cyc[k], cyc[(k + 1) % len(cyc)])] for k in range(len(cyc))})
        s.add_clause(cl)
print(f"n={n} c={c}: undecided after {args.maxiter} iterations")
