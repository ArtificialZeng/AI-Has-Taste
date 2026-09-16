#!/usr/bin/env python3
"""Independent AND-formula verifier for handoff E/F exact evidence."""

import hashlib
import json
import sys

import sympy as sp


def xor_and(x, y):
    return x + y - 2 * (x & y)


def recurrence(limit):
    values = [0, 1]
    for n in range(2, limit + 1):
        values.append(xor_and(values[-1], n) - values[-2])
    return values


def t_map(q, pair):
    x, y = pair
    return y, xor_and(y, q) - x


def a_map(q, pair):
    return t_map(q, t_map(q, pair))


def tau(pair):
    return pair[0], pair[1] - 1


def b_map(q, pair):
    first = a_map(q, pair)
    return tau(a_map(q, first)) if q % 3 == 0 else a_map(q, tau(first))


def sequence_value(values, name, q):
    indices = {"U": 6 * q + 1, "V": 12 * q + 8, "W": 6 * q + 3}
    constants = {"U": -1, "V": -1, "W": 1}
    numerator = values[indices[name]] + constants[name]
    assert numerator % 4 == 0
    return numerator // 4


def kernel_matrix(values, name, depth):
    size = (1 << (depth + 1)) - 1
    rows = []
    for e in range(depth + 1):
        for r in range(1 << e):
            rows.append([
                sequence_value(values, name, (1 << e) * column + r)
                for column in range(size)
            ])
    return rows


def matrix_digest(matrix):
    encoded = "\n".join(",".join(map(str, row)) for row in matrix)
    return hashlib.sha256(encoded.encode("ascii")).hexdigest()


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/handoff-extensions-evidence.json"
with open(path, encoding="utf-8") as handle:
    claim = json.load(handle)
assert claim["schema_version"] == 1
parameters = claim["parameters"]
values = recurrence(parameters["sequence_limit"])

direct_limit = parameters["direct_limit"]
zeros = [n for n, value in enumerate(values[: direct_limit + 1]) if value == 0]
assert zeros == claim["zeros_through_direct_limit"]
g = [value // 4 for value in values[: direct_limit + 1]]

recurrence_cases = 0
for m in range(1, direct_limit // 2):
    previous = g[2 * m - 2], g[2 * m - 1]
    image = a_map(m // 2, previous)
    delta = int(m % 6 in {1, 2, 4})
    assert (image[0], image[1] - delta) == (g[2 * m], g[2 * m + 1])
    recurrence_cases += 1
assert recurrence_cases == claim["second_strip"]["second_strip_recurrence_cases"]

grouped_cases = 0
for q in range(1, (direct_limit - 3) // 4 + 1):
    assert b_map(q, (g[4 * q - 2], g[4 * q - 1])) == (g[4 * q + 2], g[4 * q + 3])
    grouped_cases += 1
assert grouped_cases == claim["second_strip"]["grouped_pair_cases"]

for item in claim["second_strip"]["fixed_window_obstructions"]:
    q, width = item["q"], item["width"]
    states = tuple(item["state_0"]), tuple(item["state_1"])
    mask = (1 << width) - 1
    assert tuple(x & mask for x in states[0]) == tuple(x & mask for x in states[1])
    for state, expected in zip(states, (item["correction_0"], item["correction_1"])):
        baseline = a_map(q, a_map(q, state))
        actual = b_map(q, state)
        assert [actual[i] - baseline[i] for i in range(2)] == expected

orbit = claim["second_strip"]["distinguished_orbit_borrow"]
assert [g[49_142], g[49_143]] == orbit["R_24571"]
assert list(a_map(orbit["q"], tuple(orbit["R_24571"]))) == orbit["A_q_R_24571"]

layer_cases = 0
depth_max = parameters["max_layer_depth"]
size = (1 << (depth_max + 1)) - 1
for name, records in claim["normalized_determinant_layers"]["records"].items():
    for item in records:
        exponent = item["normalizing_exponent"]
        if exponent is None:
            assert name in {"U", "W"} and item["row_depth"] == item["column_scale"] == 0
            continue
        e, scale = item["row_depth"], item["column_scale"]
        seen = set()
        for offset in range(1 << scale):
            column = (1 << scale) + offset
            if column >= size:
                continue
            for r in range(1 << e):
                high = sequence_value(values, name, (1 << e) * column + r)
                low = sequence_value(values, name, (1 << e) * offset + r)
                difference = high - low
                assert difference % (1 << exponent) == 0
                seen.add((difference // (1 << exponent)) % 2)
                layer_cases += 1
        assert seen == {item["quotient_bit"]}
        assert item["cases"] == sum(1 for offset in range(1 << scale)
                                      if (1 << scale) + offset < size) * (1 << e)
assert layer_cases == claim["normalized_determinant_layers"]["total_entry_checks"]

for depth_text, by_name in claim["exact_determinants"].items():
    depth = int(depth_text)
    for name, expected in by_name.items():
        matrix = kernel_matrix(values, name, depth)
        assert matrix_digest(matrix) == expected["matrix_sha256"]
        determinant = int(sp.Matrix(matrix).det(method="domain-ge"))
        assert determinant == int(expected["determinant"])
        assert determinant != 0
        valuation = (abs(determinant) & -abs(determinant)).bit_length() - 1
        assert valuation == expected["valuation_two"]
        assert valuation >= expected["proved_lower_bound"] >= expected["handoff_lower_bound"]
        for prime, residue in expected["residues"].items():
            assert determinant % int(prime) == residue

print(json.dumps({
    "status": "PASS",
    "direct_limit": direct_limit,
    "layer_depth": depth_max,
    "normalized_entry_checks": layer_cases,
    "determinant_depth": parameters["max_determinant_depth"],
    "zeros": zeros,
}, separators=(",", ":")))
