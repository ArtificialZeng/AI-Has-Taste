"""Rings that replace one arc: a lower bound for the number of coils that such a ring adds.

Let T0, T1 be whirling knight's tours of sides N - 2w and N such that T1 contains every arc of T0 + (w,w) but one.
Then T1 has at least rho more coils than T0, where rho is the least number of disjoint paths that cover the ring cells
(depth < w) of a wedge of a quarter turn, the arcs being the arcs of the whirling digraph between these cells.
The wedge used here lies between two diagonals (turned slightly, so that no cell lies on its boundary): the left side.

The program computes rho by a maximum matching (Hopcroft-Karp) and turns the matching into a labelling of the cells
with B, N, O, I such that no arc leads from a cell labelled B or O to a cell labelled B or I (Koenig's theorem); then
|B| - |N| = rho.  It checks both certificates directly, so the result does not depend on the matching code:
the labelling (which gives rho >= |B| - |N|) and the matched arcs, which must be a cover of the cells by exactly
|B| - |N| disjoint paths (which gives rho <= |B| - |N|).
  python3 ring_bound.py [w] [Nmax]     default: w = 12 and every N from 2w+3 = 27 to 1003, by N mod 4
  python3 ring_bound.py w N --show     one board, with the labelling
  python3 ring_bound.py --table        widths 2..24 and 4w+3 <= N <= 403
Standard library only."""
import sys
from collections import deque
MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
def wedge_cells(N, w):
    """ring cells whose direction from the pivot lies strictly between lo and hi = lo turned by a quarter turn"""
    lo = (-(2 * N + 1), -(2 * N - 3)); hi = (-lo[1], lo[0])
    out = []
    for i in range(N):
        for j in range(N):
            if min(i, j, N - 1 - i, N - 1 - j) >= w: continue
            x, y = 2 * i - (N - 1), 2 * j - (N - 1)
            if lo[0] * y - x * lo[1] > 0 and x * hi[1] - hi[0] * y > 0: out.append((i, j))
    return out
def arcs_of(N, cells):
    idx = {c: k for k, c in enumerate(cells)}; adj = [[] for _ in cells]
    for (i, j), k in idx.items():
        x, y = 2 * i - (N - 1), 2 * j - (N - 1)
        for a, b in MOVES:
            c2 = (i + a, j + b)
            if c2 in idx and x * (2 * c2[1] - (N - 1)) - (2 * c2[0] - (N - 1)) * y > 0: adj[k].append(idx[c2])
    return adj
def hopcroft_karp(adj, n):
    """Maximum matching of the bipartite graph (out-copies, in-copies); ml[u] = v, mr[v] = u."""
    INF = n + 5; ml = [-1] * n; mr = [-1] * n
    while True:
        dist = [INF] * n; dq = deque()
        for u in range(n):
            if ml[u] < 0: dist[u] = 0; dq.append(u)
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                u2 = mr[v]
                if u2 < 0: found = True
                elif dist[u2] == INF: dist[u2] = dist[u] + 1; dq.append(u2)
        if not found: return ml, mr
        ptr = [0] * n; via = [-1] * n
        for root in range(n):
            if ml[root] >= 0: continue
            stack = [root]
            while stack:
                u = stack[-1]
                if ptr[u] < len(adj[u]):
                    v = adj[u][ptr[u]]; ptr[u] += 1; u2 = mr[v]
                    if u2 < 0:                                   # augment along the stack
                        via[u] = v
                        for x in stack: ml[x] = via[x]; mr[via[x]] = x
                        break
                    if dist[u2] == dist[u] + 1: via[u] = v; stack.append(u2)
                else:
                    dist[u] = INF; stack.pop()
def labelling(adj, n):
    """Koenig: Z = left vertices reachable from free left vertices by alternating paths; cover = (L - Z) + (R in Z)."""
    ml, mr = hopcroft_karp(adj, n)
    zl = [ml[u] < 0 for u in range(n)]; zr = [False] * n; dq = deque(u for u in range(n) if zl[u])
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if not zr[v]:
                zr[v] = True
                u2 = mr[v]
                if u2 >= 0 and not zl[u2]: zl[u2] = True; dq.append(u2)
    lab = []
    for k in range(n):
        out_cov, in_cov = not zl[k], zr[k]          # the out-copy / the in-copy of the cell is in the cover
        lab.append("N" if out_cov and in_cov else "I" if out_cov else "O" if in_cov else "B")
    return lab, ml
def check(adj, lab):
    """no arc from a cell labelled B or O to a cell labelled B or I"""
    return all(not (lab[u] in "BO" and lab[v] in "BI") for u in range(len(adj)) for v in adj[u])
def paths_of(adj, ml):
    """the number of paths if the matched arcs u -> ml[u] are a cover of all cells by disjoint paths, else None"""
    n = len(adj); pred = [-1] * n
    for u in range(n):
        v = ml[u]
        if v < 0: continue
        if v not in adj[u] or pred[v] >= 0: return None          # not an arc, or two arcs into one cell
        pred[v] = u
    seen = 0; paths = 0
    for u in range(n):
        if pred[u] >= 0: continue
        paths += 1
        while u >= 0: seen += 1; u = ml[u]
    return paths if seen == n else None                          # seen < n would mean a cycle
def rho(N, w, show=False):
    cells = wedge_cells(N, w); adj = arcs_of(N, cells); lab, ml = labelling(adj, len(cells))
    assert check(adj, lab), "the labelling is not valid"
    r = lab.count("B") - lab.count("N")
    assert paths_of(adj, ml) == r, "the matched arcs are not a cover by |B| - |N| paths"
    if show:
        d = dict(zip(cells, lab))
        for i in range(N):
            row = "".join(d.get((i, j), ".") for j in range(N))
            if set(row) != {"."}: print(f"{i:4d} {row.rstrip('.')}")
    return r
if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    w = int(args[0]) if args else 12
    if "--show" in sys.argv:
        N = int(args[1]); print(f"N={N}, w={w}: rho = {rho(N, w, True)}"); sys.exit(0)
    if "--table" in sys.argv:                    # widths 2..24, 4w+3 <= N <= 403: the values of rho by N mod 4
        for w in range(2, 25):
            by = {}
            for N in range(4 * w + 3, 404): by.setdefault(N % 4, set()).add(rho(N, w))
            print(f"w={w}: " + ", ".join(f"N = {k} (mod 4): {sorted(v)}" for k, v in sorted(by.items())), flush=True)
        sys.exit(0)
    Nmax = int(args[1]) if len(args) > 1 else 1003
    vals = {N: rho(N, w) for N in range(2 * w + 3, Nmax + 1)}
    for k in range(4):
        s = sorted({v for N, v in vals.items() if N % 4 == k})
        print(f"w={w}, N = {k} (mod 4), {2 * w + 3} <= N <= {Nmax}: rho takes the values {s}")
