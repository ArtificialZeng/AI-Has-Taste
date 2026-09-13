#!/usr/bin/env python3
"""Finite exact mex scan for triage; it is evidence, not an all-c proof."""

from argparse import ArgumentParser


def grundy(c: int, length: int) -> list[int]:
    values: list[int] = []
    for n in range(length):
        options = {values[n - s] for s in (2, 5, c) if s <= n}
        g = 0
        while g in options:
            g += 1
        values.append(g)
    return values


def is_period(values: list[int], p: int) -> bool:
    return all(values[n] == values[n + p] for n in range(len(values) - p))


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--max-c", type=int, default=99)
    parser.add_argument("--length", type=int, default=20_000)
    args = parser.parse_args()
    print("c\trho\tcandidate_periods_passing\tleast_period_up_to_c+5")
    for c in range(6, args.max_c + 1):
        if c == 7:
            continue
        values = grundy(c, args.length)
        candidates = [p for p in (7, c + 2, c + 5) if is_period(values, p)]
        tested = [p for p in range(1, c + 6) if is_period(values, p)]
        least = tested[0] if tested else "-"
        passed = ",".join(map(str, candidates)) or "-"
        print(f"{c}\t{c % 7}\t{passed}\t{least}")


if __name__ == "__main__":
    main()

