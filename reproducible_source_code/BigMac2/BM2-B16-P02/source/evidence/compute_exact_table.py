#!/usr/bin/env python3
"""Exact finite experiment for the cube-of-broom closed-neighborhood ideal.

The graph balls are reconstructed from the edge list by breadth-first search;
no closed-form generator description is used to create the Singular input.
For each requested case Singular 4.4.1 computes a minimal graded resolution
over the chosen field and the Krull dimension.  A separate exhaustive hitting-
set calculation checks the monomial height and supplies a minimum cover.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import pathlib
import subprocess
import tempfile
from collections import deque


def broom(n: int, m: int):
    vertices = [f"x{i}" for i in range(1, n + 1)] + [f"y{j}" for j in range(1, m + 1)]
    adjacency = {v: set() for v in vertices}
    for i in range(1, n + 1):
        adjacency[f"x{i}"].add("y1")
        adjacency["y1"].add(f"x{i}")
    for j in range(1, m):
        a, b = f"y{j}", f"y{j + 1}"
        adjacency[a].add(b)
        adjacency[b].add(a)
    return vertices, adjacency


def radius_three_balls(n: int, m: int):
    vertices, adjacency = broom(n, m)
    balls = []
    for root in vertices:
        distances = {root: 0}
        queue = deque([root])
        while queue:
            v = queue.popleft()
            if distances[v] == 3:
                continue
            for w in adjacency[v]:
                if w not in distances:
                    distances[w] = distances[v] + 1
                    queue.append(w)
        balls.append(frozenset(distances))
    return vertices, balls


def minimal_supports(balls):
    unique = sorted(set(balls), key=lambda s: (len(s), sorted(s)))
    return [s for s in unique if not any(t < s for t in unique)]


def expected_supports(n: int, m: int):
    xs = {f"x{i}" for i in range(1, n + 1)}
    if m <= 3:
        return [frozenset(xs | {f"y{j}" for j in range(1, m + 1)})]
    answer = [frozenset(xs | {"y1", "y2", "y3"})]
    answer.extend(
        frozenset(f"y{j}" for j in range(a, a + 7))
        for a in range(1, m - 6)
    )
    answer.append(frozenset(f"y{j}" for j in range(m - 3, m + 1)))
    return sorted(answer, key=lambda s: (len(s), sorted(s)))


def minimum_hitting_set(vertices, supports):
    for size in range(len(vertices) + 1):
        for choice in itertools.combinations(vertices, size):
            cover = set(choice)
            if all(cover & support for support in supports):
                return list(choice), size
    raise AssertionError("finite hypergraph had no hitting set")


def singular_case(singular: str, characteristic: int, vertices, supports):
    variables = ",".join(vertices)
    monomials = ["*".join(v for v in vertices if v in support) for support in supports]
    ideal = ",".join(monomials)
    program = f"""ring r={characteristic},({variables}),dp;
ideal I={ideal};
resolution R=mres(I,0);
intmat B=betti(R);
int pd=size(R)-1;
int reg=-1;
int rr;
int cc;
for (rr=1;rr<=nrows(B);rr++) {{
  for (cc=1;cc<=ncols(B);cc++) {{
    if (B[rr,cc]<>0) {{ reg=rr-1; }}
  }}
}}
int ht=nvars(r)-dim(std(I));
print("SUMMARY "+string(pd)+" "+string(reg)+" "+string(ht)+" "+string(nrows(B))+" "+string(ncols(B)));
for (rr=1;rr<=nrows(B);rr++) {{
  string row="ROW";
  for (cc=1;cc<=ncols(B);cc++) {{ row=row+" "+string(B[rr,cc]); }}
  print(row);
}}
quit;
"""
    with tempfile.TemporaryDirectory(prefix="broom-cube-") as directory:
        input_path = pathlib.Path(directory) / "case.sing"
        input_path.write_text(program, encoding="utf-8")
        completed = subprocess.run(
            [singular, "-q", str(input_path)],
            check=True,
            capture_output=True,
            text=True,
        )
    lines = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    summary = next((line for line in lines if line.startswith("SUMMARY ")), None)
    if summary is None:
        raise RuntimeError(f"Singular output lacked SUMMARY: {completed.stdout}\n{completed.stderr}")
    pd, reg, height, nrows, ncols = map(int, summary.split()[1:])
    rows = [[int(x) for x in line.split()[1:]] for line in lines if line.startswith("ROW")]
    if len(rows) != nrows or any(len(row) != ncols for row in rows):
        raise RuntimeError(f"malformed Betti matrix: {lines}")
    return {"pd": pd, "reg": reg, "height": height, "betti": rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--singular", default="/opt/homebrew/bin/Singular")
    parser.add_argument("--max-m", type=int, default=24)
    parser.add_argument("--output", default="evidence/exact_table.json")
    args = parser.parse_args()

    source_hash = hashlib.sha256(pathlib.Path("source.md").read_bytes()).hexdigest()
    version = subprocess.run(
        [args.singular, "--version"], check=True, capture_output=True, text=True
    ).stdout.splitlines()[0]
    cases = []
    for n in (2, 3):
        for m in range(2, args.max_m + 1):
            vertices, balls = radius_three_balls(n, m)
            supports = minimal_supports(balls)
            expected = expected_supports(n, m)
            if sorted(supports, key=lambda s: (len(s), sorted(s))) != expected:
                raise AssertionError(f"generator formula mismatch at n={n}, m={m}")
            cover, combinatorial_height = minimum_hitting_set(vertices, supports)
            by_characteristic = {}
            for characteristic in (0, 2):
                result = singular_case(args.singular, characteristic, vertices, supports)
                if result["height"] != combinatorial_height:
                    raise AssertionError(
                        f"height mismatch at {(n, m, characteristic)}: "
                        f"{result['height']} vs {combinatorial_height}"
                    )
                by_characteristic[str(characteristic)] = result
            cases.append(
                {
                    "n": n,
                    "m": m,
                    "minimal_generator_supports": [
                        [v for v in vertices if v in support] for support in supports
                    ],
                    "height_cover": cover,
                    "height_lower_bound_method": (
                        "exhaustive rejection of every smaller subset of the displayed vertex order"
                    ),
                    "characteristics": by_characteristic,
                }
            )

    char_discrepancies = []
    for case in cases:
        zero = case["characteristics"]["0"]
        two = case["characteristics"]["2"]
        if zero != two:
            char_discrepancies.append({"n": case["n"], "m": case["m"]})
    formula_discrepancies = []
    n_invariant_pattern_discrepancies = []
    keyed = {(case["n"], case["m"]): case for case in cases}
    for case in cases:
        n, m = case["n"], case["m"]
        predicted = {
            "pd": m // 4 + 1,
            "reg": n + m - 1 - m // 4,
            "height": m // 7 + 1,
        }
        for characteristic in ("0", "2"):
            observed = case["characteristics"][characteristic]
            if any(observed[key] != predicted[key] for key in predicted):
                formula_discrepancies.append(
                    {
                        "n": n,
                        "m": m,
                        "characteristic": int(characteristic),
                        "observed": {key: observed[key] for key in predicted},
                        "predicted": predicted,
                    }
                )
    for m in range(2, args.max_m + 1):
        for characteristic in ("0", "2"):
            left = keyed[(2, m)]["characteristics"][characteristic]
            right = keyed[(3, m)]["characteristics"][characteristic]
            if not (
                left["pd"] == right["pd"]
                and left["height"] == right["height"]
                and right["reg"] == left["reg"] + 1
            ):
                n_invariant_pattern_discrepancies.append(
                    {"m": m, "characteristic": int(characteristic)}
                )

    payload = {
        "schema": "broom-cube-exact-table-v1",
        "method": {
            "balls": "BFS from every vertex in the defining broom edge list, truncated at distance 3",
            "minimal_generators": "deduplicate ball supports and delete every strict superset",
            "resolution": "Singular mres(I,0), with pd=size(R)-1 and reg read from betti(R)",
            "height": "nvars-dim(std(I)), independently checked by exhaustive minimum hitting sets",
            "singular_version": version,
            "source_sha256_before_run": source_hash,
        },
        "coverage": {"n": [2, 3], "m": [2, args.max_m], "characteristics": [0, 2]},
        "checks": {
            "all_generator_sets_match_problem_md_formula": True,
            "all_singular_heights_match_exhaustive_hitting_sets": True,
            "characteristic_discrepancies": char_discrepancies,
            "formula_discrepancies": formula_discrepancies,
            "n_invariant_pattern_discrepancies": n_invariant_pattern_discrepancies,
        },
        "cases": cases,
    }
    output = pathlib.Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "cases": len(cases), "checks": payload["checks"]}))


if __name__ == "__main__":
    main()
