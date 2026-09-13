#!/usr/bin/env python3
"""Exact retrograde solver for the three-probe directional game on Q_3.

The implementation uses 8-bit masks for beliefs.  It deliberately emits a
fully explicit positional certificate: either decreasing ranks and actions,
or one answer witness for every trap-belief/action pair.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


VERTICES = tuple(range(8))
ACTIONS = tuple(itertools.product(VERTICES, repeat=3))
FULL = (1 << 8) - 1


def popcount(mask: int) -> int:
    return mask.bit_count()


def legal_answers(probe: int, robber: int) -> tuple[int, ...]:
    if probe == robber:
        return (probe,)
    return tuple(probe ^ (1 << j) for j in range(3) if ((probe ^ robber) >> j) & 1)


def closed_neighborhood(mask: int) -> int:
    result = mask
    for vertex in VERTICES:
        if mask & (1 << vertex):
            for j in range(3):
                result |= 1 << (vertex ^ (1 << j))
    return result


CLOSURE = tuple(closed_neighborhood(mask) for mask in range(1 << 8))


def action_profile(action: tuple[int, int, int]) -> tuple[tuple[tuple[int, int, int], int], ...]:
    """Return (public answer tuple, supporting robber-position mask)."""
    supports: dict[tuple[int, int, int], int] = {}
    for robber in VERTICES:
        choices = [legal_answers(probe, robber) for probe in action]
        for answer in itertools.product(*choices):
            supports[answer] = supports.get(answer, 0) | (1 << robber)
    return tuple(sorted(supports.items()))


def synthesize() -> tuple[dict[int, int], dict[int, tuple[int, int, int]], list[tuple[tuple[tuple[int, int, int], int], ...]]]:
    profiles = [action_profile(action) for action in ACTIONS]

    # W_k is the set of beliefs localizable within k further probe rounds.
    ranks: dict[int, int] = {1 << vertex: 0 for vertex in VERTICES}
    strategy: dict[int, tuple[int, int, int]] = {}
    frontier_rank = 0

    while True:
        known = set(ranks)
        additions: dict[int, tuple[int, int, int]] = {}
        for belief in range(1, FULL + 1):
            if belief in known:
                continue
            for action_index, action in enumerate(ACTIONS):
                good = True
                for _answer, support in profiles[action_index]:
                    fiber = belief & support
                    if fiber == 0 or popcount(fiber) == 1:
                        continue
                    if CLOSURE[fiber] not in known:
                        good = False
                        break
                if good:
                    additions[belief] = action
                    break
        if not additions:
            break
        frontier_rank += 1
        for belief, action in additions.items():
            ranks[belief] = frontier_rank
            strategy[belief] = action

    return ranks, strategy, profiles


def choose_trap_witness(
    belief: int,
    profile: tuple[tuple[tuple[int, int, int], int], ...],
    losing: set[int],
) -> tuple[int, int, int]:
    for answer, support in profile:
        fiber = belief & support
        if popcount(fiber) >= 2 and CLOSURE[fiber] in losing:
            return answer
    raise AssertionError(f"no trap witness for belief {belief}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=Path("evidence/q3_certificate.json"))
    parser.add_argument("--report", type=Path, default=Path("evidence/solver_report.json"))
    args = parser.parse_args()

    ranks, strategy, profiles = synthesize()
    winning = set(ranks)
    losing = set(range(1, FULL + 1)) - winning

    strategy_rows = []
    for belief in sorted(winning):
        row: dict[str, object] = {"belief": belief, "rank": ranks[belief]}
        if belief in strategy:
            row["probes"] = list(strategy[belief])
        strategy_rows.append(row)

    certificate: dict[str, object] = {
        "schema": "q3-directional-localization-certificate-v1",
        "vertex_encoding": "integers 0..7, with Q_3 adjacency x xor 2^j",
        "belief_encoding": "nonzero 8-bit mask; bit r means robber position r is possible",
        "probe_count": 3,
        "all_nonempty_beliefs_count": FULL,
        "all_ordered_probe_actions_count": len(ACTIONS),
        "initial_belief": FULL,
        "winning_beliefs_count": len(winning),
        "losing_beliefs_count": len(losing),
        "strategy": strategy_rows,
    }

    if FULL in winning:
        certificate["result"] = "three_cops_win"
        certificate["initial_rank"] = ranks[FULL]
        certificate["trap_beliefs"] = []
        certificate["trap_witnesses"] = []
    else:
        certificate["result"] = "three_cops_do_not_win"
        certificate["initial_rank"] = None
        certificate["trap_beliefs"] = sorted(losing)
        witness_rows = []
        for belief in sorted(losing):
            answers = [list(choose_trap_witness(belief, profile, losing)) for profile in profiles]
            witness_rows.append({"belief": belief, "answers_in_action_order": answers})
        certificate["trap_witnesses"] = witness_rows

    args.certificate.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(certificate, indent=2, sort_keys=True) + "\n").encode("utf-8")
    args.certificate.write_bytes(encoded)
    digest = hashlib.sha256(encoded).hexdigest()

    report = {
        "solver": "exact integer bit-mask retrograde fixed point",
        "certificate": str(args.certificate),
        "certificate_sha256": digest,
        "result": certificate["result"],
        "initial_belief": FULL,
        "initial_rank": certificate["initial_rank"],
        "winning_beliefs_count": len(winning),
        "losing_beliefs_count": len(losing),
        "beliefs_enumerated": FULL,
        "ordered_probe_actions_enumerated": len(ACTIONS),
        "fixed_point_partition_complete": len(winning | losing) == FULL and not (winning & losing),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
