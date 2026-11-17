"""Exercise 7.2.2.4-157(b): no closed 8x8 knight's tour has at least two moves of each of the 21 symmetry classes.
Classes are orbits of edges under the 8 symmetries of the board; cells ij = row i, column j."""
import itertools, sys
from ortools.sat.python import cp_model
N = 8
cells = [(i, j) for i in range(N) for j in range(N)]; idx = {c: k for k, c in enumerate(cells)}
edges = sorted({tuple(sorted(((i, j), (i + a, j + b)))) for (i, j) in cells for a, b in itertools.product((1, -1, 2, -2), repeat=2)
                if abs(a) != abs(b) and 0 <= i + a < N and 0 <= j + b < N})
syms = [lambda i, j: (i, j), lambda i, j: (j, N - 1 - i), lambda i, j: (N - 1 - i, N - 1 - j), lambda i, j: (N - 1 - j, i),
        lambda i, j: (i, N - 1 - j), lambda i, j: (N - 1 - i, j), lambda i, j: (j, i), lambda i, j: (N - 1 - j, N - 1 - i)]
orbit = {}; classes = []
for e in edges:
    if e in orbit: continue
    o = sorted({tuple(sorted((s(*e[0]), s(*e[1])))) for s in syms}); k = len(classes); classes.append(o)
    for f in o: orbit[f] = k
assert len(classes) == 21 and all(len(o) == 8 for o in classes)
def rep(o):   # canonical representative: lexicographically least edge, written as Knuth's ij -- kl
    a, b = o[0]; return f"{a[0]}{a[1]}--{b[0]}{b[1]}"
def model(req, k=2):
    md = cp_model.CpModel(); X = {e: md.NewBoolVar("") for e in edges}; arcs = []
    for (a, b), v in X.items():
        f = md.NewBoolVar(""); g = md.NewBoolVar(""); md.Add(f + g == v)
        arcs.append((idx[a], idx[b], f)); arcs.append((idx[b], idx[a], g))
    md.AddCircuit(arcs)
    for c in req: md.Add(sum(X[e] for e in classes[c]) >= k)
    return md, X
def feasible(req, tl=60):
    md, X = model(req); s = cp_model.CpSolver(); s.parameters.max_time_in_seconds = tl; s.parameters.num_workers = 8
    r = s.Solve(md); return s.StatusName(r)
if __name__ == "__main__":
    for k, o in enumerate(classes): print(k, rep(o), [f"{a[0]}{a[1]}-{b[0]}{b[1]}" for a, b in o][:3])
    print("all 21 classes at least twice:", feasible(range(21), 300))
