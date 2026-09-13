#!/usr/bin/env python3
"""Enumerate all PLEs of B_3 and emit exact set-cover models.

Elements of B_3 are encoded by integers 0,...,7, whose three binary bits
are their characteristic vectors.  A PLE is serialized as an ordered list
of these integers.  The enumeration loops over every nonempty induced
ground set and recursively chooses all currently minimal elements, so each
linear extension occurs exactly once.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


ELEMENTS = tuple(range(8))


def strict_below(a: int, b: int) -> bool:
    return a != b and (a & b) == a


def enumerate_orders(mask: int, prefix: tuple[int, ...] = ()):
    if mask == 0:
        yield prefix
        return
    for x in ELEMENTS:
        if not (mask >> x) & 1:
            continue
        if any((mask >> y) & 1 and strict_below(y, x) for y in ELEMENTS):
            continue
        yield from enumerate_orders(mask ^ (1 << x), prefix + (x,))


def enumerate_ples() -> list[tuple[int, ...]]:
    return [order for mask in range(1, 1 << 8) for order in enumerate_orders(mask)]


def requirements():
    reqs: list[tuple] = [("element", x) for x in ELEMENTS]
    for a in ELEMENTS:
        for b in range(a + 1, 8):
            if strict_below(a, b) or strict_below(b, a):
                reqs.append(("comparable", a, b))
            else:
                reqs.append(("orientation", a, b))
                reqs.append(("orientation", b, a))
    return reqs


def covered(order: tuple[int, ...], req: tuple) -> bool:
    positions = {x: i for i, x in enumerate(order)}
    if req[0] == "element":
        return req[1] in positions
    if req[0] == "comparable":
        return req[1] in positions and req[2] in positions
    return req[1] in positions and req[2] in positions and positions[req[1]] < positions[req[2]]


def payload():
    ples = enumerate_ples()
    reqs = requirements()
    covers = [[i for i, p in enumerate(ples) if covered(p, r)] for r in reqs]
    return ples, reqs, covers


def write_lp(path: Path, integer: bool) -> None:
    ples, reqs, covers = payload()
    lines = ["minimize", " obj: " + " + ".join(f"{len(p)} x{i}" for i, p in enumerate(ples)), "subject to"]
    for j, indices in enumerate(covers):
        lines.append(f" r{j}: " + " + ".join(f"x{i}" for i in indices) + " >= 1")
    if integer:
        lines.append("binary")
        lines.extend(" " + " ".join(f"x{i}" for i in range(k, min(k + 20, len(ples)))) for k in range(0, len(ples), 20))
    else:
        lines.append("bounds")
        lines.extend(f" 0 <= x{i}" for i in range(len(ples)))
    lines.append("end")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    parser.add_argument("--lp", type=Path)
    parser.add_argument("--mip", type=Path)
    args = parser.parse_args()
    ples, reqs, covers = payload()
    if args.lp:
        write_lp(args.lp, False)
    if args.mip:
        write_lp(args.mip, True)
    if args.json:
        data = {
            "encoding": "B_3 elements are integers 0..7 interpreted as 3-bit characteristic vectors",
            "enumeration_method": "for each nonempty mask, recursively append every currently minimal remaining element",
            "ple_count": len(ples),
            "counts_by_size": dict(sorted(Counter(map(len, ples)).items())),
            "requirement_count": len(reqs),
            "requirements": [list(r) for r in reqs],
            "ples": [list(p) for p in ples],
            "cover_indices": covers,
        }
        raw = json.dumps(data, sort_keys=True, separators=(",", ":")) + "\n"
        args.json.write_text(raw, encoding="utf-8")
        print(hashlib.sha256(raw.encode()).hexdigest(), args.json)
    print(json.dumps({"ple_count": len(ples), "counts_by_size": dict(Counter(map(len, ples))), "requirements": len(reqs)}, sort_keys=True))


if __name__ == "__main__":
    main()
