#!/usr/bin/env python3
"""Direct simulation of the intended multicolor CircularShift algorithm.

The displayed color-update cases in Definition 4.3 of arXiv:2408.00903v3
conflict with the immediately preceding prose, Figure 6, and the proof of
Lemma 4.4.  The latter three agree on the operational rule used here: a moved
rank's color is incremented exactly when its clockwise move crosses that
rank's starting position in the identity permutation.  The script first
replays Figure 6 and then exhaustively simulates the frozen n=3,s=2 game.
"""

from __future__ import annotations

import argparse
import csv
import itertools
import json
from collections import Counter
from pathlib import Path


def code(permutation, colors):
    return "".join(map(str, permutation)) + "-" + "".join(map(str, colors))


def feedback(permutation, colors, secret_permutation, secret_colors):
    return tuple(
        i for i in range(len(permutation))
        if permutation[i] == secret_permutation[i]
        and colors[permutation[i] - 1] == secret_colors[secret_permutation[i] - 1]
    )


def clockwise_arc_crosses_rank(old_position, new_position, rank):
    """Whether rank lies in the clockwise arc (old_position,new_position].

    Positions and ranks are one based.  A stationary move occurs precisely
    when only one position remains unmatched; it represents one complete
    circuit and therefore crosses every (in particular, the moved) rank.
    """
    if old_position < new_position:
        return old_position < rank <= new_position
    return old_position < rank or rank <= new_position


def next_guess(permutation, colors, correct_positions):
    n = len(permutation)
    assert len(colors) == n
    # Paper positions a_j are one based; array offsets below are zero based.
    fixed = set(correct_positions)
    a = [i + 1 for i in range(n) if i not in fixed]
    # Unlike the monochrome game, one unmatched position is possible when the
    # rank is correct there but its proposed color is not.
    assert len(a) >= 1

    old = (None,) + tuple(permutation)
    new = list(old)
    for j in range(1, len(a)):
        new[a[j]] = old[a[j - 1]]
    new[a[0]] = old[a[-1]]

    new_colors = list(colors)
    # Every active rank moves from a[j] to a[j+1], cyclically.  The proof of
    # Lemma 4.4 says to increment rank i on a noncyclic move exactly when
    # a[j] < i <= a[j+1], and on the cyclic move exactly when i > a[-1] or
    # i <= a[0].  These are the two cases of the arc test below.
    for j, old_position in enumerate(a):
        new_position = a[(j + 1) % len(a)]
        rank = old[old_position]
        assert new[new_position] == rank
        if clockwise_arc_crosses_rank(old_position, new_position, rank):
            new_colors[rank - 1] += 1
    return tuple(new[1:]), tuple(new_colors)


def simulate(secret_permutation, secret_colors):
    n = len(secret_permutation)
    assert sorted(secret_permutation) == list(range(1, n + 1))
    assert len(secret_colors) == n
    permutation = tuple(range(1, n + 1))
    colors = (0,) * n
    transcript = []
    for round_number in range(1, 1000):
        # No color counter may overshoot the corresponding secret color.
        # In particular, all submitted guesses in the frozen s=2 run are
        # members of its legal 48-element alphabet.
        assert all(0 <= colors[i] <= secret_colors[i] for i in range(n))
        u = feedback(permutation, colors, secret_permutation, secret_colors)
        transcript.append((round_number, permutation, colors, u))
        if len(u) == n:
            assert permutation == secret_permutation and colors == secret_colors
            return transcript
        permutation, colors = next_guess(permutation, colors, u)
    raise AssertionError("CircularShift did not terminate")


def verify_primary_figure_6():
    """Replay the six rows of the explicit n=5 two-color example."""
    secret_permutation = (3, 2, 5, 1, 4)
    secret_colors = (1, 1, 0, 0, 1)  # by rank 1,...,5
    wanted = [
        ((1, 2, 3, 4, 5), (0, 0, 0, 0, 0)),
        ((5, 1, 2, 3, 4), (0, 0, 0, 0, 0)),
        ((3, 5, 1, 2, 4), (0, 0, 0, 0, 0)),
        ((3, 2, 5, 1, 4), (0, 1, 0, 0, 0)),
        ((3, 2, 1, 5, 4), (1, 1, 0, 0, 0)),
        ((3, 2, 5, 1, 4), (1, 1, 0, 0, 1)),
    ]
    transcript = simulate(secret_permutation, secret_colors)
    observed = [(p, c) for _, p, c, _ in transcript]
    assert observed == wanted
    assert len(transcript) == 1 + 2 + 3
    return {
        "secret_permutation": "32514",
        "secret_colors_by_rank": "11001",
        "guess_rows": [code(p, c) for p, c in wanted],
        "matched": True,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path,
                    default=Path("evidence/circular-shift-output"))
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    figure_6 = verify_primary_figure_6()

    secrets = []
    for p in itertools.permutations((1, 2, 3)):
        for color_mask in range(8):
            c = tuple((color_mask >> j) & 1 for j in range(3))
            secrets.append((p, c))

    completion = Counter()
    cumulative = []
    transcript_rows = []
    per_secret = []
    for secret_index, (p, c) in enumerate(secrets):
        transcript = simulate(p, c)
        rounds = len(transcript)
        formula = 1 + sum(p[i] > i + 1 for i in range(3)) + sum(c)
        assert rounds == formula
        completion[rounds] += 1
        per_secret.append({
            "secret_index": secret_index,
            "secret_code": code(p, c),
            "rounds": rounds,
            "formula_rounds": formula,
        })
        for round_number, gp, gc, u in transcript:
            transcript_rows.append([
                secret_index, code(p, c), round_number, code(gp, gc),
                sum(1 << i for i in u), "{" + " ".join(str(i + 1) for i in u) + "}",
            ])

    running = 0
    for r in range(1, 7):
        running += completion[r]
        cumulative.append(running)
    exact = [completion[r] for r in range(1, 7)]
    assert exact == [1, 7, 16, 16, 7, 1]
    assert cumulative == [1, 8, 24, 40, 47, 48]

    with (args.output / "transcripts.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["secret_index", "secret_code", "round", "guess_code",
                    "feedback_mask", "feedback_set"])
        w.writerows(transcript_rows)
    with (args.output / "per-secret.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(per_secret[0]))
        w.writeheader()
        w.writerows(per_secret)

    summary = {
        "algorithm": "direct simulation of the intended Kutin--Smithline multicolor CircularShift rule",
        "interpretation": "increment a moved rank exactly when its clockwise move crosses its identity starting position",
        "primary_support": [
            "prose immediately before Definition 4.3",
            "Figure 6",
            "case analysis in the proof of Lemma 4.4",
        ],
        "displayed_definition_discrepancy_disclosed": True,
        "figure_6_replay": figure_6,
        "secrets_simulated": 48,
        "all_submitted_guesses_legal": True,
        "all_completion_times_match_lemma_4_4_formula": True,
        "exact_round_counts": exact,
        "cumulative_counts": cumulative,
        "transcript_rows": len(transcript_rows),
    }
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
