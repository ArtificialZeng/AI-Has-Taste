# Proof audit

Status: **PASS** for the locked theorem, 2026-08-29.

- Formal theorem SHA-256:
  `cd1348a3acb960aceac6feb71676d369e7d57fe05bdba210e5b3e0eb2da3d4b5`.
- Exact certificate SHA-256:
  `889e65022bac2a3b413bddd356eeb526f6067c280155a90c2d54aef39f50961e`.
- Standard-library verifier SHA-256:
  `50eea19e32b3598fb94408d252cafcc96e5ff8fda652e4cea240bc3e412270d7`.
- Complete finite coverage: 64 canonical cuts, 189 directed comparisons.
- Exact continuum coverage: 185 Sturm zero-root checks on rational
  superintervals plus four threshold identities.
- Equality, complement normalization, zero cut, excluded \(r=1\), and
  limiting \(r\to2^-\) audited.
- Deterministic regeneration and two negative mutation tests passed.
- Fatal gaps open: 0.  Major gaps open: 0.
- Proof assistant used: no.

The audit does not by itself certify novelty or manuscript metadata; see the
separate citation and PDF audits.
