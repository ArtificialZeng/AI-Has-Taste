#!/usr/bin/env python3
"""Exact owner-side analysis of the unreviewed handoff sections E and F.

The finite computations in this file are falsification tests.  Universal
claims are justified separately in proof/handoff_extension_rederivation.md.
"""

import argparse
import hashlib
import json
import platform


KNOWN_ZEROS = [0, 6, 11, 23, 36, 42, 48, 54]
PRIMES = [5, 11, 103, 1_000_003]


def recurrence(limit):
    values = [0, 1]
    for n in range(2, limit + 1):
        values.append((values[-1] ^ n) - values[-2])
    return values


def t_map(q, pair):
    x, y = pair
    return y, (y ^ q) - x


def a_map(q, pair):
    return t_map(q, t_map(q, pair))


def tau(pair):
    return pair[0], pair[1] - 1


def b_map(q, pair):
    if q % 3 == 0:
        return tau(a_map(q, a_map(q, pair)))
    return a_map(q, tau(a_map(q, pair)))


def delta_closed(q, v):
    if v == 0:
        return -2 * q - 1
    t = (abs(v) & -abs(v)).bit_length() - 1
    return (1 << (t + 1)) * ((q >> t) & 1) - 2 * (q % (1 << t)) - 1


def sequence_value(values, name, q):
    if name == "U":
        numerator = values[6 * q + 1] - 1
    elif name == "V":
        numerator = values[12 * q + 8] - 1
    else:
        assert name == "W"
        numerator = values[6 * q + 3] + 1
    assert numerator % 4 == 0
    return numerator // 4


def matrix_digest(matrix):
    encoded = "\n".join(",".join(str(value) for value in row) for row in matrix)
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


def kernel_matrix(values, name, depth_max):
    size = (1 << (depth_max + 1)) - 1
    return [
        [sequence_value(values, name, (1 << e) * j + r) for j in range(size)]
        for e in range(depth_max + 1)
        for r in range(1 << e)
    ]


def bareiss_determinant(matrix):
    """Fraction-free exact determinant with explicit row swaps."""
    size = len(matrix)
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot_row = next((r for r in range(column, size) if a[r][column]), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            a[column], a[pivot_row] = a[pivot_row], a[column]
            sign = -sign
        pivot = a[column][column]
        for row in range(column + 1, size):
            for j in range(column + 1, size):
                numerator = a[row][j] * pivot - a[row][column] * a[column][j]
                assert numerator % previous == 0
                a[row][j] = numerator // previous
            a[row][column] = 0
        previous = pivot
    return sign * a[-1][-1]


def valuation_two(value):
    assert value
    value = abs(value)
    return (value & -value).bit_length() - 1


def maximum_sequence_index(depth_max):
    size = (1 << (depth_max + 1)) - 1
    maximum_q = (1 << depth_max) * (size - 1) + (1 << depth_max) - 1
    return 12 * maximum_q + 8


def check_second_strip(values, direct_limit, maximum_window):
    g = [value // 4 for value in values[: direct_limit + 1]]
    delta_counts = {str(residue): 0 for residue in range(6)}
    recurrence_cases = 0
    for m in range(1, direct_limit // 2):
        previous = (g[2 * m - 2], g[2 * m - 1])
        predicted = a_map(m // 2, previous)
        delta = int(m % 6 in {1, 2, 4})
        predicted = predicted[0], predicted[1] - delta
        actual = g[2 * m], g[2 * m + 1]
        assert predicted == actual
        delta_counts[str(m % 6)] += 1
        recurrence_cases += 1

    grouped_cases = 0
    for q in range(1, (direct_limit - 3) // 4 + 1):
        source = (g[4 * q - 2], g[4 * q - 1])
        actual = g[4 * q + 2], g[4 * q + 3]
        assert b_map(q, source) == actual
        grouped_cases += 1

    delta_cases = 0
    for q in range(256):
        for v in range(-1024, 1025):
            assert ((v - 1) ^ q) - (v ^ q) == delta_closed(q, v)
            delta_cases += 1

    window_obstructions = []
    for width in range(maximum_window + 1):
        s = (width + 1) // 2
        q = 1 << (2 * s)
        p0, p1 = (0, q), (q, 0)
        mask = (1 << width) - 1
        assert tuple(value & mask for value in p0) == tuple(value & mask for value in p1)
        assert q % 3 == 1
        a2_p0 = a_map(q, a_map(q, p0))
        a2_p1 = a_map(q, a_map(q, p1))
        b_p0, b_p1 = b_map(q, p0), b_map(q, p1)
        correction_p0 = tuple(b_p0[i] - a2_p0[i] for i in range(2))
        correction_p1 = tuple(b_p1[i] - a2_p1[i] for i in range(2))
        assert correction_p0 == (-2 * q - 1, 0)
        assert correction_p1 == (2 * q - 1, 0)
        assert correction_p0 != correction_p1
        window_obstructions.append({
            "width": width,
            "q": q,
            "state_0": list(p0),
            "state_1": list(p1),
            "correction_0": list(correction_p0),
            "correction_1": list(correction_p1),
        })

    borrow_cases = 0
    for z in range(-4096, 4097):
        low_bit = z & 1
        high = (z - low_bit) // 2
        for borrow in (0, 1):
            propagated = borrow * (1 - low_bit)
            reconstructed = 2 * (high - propagated) + (low_bit ^ borrow)
            assert z - borrow == reconstructed
            borrow_cases += 1

    q = 12_286
    orbit_state = (g[49_142], g[49_143])
    orbit_image = a_map(q, orbit_state)
    assert orbit_state == (-8_388_608, -2_666_497)
    assert orbit_image == (5_726_209, 1 << 23)
    assert b_map(4, (0, 4)) == (-5, 0)
    assert b_map(4, (4, 0)) == (7, 0)
    assert a_map(4, a_map(4, (0, 4))) == (4, 0)
    assert a_map(4, a_map(4, (4, 0))) == (0, 0)

    return {
        "second_strip_recurrence_cases": recurrence_cases,
        "residue_counts": delta_counts,
        "grouped_pair_cases": grouped_cases,
        "delta_closed_form_cases": delta_cases,
        "fixed_window_obstructions": window_obstructions,
        "borrow_identity_cases": borrow_cases,
        "small_q4_example": {
            "B4_[0,4]": [-5, 0],
            "B4_[4,0]": [7, 0],
            "A4_squared_[0,4]": [4, 0],
            "A4_squared_[4,0]": [0, 0],
        },
        "distinguished_orbit_borrow": {
            "q": q,
            "R_24571": list(orbit_state),
            "A_q_R_24571": list(orbit_image),
            "power_of_two_coordinate": 1 << 23,
        },
    }


def normalized_layer_checks(values, depth_max):
    records = {}
    total_cases = 0
    for name in ("U", "V", "W"):
        layers = []
        for e in range(depth_max + 1):
            for scale in range(depth_max + 1):
                exponent = e + scale if name == "V" else e + scale - 1
                if exponent < 0:
                    layers.append({
                        "row_depth": e,
                        "column_scale": scale,
                        "normalizing_exponent": None,
                        "quotient_bit": None,
                        "cases": 0,
                    })
                    continue
                bits = set()
                cases = 0
                size = (1 << (depth_max + 1)) - 1
                for r in range(1 << e):
                    for offset in range(1 << scale):
                        column = (1 << scale) + offset
                        if column >= size:
                            continue
                        current_q = (1 << e) * column + r
                        parent_q = (1 << e) * offset + r
                        difference = (
                            sequence_value(values, name, current_q)
                            - sequence_value(values, name, parent_q)
                        )
                        assert difference % (1 << exponent) == 0
                        bits.add((difference >> exponent) & 1)
                        cases += 1
                assert len(bits) == 1
                quotient_bit = next(iter(bits))
                if name == "U":
                    k, phase = e + scale + 1, 1
                elif name == "W":
                    k, phase = e + scale + 1, 0
                else:
                    k, phase = e + scale + 2, 2
                expected = ((values[phase + 3 * (1 << k)] - values[phase]) >> k) & 1
                assert quotient_bit == expected
                total_cases += cases
                layers.append({
                    "row_depth": e,
                    "column_scale": scale,
                    "normalizing_exponent": exponent,
                    "quotient_bit": quotient_bit,
                    "cases": cases,
                })
        records[name] = layers
    return records, total_cases


def determinant_checks(values, maximum_depth):
    records = {}
    for depth in range(2, maximum_depth + 1):
        size = (1 << (depth + 1)) - 1
        records[str(depth)] = {}
        for name in ("U", "V", "W"):
            matrix = kernel_matrix(values, name, depth)
            determinant = bareiss_determinant(matrix)
            assert determinant
            valuation = valuation_two(determinant)
            handoff_bound = (
                (4 * depth - 2) * (1 << depth) - 3 * depth + 1
                if name == "V"
                else (4 * depth - 4) * (1 << depth) - 4 * depth + 3
            )
            proved_bound = (
                handoff_bound
                if name == "V"
                else (4 * depth - 4) * (1 << depth) - 3 * depth + 3
            )
            assert valuation >= proved_bound >= handoff_bound
            records[str(depth)][name] = {
                "dimension": size,
                "matrix_sha256": matrix_digest(matrix),
                "determinant": str(determinant),
                "determinant_bit_length": abs(determinant).bit_length(),
                "valuation_two": valuation,
                "handoff_lower_bound": handoff_bound,
                "proved_lower_bound": proved_bound,
                "residues": {str(prime): determinant % prime for prime in PRIMES},
            }
    assert records["2"]["U"]["residues"]["103"] == 0
    assert records["3"]["U"]["residues"]["103"] == 47
    assert records["2"]["V"]["residues"]["5"] == 0
    assert records["3"]["V"]["residues"]["5"] == 3
    assert records["2"]["W"]["residues"]["11"] == 0
    assert records["3"]["W"]["residues"]["11"] == 7
    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct-limit", type=int, default=200_000)
    parser.add_argument("--max-window", type=int, default=12)
    parser.add_argument("--max-layer-depth", type=int, default=8)
    parser.add_argument("--max-determinant-depth", type=int, default=4)
    parser.add_argument("--output")
    args = parser.parse_args()
    assert args.direct_limit >= 49_143
    assert 2 <= args.max_determinant_depth <= 4
    assert args.max_layer_depth >= args.max_determinant_depth

    sequence_limit = max(
        args.direct_limit,
        maximum_sequence_index(args.max_layer_depth),
    )
    values = recurrence(sequence_limit)
    second_strip = check_second_strip(values, args.direct_limit, args.max_window)
    layers, layer_cases = normalized_layer_checks(values, args.max_layer_depth)
    determinants = determinant_checks(values, args.max_determinant_depth)
    zeros = [n for n, value in enumerate(values[: args.direct_limit + 1]) if value == 0]
    assert zeros == KNOWN_ZEROS

    record = {
        "schema_version": 1,
        "purpose": "independent owner falsification and rederivation of handoff sections E and F",
        "handoff_status": "unreviewed external material; only rederived claims are adopted",
        "parameters": vars(args) | {"output": None, "sequence_limit": sequence_limit},
        "semantics": "Python arbitrary-precision infinite-width signed XOR",
        "zeros_through_direct_limit": zeros,
        "second_strip": second_strip,
        "normalized_determinant_layers": {
            "total_entry_checks": layer_cases,
            "records": layers,
            "meaning": "After descending binary-parent column subtraction, the first normalized quotient bit is constant on each row-depth/column-scale block.",
        },
        "exact_determinants": determinants,
        "proved_partial_consequences": [
            "The second-strip recurrence and grouped map hold for all indices by the six-residue derivation.",
            "No correction depending only on a fixed low-bit state window and q mod 3 can represent the internal translation in B_q for all integer states.",
            "For every E>=2, the V determinant has the handoff's stated 2-adic divisor; U and W obey the stronger exponent (4E-4)2^E-3E+3.",
        ],
        "limitations": [
            "The fixed-window obstruction concerns all-state static affine corrections; it does not exclude a bit-serial transducer, an unbounded carry state, or special closure on the distinguished orbit.",
            "Large 2-adic divisibility does not prove any determinant nonzero and therefore does not prove C002.",
            "The finite determinant and normalized-layer checks do not classify the infinite zero tail.",
        ],
        "python": platform.python_version(),
    }
    output = json.dumps(record, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
