#!/usr/bin/env python3
"""Generate the exact 61-cube first-window partition for anchored F_(17,6)."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from compact_sat import triple_variables


def read_dimacs(path: Path) -> tuple[list[str], int, int, list[tuple[int, ...]], list[str]]:
    comments: list[str] = []
    clauses: list[tuple[int, ...]] = []
    body: list[str] = []
    nvars = nclauses = 0
    with path.open("r", encoding="ascii") as stream:
        for line in stream:
            if line.startswith("c"):
                comments.append(line)
            elif line.startswith("p cnf"):
                _, _, raw_vars, raw_clauses = line.split()
                nvars, nclauses = int(raw_vars), int(raw_clauses)
            elif line.strip():
                values = tuple(map(int, line.split()))
                if values[-1] != 0:
                    raise ValueError("unterminated DIMACS clause")
                clauses.append(values[:-1])
                body.append(line)
    if len(clauses) != nclauses:
        raise ValueError("DIMACS clause count mismatch")
    return comments, nvars, nclauses, clauses, body


def clause_value(clause: tuple[int, ...], assignment: dict[int, bool]) -> bool:
    return any(assignment[abs(literal)] == (literal > 0) for literal in clause)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    comments, nvars, nclauses, clauses, body = read_dimacs(args.base)
    variables = triple_variables(17)
    local_triples = tuple(itertools.combinations(range(6), 3))
    local_variables = {variables[triple] for triple in local_triples}
    extreme_variables = {
        variables[triple]
        for triple in local_triples
        if triple[0] == 0
    }
    cube_variables = tuple(
        variables[triple]
        for triple in local_triples
        if triple[0] != 0
    )
    local_clauses = tuple(
        clause for clause in clauses if {abs(literal) for literal in clause} <= local_variables
    )
    assert len(extreme_variables) == 10
    assert cube_variables == (121, 122, 123, 135, 136, 148, 226, 227, 239, 317)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for bits in itertools.product((False, True), repeat=10):
        assignment = {variable: True for variable in extreme_variables}
        assignment.update(dict(zip(cube_variables, bits)))
        if not all(clause_value(clause, assignment) for clause in local_clauses):
            continue
        tag = "".join("1" if bit else "0" for bit in bits)
        units = tuple(variable if bit else -variable for variable, bit in zip(cube_variables, bits))
        output = args.out_dir / f"cube_{tag}.cnf"
        with output.open("w", encoding="ascii", buffering=1 << 20) as stream:
            stream.writelines(comments)
            stream.write("c exact first-window cube after extreme-element normalization\n")
            stream.write(f"p cnf {nvars} {nclauses + len(units)}\n")
            stream.writelines(body)
            for literal in units:
                stream.write(f"{literal} 0\n")
        entries.append({"cube": tag, "file": output.name, "units": list(units)})
    assert len(entries) == 61
    manifest = {
        "schema_version": 1,
        "base": str(args.base),
        "normalization": "x_(0,j,k)=true for 1<=j<k<=16",
        "cube_variables": list(cube_variables),
        "all_assignments": 1024,
        "locally_inconsistent_assignments_omitted": 963,
        "local_filter_clauses": len(local_clauses),
        "cube_count": 61,
        "coverage": "every model of the normalized base formula restricts to exactly one retained first-window cube",
        "cubes": entries,
    }
    (args.out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print("verified_first_window_assignments=1024")
    print("verified_locally_inconsistent_assignments=963")
    print("wrote_exact_cubes=61")
    print(f"manifest={args.out_dir / 'manifest.json'}")


if __name__ == "__main__":
    main()
