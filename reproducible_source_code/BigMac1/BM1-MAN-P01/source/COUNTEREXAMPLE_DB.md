# Counterexample and obstruction database

## BS-O01: the real order-16 polyhedral POT example is not an `F_A` witness

- Construction: the 16 unoriented radius-one directions obtained from the
  vertices of a regular dodecahedron and its dual icosahedron.
- Numerical definition-level test: the largest eigenvalue of `F_A` agrees
  with `per(A)` to floating-point precision; the next eigenvalue is about
  `0.57336908 per(A)`.
- Consequence: importing this famous real POT example does not solve the
  present problem.  This is a route obstruction, not a proof of the real
  conjecture.

## BS-O02: low-rank random/hill-climbing scan through order 15

- Domain sampled: real unit Gram vectors, ranks 2, 3, 4, and 5, orders 6--15.
- Total objective evaluations: 99,850.
- Outcome: no top eigenvalue exceeded `per(A)` beyond numerical tolerance.
  Optimization drove the second eigenvalue toward one only at nearly
  degenerate boundary configurations.
- Consequence: this scan supplies no counterexample and no exclusion proof.
  It motivated the exact regular-projective-polygon theorem instead of a
  larger unstructured numerical search.
