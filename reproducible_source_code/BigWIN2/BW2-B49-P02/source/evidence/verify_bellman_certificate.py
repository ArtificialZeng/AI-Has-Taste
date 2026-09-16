#!/usr/bin/env python3
"""Independent replay checker for the Bellman certificate.

This program does not import bellman_exact.py.  It reconstructs the canonical
universe and feedback partitions, validates the serialized 48-by-48 table, and
then checks every certificate state against every one of the 48 possible
actions.  Thus the checked maximum is an upper bound as well as an attained
value; checking only each row's retained action would establish attainment but
would not establish optimality.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from pathlib import Path


def canonical_items():
    rows = []
    for p in itertools.permutations((1, 2, 3)):
        # The certificate index orders the three-bit little-endian color mask
        # numerically (0,...,7); the displayed word remains c(1)c(2)c(3).
        for color_mask in range(8):
            c = tuple((color_mask >> v) & 1 for v in range(3))
            rows.append((p, c, "".join(map(str, p)) + "-" + "".join(map(str, c))))
    return rows


def response(guess, secret):
    gp, gc, _ = guess
    sp, sc, _ = secret
    ans = 0
    for pos in range(3):
        value = gp[pos]
        # Colors are indexed by value, while gp/sp are one-based values.
        if value == sp[pos] and gc[value - 1] == sc[value - 1]:
            ans |= 1 << pos
    return ans


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while block := f.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path, nargs="?",
                    default=Path("evidence/bellman-output"))
    args = ap.parse_args()
    cert = args.certificate
    expected = canonical_items()
    full = (1 << 48) - 1

    with (cert / "items.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 48
    for i, row in enumerate(rows):
        p, c, code = expected[i]
        assert int(row["index"]) == i
        assert row["code"] == code
        assert row["permutation"] == "".join(map(str, p))
        assert row["colors_by_value"] == "".join(map(str, c))

    table = [[None] * 48 for _ in range(48)]
    seen_pairs = set()
    with (cert / "feedback.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            g, x, u = int(row["guess_index"]), int(row["secret_index"]), int(row["feedback_mask"])
            assert 0 <= g < 48 and 0 <= x < 48 and 0 <= u < 8
            assert (g, x) not in seen_pairs
            seen_pairs.add((g, x))
            assert row["guess_code"] == expected[g][2]
            assert row["secret_code"] == expected[x][2]
            assert u == response(expected[g], expected[x])
            wanted_set = "{" + " ".join(str(i + 1) for i in range(3) if (u >> i) & 1) + "}"
            assert row["feedback_set"] == wanted_set
            table[g][x] = u
    assert len(seen_pairs) == 48 * 48

    partitions = []
    for g in range(48):
        cells = [0] * 8
        for x, u in enumerate(table[g]):
            assert u is not None
            cells[u] |= 1 << x
        assert sum(m.bit_count() for m in cells) == 48
        assert cells[7] == 1 << g
        assert (cells[0] | cells[1] | cells[2] | cells[3] |
                cells[4] | cells[5] | cells[6] | cells[7]) == full
        partitions.append(cells)

    # values[(r, A)] = (claimed value, claimed least optimal action).
    values = {}
    chosen_cells = {}
    with (cert / "states.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            r, a = int(row["horizon"]), int(row["state_mask"], 16)
            value, action = int(row["value"]), int(row["action_index"])
            key = (r, a)
            assert key not in values
            assert 1 <= r <= 6 and 0 < a <= full
            assert int(row["state_size"]) == a.bit_count()
            assert 0 <= value <= a.bit_count()
            assert 0 <= action < 48 and row["action_code"] == expected[action][2]
            cells = []
            for u in range(8):
                child = int(row[f"cell{u}_mask"], 16)
                assert int(row[f"cell{u}_size"]) == child.bit_count()
                assert child == (a & partitions[action][u])
                cells.append(child)
            values[key] = (value, action)
            chosen_cells[key] = cells

    checked_actions = 0
    missing_dependencies = []
    # All dependencies have horizon r-1, so increasing r is a transparent
    # bottom-up replay even though the certificate was discovered top-down.
    for r in range(1, 7):
        for (rr, a), (claimed, chosen) in sorted(values.items()):
            if rr != r:
                continue
            scores = []
            for g in range(48):
                score = (a >> g) & 1
                for u in range(7):
                    child = a & partitions[g][u]
                    if not child or r == 1:
                        child_value = 0
                    else:
                        dependency = values.get((r - 1, child))
                        if dependency is None:
                            missing_dependencies.append((r, f"{a:012x}", g, u,
                                                         f"{child:012x}"))
                            child_value = 0
                        else:
                            child_value = dependency[0]
                    score += child_value
                scores.append(score)
                checked_actions += 1
            assert not missing_dependencies, missing_dependencies[:3]
            maximum = max(scores)
            least_maximizer = scores.index(maximum)
            assert claimed == maximum, (r, f"{a:012x}", claimed, maximum)
            assert chosen == least_maximizer, (r, f"{a:012x}", chosen, least_maximizer)

    roots = [values[(r, full)][0] for r in range(1, 7)]
    assert roots == [1, 8, 24, 40, 47, 48]
    state_counts = [sum(1 for rr, _ in values if rr == r) for r in range(1, 7)]
    assert checked_actions == 48 * len(values)

    report = {
        "status": "verified",
        "canonical_items": 48,
        "feedback_entries_recomputed": 48 * 48,
        "states_replayed": len(values),
        "states_by_horizon": state_counts,
        "actions_replayed": checked_actions,
        "missing_dependencies": 0,
        "root_values": roots,
        "least_root_actions": [values[(r, full)][1] for r in range(1, 7)],
        "sha256": {
            name: digest(cert / name) for name in
            ("items.csv", "feedback.csv", "states.csv", "root-decompositions.csv", "summary.json")
        },
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
