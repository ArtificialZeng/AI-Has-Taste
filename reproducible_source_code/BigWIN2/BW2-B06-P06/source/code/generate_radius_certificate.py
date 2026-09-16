#!/usr/bin/env python3
"""Generate pure-radius chamber certificates using exact scaled integers.

The output payload contains one unsigned byte per adjacent nonzero
positive/negative coefficient pair, in canonical chamber order.  This is a
discovery/generation implementation.  The independent verifier does not
import it and uses vertex measures rather than edge-difference rows.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import os
import platform
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linprog


def lcm_through(n: int) -> int:
    answer = 1
    for k in range(1, n + 1):
        answer = math.lcm(answer, k)
    return answer


def ball_bounds(n: int, vertex: int, radius: int) -> tuple[int, int]:
    return max(0, vertex - radius), min(n - 1, vertex + radius)


def scaled_edge_rows(n: int, scale: int) -> list[list[tuple[int, ...]]]:
    rows: list[list[tuple[int, ...]]] = []
    for vertex in range(n):
        vertex_rows = []
        for radius in range(max(vertex, n - 1 - vertex) + 1):
            left, right = ball_bounds(n, vertex, radius)
            size = right - left + 1
            multiplier = scale // size
            row = tuple(
                max(0, right - max(left, edge + 1) + 1) * multiplier
                for edge in range(n - 1)
            )
            if not vertex_rows or row != vertex_rows[-1]:
                vertex_rows.append(row)
        rows.append(vertex_rows)
    return rows


def coefficients(signs: tuple[int, ...]) -> tuple[int, ...]:
    return (
        (signs[0],)
        + tuple(signs[i] - signs[i - 1] for i in range(1, len(signs)))
        + (-signs[-1],)
    )


def max_abs(values: list[int]) -> int:
    return max((abs(value) for value in values), default=0)


def find_certificate(
    n: int,
    rows: list[list[tuple[int, ...]]],
    coeffs: tuple[int, ...],
    positive_radii: tuple[int, ...],
    target_scaled: int,
) -> list[int] | None:
    positive = [i for i, value in enumerate(coeffs) if value > 0]
    radius_at = dict(zip(positive, positive_radii))
    nonzero = [i for i, value in enumerate(coeffs) if value]

    positive_sum = [0] * (n - 1)
    for vertex in positive:
        row = rows[vertex][radius_at[vertex]]
        weight = coeffs[vertex]
        positive_sum = [x + weight * y for x, y in zip(positive_sum, row)]

    slot_metadata: list[tuple[int, int, int, int]] = []
    for left_vertex, right_vertex in zip(nonzero, nonzero[1:]):
        if coeffs[left_vertex] * coeffs[right_vertex] >= 0:
            raise AssertionError("nonzero coefficients must alternate")
        if coeffs[left_vertex] > 0:
            positive_vertex, negative_vertex = left_vertex, right_vertex
        else:
            positive_vertex, negative_vertex = right_vertex, left_vertex
        pradius = radius_at[positive_vertex]
        ball_left, ball_right = ball_bounds(n, positive_vertex, pradius)
        containing = max(
            abs(negative_vertex - ball_left),
            abs(negative_vertex - ball_right),
        )
        containing = min(containing, len(rows[negative_vertex]) - 1)
        external = min(
            pradius + abs(positive_vertex - negative_vertex),
            len(rows[negative_vertex]) - 1,
        )
        same = min(pradius, len(rows[negative_vertex]) - 1)
        slot_metadata.append((negative_vertex, containing, external, same))

    def descend(initial: list[int], reverse: bool) -> list[int] | None:
        slots = [
            [negative_vertex, min(radius, len(rows[negative_vertex]) - 1)]
            for (negative_vertex, _, _, _), radius in zip(slot_metadata, initial)
        ]
        h = positive_sum[:]
        for negative_vertex, radius in slots:
            h = [x - y for x, y in zip(h, rows[negative_vertex][radius])]
        if max_abs(h) <= target_scaled:
            return [radius for _, radius in slots]

        order = list(range(len(slots)))
        if reverse:
            order.reverse()
        for _ in range(8):
            changed = False
            for index in order:
                negative_vertex, old_radius = slots[index]
                base = [
                    x + y
                    for x, y in zip(h, rows[negative_vertex][old_radius])
                ]
                best_radius = min(
                    range(len(rows[negative_vertex])),
                    key=lambda radius: (
                        max_abs([
                            x - y
                            for x, y in zip(base, rows[negative_vertex][radius])
                        ]),
                        radius,
                    ),
                )
                if best_radius != old_radius:
                    h = [
                        x - y
                        for x, y in zip(base, rows[negative_vertex][best_radius])
                    ]
                    slots[index][1] = best_radius
                    changed = True
                if max_abs(h) <= target_scaled:
                    return [radius for _, radius in slots]
            if not changed:
                break
        if max_abs(h) <= target_scaled:
            return [radius for _, radius in slots]
        return None

    starts = [
        [metadata[1] for metadata in slot_metadata],
        [metadata[2] for metadata in slot_metadata],
        [metadata[3] for metadata in slot_metadata],
        [0] * len(slot_metadata),
        [n - 1] * len(slot_metadata),
    ]
    starts.extend([[radius] * len(slot_metadata) for radius in range(1, n - 1)])
    for initial in starts:
        answer = descend(initial, reverse=False)
        if answer is not None:
            return answer
        answer = descend(initial, reverse=True)
        if answer is not None:
            return answer
    return None


def find_fractional_certificate(
    n: int,
    rows: list[list[tuple[int, ...]]],
    coeffs: tuple[int, ...],
    positive_radii: tuple[int, ...],
    target_scaled: int,
) -> list[dict[str, object]]:
    """Locate rational negative-ball mixtures, then check them exactly.

    Floating point is used only to locate the support of a rational LP vertex.
    The returned weights are reconstructed as Fractions and accepted only if
    their masses and target edge bounds hold exactly.
    """
    positive = [i for i, value in enumerate(coeffs) if value > 0]
    negative = [i for i, value in enumerate(coeffs) if value < 0]
    positive_sum = [0] * (n - 1)
    for vertex, radius in zip(positive, positive_radii):
        positive_sum = [
            x + coeffs[vertex] * y
            for x, y in zip(positive_sum, rows[vertex][radius])
        ]

    offsets: dict[int, tuple[int, int]] = {}
    cursor = 0
    for vertex in negative:
        offsets[vertex] = (cursor, cursor + len(rows[vertex]))
        cursor += len(rows[vertex])
    t_index = cursor
    variable_count = cursor + 1
    a_eq = np.zeros((len(negative), variable_count))
    b_eq = np.zeros(len(negative))
    for equation, vertex in enumerate(negative):
        start, stop = offsets[vertex]
        a_eq[equation, start:stop] = 1.0
        b_eq[equation] = -coeffs[vertex]
    a_ub = np.zeros((2 * (n - 1), variable_count))
    b_ub = np.zeros(2 * (n - 1))
    for edge in range(n - 1):
        for vertex in negative:
            start, stop = offsets[vertex]
            column = np.array([row[edge] for row in rows[vertex]], dtype=float)
            a_ub[2 * edge, start:stop] = -column
            a_ub[2 * edge + 1, start:stop] = column
        a_ub[2 * edge, t_index] = -1.0
        a_ub[2 * edge + 1, t_index] = -1.0
        b_ub[2 * edge] = -positive_sum[edge]
        b_ub[2 * edge + 1] = positive_sum[edge]
    objective = np.zeros(variable_count)
    objective[t_index] = 1.0
    result = linprog(
        objective,
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, None)] * variable_count,
        method="highs",
    )
    if not result.success or result.fun > target_scaled + 1e-7:
        raise RuntimeError(
            json.dumps({
                "fractional_lp_failed": result.message,
                "objective": None if not result.success else result.fun,
                "target_scaled": target_scaled,
            })
        )

    for denominator_limit in (10_000, 1_000_000, 100_000_000, 10_000_000_000):
        reconstructed: dict[int, list[Fraction]] = {}
        reconstruction_ok = True
        for vertex in negative:
            start, stop = offsets[vertex]
            values = result.x[start:stop]
            support = [index for index, value in enumerate(values) if value > 1e-9]
            if not support:
                reconstruction_ok = False
                break
            pivot = max(support, key=lambda index: values[index])
            weights = [Fraction(0) for _ in values]
            for radius in support:
                if radius != pivot:
                    weights[radius] = Fraction(float(values[radius])).limit_denominator(
                        denominator_limit
                    )
            weights[pivot] = Fraction(-coeffs[vertex]) - sum(weights, Fraction(0))
            if any(weight < 0 for weight in weights):
                reconstruction_ok = False
                break
            reconstructed[vertex] = weights
        if not reconstruction_ok:
            continue

        h = [Fraction(value) for value in positive_sum]
        for vertex in negative:
            for radius, weight in enumerate(reconstructed[vertex]):
                if weight:
                    h = [
                        x - weight * y
                        for x, y in zip(h, rows[vertex][radius])
                    ]
        if max((abs(value) for value in h), default=Fraction(0)) > target_scaled:
            continue

        answer: list[dict[str, object]] = []
        for vertex in negative:
            entries = []
            for radius, weight in enumerate(reconstructed[vertex]):
                if weight:
                    entries.append([radius, weight.numerator, weight.denominator])
            answer.append({"vertex": vertex, "weights": entries})
        return answer
    raise RuntimeError("floating support could not be reconstructed exactly")


def generate(n: int, output_directory: Path) -> dict[str, object]:
    if not 2 <= n <= 255:
        raise ValueError("n must lie in [2,255]")
    output_directory.mkdir(parents=True, exist_ok=True)
    payload_path = output_directory / f"p{n}_radius_certificate.bin"
    header_path = output_directory / f"p{n}_radius_certificate.json"
    exceptions_path = output_directory / f"p{n}_fractional_exceptions.json"
    temporary_path = output_directory / f".p{n}_radius_certificate.tmp"

    scale = lcm_through(n)
    target_scaled = scale * (n - 1) // n
    rows = scaled_edge_rows(n, scale)
    chamber_count = 0
    slot_count = 0
    exceptions: list[dict[str, object]] = []
    digest = hashlib.sha256()
    started = time.monotonic()

    with temporary_path.open("wb") as stream:
        for signs in itertools.product((-1, 1), repeat=n - 1):
            coeffs = coefficients(signs)
            positive = [i for i, value in enumerate(coeffs) if value > 0]
            radius_ranges = [range(len(rows[i])) for i in positive]
            for positive_radii in itertools.product(*radius_ranges):
                slot_total = len([i for i, value in enumerate(coeffs) if value]) - 1
                answer = find_certificate(
                    n, rows, coeffs, positive_radii, target_scaled
                )
                chamber_count += 1
                if answer is None:
                    fractional = find_fractional_certificate(
                        n, rows, coeffs, positive_radii, target_scaled
                    )
                    exceptions.append({
                        "chamber_index": chamber_count - 1,
                        "negative_mixtures": fractional,
                    })
                    raw = bytes(slot_total)
                else:
                    raw = bytes(answer)
                stream.write(raw)
                digest.update(raw)
                slot_count += slot_total
        stream.flush()
        os.fsync(stream.fileno())

    elapsed = time.monotonic() - started
    temporary_path.replace(payload_path)

    exceptions_raw = (json.dumps({
        "schema": "path-hl-fractional-exceptions-v1",
        "n": n,
        "exceptions": exceptions,
    }, separators=(",", ":")) + "\n").encode("utf-8")
    exceptions_path.write_bytes(exceptions_raw)

    header: dict[str, object] = {
        "schema": "path-hl-radius-certificate-v2",
        "n": n,
        "target_numerator": n - 1,
        "target_denominator": n,
        "canonical_sign_order": "lexicographic with -1 before +1",
        "canonical_positive_radius_order": "lexicographic from radius 0",
        "payload_encoding": "one uint8 negative radius per consecutive nonzero coefficient pair",
        "chamber_count": chamber_count,
        "slot_count": slot_count,
        "payload_bytes": payload_path.stat().st_size,
        "payload_sha256": digest.hexdigest(),
        "fractional_exception_count": len(exceptions),
        "exceptions_file": exceptions_path.name,
        "exceptions_bytes": len(exceptions_raw),
        "exceptions_sha256": hashlib.sha256(exceptions_raw).hexdigest(),
        "generator": Path(__file__).name,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "elapsed_seconds_diagnostic": elapsed,
    }
    header_path.write_text(json.dumps(header, indent=2) + "\n", encoding="utf-8")
    return header


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--output-directory", type=Path, default=Path("certificates"))
    args = parser.parse_args()
    print(json.dumps(generate(args.n, args.output_directory), indent=2))


if __name__ == "__main__":
    main()
