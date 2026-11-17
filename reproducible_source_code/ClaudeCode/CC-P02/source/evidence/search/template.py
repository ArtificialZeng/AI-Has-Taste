"""Tours from a template: uniform field (1,2), prescribed periodic patterns in all wall zones, free patches at the
four corners and at the midpoints of the top and bottom walls.
Top/bottom zones: single-move patterns A or B (see uniform3.py), letters for top-left, top-right, bottom-left,
bottom-right.  Side walls: a pattern of the shallow wall in canonical form (strip with the wall on top, field (2,1),
period P, height H, rows < F forced), given as a table cell -> moves; it is placed on the left wall by
(xs, ys) -> (H-1-ys, CL - xs) and on the right wall by (xs, ys) -> (n-H+ys, CR + xs).
  python template.py n --left i,c --right i,c [--states AABA] [--mc m] [--mm m] [--time T] [--cover] [--save f]
where i is the index of a canonical pattern in shallow4.json (made by `python template.py --make`) and c its phase."""
import sys, time, json
from ortools.sat.python import cp_model
from kx import edges_of, crossing_pairs
from uniform import save, load, FLD
H, F, P4 = 10, 4, 4
def make_patterns(fn="shallow4.json", P=P4, maxcost=10):
    from states2 import enumerate_states
    cb = enumerate_states((2, 1), P, H, maxcost, F=F, limit=300000, tl=300)
    out = []
    for key, (cost, used) in sorted(cb.found.items(), key=lambda t: (t[1][0], str(t[0]))):
        if key is None: continue
        mv = {}
        for (u, v) in used:
            d = (v[0] - u[0], v[1] - u[1])
            mv.setdefault(f"{u[0]},{u[1]}", []).append(list(d)); mv.setdefault(f"{v[0] % P},{v[1]}", []).append([-d[0], -d[1]])
        out.append({"cost": cost, "matching": {str(k): d for k, d in key}, "moves": mv})
    json.dump({"P": P, "H": H, "F": F, "patterns": out}, open(fn, "w"))
    print(f"wrote {len(out)} patterns to {fn}:", [(p["cost"], sorted(set(p["matching"].values()))) for p in out])
def side_moves(pat, P):
    """canonical table: (xs mod P, ys) -> set of moves, rows ys >= F only"""
    return {tuple(int(v) for v in k.split(",")): {tuple(d) for d in ds} for k, ds in pat["moves"].items() if int(k.split(",")[1]) >= F}
def build(n, states, left, right, pats, mc=8, mm=4, Dt=3):
    """returns presc: cell -> set of moves for prescribed cells"""
    P = pats["P"]; h = n // 2; Dl = H - F; presc = {}
    # side walls
    for side, (pi, c) in (("L", left), ("R", right)):
        tab = side_moves(pats["patterns"][pi], P)
        for y in range(mc, n - mc):
            for d in range(Dl):
                if side == "L":
                    cell = (d, y); src = ((c - y) % P, H - 1 - d); mvs = {(-dy, -dx) for (dx, dy) in tab[src]}
                else:
                    cell = (n - 1 - d, y); src = ((y - c) % P, H - 1 - d); mvs = {(dy, dx) for (dx, dy) in tab[src]}
                presc[cell] = mvs
    # top and bottom zones
    xz = [(mc, h - mm), (h + mm, n - mc)]
    for (wall, zi), st in zip((("top", 0), ("top", 1), ("bot", 0), ("bot", 1)), states):
        lo, hi = xz[zi]
        for x in range(lo, hi):
            x2 = x + 2 if st == "A" else x - 2
            if not (lo <= x2 < hi): continue
            u, v = ((x, n - 2), (x2, n - 1)) if wall == "top" else ((x, 0), (x2, 1))
            for a, b in ((u, v), (v, u)):
                fm = (-1, -2) if wall == "top" else (1, 2)
                presc[a] = {(b[0] - a[0], b[1] - a[1]), fm}
        for x in range(lo + 3, hi - 3):
            for d in range(2, Dt):
                presc[(x, n - 1 - d) if wall == "top" else (x, d)] = {(1, 2), (-1, -2)}
    # interior
    for x in range(Dl, n - Dl):
        for y in range(Dt, n - Dt): presc[(x, y)] = {(1, 2), (-1, -2)}
    return presc
def solve(n, presc, tlim=300, workers=8, cover=False, hint=None, ub=None):
    cells = [(i, j) for i in range(n) for j in range(n)]; idx = {c: k for k, c in enumerate(cells)}
    E = []; forced = []; bad = 0
    for e in edges_of(cells):
        a, b = e; d = (b[0] - a[0], b[1] - a[1]); md = (-d[0], -d[1])
        pa, pb = presc.get(a), presc.get(b)
        ina = None if pa is None else (d in pa); inb = None if pb is None else (md in pb)
        if ina is None and inb is None: E.append(e); continue
        if ina is False or inb is False:
            if ina is True or inb is True: bad += 1                 # the two prescriptions disagree
            continue
        E.append(e); forced.append(len(E) - 1)
    if bad: return "INCONSISTENT", None, None, None
    Pc = crossing_pairs(E)
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
    for (i, j) in Pc:
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    if ub is not None: M.Add(sum(cv) <= ub)
    M.Minimize(sum(cv))
    if hint:
        hs = set(frozenset(e) for e in hint)
        for k, e in enumerate(E): M.AddHint(x[k], 1 if frozenset(e) in hs else 0)
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M); name = S.StatusName(st)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None, S.BestObjectiveBound(), None
    return name, int(S.ObjectiveValue()), S.BestObjectiveBound(), [E[k] for k in range(len(E)) if S.Value(x[k])]
if __name__ == "__main__":
    av = sys.argv[1:]
    if "--make" in av: make_patterns(); sys.exit(0)
    OPTS = ("--left", "--right", "--states", "--mc", "--mm", "--time", "--workers", "--save", "--hint", "--pats")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    n = int(A[0]); pats = json.load(open(opt("--pats", "shallow4.json")))
    left = tuple(int(v) for v in opt("--left", "0,0").split(",")); right = tuple(int(v) for v in opt("--right", "0,0").split(","))
    presc = build(n, opt("--states", "AABA"), left, right, pats, opt("--mc", 8), opt("--mm", 4))
    t0 = time.time()
    name, val, bd, used = solve(n, presc, opt("--time", 300.0), opt("--workers", 8), "--cover" in av, load(opt("--hint", "")) if "--hint" in av else None)
    print(f"n={n} states={opt('--states','AABA')} left={left} right={right} free cells={n*n-len(presc)} {'cover' if '--cover' in av else 'tour'}: "
          f"{name} crossings={val} ({(val or 0)/n:.2f} n) time={time.time()-t0:.0f}s", flush=True)
    if used and "--save" in av: save(opt("--save", "tpl.txt"), used)
