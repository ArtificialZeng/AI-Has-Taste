"""Exact check of the weights in the manuscript (Sections 3 and 4), for every n in a range with n not divisible by 4.

For each n it checks, in exact rational arithmetic and over ALL arcs of the whirling-knight digraph:
  * g(a) <= 0  (g'(a) <= 0 when n = 3 mod 4), and
  * the right-hand side of the counting identity with c = n:  4, 4 and 0 (+ at least one arc leaving S).
This is a numerical cross-check; the manuscript proves the statements for all n.

  python verify_weights.py [nmax]        (default 60; needs only the Python standard library)
"""
import sys
from fractions import Fraction as F

MOVES = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))


def rot(v):                      # quarter turn in centred coordinates: (x, y) -> (y, -x)
    return (v[1], -v[0])


def orbit(A):
    out = set()
    for v in A:
        for _ in range(4):
            out.add(v); v = rot(v)
    return out


def arcs_of(cells):
    cs = set(cells)
    for u in cells:
        for d in MOVES:
            w = (u[0] + d[0], u[1] + d[1])
            if w in cs and u[0] * w[1] - w[0] * u[1] > 0:
                yield u, w


def crosses(u, w, r):
    """Does the open segment u-w cross the open ray {t r : t > 0}? (exact; u x w > 0 is assumed)"""
    cu = r[0] * u[1] - r[1] * u[0]          # r x u
    cw = r[0] * w[1] - r[1] * w[0]          # r x w
    # the angle increases from u to w by less than pi: r lies strictly inside the sweep iff u x r > 0 and r x w > 0
    return -cu > 0 and cw > 0


def check_even(n):
    h = n // 2
    half = F(1, 2)
    c = lambda i, j: (i - h + half, j - h + half)                       # centred coordinates
    cells = [c(i, j) for i in range(n) for j in range(n)]
    kappa = {c(i, j): (i + j + (i < h) + (j < h)) % 2 for i in range(n) for j in range(n)}
    X = orbit({c(i, h) for i in range(1, h - 1, 2)})
    Y = orbit({c(i, h - 1) for i in range(1, h - 1, 2)})
    rays = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    worst = -10
    for u, w in arcs_of(cells):
        k = sum(crosses(u, w, r) for r in rays)
        g = (kappa[u] == 1) - 2 * (u in X) - (kappa[w] == 0) - 2 * (w in Y) + k
        worst = max(worst, g)
    V = sum((kappa[v] == 1) - (kappa[v] == 0) for v in cells) - 2 * len(X) - 2 * len(Y) + 4 * n
    return worst, V, 0


def check_odd(n):
    m = (n - 1) // 2
    eps = F(1, 2 * m + 1)                                               # any 0 < eps < 1/m
    cells = [(x, y) for x in range(-m, m + 1) for y in range(-m, m + 1) if (x, y) != (0, 0)]
    C = {v for v in cells if v[0] == 0 or v[1] == 0}
    P = orbit({(x, 1) for x in range(-m, 0) if (x - m - 1) % 2 == 0})
    Q = orbit({(x, -1) for x in range(-m, 0) if (x - m - 1) % 2 == 0})
    S = {(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1)} - {(0, 0)}
    Din = C | Q
    Dout = P | S if m % 2 else P
    rays = [(-1, eps)]
    for _ in range(3):
        rays.append(rot(rays[-1]))
    worst = -10
    for u, w in arcs_of(cells):
        k = sum(crosses(u, w, r) for r in rays)
        g = k - (u in Dout) - (w in Din)
        if m % 2 and u in S and w not in S:
            g += 1
        worst = max(worst, g)
    V = sum((v[0] + v[1]) % 2 - (1 - (v[0] + v[1]) % 2) for v in cells) - len(Dout) - len(Din) + 4 * n
    return worst, V, (1 if m % 2 else 0)        # third entry: guaranteed extra from arcs leaving S


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    ok = True
    for n in range(5, nmax + 1):
        if n % 4 == 0:
            continue
        worst, V, extra = check_even(n) if n % 2 == 0 else check_odd(n)
        good = worst <= 0 and V + extra > 0
        ok &= good
        print(f"n={n:3d} (n mod 4 = {n % 4}): max over arcs = {worst}, right-hand side = {V}"
              f"{' (+>=1 for leaving S)' if extra else ''} -> {'OK' if good else 'FAILS'}")
    print("ALL OK" if ok else "SOME CASE FAILS")
