#!/usr/bin/env python3
"""Independent replay checker for the CircularShift transcript certificate.

This file does not import circular_shift_sim.py.  It parses every serialized
guess, recomputes every feedback set, reconstructs each successor from the
operational circuit rule, and checks the published Lemma 4.4 cost formula.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path


def decode(item):
    permutation_word, color_word = item.split("-")
    return tuple(map(int, permutation_word)), tuple(map(int, color_word))


def encode(permutation, colors):
    return "".join(map(str, permutation)) + "-" + "".join(map(str, colors))


def response(guess_permutation, guess_colors, secret_permutation, secret_colors):
    mask = 0
    for pos, rank in enumerate(guess_permutation):
        if (rank == secret_permutation[pos]
                and guess_colors[rank - 1] == secret_colors[rank - 1]):
            mask |= 1 << pos
    return mask


def crosses_home(old_position, new_position, rank):
    # Clockwise means increasing position, with wrap n -> 1.  The endpoint is
    # included and the starting point excluded.  Equality denotes a full lap.
    if old_position < new_position:
        return old_position < rank <= new_position
    return rank > old_position or rank <= new_position


def successor(permutation, colors, feedback_mask):
    n = len(permutation)
    active = [pos for pos in range(1, n + 1)
              if not ((feedback_mask >> (pos - 1)) & 1)]
    assert active

    following = {active[j]: active[(j + 1) % len(active)]
                 for j in range(len(active))}
    new_permutation = list(permutation)
    new_colors = list(colors)
    for old_position in active:
        new_position = following[old_position]
        rank = permutation[old_position - 1]
        new_permutation[new_position - 1] = rank
        if crosses_home(old_position, new_position, rank):
            new_colors[rank - 1] += 1
    return tuple(new_permutation), tuple(new_colors)


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as f:
        while block := f.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate", type=Path, nargs="?",
                    default=Path("evidence/circular-shift-output"))
    args = ap.parse_args()
    cert = args.certificate

    expected_secrets = []
    for permutation in itertools.permutations((1, 2, 3)):
        for color_mask in range(8):
            colors = tuple((color_mask >> rank) & 1 for rank in range(3))
            expected_secrets.append((permutation, colors, encode(permutation, colors)))

    with (cert / "per-secret.csv").open(newline="") as f:
        per_secret_rows = list(csv.DictReader(f))
    assert len(per_secret_rows) == 48

    transcript_groups = defaultdict(list)
    with (cert / "transcripts.csv").open(newline="") as f:
        transcript_rows = list(csv.DictReader(f))
    for row in transcript_rows:
        index = int(row["secret_index"])
        assert 0 <= index < 48
        transcript_groups[index].append(row)

    completion_counts = Counter()
    transitions_checked = 0
    feedback_checked = 0
    for index, (secret_permutation, secret_colors, secret_code) in enumerate(expected_secrets):
        meta = per_secret_rows[index]
        assert int(meta["secret_index"]) == index
        assert meta["secret_code"] == secret_code
        rows = transcript_groups[index]
        assert rows
        assert len(rows) == int(meta["rounds"])
        formula = 1 + sum(value > pos + 1 for pos, value in enumerate(secret_permutation)) \
            + sum(secret_colors)
        assert int(meta["formula_rounds"]) == formula == len(rows)
        completion_counts[len(rows)] += 1

        wanted_permutation = (1, 2, 3)
        wanted_colors = (0, 0, 0)
        for round_index, row in enumerate(rows, 1):
            assert int(row["secret_index"]) == index
            assert row["secret_code"] == secret_code
            assert int(row["round"]) == round_index
            permutation, colors = decode(row["guess_code"])
            assert sorted(permutation) == [1, 2, 3]
            assert all(color in (0, 1) for color in colors)
            assert (permutation, colors) == (wanted_permutation, wanted_colors)

            feedback_mask = response(permutation, colors,
                                     secret_permutation, secret_colors)
            assert int(row["feedback_mask"]) == feedback_mask
            wanted_set = "{" + " ".join(
                str(pos + 1) for pos in range(3) if (feedback_mask >> pos) & 1
            ) + "}"
            assert row["feedback_set"] == wanted_set
            feedback_checked += 1

            solved = feedback_mask == 7
            assert solved == (round_index == len(rows))
            if solved:
                assert (permutation, colors) == (secret_permutation, secret_colors)
            else:
                wanted_permutation, wanted_colors = successor(
                    permutation, colors, feedback_mask
                )
                transitions_checked += 1

    exact_counts = [completion_counts[round_number] for round_number in range(1, 7)]
    assert exact_counts == [1, 7, 16, 16, 7, 1]
    cumulative_counts = list(itertools.accumulate(exact_counts))
    assert cumulative_counts == [1, 8, 24, 40, 47, 48]

    with (cert / "summary.json").open() as f:
        summary = json.load(f)
    assert summary["figure_6_replay"]["matched"] is True
    assert summary["figure_6_replay"]["guess_rows"] == [
        "12345-00000", "51234-00000", "35124-00000",
        "32514-01000", "32154-11000", "32514-11001",
    ]
    figure_secret_permutation = (3, 2, 5, 1, 4)
    figure_secret_colors = (1, 1, 0, 0, 1)
    figure_wanted = ((1, 2, 3, 4, 5), (0, 0, 0, 0, 0))
    for figure_round, item in enumerate(summary["figure_6_replay"]["guess_rows"], 1):
        figure_guess = decode(item)
        assert figure_guess == figure_wanted
        figure_feedback = response(*figure_guess,
                                   figure_secret_permutation, figure_secret_colors)
        if figure_round == 6:
            assert figure_feedback == 31
            assert figure_guess == (figure_secret_permutation, figure_secret_colors)
        else:
            assert figure_feedback != 31
            figure_wanted = successor(*figure_guess, figure_feedback)
    assert summary["secrets_simulated"] == 48
    assert summary["all_submitted_guesses_legal"] is True
    assert summary["all_completion_times_match_lemma_4_4_formula"] is True
    assert summary["exact_round_counts"] == exact_counts
    assert summary["cumulative_counts"] == cumulative_counts
    assert summary["transcript_rows"] == len(transcript_rows)

    report = {
        "status": "verified",
        "implementation_independence": "does not import circular_shift_sim.py",
        "primary_figure_6_rows_replayed": 6,
        "canonical_secrets": 48,
        "transcript_rows_replayed": len(transcript_rows),
        "feedback_entries_recomputed": feedback_checked,
        "transitions_recomputed": transitions_checked,
        "all_guesses_legal": True,
        "all_completion_times_match_lemma_4_4": True,
        "exact_round_counts": exact_counts,
        "cumulative_counts": cumulative_counts,
        "sha256": {
            name: file_hash(cert / name)
            for name in ("per-secret.csv", "transcripts.csv", "summary.json")
        },
    }
    (cert / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
