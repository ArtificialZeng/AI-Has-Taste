#!/usr/bin/env python3
"""Export exact upper- and lower-bound certificates for C4 square C4.

The certificate uses sorted cop multisets.  Four-cop entries give an attractor
rank and a selected cop move for every legal start-of-cop-turn state.  Three-cop
entries give, for every state in a closed robber region and every distinct
sorted cop move, a legal robber response that remains in that region.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


N = 16
ALL = (1 << N) - 1
VERTICES = tuple(range(N))
EDGES = tuple(
    sorted(
        {
            tuple(sorted((4 * x + y, 4 * ((x + dx) % 4) + (y + dy) % 4)))
            for x in range(4)
            for y in range(4)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
        }
    )
)
STEP = tuple(
    tuple(sorted({v} | {w if v == u else u for u, w in EDGES if v in (u, w)}))
    for v in VERTICES
)
GRAPH_SHA256 = hashlib.sha256(
    json.dumps({"vertices": VERTICES, "edges": EDGES}, separators=(",", ":")).encode()
).hexdigest()


def components(blocked: int) -> tuple[int, ...]:
    answer = [0] * N
    unseen = ALL ^ blocked
    while unseen:
        frontier = unseen & -unseen
        component = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            unseen ^= bit
            component |= bit
            v = bit.bit_length() - 1
            for w in STEP[v][1:] if STEP[v][0] == v else STEP[v]:
                wbit = 1 << w
                if unseen & wbit:
                    frontier |= wbit
        for v in VERTICES:
            if component >> v & 1:
                answer[v] = component
    return tuple(answer)


def game_data(k: int):
    configs = tuple(itertools.combinations_with_replacement(VERTICES, k))
    config_index = {c: i for i, c in enumerate(configs)}
    occupied = tuple(sum(1 << v for v in set(c)) for c in configs)
    component = tuple(components(mask) for mask in occupied)
    successors = []
    for c in configs:
        next_configs = {
            tuple(sorted(move)) for move in itertools.product(*(STEP[v] for v in c))
        }
        successors.append(tuple(sorted(config_index[d] for d in next_configs)))
    return configs, occupied, component, tuple(successors)


def attractor(k: int):
    configs, occupied, component, successors = game_data(k)
    winning = [0] * len(configs)
    ranks = [[-1 if occupied[i] >> r & 1 else 0 for r in VERTICES]
             for i in range(len(configs))]
    moves = [[-1] * N for _ in configs]
    round_number = 0
    while True:
        round_number += 1
        added = 0
        old = tuple(winning)
        for i in range(len(configs)):
            for r in VERTICES:
                bit = 1 << r
                if occupied[i] & bit or old[i] & bit:
                    continue
                for j in successors[i]:
                    if occupied[j] & bit:
                        winning[i] |= bit
                        ranks[i][r] = round_number
                        moves[i][r] = j
                        added += 1
                        break
                    reach = component[j][r]
                    if reach & ~old[j] == 0:
                        winning[i] |= bit
                        ranks[i][r] = round_number
                        moves[i][r] = j
                        added += 1
                        break
        if added == 0:
            return configs, occupied, component, successors, tuple(winning), ranks, moves, round_number - 1


def main() -> None:
    configs4, occupied4, _, successors4, winning4, ranks4, moves4, rounds4 = attractor(4)
    if any((ALL ^ occupied4[i]) & ~winning4[i] for i in range(len(configs4))):
        raise RuntimeError("four-cop attractor is not all legal states")

    configs3, occupied3, component3, successors3, winning3, _, _, rounds3 = attractor(3)
    losing3 = tuple((ALL ^ occupied3[i]) & ~winning3[i] for i in range(len(configs3)))
    response_records = []
    for i, losing_mask in enumerate(losing3):
        for r in VERTICES:
            if not (losing_mask >> r & 1):
                continue
            responses = []
            for j in successors3[i]:
                if occupied3[j] >> r & 1:
                    raise RuntimeError("a losing state admits immediate capture")
                candidates = component3[j][r] & losing3[j]
                if candidates == 0:
                    raise RuntimeError("three-cop losing region is not closed")
                reply = (candidates & -candidates).bit_length() - 1
                responses.append([j, reply])
            response_records.append([i, r, responses])

    rank_histogram = {
        str(rank): sum(row.count(rank) for row in ranks4)
        for rank in range(1, rounds4 + 1)
    }
    report = {
        "schema": "c4xc4-fast-robber-certificate-v1",
        "convention": {
            "vertex_encoding": "(x,y) maps to 4*x+y, x,y in {0,1,2,3}",
            "configuration_order": "lexicographic combinations_with_replacement(range(16),k)",
            "flat_array_order": "configuration index first, then robber vertex 0..15",
            "illegal_state_sentinel": -1,
            "capture_timing": "after simultaneous cop step and before robber response",
        },
        "graph": {
            "vertices": list(VERTICES),
            "edges": [list(edge) for edge in EDGES],
            "sha256": GRAPH_SHA256,
        },
        "four_cops": {
            "configurations": len(configs4),
            "legal_states": sum(N - len(set(c)) for c in configs4),
            "distinct_configuration_transitions": sum(map(len, successors4)),
            "attractor_rounds": rounds4,
            "rank_histogram": rank_histogram,
            "rank_by_config_then_robber": [x for row in ranks4 for x in row],
            "move_config_index_by_config_then_robber": [x for row in moves4 for x in row],
        },
        "three_cops": {
            "configurations": len(configs3),
            "legal_states": sum(N - len(set(c)) for c in configs3),
            "winning_states": sum(mask.bit_count() for mask in winning3),
            "losing_states": sum(mask.bit_count() for mask in losing3),
            "attractor_rounds": rounds3,
            "losing_mask_by_configuration": list(losing3),
            "response_record_format": "[source_config_index, robber, [[destination_config_index, response],...]]",
            "response_records": response_records,
        },
    }
    output = Path(__file__).with_name("attractor_certificate.json")
    output.write_text(json.dumps(report, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "bytes": output.stat().st_size,
        "graph_sha256": GRAPH_SHA256,
        "four_rank_histogram": rank_histogram,
        "three_losing_states": report["three_cops"]["losing_states"],
        "three_response_records": len(response_records),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
