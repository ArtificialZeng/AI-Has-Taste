"""Exact certificate for the minimum lag of a 2-by-2 SE witness.

For A=[[1,12],[11,1]] and B=[[1,132],[1,1]], this script checks that
there are no nonnegative integer 2-by-2 matrices R,S satisfying

    AR=RB, SA=BS, RS=A**L, SR=B**L

for 1 <= L < 22, and it reconstructs and checks a witness for L=22.

Completeness of the finite Pell-orbit enumeration is proved in the companion
file lag1_22_2x2_minimality.md.  The computation uses only Python integers.
"""

from math import gcd, isqrt


def mat_mul(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def mat_pow(matrix, exponent):
    result = [[1, 0], [0, 1]]
    base = matrix
    while exponent:
        if exponent & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        exponent //= 2
    return result


# A pair (x,y) denotes x+y*sqrt(132)=x+2y*sqrt(33).
def pair_mul(left, right):
    x, y = left
    u, v = right
    return x * u + 132 * y * v, x * v + y * u


def pair_pow(pair, exponent):
    result = (1, 0)
    base = pair
    while exponent:
        if exponent & 1:
            result = pair_mul(result, base)
        base = pair_mul(base, base)
        exponent //= 2
    return result


def lag_coefficients(lag):
    """Return a,b such that A**lag=[[a,12b],[11b,a]]."""
    return pair_pow((1, 1), lag)


def scalar_candidates(lag):
    """Enumerate every feasible (p,q,r,s) by complete Pell orbits.

    The generalized Pell equation is
        X**2 - 132*Y**2 = (-131)**lag.
    Its solutions are
        +/-(1+sqrt(132))**j (1-sqrt(132))**(lag-j)
            (23+2*sqrt(132))**n,
    for 0<=j<=lag and n in Z.  Under |X|<=a, 0<=Y<=b, it is enough
    to take -lag<=n<=lag; see the companion proof.
    """
    a, b = lag_coefficients(lag)
    lam = (1, 1)
    conjugate_lam = (1, -1)
    unit = (23, 2)
    inverse_unit = (23, -2)
    found = set()
    orbit_records = set()

    for j in range(lag + 1):
        base = pair_mul(pair_pow(lam, j), pair_pow(conjugate_lam, lag - j))
        for n in range(-lag, lag + 1):
            unit_power = pair_pow(unit if n >= 0 else inverse_unit, abs(n))
            raw_x, raw_y = pair_mul(base, unit_power)
            for sign in (1, -1):
                x = sign * raw_x
                y = sign * raw_y
                if not (0 <= y <= b and abs(x) <= a):
                    continue
                if (x + a) % 24:
                    continue
                q = (x + a) // 24
                if q < 0 or 12 * q > a or q % 11 != a % 11:
                    continue
                p = (a - 12 * q) // 11
                if (b - y) % 2:
                    continue
                r = (b + y) // 2
                s = (b - y) // 2
                if min(p, q, r, s) < 0 or p * q != r * s:
                    continue
                found.add((p, q, r, s))
                orbit_records.add((p, q, r, s, x, y, j, n, sign))

    return sorted(found), sorted(orbit_records)


def direct_scalar_scan(lag):
    """Independent q-enumeration, used on lags small enough for direct replay."""
    a, b = lag_coefficients(lag)
    found = set()
    for q in range(a % 11, a // 12 + 1, 11):
        p = (a - 12 * q) // 11
        discriminant = b * b - 4 * p * q
        if discriminant < 0:
            continue
        y = isqrt(discriminant)
        if y * y != discriminant or (b - y) % 2:
            continue
        r = (b + y) // 2
        s = (b - y) // 2
        found.add((p, q, r, s))
    return sorted(found)


def outer_factor(p, q, r, s):
    """Lift a nonnegative rank-one [[p,r],[s,q]] to [x,z]^T [u,v]."""
    assert min(p, q, r, s) >= 0 and p * q == r * s
    if p or r:
        x = gcd(p, r)
        u, v = p // x, r // x
        assert s % u == 0 if u else q % v == 0
        z = s // u if u else q // v
    elif s or q:
        x = 0
        z = gcd(s, q)
        u, v = s // z, q // z
    else:
        x = z = u = v = 0
    assert (x * u, z * v, x * v, z * u) == (p, q, r, s)
    return x, z, u, v


A = [[1, 12], [11, 1]]
B = [[1, 132], [1, 1]]

# Ring-theoretic constants used by the completeness proof.
assert pair_mul((1, 1), (1, -1)) == (-131, 0)
assert pair_mul((23, 2), (23, -2)) == (1, 0)
# In O_Q(sqrt(33)), (5+sqrt(33))/2 has norm -2, principalizing
# either prime ideal above 2 in the Minkowski class-number argument.
assert 5 * 5 - 33 == -8
# The finite check in the standard least-positive-unit argument: no
# (u+v*sqrt(33))/2 with 1<=v<8 has norm +/-1, while (u,v)=(46,8) does.
for v in range(1, 8):
    assert all(isqrt(33 * v * v + sign * 4) ** 2 != 33 * v * v + sign * 4
               for sign in (1, -1))
assert 46 * 46 - 33 * 8 * 8 == 4
assert isqrt(33 * 8 * 8 - 4) ** 2 != 33 * 8 * 8 - 4

all_counts = []
for lag in range(1, 23):
    candidates, records = scalar_candidates(lag)
    all_counts.append(len(candidates))
    if lag <= 8:
        assert candidates == direct_scalar_scan(lag)
    if lag < 22:
        assert candidates == []
    else:
        assert candidates == [
            (
                330834707029117152443,
                56286015521267519916875,
                56286015521267519916875,
                330834707029117152443,
            )
        ]
        assert records == [
            candidates[0]
            + (
                671793004477889950325627,
                55955180814238402764432,
                0,
                1,
                1,
            )
        ]

assert all_counts == [0] * 21 + [1]

p, q, r, s = scalar_candidates(22)[0][0]
x, z, u, v = outer_factor(p, q, r, s)
R = [[x, 12 * z], [z, 11 * x]]
S = [[11 * u, 12 * v], [v, u]]
assert R == [[1, 12], [1, 11]]
assert all(entry >= 0 for matrix in (R, S) for row in matrix for entry in row)
assert mat_mul(A, R) == mat_mul(R, B)
assert mat_mul(S, A) == mat_mul(B, S)
assert mat_mul(R, S) == mat_pow(A, 22)
assert mat_mul(S, R) == mat_pow(B, 22)

print("PASS: candidate counts for lags 1..22 are", all_counts)
print("PASS: lag 22 is minimal among nonnegative integer 2x2 SE witnesses")
print("R =", R)
print("S =", S)
