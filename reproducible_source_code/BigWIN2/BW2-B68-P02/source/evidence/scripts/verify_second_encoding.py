#!/usr/bin/env python3
"""Bind and replay the independent order-16 equitable-UNSAT certificates.

This verifier deliberately avoids NetworkX, the primary SAT encoder, and
PySAT's cardinality encoders.  It reconstructs each DIMACS file directly from
its graph6 row and the at-most-four vertex-color characterization, then replays
the retained DRAT trace.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_graph6(code: str) -> tuple[int, list[tuple[int, int]]]:
    assert code and 63 < ord(code[0]) < 126
    n = ord(code[0]) - 63
    assert n == 16
    bits = [((ord(char) - 63) >> shift) & 1 for char in code[1:] for shift in range(5, -1, -1)]
    needed = n * (n - 1) // 2
    assert len(bits) >= needed and not any(bits[needed:])
    edges: list[tuple[int, int]] = []
    cursor = 0
    for v in range(n):
        for u in range(v):
            if bits[cursor]:
                edges.append((u, v))
            cursor += 1
    assert len(edges) == 3 * n // 2
    assert all(sum(vertex in edge for edge in edges) == 3 for vertex in range(n))
    return n, edges


def expected_dimacs(code: str) -> tuple[bytes, int, int]:
    n, edges = decode_graph6(code)
    edge_set = set(edges)
    elements = [frozenset((v,)) for v in range(n)] + [frozenset(edge) for edge in sorted(edges)]

    def variable(element: int, color: int) -> int:
        return 4 * element + color + 1

    clauses: list[list[int]] = []
    for element in range(len(elements)):
        clauses.append([variable(element, color) for color in range(4)])
        clauses.extend(
            [-variable(element, first), -variable(element, second)]
            for first, second in itertools.combinations(range(4), 2)
        )
    for first, second in itertools.combinations(range(len(elements)), 2):
        conflict = (
            (first < n and second < n and (first, second) in edge_set)
            or (second >= n and bool(elements[first] & elements[second]))
        )
        if conflict:
            clauses.extend(
                [-variable(first, color), -variable(second, color)] for color in range(4)
            )
    clauses.append([variable(0, 0)])
    for color in range(4):
        clauses.extend(
            [-variable(vertex, color) for vertex in subset]
            for subset in itertools.combinations(range(n), 5)
        )
    variables = 4 * len(elements)
    raw = (
        f"p cnf {variables} {len(clauses)}\n"
        + "".join(" ".join(map(str, clause)) + " 0\n" for clause in clauses)
    ).encode("ascii")
    return raw, variables, len(clauses)


def main() -> None:
    witnesses = [
        json.loads(line)
        for line in (ROOT / "evidence/coloring_witnesses.jsonl").read_text().splitlines()
    ]
    candidates = [row for row in witnesses if row["classification"] == "A_sat_E_unsat_observed"]
    assert len(candidates) == 16 and all(row["n"] == 16 for row in candidates)

    generation = json.loads((ROOT / "evidence/second_encoding_verification.json").read_text())
    assert generation["status"] == "pass" and generation["count"] == 16
    records = {(row["n"], row["index"]): row for row in generation["records"]}
    candidate_keys = {(row["n"], row["index"]) for row in candidates}
    assert set(records) == candidate_keys

    census = (ROOT / "census/n16.g6").read_text().splitlines()
    replayed = 0
    bound = 0
    for candidate in candidates:
        key = candidate["n"], candidate["index"]
        record = records[key]
        code = candidate["graph6"]
        assert census[candidate["index"]] == record["graph6"] == code
        expected, variables, clauses = expected_dimacs(code)
        cnf = ROOT / record["cnf"]
        proof = ROOT / record["proof"]
        assert cnf.read_bytes() == expected
        assert record["variables"] == variables == 160
        assert record["clauses"] == clauses == 18233
        assert sha256(cnf) == record["cnf_sha256"]
        assert sha256(proof) == record["proof_sha256"]
        result = subprocess.run(
            [str(ROOT / "tools/drat-trim"), str(cnf), str(proof)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        assert result.returncode == 0 and "s VERIFIED" in result.stdout, (key, result.stdout[-2000:])
        bound += 1
        replayed += 1

    report = {
        "status": "pass",
        "script": str(Path(__file__).relative_to(ROOT)),
        "encoding_basis": (
            "At order 16, a proper 4-total coloring is equitable iff each color is used on "
            "exactly four vertices: at every cubic vertex its own color and the colors of its "
            "three incident edges are all four colors, so a color class has size (16+|S_c|)/2. "
            "The CNF enforces |S_c|<=4 for all c; the 16 exactly-one vertex colors force equality."
        ),
        "candidate_bindings_checked": bound,
        "drat_proofs_replayed": replayed,
        "checker": "tools/drat-trim",
        "checker_sha256": sha256(ROOT / "tools/drat-trim"),
        "generation_report_sha256": sha256(ROOT / "evidence/second_encoding_verification.json"),
    }
    output = ROOT / "evidence/second_encoding_replay.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
