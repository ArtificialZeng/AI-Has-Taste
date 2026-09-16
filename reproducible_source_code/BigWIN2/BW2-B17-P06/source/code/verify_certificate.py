#!/usr/bin/env python3
"""Independent minimal checker for a serialized N=41 covering witness."""
import argparse
import hashlib
import json
from fractions import Fraction


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("certificate")
    a = ap.parse_args()
    d = json.load(open(a.certificate, encoding="utf-8"))
    nmax = d["N"]
    classes = d["classes"]
    assert nmax == 41
    assert len({p for p, _ in classes}) == len(classes)
    assert all(2 <= p <= nmax and all(p % q for q in range(2, p)) for p, _ in classes)
    assert all(0 <= r < p for p, r in classes)
    uncovered = [n for n in range(1, nmax + 1) if not any(n % p == r for p, r in classes)]
    cost = sum((Fraction(1, p) for p, _ in classes), Fraction())
    assert not uncovered
    assert [cost.numerator, cost.denominator] == d["exact_cost"]
    cert_hash = hashlib.sha256(open(a.certificate, "rb").read()).hexdigest()
    code_hash = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    print(f"PASS N={nmax} cost={cost} classes={len(classes)} certificate_sha256={cert_hash} verifier_sha256={code_hash}")


if __name__ == "__main__":
    main()
