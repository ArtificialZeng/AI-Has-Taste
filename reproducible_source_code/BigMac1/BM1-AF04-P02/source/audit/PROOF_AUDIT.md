# Proof audit

Status: **PASS — CERTIFIED_FINITE_RESULT**  
Date: 2026-08-30 (Asia/Shanghai)

## Endpoint checked

The simple Pasch-switch quotient graph on the 80 STS(15) isomorphism
classes has 258 edges and components of orders 79 and 1. The nontrivial
component has diameter 11 and radius 6; the isolated component has diameter
0. Exactly two unordered pairs attain distance 11 in the released naming.

## Independent reconstruction

- Discovery searched four-block subsets and used nauty only for canonical
  naming.
- Certification did not import discovery output or invoke nauty. It found
  Pasches as 4-cycles in derived two-point cycle graphs.
- All 80 representatives passed exact 105-pair coverage.
- All 80 exact point-Pasch signatures were distinct.
- Every one of 1,390 switches was reconstructed and matched by an explicit
  Steiner-quasigroup isomorphism.
- Removing 83 self-switch occurrences and parallel quotient targets gave
  exactly 258 simple undirected edges, all witnessed in both directions.
- Two separately implemented all-pairs BFS checks returned 79+1,
  diameter 11, radius 6, and the same two extremal pairs.

## Lower and upper bounds

The stored BFS layers place `V006` and `V028` in layer 11 from `V000`, so
their distance is at least 11. The certificate stores an 11-edge path to
`V006`. All 79 BFS eccentricities are at most 11, giving the global upper
bound.

## Breaker tests

The fail-closed verifier accepted the baseline and rejected all six
mutations: malformed block, missing vertex, deleted edge, duplicate edge,
false diameter, and false switch target. See
`certificate/negative_tests.json`.

## Trust boundary

All decisive arithmetic is integer/set arithmetic. No floating point,
randomness, optimizer, SAT solver, or proof assistant was used. Exhaustion
of the universe invokes the classical 80-class classification and is
cross-checked by exact equality with the official complete catalogue.
