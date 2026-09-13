#!/usr/bin/env python3
"""Independent mask enumeration for multiplicity and divisibility claims."""

from __future__ import annotations

from itertools import product


PARTITIONS = (
    (5,), (4, 1), (3, 2), (3, 1, 1),
    (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1),
)
PRIME_DATA = ((2, 8), (3, 9), (7, 7))


def admissible(partition: tuple[int, ...], masks: tuple[int, ...], rhs_mask: int) -> bool:
    for bit, (_, modulus) in enumerate(PRIME_DATA):
        lhs_units = sum(mult for mult, mask in zip(partition, masks) if mask & (1 << bit))
        rhs_unit = int(bool(rhs_mask & (1 << bit)))
        if (lhs_units - rhs_unit) % modulus:
            return False
        if lhs_units == 0 and rhs_unit == 0:
            return False  # nonprimitive at this prime
    return True


def main() -> int:
    survivors: dict[tuple[int, ...], list[tuple[tuple[int, ...], int]]] = {}
    for partition in PARTITIONS:
        rows = []
        for masks in product(range(8), repeat=len(partition)):
            for rhs_mask in range(8):
                if admissible(partition, masks, rhs_mask):
                    rows.append((masks, rhs_mask))
                    assert rhs_mask == 7
                    for mult, mask in zip(partition, masks):
                        if mult >= 2:
                            assert mask == 0
        survivors[partition] = rows

    assert not survivors[(5,)]
    assert not survivors[(3, 2)]
    assert survivors[(4, 1)]

    for masks, rhs in survivors[(3, 1, 1)]:
        assert masks[0] == 0 and rhs == 7
        assert all(bool(masks[1] & (1 << j)) != bool(masks[2] & (1 << j)) for j in range(3))

    for masks, rhs in survivors[(2, 2, 1)]:
        assert masks == (0, 0, 7) and rhs == 7

    print("INDEPENDENT VERIFIED: repeated blocks have divisibility mask 000, hence 42 divides their bases")
    print("INDEPENDENT VERIFIED: local patterns (5) and (3,2) are impossible in a primitive solution")
    print("INDEPENDENT VERIFIED: the exactly-three-distinct divisibility classification is complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
