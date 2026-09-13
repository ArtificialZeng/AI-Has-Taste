#!/usr/bin/env python3
"""Fresh referee checks for the frozen time-eight candidate.

This verifier is intentionally independent of evidence/time8_exact.py.  It
evaluates the path recursion over a finite field on a full interpolation grid
instead of using sparse symbolic-polynomial matrices.  It also checks the
decisive one-variable identities with a separate dense coefficient-list
implementation over the rationals.
"""

from fractions import Fraction
from itertools import combinations


PRIME = 1_000_003


def matmul(a, b, modulus):
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(2)) % modulus
            for j in range(2)
        ]
        for i in range(2)
    ]


def matadd(a, b, modulus):
    return [
        [(a[i][j] + b[i][j]) % modulus for j in range(2)]
        for i in range(2)
    ]


def path_sums(r, s, z, modulus):
    p = [[r, s * z % modulus], [0, 0]]
    q = [[0, 0], [s, -r * z % modulus]]
    total = {k: [[0, 0], [0, 0]] for k in range(9)}
    counts = {k: 0 for k in range(9)}
    for right_tuple in combinations(range(8), 4):
        right = set(right_tuple)
        position = 0
        sojourn = 0
        amplitude = [[1, 0], [0, 1]]
        for j in range(8):
            step = 1 if j in right else -1
            if position > 0 or (position == 0 and step == 1):
                sojourn += 1
            amplitude = matmul(q if step == 1 else p, amplitude, modulus)
            position += step
        assert position == 0
        total[sojourn] = matadd(total[sojourn], amplitude, modulus)
        counts[sojourn] += 1
    return total, counts


def closed_sums(r, s, z, modulus):
    x = r * r % modulus
    y = s * s % modulus
    u = r * s % modulus
    f = (y**3 - 6 * x * y**2 + 6 * x**2 * y - x**3) % modulus
    a = (-y**2 + 3 * x * y - x**2) % modulus
    b = (y**2 - 5 * x * y + 3 * x**2) % modulus
    c = (-3 * y**2 + 5 * x * y - x**2) % modulus
    m = (-2 * y**2 + 4 * x * y - x**2) % modulus
    n = (-y**2 + 4 * x * y - 2 * x**2) % modulus
    zero = [[0, 0], [0, 0]]
    out = {k: [row[:] for row in zero] for k in range(9)}
    out[0] = [[0, 0], [r * s * z**3 * f, s**2 * z**4 * f]]
    out[2] = [
        [u**2 * a * z**4, u * y * a * z**5],
        [u * y * b * z**3, u**2 * c * z**4],
    ]
    out[4] = [
        [u**2 * m * z**4, u * y * n * z**5],
        [-u * y * n * z**3, u**2 * m * z**4],
    ]
    out[6] = [
        [u**2 * c * z**4, -u * y * b * z**5],
        [-u * y * a * z**3, u**2 * a * z**4],
    ]
    out[8] = [[s**2 * z**4 * f, -r * s * z**5 * f], [0, 0]]
    return {
        k: [[entry % modulus for entry in row] for row in matrix]
        for k, matrix in out.items()
    }


expected_counts = {
    0: 14,
    1: 0,
    2: 14,
    3: 0,
    4: 14,
    5: 0,
    6: 14,
    7: 0,
    8: 14,
}

# Each matrix-entry difference has degree at most eight in each of r,s,z.
# Agreement on the 9^3 grid therefore proves the polynomial identity modulo
# PRIME.  The integer coefficients have absolute value below 100, so reduction
# modulo this prime is injective for the possible differences.
for r_value in range(9):
    for s_value in range(9):
        for z_value in range(9):
            actual, counts = path_sums(r_value, s_value, z_value, PRIME)
            assert counts == expected_counts
            assert actual == closed_sums(r_value, s_value, z_value, PRIME)


# Dense coefficient lists, low degree first.
def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    n = max(len(p), len(q))
    return trim(
        [
            (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
            for i in range(n)
        ]
    )


def scale(c, p):
    return trim([Fraction(c) * coefficient for coefficient in p])


def sub(p, q):
    return add(p, scale(-1, q))


def mul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def power(p, exponent):
    out = [Fraction(1)]
    for _ in range(exponent):
        out = mul(out, p)
    return out


one = [Fraction(1)]
x = [Fraction(0), Fraction(1)]
y = sub(one, x)
xy = mul(x, y)
t = sub(scale(2, x), one)
f = add(
    add(power(y, 3), scale(-6, mul(x, power(y, 2)))),
    add(scale(6, mul(power(x, 2), y)), scale(-1, power(x, 3))),
)
a = add(add(scale(-1, power(y, 2)), scale(3, xy)), scale(-1, power(x, 2)))
b = add(add(power(y, 2), scale(-5, xy)), scale(3, power(x, 2)))
c = add(add(scale(-3, power(y, 2)), scale(5, xy)), scale(-1, power(x, 2)))
m = add(add(scale(-2, power(y, 2)), scale(4, xy)), scale(-1, power(x, 2)))
n = add(add(scale(-1, power(y, 2)), scale(4, xy)), scale(-2, power(x, 2)))

assert f == [Fraction(1), Fraction(-9), Fraction(21), Fraction(-14)]
assert f == mul(sub(one, scale(2, x)), add(sub(one, scale(7, x)), scale(7, power(x, 2))))
assert add(power(a, 2), mul(b, c)) == scale(2, mul(t, f))

u4 = power(xy, 2)
u2y2 = mul(xy, power(y, 2))
twice_w = add(
    add(mul(u4, power(a, 2)), mul(u2y2, power(a, 2))),
    add(mul(u2y2, power(b, 2)), mul(u4, power(c, 2))),
)
w4 = add(mul(u4, power(m, 2)), mul(u2y2, power(n, 2)))
gap = mul(mul(power(x, 2), power(y, 3)), power(t, 2))
assert sub(scale(Fraction(1, 2), twice_w), w4) == gap

def evaluate(p, value):
    value = Fraction(value)
    return sum(coefficient * value**degree for degree, coefficient in enumerate(p))


assert evaluate(w4, Fraction(1, 2)) == Fraction(1, 128)
assert evaluate(gap, Fraction(1, 2)) == 0

print("PASS: independent 9^3 finite-field interpolation check of all path sums")
print("PASS: independent dense-polynomial check of all decisive identities")
print("PASS: balanced weights are exactly 1/128 and the equality gap vanishes")
