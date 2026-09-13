#!/usr/bin/env python3
"""Fail-closed, no-import verifier for the regular-snake counterexample.

This program does not import the discovery search.  It rebuilds h* by directly
enumerating linear extensions of the source-defined 24-element poset, rebuilds
24!L(t) in the binomial basis, checks the exact factorization, and verifies a
Rouche disk using rational arithmetic only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"REJECT: {message}")


def parse_fraction(value: object) -> Fraction:
    require(isinstance(value, list) and len(value) == 2, "fraction must be [numerator,denominator]")
    numerator, denominator = value
    require(type(numerator) is int and type(denominator) is int, "fraction entries must be integers")
    require(denominator > 0, "fraction denominator must be positive")
    return Fraction(numerator, denominator)


def poly_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return tuple(out)


def poly_shift(a: tuple[int, ...], shift: int) -> tuple[int, ...]:
    out = [0] * len(a)
    for i, coefficient in enumerate(a):
        for j in range(i + 1):
            out[j] += coefficient * comb(i, j) * shift ** (i - j)
    return tuple(out)


def source_poset(word: str) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Cover edges lower -> upper, literally following Definition 2.2."""
    edges = [(3, 1), (3, 2), (1, 0), (2, 0)]
    for n, letter in enumerate(word, start=1):
        edges.extend([(2 * n + 3, 2 * n + 1), (2 * n + 3, 2 * n + 2)])
        switch = n >= 2 and word[n - 2] != letter
        target = 2 * n - 1 if (n == 1 and letter == "L") or switch else 2 * n
        edges.append((2 * n + 2, target))
    return 2 * len(word) + 4, tuple(edges)


def natural_labels(vertex_count: int, edges: tuple[tuple[int, int], ...]) -> dict[int, int]:
    successors = [[] for _ in range(vertex_count)]
    indegree = [0] * vertex_count
    for lower, upper in edges:
        successors[lower].append(upper)
        indegree[upper] += 1
    ready = sorted(vertex for vertex in range(vertex_count) if indegree[vertex] == 0)
    order = []
    while ready:
        vertex = ready.pop(0)
        order.append(vertex)
        for upper in sorted(successors[vertex]):
            indegree[upper] -= 1
            if indegree[upper] == 0:
                ready.append(upper)
                ready.sort()
    require(len(order) == vertex_count, "source relation is not a poset")
    return {vertex: index + 1 for index, vertex in enumerate(order)}


def direct_hstar(word: str) -> tuple[int, ...]:
    """Descent enumerator of all linear extensions under a natural labeling."""
    vertex_count, edges = source_poset(word)
    labels = natural_labels(vertex_count, edges)
    predecessor_masks = [0] * vertex_count
    for lower, upper in edges:
        predecessor_masks[upper] |= 1 << lower
    full = (1 << vertex_count) - 1
    counts = [0] * vertex_count

    def visit(mask: int, last_label: int | None, descents: int) -> None:
        if mask == full:
            counts[descents] += 1
            return
        for vertex in range(vertex_count):
            if mask & (1 << vertex):
                continue
            if predecessor_masks[vertex] & ~mask:
                continue
            label = labels[vertex]
            visit(mask | (1 << vertex), label, descents + int(last_label is not None and last_label > label))

    visit(0, None, 0)
    while counts and counts[-1] == 0:
        counts.pop()
    return tuple(counts)


def ehrhart_numerator(hstar: tuple[int, ...], dimension: int) -> tuple[int, ...]:
    out = [0] * (dimension + 1)
    for i, h_i in enumerate(hstar):
        term = (1,)
        for q in range(1 - i, dimension - i + 1):
            term = poly_mul(term, (q, 1))
        for j, coefficient in enumerate(term):
            out[j] += h_i * coefficient
    return tuple(out)


def gaussian_mul(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_add(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def gaussian_scale(value: tuple[Fraction, Fraction], scalar: Fraction) -> tuple[Fraction, Fraction]:
    return value[0] * scalar, value[1] * scalar


def norm_squared(value: tuple[Fraction, Fraction]) -> Fraction:
    return value[0] ** 2 + value[1] ** 2


def taylor_coefficients(coefficients: tuple[int, ...], center: tuple[Fraction, Fraction]) -> tuple[tuple[Fraction, Fraction], ...]:
    powers = [(Fraction(1), Fraction(0))]
    for _ in range(1, len(coefficients)):
        powers.append(gaussian_mul(powers[-1], center))
    answer = []
    for k in range(len(coefficients)):
        total = (Fraction(0), Fraction(0))
        for j in range(k, len(coefficients)):
            total = gaussian_add(total, gaussian_scale(powers[j - k], Fraction(coefficients[j] * comb(j, k))))
        answer.append(total)
    return tuple(answer)


def verify(certificate_path: Path) -> dict[str, object]:
    raw = certificate_path.read_bytes()
    try:
        certificate = json.loads(raw)
    except Exception as exc:
        raise SystemExit(f"REJECT: invalid JSON: {exc}") from exc
    require(type(certificate) is dict, "top-level JSON must be an object")
    required_keys = {
        "schema",
        "word",
        "length",
        "dimension",
        "disk_center",
        "disk_radius",
        "hstar_coefficients_ascending",
        "primitive_y_quintic_coefficients_ascending",
        "rouche_center",
        "rouche_radius",
        "taylor_coefficients",
        "absolute_value_bounds",
    }
    require(set(certificate) == required_keys, "unexpected or missing top-level fields")
    require(certificate["schema"] == "snake-ehrhart-counterexample-v1", "unknown schema")
    require(certificate["word"] == "LRLRLRLRLR", "certificate is not pinned to the audited word")
    require(certificate["length"] == 10 and certificate["dimension"] == 24, "wrong length or dimension")
    require(certificate["disk_center"] == -7 and certificate["disk_radius"] == 6, "wrong corrected disk")

    expected_hstar = direct_hstar(certificate["word"])
    serialized_hstar = certificate["hstar_coefficients_ascending"]
    require(type(serialized_hstar) is list and all(type(x) is int for x in serialized_hstar), "invalid h* array")
    require(tuple(serialized_hstar) == expected_hstar, "serialized h* disagrees with direct linear-extension enumeration")
    require(sum(expected_hstar) == 13860, "unexpected linear-extension count")

    numerator = ehrhart_numerator(expected_hstar, 24)
    shifted = poly_shift(numerator, -7)  # t=x-7
    require(all(coefficient == 0 for coefficient in shifted[1::2]), "24!L(x-7) is not even")
    actual_g = shifted[::2]
    base = (1,)
    for k in range(7):
        base = poly_mul(base, (-k * k, 1))
    q_values = certificate["primitive_y_quintic_coefficients_ascending"]
    require(type(q_values) is list and all(type(x) is int for x in q_values), "invalid quintic array")
    q_poly = tuple(q_values)
    require(len(q_poly) == 6 and q_poly[-1] > 0, "quintic has wrong degree or sign")
    require(actual_g == tuple(36 * value for value in poly_mul(base, q_poly)), "exact Ehrhart factorization failed")

    center_data = certificate["rouche_center"]
    require(type(center_data) is dict and set(center_data) == {"real", "imag"}, "invalid Rouche center")
    center = parse_fraction(center_data["real"]), parse_fraction(center_data["imag"])
    radius = parse_fraction(certificate["rouche_radius"])
    require(center == (Fraction(-53, 2), Fraction(29)) and radius == Fraction(1, 6), "unexpected Rouche disk")
    actual_taylor = taylor_coefficients(q_poly, center)
    serialized_taylor = certificate["taylor_coefficients"]
    require(type(serialized_taylor) is list and len(serialized_taylor) == 6, "invalid Taylor data")
    parsed_taylor = []
    for entry in serialized_taylor:
        require(type(entry) is dict and set(entry) == {"real", "imag"}, "invalid Taylor coefficient")
        parsed_taylor.append((parse_fraction(entry["real"]), parse_fraction(entry["imag"])))
    require(tuple(parsed_taylor) == actual_taylor, "Taylor coefficients were not recomputed correctly")

    bounds = certificate["absolute_value_bounds"]
    require(type(bounds) is dict and set(bounds) == {"a0_upper", "a1_lower", "a2_upper", "a3_upper", "a4_upper", "a5_upper"}, "invalid bounds")
    require(all(type(value) is int and value > 0 for value in bounds.values()), "bounds must be positive integers")
    require(norm_squared(actual_taylor[0]) < bounds["a0_upper"] ** 2, "a0 upper bound failed")
    require(norm_squared(actual_taylor[1]) > bounds["a1_lower"] ** 2, "a1 lower bound failed")
    for index in range(2, 6):
        require(norm_squared(actual_taylor[index]) <= bounds[f"a{index}_upper"] ** 2, f"a{index} upper bound failed")
    lower_linear = Fraction(bounds["a1_lower"]) * radius
    upper_remainder = Fraction(bounds["a0_upper"])
    for index in range(2, 6):
        upper_remainder += Fraction(bounds[f"a{index}_upper"]) * radius ** index
    require(lower_linear > upper_remainder, "strict Rouche inequality failed")

    # Reverse triangle inequality: every y in D(c,r) has |y| > 36.
    require(norm_squared(center) > (Fraction(36) + radius) ** 2, "Rouche disk is not strictly outside |y|=36")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    return {
        "status": "CERTIFIED_COUNTEREXAMPLE",
        "word": certificate["word"],
        "linear_extensions": sum(expected_hstar),
        "hstar": expected_hstar,
        "factorization": "24!L(x-7)=36*prod_{k=0}^6(x^2-k^2)*Q(x^2)",
        "rouche_conclusion": "Q has exactly one root y0 in |y0-(-53/2+29i)|<1/6, and |y0|>36",
        "ehrhart_conclusion": "for either x0^2=y0, t0=x0-7 is a root and |t0+7|>6",
        "certificate_sha256": input_hash,
        "verifier_sha256": code_hash,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate",
        nargs="?",
        type=Path,
        default=Path("experiments/breaker_counterexample_certificate.json"),
    )
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (OSError, ValueError, TypeError, KeyError, OverflowError) as exc:
        raise SystemExit(f"REJECT: {exc}") from exc
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
