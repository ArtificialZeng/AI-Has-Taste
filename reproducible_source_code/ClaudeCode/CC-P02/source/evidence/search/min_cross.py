"""Least number of crossings of a closed knight's tour on an m x n board (CP-SAT).
  python min_cross.py n [m] [--cover] [--time T] [--workers W] [--ub B]
--cover: 2-factors (cycle covers) instead of single cycles."""
import sys, time
from ortools.sat.python import cp_model
from kx import edges_of, crossing_pairs, MOVES8
def solve(n, m=None, cover=False, tlim=600, workers=8, ub=None, hint=None, log=False):
    m = m or n
    cells = [(x, y) for x in range(m) for y in range(n)]; idx = {c: k for k, c in enumerate(cells)}
    E = edges_of(cells); P = crossing_pairs(E)
    M = cp_model.CpModel()
    x = [M.NewBoolVar(f"x{k}") for k in range(len(E))]
    if cover:
        inc = {c: [] for c in cells}
        for k, (a, b) in enumerate(E): inc[a].append(x[k]); inc[b].append(x[k])
        for c in cells: M.Add(sum(inc[c]) == 2)
    else:
        arcs = []
        for k, (a, b) in enumerate(E):
            f = M.NewBoolVar(f"f{k}"); g = M.NewBoolVar(f"g{k}")
            arcs.append((idx[a], idx[b], f)); arcs.append((idx[b], idx[a], g))
            M.Add(f + g == x[k])
        M.AddCircuit(arcs)
    cv = []
    for (i, j) in P:
        c = M.NewBoolVar(f"c{i}_{j}"); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    obj = sum(cv)
    if ub is not None: M.Add(obj <= ub)
    M.Minimize(obj)
    if hint:
        hs = set(hint)
        for k, e in enumerate(E): M.AddHint(x[k], 1 if (e in hs or (e[1], e[0]) in hs) else 0)
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    S.parameters.log_search_progress = log
    st = S.Solve(M)
    name = S.StatusName(st)
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        used = [E[k] for k in range(len(E)) if S.Value(x[k])]
        return name, int(S.ObjectiveValue()), S.BestObjectiveBound(), used
    return name, None, S.BestObjectiveBound(), None
if __name__ == "__main__":
    OPTS = ("--time", "--workers", "--ub", "--save"); av = sys.argv[1:]
    a = [s for k, s in enumerate(av) if not s.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    def opt(name, d):
        return type(d)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else d
    n = int(a[0]); m = int(a[1]) if len(a) > 1 else n
    t0 = time.time()
    name, val, bound, used = solve(n, m, "--cover" in sys.argv, opt("--time", 600.0), opt("--workers", 8), log="--log" in sys.argv)
    print(f"{m}x{n} {'cover' if '--cover' in sys.argv else 'tour'}: {name} value={val} bound={bound:.1f} time={time.time()-t0:.1f}s", flush=True)
    if used and "--save" in sys.argv:
        open(opt("--save", "out.txt"), "w").write(" ".join(f"{a[0]},{a[1]}-{b[0]},{b[1]}" for a, b in used) + "\n")
