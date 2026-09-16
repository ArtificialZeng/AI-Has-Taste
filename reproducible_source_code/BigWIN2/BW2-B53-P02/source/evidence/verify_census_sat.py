#!/usr/bin/env python3
"""Independent exact replay of the n <= 60 ICG census.

Unlike enumerate_icg.py, this program stores ordinary neighbour sets, tests
connectivity with union-find, tests bipartiteness by parity propagation, and
decides 3-colourability/uniqueness through an explicit CNF and DPLL SAT solver.
It also validates every witness emitted by the primary census.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path


def divisors(n: int) -> list[int]:
    out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            if d < n:
                out.append(d)
            q = n // d
            if q != d and q < n:
                out.append(q)
        d += 1
    return sorted(out)


def make_graph(n: int, ds: list[int]) -> tuple[list[set[int]], list[tuple[int, int]]]:
    allowed_steps = {
        a for a in range(1, n) if math.gcd(a, n) in set(ds)
    }
    nbr = [set() for _ in range(n)]
    for u in range(n):
        for a in allowed_steps:
            nbr[u].add((u + a) % n)
    edges = [(u, v) for u in range(n) for v in nbr[u] if u < v]
    return nbr, edges


def row_digest(nbr: list[set[int]]) -> str:
    h = hashlib.sha256()
    width = max(1, (len(nbr) + 7) // 8)
    for neighbors in nbr:
        row = sum(1 << v for v in neighbors)
        h.update(row.to_bytes(width, "little"))
    return h.hexdigest()


class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[b] = a


def connected(n: int, edges: list[tuple[int, int]]) -> bool:
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return len({uf.find(v) for v in range(n)}) == 1


def triangle(nbr: list[set[int]], edges: list[tuple[int, int]]) -> bool:
    return any(nbr[u].intersection(nbr[v]) for u, v in edges)


def two_colorable(nbr: list[set[int]]) -> bool:
    sign: dict[int, int] = {}
    for root in range(len(nbr)):
        if root in sign:
            continue
        sign[root] = 0
        todo = [root]
        while todo:
            u = todo.pop()
            for v in nbr[u]:
                if v not in sign:
                    sign[v] = 1 - sign[u]
                    todo.append(v)
                elif sign[v] == sign[u]:
                    return False
    return True


def var(v: int, c: int) -> int:
    return 3 * v + c + 1


def coloring_cnf(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, ...]]:
    clauses: list[tuple[int, ...]] = []
    for v in range(n):
        clauses.append((var(v, 0), var(v, 1), var(v, 2)))
        for a, b in ((0, 1), (0, 2), (1, 2)):
            clauses.append((-var(v, a), -var(v, b)))
    for u, v in edges:
        for c in range(3):
            clauses.append((-var(u, c), -var(v, c)))
    # Every unlabelled partition has a representative with vertex 0 coloured 0.
    clauses.append((var(0, 0),))
    return clauses


def dpll(clauses: list[tuple[int, ...]], nvars: int) -> list[bool] | None:
    def propagate(assignment: dict[int, bool]) -> tuple[bool, dict[int, bool]]:
        assignment = dict(assignment)
        while True:
            unit: int | None = None
            for clause in clauses:
                satisfied = False
                remaining: list[int] = []
                for lit in clause:
                    value = assignment.get(abs(lit))
                    if value is None:
                        remaining.append(lit)
                    elif value == (lit > 0):
                        satisfied = True
                        break
                if satisfied:
                    continue
                if not remaining:
                    return False, assignment
                if len(remaining) == 1:
                    unit = remaining[0]
                    break
            if unit is None:
                return True, assignment
            key, value = abs(unit), unit > 0
            if key in assignment and assignment[key] != value:
                return False, assignment
            assignment[key] = value

    def search(assignment: dict[int, bool]) -> dict[int, bool] | None:
        ok, assignment = propagate(assignment)
        if not ok:
            return None
        scores: Counter[int] = Counter()
        all_satisfied = True
        for clause in clauses:
            sat = any(
                abs(lit) in assignment and assignment[abs(lit)] == (lit > 0)
                for lit in clause
            )
            if sat:
                continue
            all_satisfied = False
            for lit in clause:
                if abs(lit) not in assignment:
                    scores[abs(lit)] += 1
        if all_satisfied:
            return assignment
        choice = max(scores, key=lambda x: (scores[x], -x))
        for value in (True, False):
            branch = dict(assignment)
            branch[choice] = value
            answer = search(branch)
            if answer is not None:
                return answer
        return None

    answer = search({})
    if answer is None:
        return None
    return [answer.get(i, False) for i in range(1, nvars + 1)]


def sat_coloring(n: int, model: list[bool]) -> list[int]:
    result = []
    for v in range(n):
        colors = [c for c in range(3) if model[var(v, c) - 1]]
        assert len(colors) == 1
        result.append(colors[0])
    return result


def sat_three_color_status(n: int, edges: list[tuple[int, int]]) -> tuple[bool, bool | None]:
    clauses = coloring_cnf(n, edges)
    model = dpll(clauses, 3 * n)
    if model is None:
        return False, None
    coloring = sat_coloring(n, model)
    # With c(0)=0, precisely two labelled solutions realize this partition.
    # Block both: the model and the result of swapping names 1 and 2.
    clauses.append(tuple(-var(v, coloring[v]) for v in range(n)))
    swapped = [0 if c == 0 else 3 - c for c in coloring]
    clauses.append(tuple(-var(v, swapped[v]) for v in range(n)))
    other = dpll(clauses, 3 * n)
    return True, other is None


def partition_valid(part: list[list[int]], n: int, edges: list[tuple[int, int]]) -> bool:
    if len(part) != 3 or any(not cls for cls in part):
        return False
    flat = [v for cls in part for v in cls]
    if sorted(flat) != list(range(n)) or len(flat) != len(set(flat)):
        return False
    col = {v: c for c, cls in enumerate(part) for v in cls}
    return all(col[u] != col[v] for u, v in edges)


def same_unordered_partition(a: list[list[int]], b: list[list[int]]) -> bool:
    return {frozenset(x) for x in a} == {frozenset(x) for x in b}


def validate_primary_record(rec: dict, ds: list[int], nbr: list[set[int]], edges: list[tuple[int, int]]) -> list[str]:
    errors: list[str] = []
    n = rec["n"]
    if rec["D"] != ds or rec["edges"] != len(edges):
        errors.append("domain-or-edge-count")
    if rec.get("adjacency_sha256") != row_digest(nbr):
        errors.append("adjacency-digest")
    reason = rec["reason"]
    if reason == "edgeless" and edges:
        errors.append("edgeless-witness")
    elif reason == "disconnected":
        comps = rec.get("components", [])
        if connected(n, edges) or sorted(v for c in comps for v in c) != list(range(n)):
            errors.append("component-witness")
        for c in comps:
            cs = set(c)
            if any((u in cs) != (v in cs) for u, v in edges):
                errors.append("component-cross-edge")
                break
    elif reason == "triangle":
        t = rec.get("triangle", [])
        if len(t) != 3 or any(v not in nbr[u] for u, v in itertools.combinations(t, 2)):
            errors.append("triangle-witness")
    elif reason == "bipartite":
        p = rec.get("bipartition", [])
        if len(p) != 2 or sorted(v for c in p for v in c) != list(range(n)):
            errors.append("bipartition-cover")
        else:
            side = {v: i for i, c in enumerate(p) for v in c}
            if any(side[u] == side[v] for u, v in edges):
                errors.append("bipartition-edge")
    elif reason == "nonunique_3_colorable":
        p = rec.get("color_partitions", [])
        if len(p) < 2 or any(not partition_valid(x, n, edges) for x in p[:2]):
            errors.append("multiple-coloring-witness")
        elif same_unordered_partition(p[0], p[1]):
            errors.append("colorings-not-distinct")
    elif reason == "qualifies":
        if not partition_valid(rec.get("unique_color_partition", []), n, edges):
            errors.append("unique-coloring-witness")
    if reason in {"not_3_colorable", "nonunique_3_colorable", "qualifies"}:
        cyc = rec.get("odd_cycle", [])
        if len(cyc) % 2 != 1 or len(cyc) < 3:
            errors.append("odd-cycle-parity")
        elif any(cyc[(i + 1) % len(cyc)] not in nbr[cyc[i]] for i in range(len(cyc))):
            errors.append("odd-cycle-edge")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--primary", type=Path, required=True)
    ap.add_argument("--records", type=Path, required=True)
    ap.add_argument("--audit", type=Path, required=True)
    ap.add_argument("--max-n", type=int, default=60)
    args = ap.parse_args()

    primary_lines = args.primary.read_text(encoding="utf-8").splitlines()
    primary = [json.loads(line) for line in primary_lines]
    expected_pairs = sum(1 << len(divisors(n)) for n in range(1, args.max_n + 1))
    mismatches: list[dict] = []
    witness_errors: list[dict] = []
    independent_counts: Counter[str] = Counter()
    qualifiers: list[dict] = []
    index = 0
    h = hashlib.sha256()
    with args.records.open("w", encoding="utf-8") as out:
        for n in range(1, args.max_n + 1):
            divs = divisors(n)
            for mask in range(1 << len(divs)):
                ds = [d for i, d in enumerate(divs) if mask & (1 << i)]
                nbr, edges = make_graph(n, ds)
                if not edges:
                    verdict = "edgeless"
                elif not connected(n, edges):
                    verdict = "disconnected"
                elif triangle(nbr, edges):
                    verdict = "triangle"
                elif two_colorable(nbr):
                    verdict = "bipartite"
                else:
                    sat3, unique = sat_three_color_status(n, edges)
                    if not sat3:
                        verdict = "not_3_colorable"
                    elif unique:
                        verdict = "qualifies"
                    else:
                        verdict = "nonunique_3_colorable"
                rec = {
                    "n": n,
                    "mask": mask,
                    "D": ds,
                    "edges": len(edges),
                    "adjacency_sha256": row_digest(nbr),
                    "verdict": verdict,
                }
                line = json.dumps(rec, sort_keys=True, separators=(",", ":"))
                out.write(line + "\n")
                h.update((line + "\n").encode())
                independent_counts[verdict] += 1
                if verdict == "qualifies":
                    qualifiers.append({"n": n, "D": ds})
                if index >= len(primary):
                    mismatches.append({"index": index, "error": "missing-primary"})
                else:
                    p = primary[index]
                    if (p.get("n"), p.get("mask"), p.get("D"), p.get("reason")) != (n, mask, ds, verdict):
                        mismatches.append({
                            "index": index,
                            "primary": [p.get("n"), p.get("mask"), p.get("D"), p.get("reason")],
                            "independent": [n, mask, ds, verdict],
                        })
                    errs = validate_primary_record(p, ds, nbr, edges)
                    if errs:
                        witness_errors.append({"index": index, "errors": errs})
                index += 1
    if len(primary) != expected_pairs:
        mismatches.append({"error": "primary-length", "actual": len(primary), "expected": expected_pairs})
    audit = {
        "method": "independent neighbor-set/union-find predicates and CNF DPLL 3-color audit",
        "max_n": args.max_n,
        "expected_pairs": expected_pairs,
        "checked_pairs": index,
        "primary_file_sha256": hashlib.sha256(args.primary.read_bytes()).hexdigest(),
        "independent_records_sha256": h.hexdigest(),
        "independent_counts": dict(sorted(independent_counts.items())),
        "qualifiers": qualifiers,
        "classification_mismatches": mismatches,
        "primary_witness_errors": witness_errors,
        "all_classifications_match": not mismatches,
        "all_primary_witnesses_valid": not witness_errors,
    }
    args.audit.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if mismatches or witness_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
