"""Steep-wall patterns that carry colour: periodic strip (period P, wall at the top row H-1, field (1,2) forced in
the rows y < F).  For a cut between the columns 1 and 2 let Psi = sum over the used moves across the cut of the
colour (+1 if x+y is even, -1 if odd) of the end on the right.  J = Psi - Psi(pattern A).  We minimise the crossings
per period for a given J.      python flux.py P H J [--F f] [--time T] [--show]"""
import sys, time
from ortools.sat.python import cp_model
from kx import cross, HALF
FLD = (1, 2)
def build(P, H):
    cells = [(x, y) for x in range(P) for y in range(H)]
    E = []
    for u in cells:
        for d in HALF:
            v = (u[0] + d[0], u[1] + d[1])
            if 0 <= v[1] < H: E.append((u, v))
    pairs = []
    for i, e in enumerate(E):
        for j in range(i + 1, len(E)):
            f = E[j]
            if abs(f[0][1] - e[0][1]) > 3: continue
            for k in (-2, -1, 0, 1, 2):
                if cross(e, ((f[0][0] + k * P, f[0][1]), (f[1][0] + k * P, f[1][1]))): pairs.append((i, j)); break
    return cells, E, pairs
def chi(c): return 1 if (c[0] + c[1]) % 2 == 0 else -1
def psi_coeff(e, c0=2):
    """coefficient of the move e in Psi for the cut between the columns c0-1 and c0"""
    (u, v) = e
    if u[0] < c0 <= v[0]: return chi(v)
    if v[0] < c0 <= u[0]: return chi(u)
    return 0
def pattern_A(P, H, E):
    used = set()
    for k, (u, v) in enumerate(E):
        d = (v[0] - u[0], v[1] - u[1])
        if d == FLD: used.add(k)
        if d == (2, 1) and u[1] == H - 2: used.add(k)
    return used
def solve(P, H, J, F=4, tlim=120, workers=8, forbidA=False, extra=None):
    cells, E, pairs = build(P, H); canon = lambda c: (c[0] % P, c[1])
    psiA = sum(psi_coeff(E[k]) for k in pattern_A(P, H, E))
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    inc = {c: [] for c in cells}
    for k, (u, v) in enumerate(E): inc[u].append(k); inc[canon(v)].append(k)
    for c in cells:
        if c[1] < F:
            for k in inc[c]:
                d = (E[k][1][0] - E[k][0][0], E[k][1][1] - E[k][0][1]); M.Add(x[k] == (1 if d == FLD else 0))
        else: M.Add(sum(x[k] for k in inc[c]) == 2)
    if J is not None: M.Add(sum(psi_coeff(E[k]) * x[k] for k in range(len(E))) == psiA + J)
    if extra: extra(M, x, E)
    cv = []
    for (i, j) in pairs:
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); cv.append(c)
    M.Minimize(sum(cv))
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M); name = S.StatusName(st)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None, None
    return name, int(S.ObjectiveValue()), [E[k] for k in range(len(E)) if S.Value(x[k])]
def nonfield(used):
    nf = sorted((e for e in used if (e[1][0] - e[0][0], e[1][1] - e[0][1]) != FLD), key=lambda e: (-max(e[0][1], e[1][1]), e[0][0]))
    return " ".join(f"{u[0]},{u[1]}>{v[0]},{v[1]}" for u, v in nf)
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--F", "--time")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    P, H = int(A[0]), int(A[1]); Js = [int(A[2])] if len(A) > 2 else [-2, -1, 0, 1, 2]
    for J in Js:
        t0 = time.time(); name, val, used = solve(P, H, J, opt("--F", 4), opt("--time", 120.0))
        print(f"P={P} H={H} F={opt('--F',4)} J={J}: {name} crossings/period={val}" + (f" = {val/P:.3f} per column" if val is not None else "") + f" ({time.time()-t0:.0f}s)", flush=True)
        if used and "--show" in av: print("   non-field moves:", nonfield(used))
