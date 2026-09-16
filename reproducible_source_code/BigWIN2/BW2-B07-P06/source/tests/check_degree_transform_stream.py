#!/usr/bin/env python3
"""Exhaustively check the degree transform on a graph6 stream."""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

from test_degree_transform import lhs, rhs


def main() -> None:
    count = 0
    for line in sys.stdin.buffer:
        if not line.strip() or line.startswith(b">>"):
            continue
        graph6 = line.strip()
        if lhs(graph6) != rhs(graph6):
            raise AssertionError(graph6)
        count += 1
    print(f"PASS exhaustive degree-transform stream: {count} graphs")


if __name__ == "__main__":
    main()
