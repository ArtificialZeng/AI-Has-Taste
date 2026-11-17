#!/usr/bin/env python3
"""Verification program for: "How many edges can be removed from a flower snark line graph?"
(answer to Knuth, TAOCP exercise 7.2.2.3-233).  Python 3 standard library only.

Theorem. For odd q >= 5, at most 9 edges can be removed from L(J_q) so that the rest is still not 3-colorable, and
the 9-edge sets that work are exactly the 4q "claw sets": all edges of L(J_q) that touch the three line-vertices
belonging to one vertex of J_q.  For q = 3 the maximum is 15 (one set).

Usage:  python3 snark_check.py [all|model|period|pairs|window|small|claws]
"""
import itertools, sys
from functools import lru_cache

# ---------------------------------------------------------------- the graphs
def flower(q):
    """J_q: centres a_i, petals b_i, c_i, d_i (i mod q); b's form a q-cycle; c_0..c_{q-1} d_0..d_{q-1} one 2q-cycle."""
    E = []
    for i in range(q):
        E += [(("a", i), ("b", i)), (("a", i), ("c", i)), (("a", i), ("d", i)), (("b", i), ("b", (i + 1) % q))]
        if i < q - 1: E += [(("c", i), ("c", i + 1)), (("d", i), ("d", i + 1))]
    E += [(("c", q - 1), ("d", 0)), (("d", q - 1), ("c", 0))]
    return E
def line_graph(E):
    inc = {}
    for k, (u, v) in enumerate(E):
        inc.setdefault(u, []).append(k); inc.setdefault(v, []).append(k)
    assert all(len(ks) == 3 for ks in inc.values())          # J_q is cubic
    LE = sorted({(x, y) for ks in inc.values() for x, y in itertools.combinations(sorted(ks), 2)})
    return LE, inc
def three_colorable(nv, edges):
    """Plain backtracking (vertices in BFS order); returns True iff the graph is 3-colorable."""
    adj = [[] for _ in range(nv)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    order, seen = [], [False] * nv
    for s in range(nv):
        if seen[s]: continue
        seen[s] = True; order.append(s); h = len(order) - 1
        while h < len(order):
            v = order[h]; h += 1
            for w in adj[v]:
                if not seen[w]: seen[w] = True; order.append(w)
    col = [-1] * nv
    def bt(p):
        if p == nv: return True
        v = order[p]
        for c in range(3):
            if all(col[w] != c for w in adj[v]):
                col[v] = c
                if bt(p + 1): return True
                col[v] = -1
            if p == 0: break          # symmetry: first vertex gets color 0
        return False
    return bt(0)

def line_graph_any(E):
    """Line graph of any graph given by an edge list (vertices = edge indices)."""
    inc = {}
    for k, (u, v) in enumerate(E):
        inc.setdefault(u, []).append(k); inc.setdefault(v, []).append(k)
    return sorted({(x, y) for ks in inc.values() for x, y in itertools.combinations(sorted(ks), 2)}), inc

# ---------------------------------------------------------------- transfer matrices
# Unit i = {a_i, b_i, c_i, d_i}; spokes A = a_i b_i, B = a_i c_i, C = a_i d_i; right connectors X, Y, Z leave b_i, c_i, d_i
# (X = b_i b_{i+1}; Y = c_i c_{i+1}, Z = d_i d_{i+1}, except Y = c_{q-1} d_0 and Z = d_{q-1} c_0: the twist).
# State = colors (X, Y, Z) of the right connectors.  The 12 edges of L(J_q) at unit i get local numbers:
#   at a_i: 0 {A,B}  1 {A,C}  2 {B,C};  at b_i: 3 {XL,A}  4 {A,XR}  5 {XL,XR};
#   at c_i: 6 {YL,B} 7 {B,YR} 8 {YL,YR}; at d_i: 9 {ZL,C} 10 {C,ZR} 11 {ZL,ZR}   (L = left connector, R = right).
# Removing an edge of L(J_q) allows its two end edges of J_q to get the same color.
STATES = list(itertools.product(range(3), repeat=3)); IDX = {s: k for k, s in enumerate(STATES)}; NS = 27
@lru_cache(maxsize=None)
def unit(R=frozenset()):
    M = [0] * NS
    ok = lambda u, v, e: u != v or e in R
    for s in STATES:
        XL, YL, ZL = s
        for A, B, C in itertools.product(range(3), repeat=3):
            if not (ok(A, B, 0) and ok(A, C, 1) and ok(B, C, 2)): continue
            for t in STATES:
                XR, YR, ZR = t
                if (ok(XL, A, 3) and ok(A, XR, 4) and ok(XL, XR, 5) and ok(YL, B, 6) and ok(B, YR, 7) and ok(YL, YR, 8)
                        and ok(ZL, C, 9) and ok(C, ZR, 10) and ok(ZL, ZR, 11)):
                    M[IDX[s]] |= 1 << IDX[t]
    return tuple(M)
def mul(P, Q):
    out = []
    for row in P:
        acc, k = 0, 0
        while row:
            if row & 1: acc |= Q[k]
            row >>= 1; k += 1
        out.append(acc)
    return tuple(out)
I = tuple(1 << k for k in range(NS))
SW = tuple(1 << IDX[(s[0], s[2], s[1])] for s in STATES)   # left state of unit 0 = (X, Z, Y) of unit q-1
T = unit()
def power(M, k):
    out, B = I, M
    while k:
        if k & 1: out = mul(out, B)
        B = mul(B, B); k >>= 1
    return out
def trace_nonzero(P): return any((P[k] >> k) & 1 for k in range(NS))
def colorable_tm(q, R):
    """R = set of (unit, local index). True iff L(J_q) minus R is 3-colorable (transfer-matrix computation)."""
    d = {}
    for u, e in R: d.setdefault(u, set()).add(e)
    P = SW
    for i in range(q): P = mul(P, unit(frozenset(d[i])) if i in d else T)
    return trace_nonzero(P)
SIGMA = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5, 6: 9, 7: 10, 8: 11, 9: 6, 10: 7, 11: 8}   # c <-> d inside a unit

def local_index(q, E, inc, le):
    """Map an edge of L(J_q) (pair of J-edge indices) to (unit, local index)."""
    x, y = le; ex, ey = E[x], E[y]
    v = (set(ex) & set(ey)).pop(); kind, i = v
    def role(e):                       # role of J-edge e at vertex v
        w = e[0] if e[1] == v else e[1]
        if kind == "a": return {"b": "A", "c": "B", "d": "C"}[w[0]]
        if w[0] == "a": return {"b": "A", "c": "B", "d": "C"}[kind]
        # connector: right connector of unit i if it goes to unit i+1 (or wraps from q-1 to 0), else left
        return {"b": "X", "c": "Y", "d": "Z"}[kind] + ("R" if w[1] == (i + 1) % q and not (q == 1) else "L")
    ra, rb = sorted([role(ex), role(ey)])
    table = {"a": {("A", "B"): 0, ("A", "C"): 1, ("B", "C"): 2},
             "b": {("A", "XL"): 3, ("A", "XR"): 4, ("XL", "XR"): 5},
             "c": {("B", "YL"): 6, ("B", "YR"): 7, ("YL", "YR"): 8},
             "d": {("C", "ZL"): 9, ("C", "ZR"): 10, ("ZL", "ZR"): 11}}
    return (i, table[kind][(ra, rb)])

# ---------------------------------------------------------------- checks
def check_model(qs=(3, 5, 7)):
    """The transfer model agrees with direct 3-coloring of the explicit graph L(J_q) minus R for every R of size <= 2."""
    for q in qs:
        E = flower(q); LE, inc = line_graph(E)
        loc = [local_index(q, E, inc, le) for le in LE]
        assert len(set(loc)) == 12 * q, "local numbering must be a bijection"
        nv = len(E); bad = 0; n = 0
        for k in range(3):
            for R in itertools.combinations(range(len(LE)), k):
                Rs = set(R); direct = three_colorable(nv, [LE[e] for e in range(len(LE)) if e not in Rs])
                tm = colorable_tm(q, {loc[e] for e in R}); n += 1
                if direct != tm: bad += 1
        print(f"model q={q}: {n} edge sets of size <= 2 compared with direct coloring, disagreements: {bad}")
        assert bad == 0
def check_period():
    T2, T4 = power(T, 2), power(T, 4)
    print("T^2 == T^4:", T2 == T4, "  T == T^3:", T == power(T, 3))
    assert T2 == T4
    ok = all(mul(mul(SW, unit(frozenset(R))), SW) == unit(frozenset(SIGMA[e] for e in R))
             for k in range(13) for R in itertools.combinations(range(12), k))
    print("SW U(R) SW == U(sigma R) for all 4096 subsets R:", ok, "  SW T SW == T:", mul(mul(SW, T), SW) == T)
    assert ok
def rep(k): return k if k < 2 else 2 + k % 2          # T^k depends only on k mod 2 once k >= 2
def check_pairs():
    """For odd q >= 5: removing two edges of L(J_q) in units at cyclic distance >= 3 always makes it 3-colorable.
    Put the first edge in unit 0 (allowed by rotation, the twist moves by SW); the second is in unit delta; k1 = delta-1,
    k2 = q-1-delta, and T^k1, T^k2 depend only on rep(k).  All representative cases are checked."""
    worst = 0
    for k1 in range(4):
        for k2 in range(4):
            if (k1 + k2) % 2 == 0 or k1 + k2 + 2 < 5: continue
            A, B = power(T, k1), power(T, k2)
            for e in range(12):
                for f in range(12):
                    if not trace_nonzero(mul(mul(mul(mul(SW, unit(frozenset([e]))), A), unit(frozenset([f]))), B)):
                        worst = max(worst, min(k1, k2) + 1)
    print("largest cyclic unit distance of two removable edges that keep L(J_q) uncolorable:", worst)
    assert worst <= 2
def check_window():
    """For odd q >= 7 a removable set lies in 3 consecutive units (pairwise distances <= 2 and q > 6); rotate them to units
    0, 1, 2. Then removability means trace(SW D0 D1 D2 T^(q-3)) = 0 and T^(q-3) = T^2. Enumerate all removable sets."""
    T2 = power(T, 2); L = [(u, e) for u in range(3) for e in range(12)]
    def removable(R):
        D = [unit(frozenset(e for u, e in R if u == i)) for i in range(3)]
        return not trace_nonzero(mul(mul(mul(mul(SW, D[0]), D[1]), D[2]), T2))
    count, best, opt = {}, 0, []
    def dfs(start, R):
        nonlocal best
        count[len(R)] = count.get(len(R), 0) + 1
        if len(R) > best: best, opt[:] = len(R), []
        if len(R) == best: opt.append(tuple(R))
        for k in range(start, len(L)):
            if removable(R + [L[k]]): dfs(k + 1, R + [L[k]])     # removability is inherited by subsets
    dfs(0, [])
    print("removable sets inside 3 consecutive units, by size:", dict(sorted(count.items())))
    anch = [R for R in opt if any(u == 0 for u, e in R)]
    print(f"maximum size {best}; maximum sets meeting unit 0: {len(anch)}")
    claws = {"a_0": [(0, e) for e in (0, 1, 2, 3, 4, 6, 7, 9, 10)],
             "b_1": [(0, 4), (0, 5), (1, 0), (1, 1), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5)],
             "c_1": [(0, 7), (0, 8), (1, 0), (1, 2), (1, 6), (1, 7), (1, 8), (2, 6), (2, 8)],
             "d_1": [(0, 10), (0, 11), (1, 1), (1, 2), (1, 9), (1, 10), (1, 11), (2, 9), (2, 11)]}
    E = flower(7); LE, inc = line_graph(E)                          # the same claws, read off the explicit graph
    for name, (kind, i) in {"a_0": ("a", 0), "b_1": ("b", 1), "c_1": ("c", 1), "d_1": ("d", 1)}.items():
        ks = inc[(kind, i)]
        got = sorted(local_index(7, E, inc, le) for le in LE if le[0] in ks or le[1] in ks)
        assert got == sorted(claws[name]), name
    assert best == 9 and sorted(map(sorted, anch)) == sorted(map(sorted, claws.values()))
    print("  they are the claw sets of a_0, b_1, c_1, d_1, so there are exactly 4q maximum sets for every odd q >= 7")
def check_small():
    """q = 3 and q = 5 exhaustively (every removable set of the whole graph, transfer model)."""
    for q in (3, 5):
        L = [(u, e) for u in range(q) for e in range(12)]; best, nbest = 0, 0; bysize = {}
        def dfs(start, R):
            nonlocal best, nbest
            bysize[len(R)] = bysize.get(len(R), 0) + 1
            if len(R) > best: best, nbest = len(R), 0
            if len(R) == best: nbest += 1
            for k in range(start, len(L)):
                R2 = R + [L[k]]
                if not colorable_tm(q, R2): dfs(k + 1, R2)
        dfs(0, [])
        print(f"q={q}: maximum {best}, attained by {nbest} sets; removable sets by size / q:",
              [bysize[k] / q for k in sorted(bysize) if k > 0])
        if q == 5: assert [bysize[k] // 5 for k in range(1, 10)] == [12, 132, 325, 498, 504, 336, 144, 36, 4]
        if q == 3:   # the unique 15-set isolates the six edges of J_3 at b_0, b_1, b_2
            E = flower(3); LE, inc = line_graph(E); loc = [local_index(3, E, inc, le) for le in LE]
            ks = set(inc[("b", 0)] + inc[("b", 1)] + inc[("b", 2)])
            R = {loc[k] for k, (x, y) in enumerate(LE) if x in ks or y in ks}
            assert len(R) == 15 and not colorable_tm(3, R)
            rest = [e for e in E if ("b", 0) not in e and ("b", 1) not in e and ("b", 2) not in e]
            LR, _ = line_graph_any(rest)
            assert not three_colorable(len(rest), LR)
            print("  it is the set touching the edges at b_0, b_1, b_2; J_3 - {b_0,b_1,b_2} has no 3-edge-coloring")
        assert (best, nbest) == ((15, 1) if q == 3 else (9, 20))
def check_claws(qmax=41):
    """Every claw set keeps L(J_q) uncolorable (direct coloring for q <= 9, transfer model up to qmax)."""
    for q in range(3, qmax + 1, 2):
        E = flower(q); LE, inc = line_graph(E); loc = [local_index(q, E, inc, le) for le in LE]
        for v, ks in inc.items():
            R = [k for k, (x, y) in enumerate(LE) if x in ks or y in ks]
            assert len(R) == 9 and not colorable_tm(q, {loc[k] for k in R})
            if q <= 9:
                Rs = set(R); assert not three_colorable(len(E), [LE[k] for k in range(len(LE)) if k not in Rs])
    print(f"all 4q claw sets keep L(J_q) uncolorable for odd q = 3..{qmax} (direct check for q <= 9)")
if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    steps = {"model": check_model, "period": check_period, "pairs": check_pairs, "window": check_window,
             "small": check_small, "claws": check_claws}
    for name, f in steps.items():
        if what in ("all", name): f()
    print("all checks passed")
