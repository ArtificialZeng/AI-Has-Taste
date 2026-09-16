#!/usr/bin/env python3
"""Reproducible structured search for the d=4 hypercube inequality.

The search enumerates all two- and three-level colourings that are constant on
either Hamming-weight or fixed-facet-layer orbits.  The objective is evaluated
from exact integer coefficient tables; only the optimization is floating point.
It also optimizes unrestricted positive values on each of those orbit systems.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations, product
from math import exp, log

import numpy as np
from scipy.optimize import differential_evolution, minimize, minimize_scalar


VERTICES = list(product((0, 1), repeat=4))
FACETS = [[j for j, v in enumerate(VERTICES) if v[i] == b]
          for i in range(4) for b in (0, 1)]


def permutation_sign(p: tuple[int, ...]) -> int:
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions % 2 else 1


PERMS = [(p, permutation_sign(p)) for p in permutations(range(4))]


def simplex_volume(indices: tuple[int, ...]) -> int:
    base = VERTICES[indices[0]]
    matrix = [[VERTICES[indices[c + 1]][r] - base[r] for c in range(4)]
              for r in range(4)]
    return abs(sum(sign * np.prod([matrix[r][p[r]] for r in range(4)], dtype=int)
                   for p, sign in PERMS))


SIMPLEXES = [(s, simplex_volume(s)) for s in combinations(range(16), 5)]
SIMPLEXES = [(s, vol) for s, vol in SIMPLEXES if vol]


def restricted_growth_strings(n: int, k: int):
    """Canonical set partitions of range(n) into exactly k nonempty blocks."""
    a = [0] * n

    def visit(pos: int, maximum: int):
        if pos == n:
            if maximum == k - 1:
                yield tuple(a)
            return
        for value in range(min(maximum + 1, k - 1) + 1):
            a[pos] = value
            yield from visit(pos + 1, max(maximum, value))

    yield from visit(1, 0)


def coefficient_table(colors: tuple[int, ...], levels: int):
    counts = [colors.count(c) for c in range(levels)]
    facet_counts = [[sum(colors[j] == c for j in facet) for c in range(levels)]
                    for facet in FACETS]
    coeff = defaultdict(int)
    for simplex, vol in SIMPLEXES:
        exponent = tuple(sum(colors[j] == c for j in simplex) for c in range(levels - 1))
        coeff[exponent] += vol
    return counts, facet_counts, dict(coeff)


def log_ratio(log_values, counts, facet_counts, coeff):
    values = [exp(float(t)) for t in log_values] + [1.0]
    terms = []
    for exponent, c in coeff.items():
        terms.append(log(c) + sum(exponent[i] * log_values[i] for i in range(len(log_values))))
    peak = max(terms)
    log_a = peak + log(sum(exp(t - peak) for t in terms))
    total = sum(n * a for n, a in zip(counts, values))
    facet_sums = [sum(n * a for n, a in zip(row, values)) for row in facet_counts]
    if total <= 0 or min(facet_sums) <= 0:
        return -np.inf
    return log_a + 3.0 * log(total) - sum(log(s) for s in facet_sums)


def optimize_coloring(colors: tuple[int, ...], levels: int):
    counts, facet_counts, coeff = coefficient_table(colors, levels)
    if levels == 2:
        objective = lambda z: -log_ratio((float(z),), counts, facet_counts, coeff)
        result = minimize_scalar(objective, bounds=(-28.0, 28.0), method="bounded",
                                 options={"xatol": 1e-11, "maxiter": 250})
        candidates = [(result.x, -result.fun), (-28.0, -objective(-28.0)),
                      (0.0, -objective(0.0)), (28.0, -objective(28.0))]
        best = max(candidates, key=lambda q: q[1])
        return best[1], (best[0],)

    grid = (-24.0, -12.0, -6.0, 0.0, 6.0, 12.0, 24.0)
    seeds = sorted(((log_ratio((u, v), counts, facet_counts, coeff), (u, v))
                    for u in grid for v in grid), reverse=True)[:4]
    best = seeds[0]
    for _, seed in seeds:
        result = minimize(lambda z: -log_ratio(z, counts, facet_counts, coeff), seed,
                          method="Nelder-Mead",
                          options={"maxiter": 500, "xatol": 2e-9, "fatol": 2e-12})
        clipped = np.clip(result.x, -30.0, 30.0)
        value = log_ratio(clipped, counts, facet_counts, coeff)
        if value > best[0]:
            best = (value, tuple(float(z) for z in clipped))
    return best


def evaluate_vector(values: list[float]) -> float:
    a = sum(vol * np.prod([values[j] for j in simplex]) for simplex, vol in SIMPLEXES)
    total = sum(values)
    b = np.prod([sum(values[j] for j in facet) for facet in FACETS])
    return a * total**3 / b


def optimize_full_orbits(orbit_index: tuple[int, ...], orbit_count: int, seed: int):
    multiplicity = [orbit_index.count(i) for i in range(orbit_count)]

    def objective(logs):
        orbit_values = list(np.exp(np.r_[logs, 0.0]))
        values = [orbit_values[i] for i in orbit_index]
        return -log(evaluate_vector(values))

    result = differential_evolution(objective, [(-18.0, 18.0)] * (orbit_count - 1),
                                    seed=seed, popsize=12, maxiter=180,
                                    polish=True, updating="immediate", workers=1,
                                    tol=1e-10)
    logs = tuple(float(z) for z in result.x)
    return -result.fun, logs, multiplicity


def run_family(name: str, orbit_index: tuple[int, ...], orbit_count: int):
    print(f"FAMILY {name}: {orbit_count} orbits")
    for levels in (2, 3):
        best = (-np.inf, None, None)
        tested = 0
        for partition in restricted_growth_strings(orbit_count, levels):
            colors = tuple(partition[i] for i in orbit_index)
            value, logs = optimize_coloring(colors, levels)
            tested += 1
            if value > best[0]:
                best = (value, partition, logs)
        ratio = exp(best[0])
        print(f"  {levels}-level partitions tested={tested}; best ratio={ratio:.15g}; "
              f"orbit colors={best[1]}; log-values={best[2]}")
    value, logs, multiplicity = optimize_full_orbits(orbit_index, orbit_count,
                                                     seed=20260906 + orbit_count)
    print(f"  full-orbit optimization best ratio={exp(value):.15g}; "
          f"log-values={logs}; orbit multiplicities={multiplicity}")


def main():
    volume_distribution = defaultdict(int)
    for s in combinations(range(16), 5):
        volume_distribution[simplex_volume(s)] += 1
    print("volume distribution", dict(sorted(volume_distribution.items())))

    hamming = tuple(sum(v) for v in VERTICES)
    # Stabilizer of the first coordinate: layer b and Hamming weight among the
    # remaining three coordinates, encoded as 4*b+w in range(8).
    facet_layer = tuple(4 * v[0] + sum(v[1:]) for v in VERTICES)
    run_family("Hamming-weight", hamming, 5)
    run_family("fixed-facet-layer", facet_layer, 8)


if __name__ == "__main__":
    main()
