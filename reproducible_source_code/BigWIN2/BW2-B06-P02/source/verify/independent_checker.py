#!/usr/bin/env python3
"""Independent exact check using cyclic orbits and an integer Hungarian run.

This checker intentionally ignores the stored dual arrays and target order.
It regenerates primitive necklaces by orbit partition, scans the witness with
rolling eight-bit windows, and recomputes the assignment bound from scratch.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CERT = ROOT / "certificates" / "lyndon8_optimum.json"


def die(message: str) -> "None":
    raise SystemExit("FAIL: " + message)


def orbit(word: str) -> set[str]:
    return {word[k:] + word[:k] for k in range(8)}


def necklace_targets() -> list[str]:
    unseen = {format(x, "08b") for x in range(256)}
    answer = []
    while unseen:
        word = min(unseen)
        ring = orbit(word)
        unseen.difference_update(ring)
        if len(ring) == 8:
            answer.append(min(ring))
    return sorted(answer)


def shifted_overlap(left: str, right: str) -> int:
    # Try positive displacements of right rather than comparing suffix sizes.
    for displacement in range(1, 9):
        if left[displacement:] == right[: 8 - displacement]:
            return 8 - displacement
    raise AssertionError("displacement 8 must match the two empty strings")


def hungarian_min(cost: list[list[int]]) -> tuple[int, list[int]]:
    """Exact O(n^3) square assignment algorithm; returns value and row->col."""
    n = len(cost)
    if n == 0 or any(len(row) != n for row in cost):
        die("Hungarian input is not a nonempty square matrix")
    # One-indexed primal-dual implementation. All arithmetic is integer.
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)
    infinity = 10**9
    for row in range(1, n + 1):
        p[0] = row
        minv = [infinity] * (n + 1)
        used = [False] * (n + 1)
        col0 = 0
        while True:
            used[col0] = True
            row0 = p[col0]
            delta = infinity
            col1 = 0
            for col in range(1, n + 1):
                if used[col]:
                    continue
                reduced = cost[row0 - 1][col - 1] - u[row0] - v[col]
                if reduced < minv[col]:
                    minv[col] = reduced
                    way[col] = col0
                if minv[col] < delta:
                    delta = minv[col]
                    col1 = col
            if delta == infinity:
                die("assignment matrix has no augmenting column")
            for col in range(n + 1):
                if used[col]:
                    u[p[col]] += delta
                    v[col] -= delta
                else:
                    minv[col] -= delta
            col0 = col1
            if p[col0] == 0:
                break
        while True:
            col1 = way[col0]
            p[col0] = p[col1]
            col0 = col1
            if col0 == 0:
                break
    assignment = [-1] * n
    for col in range(1, n + 1):
        assignment[p[col] - 1] = col - 1
    if sorted(assignment) != list(range(n)):
        die("Hungarian output is not a permutation")
    value = sum(cost[row][assignment[row]] for row in range(n))
    if value != -v[0]:
        die("Hungarian primal and dual objective disagree")
    return value, assignment


def main() -> None:
    if len(sys.argv) > 2:
        die("usage: independent_checker.py [certificate.json]")
    path = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_CERT
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        die(f"cannot parse certificate: {exc}")
    witness = payload.get("witness")
    endpoint = payload.get("claimed_optimum_length")
    if not isinstance(witness, str) or set(witness) - {"0", "1"} or endpoint != 94:
        die("malformed witness or endpoint")

    targets = necklace_targets()
    if len(targets) != 30:
        die(f"orbit generator returned {len(targets)} targets instead of 30")
    windows = {witness[pos : pos + 8] for pos in range(max(0, len(witness) - 7))}
    if any(target not in windows for target in targets):
        die("rolling-window scan does not cover all necklace targets")

    nodes = targets + ["*"]
    forbidden = 1000
    cost: list[list[int]] = []
    for i, left in enumerate(nodes):
        row = []
        for j, right in enumerate(nodes):
            if i == j:
                row.append(forbidden)
            elif left == "*" or right == "*":
                row.append(0)
            else:
                row.append(-shifted_overlap(left, right))
        cost.append(row)
    minimum, assignment = hungarian_min(cost)
    if any(i == j for i, j in enumerate(assignment)):
        die("computed assignment used a forbidden diagonal")
    maximum_overlap = -minimum
    lower_bound = 30 * 8 - maximum_overlap
    if maximum_overlap != 146 or lower_bound != 94 or len(witness) != lower_bound:
        die("independent assignment lower bound does not meet witness length")

    print(
        "OK independent=orbit+rolling-window+hungarian-int "
        f"targets={len(targets)} assignment_overlap={maximum_overlap} "
        f"lower_bound={lower_bound} witness_length={len(witness)}"
    )
    print(f"certificate_sha256={hashlib.sha256(path.read_bytes()).hexdigest()}")
    print(f"checker_sha256={hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
