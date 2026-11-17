"""Ex. 233 with precomputed conflict pairs: a pair {e,f} of L(J_q)-edges is a conflict if L - {e,f} is 3-colorable.
Valid R contains no conflict pair; then CEGAR on the remaining colorings. Colorability via ./color3 (backtracking)."""
import sys, itertools, subprocess, time
from ortools.sat.python import cp_model
from snark import flower, line_graph
class Col:
    def __init__(self, nv, LE):
        self.p = subprocess.Popen(["./color3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        self.p.stdin.write(f"{nv} {len(LE)}\n" + "".join(f"{u} {v}\n" for u, v in LE)); self.p.stdin.flush()
    def colorable(self, R):
        self.p.stdin.write(f"{len(R)} " + " ".join(map(str, R)) + "\n"); self.p.stdin.flush()
        return self.p.stdout.readline().strip() == "1"
def coloring(nv, edges):
    md = cp_model.CpModel(); x = [md.NewIntVar(0, 2, "") for _ in range(nv)]
    for u, v in edges: md.Add(x[u] != x[v])
    sv = cp_model.CpSolver(); sv.parameters.num_workers = 8; st = sv.Solve(md)
    return [sv.Value(v) for v in x] if st in (cp_model.OPTIMAL, cp_model.FEASIBLE) else None
def solve(q):
    E = flower(q); LE = line_graph(E); nv, ne = len(E), len(LE)
    C = Col(nv, LE); t0 = time.time()
    assert not C.colorable([])
    single = [e for e in range(ne) if C.colorable([e])]
    pairs = [(a, b) for a, b in itertools.combinations(range(ne), 2) if C.colorable([a, b])]
    print(f"q={q}: ne={ne}, single-edge conflicts {len(single)}, conflict pairs {len(pairs)} ({time.time()-t0:.1f}s)", flush=True)
    cuts = [[a, b] for a, b in pairs]; it = 0
    while True:
        it += 1
        md = cp_model.CpModel(); y = [md.NewBoolVar("") for _ in range(ne)]
        for e in single: md.Add(y[e] == 0)
        for Cc in cuts: md.AddBoolOr([y[e].Not() for e in Cc])
        md.Maximize(sum(y))
        sv = cp_model.CpSolver(); sv.parameters.num_workers = 8; sv.parameters.max_time_in_seconds = 900
        st = sv.Solve(md); assert st == cp_model.OPTIMAL, sv.StatusName(st)
        R = [e for e in range(ne) if sv.Value(y[e])]
        if not C.colorable(R):
            print(f"q={q}: max removable = {len(R)} (master iterations {it}, {time.time()-t0:.1f}s)", flush=True)
            return len(R), R, E, LE
        Rs = set(R); c = coloring(nv, [LE[e] for e in range(ne) if e not in Rs])
        cuts.append([e for e in range(ne) if c[LE[e][0]] == c[LE[e][1]]])
        if it % 20 == 0: print(f"  it={it} bound={len(R)}", flush=True)
if __name__ == "__main__":
    for q in map(int, sys.argv[1:]):
        k, R, E, LE = solve(q)
        print("  removed:", [(E[LE[e][0]], E[LE[e][1]]) for e in R], flush=True)
