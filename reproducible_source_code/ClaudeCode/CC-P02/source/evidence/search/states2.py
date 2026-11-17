"""Patterns of a wall under a field (a, b) (wall at the top row H-1, period P, rows < F forced): enumerate those with
at most maxcost crossings per period and classify them by the matching of the strands.
Strand index: k = b*x - a*y (constant along the field).  python states2.py a b P H maxcost [--F f] [--limit N]"""
import sys, time
from ortools.sat.python import cp_model
from kx import cross, HALF
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
def matching(P, H, F, used, fld):
    a, b = fld; adj = {}
    for (u, v) in used:
        d = (v[0] - u[0], v[1] - u[1])
        adj.setdefault(u, []).append(d); adj.setdefault((v[0] % P, v[1]), []).append((-d[0], -d[1]))
    res = {}; visited = set()
    for x0 in range(P):
        for y0 in range(F, F + b):                         # entry cells: the field predecessor (x0-a, y0-b) is forced
            k = b * x0 - a * y0; cur = (x0, y0); prev = fld
            while True:
                visited.add((cur[0] % P, cur[1]))
                ds = adj[(cur[0] % P, cur[1])]; back = (-prev[0], -prev[1])
                nxt = [d for d in ds if d != back]
                if len(ds) != 2 or len(nxt) != 1: return None
                d = nxt[0]; cur = (cur[0] + d[0], cur[1] + d[1]); prev = d
                if cur[1] < F:
                    if d != (-a, -b): return None
                    res[k] = b * cur[0] - a * cur[1] - k; break
    if len(visited) != P * (H - F): return None
    return res
class Collector(cp_model.CpSolverSolutionCallback):
    def __init__(self, x, E, cv, P, H, F, fld, limit):
        super().__init__(); self.x, self.E, self.cv, self.P, self.H, self.F, self.fld = x, E, cv, P, H, F, fld
        self.found = {}; self.n = 0; self.limit = limit
    def on_solution_callback(self):
        self.n += 1
        used = [self.E[k] for k in range(len(self.E)) if self.Value(self.x[k])]
        cost = sum(self.Value(c) for c in self.cv)
        m = matching(self.P, self.H, self.F, used, self.fld)
        mod = self.fld[1] * self.P
        key = None if m is None else tuple(sorted((k % mod, d) for k, d in m.items()))
        if key not in self.found or cost < self.found[key][0]: self.found[key] = (cost, used)
        if self.n >= self.limit: self.StopSearch()
def enumerate_states(fld, P, H, maxcost, F=4, limit=300000, tl=600, mincost=0):
    cells, E, pairs = build(P, H); canon = lambda c: (c[0] % P, c[1])
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    inc = {c: [] for c in cells}
    for k, (u, v) in enumerate(E): inc[u].append(k); inc[canon(v)].append(k)
    for c in cells:
        if c[1] < F:
            for k in inc[c]:
                d = (E[k][1][0] - E[k][0][0], E[k][1][1] - E[k][0][1]); M.Add(x[k] == (1 if d == fld else 0))
        else: M.Add(sum(x[k] for k in inc[c]) == 2)
    cv = []
    for (i, j) in pairs:
        c = M.NewBoolVar(""); M.AddBoolOr([x[i].Not(), x[j].Not(), c]); M.AddBoolOr([x[i], c.Not()]); M.AddBoolOr([x[j], c.Not()]); cv.append(c)
    M.Add(sum(cv) <= maxcost); M.Add(sum(cv) >= mincost)
    S = cp_model.CpSolver(); S.parameters.enumerate_all_solutions = True; S.parameters.max_time_in_seconds = tl; S.parameters.num_workers = 1
    cb = Collector(x, E, cv, P, H, F, fld, limit); S.Solve(M, cb)
    return cb
def show_nonfield(used, fld):
    nf = sorted((e for e in used if (e[1][0] - e[0][0], e[1][1] - e[0][1]) != fld), key=lambda e: (-max(e[0][1], e[1][1]), e[0][0]))
    return " ".join(f"{u[0]},{u[1]}>{v[0]},{v[1]}" for u, v in nf)
if __name__ == "__main__":
    av = sys.argv[1:]; OPTS = ("--F", "--limit")
    A = [a for k, a in enumerate(av) if not a.startswith("--") and not (k > 0 and av[k - 1] in OPTS)]
    opt = lambda nm, d: type(d)(av[av.index(nm) + 1]) if nm in av else d
    fld = (int(A[0]), int(A[1])); P, H, maxcost = int(A[2]), int(A[3]), int(A[4]); F = opt("--F", 4)
    t0 = time.time(); cb = enumerate_states(fld, P, H, maxcost, F, opt("--limit", 300000))
    print(f"field {fld} P={P} H={H} F={F} cost<={maxcost}: {cb.n} patterns, {len(cb.found)} distinct matchings ({time.time()-t0:.0f}s)")
    for key, (cost, used) in sorted(cb.found.items(), key=lambda t: (t[1][0], str(t[0])))[:40]:
        if key is None: print(f"  cost {cost}: (closed cycle or irregular)"); continue
        print(f"  cost {cost}: offsets {sorted(set(d for _, d in key))}  matching {dict(key)}")
        if "--show" in av: print("       ", show_nonfield(used, fld))
