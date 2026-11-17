"""Transfer-matrix model of 3-coloring L(J_q) minus a set of L-edges.
Unit i: vertices a_i, b_i, c_i, d_i; spokes A=a_ib_i, B=a_ic_i, C=a_id_i; right connectors X=b_ib_{i+1}, Y=c_ic_{i+1}, Z=d_id_{i+1}
(at i = q-1: Y = c_{q-1}d_0, Z = d_{q-1}c_0 -> twist). State = colors (X, Y, Z) of the right connectors.
The 12 L-edges of unit i (local index): at a: 0 {A,B}, 1 {A,C}, 2 {B,C}; at b: 3 {XL,A}, 4 {A,XR}, 5 {XL,XR};
at c: 6 {YL,B}, 7 {B,YR}, 8 {YL,YR}; at d: 9 {ZL,C}, 10 {C,ZR}, 11 {ZL,ZR}.  Removed L-edge = that pair may be equal.
Boolean matrices are Python lists of 27 bitmasks (row s -> set of t)."""
import itertools
S = list(itertools.product(range(3), repeat=3)); IDX = {s: k for k, s in enumerate(S)}; N = 27
def unit(R=frozenset()):
    M = [0] * N
    def ok(u, v, e): return u != v or e in R
    for s in S:
        XL, YL, ZL = s
        for A, B, C in itertools.product(range(3), repeat=3):
            if not (ok(A, B, 0) and ok(A, C, 1) and ok(B, C, 2)): continue
            for t in S:
                XR, YR, ZR = t
                if (ok(XL, A, 3) and ok(A, XR, 4) and ok(XL, XR, 5) and ok(YL, B, 6) and ok(B, YR, 7) and ok(YL, YR, 8)
                        and ok(ZL, C, 9) and ok(C, ZR, 10) and ok(ZL, ZR, 11)):
                    M[IDX[s]] |= 1 << IDX[t]
    return M
def mul(P, Q):
    out = []
    for row in P:
        acc = 0; k = 0; r = row
        while r:
            if r & 1: acc |= Q[k]
            r >>= 1; k += 1
        out.append(acc)
    return out
I = [1 << k for k in range(N)]
SW = [1 << IDX[(s[0], s[2], s[1])] for s in S]   # left state of unit 0 = twist of right state of unit q-1
def trace_nonzero(P): return any((P[k] >> k) & 1 for k in range(N))
T = unit()
def power(M, k):
    out = I; B = M
    while k:
        if k & 1: out = mul(out, B)
        B = mul(B, B); k >>= 1
    return out
def colorable(q, defects):
    """defects: dict unit -> frozenset of local L-edge indices."""
    P = SW
    for i in range(q): P = mul(P, unit(defects[i]) if i in defects else T)
    return trace_nonzero(P)
