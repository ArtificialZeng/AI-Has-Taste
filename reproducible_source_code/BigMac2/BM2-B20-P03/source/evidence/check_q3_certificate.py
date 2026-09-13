#!/usr/bin/env python3
"""Standalone exhaustive replay checker for a Q_3 certificate.

This checker does not import the solver.  It represents vertices as coordinate
triples and derives directional answers from graph distance, rather than using
the solver's xor-toward-target formula.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


COORDS = tuple(itertools.product((0, 1), repeat=3))
LABEL_OF = {coordinate: index for index, coordinate in enumerate(COORDS)}
ALL_ACTIONS = tuple(itertools.product(range(8), repeat=3))
ALL_BELIEFS = set(range(1, 256))


def distance(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(x != y for x, y in zip(left, right))


def neighbors(vertex: tuple[int, int, int]) -> set[tuple[int, int, int]]:
    return {
        tuple(1 - bit if index == coordinate else bit for index, bit in enumerate(vertex))
        for coordinate in range(3)
    }


def responses(probe_label: int, robber_label: int) -> set[int]:
    probe = COORDS[probe_label]
    robber = COORDS[robber_label]
    if probe == robber:
        return {probe_label}
    target_distance = distance(probe, robber) - 1
    return {LABEL_OF[q] for q in neighbors(probe) if distance(q, robber) == target_distance}


def members(mask: int) -> set[int]:
    return {label for label in range(8) if mask & (1 << label)}


def mask_of(labels: set[int]) -> int:
    return sum(1 << label for label in labels)


def recontaminate(mask: int) -> int:
    positions = members(mask)
    expanded = set(positions)
    for label in positions:
        expanded.update(LABEL_OF[q] for q in neighbors(COORDS[label]))
    return mask_of(expanded)


def answer_fibers(belief: int, action: tuple[int, int, int]) -> dict[tuple[int, int, int], int]:
    fibers: dict[tuple[int, int, int], set[int]] = {}
    for robber in members(belief):
        component_responses = [responses(probe, robber) for probe in action]
        for public_answer in itertools.product(*component_responses):
            fibers.setdefault(public_answer, set()).add(robber)
    return {answer: mask_of(positions) for answer, positions in fibers.items()}


def check_metadata(certificate: dict[str, object]) -> None:
    assert certificate["schema"] == "q3-directional-localization-certificate-v1"
    assert certificate["probe_count"] == 3
    assert certificate["all_nonempty_beliefs_count"] == 255
    assert certificate["all_ordered_probe_actions_count"] == 512
    assert certificate["initial_belief"] == 255
    assert len(ALL_ACTIONS) == 512 and len(set(ALL_ACTIONS)) == 512
    assert len(ALL_BELIEFS) == 255


def check_strategy(certificate: dict[str, object]) -> tuple[set[int], int, int]:
    rows = certificate["strategy"]
    assert isinstance(rows, list)
    ranks: dict[int, int] = {}
    probes: dict[int, tuple[int, int, int]] = {}
    for row in rows:
        assert isinstance(row, dict)
        belief = row["belief"]
        rank = row["rank"]
        assert isinstance(belief, int) and belief in ALL_BELIEFS
        assert isinstance(rank, int) and rank >= 0 and belief not in ranks
        ranks[belief] = rank
        if "probes" in row:
            action = tuple(row["probes"])
            assert len(action) == 3 and all(type(x) is int and 0 <= x < 8 for x in action)
            probes[belief] = action

    for label in range(8):
        singleton = 1 << label
        assert ranks.get(singleton) == 0 and singleton not in probes

    replayed_answers = 0
    replayed_transitions = 0
    for belief, rank in sorted(ranks.items()):
        if belief.bit_count() == 1:
            assert rank == 0
            continue
        assert rank > 0 and belief in probes
        fibers = answer_fibers(belief, probes[belief])
        assert fibers
        for fiber in fibers.values():
            replayed_answers += 1
            if fiber.bit_count() == 1:
                continue
            successor = recontaminate(fiber)
            replayed_transitions += 1
            assert successor in ranks
            assert ranks[successor] < rank
    return set(ranks), replayed_answers, replayed_transitions


def check_winning(certificate: dict[str, object], winning: set[int]) -> tuple[int, int]:
    assert certificate["result"] == "three_cops_win"
    assert 255 in winning
    assert certificate["initial_rank"] == next(
        row["rank"] for row in certificate["strategy"] if row["belief"] == 255
    )
    assert certificate["trap_beliefs"] == []
    assert certificate["trap_witnesses"] == []
    return 0, 0


def check_losing(certificate: dict[str, object], winning: set[int]) -> tuple[int, int]:
    assert certificate["result"] == "three_cops_do_not_win"
    trap_list = certificate["trap_beliefs"]
    assert isinstance(trap_list, list)
    trap = set(trap_list)
    assert len(trap) == len(trap_list)
    assert trap == ALL_BELIEFS - winning
    assert 255 in trap and not any(mask.bit_count() == 1 for mask in trap)
    assert certificate["initial_rank"] is None

    witness_rows = certificate["trap_witnesses"]
    assert isinstance(witness_rows, list)
    indexed: dict[int, list[list[int]]] = {}
    for row in witness_rows:
        assert isinstance(row, dict)
        belief = row["belief"]
        assert belief in trap and belief not in indexed
        answers = row["answers_in_action_order"]
        assert isinstance(answers, list) and len(answers) == len(ALL_ACTIONS)
        indexed[belief] = answers
    assert set(indexed) == trap

    checked_pairs = 0
    checked_supports = 0
    for belief in sorted(trap):
        for action_index, action in enumerate(ALL_ACTIONS):
            answer_list = indexed[belief][action_index]
            assert isinstance(answer_list, list) and len(answer_list) == 3
            answer = tuple(answer_list)
            assert all(type(x) is int and 0 <= x < 8 for x in answer)
            fibers = answer_fibers(belief, action)
            assert answer in fibers
            fiber = fibers[answer]
            assert fiber.bit_count() >= 2
            assert recontaminate(fiber) in trap
            checked_pairs += 1
            checked_supports += fiber.bit_count()
    return checked_pairs, checked_supports


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=Path("evidence/q3_certificate.json"))
    parser.add_argument("--report", type=Path, default=Path("evidence/replay_report.json"))
    args = parser.parse_args()

    raw = args.certificate.read_bytes()
    certificate = json.loads(raw)
    check_metadata(certificate)
    winning, replayed_answers, replayed_transitions = check_strategy(certificate)

    if certificate["result"] == "three_cops_win":
        trap_pairs, trap_supports = check_winning(certificate, winning)
    elif certificate["result"] == "three_cops_do_not_win":
        trap_pairs, trap_supports = check_losing(certificate, winning)
    else:
        raise AssertionError("unknown result")

    assert certificate["winning_beliefs_count"] == len(winning)
    assert certificate["losing_beliefs_count"] == 255 - len(winning)
    report = {
        "checker": "standalone tuple-coordinate exhaustive replay",
        "certificate": str(args.certificate),
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verdict": "PASS",
        "result": certificate["result"],
        "belief_domain_size_checked": len(ALL_BELIEFS),
        "ordered_action_domain_size_checked": len(ALL_ACTIONS),
        "strategy_beliefs_checked": len(winning),
        "strategy_answer_fibers_checked": replayed_answers,
        "strategy_nonsingleton_transitions_checked": replayed_transitions,
        "trap_belief_action_pairs_checked": trap_pairs,
        "sum_of_trap_witness_fiber_sizes": trap_supports,
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
