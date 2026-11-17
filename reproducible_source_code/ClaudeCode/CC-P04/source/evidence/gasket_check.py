#!/usr/bin/env python3
"""Verification program for the answer to Knuth, TAOCP exercise 7.2.2.3-227 (Python 3 standard library only).

Theorem. For every n >= 2 the largest sets of edges that can be removed from the pinched Sierpinski gasket S^_n(3)
(corners 0...0 and 1...1 identified) without making it 3-colourable have 2^(n-1)+1 edges, and they are exactly the
2^(n-1) sets constructed by Filip Stappers (answer 227).

Usage: python3 gasket_check.py [all|model|proof|sets]
"""
import itertools, random, sys
from fractions import Fraction as Fr

# ------------------------------------------------------------ corner profiles
# A graph with three designated corners 0,1,2; a 3-colouring gives a corner pattern, up to permuting colours:
# type 0: c0=c1=c2, 1: c0=c1!=c2, 2: c0=c2!=c1, 3: c1=c2!=c0, 4: all different.  Profile = set of types (bitmask).
def typ(a, b, c):
    if a == b == c: return 0
    if a == b: return 1
    if a == c: return 2
    if b == c: return 3
    return 4
NAMES = {0: "E", 1: "01", 2: "02", 3: "12", 4: "D"}
def show(Q): return "{" + ",".join(NAMES[t] for t in range(5) if Q >> t & 1) + "}"
FORB = 1 | 2          # pinched graph colourable  <=>  some colouring has c0 = c1  <=>  profile meets {E, 01}
# S_n = copies 0,1,2 of S_{n-1}; local corner j of copy i is identified with local corner i of copy j.
# Parent corners: A = corner 0 of copy 0, B = corner 1 of copy 1, C = corner 2 of copy 2; shared D = (0:1 = 1:0),
# E = (0:2 = 2:0), F = (1:2 = 2:1). Copy 0 sees (A,D,E), copy 1 sees (D,B,F), copy 2 sees (E,F,C).
COMP = {}
for A, B, C, D, E, F in itertools.product(range(3), repeat=6):
    COMP.setdefault((typ(A, D, E), typ(D, B, F), typ(E, F, C)), set()).add(typ(A, B, C))
def phi(Q0, Q1, Q2):
    out = 0
    for (t0, t1, t2), Ts in COMP.items():
        if Q0 >> t0 & 1 and Q1 >> t1 & 1 and Q2 >> t2 & 1:
            for T in Ts: out |= 1 << T
    return out
PHI = [[[phi(a, b, c) for c in range(32)] for b in range(32)] for a in range(32)]
TRI_EDGES = ((0, 1), (0, 2), (1, 2))
def tri_profile(removed):
    kept = [e for e in TRI_EDGES if e not in removed]; Q = 0
    for c in itertools.product(range(3), repeat=3):
        if all(c[i] != c[j] for i, j in kept): Q |= 1 << typ(*c)
    return Q

# ------------------------------------------------------------ explicit graphs
def canon(s):
    """Vertex names are strings over 012 with  alpha a b^k == alpha b a^k  (k >= 1); normal form = smallest name."""
    n, best = len(s), s
    for k in range(1, n):
        a, rest = s[n - k - 1], s[n - k:]
        if len(set(rest)) == 1 and rest[0] != a: best = min(best, s[:n - k - 1] + rest[0] + a * k)
    return best
def gasket(n):
    """Edges of S_n(3): (w, i, j) = the edge w i -- w j of the finest triangle w (|w| = n-1)."""
    return [("".join(w), i, j) for w in itertools.product("012", repeat=n - 1) for i, j in TRI_EDGES]
def endpoints(e, n):
    w, i, j = e; u, v = canon(w + str(i)), canon(w + str(j))
    p = lambda x: "0" * n if x == "1" * n else x      # pinch 1...1 onto 0...0
    return p(u), p(v)
def profile(n, R):
    level = {w: tri_profile({(i, j) for i, j in TRI_EDGES if (w, i, j) in R}) for w in ("".join(t) for t in itertools.product("012", repeat=n - 1))}
    for d in range(n - 1, 0, -1):
        level = {w: PHI[level[w + "0"]][level[w + "1"]][level[w + "2"]] for w in ("".join(t) for t in itertools.product("012", repeat=d - 1))}
    return level[""]
def removable(n, R): return not profile(n, R) & FORB
def colourable_direct(n, R):
    E = [endpoints(e, n) for e in gasket(n) if e not in R]
    V = sorted({canon("".join(t)) for t in itertools.product("012", repeat=n)} - {"1" * n})
    idx = {v: k for k, v in enumerate(V)}; adj = [set() for _ in V]
    for u, v in E: adj[idx[u]].add(idx[v]); adj[idx[v]].add(idx[u])
    col = [-1] * len(V)
    def bt():
        best, bv = None, -1                                   # DSATUR-like: most constrained uncoloured vertex
        for v in range(len(V)):
            if col[v] < 0:
                k = len({col[w] for w in adj[v] if col[w] >= 0})
                if k > bv: best, bv = v, k
        if best is None: return True
        for c in range(3):
            if all(col[w] != c for w in adj[best]):
                col[best] = c
                if bt(): return True
                col[best] = -1
        return False
    return bt()

# ------------------------------------------------------------ the DP over exact profiles
def dp(N):
    """h[n][Q] = (largest |R| with profile exactly Q, number of such R), for n = 1..N."""
    h = {1: {}}
    for k in range(4):
        for Rm in itertools.combinations(TRI_EDGES, k):
            Q = tri_profile(set(Rm)); m, c = h[1].get(Q, (-1, 0))
            h[1][Q] = (k, 1) if k > m else (m, c + (k == m))
    for n in range(2, N + 1):
        new = {}
        for (a, (ma, ca)), (b, (mb, cb)), (c, (mc, cc)) in itertools.product(h[n - 1].items(), repeat=3):
            Q = PHI[a][b][c]; m = ma + mb + mc; cnt = ca * cb * cc; om, oc = new.get(Q, (-1, 0))
            new[Q] = (m, cnt) if m > om else (om, oc + cnt) if m == om else (om, oc)
        h[n] = new
    return h

def check_model():
    random.seed(1)
    for n in (2, 3):
        G = gasket(n); bad = 0
        for _ in range(300):
            R = set(random.sample(G, random.randint(0, min(len(G), 2 ** (n - 1) + 3))))
            bad += removable(n, R) == colourable_direct(n, R)
        print(f"model n={n}: profile recursion vs direct colouring of the explicit graph on 300 random sets: {bad} disagreements")
        assert bad == 0
    for n in (2, 3):
        G = gasket(n); best, sets = 0, []
        def dfs(start, R):
            nonlocal best, sets
            if len(R) > best: best, sets = len(R), []
            if len(R) == best: sets.append(frozenset(R))
            for k in range(start, len(G)):
                if not colourable_direct(n, set(R + [G[k]])): dfs(k + 1, R + [G[k]])
        dfs(0, [])
        print(f"exhaustive direct search n={n}: largest removable sets have {best} edges; {len(sets)} of them; equal to Stappers' sets: {set(sets) == set(stappers(n))}")
        assert set(sets) == set(stappers(n))

def check_proof():
    N0 = 4; h = dp(24)
    PROF = sorted(h[2]); assert set(h[3]) == set(PROF)
    print(f"reachable profiles: {len(PROF)} for n = 2 and n = 3, hence for all n >= 2")
    def solve3(rows):                                    # exact 3x3 linear solve
        M = [[Fr(v) for v in r] for r in rows]
        for i in range(3):
            p = next(k for k in range(i, 3) if M[k][i] != 0); M[i], M[p] = M[p], M[i]
            M[i] = [v / M[i][i] for v in M[i]]
            for k in range(3):
                if k != i: M[k] = [a - M[k][i] * b for a, b in zip(M[k], M[i])]
        return tuple(M[i][3] for i in range(3))
    MF = {Q: solve3([(3 ** n, 2 ** n, 1, h[n][Q][0]) for n in (6, 7, 8)]) for Q in PROF}            # m = A 3^n + B 2^n + C
    CF = {Q: solve3([(1, 2 ** n, 4 ** n, h[n][Q][1]) for n in (6, 7, 8)]) for Q in PROF}            # c = a + b 2^n + c 4^n
    mv = lambda Q, n: MF[Q][0] * 3 ** n + MF[Q][1] * 2 ** n + MF[Q][2]
    cv = lambda Q, n: CF[Q][0] + CF[Q][1] * 2 ** n + CF[Q][2] * 4 ** n
    assert all(mv(Q, n) == h[n][Q][0] and cv(Q, n) == h[n][Q][1] for Q in PROF for n in range(N0, 25))
    print(f"closed forms agree with the DP for {N0} <= n <= 24; induction step:")
    triples = {}
    for t in itertools.product(PROF, repeat=3): triples.setdefault(PHI[t[0]][t[1]][t[2]], []).append(t)
    def pmul(p, q):
        r = [Fr(0)] * (len(p) + len(q) - 1)
        for i, u in enumerate(p):
            for j, v in enumerate(q): r[i + j] += u * v
        return r
    zeros = {}
    for Q in PROF:
        A, B, C = MF[Q]; zeros[Q] = []
        for t in triples[Q]:
            dA = 3 * A - sum(MF[q][0] for q in t); dB = 2 * B - sum(MF[q][1] for q in t); dC = C - sum(MF[q][2] for q in t)
            if dA == dB == dC == 0: zeros[Q].append(t); continue
            lead = dA if dA else dB if dB else dC
            assert lead > 0, (show(Q), [show(q) for q in t])
            n1 = N0
            if dA: 
                while dA * Fr(3) ** n1 <= abs(dB) * 2 ** n1 + abs(dC): n1 += 1
            elif dB:
                while dB * 2 ** n1 <= abs(dC): n1 += 1
            for n in range(N0, n1 + 1): assert dA * 3 ** n + dB * 2 ** n + dC > 0
        assert zeros[Q], show(Q)                     # some triple attains the closed form exactly
        total = [Fr(0)] * 7
        for t in zeros[Q]:
            p = [Fr(1)]
            for q in t: p = pmul(p, list(CF[q]))
            total = [a + b for a, b in zip(total, p + [Fr(0)] * (7 - len(p)))]
        assert total[:3] == [CF[Q][0], 2 * CF[Q][1], 4 * CF[Q][2]] and not any(total[3:])
    print("  every profile: the best triples are the same for all n >= 4 and the counts satisfy the recursion")
    for Q in PROF:
        A, B, C = MF[Q]; a, b, c = CF[Q]
        print(f"  {show(Q):16s} max removed = {A}*3^n + {B}*2^n + {C}, number = {a} + {b}*2^n + {c}*4^n" + ("   <- pinched graph stays uncolourable" if not Q & FORB else ""))
    for n in range(2, 25):
        good = [(h[n][Q][0], h[n][Q][1], Q) for Q in h[n] if not Q & FORB]
        M = max(g[0] for g in good); Cn = sum(g[1] for g in good if g[0] == M)
        assert (M, Cn) == (2 ** (n - 1) + 1, 2 ** (n - 1)), n
    print("hence for every n >= 2: largest removable set 2^(n-1)+1 (profile {02,12,D}), exactly 2^(n-1) such sets")
    P = lambda *ts: sum(1 << t for t in ts)
    for Q, want in ((P(2, 3, 4), {(P(4), P(1, 4), P(2, 3, 4)), (P(1, 4), P(4), P(2, 3, 4))}),
                    (P(1, 4), {(P(2, 4), P(3, 4), P(4))}), (P(2, 4), {(P(1, 4), P(4), P(3, 4))}),
                    (P(3, 4), {(P(4), P(1, 4), P(2, 4))}), (P(4), {(P(4), P(4), P(4))})):
        assert set(zeros[Q]) == want, show(Q)
        for n in range(1, N0):                      # the same maximizing triples for the small steps n -> n+1
            m = h[n + 1][Q][0]
            arg = {t for t in itertools.product(h[n], repeat=3) if PHI[t[0]][t[1]][t[2]] == Q and sum(h[n][q][0] for q in t) == m}
            assert arg == want, (n, show(Q))
    print("structure of the largest sets (every step n -> n+1, n >= 1):")
    print("  {02,12,D}: copy 2 has a largest set of the same kind, one of copies 0, 1 has the unique {01,D}-set, the other copy nothing")
    print("  {01,D}: copy 0 has the unique {02,D}-set, copy 1 the unique {12,D}-set; similarly for {02,D}, {12,D}")

# ------------------------------------------------------------ Stappers' construction and the largest sets
def stappers(n):
    """Answer 227 (Knuth/Stappers): two tip edges at 2...2 plus non-tip edges; n = 2: 00--01 or 11--10 (= 11--01);
    n -> n+1: each non-tip edge alpha a -- alpha b becomes alpha a a -- alpha a c and alpha b b -- alpha b c (c not in {a,b}),
    plus either 2..200--2..201 or 2..211--2..210."""
    sets = [[("00", "01")], [("11", "10")]]
    for m in range(3, n + 1):
        new = []
        for S in sets:
            ref = []
            for x, y in S:
                al, a, b = x[:-1], x[-1], y[-1]; c = ({"0", "1", "2"} - {a, b}).pop()
                ref += [(al + a + a, al + a + c), (al + b + b, al + b + c)]
            new += [ref + [("2" * (m - 2) + "00", "2" * (m - 2) + "01")], ref + [("2" * (m - 2) + "11", "2" * (m - 2) + "10")]]
        sets = new
    tips = {("2" * (n - 1), 0, 2), ("2" * (n - 1), 1, 2)}
    out = []
    for S in sets:
        R = set(tips)
        for x, y in S:
            assert x[:-1] == y[:-1]; i, j = sorted((int(x[-1]), int(y[-1]))); R.add((x[:-1], i, j))
        out.append(frozenset(R))
    return out
def largest_sets(n):
    """All largest removable sets, reconstructed from the DP by following every optimal triple (explicit edge sets)."""
    h = dp(n)
    def build(level, Q, prefix):
        if level == 1:
            return [frozenset((prefix, i, j) for i, j in Rm) for k in range(4) for Rm in itertools.combinations(TRI_EDGES, k)
                    if tri_profile(set(Rm)) == Q and k == h[1][Q][0]]
        m = h[level][Q][0]; res = []
        for a, b, c in itertools.product(h[level - 1], repeat=3):
            if PHI[a][b][c] == Q and h[level - 1][a][0] + h[level - 1][b][0] + h[level - 1][c][0] == m:
                for x in build(level - 1, a, prefix + "0"):
                    for y in build(level - 1, b, prefix + "1"):
                        for z in build(level - 1, c, prefix + "2"): res.append(x | y | z)
        return res
    good = [Q for Q in h[n] if not Q & FORB]; M = max(h[n][Q][0] for Q in good)
    return [R for Q in good if h[n][Q][0] == M for R in build(n, Q, "")]
def check_sets(nmax=10):
    for n in range(2, nmax + 1):
        L = largest_sets(n); S = stappers(n)
        ok = len(set(L)) == len(L) == 2 ** (n - 1) and set(L) == set(S) and all(len(R) == 2 ** (n - 1) + 1 and removable(n, R) for R in S)
        print(f"n={n}: the {len(L)} largest removable sets (from the DP, as explicit edge sets) are exactly Stappers' sets: {ok}")
        assert ok
    ex = [("0000", "0001"), ("0022", "0021"), ("0111", "0110"), ("0122", "0120"), ("2000", "2002"), ("2011", "2012"), ("2200", "2201"), ("2202", "2222"), ("2212", "2222")]
    R = set()
    for x, y in ex:
        f = [e for e in gasket(4) if {canon(e[0] + str(e[1])), canon(e[0] + str(e[2]))} == {canon(x), canon(y)}]
        assert len(f) == 1; R.add(f[0])
    print("Knuth's n = 4 example is one of them:", frozenset(R) in set(stappers(4)))
if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    for name, f in (("model", check_model), ("proof", check_proof), ("sets", check_sets)):
        if what in ("all", name): f()
    print("all checks passed")
