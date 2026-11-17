"""Closed knight's tours with few crossings: a 'starburst' field in the interior and a free layer along the walls.
Interior: every cell is joined to its neighbours along the knight direction nearest to the direction from the
centre (eight sectors, V-shaped strands with apexes on the diagonals and next to the axes): no two of these moves
cross.  The cells within depth D of the walls and the cells near the centre (|X|,|Y| <= R in doubled coordinates)
are free.  CP-SAT looks for a single closed tour with the least number of crossings.
  python starburst.py n [--D d] [--R r] [--time T] [--workers W] [--save file] [--cover] [--hint file]"""
import sys, time
from ortools.sat.python import cp_model
from kx import edges_of, crossing_pairs
def sgn(v): return (v > 0) - (v < 0)
OFFS = {"TR": 0, "TL": 0, "BL": 0, "BR": 0}        # shift of the apex line of each diagonal ray (in cells)
SEAMS = None                                        # or a triple (o1, o2, o3): V seam, inverted seam, V seam along each diagonal
def field_moves(n, i, j, offs=None, seams=None):
    """the outward field moves of the cell (i, j)"""
    offs = offs or OFFS; seams = seams if seams is not None else SEAMS
    X, Y = 2 * i - (n - 1), 2 * j - (n - 1); sx, sy = sgn(X), sgn(Y)
    a, b = (i if sx < 0 else n - 1 - i), (j if sy < 0 else n - 1 - j)     # distances to the two walls of the quadrant
    q = ("T" if sy > 0 else "B") + ("R" if sx > 0 else "L")
    d = a - b - offs[q]            # > 0: nearer to the horizontal wall of the quadrant (top or bottom)
    if seams is None:
        kind = "apex" if d == 0 else ("H" if d < 0 else "V")
    else:
        o1, o2, o3 = seams
        kind = ("V" if d > o3 else "apex" if d == o3 else "H" if d > o2 else "sink" if d == o2 else "V" if d > o1 else "apex" if d == o1 else "H")
    if kind == "apex": return [(2 * sx, sy), (sx, 2 * sy)]               # both arms lead outwards
    if kind == "sink": return []                                          # both moves arrive from inside
    if kind == "H":
        out = [(2 * sx, sy)]
        if Y == 1 and (seams is None or d < seams[0]): out.append((2 * sx, -1))   # apex row next to the horizontal axis
        return out
    out = [(sx, 2 * sy)]
    if X == 1 and (seams is None or d > seams[2]): out.append((-1, 2 * sy))       # apex column next to the vertical axis
    return out
def field_edges(n, offs=None, seams=None):
    F = set()
    for i in range(n):
        for j in range(n):
            for d in field_moves(n, i, j, offs, seams):
                v = (i + d[0], j + d[1])
                if 0 <= v[0] < n and 0 <= v[1] < n: F.add(frozenset(((i, j), v)))
    return F
def solve(n, D=4, R=7, tlim=600, workers=8, cover=False, hint=None, log=False, ub=None):
    cells = [(i, j) for i in range(n) for j in range(n)]; idx = {c: k for k, c in enumerate(cells)}
    def free(c):
        i, j = c; X, Y = 2 * i - (n - 1), 2 * j - (n - 1)
        return min(i, j, n - 1 - i, n - 1 - j) < D or (abs(X) <= R and abs(Y) <= R)
    FE = field_edges(n)
    Eall = edges_of(cells)
    E = [e for e in Eall if (free(e[0]) and free(e[1])) or frozenset(e) in FE]      # other moves are never used
    P = crossing_pairs(E)
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    for k, e in enumerate(E):
        if not (free(e[0]) and free(e[1])): M.Add(x[k] == 1)             # a field move at a fixed cell
        elif not free(e[0]) or not free(e[1]): pass
    # a fixed cell uses exactly its field moves: its other moves are not in E unless both ends are free
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
    S.parameters.log_search_progress = log
    st = S.Solve(M); name = S.StatusName(st)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None, S.BestObjectiveBound(), None
    return name, int(S.ObjectiveValue()), S.BestObjectiveBound(), [E[k] for k in range(len(E)) if S.Value(x[k])]
def load(fn):
    return [tuple(tuple(int(v) for v in c.split(",")) for c in t.split("-")) for t in open(fn).read().split()]
def save(fn, used):
    open(fn, "w").write(" ".join(f"{a[0]},{a[1]}-{b[0]},{b[1]}" for a, b in used) + "\n")
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--D", "--R", "--time", "--workers", "--save", "--hint", "--ub")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    n = int(A[0]); t0 = time.time()
    hint = load(opt("--hint", "")) if "--hint" in av else None
    name, val, bd, used = solve(n, opt("--D", 4), opt("--R", 7), opt("--time", 600.0), opt("--workers", 8), "--cover" in av, hint, "--log" in av,
                                opt("--ub", 0) if "--ub" in av else None)
    print(f"n={n} D={opt('--D',4)} R={opt('--R',7)} {'cover' if '--cover' in av else 'tour'}: {name} crossings={val} bound={bd:.0f} "
          f"({val/n if val else 0:.2f} n) time={time.time()-t0:.0f}s", flush=True)
    if used and "--save" in av: save(opt("--save", "sb.txt"), used)
