"""Rigour checks for ex. 233.
(1) SW U(R) SW == U(sigma R) for ALL 4096 subsets R (twist can be moved anywhere).
(2) Exact maxima for q = 3 and q = 5 by monotone DFS in the transfer model (all L-edges of the cycle).
(3) Brute force on the explicit graph: for q = 5..13 the maximum sets are exactly the 4q 'claw' sets
    (the 9 L-edges touching the 3 line-vertices at one vertex of J_q)."""
import itertools, sys
from transfer import mul, SW, unit, colorable
sig = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5, 6: 9, 7: 10, 8: 11, 9: 6, 10: 7, 11: 8}
bad = [R for k in range(13) for R in itertools.combinations(range(12), k)
       if mul(mul(SW, unit(frozenset(R))), SW) != unit(frozenset(sig[e] for e in R))]
print("(1) twist symmetry fails for", len(bad), "subsets")
def dfs_max(q):
    L = [(u, e) for u in range(q) for e in range(12)]
    def val(R):
        d = {}
        for u, e in R: d.setdefault(u, set()).add(e)
        return not colorable(q, {u: frozenset(v) for u, v in d.items()})
    best = [0, []]
    def rec(start, R):
        if len(R) > best[0]: best[0] = len(R); best[1] = []
        if len(R) == best[0]: best[1].append(tuple(R))
        for k in range(start, len(L)):
            R2 = R + [L[k]]
            if val(R2): rec(k + 1, R2)
    rec(0, []); return best[0], len(best[1])
for q in (3, 5):
    print(f"(2) transfer model, q={q}: max, number of max sets =", dfs_max(q), flush=True)
from snark import flower, line_graph
from snark2 import Col
from ortools.sat.python import cp_model
for q in range(5, 14, 2):
    E = flower(q); LE = line_graph(E); C = Col(len(E), LE)
    inc = {}
    for k, (u, v) in enumerate(E): inc.setdefault(u, []).append(k); inc.setdefault(v, []).append(k)
    claws = set()
    for v, ks in inc.items():
        claws.add(frozenset(i for i, (x, y) in enumerate(LE) if x in ks or y in ks))
    assert all(len(cl) == 9 and not C.colorable(sorted(cl)) for cl in claws)
    # all max sets from count9-style enumeration
    ne = len(LE); NC = set((a, b) for a, b in itertools.combinations(range(ne), 2) if not C.colorable([a, b]))
    md = cp_model.CpModel(); y = [md.NewBoolVar("") for _ in range(ne)]
    for a, b in itertools.combinations(range(ne), 2):
        if (a, b) not in NC: md.AddBoolOr([y[a].Not(), y[b].Not()])
    md.Add(sum(y) == 9)
    class CB(cp_model.CpSolverSolutionCallback):
        def __init__(s): super().__init__(); s.S = []
        def on_solution_callback(s): s.S.append(frozenset(i for i in range(ne) if s.Value(y[i])))
    sv = cp_model.CpSolver(); sv.parameters.enumerate_all_solutions = True; sv.parameters.num_workers = 1; cb = CB(); sv.Solve(md, cb)
    opt = set(R for R in cb.S if not C.colorable(sorted(R)))
    md.Add(sum(y) >= 10)  # no 10-set even pairwise compatible
    print(f"(3) q={q}: claw sets {len(claws)}, optimal 9-sets {len(opt)}, equal: {opt == claws}", flush=True)
