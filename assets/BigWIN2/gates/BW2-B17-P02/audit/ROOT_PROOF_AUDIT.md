# Root proof audit

The finite maximum was reconstructed directly from the stated quantifiers.
The following checks were executed afresh on 2026-09-01:

1. The displayed 16-element set passed a direct check of all 560 unordered
   triples, establishing the lower bound.
2. The complete CNF generator was checked clause by clause.  Its forbidden
   clauses are exactly the triples with three equal pairwise gcds, and every
   cardinality state is encoded by a two-direction recurrence for “at least
   `j` selected among the first `i` variables.”
3. The generator was run into a fresh temporary directory.  It produced 2,132
   variables and 122,227 clauses, byte-for-byte identical to the certified
   DIMACS instance.
4. The semantic small-instance cross-check agreed with literal subset
   enumeration for every threshold through `N=12`.
5. The 417,189,026-byte DRAT derivation was replayed from the beginning with
   the independently distributed `drat-trim` binary.  It again ended in
   `s VERIFIED`, checking 1,834,588 core lemmas and 120,875,397 resolution
   steps in 181.88 seconds.

No timeout, heuristic solver answer, floating-point comparison, or claimed
optimality status is used in the theorem.  The explicit witness and checked
refutation prove exactly `f_3(126)=16`.  No proof assistant was used; the
result remains subject to ordinary external peer review.
