"""Starburst tours with regular wall gadgets and free patches.
Field: as in starburst.py.  Each wall is cut at its midpoint into two half-walls.  Away from the ends of a half-wall
the two outer rows carry a regular gadget, state A or B:
  on the right half of the top wall (field (1,2)):  A joins (x, n-2) to (x+2, n-1);  B joins (x, n-2) to (x-2, n-1);
the other half-walls are images under the symmetries of the square.  Going around the board the states alternate.
Free cells: near the corners, near the midpoints of the walls and near the centre.  CP-SAT completes the tour.
  python sb2.py n [--mc m] [--mm m] [--dc d] [--dm d] [--R r] [--time T] [--save f] [--cover] [--states ABABABAB]"""
import sys, time
from ortools.sat.python import cp_model
from kx import edges_of, crossing_pairs
from starburst import field_edges, save, load
# the eight half-walls as images of the right half of the top wall under g: (x, y) -> g(x, y), in board coordinates
def syms(n):
    m = n - 1
    return {
        "TR": lambda x, y: (x, y),            "TL": lambda x, y: (m - x, y),
        "RU": lambda x, y: (y, x),            "RD": lambda x, y: (y, m - x),
        "BR": lambda x, y: (x, m - y),        "BL": lambda x, y: (m - x, m - y),
        "LU": lambda x, y: (m - y, x),        "LD": lambda x, y: (m - y, m - x)}
ORDER = ["TR", "RU", "RD", "BR", "BL", "LD", "LU", "TL"]          # going around the board
def gadget_edges(n, states, mc, mm):
    """forced gadget edges, and the set of cells they cover (the regular cells)"""
    G = set(); reg = set(); S = syms(n); h = n // 2
    for name, st in zip(ORDER, states):
        g = S[name]
        for x in range(h + mm, n - mc):
            x2 = x + 2 if st == "A" else x - 2
            if h + mm <= x2 < n - mc:
                u, v = g(x, n - 2), g(x2, n - 1); G.add(frozenset((u, v))); reg.add(u); reg.add(v)
    return G, reg
def solve(n, states="ABABABAB", mc=6, mm=5, dc=5, dm=5, R=7, tlim=600, workers=8, cover=False, hint=None, ub=None, band=-1, offs=None):
    cells = [(i, j) for i in range(n) for j in range(n)]; idx = {c: k for k, c in enumerate(cells)}; h = n // 2
    FE = field_edges(n, offs); G, reg = gadget_edges(n, states, mc, mm)
    def free(c):
        if c in reg: return False
        i, j = c; X, Y = 2 * i - (n - 1), 2 * j - (n - 1); dep = min(i, j, n - 1 - i, n - 1 - j)
        if abs(X) <= R and abs(Y) <= R: return True
        if dep < 2: return True                                    # outer rows outside the regular gadgets
        a = min(i, n - 1 - i); b = min(j, n - 1 - j)             # distances to the nearest walls
        if band >= 0 and abs(a - b) <= band: return True          # a band along the diagonals
        if max(a, b) < mc + 0 and min(a, b) < dc: return True    # corner patch (L-shaped, depth dc)
        along = min(abs(X), abs(Y)) // 2                           # distance from the midpoint of the nearest wall
        if dep < dm and along < mm + 0: return True               # midpoint patch
        return False
    E = []; forced = set()
    for e in edges_of(cells):
        fe = frozenset(e); fr = (free(e[0]), free(e[1]))
        if fe in G: E.append(e); forced.add(len(E) - 1)
        elif fe in FE:
            E.append(e)
            if not (fr[0] and fr[1]): forced.add(len(E) - 1)       # a field move with an end that is fixed or regular
        elif fr[0] and fr[1]: E.append(e)
    P = crossing_pairs(E)
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    for k in forced: M.Add(x[k] == 1)
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
    nfree = sum(1 for c in cells if free(c))
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None, S.BestObjectiveBound(), None, nfree
    return name, int(S.ObjectiveValue()), S.BestObjectiveBound(), [E[k] for k in range(len(E)) if S.Value(x[k])], nfree
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--mc", "--mm", "--dc", "--dm", "--R", "--time", "--workers", "--save", "--hint", "--ub", "--states", "--band")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    n = int(A[0]); t0 = time.time()
    r = solve(n, opt("--states", "ABABABAB"), opt("--mc", 6), opt("--mm", 5), opt("--dc", 5), opt("--dm", 5), opt("--R", 7),
              opt("--time", 600.0), opt("--workers", 8), "--cover" in av, load(opt("--hint", "")) if "--hint" in av else None,
              opt("--ub", 0) if "--ub" in av else None, opt("--band", -1))
    name, val, bd, used, nfree = r
    print(f"n={n} {'cover' if '--cover' in av else 'tour'} free cells={nfree}: {name} crossings={val} bound={bd:.0f} "
          f"({(val or 0)/n:.2f} n; minus 6n: {(val or 0) - 6*n}) time={time.time()-t0:.0f}s", flush=True)
    if used and "--save" in av: save(opt("--save", "sb2.txt"), used)
