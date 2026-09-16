#!/usr/bin/env python3
"""Unpruned exact-mask Bellman solver for win-00049-p02.

This is a direct executable rendering of the recurrence in problem.md.  Every
legal guess is evaluated at every nonempty memoized state; there is no symmetry
quotient, dominance pruning, branch-and-bound cutoff, or floating-point step.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
import time
from pathlib import Path


def universe():
    ans = []
    for p in itertools.permutations(range(3)):
        for colors in range(8):
            code = "".join(str(v + 1) for v in p) + "-" + "".join(
                str((colors >> v) & 1) for v in range(3)
            )
            ans.append((p, colors, code))
    assert len(ans) == 48
    return ans


ITEMS = universe()
FULL = (1 << 48) - 1


def feedback(g, x):
    gp, gc, _ = g
    xp, xc, _ = x
    u = 0
    for i, value in enumerate(gp):
        if value == xp[i] and ((gc >> value) & 1) == ((xc >> value) & 1):
            u |= 1 << i
    return u


FEEDBACK_MASKS = []
FEEDBACK_TABLE = []
for g, guess in enumerate(ITEMS):
    masks = [0] * 8
    row = []
    for x, secret in enumerate(ITEMS):
        u = feedback(guess, secret)
        row.append(u)
        masks[u] |= 1 << x
    assert sum(mask.bit_count() for mask in masks) == 48
    assert (masks[0] | masks[1] | masks[2] | masks[3] |
            masks[4] | masks[5] | masks[6] | masks[7]) == FULL
    assert masks[7] == 1 << g
    FEEDBACK_MASKS.append(tuple(masks))
    FEEDBACK_TABLE.append(tuple(row))
FEEDBACK_MASKS = tuple(FEEDBACK_MASKS)
FEEDBACK_TABLE = tuple(FEEDBACK_TABLE)


# MEMO[r][mask] = (value, least-index optimal action).
MEMO = [{} for _ in range(7)]
ACTION_EVALUATIONS = [0] * 7


def solve(a: int, r: int) -> int:
    if not a or not r:
        return 0
    table = MEMO[r]
    old = table.get(a)
    if old is not None:
        return old[0]

    best = -1
    best_g = -1
    lower = r - 1
    for g, masks in enumerate(FEEDBACK_MASKS):
        ACTION_EVALUATIONS[r] += 1
        score = (a >> g) & 1
        # u=7 is solved immediately and is therefore not recursed on.
        score += solve(a & masks[0], lower)
        score += solve(a & masks[1], lower)
        score += solve(a & masks[2], lower)
        score += solve(a & masks[3], lower)
        score += solve(a & masks[4], lower)
        score += solve(a & masks[5], lower)
        score += solve(a & masks[6], lower)
        if score > best:
            best, best_g = score, g
    table[a] = (best, best_g)
    return best


def hex_mask(mask):
    return f"{mask:012x}"


def write_static_tables(out_dir: Path):
    with (out_dir / "items.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["index", "code", "permutation", "colors_by_value"])
        for i, (p, colors, code) in enumerate(ITEMS):
            w.writerow([i, code, "".join(str(v + 1) for v in p),
                        "".join(str((colors >> v) & 1) for v in range(3))])

    with (out_dir / "feedback.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["guess_index", "guess_code", "secret_index", "secret_code",
                    "feedback_mask", "feedback_set"])
        for g, guess in enumerate(ITEMS):
            for x, secret in enumerate(ITEMS):
                u = FEEDBACK_TABLE[g][x]
                feedback_set = "{" + " ".join(str(i + 1) for i in range(3)
                                                  if (u >> i) & 1) + "}"
                w.writerow([g, guess[2], x, secret[2], u, feedback_set])


def write_results(out_dir: Path, values, elapsed):
    with (out_dir / "root-decompositions.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["horizon", "value", "action_index", "action_code",
                    "feedback_mask", "cell_mask", "cell_size", "child_value"])
        for r in range(1, len(values)):
            value, g = MEMO[r][FULL]
            for u in range(8):
                child = FULL & FEEDBACK_MASKS[g][u]
                child_value = child.bit_count() if u == 7 else solve(child, r - 1)
                w.writerow([r, value, g, ITEMS[g][2], u, hex_mask(child),
                            child.bit_count(), child_value])

    with (out_dir / "states.csv").open("w", newline="") as f:
        w = csv.writer(f)
        header = ["horizon", "state_mask", "state_size", "value",
                  "action_index", "action_code"]
        for u in range(8):
            header += [f"cell{u}_mask", f"cell{u}_size"]
        w.writerow(header)
        for r in range(1, len(values)):
            for a, (value, g) in sorted(MEMO[r].items()):
                row = [r, hex_mask(a), a.bit_count(), value, g, ITEMS[g][2]]
                for u in range(8):
                    child = a & FEEDBACK_MASKS[g][u]
                    row += [hex_mask(child), child.bit_count()]
                w.writerow(row)

    summary = {
        "method": "exact integer masks; all 48 guesses at every memoized state; no pruning or symmetry quotient",
        "bellman_values": values[1:],
        "circular_shift_benchmark": [1, 8, 24, 40, 47, 48],
        "elapsed_seconds": elapsed,
        "horizons": [],
    }
    for r in range(1, len(values)):
        value, g = MEMO[r][FULL]
        summary["horizons"].append({
            "horizon": r,
            "states": len(MEMO[r]),
            "actions_evaluated": ACTION_EVALUATIONS[r],
            "root_action_index": g,
            "root_action_code": ITEMS[g][2],
            "value": value,
        })
    (out_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("evidence/bellman-output"))
    parser.add_argument("--max-horizon", type=int, default=6, choices=range(1, 7))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    write_static_tables(args.output)

    start = time.monotonic()
    values = [0]
    for r in range(1, args.max_horizon + 1):
        value = solve(FULL, r)
        values.append(value)
        entry = MEMO[r][FULL]
        print(json.dumps({
            "horizon": r, "value": value, "states": len(MEMO[r]),
            "actions_evaluated": ACTION_EVALUATIONS[r],
            "root_action": [entry[1], ITEMS[entry[1]][2]],
            "elapsed_seconds": time.monotonic() - start,
        }), flush=True)

    elapsed = time.monotonic() - start
    write_results(args.output, values, elapsed)


if __name__ == "__main__":
    main()
