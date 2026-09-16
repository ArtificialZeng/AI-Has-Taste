#!/usr/bin/env python3
"""Independent exact verifier for path-HL pure-radius certificates.

This file deliberately imports no project module.  It enumerates sign and
active-radius chambers with integer odometers, reconstructs signed uniform
measures on vertices, and checks their cumulative masses using Fraction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def radii_count(n: int, vertex: int) -> int:
    return max(vertex, n - 1 - vertex) + 1


def bounds(n: int, vertex: int, radius: int) -> tuple[int, int]:
    if radius < 0 or radius >= radii_count(n, vertex):
        raise ValueError("radius outside canonical distinct-ball range")
    return max(0, vertex - radius), min(n - 1, vertex + radius)


def add_ball_mass(
    mass: list[Fraction],
    n: int,
    vertex: int,
    radius: int,
    weight: int,
) -> None:
    left, right = bounds(n, vertex, radius)
    increment = Fraction(weight, right - left + 1)
    for point in range(left, right + 1):
        mass[point] += increment


def sign_tuple(mask: int, length: int) -> tuple[int, ...]:
    return tuple(
        1 if mask & (1 << (length - 1 - position)) else -1
        for position in range(length)
    )


def coefficient_tuple(signs: tuple[int, ...]) -> tuple[int, ...]:
    result = [signs[0]]
    for position in range(1, len(signs)):
        result.append(signs[position] - signs[position - 1])
    result.append(-signs[-1])
    return tuple(result)


def radius_tuples(limits: list[int]):
    if not limits:
        yield ()
        return
    digits = [0] * len(limits)
    while True:
        yield tuple(digits)
        position = len(digits) - 1
        while position >= 0:
            digits[position] += 1
            if digits[position] < limits[position]:
                break
            digits[position] = 0
            position -= 1
        if position < 0:
            return


def verify(header_path: Path, payload_path: Path) -> dict[str, object]:
    header = json.loads(header_path.read_text(encoding="utf-8"))
    if header.get("schema") != "path-hl-radius-certificate-v2":
        raise ValueError("unsupported certificate schema")
    n = header.get("n")
    if not isinstance(n, int) or not 2 <= n <= 255:
        raise ValueError("invalid n")
    if header.get("target_numerator") != n - 1:
        raise ValueError("wrong target numerator")
    if header.get("target_denominator") != n:
        raise ValueError("wrong target denominator")
    target = Fraction(n - 1, n)

    raw = payload_path.read_bytes()
    if len(raw) != header.get("payload_bytes"):
        raise ValueError("payload length differs from header")
    digest = hashlib.sha256(raw).hexdigest()
    if digest != header.get("payload_sha256"):
        raise ValueError("payload digest differs from header")

    exceptions_name = header.get("exceptions_file")
    if not isinstance(exceptions_name, str) or Path(exceptions_name).name != exceptions_name:
        raise ValueError("invalid exceptions filename")
    exceptions_path = header_path.parent / exceptions_name
    exceptions_raw = exceptions_path.read_bytes()
    if len(exceptions_raw) != header.get("exceptions_bytes"):
        raise ValueError("exceptions length differs from header")
    if hashlib.sha256(exceptions_raw).hexdigest() != header.get("exceptions_sha256"):
        raise ValueError("exceptions digest differs from header")
    exception_document = json.loads(exceptions_raw)
    if exception_document.get("schema") != "path-hl-fractional-exceptions-v1":
        raise ValueError("unsupported exceptions schema")
    if exception_document.get("n") != n:
        raise ValueError("exceptions n differs from header")
    exception_records = exception_document.get("exceptions")
    if not isinstance(exception_records, list):
        raise ValueError("exceptions must be a list")
    exceptions: dict[int, object] = {}
    previous_index = -1
    for record in exception_records:
        if not isinstance(record, dict):
            raise ValueError("malformed exception record")
        index = record.get("chamber_index")
        if not isinstance(index, int) or index <= previous_index:
            raise ValueError("exception indices must be strictly increasing")
        previous_index = index
        exceptions[index] = record.get("negative_mixtures")
    if len(exceptions) != header.get("fractional_exception_count"):
        raise ValueError("exception count differs from header")

    cursor = 0
    chambers = 0
    slots_seen = 0
    for mask in range(1 << (n - 1)):
        signs = sign_tuple(mask, n - 1)
        coeffs = coefficient_tuple(signs)
        if sum(coeffs) != 0:
            raise AssertionError("telescoping coefficients do not sum to zero")
        nonzero = [i for i, value in enumerate(coeffs) if value]
        for left, right in zip(nonzero, nonzero[1:]):
            if coeffs[left] * coeffs[right] >= 0:
                raise AssertionError("nonzero coefficients fail to alternate")
        positive = [i for i, value in enumerate(coeffs) if value > 0]
        limits = [radii_count(n, vertex) for vertex in positive]
        for positive_radii in radius_tuples(limits):
            slot_total = len(nonzero) - 1
            stop = cursor + slot_total
            if stop > len(raw):
                raise ValueError("truncated payload")
            negative_radii = raw[cursor:stop]
            cursor = stop

            mass = [Fraction(0) for _ in range(n)]
            for vertex, radius in zip(positive, positive_radii):
                add_ball_mass(mass, n, vertex, radius, coeffs[vertex])
            if chambers in exceptions:
                mixtures = exceptions[chambers]
                if not isinstance(mixtures, list):
                    raise ValueError("malformed negative mixtures")
                expected_negative = [i for i, value in enumerate(coeffs) if value < 0]
                seen_negative = []
                for mixture in mixtures:
                    if not isinstance(mixture, dict):
                        raise ValueError("malformed mixture")
                    vertex = mixture.get("vertex")
                    weights = mixture.get("weights")
                    if not isinstance(vertex, int) or not isinstance(weights, list):
                        raise ValueError("malformed mixture fields")
                    seen_negative.append(vertex)
                    total_weight = Fraction(0)
                    previous_radius = -1
                    for entry in weights:
                        if not isinstance(entry, list) or len(entry) != 3:
                            raise ValueError("malformed rational weight")
                        radius, numerator, denominator = entry
                        if not all(isinstance(value, int) for value in entry):
                            raise ValueError("noninteger rational encoding")
                        if radius <= previous_radius or denominator <= 0 or numerator <= 0:
                            raise ValueError("invalid or unordered rational weight")
                        previous_radius = radius
                        if radius >= radii_count(n, vertex):
                            raise ValueError("fractional certificate radius is invalid")
                        weight = Fraction(numerator, denominator)
                        total_weight += weight
                        left_bound, right_bound = bounds(n, vertex, radius)
                        increment = -weight / (right_bound - left_bound + 1)
                        for point in range(left_bound, right_bound + 1):
                            mass[point] += increment
                    if total_weight != -coeffs[vertex]:
                        raise ValueError("fractional mixture has wrong total weight")
                if seen_negative != expected_negative:
                    raise ValueError("fractional mixtures do not match negative vertices")
            else:
                for index, (left, right) in enumerate(zip(nonzero, nonzero[1:])):
                    negative_vertex = left if coeffs[left] < 0 else right
                    radius = negative_radii[index]
                    if radius >= radii_count(n, negative_vertex):
                        raise ValueError("certificate radius is invalid")
                    add_ball_mass(mass, n, negative_vertex, radius, -1)

            if sum(mass, Fraction(0)) != 0:
                raise ValueError("signed certificate mass is not zero")
            prefix = Fraction(0)
            for edge in range(n - 1):
                prefix += mass[edge]
                if abs(prefix) > target:
                    raise ValueError(
                        f"edge-flux bound failed at chamber {chambers}, edge {edge}"
                    )
            chambers += 1
            slots_seen += slot_total

    if cursor != len(raw):
        raise ValueError("trailing payload bytes")
    if exceptions and max(exceptions) >= chambers:
        raise ValueError("exception index outside chamber range")
    if chambers != header.get("chamber_count"):
        raise ValueError("chamber count differs from header")
    if slots_seen != header.get("slot_count"):
        raise ValueError("slot count differs from header")
    return {
        "status": "VERIFIED",
        "n": n,
        "target": f"{n - 1}/{n}",
        "chambers": chambers,
        "slots": slots_seen,
        "payload_bytes": len(raw),
        "payload_sha256": digest,
        "fractional_exceptions": len(exceptions),
        "method": "exact Fraction vertex masses and cumulative edge flux",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("header", type=Path)
    parser.add_argument("payload", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(verify(args.header, args.payload), indent=2) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
