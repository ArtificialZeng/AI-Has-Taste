"""Explicit pinched Sierpinski gasket S^_n(3) (Knuth's naming), profile evaluation of S_n - R, Stappers' construction."""
import itertools, random, sys
from gdp import PHI, typ, FORB, base, step
def canon(s):
    """Vertex names: strings over {0,1,2}; alpha a b^k == alpha b a^k (k >= 1). Normal form: the smaller string."""
    n = len(s); best = s
    for k in range(1, n):
        a, rest = s[n - k - 1], s[n - k:]
        if len(set(rest)) == 1 and rest[0] != a:
            b = rest[0]; t = s[:n - k - 1] + b + a * k; best = min(best, t)
    return best
def gasket(n):
    """Edges of S_n(3) as (prefix w of length n-1, i, j), i < j: the edge w i -- w j of the finest triangle w."""
    E = []
    for w in itertools.product("012", repeat=n - 1):
        w = "".join(w)
        for i, j in ((0, 1), (0, 2), (1, 2)): E.append((w, i, j))
    return E
def endpoints(e, n, pinch=True):
    w, i, j = e; u, v = canon(w + str(i)), canon(w + str(j))
    if pinch:
        if u == "1" * n: u = "0" * n
        if v == "1" * n: v = "0" * n
    return u, v
def profile(n, R):
    """Exact corner profile of S_n - R by the recursion (R = set of edges (w,i,j))."""
    tri = {}
    for w in itertools.product("012", repeat=n - 1):
        w = "".join(w); kept = [(i, j) for i, j in ((0, 1), (0, 2), (1, 2)) if (w, i, j) not in R]
        Q = 0
        for c in itertools.product(range(3), repeat=3):
            if all(c[i] != c[j] for i, j in kept): Q |= 1 << typ(*c)
        tri[w] = Q
    level = tri
    for d in range(n - 1, 0, -1):
        nxt = {}
        for w in itertools.product("012", repeat=d - 1):
            w = "".join(w); nxt[w] = PHI[level[w + "0"]][level[w + "1"]][level[w + "2"]]
        level = nxt
    return level[""]
def removable(n, R): return not profile(n, R) & FORB
def colorable_direct(n, R):
    """Direct backtracking 3-colouring of the pinched graph S^_n - R (independent of the profile machinery)."""
    E = [endpoints(e, n) for e in gasket(n) if e not in R]
    V = sorted({x for e in E for x in e} | {canon("".join(t)) for t in itertools.product("012", repeat=n)} - {"1" * n})
    idx = {v: k for k, v in enumerate(V)}; adj = [[] for _ in V]
    for u, v in E: adj[idx[u]].append(idx[v]); adj[idx[v]].append(idx[u])
    order = sorted(range(len(V)), key=lambda k: -len(adj[k])); col = [-1] * len(V)
    sys.setrecursionlimit(10000)
    def bt(p):
        if p == len(V): return True
        v = order[p]
        for c in range(3):
            if all(col[w] != c for w in adj[v]):
                col[v] = c
                if bt(p + 1): return True
                col[v] = -1
            if p == 0: break
        return False
    return bt(0)
def stappers(n):
    """Knuth's answer 227: sets of 2^(n-1)+1 removable edges (n >= 2). Non-tip edges as pairs of vertex strings."""
    tips = [e for e in gasket(n) if "2" * n in (canon(e[0] + str(e[1])), canon(e[0] + str(e[2])))]
    sets = [[("00", "01")], [("11", "10")]]       # n = 2: 00--01 or 11--01 (01 == 10)
    for m in range(3, n + 1):
        new = []
        for S in sets:
            base_edges = []
            for x, y in S:                        # x = alpha a, y = alpha b
                alpha, a, b = x[:-1], x[-1], y[-1]; c = ({"0", "1", "2"} - {a, b}).pop()
                base_edges += [(alpha + a + a, alpha + a + c), (alpha + b + b, alpha + b + c)]
            for extra in (("2" * (m - 2) + "00", "2" * (m - 2) + "01"), ("2" * (m - 2) + "11", "2" * (m - 2) + "10")):
                new.append(base_edges + [extra])
        sets = new
    out = []
    for S in sets:
        R = set(tips)
        for x, y in S:
            w = x[:-1]; assert y[:-1] == w
            i, j = sorted((int(x[-1]), int(y[-1]))); R.add((w, i, j))
        out.append(frozenset(R))
    return out
if __name__ == "__main__":
    random.seed(7)
    # (1) profile recursion vs direct colouring, random edge sets, n = 2, 3, 4
    for n in (2, 3, 4):
        G = gasket(n); bad = 0
        for t in range(400):
            k = random.randint(0, min(len(G), 12)); R = set(random.sample(G, k))
            if removable(n, R) == colorable_direct(n, R): bad += 1
        print(f"n={n}: profile recursion vs direct colouring on 400 random sets: disagreements {bad}")
    # (2) Stappers' sets
    for n in range(2, 13):
        S = stappers(n)
        ok = all(len(R) == 2 ** (n - 1) + 1 and removable(n, R) for R in S)
        print(f"n={n}: Stappers sets {len(S)}, distinct {len(set(S))}, all of size 2^(n-1)+1 and removable: {ok}")
    # Knuth's n = 4 example
    ex = [("0000", "0001"), ("0022", "0021"), ("0111", "0110"), ("0122", "0120"), ("2000", "2002"), ("2011", "2012"), ("2200", "2201"), ("2202", "2222"), ("2212", "2222")]
    R = set()
    for x, y in ex:
        found = [e for e in gasket(4) if {canon(e[0] + str(e[1])), canon(e[0] + str(e[2]))} == {canon(x), canon(y)}]
        assert len(found) == 1, (x, y, found); R.add(found[0])
    print("Knuth's n=4 example removable:", removable(4, R), "; it is one of Stappers' sets:", frozenset(R) in set(stappers(4)))
