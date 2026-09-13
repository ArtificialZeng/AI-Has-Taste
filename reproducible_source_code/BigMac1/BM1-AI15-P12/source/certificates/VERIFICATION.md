# Exact verification record

## Serialized certificate

File: `n3_sos_certificate.json`

SHA-256:
`b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0`

The certificate fixes the `n=3` theorem, the two homogeneous projective row
normal forms, the permanent convention, the doubled-block convention, and
the two claimed sum-of-squares gaps.

## Verifier 1: pure standard library

Command:

```bash
python certificates/verify_n3_sos_stdlib.py
```

Recorded environment: Python 3.13.5.  Result: `PASS`; both remainder
polynomials had zero monomials.  Verifier SHA-256:
`417ef6ada623660d9268b22041f4c3bb32799c9a7ab00fabaa0ede29e6e7a5b4`.

This verifier enumerates the permanent definition and implements sparse
integer polynomial arithmetic without a CAS.

## Verifier 2: SymPy implementation

Command:

```bash
python certificates/verify_n3_sos.py
```

Recorded environment: Python 3.13.5, SymPy 1.13.3.  Result: `PASS`; the two
expanded integer-coefficient remainders were zero.  Verifier SHA-256:
`ebb692bb0a4914ddcd11c01baede7e8e9fd2d2e2468dfe1f8afb78b7cb8a6e3d`.

## Fail-closed negative suite

Both verifiers bind the canonical certificate SHA-256, enforce exact
top-level and nested key sets, exact JSON types, and all theorem-bound values,
and reject duplicate keys, non-finite JSON constants, and invalid UTF-8.

```bash
python certificates/test_fail_closed.py
```

Result: `PASS`.  Each of `badhash`, `extra`, `drop`, and `tamper` was rejected
by both command-line verifiers; duplicate-key and `NaN` parser inputs were
also rejected.  The canonical certificate hash was unchanged.  Negative-test
SHA-256:
`4c455c63a082812798621f69243f7182f71bcfce040ce3df65c9030454121c81`.

## Equality cross-check

Command:

```bash
python certificates/builder_verify_n3_equality.py
```

Recorded result:

```text
PASS: distinct GL2/SOS identity
PASS: repeated GL2/SOS identity
PASS: symbolic 2x2 zero-block family
PASS: symbolic rank-one family
ALL EQUALITY CROSS-CHECKS PASSED
```

## Independent binary-form cross-check

Command:

```bash
python experiments/builder_verify_n3.py
```

This independently verifies the binary-form contraction identities, the
ordered-root discriminant, the repeated-root stratum, and one mixed-sign
integer matrix by direct permutation enumeration.  Recorded result:
`ALL EXACT CHECKS PASSED`.

## Pinned clean reproduction

The single command

```bash
bash scripts/reproduce_clean.sh
```

requires CPython 3.13.5, creates a fresh temporary virtual environment,
installs `SymPy==1.13.3` and `mpmath==1.3.0` from
`requirements-repro.txt` using required wheel SHA-256 hashes, runs all
positive, negative, equality, builder, referee, and breaker verification
targets, and performs a clean LaTeX build in a separate temporary directory.
Recorded result: `ALL CLEAN REPRODUCTION CHECKS PASSED`.

No proof assistant was used.
