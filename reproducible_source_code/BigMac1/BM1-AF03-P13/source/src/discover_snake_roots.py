#!/usr/bin/env python3
"""Exact discovery scan for generalized-snake Ehrhart root disks.

This is discovery code, not the release verifier.  It reconstructs h* from
the recursively defined poset by enumerating every order ideal and counting
multichains.  It then applies an exact Cayley/Routh reduction to the nonfixed
Ehrhart factor.  Only Python's standard library is used.

Coefficient lists are always in ascending order unless a variable says
``descending`` explicitly.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_add(a: list[int], b: list[int]) -> list[int]:
    out = [0] * max(len(a), len(b))
    for index, value in enumerate(a):
        out[index] += value
    for index, value in enumerate(b):
        out[index] += value
    return trim(out)


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def poly_pow(base: list[int], exponent: int) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent //= 2
    return out


def poly_div_monic(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    if not divisor or divisor[-1] != 1:
        raise ValueError("the divisor must be nonzero and monic")
    remainder = dividend[:]
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            remainder[shift + index] -= coefficient * value
        trim(remainder)
    return trim(quotient), trim(remainder)


def determinant_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant with row pivoting."""
    size = len(matrix)
    if size == 0:
        return 1
    work = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            swap = next(
                (row for row in range(pivot_index + 1, size) if work[row][pivot_index]),
                None,
            )
            if swap is None:
                return 0
            work[pivot_index], work[swap] = work[swap], work[pivot_index]
            sign = -sign
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                if numerator % previous:
                    raise ArithmeticError("Bareiss exact division failed")
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def poset_covers(word: str) -> list[tuple[int, int]]:
    """Return covers (lower, upper) from Definition 2.2."""
    covers = [(1, 0), (2, 0), (3, 1), (3, 2)]
    for length, letter in enumerate(word, 1):
        covers.extend(
            [(2 * length + 3, 2 * length + 1), (2 * length + 3, 2 * length + 2)]
        )
        turns = (length == 1 and letter == "L") or (
            length >= 2 and word[length - 2] != letter
        )
        covers.append((2 * length + 2, 2 * length - 1 if turns else 2 * length))
    return covers


def all_order_ideals(word: str) -> list[int]:
    """Enumerate all ideals as bit masks, without a 2^d ambient scan."""
    element_count = 2 * len(word) + 4
    successors = [[] for _ in range(element_count)]
    indegree = [0] * element_count
    predecessor_masks = [0] * element_count
    for lower, upper in poset_covers(word):
        successors[lower].append(upper)
        indegree[upper] += 1

    queue = [vertex for vertex in range(element_count) if indegree[vertex] == 0]
    topological_order: list[int] = []
    while queue:
        vertex = queue.pop()
        topological_order.append(vertex)
        for upper in successors[vertex]:
            indegree[upper] -= 1
            if indegree[upper] == 0:
                queue.append(upper)
    if len(topological_order) != element_count:
        raise ValueError("the reconstructed cover graph is not acyclic")

    for lower in topological_order:
        for upper in successors[lower]:
            predecessor_masks[upper] |= predecessor_masks[lower] | (1 << lower)

    ideals = [0]
    for vertex in topological_order:
        old = ideals[:]
        ideals.extend(
            ideal | (1 << vertex)
            for ideal in old
            if predecessor_masks[vertex] & ~ideal == 0
        )
    ideals = sorted(set(ideals), key=lambda value: (value.bit_count(), value))
    return ideals


def hstar_from_poset(word: str) -> tuple[list[int], list[int], int]:
    """Return h*, L(0..d), and the number of order ideals.

    L(t) is the number of length-(t+1) multichains from the empty to the full
    ideal.  The numerator identity h*(z)=(1-z)^(d+1) sum L(t)z^t then gives
    every h* coefficient by an integer binomial transform.
    """
    dimension = 2 * len(word) + 4
    ideals = all_order_ideals(word)
    index = {ideal: position for position, ideal in enumerate(ideals)}
    subideals = [
        [position for position, left in enumerate(ideals) if left & ~right == 0]
        for right in ideals
    ]
    counts = [0] * len(ideals)
    counts[index[0]] = 1
    full = (1 << dimension) - 1
    values: list[int] = []
    for _ in range(dimension + 1):
        counts = [sum(counts[position] for position in lower) for lower in subideals]
        values.append(counts[index[full]])
    hstar = [
        sum(
            (-1) ** shift
            * math.comb(dimension + 1, shift)
            * values[degree - shift]
            for shift in range(degree + 1)
        )
        for degree in range(dimension + 1)
    ]
    expected_degree = len(word) + 1
    if any(hstar[expected_degree + 1 :]):
        raise ArithmeticError("unexpected nonzero h* tail")
    return hstar[: expected_degree + 1], values, len(ideals)


def scaled_ehrhart_numerator(hstar: list[int], dimension: int) -> list[int]:
    """Return coefficients of dimension! times L(t)."""
    answer = [0]
    for index, h_coefficient in enumerate(hstar):
        basis = [1]
        for offset in range(dimension):
            basis = poly_mul(basis, [dimension - index - offset, 1])
        answer = poly_add(answer, [h_coefficient * value for value in basis])
    return answer


def centered_radial_factor(word: str, hstar: list[int]) -> dict[str, object]:
    """Reduce the residual disk test to a real polynomial R(y).

    The centered coordinate is x=2t+m+4.  After removing the fixed roots,
    2^(m+1)Q((x-m-4)/2) is even or odd.  Removing its possible x factor and
    writing y=x^2 gives R(y); the target is |y| <= (m+2)^2.
    """
    length = len(word)
    dimension = 2 * length + 4
    numerator = scaled_ehrhart_numerator(hstar, dimension)
    fixed = [1]
    for root in range(1, length + 4):
        fixed = poly_mul(fixed, [root, 1])
    quotient, remainder = poly_div_monic(numerator, fixed)
    if remainder != [0] or len(quotient) - 1 != length + 1:
        raise ArithmeticError("known fixed Ehrhart factor did not divide exactly")

    residual_degree = length + 1
    center_twice = length + 4
    centered = [0]
    # 2^n Q((x-center_twice)/2)
    for degree, coefficient in enumerate(quotient):
        term = poly_pow([-center_twice, 1], degree)
        multiplier = coefficient * 2 ** (residual_degree - degree)
        centered = poly_add(centered, [multiplier * value for value in term])
    required_parity = residual_degree & 1
    for degree, coefficient in enumerate(centered):
        if degree % 2 != required_parity and coefficient:
            raise ArithmeticError("centered quotient has the wrong parity")
    radial = [centered[2 * k + required_parity] for k in range(residual_degree // 2 + 1)]
    common = 0
    for coefficient in radial:
        common = math.gcd(common, abs(coefficient))
    if common == 0:
        raise ArithmeticError("zero residual polynomial")
    radial = [coefficient // common for coefficient in radial]
    if radial[-1] < 0:
        radial = [-coefficient for coefficient in radial]
    return {
        "radial_coefficients_ascending": radial,
        "radial_content_removed": common,
        "target_y_radius": (length + 2) ** 2,
        "order_ideal_count": None,
    }


def cayley_polynomial(radial: list[int], boundary: int) -> list[int]:
    """Return P(s)=(s-1)^q R(boundary*(s+1)/(s-1))."""
    degree = len(radial) - 1
    answer = [0]
    for index, coefficient in enumerate(radial):
        term = poly_mul(poly_pow([1, 1], index), poly_pow([-1, 1], degree - index))
        answer = poly_add(
            answer,
            [coefficient * boundary**index * value for value in term],
        )
    common = 0
    for coefficient in answer:
        common = math.gcd(common, abs(coefficient))
    answer = [coefficient // common for coefficient in answer]
    if answer[-1] < 0:
        answer = [-coefficient for coefficient in answer]
    return answer


def routh_table(poly_ascending: list[int]) -> tuple[list[list[Fraction]], int]:
    """Build a nonsingular Routh table and count RHP roots exactly."""
    degree = len(poly_ascending) - 1
    if degree == 0:
        return [[Fraction(poly_ascending[0])]], 0
    descending = list(reversed(poly_ascending))
    columns = (degree + 2) // 2
    table = [[Fraction(0) for _ in range(columns)] for _ in range(degree + 1)]
    even_row = [Fraction(descending[index]) for index in range(0, degree + 1, 2)]
    odd_row = [Fraction(descending[index]) for index in range(1, degree + 1, 2)]
    table[0][: len(even_row)] = even_row
    table[1][: len(odd_row)] = odd_row
    for row in range(2, degree + 1):
        if table[row - 1][0] == 0:
            raise ArithmeticError("Routh first-column zero: boundary case unresolved")
        for column in range(columns - 1):
            table[row][column] = (
                table[row - 1][0] * table[row - 2][column + 1]
                - table[row - 2][0] * table[row - 1][column + 1]
            ) / table[row - 1][0]
        if all(value == 0 for value in table[row]):
            raise ArithmeticError("Routh zero row: imaginary-axis roots unresolved")
    first_column = [row[0] for row in table]
    if any(value == 0 for value in first_column):
        raise ArithmeticError("Routh first-column zero: boundary case unresolved")
    signs = [1 if value > 0 else -1 for value in first_column]
    variations = sum(left != right for left, right in zip(signs, signs[1:]))
    return table, variations


def fraction_json(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def scan(max_length: int) -> dict[str, object]:
    lengths: list[dict[str, object]] = []
    all_length10_records: dict[str, dict[str, object]] = {}
    for length in range(max_length + 1):
        words = ["".join(letters) for letters in itertools.product("LR", repeat=length)]
        hstars: dict[str, list[int]] = {}
        failures: list[dict[str, object]] = []
        maximum_ideals = 0
        for word in words:
            hstar, values, ideal_count = hstar_from_poset(word)
            maximum_ideals = max(maximum_ideals, ideal_count)
            reduction = centered_radial_factor(word, hstar)
            radial = reduction["radial_coefficients_ascending"]
            boundary = reduction["target_y_radius"]
            cayley = cayley_polynomial(radial, boundary)
            table, outside_count = routh_table(cayley)
            key = ",".join(map(str, hstar))
            hstars.setdefault(key, []).append(word)
            record = {
                "word": word,
                "hstar_coefficients_ascending": hstar,
                "ehrhart_values_0_through_dimension": values,
                "order_ideal_count": ideal_count,
                "radial_coefficients_ascending": radial,
                "target_y_radius": boundary,
                "cayley_coefficients_ascending": cayley,
                "routh_first_column": [fraction_json(row[0]) for row in table],
                "outside_root_count": outside_count,
            }
            if outside_count:
                failures.append(record)
            if length == 10:
                all_length10_records[word] = record
        complement_mismatches = [
            word
            for word in words
            if all_length10_records.get(word, {}).get("hstar_coefficients_ascending")
            != all_length10_records.get(word.translate(str.maketrans("LR", "RL")), {}).get(
                "hstar_coefficients_ascending"
            )
        ] if length == 10 else []
        reversal_mismatches = [
            word
            for word in words
            if all_length10_records.get(word, {}).get("hstar_coefficients_ascending")
            != all_length10_records.get(word[::-1], {}).get("hstar_coefficients_ascending")
        ] if length == 10 else []
        lengths.append(
            {
                "length": length,
                "literal_word_count": len(words),
                "distinct_hstar_count": len(hstars),
                "maximum_order_ideal_count": maximum_ideals,
                "outside_words": [entry["word"] for entry in failures],
                "outside_count": len(failures),
                "complement_mismatches": complement_mismatches,
                "reversal_mismatches": reversal_mismatches,
            }
        )
    witness = all_length10_records.get("LRLRLRLRLR")
    return {
        "schema_version": 1,
        "method": "poset-order-ideal multichains + integer Ehrhart transform + exact Routh count",
        "python": sys.version,
        "platform": platform.platform(),
        "max_length": max_length,
        "length_summaries": lengths,
        "preferred_witness": witness,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if not 0 <= args.max_length <= 10:
        parser.error("this bounded discovery implementation supports 0 <= max-length <= 10")
    result = scan(args.max_length)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    args.output.write_bytes(encoded)
    print(
        json.dumps(
            {
                "status": "OK",
                "output": str(args.output),
                "sha256": hashlib.sha256(encoded).hexdigest(),
                "length_summaries": result["length_summaries"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
