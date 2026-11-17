"""Interfaces and walls for fields of parallel knight moves, periodic along a lattice vector p.
Cells (x, y) with 0 <= x < P (the period vector is p = (P, s*P), s in {0, 1, -1}) and depth t = y - s*x in [0, T).
Bottom (t < FA): forced field A = (a, b), or a wall if A is None.  Top (t >= T - FB): forced field B or a wall.
A forced cell uses exactly its field moves (partners outside the range are virtual).  All other cells have degree 2.
Minimise the number of crossings per period.
  python iface.py P T s  a,b|wall  a,b|wall [--FA f] [--FB f] [--time T] [--show]"""
import sys, time
from ortools.sat.python import cp_model
from kx import cross, HALF
def build(P, T, s):
    dep = lambda c: c[1] - s * c[0]
    cells = [(x, t + s * x) for x in range(P) for t in range(T)]
    cs = set(cells)
    def canon(c):
        k = c[0] // P; return (c[0] - k * P, c[1] - k * s * P)
    E = []
    for u in cells:
        for d in HALF:
            v = (u[0] + d[0], u[1] + d[1])
            if 0 <= dep(v) < T: E.append((u, v))
    pairs = []
    for i, e in enumerate(E):
        for j in range(i + 1, len(E)):
            f = E[j]
            if abs(dep(f[0]) - dep(e[0])) > 8: continue
            for k in (-2, -1, 0, 1, 2):
                g = ((f[0][0] + k * P, f[0][1] + k * s * P), (f[1][0] + k * P, f[1][1] + k * s * P))
                if cross(e, g): pairs.append((i, j)); break
    return cells, E, pairs, canon, dep
def is_field(e, fld):
    d = (e[1][0] - e[0][0], e[1][1] - e[0][1]); return d == fld or d == (-fld[0], -fld[1])
def solve(P, T, s, A, B, FA=6, FB=6, tlim=120, workers=8, hintfield=None):
    cells, E, pairs, canon, dep = build(P, T, s)
    M = cp_model.CpModel(); x = [M.NewBoolVar(f"x{k}") for k in range(len(E))]
    inc = {c: [] for c in cells}
    for k, (u, v) in enumerate(E): inc[u].append(k); inc[canon(v)].append(k)
    for c in cells:
        t = dep(c)
        if A is not None and t < FA:
            for k in inc[c]: M.Add(x[k] == (1 if is_field(E[k], A) else 0))
        elif B is not None and t >= T - FB:
            for k in inc[c]: M.Add(x[k] == (1 if is_field(E[k], B) else 0))
        else: M.Add(sum(x[k] for k in inc[c]) == 2)
    cv = []
    for (i, j) in pairs:
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    M.Minimize(sum(cv))
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return S.StatusName(st), None, None, None
    used = [E[k] for k in range(len(E)) if S.Value(x[k])]
    return S.StatusName(st), int(S.ObjectiveValue()), S.BestObjectiveBound(), used
def picture(P, T, s, used, reps=2):
    """direction of the two moves at each cell, as a rough map: one letter per cell by the set of directions"""
    from collections import defaultdict
    dirs = defaultdict(set)
    for u, v in used:
        d = (v[0] - u[0], v[1] - u[1])
        if d[1] < 0 or (d[1] == 0 and d[0] < 0): d = (-d[0], -d[1])
        k = v[0] // P; v2 = (v[0] - k * P, v[1] - k * s * P)
        dirs[u].add(d); dirs[v2].add(d)
    sym = {frozenset([(1, 2)]): "/", frozenset([(2, 1)]): "-", frozenset([(-1, 2)]): "\\", frozenset([(-2, 1)]): "~"}
    rows = []
    for t in range(T - 1, -1, -1):
        row = ""
        for x in range(P):
            c = (x, t + s * x); row += sym.get(frozenset(dirs[c]), "*")
        rows.append(f"{t:3d} " + row * reps)
    return "\n".join(rows)
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--FA", "--FB", "--time")
    Aa = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda n, d: type(d)(av[av.index(n) + 1]) if n in av else d
    P, T, s = int(Aa[0]), int(Aa[1]), int(Aa[2])
    fld = lambda z: None if z == "wall" else tuple(int(v) for v in z.split(","))
    A, B = fld(Aa[3]), fld(Aa[4])
    t0 = time.time(); st, val, bd, used = solve(P, T, s, A, B, opt("--FA", 6), opt("--FB", 6), opt("--time", 120.0))
    print(f"P={P} T={T} s={s} A={A} B={B}: {st} crossings/period={val} bound={bd} ({time.time()-t0:.0f}s)", flush=True)
    if used and "--show" in av: print(picture(P, T, s, used))
