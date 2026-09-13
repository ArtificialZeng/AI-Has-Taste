#!/usr/bin/env python3
"""Floating-point falsification search for the exact 3+1+1 reduction.

This tests the attained certificate (3) in three_direction_segments.md.
It is discovery evidence, not an exhaustive proof.
"""

import cmath
import math
import random


SEED = 696229843253
TRIALS = 300_000


def segment_distance_squared(target, a, b):
    direction = b - a
    denominator = abs(direction) ** 2
    if denominator == 0:
        return abs(a - target) ** 2
    theta = -((a - target).conjugate() * direction).real / denominator
    theta = max(0.0, min(1.0, theta))
    return abs(a + theta * direction - target) ** 2


def certificate_ratio(P, r, w, Em=1.0):
    P1, P2, P3 = P
    V = sum(ri * abs(wi) ** 2 for ri, wi in zip(r, w))
    E = Em + P1 * V
    m1 = math.sqrt((1.0 - 2.0 * P1) * Em / P1)
    values = [2.0 * P1 * P1 * min(abs(wi) ** 2 for wi in w)]
    for Pg, Ph in ((P2, P3), (P3, P2)):
        target = -m1 / (2.0 * Pg)
        delta2 = min(
            segment_distance_squared(target, w[i], w[j])
            for i, j in ((0, 1), (0, 2), (1, 2))
        )
        residual = (1.0 - 2.0 * Pg) * Em / (2.0 * Pg)
        scale = 2.0 * P1 * Pg / (1.0 - 2.0 * Ph)
        values.append(residual + scale * delta2)
    return min(values) / E, values, E, V


def random_case(rng):
    # x_k=1-2P_k ranges over the open simplex, exactly parametrizing
    # three positive direction weights P_k<1/2.
    x = [rng.expovariate(1.0) for _ in range(3)]
    total = sum(x)
    P = tuple((1.0 - value / total) / 2.0 for value in x)

    # Mix ordinary and near-degenerate conditional weights.
    alpha = 10.0 ** rng.uniform(-1.5, 1.0)
    raw_r = [rng.gammavariate(alpha, 1.0) for _ in range(3)]
    total_r = sum(raw_r)
    r = tuple(value / total_r for value in raw_r)
    if min(r) < 1e-10:
        return None

    a = complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0))
    b = complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0))
    w = [a, b, -(r[0] * a + r[1] * b) / r[2]]
    variance = sum(ri * abs(wi) ** 2 for ri, wi in zip(r, w))
    if variance < 1e-20:
        return None
    target_variance = 10.0 ** rng.uniform(-4.0, 6.0)
    phase = cmath.exp(2j * math.pi * rng.random())
    factor = phase * math.sqrt(target_variance / variance)
    return P, r, [factor * wi for wi in w]


def boundary_family():
    # The symmetric family approaches certificate ratio 4/7 as P1 -> 1/2.
    V = 8.0 / 3.0
    w = [math.sqrt(V) * cmath.exp(2j * math.pi * k / 3) for k in range(3)]
    r = (1.0 / 3.0,) * 3
    for exponent in (2, 4, 6, 8, 10):
        eps = 10.0 ** (-exponent)
        P1 = 0.5 - eps
        P = (P1, (1.0 - P1) / 2.0, (1.0 - P1) / 2.0)
        yield eps, certificate_ratio(P, r, w)[0]


def main():
    rng = random.Random(SEED)
    accepted = 0
    hard = 0
    record = (-1.0, None)
    hard_record = (-1.0, None)
    for _ in range(TRIALS):
        case = random_case(rng)
        if case is None:
            continue
        P, r, w = case
        ratio, values, E, V = certificate_ratio(P, r, w)
        accepted += 1
        if values[0] > 5.0 * E / 8.0:
            hard += 1
            if ratio > hard_record[0]:
                hard_record = (ratio, (P, r, w, values, E, V))
        if ratio > record[0]:
            record = (ratio, (P, r, w, values, E, V))

    print("seed", SEED)
    print("accepted", accepted, "hard-kernel", hard)
    print("largest random certificate ratio", format(record[0], ".17g"))
    print("record", record[1])
    print("largest hard-kernel ratio", format(hard_record[0], ".17g"))
    print("hard-kernel record", hard_record[1])
    print("symmetric boundary family", list(boundary_family()))
    print("violates 5/8", record[0] > 5.0 / 8.0)


if __name__ == "__main__":
    main()
