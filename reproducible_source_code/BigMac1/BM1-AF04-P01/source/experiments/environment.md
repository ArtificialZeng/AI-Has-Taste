# Computational provenance

- Date: 2026-08-30 CST.
- Discovery interpreter: `python` = Python 3.13.5 with SymPy 1.13.3 (exact
  symbolic arithmetic).
- Independent-certification interpreter: `python3` = Python 3.14.7, standard
  library only (`fractions.Fraction`).
- Random seed: none; no randomized or floating-point computation is decisive.
- Discovery command: `python src/derive_annihilator.py`.
- Certification command: `python3 certificates/verify_certificate.py certificates/annihilator_certificate.json`.
- Corruption tests: `python3 tests/test_certificate.py`.
- Independent finite baseline: `python3 tests/enumerate_small.py` (complete
  perfect-matching enumeration for (1\le n\le7)).
- Convention: polynomial coefficient arrays are in ascending powers.

The discovery script is not imported by the verifier.  The absence of SymPy in
the `python3` interpreter is intentional and confirms that certification does
not transitively rely on SymPy.  All decisive equalities are rational-function
or integer-polynomial identities.
