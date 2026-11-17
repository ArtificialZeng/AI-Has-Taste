"""Stretch a tour whose wall layers are periodic: insert D columns and D rows at the middle of the board.
The cell (x', y') of the new board copies the moves of the cell (x, y) of the old board, where x = x' for x' < h,
x = x' - D for x' >= h + D, and for h <= x' < h + D, x = x' - P*j with the least j that gives x < h (h = n/2);
the same for y.  This is consistent if the old tour is invariant under the translations by P in the wall layers
around the middle of each wall and follows the field (1,2) in the interior.
  python stretch.py tourfile n P D [D2 ...]"""
import sys
from kx import crossing_pairs
def load(fn): return [tuple(tuple(int(v) for v in c.split(",")) for c in t.split("-")) for t in open(fn).read().split()]
def moves_of(used):
    mv = {}
    for a, b in used:
        mv.setdefault(a, set()).add((b[0] - a[0], b[1] - a[1])); mv.setdefault(b, set()).add((a[0] - b[0], a[1] - b[1]))
    return mv
def stretch(used, n, P, D):
    h = n // 2; mv = moves_of(used); N = n + D
    def back(t):
        if t < h: return t
        if t >= h + D: return t - D
        j = (t - h) // P + 1
        return t - P * j
    new = set(); bad = 0
    for X in range(N):
        for Y in range(N):
            for d in mv[(back(X), back(Y))]:
                X2, Y2 = X + d[0], Y + d[1]
                if not (0 <= X2 < N and 0 <= Y2 < N): bad += 1; continue
                new.add(frozenset(((X, Y), (X2, Y2))))
    # consistency: every cell has degree 2
    deg = {}
    for e in new:
        for c in e: deg[c] = deg.get(c, 0) + 1
    bad += sum(1 for X in range(N) for Y in range(N) if deg.get((X, Y), 0) != 2)
    return [tuple(e) for e in new], bad
def cycles(edges):
    adj = {}
    for a, b in edges: adj.setdefault(a, []).append(b); adj.setdefault(b, []).append(a)
    seen = set(); lens = []
    for c in adj:
        if c in seen: continue
        st = [c]; k = 0
        while st:
            u = st.pop()
            if u in seen: continue
            seen.add(u); k += 1; st.extend(adj[u])
        lens.append(k)
    return sorted(lens, reverse=True)
if __name__ == "__main__":
    fn, n, P = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    used = load(fn); base = len(crossing_pairs(used))
    print(f"n={n}: cycles {cycles(used)[:4]}, crossings {base}")
    for D in map(int, sys.argv[4:]):
        new, bad = stretch(used, n, P, D)
        cyc = cycles(new); cr = len(crossing_pairs(new))
        print(f"n={n+D}: inconsistent cells {bad}, cycles {len(cyc)} (largest {cyc[:3]}), crossings {cr} = {cr/(n+D):.2f} n, slope {(cr-base)/D:.2f}", flush=True)
