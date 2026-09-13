#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent exact certificate that the 11 representatives cover all cases.

For every displayed graph we enumerate all 8! vertex permutations to compute
its automorphism order and canonical adjacency code.  Separately, a degree-
sequence recursion counts *all labeled* simple k-regular graphs.  Distinct
canonical codes plus equality

    sum(8! / |Aut(G_i)|) = number of labeled k-regular graphs

certifies pairwise nonisomorphism and exhaustive isomorphism coverage, without
using ``geng`` for the second count.
"""

from __future__ import annotations

from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "evidence" / "order8_classification.json"
OUTPUT = ROOT / "evidence" / "coverage_report.json"
REQUIRED_PYTHON = Path(
    "/Users/mac/4prove-or-disprove-math/.research-venv/bin/python"
).resolve()
N = 8
PAIRS = tuple((i, j) for i in range(N) for j in range(i + 1, N))


def adjacency_code(adj: list[list[int]], permutation: tuple[int, ...]) -> int:
    code = 0
    for bit, (i, j) in enumerate(PAIRS):
        if adj[permutation[i]][permutation[j]]:
            code |= 1 << bit
    return code


def canonical_and_automorphisms(adj: list[list[int]]) -> tuple[int, int]:
    identity = tuple(range(N))
    original = adjacency_code(adj, identity)
    canonical = original
    automorphisms = 0
    for permutation in itertools.permutations(range(N)):
        code = adjacency_code(adj, permutation)
        canonical = min(canonical, code)
        if code == original:
            automorphisms += 1
    return canonical, automorphisms


def count_labeled_regular_graphs(degree: int) -> int:
    """Count labeled simple graphs with degree sequence (degree,)*8 exactly."""

    @lru_cache(maxsize=None)
    def recurse(vertex: int, remaining: tuple[int, ...]) -> int:
        while vertex < N and remaining[vertex] == 0:
            vertex += 1
        if vertex == N:
            return int(all(value == 0 for value in remaining))
        need = remaining[vertex]
        available = tuple(j for j in range(vertex + 1, N) if remaining[j] > 0)
        if need < 0 or need > len(available):
            return 0
        total = 0
        for chosen in itertools.combinations(available, need):
            new = list(remaining)
            new[vertex] = 0
            for j in chosen:
                new[j] -= 1
            # All future vertices remain mutually available.  A future vertex
            # can still meet at most every other vertex in that unprocessed
            # suffix; the tighter index-dependent bound would be invalid
            # because vertices between ``vertex`` and j have not been handled.
            suffix_max_degree = N - vertex - 2
            if any(
                new[j] < 0 or new[j] > suffix_max_degree
                for j in range(vertex + 1, N)
            ):
                continue
            if sum(new[vertex + 1 :]) % 2:
                continue
            total += recurse(vertex + 1, tuple(new))
        return total

    return recurse(0, (degree,) * N)


def main() -> None:
    if Path(sys.executable).resolve() != REQUIRED_PYTHON:
        raise RuntimeError(f"wrong interpreter: {sys.executable}")
    payload = json.loads(INPUT.read_text(encoding="utf-8"))
    records = payload["records"]
    results: dict[str, object] = {}
    for degree in (0, 2, 4, 6):
        degree_records = [record for record in records if record["degree"] == degree]
        classes: list[dict[str, object]] = []
        canonical_codes: list[int] = []
        labeled_sum = 0
        for record in degree_records:
            adj = [[int(x) for x in row] for row in record["adjacency_rows"]]
            canonical, automorphisms = canonical_and_automorphisms(adj)
            if math.factorial(N) % automorphisms:
                raise AssertionError("orbit-stabilizer divisibility failed")
            orbit_size = math.factorial(N) // automorphisms
            canonical_codes.append(canonical)
            labeled_sum += orbit_size
            classes.append(
                {
                    "class_id": record["class_id"],
                    "graph6": record["graph6"],
                    "canonical_28bit_code_hex": f"{canonical:07x}",
                    "automorphism_group_order": automorphisms,
                    "labeled_orbit_size": orbit_size,
                }
            )
        if len(canonical_codes) != len(set(canonical_codes)):
            raise AssertionError(f"isomorphic duplicates at degree {degree}")
        independent_total = count_labeled_regular_graphs(degree)
        if labeled_sum != independent_total:
            raise AssertionError(
                f"coverage failure at degree {degree}: orbits={labeled_sum}, "
                f"independent={independent_total}"
            )
        results[str(degree)] = {
            "representative_count": len(degree_records),
            "pairwise_nonisomorphic": True,
            "orbit_size_sum": labeled_sum,
            "independent_labeled_regular_graph_count": independent_total,
            "coverage_certified": True,
            "classes": classes,
        }

    report = {
        "status": "pass",
        "method": (
            "all 8! relabelings for canonical codes and automorphism orders, "
            "plus an independent exact labeled degree-sequence recursion"
        ),
        "classification_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "degrees": results,
        "all_degree_cases_covered": True,
    }
    OUTPUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": report["status"],
                "counts": {
                    degree: data["independent_labeled_regular_graph_count"]
                    for degree, data in results.items()
                },
                "all_degree_cases_covered": True,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
