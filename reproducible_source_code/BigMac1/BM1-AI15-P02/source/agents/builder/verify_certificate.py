#!/usr/bin/env python3
"""Independent exact verifier for the A321614 transfer/Burnside certificate.

Uses only Python's standard library.  It rebuilds all states, the transfer
matrix, reflection data and the 4x4 exceptional Burnside counts from the
definitions; the serialized matrix is never trusted as an oracle.
"""

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys


def fail(message):
    print("FAIL: " + str(message), file=sys.stderr)
    raise SystemExit(1)


def check(condition, message):
    if not condition:
        fail(message)


def trim(p):
    p = [Fraction(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(n)])


def pneg(a):
    return [-x for x in a]


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pscale(a, c):
    return trim([Fraction(c) * x for x in a])


def pdivmod(a, b):
    a, b = trim(a), trim(b)
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [Fraction(0)], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a) - len(b), a[-1] / b[-1]
        q[k] += c
        a = padd(a, pneg([Fraction(0)] * k + pscale(b, c)))
    return trim(q), trim(a)


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    return trim(pscale(a, 1 / a[-1])) if a != [0] else [Fraction(0)]


def rat_reduce(n, d):
    n, d = trim(n), trim(d)
    g = pgcd(n, d)
    n, rn = pdivmod(n, g)
    d, rd = pdivmod(d, g)
    check(rn == [0] and rd == [0], "non-exact rational-function reduction")
    c = d[0]
    return trim(pscale(n, 1 / c)), trim(pscale(d, 1 / c))


def rat_add(a, b):
    return rat_reduce(padd(pmul(a[0], b[1]), pmul(b[0], a[1])),
                      pmul(a[1], b[1]))


def substitute_square(p):
    out = [Fraction(0)] * (2 * len(p) - 1)
    for i, c in enumerate(p):
        out[2 * i] = c
    return trim(out)


def shift(p, k):
    return [Fraction(0)] * k + [Fraction(x) for x in p]


def row_times_matrix(row, mat):
    return [sum(row[i] * mat[i][j] for i in range(len(row)))
            for j in range(len(mat[0]))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matrix_times_col(mat, col):
    return [sum(mat[i][j] * col[j] for j in range(len(col)))
            for i in range(len(mat))]


def scalar_krylov(row, mat, col, exponent):
    for _ in range(exponent):
        col = matrix_times_col(mat, col)
    return dot(row, col)


def compatible(a, b):
    attacked = a | (a << 1) | (a >> 1)
    return (attacked & b) == 0


def reverse4(mask):
    return sum(((mask >> r) & 1) << (3 - r) for r in range(4))


def fixed_vector(blocks, mat, involution, kind):
    pos = {p: i for i, p in enumerate(blocks)}
    if kind == "centre":
        return [int(involution(p) == p) for p in blocks]
    if kind == "seam":
        return [mat[i][pos[involution(p)]] for i, p in enumerate(blocks)]
    raise ValueError(kind)


def check_poly(actual, expected, label):
    actual = trim(actual)
    expected = trim(expected)
    check(actual == expected,
          "%s mismatch: actual=%r expected=%r" % (label, actual, expected))


def square_fixed_counts():
    cells = [(r, c) for r in range(4) for c in range(4)]
    placements = []
    for comb in combinations(cells, 4):
        if all(not (abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1)
               for a, b in combinations(comb, 2)):
            placements.append(frozenset(comb))
    maps = {
        "identity": lambda p: p,
        "row_reflection": lambda p: (3 - p[0], p[1]),
        "column_reflection": lambda p: (p[0], 3 - p[1]),
        "half_turn": lambda p: (3 - p[0], 3 - p[1]),
        "main_diagonal": lambda p: (p[1], p[0]),
        "anti_diagonal": lambda p: (3 - p[1], 3 - p[0]),
        "quarter_turn": lambda p: (p[1], 3 - p[0]),
        "three_quarter_turn": lambda p: (3 - p[1], p[0]),
    }
    out = {name: sum(frozenset(f(p) for p in s) == s for s in placements)
           for name, f in maps.items()}
    all_eight_sum = sum(out.values())
    out["orbits_under_oriented_rectangle_subgroup"] = sum(
        out[k] for k in ("identity", "row_reflection",
                         "column_reflection", "half_turn")) // 4
    out["orbits_under_full_square_group"] = all_eight_sum // 8
    return out


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("certificate.json")
    raw = path.read_bytes()
    cert = json.loads(raw)
    check(cert.get("format") == "A321614-builder-certificate-v1",
          "missing or invalid certificate format")

    columns = [m for m in range(16) if (m & (m << 1)) == 0]
    blocks = [(a, b) for a, b in product(columns, repeat=2)
              if bin(a).count("1") + bin(b).count("1") == 2 and compatible(a, b)]
    mat = [[int(compatible(p[1], q[0])) for q in blocks] for p in blocks]
    check(columns == cert.get("column_states"), "column states mismatch")
    check([list(p) for p in blocks] == cert.get("block_states"),
          "block states mismatch")
    check(mat == cert.get("transfer_matrix"), "transfer matrix mismatch")
    check(len(blocks) == 12, "reconstructed state count is not 12")

    u = [1] * len(blocks)
    resolvent = cert["identity_resolvent"]
    den = resolvent["denominator_low_to_high"]
    z = resolvent["left_numerator_rows_low_to_high"]
    # Verify Z(x)(I-xT)=D(x)u^T coefficient by coefficient.
    lhs = [z[0]]
    for k in range(1, len(z)):
        lhs.append([z[k][j] - row_times_matrix(z[k - 1], mat)[j]
                    for j in range(len(u))])
    lhs.append([-x for x in row_times_matrix(z[-1], mat)])
    for k, row in enumerate(lhs):
        check(row == [den[k]] * len(u),
              "resolvent coefficient %d mismatch" % k)

    h = lambda p: (reverse4(p[0]), reverse4(p[1]))
    v = lambda p: (p[1], p[0])
    r = lambda p: (reverse4(p[1]), reverse4(p[0]))
    pos = {p: i for i, p in enumerate(blocks)}
    for name, involution in (("h", h), ("v", v), ("r", r)):
        image = [involution(p) for p in blocks]
        check(set(image) == set(blocks), name + " is not a permutation")
        check(all(involution(involution(p)) == p for p in blocks),
              name + " is not an involution")
    for i, p in enumerate(blocks):
        for j, q in enumerate(blocks):
            check(mat[i][j] == mat[pos[h(p)]][pos[h(q)]],
                  "horizontal transfer invariance mismatch at (%d,%d)" % (i, j))
            check(mat[i][j] == mat[pos[v(q)]][pos[v(p)]],
                  "vertical transfer invariance mismatch at (%d,%d)" % (i, j))
            check(mat[i][j] == mat[pos[r(q)]][pos[r(p)]],
                  "half-turn transfer invariance mismatch at (%d,%d)" % (i, j))

    bh = [p for p in blocks if h(p) == p]
    th = [[int(compatible(p[1], q[0])) for q in bh] for p in bh]
    check(bh == [(0, 9), (9, 0)] and th == [[1, 0], [1, 1]],
          "horizontal fixed subsystem mismatch")

    dv = fixed_vector(blocks, mat, v, "seam")
    fv = fixed_vector(blocks, mat, v, "centre")
    dr = fixed_vector(blocks, mat, r, "seam")
    fr = fixed_vector(blocks, mat, r, "centre")
    check(sum(dv) == 3 and sum(fv) == 0,
          "vertical seam/centre boundary mismatch")
    check(sum(dr) == 7 and sum(fr) == 2,
          "half-turn seam/centre boundary mismatch")

    expected_initial = {
        "identity": [1, 12, 79, 408, 1847, 7698, 30319],
        "horizontal": [1, 2, 3, 4, 5, 6, 7],
        "vertical": [1, 0, 3, 0, 9, 0, 27],
        "half_turn": [1, 2, 7, 12, 31, 52, 119],
    }
    got_i = [1] + [scalar_krylov(u, mat, u, n - 1) for n in range(1, 7)]
    uh = [1, 1]
    got_h = [1] + [scalar_krylov(uh, th, uh, n - 1) for n in range(1, 7)]
    got_v, got_r = [1], [1]
    for n in range(1, 7):
        if n % 2 == 0:
            k = n // 2
            got_v.append(scalar_krylov(u, mat, dv, k - 1))
            got_r.append(scalar_krylov(u, mat, dr, k - 1))
        else:
            k = (n - 1) // 2
            got_v.append(scalar_krylov(u, mat, fv, k))
            got_r.append(scalar_krylov(u, mat, fr, k))
    check(got_i == expected_initial["identity"], "identity initial values mismatch")
    check(got_h == expected_initial["horizontal"], "horizontal initial values mismatch")
    check(got_v == expected_initial["vertical"], "vertical initial values mismatch")
    check(got_r == expected_initial["half_turn"], "half-turn initial values mismatch")

    nu = [dot(row, u) for row in z]
    ndv = [dot(row, dv) for row in z]
    ndr = [dot(row, dr) for row in z]
    nfr = [dot(row, fr) for row in z]
    check(nu == [12, -29, 33, -9], "identity resolvent scalar products mismatch")
    check(ndv == [3, -18, 30, -9], "vertical seam scalar products mismatch")
    check(ndr == [7, -32, 36, -9], "half-turn seam scalar products mismatch")
    check(nfr == [2, -6, 0, 0], "half-turn centre scalar products mismatch")

    # Branch rational functions.  For reversal J, even paths use the seam
    # vector d_J and odd paths use the fixed-centre vector f_J.
    identity = rat_reduce(shift(nu, 1), den)
    horizontal = rat_reduce([0, 2, -1], [1, -2, 1])
    vertical = rat_reduce(shift(substitute_square(ndv), 2), substitute_square(den))
    half_turn = rat_add(
        rat_reduce(shift(substitute_square(ndr), 2), substitute_square(den)),
        rat_reduce(shift(substitute_square(nfr), 1), substitute_square(den)))

    branches = {"identity": identity, "horizontal": horizontal,
                "vertical": vertical, "half_turn": half_turn}
    for name, value in branches.items():
        expected = cert["branch_gfs_low_to_high"][name]
        check_poly(value[0], expected["numerator"], name + " numerator")
        check_poly(value[1], expected["denominator"], name + " denominator")

    total = ([Fraction(1)], [Fraction(1)])
    for value in branches.values():
        total = rat_add(total, (pscale(value[0], Fraction(1, 4)), value[1]))
    expected = cert["final_gf_low_to_high"]
    check_poly(total[0], expected["numerator"], "final numerator")
    check_poly(total[1], expected["denominator"], "final denominator")
    check(pgcd(total[0], total[1]) == [Fraction(1)],
          "final numerator and denominator are not coprime")

    sq = square_fixed_counts()
    check(sq == cert.get("square_n2_fixed_counts"),
          "4x4 fixed-count audit mismatch")

    code_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = sha256(raw).hexdigest()
    print("VERIFIED A321614 exact transfer/Burnside certificate")
    print("states=12 denominator_degree=10 gcd=1 n2_D2=23 n2_D4=14")
    print("certificate_sha256=" + input_hash)
    print("verifier_sha256=" + code_hash)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail("%s: %s" % (type(exc).__name__, exc))
