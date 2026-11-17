"""Closed knight's tours with few crossings: one field (1,2) in the whole interior, free layers along the walls.
Interior cells are joined to (x+1, y+2) and (x-1, y-2).  Free: cells within Dt of the top or bottom wall and within
Dl of the left or right wall.  Optional tying: away from the corners (margin m) the layers are periodic with period
Px along the top and bottom walls and Py along the left and right walls.
  python uniform.py n [--Dt d] [--Dl d] [--Px p] [--Py p] [--m margin] [--time T] [--workers W] [--save f] [--cover] [--hint f]"""
import sys, time
from ortools.sat.python import cp_model
from kx import edges_of, crossing_pairs
FLD = (1, 2)
def save(fn, used): open(fn, "w").write(" ".join(f"{a[0]},{a[1]}-{b[0]},{b[1]}" for a, b in used) + "\n")
def load(fn): return [tuple(tuple(int(v) for v in c.split(",")) for c in t.split("-")) for t in open(fn).read().split()]
def solve(n, Dt=3, Dl=6, Px=0, Py=0, m=8, tlim=600, workers=8, cover=False, hint=None, ub=None, W=None):
    W = W or n                                                     # board W columns by n rows
    cells = [(i, j) for i in range(W) for j in range(n)]; idx = {c: k for k, c in enumerate(cells)}
    free = lambda c: min(c[1], n - 1 - c[1]) < Dt or min(c[0], W - 1 - c[0]) < Dl
    E = []; forced = []
    for e in edges_of(cells):
        d = (e[1][0] - e[0][0], e[1][1] - e[0][1]); fr = (free(e[0]), free(e[1]))
        if d == FLD:
            E.append(e)
            if not (fr[0] and fr[1]): forced.append(len(E) - 1)
        elif fr[0] and fr[1]: E.append(e)
    P = crossing_pairs(E)
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    for k in forced: M.Add(x[k] == 1)
    # periodic tying
    eidx = {frozenset(e): k for k, e in enumerate(E)}; ntied = 0
    def tie(e, shift):
        nonlocal ntied
        f = frozenset(((e[0][0] + shift[0], e[0][1] + shift[1]), (e[1][0] + shift[0], e[1][1] + shift[1])))
        if f in eidx: M.Add(x[eidx[frozenset(e)]] == x[eidx[f]]); ntied += 1
    for k, e in enumerate(E):
        xs = (e[0][0], e[1][0]); ys = (e[0][1], e[1][1])
        if Px and min(xs) >= m and max(xs) + Px < W - m and (min(min(ys), n - 1 - max(ys)) < Dt) and max(min(ys), n - 1 - max(ys)) >= 0:
            if max(ys) >= n - Dt - 2 or min(ys) < Dt + 2: tie(e, (Px, 0))
        if Py and min(ys) >= m and max(ys) + Py < n - m:
            if max(xs) >= W - Dl - 2 or min(xs) < Dl + 2: tie(e, (0, Py))
    if cover:
        inc = {c: [] for c in cells}
        for k, (a, b) in enumerate(E): inc[a].append(x[k]); inc[b].append(x[k])
        for c in cells: M.Add(sum(inc[c]) == 2)
    else:
        arcs = []
        for k, (a, b) in enumerate(E):
            f = M.NewBoolVar(""); g = M.NewBoolVar(""); M.Add(f + g == x[k])
            arcs.append((idx[a], idx[b], f)); arcs.append((idx[b], idx[a], g))
        M.AddCircuit(arcs)
    cv = []
    for (i, j) in P:
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    if ub is not None: M.Add(sum(cv) <= ub)
    M.Minimize(sum(cv))
    if hint:
        hs = set(frozenset(e) for e in hint)
        for k, e in enumerate(E): M.AddHint(x[k], 1 if frozenset(e) in hs else 0)
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M); name = S.StatusName(st)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None, S.BestObjectiveBound(), None, ntied
    return name, int(S.ObjectiveValue()), S.BestObjectiveBound(), [E[k] for k in range(len(E)) if S.Value(x[k])], ntied
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--Dt", "--Dl", "--Px", "--Py", "--m", "--time", "--workers", "--save", "--hint", "--ub", "--W")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    n = int(A[0]); t0 = time.time()
    name, val, bd, used, ntied = solve(n, opt("--Dt", 3), opt("--Dl", 6), opt("--Px", 0), opt("--Py", 0), opt("--m", 8), opt("--time", 600.0),
                                       opt("--workers", 8), "--cover" in av, load(opt("--hint", "")) if "--hint" in av else None,
                                       opt("--ub", 0) if "--ub" in av else None, opt("--W", 0) or None)
    W = opt("--W", 0) or n
    print(f"board {W}x{n} Dt={opt('--Dt',3)} Dl={opt('--Dl',6)} Px={opt('--Px',0)} Py={opt('--Py',0)} tied={ntied} {'cover' if '--cover' in av else 'tour'}: "
          f"{name} crossings={val} bound={bd:.0f} ({(val or 0)/n:.2f} n) time={time.time()-t0:.0f}s", flush=True)
    if used and "--save" in av: save(opt("--save", "uni.txt"), used)
