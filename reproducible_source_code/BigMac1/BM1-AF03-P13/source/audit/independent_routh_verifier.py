#!/usr/bin/env python3
"""Independent exact audit of the length-10 counterexample.

Trust boundary:

* input contains only the literal word and target parameters;
* h* is rebuilt from the source poset via order-ideal multichains;
* the Ehrhart factor is rebuilt with integer polynomial arithmetic;
* an exact Routh table certifies two roots outside the y-disk.

This file imports neither discovery code nor discovery data.  It uses only
the Python standard library.  Coefficient lists are ascending.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def reject(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"REJECT: {message}")


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int]) -> list[int]:
    answer = [0] * max(len(a), len(b))
    for index, coefficient in enumerate(a):
        answer[index] += coefficient
    for index, coefficient in enumerate(b):
        answer[index] += coefficient
    return trim(answer)


def multiply(a: list[int], b: list[int]) -> list[int]:
    answer = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            answer[i + j] += left * right
    return trim(answer)


def power(poly: list[int], exponent: int) -> list[int]:
    answer = [1]
    while exponent:
        if exponent & 1:
            answer = multiply(answer, poly)
        poly = multiply(poly, poly)
        exponent //= 2
    return answer


def shift(poly: list[int], displacement: int) -> list[int]:
    """Return p(x+displacement)."""
    answer = [0]
    for degree, coefficient in enumerate(poly):
        term = [
            coefficient
            * math.comb(degree, new_degree)
            * displacement ** (degree - new_degree)
            for new_degree in range(degree + 1)
        ]
        answer = add(answer, term)
    return answer


def covers(word: str) -> list[tuple[int, int]]:
    edges = [(1, 0), (2, 0), (3, 1), (3, 2)]
    for length, letter in enumerate(word, 1):
        edges.extend(
            [(2 * length + 3, 2 * length + 1), (2 * length + 3, 2 * length + 2)]
        )
        turn = (length == 1 and letter == "L") or (
            length >= 2 and word[length - 2] != letter
        )
        edges.append((2 * length + 2, 2 * length - 1 if turn else 2 * length))
    return edges


def order_ideals(word: str) -> list[int]:
    vertex_count = 2 * len(word) + 4
    successors = [[] for _ in range(vertex_count)]
    indegrees = [0] * vertex_count
    predecessor_closures = [0] * vertex_count
    for lower, upper in covers(word):
        successors[lower].append(upper)
        indegrees[upper] += 1
    ready = [vertex for vertex in range(vertex_count) if indegrees[vertex] == 0]
    topological: list[int] = []
    while ready:
        vertex = ready.pop()
        topological.append(vertex)
        for upper in successors[vertex]:
            indegrees[upper] -= 1
            if indegrees[upper] == 0:
                ready.append(upper)
    reject(len(topological) == vertex_count, "source cover relation is cyclic")
    for lower in topological:
        for upper in successors[lower]:
            predecessor_closures[upper] |= predecessor_closures[lower] | (1 << lower)
    ideals = [0]
    for vertex in topological:
        previous = ideals[:]
        ideals.extend(
            ideal | (1 << vertex)
            for ideal in previous
            if predecessor_closures[vertex] & ~ideal == 0
        )
    # Keep the independent verifier runnable on older system Python versions;
    # int.bit_count() is not available on every deployed interpreter.
    return sorted(set(ideals), key=lambda ideal: (bin(ideal).count("1"), ideal))


def reconstruct_hstar(word: str) -> tuple[list[int], list[int], int]:
    dimension = 2 * len(word) + 4
    ideals = order_ideals(word)
    positions = {ideal: index for index, ideal in enumerate(ideals)}
    subideals = [
        [index for index, left in enumerate(ideals) if left & ~right == 0]
        for right in ideals
    ]
    counts = [0] * len(ideals)
    counts[positions[0]] = 1
    full = (1 << dimension) - 1
    ehrhart_values: list[int] = []
    for _ in range(dimension + 1):
        counts = [sum(counts[index] for index in predecessors) for predecessors in subideals]
        ehrhart_values.append(counts[positions[full]])
    hstar = [
        sum(
            (-1) ** offset
            * math.comb(dimension + 1, offset)
            * ehrhart_values[degree - offset]
            for offset in range(degree + 1)
        )
        for degree in range(dimension + 1)
    ]
    reject(not any(hstar[len(word) + 2 :]), "unexpected h* tail")
    return hstar[: len(word) + 2], ehrhart_values, len(ideals)


def ehrhart_numerator(hstar: list[int], dimension: int) -> list[int]:
    """Return dimension! L(t)."""
    answer = [0]
    for index, coefficient in enumerate(hstar):
        term = [1]
        for offset in range(dimension):
            term = multiply(term, [dimension - index - offset, 1])
        answer = add(answer, [coefficient * value for value in term])
    return answer


def cayley(radial: list[int], boundary: int) -> list[int]:
    degree = len(radial) - 1
    answer = [0]
    for index, coefficient in enumerate(radial):
        term = multiply(power([1, 1], index), power([-1, 1], degree - index))
        answer = add(answer, [coefficient * boundary**index * value for value in term])
    content = 0
    for coefficient in answer:
        content = math.gcd(content, abs(coefficient))
    reject(content > 0, "zero Cayley polynomial")
    answer = [coefficient // content for coefficient in answer]
    if answer[-1] < 0:
        answer = [-coefficient for coefficient in answer]
    return answer


def routh(poly: list[int]) -> tuple[list[list[Fraction]], int]:
    degree = len(poly) - 1
    descending = list(reversed(poly))
    columns = (degree + 2) // 2
    table = [[Fraction(0) for _ in range(columns)] for _ in range(degree + 1)]
    row0 = [Fraction(descending[index]) for index in range(0, degree + 1, 2)]
    row1 = [Fraction(descending[index]) for index in range(1, degree + 1, 2)]
    table[0][: len(row0)] = row0
    table[1][: len(row1)] = row1
    for row in range(2, degree + 1):
        reject(table[row - 1][0] != 0, "singular Routh first column")
        for column in range(columns - 1):
            table[row][column] = (
                table[row - 1][0] * table[row - 2][column + 1]
                - table[row - 2][0] * table[row - 1][column + 1]
            ) / table[row - 1][0]
        reject(any(value != 0 for value in table[row]), "Routh zero row")
    first = [row[0] for row in table]
    reject(all(value != 0 for value in first), "zero in final Routh first column")
    signs = [1 if value > 0 else -1 for value in first]
    changes = sum(left != right for left, right in zip(signs, signs[1:]))
    return table, changes


def parse_fraction(value: object, label: str) -> Fraction:
    reject(isinstance(value, list) and len(value) == 2, f"{label} must be [num,den]")
    numerator, denominator = value
    reject(type(numerator) is int and type(denominator) is int, f"{label} must be integral")
    reject(denominator > 0, f"{label} denominator must be positive")
    return Fraction(numerator, denominator)


def verify(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    try:
        data = json.loads(raw)
    except Exception as error:
        raise SystemExit(f"REJECT: invalid JSON: {error}") from error
    reject(type(data) is dict, "top-level JSON must be an object")
    expected_keys = {"schema", "word", "length", "dimension", "center", "radius"}
    reject(set(data) == expected_keys, "missing or unknown top-level field")
    reject(type(data["schema"]) is str, "schema must be a string")
    reject(data["schema"] == "snake-ehrhart-routh-audit-v1", "unsupported schema")
    reject(type(data["word"]) is str, "word must be a string")
    reject(data["word"] == "LRLRLRLRLR", "audit is pinned to the declared witness")
    reject(type(data["length"]) is int and type(data["dimension"]) is int, "endpoint fields must be integers")
    reject(data["length"] == 10 and data["dimension"] == 24, "wrong endpoint")
    reject(parse_fraction(data["center"], "center") == -7, "wrong center")
    reject(parse_fraction(data["radius"], "radius") == 6, "wrong radius")

    hstar, values, ideal_count = reconstruct_hstar(data["word"])
    expected_hstar = [1, 21, 181, 833, 2241, 3653, 3653, 2241, 833, 181, 21, 1]
    reject(hstar == expected_hstar, "independent h* reconstruction mismatch")
    reject(ideal_count == 46, "unexpected order-ideal count")

    numerator = ehrhart_numerator(hstar, 24)
    centered = shift(numerator, -7)
    reject(all(centered[degree] == 0 for degree in range(1, 25, 2)), "symmetry failed")
    primitive_q = [23924096, 70801492, 10769815, 923223, 25789, 385]
    fixed = [1]
    for square in range(7):
        fixed = multiply(fixed, [-square * square, 1])
    right_side = [36 * value for value in multiply(fixed, primitive_q)]
    reject(centered[::2] == right_side, "exact factorization failed")

    transformed = cayley(primitive_q, 36)
    expected_transformed = [
        362656325,
        1123599050,
        2899674560,
        6584369218,
        8365445947,
        3943732660,
    ]
    reject(transformed == expected_transformed, "Cayley reconstruction mismatch")
    reject(all(coefficient > 0 for coefficient in transformed), "positive-real-axis exclusion failed")
    table, outside_count = routh(transformed)
    reject(outside_count == 2, "Routh count is not the required conjugate pair")

    first = [[value.numerator, value.denominator] for value in (row[0] for row in table)]
    return {
        "status": "INDEPENDENT_EXACT_AUDIT_PASS",
        "word": data["word"],
        "order_ideals": ideal_count,
        "ehrhart_values_sha256": hashlib.sha256(
            json.dumps(values, separators=(",", ":")).encode()
        ).hexdigest(),
        "hstar": hstar,
        "primitive_Q_ascending": primitive_q,
        "cayley_P_ascending": transformed,
        "routh_first_column": first,
        "right_half_plane_roots": outside_count,
        "strict_conclusion": "Q has one nonreal conjugate pair with |y|>36; L has roots with |t+7|>6",
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=Path("certificates/routh_audit_input.json"),
    )
    args = parser.parse_args()
    try:
        result = verify(args.input)
    except (OSError, ValueError, TypeError, KeyError, OverflowError) as error:
        raise SystemExit(f"REJECT: {error}") from error
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
