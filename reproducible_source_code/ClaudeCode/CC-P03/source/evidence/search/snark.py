"""TAOCP 7.2.2.3 ex. 233: largest set R of edges of the flower snark line graph L(J_q) (q odd) such that
L(J_q) - R is still not 3-colorable.  CEGAR: master CP-SAT maximizes |R| subject to cuts
'mono(c) is not inside R' for colorings c found so far; slave CP-SAT 3-colors L - R."""
import sys, itertools, time
from ortools.sat.python import cp_model
def flower(q):
    """J_q: centers a_i, petals b_i, c_i, d_i; b's form a q-cycle; c's and d's form one 2q-cycle (twisted)."""
    E = []
    for i in range(q):
        E += [(("a", i), ("b", i)), (("a", i), ("c", i)), (("a", i), ("d", i))]
        E.append((("b", i), ("b", (i + 1) % q)))
        if i < q - 1: E += [(("c", i), ("c", i + 1)), (("d", i), ("d", i + 1))]
    E += [(("c", q - 1), ("d", 0)), (("d", q - 1), ("c", 0))]
    return E
def line_graph(E):
    inc = {}
    for k, (u, v) in enumerate(E):
        inc.setdefault(u, []).append(k); inc.setdefault(v, []).append(k)
    LE = set()
    for v, ks in inc.items():
        assert len(ks) == 3
        for x, y in itertools.combinations(sorted(ks), 2): LE.add((x, y))
    return sorted(LE)
def color(nv, edges, tl=60):
    md = cp_model.CpModel(); x = [md.NewIntVar(0, 2, "") for _ in range(nv)]
    for u, v in edges: md.Add(x[u] != x[v])
    md.Add(x[0] == 0)
    sv = cp_model.CpSolver(); sv.parameters.max_time_in_seconds = tl; sv.parameters.num_workers = 8
    st = sv.Solve(md)
    if st in (cp_model.OPTIMAL, cp_model.FEASIBLE): return [sv.Value(v) for v in x]
    assert st == cp_model.INFEASIBLE, sv.StatusName(st)
    return None
def solve(q, verbose=True):
    E = flower(q); LE = line_graph(E); nv = len(E); ne = len(LE)
    assert color(nv, LE) is None
    cuts = []
    t0 = time.time(); it = 0
    while True:
        it += 1
        md = cp_model.CpModel(); y = [md.NewBoolVar("") for _ in range(ne)]
        for C in cuts: md.AddBoolOr([y[e].Not() for e in C])
        md.Maximize(sum(y))
        sv = cp_model.CpSolver(); sv.parameters.max_time_in_seconds = 600; sv.parameters.num_workers = 8
        st = sv.Solve(md); assert st == cp_model.OPTIMAL, sv.StatusName(st)
        R = [e for e in range(ne) if sv.Value(y[e])]
        Rs = set(R)
        c = color(nv, [LE[e] for e in range(ne) if e not in Rs])
        if c is None:
            if verbose: print(f"q={q}: max removable = {len(R)} (iterations {it}, {time.time()-t0:.1f}s)", flush=True)
            return len(R), [LE[e] for e in R], E
        mono = [e for e in range(ne) if c[LE[e][0]] == c[LE[e][1]]]
        assert set(mono) <= Rs
        cuts.append(mono)
        if verbose and it % 50 == 0: print(f"  q={q} it={it} bound={len(R)} cuts={len(cuts)}", flush=True)
if __name__ == "__main__":
    for q in map(int, sys.argv[1:]):
        k, R, E = solve(q)
        print("  removed (as pairs of J_q edges):", [(E[a], E[b]) for a, b in R], flush=True)
