#!/usr/bin/env python3
"""Exact deterministic cross-check of the two parameterized mex certificates.

This is supporting arithmetic evidence, not a substitute for the uniform proof
in uniform-proof.md.
"""

from hashlib import sha256
from pathlib import Path

A = "0011021"
B = "0011223"
C = "021021"
D = "32203103"
E = "02102102"


def mex(chars):
    values = {int(x) for x in chars}
    return next(x for x in range(4) if x not in values)


def candidate(kind, k, length):
    if kind == 4:
        c = 7 * k + 4
        pre, period = A * k + B, C + A * k
    else:
        c = 7 * k
        pre, period = A * k + D, "1" + A * (k - 1) + E
    repeats = max(0, (length - len(pre) + len(period) - 1) // len(period))
    return c, pre, period, (pre + period * repeats)[:length]


def sg(c, length):
    out = []
    for n in range(length):
        out.append(str(mex(out[n - s] for s in (2, 5, c) if n >= s)))
    return "".join(out)


def primitive(word):
    return all(word != word[:d] * (len(word) // d)
               for d in range(1, len(word)) if len(word) % d == 0)


def check(kind, ks):
    for k in ks:
        c, pre, period, _ = candidate(kind, k, 1)
        q, p = len(pre), len(period)
        length = q + c + 3 * p + 9
        c2, pre2, period2, proposed = candidate(kind, k, length)
        assert c2 == c and pre2 == pre and period2 == period
        actual = sg(c, length)
        assert actual == proposed, (kind, k)
        assert p == c + 2 and primitive(period)
        assert actual[q - 1] != actual[q - 1 + p]


def row(word, r):
    p = len(word)
    triple = "".join(word[j % p] for j in (r - 5, r - 2, r + 2))
    return word[r % p], triple


def transient_row(kind, k, m):
    c, pre, period, word = candidate(kind, k, 3 * (7 * k + 20))
    n = c + m
    return word[n], "".join((word[n - 5], word[n - 2], word[m]))


def check_transcribed_tables():
    # Cyclic c=7K+4 table (K=3 is a non-overlapping representative).
    _, _, p4, _ = candidate(4, 3, 1)
    ix4 = list(range(11)) + [len(p4) - 2, len(p4) - 1]
    cur4 = "0210210011021"
    tri4 = "121 110 002 221 110 000 221 111 000 202 111 010 002".split()
    assert [row(p4, i) for i in ix4] == list(zip(cur4, tri4))

    # The complete exceptional K=1 transient table.
    cur41 = "22302102100110"
    tri41 = "110 010 021 121 130 202 221 310 000 221 111 002 202 113".split()
    assert [transient_row(4, 1, i) for i in range(14)] == list(zip(cur41, tri41))

    # Universal early and late c=7K+4 transient tables.
    cur4e = "22302102100110"
    tri4e = "110 010 021 121 130 202 221 310 000 221 111 000 202 111".split()
    assert [transient_row(4, 3, i) for i in range(14)] == list(zip(cur4e, tri4e))
    cur4z = "2100110"
    tri4z = "010 000 121 111 002 202 113".split()
    assert [transient_row(4, 3, 21 + i) for i in range(7)] == list(zip(cur4z, tri4z))

    # Cyclic c=7K table and its two transient seam tables (K=3).
    _, _, p0, _ = candidate(0, 3, 1)
    ix0 = list(range(6)) + list(range(13, 23))
    cur0 = "100110" + "2102102102"
    tri0 = "000 221 111 000 202 111 010 002 121 110 002 221 110 002 221 110".split()
    assert [row(p0, i) for i in ix0] == list(zip(cur0, tri0))
    cur0e = "32203103100110"
    tri0e = "120 110 031 221 120 302 231 210 000 331 111 000 302 111".split()
    assert [transient_row(0, 3, i) for i in range(14)] == list(zip(cur0e, tri0e))
    cur0z = "21021021"
    tri0z = "013 002 122 110 003 221 110 003".split()
    assert [transient_row(0, 3, 21 + i) for i in range(8)] == list(zip(cur0z, tri0z))


def main():
    project = Path(__file__).resolve().parents[1]
    assert sha256((project / "source.md").read_bytes()).hexdigest() == (
        "17ecfb76de9693198bff4dfd4fae5cbc89742cfbe4c00eb96b93fe0dddb46175"
    )
    assert sha256((project / "evidence/external/2609.05358v1.pdf").read_bytes()).hexdigest() == (
        "39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca"
    )
    check(4, range(1, 1001))
    check(0, range(2, 1001))
    check_transcribed_tables()
    print("PASS: exact recurrence, proposed words, primitive periods, and q-1 mismatches")
    print("coverage: c=7K+4 for K=1..1000; c=7K for K=2..1000")


if __name__ == "__main__":
    main()
