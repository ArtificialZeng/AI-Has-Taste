import sys
from sb2 import gadget_edges
from starburst import field_edges
from kx import edges_of
from ortools.sat.python import cp_model
def diag(n, mc, mm, dc, dm, R, states="ABABABAB", tl=60, offs=None, seams=None):
    cells = [(i, j) for i in range(n) for j in range(n)]
    FE = field_edges(n, offs, seams); G, reg = gadget_edges(n, states, mc, mm)
    def free(c):
        if c in reg: return False
        i, j = c; X, Y = 2*i-(n-1), 2*j-(n-1); dep = min(i, j, n-1-i, n-1-j)
        if abs(X) <= R and abs(Y) <= R: return True
        if dep < 2: return True
        a = min(i, n-1-i); b = min(j, n-1-j)
        if max(a, b) < mc and min(a, b) < dc: return True
        along = min(abs(X), abs(Y)) // 2
        if dep < dm and along < mm: return True
        return False
    E = []; forced = set()
    for e in edges_of(cells):
        fe = frozenset(e); fr = (free(e[0]), free(e[1]))
        if fe in G: E.append(e); forced.add(len(E) - 1)
        elif fe in FE:
            E.append(e)
            if not (fr[0] and fr[1]): forced.add(len(E) - 1)
        elif fr[0] and fr[1]: E.append(e)
    M = cp_model.CpModel(); x = [M.NewBoolVar("") for _ in E]
    for k in forced: M.Add(x[k] == 1)
    inc = {c: [] for c in cells}
    for k, (a, b) in enumerate(E): inc[a].append(x[k]); inc[b].append(x[k])
    sl = {}
    for c in cells:
        if not free(c): M.Add(sum(inc[c]) == 2); continue
        p = M.NewIntVar(0, 4, ""); q = M.NewIntVar(0, 4, ""); sl[c] = (p, q)
        M.Add(sum(inc[c]) + p - q == 2)
    M.Minimize(sum(p + q for p, q in sl.values()))
    S = cp_model.CpSolver(); S.parameters.max_time_in_seconds = tl; S.parameters.num_workers = 8; st = S.Solve(M)
    if st not in (cp_model.OPTIMAL, cp_model.FEASIBLE): return S.StatusName(st), None
    h = n / 2
    def where(c):
        i, j = c; a = min(i, n-1-i); b = min(j, n-1-j)
        if max(a, b) < n / 4: return "corner " + ("T" if j > h else "B") + ("R" if i > h else "L")
        if min(a, b) < n / 4: return "mid " + ("T" if j >= n - n/4 else "B" if j < n/4 else "R" if i > h else "L")
        return "centre"
    v = {}
    for c, (p, q) in sl.items():
        d = S.Value(p) + S.Value(q)
        if d: v[where(c)] = v.get(where(c), 0) + d
    return S.ObjectiveValue(), v
if __name__ == "__main__":
    n = int(sys.argv[1])
    for (mc, mm, dc, dm, R) in [(6, 5, 5, 5, 7), (8, 6, 6, 6, 7), (8, 6, 6, 6, 11), (10, 8, 8, 8, 11)]:
        print((mc, mm, dc, dm, R), diag(n, mc, mm, dc, dm, R), flush=True)
