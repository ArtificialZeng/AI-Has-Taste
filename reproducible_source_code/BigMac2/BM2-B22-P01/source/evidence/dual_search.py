#!/usr/bin/env python3
"""Numerical support search for a sparse exact PEP dual at N=2.

This uses only the Python standard library.  It is discovery evidence, not a
certificate: the final certificate, if found, must be checked exactly.
"""

from math import sqrt


N = 4
BETA = (sqrt(5.0) - 1.0) / (1.0 + sqrt(7.0 + 2.0 * sqrt(5.0)))
ALPHA = 1.0 + BETA
C = 1.0 / (2.0 + ALPHA)


def zero():
    return [[0.0 for _ in range(N)] for _ in range(N)]


def add(a, b, scale=1.0):
    return [[a[i][j] + scale * b[i][j] for j in range(N)] for i in range(N)]


def sym_outer(u, v):
    return [[0.5 * (u[i] * v[j] + v[i] * u[j]) for j in range(N)]
            for i in range(N)]


def h_matrix(i, j):
    """Gram coefficient of h_ij; indices -1,0,1,2 with -1=optimum."""
    points = {
        -1: [0.0, 0.0, 0.0, 0.0],
        0: [1.0, 0.0, 0.0, 0.0],
        1: [1.0, -1.0, 0.0, 0.0],
        2: [1.0, -1.0, -ALPHA, 0.0],
    }
    grads = {
        -1: [0.0, 0.0, 0.0, 0.0],
        0: [0.0, 1.0, 0.0, 0.0],
        1: [0.0, 0.0, 1.0, 0.0],
        2: [0.0, 0.0, 0.0, 1.0],
    }
    dx = [points[i][k] - points[j][k] for k in range(N)]
    dg = [grads[i][k] - grads[j][k] for k in range(N)]
    out = sym_outer(grads[j], dx)
    out = [[-out[r][s] for s in range(N)] for r in range(N)]
    out = add(out, sym_outer(dg, dg), scale=-0.5)
    return out


H = {(i, j): h_matrix(i, j)
     for i in (-1, 0, 1, 2) for j in (-1, 0, 1, 2) if i != j}


def dual_slack(v):
    # v=(z0,z1,z2,mu0,mu1,mu2), using cycles
    # *->2->1->0->*, *->2->1->*, and *->2->*.
    z0, z1, z2, m0, m1, m2 = v
    s = zero()
    s[0][0] = C * C
    for k, m in enumerate((m0, m1, m2), start=1):
        s[k][k] -= m
    terms = {
        (-1, 0): z0,
        (-1, 1): z1,
        (-1, 2): z2,
        (0, 1): z0,
        (1, 2): z0 + z1,
        (2, -1): z0 + z1 + z2,
    }
    for edge, lam in terms.items():
        s = add(s, H[edge], scale=-lam)
    return s


def equations():
    # S*(1,c,c,c)=0 and sum mu=1, as A v=b.
    w = [1.0, C, C, C]
    base = dual_slack([0.0] * 6)
    cols = []
    for k in range(6):
        e = [0.0] * 6
        e[k] = 1.0
        sk = add(dual_slack(e), base, scale=-1.0)
        cols.append([sum(sk[i][j] * w[j] for j in range(N)) for i in range(N)]
                    + [1.0 if k >= 3 else 0.0])
    rhs = [-sum(base[i][j] * w[j] for j in range(N)) for i in range(N)] + [1.0]
    return [[cols[k][i] for k in range(6)] for i in range(5)], rhs


def rref_affine(a, b):
    m = [row[:] + [rhs] for row, rhs in zip(a, b)]
    rows, cols = len(m), len(m[0]) - 1
    pivots = []
    r = 0
    for c in range(cols):
        p = max(range(r, rows), key=lambda q: abs(m[q][c]))
        if abs(m[p][c]) < 1e-11:
            continue
        m[r], m[p] = m[p], m[r]
        z = m[r][c]
        m[r] = [x / z for x in m[r]]
        for q in range(rows):
            if q != r:
                z = m[q][c]
                m[q] = [m[q][j] - z * m[r][j] for j in range(cols + 1)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in pivots]
    particular = [0.0] * cols
    for rr, c in enumerate(pivots):
        particular[c] = m[rr][-1]
    directions = []
    for fc in free:
        direction = [0.0] * cols
        direction[fc] = 1.0
        for rr, c in enumerate(pivots):
            direction[c] = -m[rr][fc]
        directions.append(direction)
    return particular, directions


def jacobi_eigenvalues(a):
    a = [row[:] for row in a]
    for _ in range(100):
        p, q = max(((i, j) for i in range(N) for j in range(i + 1, N)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-13:
            break
        tau = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
        t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + sqrt(1.0 + tau * tau))
        cs = 1.0 / sqrt(1.0 + t * t)
        sn = t * cs
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = app - t * apq
        a[q][q] = aqq + t * apq
        a[p][q] = a[q][p] = 0.0
        for k in range(N):
            if k not in (p, q):
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = cs * akp - sn * akq
                a[k][q] = a[q][k] = sn * akp + cs * akq
    return sorted(a[i][i] for i in range(N))


def main():
    a, b = equations()
    p, directions = rref_affine(a, b)
    print(f"beta={BETA:.16g} alpha={ALPHA:.16g} c={C:.16g} c2={C*C:.16g}")
    print("particular", [f"{x:.16g}" for x in p])
    for d in directions:
        print("direction ", [f"{x:.16g}" for x in d])
    viable = []
    assert len(directions) == 2
    d, e = directions
    for kk in range(-500, 501):
        t = kk / 500.0
        for ll in range(-500, 501):
            u = ll / 500.0
            v = [p[i] + t * d[i] + u * e[i] for i in range(6)]
            if min(v) < -1e-10:
                continue
            ev = jacobi_eigenvalues(dual_slack(v))
            if ev[0] >= -1e-9:
                viable.append(((t, u), v, ev))
    print("viable count", len(viable))
    for t, v, ev in viable[::max(1, len(viable)//8)]:
        print("tu", t, "v", [f"{x:.12g}" for x in v], "eig", [f"{x:.12g}" for x in ev])


if __name__ == "__main__":
    main()
