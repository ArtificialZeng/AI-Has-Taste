#!/usr/bin/env python3
"""Independent labelled-cop checker for attractor_certificate.json.

This file does not import the exporter.  It enumerates ordered cop tuples and
ordered cop moves, while the certificate uses sorted multisets.  The checks
therefore also validate that the multiset certificate lifts to labelled cops.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


N = 16
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "attractor_certificate.json"
TRIAGE_PATH = HERE / "triage_attractor.json"


def adjacent_or_equal(u: int, v: int) -> bool:
    ux, uy = divmod(u, 4)
    vx, vy = divmod(v, 4)
    return (u == v or
            (uy == vy and (ux - vx) % 4 in (1, 3)) or
            (ux == vx and (uy - vy) % 4 in (1, 3)))


def ordered_steps(v: int) -> tuple[int, ...]:
    return tuple(w for w in range(N) if adjacent_or_equal(v, w))


def edge_list() -> tuple[tuple[int, int], ...]:
    return tuple((u, v) for u in range(N) for v in range(u + 1, N)
                 if adjacent_or_equal(u, v))


def graph_digest(edges: tuple[tuple[int, int], ...]) -> str:
    payload = json.dumps(
        {"vertices": tuple(range(N)), "edges": edges}, separators=(",", ":")
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def reachable(start: int, blocked: frozenset[int]) -> frozenset[int]:
    seen = {start}
    stack = [start]
    while stack:
        u = stack.pop()
        for v in range(N):
            if v not in blocked and v not in seen and adjacent_or_equal(u, v) and u != v:
                seen.add(v)
                stack.append(v)
    return frozenset(seen)


def matching_move(source: tuple[int, ...], target_sorted: tuple[int, ...]):
    for target in set(itertools.permutations(target_sorted)):
        if all(adjacent_or_equal(u, v) for u, v in zip(source, target)):
            return target
    return None


def main() -> None:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    triage = json.loads(TRIAGE_PATH.read_text(encoding="utf-8"))
    edges = edge_list()
    digest = graph_digest(edges)
    assert digest == cert["graph"]["sha256"] == triage["graph_sha256"]
    assert [list(e) for e in edges] == cert["graph"]["edges"]

    configs4 = tuple(itertools.combinations_with_replacement(range(N), 4))
    index4 = {c: i for i, c in enumerate(configs4)}
    ranks = cert["four_cops"]["rank_by_config_then_robber"]
    moves = cert["four_cops"]["move_config_index_by_config_then_robber"]
    assert len(ranks) == len(moves) == len(configs4) * N
    rank_histogram_canonical: dict[int, int] = {}
    for cindex, cops in enumerate(configs4):
        for robber in range(N):
            at = N * cindex + robber
            if robber in cops:
                assert ranks[at] == moves[at] == -1
                continue
            rank = ranks[at]
            assert 1 <= rank <= cert["four_cops"]["attractor_rounds"]
            rank_histogram_canonical[rank] = rank_histogram_canonical.get(rank, 0) + 1
            target = configs4[moves[at]]
            assert matching_move(cops, target) is not None
            if robber not in target:
                for reply in reachable(robber, frozenset(target)):
                    reply_rank = ranks[N * index4[target] + reply]
                    assert 1 <= reply_rank < rank
    assert {str(k): v for k, v in sorted(rank_histogram_canonical.items())} == cert["four_cops"]["rank_histogram"]

    labelled4_legal = 0
    labelled4_rank_histogram: dict[int, int] = {}
    labelled_move_cache = {}
    for labelled_cops in itertools.product(range(N), repeat=4):
        cindex = index4[tuple(sorted(labelled_cops))]
        for robber in range(N):
            if robber in labelled_cops:
                continue
            labelled4_legal += 1
            at = N * cindex + robber
            rank = ranks[at]
            labelled4_rank_histogram[rank] = labelled4_rank_histogram.get(rank, 0) + 1
            key = (labelled_cops, moves[at])
            if key not in labelled_move_cache:
                labelled_move_cache[key] = matching_move(labelled_cops, configs4[moves[at]])
            assert labelled_move_cache[key] is not None

    configs3 = tuple(itertools.combinations_with_replacement(range(N), 3))
    index3 = {c: i for i, c in enumerate(configs3)}
    losing_masks = cert["three_cops"]["losing_mask_by_configuration"]
    response_lookup = {
        (source, robber): {destination: reply for destination, reply in responses}
        for source, robber, responses in cert["three_cops"]["response_records"]
    }
    assert len(response_lookup) == cert["three_cops"]["losing_states"]
    # Every initial multiset has at least one certified safe robber start.
    assert all(mask != 0 for mask in losing_masks)

    labelled3_legal = 0
    labelled3_losing = 0
    checked_labelled3_moves = 0
    for labelled_cops in itertools.product(range(N), repeat=3):
        source_index = index3[tuple(sorted(labelled_cops))]
        for robber in range(N):
            if robber in labelled_cops:
                continue
            labelled3_legal += 1
            if not (losing_masks[source_index] >> robber & 1):
                continue
            labelled3_losing += 1
            responses = response_lookup[(source_index, robber)]
            for labelled_target in itertools.product(*(ordered_steps(v) for v in labelled_cops)):
                checked_labelled3_moves += 1
                assert robber not in labelled_target
                target = tuple(sorted(labelled_target))
                target_index = index3[target]
                reply = responses[target_index]
                assert reply in reachable(robber, frozenset(target))
                assert losing_masks[target_index] >> reply & 1

    triage4 = next(item for item in triage["results"] if item["cop_count"] == 4)
    triage3 = next(item for item in triage["results"] if item["cop_count"] == 3)
    assert len(configs4) == cert["four_cops"]["configurations"] == triage4["configurations"]
    assert sum(rank_histogram_canonical.values()) == cert["four_cops"]["legal_states"] == triage4["legal_cop_turn_states"]
    assert sum(1 for c in configs3 for r in range(N) if r not in c) == cert["three_cops"]["legal_states"] == triage3["legal_cop_turn_states"]
    assert cert["three_cops"]["winning_states"] == triage3["winning_cop_turn_states"]
    assert cert["three_cops"]["winning_states"] + cert["three_cops"]["losing_states"] == cert["three_cops"]["legal_states"]

    certificate_sha256 = hashlib.sha256(CERT_PATH.read_bytes()).hexdigest()
    output = {
        "status": "pass",
        "checker_model": "ordered labelled cop tuples and ordered simultaneous moves",
        "graph_sha256": digest,
        "certificate_sha256": certificate_sha256,
        "four_cops": {
            "canonical_configurations": len(configs4),
            "canonical_legal_states": sum(rank_histogram_canonical.values()),
            "canonical_rank_histogram": {str(k): v for k, v in sorted(rank_histogram_canonical.items())},
            "labelled_configurations": N ** 4,
            "labelled_legal_states": labelled4_legal,
            "labelled_rank_histogram": {str(k): v for k, v in sorted(labelled4_rank_histogram.items())},
            "verified_policy_entries": sum(rank_histogram_canonical.values()),
        },
        "three_cops": {
            "canonical_configurations": len(configs3),
            "canonical_legal_states": cert["three_cops"]["legal_states"],
            "canonical_losing_states": cert["three_cops"]["losing_states"],
            "labelled_configurations": N ** 3,
            "labelled_legal_states": labelled3_legal,
            "labelled_losing_states": labelled3_losing,
            "verified_labelled_cop_moves_from_losing_states": checked_labelled3_moves,
        },
        "comparisons": {
            "triage_graph_digest": "equal",
            "triage_canonical_state_counts": "equal",
            "four_policy_strict_rank_descent": "verified",
            "three_robber_region_closed_under_every_labelled_cop_move": "verified",
            "every_three_cop_initial_placement_has_safe_robber_start": "verified",
        },
    }
    out_path = HERE / "labelled_checker_report.json"
    out_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
