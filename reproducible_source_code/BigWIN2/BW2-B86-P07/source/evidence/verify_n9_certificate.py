#!/usr/bin/env python3
"""Independent semantic and RUP replay checker for the N9 certificate.

This checker deliberately does not import the generator or any SAT package.
It reconstructs five-vertex comparability through explicit bijections, checks
every input clause against that reconstruction, and then validates each DRUP
addition by its own two-watched-literal unit-propagation implementation.  Proof
deletions deactivate a matching active clause.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from collections import defaultdict
from itertools import combinations, permutations
from pathlib import Path


EXPECTED_SOURCE_SHA256 = "0ef7e09d275314f53febd468b6f3933ff31d2255762112050dd71580ebc4b160"
EXPECTED_CNF_SHA256 = "70b78d1ae0f25858dd024eda62addf5f7d623a410725026e7a37200bb79f8cc4"
EXPECTED_DRUP_SHA256 = "cdfb10845b6fc6c282095187e9f1af6ec2f02456bbfb32d04cacadfaaeadb760"
LOCAL_VERTICES = tuple(range(5))
LOCAL_PAIRS = tuple(combinations(LOCAL_VERTICES, 2))
TSTAR = frozenset({(0, 1), (0, 2), (0, 3), (3, 4)})
BIJECTIONS = tuple(permutations(LOCAL_VERTICES))


def file_sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def edge(u, v):
    return (u, v) if u < v else (v, u)


def image(graph, bijection):
    return frozenset(edge(bijection[u], bijection[v]) for u, v in graph)


def embeds(graph_a, graph_b):
    return any(image(graph_a, bijection) <= graph_b for bijection in BIJECTIONS)


def local_graph(mask):
    return frozenset(pair for index, pair in enumerate(LOCAL_PAIRS) if mask >> index & 1)


def explicit_local_census():
    copies = {image(TSTAR, bijection) for bijection in BIJECTIONS}
    comparable = []
    forbidden = []
    for mask in range(1 << len(LOCAL_PAIRS)):
        graph = local_graph(mask)
        if embeds(graph, TSTAR) or embeds(TSTAR, graph):
            comparable.append((mask, graph))
            if graph not in copies:
                forbidden.append((mask, graph))
    return copies, comparable, forbidden


def parse_cnf(path):
    header = None
    clauses = []
    for line_number, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            if header is not None or clauses:
                raise ValueError(f"misplaced/duplicate CNF header at line {line_number}")
            fields = line.split()
            if len(fields) != 4 or fields[:2] != ["p", "cnf"]:
                raise ValueError(f"bad CNF header at line {line_number}")
            header = (int(fields[2]), int(fields[3]))
            continue
        if header is None:
            raise ValueError(f"clause before header at line {line_number}")
        values = [int(token) for token in line.split()]
        if not values or values[-1] != 0 or 0 in values[:-1]:
            raise ValueError(f"bad clause terminator at line {line_number}")
        clause = tuple(values[:-1])
        if any(abs(literal) > header[0] for literal in clause):
            raise ValueError(f"out-of-range literal at line {line_number}")
        if len(set(clause)) != len(clause) or any(-literal in clause for literal in clause):
            raise ValueError(f"duplicate/tautological clause at line {line_number}")
        clauses.append(clause)
    if header is None:
        raise ValueError("missing CNF header")
    if len(clauses) != header[1]:
        raise ValueError(f"header says {header[1]} clauses, parsed {len(clauses)}")
    return header, clauses


def verify_cnf_semantics(header, clauses, forbidden):
    if header != (36, 95_382):
        raise ValueError(f"unexpected CNF dimensions: {header}")
    global_pairs = tuple(combinations(range(9), 2))
    variable = {pair: index + 1 for index, pair in enumerate(global_pairs)}
    cursor = 0
    for vertices in combinations(range(9), 5):
        for _, graph in forbidden:
            expected = tuple(
                -variable[(vertices[i], vertices[j])]
                if (i, j) in graph
                else variable[(vertices[i], vertices[j])]
                for i, j in LOCAL_PAIRS
            )
            if clauses[cursor] != expected:
                raise ValueError(
                    f"CNF semantic/order mismatch at clause {cursor + 1}: "
                    f"got {clauses[cursor]}, expected {expected}"
                )
            cursor += 1
    if cursor != len(clauses):
        raise ValueError(f"semantic reconstruction covered {cursor} clauses")


def induced_local_graph(vertices, global_edges):
    position = {vertex: index for index, vertex in enumerate(vertices)}
    return frozenset(
        edge(position[u], position[v])
        for u, v in global_edges
        if u in position and v in position
    )


def verify_two_k4(copies):
    global_edges = frozenset(
        pair
        for component in (range(4), range(4, 8))
        for pair in combinations(component, 2)
    )
    edge_counts = set()
    checked = 0
    for vertices in combinations(range(8), 5):
        graph = induced_local_graph(vertices, global_edges)
        edge_counts.add(len(graph))
        if graph not in copies and (embeds(graph, TSTAR) or embeds(TSTAR, graph)):
            raise ValueError(f"2 K4 has a forbidden five-set: {vertices}")
        checked += 1
    if checked != 56 or edge_counts != {4, 6}:
        raise ValueError("unexpected 2 K4 audit totals")
    return checked, sorted(edge_counts)


def parse_proof_line(raw, line_number, variables):
    line = raw.strip()
    if not line or line.startswith("c"):
        return None
    fields = line.split()
    deletion = fields[0] == "d"
    if deletion:
        fields = fields[1:]
    values = [int(field) for field in fields]
    if not values or values[-1] != 0 or 0 in values[:-1]:
        raise ValueError(f"bad proof terminator at line {line_number}")
    clause = tuple(values[:-1])
    if any(abs(literal) > variables for literal in clause):
        raise ValueError(f"out-of-range proof literal at line {line_number}")
    if len(set(clause)) != len(clause) or any(-literal in clause for literal in clause):
        raise ValueError(f"duplicate/tautological proof clause at line {line_number}")
    if deletion and not clause:
        raise ValueError(f"empty-clause deletion at line {line_number}")
    return deletion, clause


class RupDatabase:
    """Mutable clause database with independently implemented unit propagation."""

    def __init__(self, variables):
        self.variables = variables
        self.clauses = []
        self.watch_a = []
        self.watch_b = []
        self.active = []
        self.watches = {literal: [] for variable in range(1, variables + 1) for literal in (variable, -variable)}
        self.units = []
        self.empty_count = 0
        self.by_key = defaultdict(list)
        self.active_count = 0
        self.peak_active_count = 0
        self.watch_moves = 0
        self.propagated_literals = 0

    @staticmethod
    def key(clause):
        return tuple(sorted(clause))

    def add(self, clause):
        clause = tuple(clause)
        cid = len(self.clauses)
        self.clauses.append(clause)
        self.active.append(True)
        self.active_count += 1
        self.peak_active_count = max(self.peak_active_count, self.active_count)
        self.by_key[self.key(clause)].append(cid)
        if not clause:
            self.watch_a.append(-1)
            self.watch_b.append(-1)
            self.empty_count += 1
        elif len(clause) == 1:
            self.watch_a.append(0)
            self.watch_b.append(0)
            self.units.append(cid)
        else:
            self.watch_a.append(0)
            self.watch_b.append(1)
            self.watches[clause[0]].append(cid)
            self.watches[clause[1]].append(cid)

    def delete(self, clause):
        ids = self.by_key.get(self.key(clause))
        if not ids:
            return False
        while ids and not self.active[ids[-1]]:
            ids.pop()
        if not ids:
            return False
        cid = ids.pop()
        self.active[cid] = False
        self.active_count -= 1
        if not self.clauses[cid]:
            self.empty_count -= 1
        return True

    @staticmethod
    def literal_value(literal, values):
        value = values[abs(literal)]
        return value if literal > 0 else -value

    def rup_conflict(self, candidate):
        if self.empty_count:
            return True
        values = [0] * (self.variables + 1)
        queue = []

        def enqueue(literal):
            variable = abs(literal)
            wanted = 1 if literal > 0 else -1
            if values[variable] == -wanted:
                return False
            if values[variable] == 0:
                values[variable] = wanted
                queue.append(literal)
            return True

        for literal in candidate:
            if not enqueue(-literal):
                return True
        for cid in self.units:
            if self.active[cid] and not enqueue(self.clauses[cid][0]):
                return True

        head = 0
        while head < len(queue):
            true_literal = queue[head]
            head += 1
            self.propagated_literals += 1
            false_literal = -true_literal
            watching = self.watches[false_literal]
            index = 0
            while index < len(watching):
                cid = watching[index]
                if not self.active[cid]:
                    watching[index] = watching[-1]
                    watching.pop()
                    continue
                clause = self.clauses[cid]
                a = self.watch_a[cid]
                b = self.watch_b[cid]
                if clause[a] == false_literal:
                    false_position, other_position = a, b
                    false_is_a = True
                elif clause[b] == false_literal:
                    false_position, other_position = b, a
                    false_is_a = False
                else:
                    watching[index] = watching[-1]
                    watching.pop()
                    continue
                other_literal = clause[other_position]
                if self.literal_value(other_literal, values) == 1:
                    index += 1
                    continue

                replacement = None
                for position, literal in enumerate(clause):
                    if position in (false_position, other_position):
                        continue
                    if self.literal_value(literal, values) != -1:
                        replacement = position
                        break
                if replacement is not None:
                    if false_is_a:
                        self.watch_a[cid] = replacement
                    else:
                        self.watch_b[cid] = replacement
                    self.watches[clause[replacement]].append(cid)
                    watching[index] = watching[-1]
                    watching.pop()
                    self.watch_moves += 1
                    continue

                if self.literal_value(other_literal, values) == -1:
                    return True
                if not enqueue(other_literal):
                    return True
                index += 1
        return False


def naive_conflict(clauses, assumptions, variables):
    values = [0] * (variables + 1)
    for literal in assumptions:
        wanted = 1 if literal > 0 else -1
        if values[abs(literal)] == -wanted:
            return True
        values[abs(literal)] = wanted
    changed = True
    while changed:
        changed = False
        for clause in clauses:
            if not clause:
                return True
            satisfied = False
            unassigned = []
            for literal in clause:
                value = values[abs(literal)]
                value = value if literal > 0 else -value
                if value == 1:
                    satisfied = True
                    break
                if value == 0:
                    unassigned.append(literal)
            if satisfied:
                continue
            if not unassigned:
                return True
            if len(unassigned) == 1:
                literal = unassigned[0]
                wanted = 1 if literal > 0 else -1
                if values[abs(literal)] == -wanted:
                    return True
                if values[abs(literal)] == 0:
                    values[abs(literal)] = wanted
                    changed = True
    return False


def self_test_watches():
    rng = random.Random(0x4E39)
    trials = 400
    for trial in range(trials):
        variables = rng.randrange(2, 9)
        clauses = []
        database = RupDatabase(variables)
        for _ in range(rng.randrange(0, 25)):
            size = rng.randrange(0, min(5, variables) + 1)
            chosen = rng.sample(range(1, variables + 1), size)
            clause = tuple(variable if rng.randrange(2) else -variable for variable in chosen)
            clauses.append(clause)
            database.add(clause)
        for _ in range(8):
            size = rng.randrange(0, variables + 1)
            chosen = rng.sample(range(1, variables + 1), size)
            candidate = tuple(variable if rng.randrange(2) else -variable for variable in chosen)
            expected = naive_conflict(clauses, tuple(-literal for literal in candidate), variables)
            observed = database.rup_conflict(candidate)
            if observed != expected:
                raise AssertionError(
                    f"watch self-test mismatch in trial {trial}: expected {expected}, got {observed}"
                )
    return trials * 8


def replay_proof(path, variables, input_clauses):
    database = RupDatabase(variables)
    for clause in input_clauses:
        database.add(clause)
    additions = 0
    deletions = 0
    checked_lines = 0
    last_operation = None
    for line_number, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        parsed = parse_proof_line(raw, line_number, variables)
        if parsed is None:
            continue
        deletion, clause = parsed
        checked_lines += 1
        if deletion:
            if not database.delete(clause):
                raise ValueError(f"deletion has no active match at proof line {line_number}")
            deletions += 1
            last_operation = ("deletion", clause)
        else:
            if not database.rup_conflict(clause):
                raise ValueError(f"addition is not RUP at proof line {line_number}: {clause}")
            database.add(clause)
            additions += 1
            last_operation = ("addition", clause)
    if last_operation != ("addition", ()):
        raise ValueError("proof does not finish by adding the empty clause")
    return {
        "proof_lines_checked": checked_lines,
        "rup_additions_verified": additions,
        "deletions_applied": deletions,
        "final_empty_clause_verified": True,
        "peak_active_clauses": database.peak_active_count,
        "watch_moves": database.watch_moves,
        "propagated_literals": database.propagated_literals,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("source.md"))
    parser.add_argument("--cnf", type=Path, default=Path("evidence/n9_tstar_exact.cnf"))
    parser.add_argument("--proof", type=Path, default=Path("evidence/n9_tstar_exact.drup"))
    parser.add_argument("--log", type=Path, default=Path("evidence/n9_independent_replay.log"))
    args = parser.parse_args()

    source_digest = file_sha256(args.source)
    cnf_digest = file_sha256(args.cnf)
    proof_digest = file_sha256(args.proof)
    if source_digest != EXPECTED_SOURCE_SHA256:
        raise SystemExit(f"unexpected immutable source SHA-256: {source_digest}")
    if cnf_digest != EXPECTED_CNF_SHA256:
        raise SystemExit(f"unexpected CNF SHA-256: {cnf_digest}")
    if proof_digest != EXPECTED_DRUP_SHA256:
        raise SystemExit(f"unexpected DRUP SHA-256: {proof_digest}")

    synthetic_checks = self_test_watches()
    copies, comparable, forbidden = explicit_local_census()
    if (len(copies), len(comparable), len(forbidden)) != (60, 817, 757):
        raise SystemExit("explicit-bijection census mismatch")
    header, clauses = parse_cnf(args.cnf)
    verify_cnf_semantics(header, clauses, forbidden)
    lower_checked, lower_edge_counts = verify_two_k4(copies)
    replay = replay_proof(args.proof, header[0], clauses)

    lines = [
        "checker=independent explicit-bijection semantic audit and two-watched-literal RUP replay",
        "sat_library_imported=false",
        f"synthetic_watched_vs_naive_checks={synthetic_checks}",
        f"source_sha256={source_digest}",
        f"labeled_tstar_copies={len(copies)}",
        f"comparable_patterns_including_tstar={len(comparable)}",
        f"forbidden_comparable_nonisomorphic_patterns={len(forbidden)}",
        "nine_vertex_five_sets=126",
        f"cnf_variables={header[0]}",
        f"cnf_clauses_semantically_checked={len(clauses)}",
        f"cnf_sha256={cnf_digest}",
        f"two_k4_five_sets_checked={lower_checked}",
        f"two_k4_distinct_induced_edge_counts={lower_edge_counts}",
        "two_k4_is_tstar_exact=true",
        f"proof_sha256={proof_digest}",
    ]
    lines.extend(f"{key}={str(value).lower() if isinstance(value, bool) else value}" for key, value in replay.items())
    lines.append("result=VERIFIED")
    args.log.write_text("\n".join(lines) + "\n", encoding="ascii")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
