# Proof dependency graph

## Exact reduction (complete)

1. Positive common distance permits translation and scaling normalization.
2. Sorting one coordinate expresses its absolute-difference metric as a
   nonnegative sum of the ten nested cut metrics determined by consecutive
   gaps.
3. Summing the five coordinate metrics gives system (LP) in
   `problem/formal_statement.md`.
4. Conversely, cumulative sums of any feasible gaps reconstruct five real
   coordinates with the prescribed distances.
5. Zero gaps cover ties and constant coordinates.
6. Rational-polyhedron feasibility gives a rational point whenever a real
   point exists.

## Full target (open dependency)

To prove \(e(\ell_1^5)=10\), it remains to prove every five-chain branch of
(LP) infeasible.  To disprove it, it suffices to exhibit one feasible branch
and its exact rational gaps.

## Spectral sparse-stratum partial theorem (complete human proof)

1. Five-path reduction gives the cut decomposition.
2. Double centering gives the Parseval/tight-frame identity (F).
3. Rank gives at least ten positive gaps.
4. Primality of eleven makes all two nontrivial centered cut indicators
   nonorthogonal, excluding exactly ten columns.
5. A Parseval frame of eleven columns in dimension ten has Gram projection
   \(I-zz^T\); hence every triple of distinct column inner products has
   negative product.
6. Three cuts from one coordinate are nested and have positive pairwise inner
   products; hence each coordinate supplies at most two positive gaps.
7. Five coordinates then supply at most ten, excluding exactly eleven.
8. Therefore every putative target counterexample has at least twelve
   positive gaps.
9. Grouping the Parseval columns by coordinate gives an exact total spectral
   deficit budget \(t-10\).
10. The Markov inverse of a nested-cut correlation matrix, together with
    Cauchy--Schwarz and Jensen, gives a weight-free lower deficit for every
    coordinate chain.
11. Exact rational lower bounds make the minimum total deficit exceed its
    budget for \(t=12,13,14\).
12. Therefore every putative target counterexample has at least fifteen
    positive gaps, or at least twenty coordinate levels in total.
13. At \(t=15\), the same exact convex bound leaves only gap-count patterns
    \((3,3,3,3,3)\) and \((4,3,3,3,2)\).
14. Endpoint-deficit separation forces all but at most one triple chain to
    have singleton rays at both ends, and forces every chain in the mixed
    pattern to do so.
15. Singleton compression subtracts those endpoint rays from the Parseval
    identity; its low-rank kernel forces a large zero set on which every
    remaining cut is constant.
16. The resulting endpoint-capacity and equality-compression contradictions
    eliminate both \(t=15\) patterns.
17. Therefore every putative target counterexample has at least sixteen
    positive gaps, or at least twenty-one coordinate levels in total.
18. At \(t=16\), exact convex deficit bounds leave only
    \((4,3,3,3,3)\), \((4,4,3,3,2)\), and \((5,3,3,3,2)\).
19. Endpoint-loss bounds force at least eight singleton cut copies in each
    case.  Singleton compression excludes every decomposition with between
    one and eight non-singleton copies.  Hence \(t\ne16\).
20. At \(t=17\), exact deficit bounds leave five patterns:
    \((4,4,3,3,3)\), \((5,3,3,3,3)\), \((4,4,4,3,2)\),
    \((5,4,3,3,2)\), and \((6,3,3,3,2)\).
21. The compression obstruction extends through nine non-singleton copies.
    In the rank-nine boundary case, positivity forces exactly one negative
    diagonal coefficient, so the kernel vector has no nonempty proper
    zero-sum subset; every remaining proper cut would require one.
22. Exhaustive exact endpoint-loss checks leave at least eight singleton
    copies in all five patterns, and hence at most nine non-singleton copies.
    Thus \(t\ne17\).
23. Therefore every putative target counterexample has at least eighteen
    positive gaps, or at least twenty-three coordinate levels in total.
24. At \(t=18\), exact convex costs reduce 88 sorted gap-count partitions
    to eight, and exhaustive endpoint-loss bounds leave at least eight
    singleton cut copies in every survivor.
25. Thus the number \(R\) of non-singleton copies lies between eight and
    ten.  The earlier compression lemma excludes \(R\le9\).
26. At \(R=10\), orienting all remaining cuts away from a reference label
    gives \(D+c_pJ=BGB^{\mathsf T}\).  Positivity and
    Sherman--Morrison force the ten oriented blocks to intersect pairwise
    without containment.
27. Two cuts from one coordinate chain become either nested or disjoint
    after that orientation, so every coordinate could contribute at most
    one non-singleton cut.  This contradicts \(R=10>5\).
28. Therefore every putative target counterexample has at least nineteen
    positive gaps, or at least twenty-four coordinate levels in total.

The finite arithmetic in steps 4, 5, 7, 10, 11, 14, 18, 22, and 24 is
independently checked, but the frame and compression implications remain
human proofs.  The full target is still open on all strata with at least
nineteen positive gaps.
