"""Edge gadgets: a strip that is periodic in x (period P) with a wall at the top (y = H-1).
Below the strip the tour follows a field of parallel moves of direction (a, b), b > 0: every cell (x, y) is joined
to (x+a, y+b) and (x-a, y-b).  The cells of the rows y < F are forced to follow the field (their partners below the
strip are virtual).  We minimise the number of crossings per period among all sets of moves in which every cell has
degree 2 (degree 1 for cells whose lower field partner is virtual), counting the crossings with the virtual moves
of the field below the strip as well.
  python strip.py P H a b [--F f] [--time T] [--both]   (--both: walls at top and bottom, no field forced)"""
import sys, time
from ortools.sat.python import cp_model
from kx import cross, HALF
def build(P, H, a, b, F, both=False):
    ylo = 0 if both else -4                                  # virtual rows -4..-1 carry the field
    cells = [(x, y) for x in range(P) for y in range(ylo, H)]
    E = []                                                   # edges as (cell, cell2) with cell2 possibly outside [0,P)
    for (x, y) in cells:
        for dx, dy in HALF:
            if ylo <= y + dy < H: E.append(((x, y), (x + dx, y + dy)))
    def canon(c): return (c[0] % P, c[1])
    pairs = []
    for i, e in enumerate(E):
        for j in range(i + 1, len(E)):
            f = E[j]
            if abs(f[0][1] - e[0][1]) > 3: continue
            for k in (-2, -1, 0, 1, 2):
                g = ((f[0][0] + k * P, f[0][1]), (f[1][0] + k * P, f[1][1]))
                if cross(e, g): pairs.append((i, j)); break
    return cells, E, pairs, canon
def is_field(e, a, b):
    d = (e[1][0] - e[0][0], e[1][1] - e[0][1]); return d == (a, b) or d == (-a, -b)
def solve(P, H, a, b, F=4, both=False, tlim=120, workers=8, forbid=None, extra=None):
    cells, E, pairs, canon = build(P, H, a, b, F, both)
    M = cp_model.CpModel(); x = [M.NewBoolVar(f"x{k}") for k in range(len(E))]
    inc = {c: [] for c in cells}
    for k, (u, v) in enumerate(E): inc[u].append(k); inc[canon(v)].append(k)
    for c in cells:
        if not both and c[1] < F:                            # forced field
            for k in inc[c]: M.Add(x[k] == (1 if is_field(E[k], a, b) else 0))
        else: M.Add(sum(x[k] for k in inc[c]) == 2)
    cv = []
    for (i, j) in pairs:
        lo = min(E[i][0][1], E[i][1][1], E[j][0][1], E[j][1][1])
        if not both and lo < 0 and False: continue
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    M.Minimize(sum(cv))
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return S.StatusName(st), None, None, None
    used = [E[k] for k in range(len(E)) if S.Value(x[k])]
    return S.StatusName(st), int(S.ObjectiveValue()), S.BestObjectiveBound(), used
def show(P, H, used, a, b, ylo):
    """list the moves that are not field moves, by row"""
    non = sorted((e for e in used if not is_field(e, a, b)), key=lambda e: (-max(e[0][1], e[1][1]), e[0][0]))
    return " ".join(f"{u[0]},{u[1]}>{v[0]},{v[1]}" for u, v in non)
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--F", "--time")
    A = [s for k, s in enumerate(av) if not s.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda n, d: type(d)(av[av.index(n) + 1]) if n in av else d
    P, H, a, b = map(int, A[:4]); both = "--both" in av
    t0 = time.time(); st, val, bd, used = solve(P, H, a, b, opt("--F", 4), both, opt("--time", 120.0))
    print(f"P={P} H={H} field=({a},{b}) both={both}: {st} crossings/period={val} bound={bd} ({time.time()-t0:.0f}s)")
    if used and "--show" in av: print("non-field moves:", show(P, H, used, a, b, 0 if both else -4))
