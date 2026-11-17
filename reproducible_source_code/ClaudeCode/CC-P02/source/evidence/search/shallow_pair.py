"""Cheapest pattern of the shallow wall (field (2,1), wall on top, period P) that pairs with a given pattern of the
steep wall at the other end of the strands.  The steep pattern joins strand k to strand k + off (for k in one parity
class): A has off = 3, B has off = -5.  Here this is a link between the lowest cells (x, 0) and (x + off, 0) of the
strip, for x = c (mod 2).  We ask for one cycle in the quotient with total x-displacement w*P and minimise crossings.
  python shallow_pair.py P H off c w [--F f] [--time T]"""
import sys, time
from ortools.sat.python import cp_model
from kx import cross, HALF
FLD = (2, 1)
def run(P, H, off, c, w, F=4, tlim=120, workers=8):
    cells = [(x, y) for x in range(P) for y in range(H)]; idx = {cc: k for k, cc in enumerate(cells)}
    canon = lambda cc: (cc[0] % P, cc[1])
    E = []
    for u in cells:
        for d in HALF:
            v = (u[0] + d[0], u[1] + d[1])
            if 0 <= v[1] < H: E.append((u, v, d))
    pairs = []
    for i, e in enumerate(E):
        for j in range(i + 1, len(E)):
            f = E[j]
            if abs(f[0][1] - e[0][1]) > 3: continue
            for k in (-2, -1, 0, 1, 2):
                if cross((e[0], e[1]), ((f[0][0] + k * P, f[0][1]), (f[1][0] + k * P, f[1][1]))): pairs.append((i, j)); break
    M = cp_model.CpModel(); arcs = []; disp = []; xs = []
    for k, (u, v, d) in enumerate(E):
        fw = M.NewBoolVar(""); bw = M.NewBoolVar(""); x = M.NewBoolVar(""); xs.append(x); M.Add(fw + bw == x)
        arcs.append((idx[u], idx[canon(v)], fw)); arcs.append((idx[canon(v)], idx[u], bw))
        disp.append((d[0], fw)); disp.append((-d[0], bw))
        if u[1] < F or v[1] < F: M.Add(x == (1 if d == FLD else 0))
    for x0 in range(P):
        if x0 % 2 != c % 2: continue
        a = M.NewBoolVar(""); b = M.NewBoolVar(""); M.Add(a + b == 1)
        arcs.append((idx[(x0, 0)], idx[((x0 + off) % P, 0)], a)); arcs.append((idx[((x0 + off) % P, 0)], idx[(x0, 0)], b))
        disp.append((off, a)); disp.append((-off, b))
    M.AddCircuit(arcs)
    M.Add(sum(dx * v for dx, v in disp) == w * P)
    cost = []
    for (i, j) in pairs:
        cc = M.NewBoolVar(""); M.AddBoolOr([xs[i].Not(), xs[j].Not(), cc]); cost.append(cc)
    M.Minimize(sum(cost))
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tlim; S.parameters.num_workers = workers
    st = S.Solve(M); name = S.StatusName(st)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return name, None
    return name, int(S.ObjectiveValue())
if __name__ == "__main__":
    av = sys.argv[1:]
    if av[0] == "scan":
        for P in map(int, av[1].split(",")):
            for off, nm in ((3, "A"), (-5, "B")):
                best = None
                for c in (0, 1):
                    for w in (-6, -4, -2, 2, 4, 6):
                        name, val = run(P, 10, off, c, w, tlim=float(av[2]))
                        if val is not None and (best is None or val < best[0]): best = (val, c, w, name)
                print(f"period {P}, steep pattern {nm}: best {best}" + (f" = {best[0]/P:.3f} per row" if best else ""), flush=True)
    else:
        P, H, off, c, w = map(int, av[:5]); print(run(P, H, off, c, w))
