# Root proof audit

The finite invariant was reconstructed from the corrected quantifiers: primes
may be omitted, and at most one canonical residue class is chosen for each
selected prime.  On 2026-09-01 the following checks were executed afresh:

1. The independent witness verifier recomputed primality, distinct moduli,
   canonical residues, full coverage of `[1,41]`, and the reduced exact cost.
2. The Cartesian brute-force checker agreed with the main enumerator for every
   instance through `N=10`.
3. The full standard-library enumeration was rerun from the empty state.  It
   entered 28,998,666 states, stored 5,536,355 failed states, applied
   22,110,683 exact capacity prunes, and again returned
   `"cheaper_cover_exists": false` after 430.74 seconds.

Forced branching is complete because any completion must cover the selected
uncovered point with its unique residue for some unused prime.  The fractional
capacity calculation is a relaxation: it ignores overlaps and permits
fractional use of each prime's best gain, so its optimum is a lower bound on
every genuine completion.  All comparisons use integer-scaled costs.  The
cache key `(covered, unused primes)` determines the selected prime set and
therefore its accumulated cost.

The witness and exhaustive strict-lower-cost exclusion prove exactly
`mu(41)=4369938619315/3202634352918`.  No proof assistant was used; the result
remains subject to ordinary external peer review.
