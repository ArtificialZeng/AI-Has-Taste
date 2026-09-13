#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Exact exhaustive weak-abelian-square test on h^3(0).

For each split q, an interval ending at q and one starting at q have equal
letter frequencies exactly when their Parikh vectors, divided by the gcd of
their five coordinates, agree.  Thus intersecting these primitive signatures
tests every triple 0 <= p < q < r <= |h^3(0)| in O(N^2) time.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


BASE = tuple(map(int, "01213101314310"))
POWER = 3


def morph(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a + x) % 5 for a in word for x in BASE)


def primitive_signature(v: tuple[int, ...]) -> tuple[int, ...]:
    g = 0
    for x in v:
        g = math.gcd(g, x)
    assert g > 0
    return tuple(x // g for x in v)


def main() -> None:
    word = (0,)
    for _ in range(POWER):
        word = morph(word)
    n = len(word)
    assert n == 14**POWER == 2744

    prefix = [[0, 0, 0, 0, 0]]
    for a in word:
        row = prefix[-1].copy()
        row[a] += 1
        prefix.append(row)

    witness = None
    signatures_compared = 0
    # Deterministic enumeration: increasing q, then increasing r.  For a
    # matching signature, retain the smallest p that ends at q.
    for q in range(1, n):
        left: dict[tuple[int, ...], int] = {}
        for p in range(q):
            v = tuple(prefix[q][i] - prefix[p][i] for i in range(5))
            sig = primitive_signature(v)
            if sig not in left:
                left[sig] = p
        for r in range(q + 1, n + 1):
            v = tuple(prefix[r][i] - prefix[q][i] for i in range(5))
            sig = primitive_signature(v)
            signatures_compared += 1
            if sig in left:
                p = left[sig]
                xvec = tuple(prefix[q][i] - prefix[p][i] for i in range(5))
                yvec = tuple(prefix[r][i] - prefix[q][i] for i in range(5))
                m, ell = q - p, r - q
                assert all(ell * xvec[i] == m * yvec[i] for i in range(5))
                witness = {
                    "p": p,
                    "q": q,
                    "r": r,
                    "m": m,
                    "n": ell,
                    "x": "".join(map(str, word[p:q])),
                    "y": "".join(map(str, word[q:r])),
                    "parikh_x": list(xvec),
                    "parikh_y": list(yvec),
                    "primitive_signature": list(sig),
                }
                break
        if witness is not None:
            break

    result = {
        "test": "all triples 0 <= p < q < r <= 2744 for h^3(0)",
        "method": (
            "For each q, intersect primitive Parikh signatures of every "
            "factor ending at q with every factor starting at q."
        ),
        "completeness": (
            "Every admissible triple occurs uniquely in the loops at its split q; "
            "signature equality is equivalent to the cross-multiplied five-coordinate equality."
        ),
        "base": "01213101314310",
        "power": POWER,
        "prefix_length": n,
        "prefix_sha256": hashlib.sha256(bytes(word)).hexdigest(),
        "word_encoding_for_digest": "raw bytes with values 0,1,2,3,4",
        "outcome": "violation" if witness is not None else "no_violation_in_finite_prefix",
        "signatures_compared_before_stop": signatures_compared,
        "witness": witness,
    }
    out = Path(__file__).with_name("h3_collinearity.json")
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
