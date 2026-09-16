# Root proof audit

The theorem was reconstructed from the formal definition rather than from the
task's conclusion.  The following checks were executed afresh on 2026-09-01:

1. `check_witness.py` verified 41 distinct starts, 82 distinct integers in
   range, and all 3,321 pairwise gcds for the `x=529, d=42` witness.
2. `crosscheck_small.py` compared both decision implementations with literal
   combination enumeration on 568 decisions for all even gaps at
   `8 <= x <= 30`; all decisions agreed.
3. `clique_search.py 528 41` exhaustively processed all 263 even gaps and
   returned `overall=UNSAT` in a fresh log.
4. `packing_verify.py 528 41` independently rebuilt prime supports, processed
   all 263 even gaps and returned `overall=UNSAT` in a second fresh log.

The parity lemma eliminates every odd gap for `n=41`; the code covers the
remaining full range `d=2,4,...,526`.  The graph/clique and support/packing
reductions are both biconditional.  The greedy coloring bound is sound because
each generated color class is independent, so a clique contains at most one
vertex from each class.  No timeout, floating-point comparison, random seed or
external solver status enters the theorem.

Conclusion: the exact finite statement `L_41=529` passes independent root
audit.  Priority remains bounded to the recorded searches and is not an
absolute claim.
