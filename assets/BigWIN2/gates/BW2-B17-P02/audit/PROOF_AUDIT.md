# Proof audit

Status: PASS; scientific status is `certified finite result`.

- The theorem uses the maximum-avoiding convention and records the historical
  least-forcing off-by-one convention.
- All 560 triples of the displayed 16-set pass an exact gcd verifier.
- The deterministic CNF has 2132 variables and 122227 clauses.
- Every cardinality recurrence is encoded in both directions; all thresholds
  for every N from 1 through 12 agree with complete subset enumeration.
- DRAT-trim reports `s VERIFIED`, with 112162 core input clauses, 1834588 core
  lemmas, and 120875397 resolution steps.
- Every fatal and major gap is closed. UNKNOWN, timeout, interrupted
  optimization, and local-search outcomes are excluded from the proof.
- Builder, breaker, certifier, and referee records are separate.
- No proof assistant was used.
