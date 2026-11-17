"""Proof for all n of: max removable set of the pinched gasket = 2^(n-1)+1, attained by exactly 2^(n-1) sets.
(i) the set of reachable profiles is the same for n = 2 and n = 3, hence for all n >= 2;
(ii) closed forms m_n(Q) = A 3^n + B 2^n + C and c_n(Q) = polynomial in x = 2^n hold for n = N0 (checked by the DP);
(iii) induction step n -> n+1 for n >= N0: for every profile Q and every triple (Q0,Q1,Q2) with PHI = Q,
      D(n) = m_{n+1}(Q) - sum m_n(Qi) is either identically 0 or > 0 for all n >= N0 (explicit threshold + direct check),
      and c_{n+1}(Q) = sum over the identically-0 triples of prod c_n(Qi) as polynomials in x."""
from fractions import Fraction as Fr
from gdp import base, step, PHI, FORB
N0 = 4
hist = {1: base()}
for n in range(2, 25): hist[n] = step(hist[n - 1])
P2, P3 = set(hist[2]), set(hist[3])
assert P2 == P3; PROF = sorted(P2)
print("(i) reachable profiles for n >= 2:", len(PROF))
# closed forms: fit A,B,C from n = 6,7,8; counts: fit polynomial in x of degree <= 2 from n = 6,7,8
def fit_m(Q):
    import itertools
    rows = [(3 ** n, 2 ** n, 1, hist[n][Q][0]) for n in (6, 7, 8)]
    # solve 3x3 exactly
    M = [[Fr(v) for v in r] for r in rows]
    for i in range(3):
        p = next(k for k in range(i, 3) if M[k][i] != 0); M[i], M[p] = M[p], M[i]
        M[i] = [v / M[i][i] for v in M[i]]
        for k in range(3):
            if k != i: M[k] = [a - M[k][i] * b for a, b in zip(M[k], M[i])]
    return tuple(M[i][3] for i in range(3))
def fit_c(Q):
    pts = [(Fr(2 ** n), Fr(hist[n][Q][1])) for n in (6, 7, 8)]
    # Lagrange -> coefficients of degree <= 2
    coef = [Fr(0)] * 3
    for i, (xi, yi) in enumerate(pts):
        others = [xj for j, (xj, _) in enumerate(pts) if j != i]
        den = Fr(1)
        for xj in others: den *= xi - xj
        a, b = others  # (x - a)(x - b) = x^2 - (a+b) x + ab
        coef[2] += yi / den; coef[1] += -yi * (a + b) / den; coef[0] += yi * a * b / den
    return tuple(coef)
MF = {Q: fit_m(Q) for Q in PROF}; CF = {Q: fit_c(Q) for Q in PROF}
mval = lambda Q, n: MF[Q][0] * 3 ** n + MF[Q][1] * 2 ** n + MF[Q][2]
cval = lambda Q, n: CF[Q][0] + CF[Q][1] * 2 ** n + CF[Q][2] * 4 ** n
for n in range(N0, 25):
    for Q in PROF: assert mval(Q, n) == hist[n][Q][0] and cval(Q, n) == hist[n][Q][1], (Q, n)
print(f"(ii) closed forms agree with the DP for {N0} <= n <= 24")
# (iii) induction step
triples = {}
for a in PROF:
    for b in PROF:
        for c in PROF: triples.setdefault(PHI[a][b][c], []).append((a, b, c))
assert set(triples) == set(PROF)
def polymul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q): r[i + j] += u * v
    return r
worst_threshold = 0
for Q in PROF:
    A, B, C = MF[Q]
    zero = []
    for t in triples[Q]:
        dA = 3 * A - sum(MF[q][0] for q in t); dB = 2 * B - sum(MF[q][1] for q in t); dC = C - sum(MF[q][2] for q in t)
        if dA == dB == dC == 0: zero.append(t); continue
        # need D(n) = dA 3^n + dB 2^n + dC > 0 for all n >= N0
        if dA != 0:
            assert dA > 0, (Q, t, "negative 3^n coefficient")
            n1 = N0
            while dA * Fr(3) ** n1 <= abs(dB) * 2 ** n1 + abs(dC): n1 += 1
        elif dB != 0:
            assert dB > 0, (Q, t, "negative 2^n coefficient")
            n1 = N0
            while dB * 2 ** n1 <= abs(dC): n1 += 1
        else:
            assert dC > 0, (Q, t, "negative constant"); n1 = N0
        for n in range(N0, n1 + 1): assert dA * 3 ** n + dB * 2 ** n + dC > 0, (Q, t, n)
        worst_threshold = max(worst_threshold, n1)
    # counts: c_{n+1}(Q)(x) with x = 2^n  ->  c(2x)
    target = [CF[Q][0], CF[Q][1] * 2, CF[Q][2] * 4]
    total = [Fr(0)] * 7
    for t in zero:
        p = [Fr(1)]
        for q in t: p = polymul(p, list(CF[q]))
        for i, v in enumerate(p): total[i] += v
    assert total[:3] == target and all(v == 0 for v in total[3:]), (Q, total, target)
print(f"(iii) induction step verified for every profile (largest explicit threshold n = {worst_threshold}, below it checked directly)")
def show(Q):
    names = {0: "E", 1: "01", 2: "02", 3: "12", 4: "D"}
    return "{" + ",".join(names[t] for t in range(5) if Q >> t & 1) + "}"
print("closed forms (n >= 4):")
for Q in PROF:
    A, B, C = MF[Q]; c0, c1, c2 = CF[Q]
    print(f"  {show(Q):16s} {'pinched-uncolourable' if not Q & FORB else '':21s} m = {A}*3^n + {B}*2^n + {C};  count = {c0} + {c1}*2^n + {c2}*4^n")
good = [Q for Q in PROF if not Q & FORB]
M = max((MF[Q] for Q in good), key=lambda f: (f[0], f[1], f[2]))
print("pinched maximum (n >= 4):", [show(Q) for Q in good if MF[Q] == M], "value", M)
