#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Exact bit-set implementation of Proposition 36.

The bit at position m-2 represents m in X_n={2,...,n+1}.  This module knows
nothing about extendibility or the Theorem 30 CSP.
"""

from __future__ import annotations

import hashlib


def mask_digest(masks: set[int]) -> str:
    """Canonical SHA-256 of a finite set of nonnegative integer masks."""
    payload = "".join(f"{value:x}\n" for value in sorted(masks)).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def local_elimination_masks(n: int, modulus: int) -> tuple[int, ...]:
    """Distinct E^(n)_{modulus,a}, ordered by their integer bit masks."""
    masks: set[int] = set()
    for residue in range(modulus):
        mask = 0
        for m in range(modulus + 1, n + 2):
            if m % modulus == residue:
                mask |= 1 << (m - 2)
        masks.add(mask)
    return tuple(sorted(masks))


def generate_survivors(n: int) -> tuple[set[int], list[dict[str, object]]]:
    """Return F_n as survivor masks and a complete recurrence transcript."""
    if n < 1:
        raise ValueError("n must be positive")
    unions = {0}
    stages: list[dict[str, object]] = [
        {
            "j": 1,
            "local_count": 1,
            "local_masks_hex": ["0"],
            "union_count": 1,
            "union_sha256": mask_digest(unions),
        }
    ]
    for j in range(2, n + 1):
        local = local_elimination_masks(n, j)
        unions = {old | new for old in unions for new in local}
        stages.append(
            {
                "j": j,
                "local_count": len(local),
                "local_masks_hex": [f"{value:x}" for value in local],
                "union_count": len(unions),
                "union_sha256": mask_digest(unions),
            }
        )
    x_mask = (1 << n) - 1
    survivors = {x_mask ^ eliminated for eliminated in unions}
    assert len(survivors) == len(unions)
    return survivors, stages


def mask_to_set(mask: int, n: int) -> list[int]:
    return [m for m in range(2, n + 2) if mask & (1 << (m - 2))]
