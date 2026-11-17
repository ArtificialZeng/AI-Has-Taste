"""Cross-checks: (1) profile recursion vs direct 3-colouring (C backtracking) of the explicit pinched gasket minus R;
(2) exhaustive largest removable sets for n = 2, 3, 4 by monotone search with direct colouring;
(3) Stappers' sets: distinct, size 2^(n-1)+1, removable (profile recursion), n = 2..12; Knuth's n = 4 example."""
import itertools, random, subprocess
from explicit import gasket, endpoints, canon, removable, stappers
class Col:
    def __init__(self, n):
        self.E = gasket(n); ends = [endpoints(e, n) for e in self.E]
        V = sorted({x for e in ends for x in e}); self.idx = {v: k for k, v in enumerate(V)}
        self.p = subprocess.Popen(["./color3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        self.p.stdin.write(f"{len(V)} {len(ends)}\n" + "".join(f"{self.idx[u]} {self.idx[v]}\n" for u, v in ends)); self.p.stdin.flush()
        self.eid = {e: k for k, e in enumerate(self.E)}
    def colorable(self, R):
        ids = [self.eid[e] for e in R]
        self.p.stdin.write(f"{len(ids)} " + " ".join(map(str, ids)) + "\n"); self.p.stdin.flush()
        return self.p.stdout.readline().strip() == "1"
random.seed(7)
for n in (2, 3, 4, 5):
    C = Col(n); G = C.E; bad = 0
    for t in range(1000):
        k = random.randint(0, min(len(G), 2 ** (n - 1) + 3)); R = set(random.sample(G, k))
        if removable(n, R) == C.colorable(R): bad += 1
    print(f"(1) n={n}: profile recursion vs direct colouring on 1000 random sets: disagreements {bad}", flush=True)
for n in (2, 3, 4):
    C = Col(n); G = C.E; best, sets = 0, []
    def dfs(start, R):
        global best, sets
        if len(R) > best: best, sets = len(R), []
        if len(R) == best: sets.append(frozenset(R))
        for k in range(start, len(G)):
            R2 = R + [G[k]]
            if not C.colorable(R2): dfs(k + 1, R2)
    dfs(0, [])
    st = set(stappers(n))
    print(f"(2) n={n}: largest removable set {best} edges, {len(sets)} sets; equal to Stappers' sets: {set(sets) == st}", flush=True)
for n in range(2, 13):
    S = stappers(n)
    ok = all(len(R) == 2 ** (n - 1) + 1 and removable(n, R) for R in S)
    print(f"(3) n={n}: Stappers sets {len(S)}, distinct {len(set(S))}, size 2^(n-1)+1 and removable: {ok}", flush=True)
ex = [("0000", "0001"), ("0022", "0021"), ("0111", "0110"), ("0122", "0120"), ("2000", "2002"), ("2011", "2012"), ("2200", "2201"), ("2202", "2222"), ("2212", "2222")]
R = set()
for x, y in ex:
    found = [e for e in gasket(4) if {canon(e[0] + str(e[1])), canon(e[0] + str(e[2]))} == {canon(x), canon(y)}]
    assert len(found) == 1, (x, y, found); R.add(found[0])
print("(3) Knuth's n=4 example: removable", removable(4, R), "; one of Stappers' sets:", frozenset(R) in set(stappers(4)))
