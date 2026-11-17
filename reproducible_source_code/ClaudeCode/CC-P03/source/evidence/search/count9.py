"""For each odd q: max removable via conflict pairs + CEGAR (snark2), then count ALL optimal sets
(enumerate solutions of the pairwise model of size = max and keep those with L - R non-colorable)."""
import sys, itertools, time
from ortools.sat.python import cp_model
from snark import flower, line_graph
from snark2 import Col
class Collect(cp_model.CpSolverSolutionCallback):
    def __init__(self, y): super().__init__(); self.y = y; self.sols = []
    def on_solution_callback(self): self.sols.append([i for i, v in enumerate(self.y) if self.Value(v)])
for q in map(int, sys.argv[1:]):
    t0 = time.time(); E = flower(q); LE = line_graph(E); nv, ne = len(E), len(LE); C = Col(nv, LE)
    ok = {}
    def nonconf(a, b): return not C.colorable([a, b])
    NC = [(a, b) for a, b in itertools.combinations(range(ne), 2) if nonconf(a, b)]
    deg = [0] * ne
    for a, b in NC: deg[a] += 1; deg[b] += 1
    ncset = set(NC)
    best = None
    for k in range(20, 0, -1):
        md = cp_model.CpModel(); y = [md.NewBoolVar("") for _ in range(ne)]
        for a, b in itertools.combinations(range(ne), 2):
            if (a, b) not in ncset: md.AddBoolOr([y[a].Not(), y[b].Not()])
        md.Add(sum(y) == k)
        sv = cp_model.CpSolver(); sv.parameters.enumerate_all_solutions = True; sv.parameters.num_workers = 1
        cb = Collect(y); sv.Solve(md, cb)
        valid = [R for R in cb.sols if not C.colorable(R)]
        if valid:
            best = k; break
    print(f"q={q}: non-conflict pairs {len(NC)} (= {len(NC)/q:.1f} q), degrees {sorted(set(deg))}; max removable {best}; "
          f"pairwise-compatible {best}-sets {len(cb.sols)}, valid {len(valid)} (= {len(valid)/q:.2f} q)  [{time.time()-t0:.1f}s]", flush=True)
