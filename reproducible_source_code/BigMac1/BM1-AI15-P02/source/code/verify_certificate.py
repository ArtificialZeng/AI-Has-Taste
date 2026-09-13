#!/usr/bin/env python3
"""Fail-closed independent verifier for the serialized A321614 certificate.

This file intentionally imports no discovery/generator module.  It rebuilds
the state set, group action, transfer matrices, Burnside representation,
Cayley--Hamilton witness, rational generating function, and Bezout identity.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
DEFAULT_CERT = BASE / "certificate" / "a321614_certificate.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def zero_matrix(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def matrix_vector(M, x):
    require(all(len(row) == len(x) for row in M), "matrix/vector size mismatch")
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def scalar_product(x, y):
    require(len(x) == len(y), "dot product size mismatch")
    return sum(x[i] * y[i] for i in range(len(x)))


def direct_state_list():
    answer = []
    for top_row in range(2):
        for bottom_row in range(2, 4):
            for top_side in range(2):
                for bottom_side in range(2):
                    cells = ((top_row, top_side), (bottom_row, bottom_side))
                    attack = max(abs(top_row - bottom_row), abs(top_side - bottom_side)) <= 1
                    if not attack:
                        answer.append(cells)
    return answer


def direct_compatible(s, t):
    for r1, local_c1 in s:
        for r2, local_c2 in t:
            global_difference = (2 + local_c2) - local_c1
            if abs(r1 - r2) <= 1 and abs(global_difference) <= 1:
                return False
    return True


def state_image(s, horizontal, vertical):
    image = []
    for row, side in s:
        image.append((3 - row if horizontal else row, 1 - side if vertical else side))
    return tuple(sorted(image))


def induced_permutation(states, horizontal=False, vertical=False):
    lookup = {s: i for i, s in enumerate(states)}
    require(len(lookup) == len(states), "duplicate local state")
    return [lookup[state_image(s, horizontal, vertical)] for s in states]


def make_augmented(A, b):
    d = len(A)
    require(len(b) == d and all(len(row) == d for row in A), "bad augmented input")
    T = zero_matrix(d + 1, d + 1)
    for i in range(d):
        T[i + 1][0] = b[i]
        for j in range(d):
            T[i + 1][j + 1] = A[i][j]
    return T, [1] + [0] * d, [1] + [1] * d


def make_interleaving(T, p, q, ell):
    d = len(T)
    require(len(p) == len(q) == len(ell) == d, "bad interleaving vectors")
    M = zero_matrix(2 * d, 2 * d)
    for i in range(d):
        M[i][d + i] = 1
        for j in range(d):
            M[d + i][j] = T[i][j]
    return M, p + q, ell + [0] * d


def diagonal_join(blocks):
    total = sum(len(A) for A in blocks)
    M = zero_matrix(total, total)
    offset = 0
    for A in blocks:
        require(all(len(row) == len(A) for row in A), "nonsquare block")
        for i in range(len(A)):
            for j in range(len(A)):
                M[offset + i][offset + j] = A[i][j]
        offset += len(A)
    return M


def convolve(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            out[i + j] += a[i] * b[j]
    return out


def fraction_poly_product(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def fraction_poly_sum(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def json_digest(value):
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def as_int_tree(value, label):
    if isinstance(value, bool):
        raise ValueError(f"boolean in integer tree {label}")
    if isinstance(value, int):
        return
    if isinstance(value, list):
        for item in value:
            as_int_tree(item, label)
        return
    raise ValueError(f"noninteger in {label}")


def verify(path):
    raw = path.read_bytes()
    cert = json.loads(raw)
    require(isinstance(cert, dict), "certificate root must be an object")
    require(cert.get("schema_version") == 1, "unsupported schema")
    require(
        cert.get("claim") == "A321614 Barker generating function and minimal order-10 recurrence for all n",
        "claim endpoint mismatch",
    )
    require(cert.get("arithmetic") == "integers and exact rational Bezout coefficients only", "arithmetic declaration mismatch")
    require(
        cert.get("board")
        == {
            "rows": 4,
            "columns": "2*n",
            "kings": "2*n",
            "attack": "Chebyshev distance at most 1",
            "group": ["identity", "horizontal", "vertical", "half_turn"],
            "square_n2_convention": "retain the order-four rectangle group",
        },
        "board/group metadata mismatch",
    )
    environment = cert.get("environment", {})
    require(environment.get("random_seed") is None, "certificate unexpectedly used randomness")
    require(environment.get("third_party_dependencies") == [], "certificate unexpectedly declares third-party dependencies")

    serialized_states = cert.get("local_states_zero_based")
    require(isinstance(serialized_states, list), "missing local states")
    states = direct_state_list()
    encoded_states = [[list(cell) for cell in s] for s in states]
    require(serialized_states == encoded_states, "state list is not the complete definition-level enumeration")
    require(len(states) == 12, "local state count is not 12")

    A = [[int(direct_compatible(s, t)) for t in states] for s in states]
    require(cert.get("adjacency") == A, "serialized adjacency mismatch")
    h = induced_permutation(states, horizontal=True)
    v = induced_permutation(states, vertical=True)
    rot = induced_permutation(states, horizontal=True, vertical=True)
    require(cert.get("involutions") == {"horizontal": h, "vertical": v, "half_turn": rot}, "involution mismatch")
    for name, perm in (("horizontal", h), ("vertical", v), ("half_turn", rot)):
        require(sorted(perm) == list(range(12)), f"{name} is not a permutation")
        require(all(perm[perm[i]] == i for i in range(12)), f"{name} is not an involution")
    require(
        all(A[i][j] == A[h[i]][h[j]] for i in range(12) for j in range(12)),
        "horizontal action does not preserve transfer edges",
    )
    require(
        all(A[i][j] == A[v[j]][v[i]] for i in range(12) for j in range(12)),
        "vertical reversal identity failed",
    )
    require(
        all(A[i][j] == A[rot[j]][rot[i]] for i in range(12) for j in range(12)),
        "half-turn reversal identity failed",
    )

    hfix = [i for i in range(12) if h[i] == i]
    vfix = [i for i in range(12) if v[i] == i]
    rfix = [i for i in range(12) if rot[i] == i]
    require(cert.get("fixed_state_indices") == {"horizontal": hfix, "vertical": vfix, "half_turn": rfix}, "fixed-state mismatch")
    AH = [[A[i][j] for j in hfix] for i in hfix]
    dv = [A[i][v[i]] for i in range(12)]
    dr = [A[i][rot[i]] for i in range(12)]
    require(cert.get("middle_edge_vectors") == {"vertical": dv, "half_turn": dr}, "middle-edge mismatch")

    TI, pI, lI = make_augmented(A, [1] * 12)
    TH, pH, lH = make_augmented(AH, [1] * len(AH))
    TV, pV, lV = make_augmented(A, dv)
    MV, xV, yV = make_interleaving(TV, pV, [0] + [int(i in vfix) for i in range(12)], lV)
    TR, pR, lR = make_augmented(A, dr)
    MR, xR, yR = make_interleaving(TR, pR, [0] + [int(i in rfix) for i in range(12)], lR)
    B = diagonal_join([TI, TH, MV, MR])
    b = pI + pH + xV + xR
    ell = lI + lH + yV + yR
    require(len(B) == 68, "unexpected global dimension")

    rep = cert.get("global_representation", {})
    require(rep.get("dimension") == 68, "serialized dimension mismatch")
    for obj, label in ((rep.get("matrix"), "matrix"), (rep.get("input"), "input"), (rep.get("output"), "output")):
        as_int_tree(obj, label)
    require(rep.get("matrix") == B, "serialized global matrix mismatch")
    require(rep.get("input") == b and rep.get("output") == ell, "serialized global vectors mismatch")
    require(rep.get("matrix_sha256") == json_digest(B), "matrix digest mismatch")
    require(rep.get("input_sha256") == json_digest(b), "input digest mismatch")
    require(rep.get("output_sha256") == json_digest(ell), "output digest mismatch")

    gf = cert.get("generating_function", {})
    factors = [[1, -1], [1, -1], [1, -3], [1, -3], [1, -3, 1], [1, -1, -1], [1, 0, -3]]
    require(gf.get("denominator_factors_ascending") == factors, "denominator factors mismatch")
    D = [1]
    for factor in factors:
        D = convolve(D, factor)
    N = convolve([1, -2], [1, -6, 17, -18, -2, 7, 6, -3])
    require(gf.get("denominator_ascending") == D, "expanded denominator mismatch")
    require(gf.get("numerator_ascending") == N, "expanded numerator mismatch")
    require(gf.get("recurrence_coefficients") == [-x for x in D[1:]], "recurrence mismatch")

    vectors = [b]
    for _ in range(10):
        vectors.append(matrix_vector(B, vectors[-1]))
    w = [sum(D[j] * vectors[10 - j][i] for j in range(11)) for i in range(68)]
    ch = cert.get("cayley_hamilton_observable_certificate", {})
    require(ch.get("annihilation_vector") == w, "annihilation vector mismatch")
    require(ch.get("annihilation_vector_sha256") == json_digest(w), "annihilation vector digest mismatch")
    observed = []
    current = w
    for _ in range(68):
        observed.append(scalar_product(ell, current))
        current = matrix_vector(B, current)
    require(observed == [0] * 68, "observable annihilation identity failed")
    require(ch.get("checked_moments") == 68 and ch.get("moments") == observed, "serialized moments mismatch")

    branch_reps = [(TI, pI, lI), (TH, pH, lH), (MV, xV, yV), (MR, xR, yR)]
    branch_names = ["identity", "horizontal", "vertical", "half_turn"]
    branch_values = {}
    for name, (M, initial, output) in zip(branch_names, branch_reps):
        values = []
        current = initial
        for _ in range(31):
            values.append(scalar_product(output, current))
            current = matrix_vector(M, current)
        branch_values[name] = values
    require({k: v[:22] for k, v in branch_values.items()} == cert.get("branch_values_n0_to_21"), "branch prefix mismatch")
    orbit = []
    for n in range(31):
        burnside_sum = sum(branch_values[name][n] for name in branch_names)
        require(burnside_sum % 4 == 0, f"Burnside nonintegrality at n={n}")
        orbit.append(burnside_sum // 4)
    published = [
        1, 4, 23, 106, 473, 1939, 7618, 28703, 105112, 375597,
        1316944, 4544124, 15474559, 52108212, 173799309, 574908646,
        1888125243, 6162032375, 19998659760, 64584817367,
        207655073310, 665017743665,
    ]
    require(orbit[:22] == published, "OEIS regression mismatch")
    require(cert.get("orbit_values_n0_to_21") == published, "serialized orbit prefix mismatch")
    numerator_from_series = [
        sum(D[j] * orbit[n - j] for j in range(min(n, len(D) - 1) + 1))
        for n in range(31)
    ]
    require(numerator_from_series[: len(N)] == N, "generating numerator mismatch")
    require(numerator_from_series[len(N) :] == [0] * (31 - len(N)), "nonzero rational tail")

    bezout = cert.get("minimality_bezout", {})
    def parse_fraction_list(data, label):
        require(isinstance(data, list) and data, f"missing {label}")
        answer = []
        for pair in data:
            require(isinstance(pair, list) and len(pair) == 2, f"bad fraction in {label}")
            n, d = pair
            require(type(n) is int and type(d) is int and d > 0, f"bad fraction integers in {label}")
            require(math.gcd(n, d) == 1, f"nonreduced fraction in {label}")
            answer.append(Fraction(n, d))
        return answer
    U = parse_fraction_list(bezout.get("U"), "U")
    V = parse_fraction_list(bezout.get("V"), "V")
    lhs = fraction_poly_sum(fraction_poly_product(U, N), fraction_poly_product(V, D))
    require(lhs == [Fraction(1)], "Bezout identity failed; denominator minimality is uncertified")

    cert_sha = hashlib.sha256(raw).hexdigest()
    code_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return {
        "status": "PASS",
        "certificate_sha256": cert_sha,
        "verifier_sha256": code_sha,
        "states": 12,
        "global_dimension": 68,
        "observable_zero_moments": 68,
        "oeis_prefix_terms": 22,
        "minimal_denominator_degree": len(D) - 1,
        "proof_assistant": False,
    }


def main():
    path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_CERT
    try:
        result = verify(path)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
