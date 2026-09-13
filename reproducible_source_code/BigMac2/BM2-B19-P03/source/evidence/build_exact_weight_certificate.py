#!/usr/bin/env python3
"""Round the discovery LP ray and serialize its nonzero cycle weights.

This is a certificate *builder*, not its verifier.  The verifier deliberately
does not import this module or trust the LP ray/orientation-instance files.
"""

from __future__ import annotations

import argparse
import hashlib
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path


EXPECTED_N = 812
EXPECTED_M = 7308


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("census", type=Path)
    parser.add_argument("ray", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    census_bytes = args.census.read_bytes()
    census_lines = census_bytes.decode("ascii").splitlines()
    if len(census_lines) != EXPECTED_M:
        raise ValueError(f"expected {EXPECTED_M} census rows, got {len(census_lines)}")

    ray_lines = args.ray.read_text(encoding="ascii").splitlines()
    if ray_lines[0] != f"dual_ray_v1 {EXPECTED_N} {EXPECTED_M}":
        raise ValueError("unexpected dual-ray header")
    ray: dict[int, Decimal] = {}
    for line in ray_lines[1:]:
        row_text, value_text = line.split()
        row = int(row_text)
        if row in ray:
            raise ValueError(f"duplicate ray row {row}")
        ray[row] = Decimal(value_text)

    records: list[str] = []
    counts = {14: 0, 15: 0, 16: 0}
    total_weight = 0
    for cycle_index, line in enumerate(census_lines):
        value = ray.get(EXPECTED_N + cycle_index, Decimal(0))
        weight = int(value.to_integral_value(rounding=ROUND_HALF_EVEN))
        if weight < 0:
            raise ValueError(f"negative rounded cycle weight at row {cycle_index}")
        if weight == 0:
            continue
        fields = [int(part) for part in line.split()]
        length, vertices = fields[0], fields[1:]
        if length not in counts or len(vertices) != length:
            raise ValueError(f"malformed census row {cycle_index}")
        records.append("\t".join(map(str, (cycle_index, weight, length, *vertices))))
        counts[length] += 1
        total_weight += weight

    headers = [
        "# exact-cycle-weight-certificate-v1",
        "# construction rounded-nonnegative-cycle-part-of-lp-ray-nearest-integer-ties-to-even",
        f"# census_sha256 {hashlib.sha256(census_bytes).hexdigest()}",
        f"# ray_sha256 {hashlib.sha256(args.ray.read_bytes()).hexdigest()}",
        f"# nonzero_weights {len(records)}",
        f"# support_by_length 14:{counts[14]} 15:{counts[15]} 16:{counts[16]}",
        f"# total_weight {total_weight}",
        "# columns census_index weight length vertex_0 ... vertex_(length-1)",
    ]
    payload = "\n".join((*headers, *records)) + "\n"
    args.output.write_text(payload, encoding="ascii")
    print(
        f"wrote {args.output}: support={len(records)}, "
        f"counts={counts}, total_weight={total_weight}, "
        f"sha256={hashlib.sha256(payload.encode('ascii')).hexdigest()}"
    )


if __name__ == "__main__":
    main()
