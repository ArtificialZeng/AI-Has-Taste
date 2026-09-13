# Referee-style assessment

## Scope and correctness

The manuscript is not a solution of the 33-point Erdős--Szekeres problem.  It
is a computational-discrete-geometry methods paper proving a refutation-sound
encoding
compression.  The abstract, title, main theorem, and limitations consistently
state this scope.

The parity theorem has a self-contained affine-cofactor proof.  The signotope
rule is derived from consecutive slopes.  The global SAT implication follows
in the correct contrapositive direction from the four-set criterion.  Exact
counts are transparent binomial identities and are independently executable.

## Novelty and utility

Orientation signs, signotopes, Radon partitions, the four-set convexity
criterion, parity characterization, one four-set variable, and the
endpoint/middle factorization are prior art.  The potentially useful
contribution is narrower: applying that factorization to a single
polarity-aware witness with only the implication needed for refutation,
integrating it into every exclusion clause, and auditing the resulting
33-point formula.  The manuscript now cites the closest 2025/2026 work and
makes only this bounded novelty claim.

## Required language retained

- `ES(7)=33` remains open.
- SAT does not imply geometric realizability.
- Formula size does not imply improved runtime.
- The known `(9,5)` check has independently accepted DRAT and LRAT traces;
  the unanchored `(17,6)` formula is known UNSAT from Szekeres--Peters, and a
  separate extreme-normalized 61-cube DRAT/LRAT certificate is checked here.
- A future exact solution requires either a checked full proof trace or exact
  rational coordinates.

## Recommendation

Suitable for circulation or submission as a reproducible certified encoding
paper after author approval and venue-specific formatting.  It must not be
submitted or advertised under a title claiming to determine `ES(7)`.
