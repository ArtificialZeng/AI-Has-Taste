#!/usr/bin/env python3
"""Cross-check PRINT_ALL output from the C plugin by direct subset counting."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess


LINE = re.compile(
    r"^SEQUENCE n=(\d+) parent=([0-9,]+) coefficients=([0-9,]+)$"
)


def direct_coefficients(n: int, parent: list[int]) -> list[int]:
    edge_masks = [
        (1 << (vertex - 1)) | (1 << (parent[vertex - 1] - 1))
        for vertex in range(2, n + 1)
    ]
    result = [0] * (n + 1)
    for mask in range(1 << n):
        if all(mask & edge_mask != edge_mask for edge_mask in edge_masks):
            result[mask.bit_count()] += 1
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("binary", type=pathlib.Path)
    parser.add_argument("--max-n", type=int, default=11)
    args = parser.parse_args()
    if not 1 <= args.max_n <= 11:
        raise SystemExit("--max-n must be in [1,11]")

    process = subprocess.run(
        [str(args.binary), "-q", f"1:{args.max_n}"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    checked = 0
    by_order: dict[int, int] = {}
    for raw_line in process.stdout.splitlines():
        match = LINE.fullmatch(raw_line)
        if match is None:
            if raw_line.startswith("NONLOGCONCAVE "):
                continue
            raise AssertionError(f"unparsed checker line: {raw_line!r}")
        n = int(match.group(1))
        parent = [int(value) for value in match.group(2).split(",")]
        coefficients = [int(value) for value in match.group(3).split(",")]
        if len(parent) != n or parent[0] != 0:
            raise AssertionError(("bad serialized parent array", raw_line))
        direct = direct_coefficients(n, parent)
        if coefficients != direct:
            raise AssertionError((n, parent, coefficients, direct))
        checked += 1
        by_order[n] = by_order.get(n, 0) + 1

    expected = [1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235]
    for n in range(1, args.max_n + 1):
        if by_order.get(n) != expected[n - 1]:
            raise AssertionError(("tree count mismatch", n, by_order.get(n)))

    code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "method": "direct subset enumeration from every serialized parent array",
        "max_order": args.max_n,
        "trees": checked,
        "by_order": by_order,
        "c_summary": process.stderr.strip(),
        "code_sha256": code_hash,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
