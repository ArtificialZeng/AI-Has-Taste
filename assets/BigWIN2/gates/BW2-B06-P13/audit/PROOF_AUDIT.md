# Proof audit

Audit date: 2026-08-30 UTC.

## Verdict

- Unrestricted AS-C1(5,3): **open in this project**.
- Centered rectangular pyramids: **proved and exactly certified**.
- Centered rhombic pyramids: **proved and exactly certified**.
- One-point nondegenerate escape boundary: **proved by exact reduction to the
  four-point theorem**.

## Scope and definition checks

- [x] Source statement preserved literally in `problem/source_statement.md`.
- [x] Hopf map, lifts, binary quartics, coefficient order, determinant, and
  quantifiers fixed in the locked formal statement.
- [x] The special-family theorem statements require exactly \(A,H>0\), so all
  five points are distinct and the apex is off the base plane.
- [x] Similarity and reflection reductions cover every rectangle/rhombus in
  the claimed centered-apex geometry.
- [x] No north-pole chart exception occurs in either family.
- [x] No statement about C2, C3, or arbitrary five points is inferred.

## Identity and sign checks

- [x] Rectangle identity checked by exact coefficient determinant over
  `ZZ_I[w,A,S]` modulo `S^2-A^2-1`.
- [x] Rectangle identity independently checked from five exact projective
  values and Vandermonde determinant `-16*I`.
- [x] Rhombus identity checked by exact coefficient determinant over
  `ZZ_I[u,v,A,S]`; it is a polynomial identity before geometric relations.
- [x] Rhombus identity independently checked from five exact projective
  values and Vandermonde determinant `-16*I`.
- [x] Every denominator-clearing factor is strictly positive on the theorem
  domain.
- [x] Both final sign/nonzero arguments are human-readable sums of positive
  terms; no numerical lower bound is used.
- [x] Direct-coordinate Referee specializations and the Hopf bridge passed.

## Boundary and failure checks

- [x] Degenerate \(A=0\) and coplanar \(H=0\) are not silently included.
- [x] Reflection handles negative signed height without changing the zero set.
- [x] One-point escape is block triangular and locally stable by continuity.
- [ ] Collision, degenerate-cluster, and multi-cluster boundaries remain open.
- [ ] The general centered-parallelogram parent has no nonvanishing
  certificate; its exact expression sizes are recorded.
- [ ] The unrestricted eight-parameter theorem remains open.

## Reproduction commands

```text
python3 code/certify_rectangular_pyramid.py
python3 code/verify_rectangular_pyramid_identity.py
python3 code/certify_rhombic_pyramid.py
python3 code/verify_rhombic_pyramid_identity.py
python3 code/referee_geometry_checks.py
python3 code/test_evaluators.py
```

All six commands passed in the recorded environment. The numerical Breaker
campaign is classified as diagnostic and is not a premise of either theorem.
