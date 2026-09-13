#!/usr/bin/env python3
"""Build the exact A321614 all-n matrix certificate.

Discovery and certification use integers only.  The independent verifier in
verify_certificate.py does not import this file.
"""

from __future__ import annotations

import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificate" / "a321614_certificate.json"


def states_from_definition():
    states = []
    for rt in (0, 1):
        for rb in (2, 3):
            for ct in (0, 1):
                for cb in (0, 1):
                    state = ((rt, ct), (rb, cb))
                    if max(abs(rt - rb), abs(ct - cb)) > 1:
                        states.append(state)
    return states


def compatible(left, right):
    return all(
        max(abs(rl - rr), abs(cl - (2 + cr))) > 1
        for rl, cl in left
        for rr, cr in right
    )


def adjacency(states):
    return [[int(compatible(s, t)) for t in states] for s in states]


def transform_state(state, kind):
    out = []
    for r, c in state:
        if kind in ("h", "r"):
            r = 3 - r
        if kind in ("v", "r"):
            c = 1 - c
        out.append((r, c))
    return tuple(sorted(out))


def permutation(states, kind):
    index = {s: i for i, s in enumerate(states)}
    return [index[transform_state(s, kind)] for s in states]


def zeros(rows, cols):
    return [[0] * cols for _ in range(rows)]


def mat_vec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def block_diag(blocks):
    size = sum(len(block) for block in blocks)
    out = zeros(size, size)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            out[offset + i][offset : offset + len(block)] = row
        offset += len(block)
    return out


def augmented_transition(matrix, entrance):
    """Represent e_0=1 and e_n=1^T A^(n-1) entrance for n>=1."""
    d = len(matrix)
    out = zeros(d + 1, d + 1)
    for i in range(d):
        out[i + 1][0] = entrance[i]
        out[i + 1][1:] = matrix[i]
    initial = [1] + [0] * d
    observable = [1] + [1] * d
    return out, initial, observable


def interleaved_transition(augmented, even_initial, odd_initial, observable):
    """Represent z_2m=l*T^m*p and z_(2m+1)=l*T^m*q."""
    d = len(augmented)
    out = zeros(2 * d, 2 * d)
    for i in range(d):
        out[i][d + i] = 1
        out[d + i][0:d] = augmented[i]
    initial = even_initial + odd_initial
    output = observable + [0] * d
    return out, initial, output


def poly_mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def trim(poly):
    poly = list(poly)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_divmod_fraction(dividend, divisor):
    a = trim([Fraction(x) for x in dividend])
    b = trim([Fraction(x) for x in divisor])
    if b == [0]:
        raise ZeroDivisionError("zero polynomial")
    if len(a) < len(b):
        return [Fraction(0)], a
    q = [Fraction(0)] * (len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        shift = len(a) - len(b)
        coeff = a[-1] / b[-1]
        q[shift] += coeff
        for i, value in enumerate(b):
            a[i + shift] -= coeff * value
        a = trim(a)
    return trim(q), a


def poly_sub(left, right):
    out = [Fraction(0)] * max(len(left), len(right))
    for i in range(len(left)):
        out[i] += left[i]
    for i in range(len(right)):
        out[i] -= right[i]
    return trim(out)


def poly_mul_fraction(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(out)


def poly_xgcd(left, right):
    old_r, r = [Fraction(x) for x in left], [Fraction(x) for x in right]
    old_s, s = [Fraction(1)], [Fraction(0)]
    old_t, t = [Fraction(0)], [Fraction(1)]
    while trim(r) != [0]:
        q, rem = poly_divmod_fraction(old_r, r)
        old_r, r = r, rem
        old_s, s = s, poly_sub(old_s, poly_mul_fraction(q, s))
        old_t, t = t, poly_sub(old_t, poly_mul_fraction(q, t))
    scale = old_r[-1]
    return (
        [x / scale for x in trim(old_r)],
        [x / scale for x in trim(old_s)],
        [x / scale for x in trim(old_t)],
    )


def fraction_list(values):
    return [[x.numerator, x.denominator] for x in values]


def sha256_json(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def build():
    states = states_from_definition()
    assert len(states) == 12
    adj = adjacency(states)
    h = permutation(states, "h")
    v = permutation(states, "v")
    r = permutation(states, "r")

    horizontal_indices = [i for i in range(12) if h[i] == i]
    horizontal_matrix = [[adj[i][j] for j in horizontal_indices] for i in horizontal_indices]
    vertical_middle = [adj[i][v[i]] for i in range(12)]
    rotation_middle = [adj[i][r[i]] for i in range(12)]
    vertical_centers = [int(v[i] == i) for i in range(12)]
    rotation_centers = [int(r[i] == i) for i in range(12)]

    identity_T, identity_p, identity_l = augmented_transition(adj, [1] * 12)
    horizontal_T, horizontal_p, horizontal_l = augmented_transition(
        horizontal_matrix, [1] * len(horizontal_indices)
    )
    vertical_T, vertical_p, vertical_l = augmented_transition(adj, vertical_middle)
    vertical_M, vertical_input, vertical_output = interleaved_transition(
        vertical_T, vertical_p, [0] + vertical_centers, vertical_l
    )
    rotation_T, rotation_p, rotation_l = augmented_transition(adj, rotation_middle)
    rotation_M, rotation_input, rotation_output = interleaved_transition(
        rotation_T, rotation_p, [0] + rotation_centers, rotation_l
    )

    global_matrix = block_diag([identity_T, horizontal_T, vertical_M, rotation_M])
    global_input = identity_p + horizontal_p + vertical_input + rotation_input
    global_output = identity_l + horizontal_l + vertical_output + rotation_output
    dimension = len(global_matrix)
    assert dimension == 68

    factors = [[1, -1], [1, -1], [1, -3], [1, -3], [1, -3, 1], [1, -1, -1], [1, 0, -3]]
    denominator = [1]
    for factor in factors:
        denominator = poly_mul(denominator, factor)
    numerator = poly_mul([1, -2], [1, -6, 17, -18, -2, 7, 6, -3])
    assert denominator == [1, -12, 54, -98, -17, 346, -505, 210, 120, -126, 27]
    assert numerator == [1, -8, 29, -52, 34, 11, -8, -15, 6]

    powers = [global_input]
    for _ in range(10):
        powers.append(mat_vec(global_matrix, powers[-1]))
    annihilation_vector = [0] * dimension
    for j, coeff in enumerate(denominator):
        power = powers[10 - j]
        for i in range(dimension):
            annihilation_vector[i] += coeff * power[i]
    moments = []
    probe = annihilation_vector
    for _ in range(dimension):
        moments.append(dot(global_output, probe))
        probe = mat_vec(global_matrix, probe)
    assert moments == [0] * dimension

    branch_specs = [
        (identity_T, identity_p, identity_l),
        (horizontal_T, horizontal_p, horizontal_l),
        (vertical_M, vertical_input, vertical_output),
        (rotation_M, rotation_input, rotation_output),
    ]
    branches = []
    for matrix, initial, output in branch_specs:
        values = []
        current = initial
        for _ in range(31):
            values.append(dot(output, current))
            current = mat_vec(matrix, current)
        branches.append(values)
    orbit_values = [sum(values) // 4 for values in zip(*branches)]
    assert all(sum(values) % 4 == 0 for values in zip(*branches))
    expected_prefix = [
        1, 4, 23, 106, 473, 1939, 7618, 28703, 105112, 375597,
        1316944, 4544124, 15474559, 52108212, 173799309, 574908646,
        1888125243, 6162032375, 19998659760, 64584817367,
        207655073310, 665017743665,
    ]
    assert orbit_values[:22] == expected_prefix
    convolution = []
    for n in range(31):
        convolution.append(
            sum(denominator[j] * orbit_values[n - j] for j in range(min(n, 10) + 1))
        )
    assert convolution[: len(numerator)] == numerator
    assert convolution[len(numerator) :] == [0] * (31 - len(numerator))

    gcd, bezout_n, bezout_d = poly_xgcd(numerator, denominator)
    assert gcd == [Fraction(1)]

    certificate = {
        "schema_version": 1,
        "claim": "A321614 Barker generating function and minimal order-10 recurrence for all n",
        "arithmetic": "integers and exact rational Bezout coefficients only",
        "board": {
            "rows": 4,
            "columns": "2*n",
            "kings": "2*n",
            "attack": "Chebyshev distance at most 1",
            "group": ["identity", "horizontal", "vertical", "half_turn"],
            "square_n2_convention": "retain the order-four rectangle group",
        },
        "local_states_zero_based": [[list(cell) for cell in state] for state in states],
        "adjacency": adj,
        "involutions": {"horizontal": h, "vertical": v, "half_turn": r},
        "fixed_state_indices": {
            "horizontal": horizontal_indices,
            "vertical": [i for i, x in enumerate(vertical_centers) if x],
            "half_turn": [i for i, x in enumerate(rotation_centers) if x],
        },
        "middle_edge_vectors": {"vertical": vertical_middle, "half_turn": rotation_middle},
        "global_representation": {
            "dimension": dimension,
            "matrix": global_matrix,
            "input": global_input,
            "output": global_output,
            "matrix_sha256": sha256_json(global_matrix),
            "input_sha256": sha256_json(global_input),
            "output_sha256": sha256_json(global_output),
        },
        "generating_function": {
            "denominator_factors_ascending": factors,
            "denominator_ascending": denominator,
            "numerator_ascending": numerator,
            "recurrence_coefficients": [-x for x in denominator[1:]],
        },
        "cayley_hamilton_observable_certificate": {
            "polynomial_vector_convention": "w=sum(D[j]*B^(10-j)*input,j=0..10)",
            "annihilation_vector": annihilation_vector,
            "checked_moments": dimension,
            "moments": moments,
            "annihilation_vector_sha256": sha256_json(annihilation_vector),
        },
        "minimality_bezout": {
            "convention": "U*numerator + V*denominator = 1; coefficients ascending",
            "U": fraction_list(bezout_n),
            "V": fraction_list(bezout_d),
        },
        "branch_values_n0_to_21": {
            "identity": branches[0][:22],
            "horizontal": branches[1][:22],
            "vertical": branches[2][:22],
            "half_turn": branches[3][:22],
        },
        "orbit_values_n0_to_21": orbit_values[:22],
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "random_seed": None,
            "third_party_dependencies": [],
        },
    }
    return certificate


def main():
    certificate = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
    print(f"BUILT {OUT.relative_to(ROOT)}")
    print(f"dimension={certificate['global_representation']['dimension']}")
    print(f"certificate_sha256={digest}")
    print("observable_moments=68 zeros")
    print("oeis_prefix=22/22 exact")
    print("gcd(numerator,denominator)=1")


if __name__ == "__main__":
    main()
