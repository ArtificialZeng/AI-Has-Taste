#!/usr/bin/env python3
"""Floating-point reconnaissance for the five-atom / three-point problem.

This is discovery evidence only: it samples balanced directions and moment-null
responses, then computes the distance from 0 to every interpolation triangle.
It also reports whether the nearest point is a vertex, edge interior (not
attained for three distinct directions), or triangle interior.
"""

import cmath
import itertools
import math
import random


def solve_square(a, b):
    a = [list(map(complex, row)) + [complex(rhs)] for row, rhs in zip(a, b)]
    n = len(a)
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if abs(a[pivot][col]) < 1e-12:
            raise ValueError("singular")
        a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [x / q for x in a[col]]
        for r in range(n):
            if r != col:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[col])]
    return [row[-1] for row in a]


def balanced_weights(t):
    # Set p_3,p_4 to a small common value and solve for p_0,p_1,p_2.
    eps = random.uniform(0.01, 0.12)
    fixed = [eps, eps]
    rhs = [1 - sum(fixed),
           -sum(fixed[j] * t[j + 3].real for j in range(2)),
           -sum(fixed[j] * t[j + 3].imag for j in range(2))]
    mat = [[1, 1, 1],
           [t[j].real for j in range(3)],
           [t[j].imag for j in range(3)]]
    try:
        head = solve_square(mat, rhs)
    except ValueError:
        return None
    p = [x.real for x in head] + fixed
    return p if min(p) > 1e-5 else None


def response_from_free(t, p):
    z = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(3)]
    mat = [[p[3], p[4]],
           [p[3] * t[3].conjugate(), p[4] * t[4].conjugate()]]
    rhs = [-sum(p[j] * z[j] for j in range(3)),
           -sum(p[j] * t[j].conjugate() * z[j] for j in range(3))]
    try:
        z.extend(solve_square(mat, rhs))
    except ValueError:
        return None
    return z


def dot(x, y):
    return sum((a.conjugate() * b).real for a, b in zip(x, y))


def edge_nearest(x, y):
    d = [b - a for a, b in zip(x, y)]
    dd = dot(d, d)
    u = 0.0 if dd == 0 else max(0.0, min(1.0, -dot(x, d) / dd))
    v = [a + u * h for a, h in zip(x, d)]
    kind = "edge" if 1e-9 < u < 1 - 1e-9 else "vertex"
    return dot(v, v), (1 - u, u), kind


def triangle_nearest(v):
    candidates = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        val, w, kind = edge_nearest(v[i], v[j])
        alpha = [0.0, 0.0, 0.0]
        alpha[i], alpha[j] = w
        candidates.append((val, alpha, kind))
    x, d1, d2 = v[0], [b-a for a, b in zip(v[0], v[1])], [b-a for a, b in zip(v[0], v[2])]
    gram = [[dot(d1, d1), dot(d1, d2)], [dot(d1, d2), dot(d2, d2)]]
    rhs = [-dot(x, d1), -dot(x, d2)]
    try:
        u, w = (q.real for q in solve_square(gram, rhs))
        alpha = [1-u-w, u, w]
        if min(alpha) > 1e-10:
            point = [alpha[0]*v[0][r] + alpha[1]*v[1][r] + alpha[2]*v[2][r] for r in range(2)]
            candidates.append((dot(point, point), alpha, "interior"))
    except ValueError:
        pass
    return min(candidates, key=lambda x: x[0])


def evaluate(t, p, z):
    B = {}
    for i, j in itertools.combinations(range(5), 2):
        B[i, j] = ((t[i]*z[j] - t[j]*z[i])/(t[i]-t[j]),
                   (z[i]-z[j])/(t[i]-t[j]))
    best = None
    for tri in itertools.combinations(range(5), 3):
        edges = [tuple(sorted(e)) for e in itertools.combinations(tri, 2)]
        val, alpha, kind = triangle_nearest([B[e] for e in edges])
        item = (val, tri, edges, alpha, kind)
        if best is None or item[0] < best[0]:
            best = item
    E = sum(pi * abs(zi)**2 for pi, zi in zip(p, z))
    return best[0] / E, best


def main():
    random.seed(20260906)
    record = (-1, None)
    accepted = 0
    for _ in range(200000):
        # The first three directions straddle the origin; the other two vary.
        angles = [random.uniform(-0.18, 0.18),
                  random.uniform(2.0, 2.25),
                  random.uniform(4.0, 4.25),
                  random.uniform(0, 2*math.pi),
                  random.uniform(0, 2*math.pi)]
        t = [cmath.exp(1j*a) for a in angles]
        if min(abs(t[i]-t[j]) for i, j in itertools.combinations(range(5), 2)) < 1e-4:
            continue
        p = balanced_weights(t)
        if p is None:
            continue
        z = response_from_free(t, p)
        if z is None:
            continue
        ratio, witness = evaluate(t, p, z)
        accepted += 1
        if ratio > record[0]:
            record = (ratio, (angles, p, z, witness))
    ratio, data = record
    print("accepted", accepted)
    print("largest sampled closure optimum C/E", format(ratio, ".17g"))
    if data:
        angles, p, z, witness = data
        print("angles", [float(format(x, ".17g")) for x in angles])
        print("p", [float(format(x, ".17g")) for x in p])
        print("z", [(float(format(x.real, ".17g")), float(format(x.imag, ".17g"))) for x in z])
        print("best triangle", witness)


if __name__ == "__main__":
    main()
