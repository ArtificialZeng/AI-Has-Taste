"""Exact DP for TAOCP 7.2.2.3-227: largest removable edge sets of the pinched Sierpinski gasket S^_n(3).
S_n = three copies of S_{n-1} (prefixes 0,1,2) glued: copy i's local corner j = copy j's local corner i.
Profile of a graph with three corners = set of corner colour patterns (up to colour permutation) of its 3-colourings:
type 0: c0=c1=c2; 1: c0=c1!=c2; 2: c0=c2!=c1; 3: c1=c2!=c0; 4: all distinct.  Profiles = subsets of {0..4} (bitmask).
For each exact profile Q keep (max number of removed edges, number of edge sets attaining it).
Pinched graph (corners 0^n and 1^n identified) is non-3-colourable iff the profile avoids types 0 and 1."""
import itertools, sys
def typ(a, b, c):
    if a == b == c: return 0
    if a == b: return 1
    if a == c: return 2
    if b == c: return 3
    return 4
# composition table: child types (t0,t1,t2) -> set of parent types
COMP = {}
for A, B, C, D, E, F in itertools.product(range(3), repeat=6):
    t0, t1, t2 = typ(A, D, E), typ(D, B, F), typ(E, F, C)     # child 0 sees (A,D,E), child 1 (D,B,F), child 2 (E,F,C)
    COMP.setdefault((t0, t1, t2), set()).add(typ(A, B, C))
def phi(Q0, Q1, Q2):
    out = 0
    for t0 in range(5):
        if not Q0 >> t0 & 1: continue
        for t1 in range(5):
            if not Q1 >> t1 & 1: continue
            for t2 in range(5):
                if not Q2 >> t2 & 1: continue
                for T in COMP.get((t0, t1, t2), ()): out |= 1 << T
    return out
PHI = [[[phi(a, b, c) for c in range(32)] for b in range(32)] for a in range(32)]
def base():
    """S_1 = triangle on corners 0,1,2; edges 01, 02, 12."""
    best = {}
    edges = [(0, 1), (0, 2), (1, 2)]
    for k in range(4):
        for R in itertools.combinations(range(3), k):
            kept = [edges[e] for e in range(3) if e not in R]
            Q = 0
            for c in itertools.product(range(3), repeat=3):
                if all(c[i] != c[j] for i, j in kept): Q |= 1 << typ(*c)
            m, n = best.get(Q, (-1, 0))
            if k > m: best[Q] = (k, 1)
            elif k == m: best[Q] = (m, n + 1)
    return best
def step(prev):
    new = {}
    items = list(prev.items())
    for Q0, (m0, n0) in items:
        for Q1, (m1, n1) in items:
            for Q2, (m2, n2) in items:
                Q = PHI[Q0][Q1][Q2]; m = m0 + m1 + m2; c = n0 * n1 * n2
                om, oc = new.get(Q, (-1, 0))
                if m > om: new[Q] = (m, c)
                elif m == om: new[Q] = (m, oc + c)
    return new
FORB = (1 << 0) | (1 << 1)
if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    cur = base()
    for n in range(1, N + 1):
        if n > 1: cur = step(cur)
        cands = [(m, c, Q) for Q, (m, c) in cur.items() if not Q & FORB]
        M = max(m for m, c, Q in cands); C = sum(c for m, c, Q in cands if m == M)
        print(f"n={n}: profiles {len(cur)}; largest removable set {M} (2^(n-1)+1 = {2**(n-1)+1}); number of largest sets {C} (2^(n-1) = {2**(n-1)})", flush=True)
