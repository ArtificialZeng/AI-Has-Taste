#!/usr/bin/env python3
"""Small-rank independent audit of exhaustive_rtilde.cpp.

This intentionally does not use fixed-word subword enumeration, compressed
q^{-2} coefficients, or the C++ allowed-product catalog.  It enumerates S_n,
uses the exact rank-matrix criterion for Bruhat order, evaluates the Dyer
recurrence as ordinary polynomials in q, and tests product membership by exact
integer polynomial division.
"""

from __future__ import annotations

import functools
import hashlib
import itertools
import json
import platform
import sys
import time
from pathlib import Path


MAX_N = 8


def inv_length(p: tuple[int, ...]) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


@functools.lru_cache(maxsize=None)
def bruhat_leq(u: tuple[int, ...], v: tuple[int, ...]) -> bool:
    """Ehresmann prefix/rank criterion, in one-line notation."""
    for k in range(1, len(u) + 1):
        if any(a > b for a, b in zip(sorted(u[:k]), sorted(v[:k]))):
            return False
    return True


def right_multiply(p: tuple[int, ...], s: int) -> tuple[int, ...]:
    q = list(p)
    q[s - 1], q[s] = q[s], q[s - 1]
    return tuple(q)


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        ans[i] += x
    for i, x in enumerate(b):
        ans[i] += x
    while ans and ans[-1] == 0:
        ans.pop()
    return tuple(ans)


@functools.lru_cache(maxsize=None)
def rtilde(u: tuple[int, ...], v: tuple[int, ...]) -> tuple[int, ...]:
    if not bruhat_leq(u, v):
        return ()
    if u == v:
        return (1,)
    s = next(i for i in range(1, len(v)) if v[i - 1] > v[i])
    us = right_multiply(u, s)
    vs = right_multiply(v, s)
    if u[s - 1] > u[s]:
        return rtilde(us, vs)
    return add(rtilde(us, vs), (0,) + rtilde(u, vs))


def fibonacci(max_h: int) -> list[tuple[int, ...]]:
    fs: list[tuple[int, ...]] = [(1,), (1,)]
    for h in range(2, max_h + 1):
        fs.append(add(fs[h - 1], (0,) + fs[h - 2]))
    return fs


def exact_divide(
    dividend: tuple[int, ...], divisor: tuple[int, ...]
) -> tuple[int, ...] | None:
    """Exact division in Z[t], using leading terms and rejecting fractions."""
    if len(dividend) < len(divisor):
        return None
    remainder = list(dividend)
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    lead = divisor[-1]
    while len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        if remainder[-1] % lead:
            return None
        coefficient = remainder[-1] // lead
        if coefficient < 0:
            return None
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] -= coefficient * value
        while remainder and remainder[-1] == 0:
            remainder.pop()
    if remainder:
        return None
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return tuple(quotient)


def allowed_factorization(
    polynomial: tuple[int, ...], fs: list[tuple[int, ...]]
) -> tuple[int, ...] | None:
    @functools.lru_cache(maxsize=None)
    def visit(p: tuple[int, ...], minimum_h: int) -> tuple[int, ...] | None:
        if p == (1,):
            return ()
        degree = len(p) - 1
        for h in range(minimum_h, 2 * degree + 2):
            factor = fs[h]
            if len(factor) > len(p):
                continue
            quotient = exact_divide(p, factor)
            if quotient is None:
                continue
            suffix = visit(quotient, h)
            if suffix is not None:
                return (h,) + suffix
        return None

    return visit(polynomial, 2)


def normalized_q_inverse(poly: tuple[int, ...]) -> tuple[int, ...]:
    degree = len(poly) - 1
    if poly[degree] != 1:
        raise AssertionError("Rtilde leading coefficient is not one")
    if any(poly[e] for e in range(degree + 1) if (degree - e) % 2):
        raise AssertionError("Rtilde contains an exponent of the wrong parity")
    ans = tuple(poly[degree - 2 * j] for j in range(degree // 2 + 1))
    while len(ans) > 1 and ans[-1] == 0:
        ans = ans[:-1]
    return ans


def top_permutation(n: int) -> tuple[int, ...]:
    if n == 2:
        return (1, 2)
    return tuple(range(3, n + 1)) + (1, 2)


def run() -> dict[str, object]:
    fs = fibonacci(2 * (MAX_N - 2) + 1)
    report: dict[str, object] = {
        "schema_version": 1,
        "status": "independent_discovery_crosscheck_not_a_certificate",
        "python": sys.version,
        "platform": platform.platform(),
        "max_n": MAX_N,
        "runs": [],
    }
    for n in range(2, MAX_N + 1):
        bruhat_leq.cache_clear()
        rtilde.cache_clear()
        started = time.perf_counter()
        top = top_permutation(n)
        elements = [
            p for p in itertools.permutations(range(1, n + 1)) if bruhat_leq(p, top)
        ]
        elements.sort(key=lambda p: (inv_length(p), p))
        pairs = 0
        rejected = 0
        max_coefficient = 0
        patterns: dict[str, int] = {}
        digest = hashlib.sha256()
        for v in elements:
            for u in elements:
                if not bruhat_leq(u, v):
                    continue
                pairs += 1
                qpoly = rtilde(u, v)
                if len(qpoly) - 1 != inv_length(v) - inv_length(u):
                    raise AssertionError("unexpected Rtilde degree")
                max_coefficient = max(max_coefficient, *qpoly)
                normalized = normalized_q_inverse(qpoly)
                factors = allowed_factorization(normalized, fs)
                if factors is None:
                    rejected += 1
                    pattern = "REJECTED"
                else:
                    pattern = "empty" if not factors else "*".join(f"F{h}" for h in factors)
                patterns[pattern] = patterns.get(pattern, 0) + 1
                digest.update(bytes(u))
                digest.update(bytes(v))
                for coefficient in qpoly:
                    digest.update(coefficient.to_bytes(8, "little"))
        top_value = normalized_q_inverse(rtilde(tuple(range(1, n + 1)), top))
        if top_value != fs[n - 2]:
            raise AssertionError("known top formula failed")
        report["runs"].append(
            {
                "n": n,
                "elements": len(elements),
                "comparable_pairs": pairs,
                "rejected_pairs": rejected,
                "max_coefficient": max_coefficient,
                "top_fibonacci_check": True,
                "sha256_digest": digest.hexdigest(),
                "factor_patterns": dict(sorted(patterns.items())),
                "seconds": round(time.perf_counter() - started, 6),
            }
        )
    return report


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: independent_crosscheck.py OUTPUT_JSON")
    report = run()
    Path(sys.argv[1]).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    for item in report["runs"]:
        print(
            f"n={item['n']} elements={item['elements']} pairs={item['comparable_pairs']} "
            f"rejected={item['rejected_pairs']} seconds={item['seconds']:.3f}"
        )


if __name__ == "__main__":
    main()
