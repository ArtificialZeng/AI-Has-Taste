#!/usr/bin/env python3
"""Independent exact verifier for the length-9 regular-snake counterexample.

No length-10 discovery module and no main-thread artifact is imported.  The
program reconstructs the source poset, enumerates all linear extensions,
builds 22!L(t), checks an integer factorization after u=2t+13, and verifies a
rational Rouche isolating disk outside |s|=121.
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
    answer = [0] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            answer[i + j] += left * right
    return tuple(answer)


def source_poset(word: str) -> tuple[int, tuple[tuple[int, int], ...]]:
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
    require(len(order) == vertex_count, "source relation is not acyclic")
    return {vertex: index + 1 for index, vertex in enumerate(order)}


def direct_hstar(word: str) -> tuple[int, ...]:
    vertex_count, edges = source_poset(word)
    labels = natural_labels(vertex_count, edges)
    predecessors = [0] * vertex_count
    for lower, upper in edges:
        predecessors[upper] |= 1 << lower
    full = (1 << vertex_count) - 1
    counts = [0] * vertex_count

    def visit(mask: int, last_label: int | None, descents: int) -> None:
        if mask == full:
            counts[descents] += 1
            return
        for vertex in range(vertex_count):
            if mask & (1 << vertex) or predecessors[vertex] & ~mask:
                continue
            label = labels[vertex]
            visit(mask | (1 << vertex), label, descents + int(last_label is not None and last_label > label))

    visit(0, None, 0)
    while counts and counts[-1] == 0:
        counts.pop()
    return tuple(counts)


def ehrhart_numerator(hstar: tuple[int, ...], dimension: int) -> tuple[int, ...]:
    answer = [0] * (dimension + 1)
    for i, h_i in enumerate(hstar):
        term = (1,)
        for q in range(1 - i, dimension - i + 1):
            term = poly_mul(term, (q, 1))
        for j, coefficient in enumerate(term):
            answer[j] += h_i * coefficient
    return tuple(answer)


def scaled_affine_substitution(coefficients: tuple[int, ...], dimension: int) -> tuple[int, ...]:
    """Ascending coefficients of 2^d F((u-13)/2), for F=22!L."""
    answer = [0] * (dimension + 1)
    for i, coefficient in enumerate(coefficients):
        for j in range(i + 1):
            answer[j] += coefficient * comb(i, j) * (-13) ** (i - j) * 2 ** (dimension - i)
    return tuple(answer)


def gaussian_add(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return left[0] + right[0], left[1] + right[1]


def gaussian_mul(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


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


def verify(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    try:
        certificate = json.loads(raw)
    except Exception as exc:
        raise SystemExit(f"REJECT: invalid JSON: {exc}") from exc
    require(type(certificate) is dict, "top level must be an object")
    expected_keys = {
        "schema", "word", "length", "dimension", "disk_center", "disk_radius",
        "hstar_coefficients_ascending", "primitive_s_quartic_coefficients_ascending",
        "rouche_center", "rouche_radius", "taylor_coefficients", "absolute_value_bounds",
    }
    require(set(certificate) == expected_keys, "unexpected or missing top-level fields")
    require(certificate["schema"] == "snake-ehrhart-length9-counterexample-v1", "wrong schema")
    require(certificate["word"] == "LRLRLRLRL", "not the pinned length-9 regular word")
    require(certificate["length"] == 9 and certificate["dimension"] == 22, "wrong endpoint")
    require(parse_fraction(certificate["disk_center"]) == Fraction(-13, 2), "wrong disk center")
    require(parse_fraction(certificate["disk_radius"]) == Fraction(11, 2), "wrong disk radius")

    actual_hstar = direct_hstar(certificate["word"])
    serialized_hstar = certificate["hstar_coefficients_ascending"]
    require(type(serialized_hstar) is list and all(type(x) is int for x in serialized_hstar), "invalid h* data")
    require(tuple(serialized_hstar) == actual_hstar, "h* disagrees with direct linear-extension enumeration")
    require(sum(actual_hstar) == 5741, "unexpected number of linear extensions")

    f_poly = ehrhart_numerator(actual_hstar, 22)
    u_poly = scaled_affine_substitution(f_poly, 22)
    require(all(coefficient == 0 for coefficient in u_poly[1::2]), "scaled polynomial is not even in u")
    s_poly = u_poly[::2]
    fixed = (1,)
    for k in (1, 3, 5, 7, 9, 11):
        fixed = poly_mul(fixed, (-k * k, 1))
    quartic_values = certificate["primitive_s_quartic_coefficients_ascending"]
    require(type(quartic_values) is list and all(type(x) is int for x in quartic_values), "invalid quartic data")
    quartic = tuple(quartic_values)
    require(len(quartic) == 5 and quartic[-1] == 5741, "wrong quartic degree or leading coefficient")
    require(s_poly == poly_mul(poly_mul(fixed, (-1, 1)), quartic), "exact Ehrhart factorization failed")

    center_data = certificate["rouche_center"]
    require(type(center_data) is dict and set(center_data) == {"real", "imag"}, "invalid Rouche center")
    center = parse_fraction(center_data["real"]), parse_fraction(center_data["imag"])
    radius = parse_fraction(certificate["rouche_radius"])
    require(center == (Fraction(-82), Fraction(91)) and radius == Fraction(1, 2), "unexpected Rouche disk")
    actual_taylor = taylor_coefficients(quartic, center)
    serialized_taylor = certificate["taylor_coefficients"]
    require(type(serialized_taylor) is list and len(serialized_taylor) == 5, "invalid Taylor data")
    parsed_taylor = []
    for entry in serialized_taylor:
        require(type(entry) is dict and set(entry) == {"real", "imag"}, "invalid Taylor entry")
        parsed_taylor.append((parse_fraction(entry["real"]), parse_fraction(entry["imag"])))
    require(tuple(parsed_taylor) == actual_taylor, "Taylor coefficients failed reconstruction")

    bounds = certificate["absolute_value_bounds"]
    require(type(bounds) is dict and set(bounds) == {"a0_upper", "a1_lower", "a2_upper", "a3_upper", "a4_upper"}, "invalid bounds")
    require(all(type(value) is int and value > 0 for value in bounds.values()), "bounds must be positive integers")
    require(norm_squared(actual_taylor[0]) < bounds["a0_upper"] ** 2, "a0 bound failed")
    require(norm_squared(actual_taylor[1]) > bounds["a1_lower"] ** 2, "a1 bound failed")
    for index in range(2, 5):
        require(norm_squared(actual_taylor[index]) <= bounds[f"a{index}_upper"] ** 2, f"a{index} bound failed")
    linear_lower = Fraction(bounds["a1_lower"]) * radius
    remainder_upper = Fraction(bounds["a0_upper"])
    for index in range(2, 5):
        remainder_upper += Fraction(bounds[f"a{index}_upper"]) * radius ** index
    require(linear_lower > remainder_upper, "strict Rouche inequality failed")

    # The full Rouche disk is outside |s|=121 by reverse triangle inequality.
    require(norm_squared(center) > (Fraction(121) + radius) ** 2, "isolating disk is not outside |s|=121")

    return {
        "status": "CERTIFIED_LENGTH9_COUNTEREXAMPLE",
        "word": certificate["word"],
        "linear_extensions": sum(actual_hstar),
        "hstar": actual_hstar,
        "factorization": "2^22*22!*L((u-13)/2)=prod_{k=1,3,5,7,9,11}(u^2-k^2)*(u^2-1)*R(u^2)",
        "rouche_conclusion": "R has exactly one root s0 in |s0-(-82+91i)|<1/2, and |s0|>121",
        "ehrhart_conclusion": "for u0^2=s0 and t0=(u0-13)/2, L(t0)=0 and |t0+13/2|>11/2",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "certificate", nargs="?", type=Path,
        default=Path("experiments/breaker_length9_counterexample_certificate.json"),
    )
    args = parser.parse_args()
    try:
        result = verify(args.certificate)
    except (OSError, ValueError, TypeError, KeyError, OverflowError) as exc:
        raise SystemExit(f"REJECT: {exc}") from exc
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
