"""Which doubly periodic sets of knight moves give every cell two moves and have no crossings?
Torus P x Q.  Enumerate all such configurations (CP-SAT) and classify them by the directions of the moves used.
  python torus_fields.py P Q [limit]"""
import sys
from collections import Counter
from ortools.sat.python import cp_model
from kx import cross, HALF
P, Q = int(sys.argv[1]), int(sys.argv[2]); limit = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
cells = [(x, y) for x in range(P) for y in range(Q)]
E = [(u, d) for u in cells for d in HALF]
def seg(k, sx=0, sy=0):
    (u, d) = E[k]; a = (u[0] + sx * P, u[1] + sy * Q); return (a, (a[0] + d[0], a[1] + d[1]))
pairs = []
for i in range(len(E)):
    for j in range(i + 1, len(E)):
        if any(cross(seg(i), seg(j, sx, sy)) for sx in (-1, 0, 1) for sy in (-1, 0, 1)): pairs.append((i, j))
M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
inc = {c: [] for c in cells}
for k, (u, d) in enumerate(E):
    inc[u].append(x[k]); inc[((u[0] + d[0]) % P, (u[1] + d[1]) % Q)].append(x[k])
for c in cells: M.Add(sum(inc[c]) == 2)
for i, j in pairs: M.AddBoolOr([x[i].Not(), x[j].Not()])
class CB(cp_model.CpSolverSolutionCallback):
    def __init__(self): super().__init__(); self.kinds = Counter(); self.n = 0; self.ex = {}
    def on_solution_callback(self):
        self.n += 1
        used = [E[k] for k in range(len(E)) if self.Value(x[k])]
        key = tuple(sorted(Counter(d for _, d in used).items()))
        self.kinds[key] += 1; self.ex.setdefault(key, used)
        if self.n >= limit: self.StopSearch()
S = cp_model.CpSolver(); S.parameters.enumerate_all_solutions = True; S.parameters.num_workers = 1; S.parameters.max_time_in_seconds = 300
cb = CB(); S.Solve(M, cb)
print(f"torus {P}x{Q}: {cb.n} configurations without crossings; by numbers of moves in the directions (1,2),(2,1),(-1,2),(-2,1):")
for key, c in sorted(cb.kinds.items(), key=lambda t: -t[1])[:30]:
    print("  ", dict(key), "x", c)
