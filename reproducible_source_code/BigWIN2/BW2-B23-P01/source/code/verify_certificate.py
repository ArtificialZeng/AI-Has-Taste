#!/usr/bin/env python3
"""Independent exact checker for the A022030 defect certificate."""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from pathlib import Path


def nonlinear(count: int) -> list[int]:
    a = [4, 16]
    for n in range(count - 2):
        q, r = divmod(a[n + 1] * a[n + 1], a[n])
        if n % 2 == 0:
            a.append(q if r else q - 1)
        else:
            a.append(q + 1)
    return a


def linear(count: int) -> list[int]:
    a = [4, 16, 63, 249]
    while len(a) < count:
        a.append(4 * a[-1] - a[-3] + a[-4])
    return a[:count]


def main() -> int:
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    if count < 12:
        raise SystemExit("count must be at least 12")
    L = linear(count + 2)
    A = nonlinear(count + 2)
    assert A == L
    e = [(-1) ** n * (L[n + 1] ** 2 - L[n] * L[n + 2]) for n in range(count)]
    assert e[:10] == [4, 15, 9, 105, 241, 405, 2275, 4530, 12186, 46605]
    for n in range(10, count):
        rhs = (460 * e[n - 2] + 3435 * e[n - 3] + 3585 * e[n - 5]
               + 215 * e[n - 8] + 30 * e[n - 9] + 6 * e[n - 10])
        assert 231 * e[n] == rhs
    assert all(1 <= e[n] <= L[n] for n in range(count))
    weighted_numerator = (460 * 3**8 + 3435 * 3**7 + 3585 * 3**5
                          + 215 * 3**2 + 30 * 3 + 6)
    assert weighted_numerator == 11403591
    assert weighted_numerator % 3 == 0
    assert weighted_numerator // 3 == 3801197
    assert weighted_numerator < 231 * 3**10
    source = Path(__file__).read_bytes()
    out = {
        "status": "PASS",
        "terms_checked": count,
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "last_term_digits": len(str(L[count - 1])),
    }
    print(json.dumps(out, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
