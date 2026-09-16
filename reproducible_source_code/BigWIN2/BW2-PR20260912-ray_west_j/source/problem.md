# Ray–West correction statistic: precise interpretation and current scope

The immutable original is source.md (SHA256
92f387c6551ae42e866ea2561665abf78b80baa018f1808f81a0d899ea4b7bf2).

For every integer m>=1, let S_m be the permutations of {1,...,m}.
Standardization replaces each entry in a tuple of distinct values by its rank.
Classical containment beta<=pi means that some (not necessarily consecutive)
subsequence of pi standardizes to beta. Define

    g_k(beta) = |{pi in S_(m+k): beta<=pi}|, k>=0,
    B(m) = (m^4+2m^3+m^2+4m+4)/2,
    j(beta) = B(m)-g_2(beta).

Each ambient permutation is counted once, regardless of embedding multiplicity.
The empty permutation is excluded. The original task seeks an intrinsic
statistical description of j valid for every m and beta. Repeating the residual
definition or merely renaming existing tracks is not a contribution. No formal
statistic family is silently imposed on the original problem.

## Nearest prior result and literature scope

Ray–West (2003), Proposition 8.5, Corollary 8.6 and Theorem 8.7, printed
pp. 80–83, describe active pattern-(C) configurations, at most one counted
lefthand triple for each adjacent-column pair. Their count is j. The bounds
0<=j<=m-1 and the realization of every value for m>=5 are already known.
The primary PDF/text are copied into evidence/external/. Corollary 8.6 has
a repeated printed sign in its second signed-track case; use explicit
reflection and the examples when checking that case, not an implicit correction.

The live Vatter v2 paper still asks Problem 3.7 in the inspected passage on
2026-09-12. This supports open status within the inspected sources only.
See literature/triage-sources.md and literature/research-sources.md for the
bounded searches, source positions and limitations. No novelty clearance or
independent mathematical referee is claimed.

## Subsidiary equality target, unchanged

    For every m>=1 and beta in S_m,
    j(beta)=m-1 iff beta is layered or colayered.              (E)

Layered means a direct sum of decreasing blocks, equivalently Av(231,312).
Colayered means a skew sum of increasing blocks, equivalently Av(132,213).
A direct sum alpha⊕beta puts beta to the right with all values increased by
|alpha|; a skew sum puts beta to the right and increases alpha's values by
|beta|. These classes are explicitly separate from the original universal
statistics problem. E would classify equality, not determine intermediate j.

The implication from layered/colayered to equality is proved using active insertion
identities at each internal bond and at each boundary of decreasing blocks;
value complementation gives the colayered case. The full argument and its
primary-source dependencies are in evidence/structural-progress.md. This
special case has not been separately established as a novel publishable result.
The converse for arbitrary permutations remains unproved; the candidate
below establishes it for every sum- or skew-decomposable permutation.

## Deletion route and its failed strengthening

Writing d(beta)=|beta|-1-j(beta), the unproved sufficient lemma is

    j(beta)<=j(std(beta with one entry removed))+1.            (D)

If D holds universally, d is nondecreasing under pattern containment, making
the zero-deficit class hereditary. The ten nonextremal length-4 patterns in
evidence/extremal-test.json would then be forbidden. This is a proposed route,
not a proof of E or an established equivalence to the original task.

The stronger pointwise claim that a good gap survives deletion of any other
entry is false: 246135 -> 25134 by deleting position 2 loses the good gap
between the surviving values 6 and 1. Both have j=1. The exact triples,
exhaustive finite gap tests and separate insertion recounts are in
evidence/gap-deletion-test.json and evidence/structural-verification.json.
This rejects that literal gap-preserving proof route, not D itself.

## Exact finite evidence and provenance

All 409,113 permutations of lengths 1 through 9 have exact g2 counts.
The new implementation enumerates every ambient permutation, deduplicates
all two-position deletions by integer Lehmer ranks, and reproduces every
prior count through length 7. Length 8 and 9 used all 10! and 11! ambient
permutations respectively; all 3,588,480 deletions from these two new lengths
satisfy D. E also has zero discrepancies. Their extremizer counts are 254
and 510. Including the prior range gives 3,628,798 tested deletions.

All 254 length-8 and 510 length-9 extremizers, plus 64 seeded samples at each
length, were independently recounted by the insertion algorithm. The numbers
of distinct checked patterns are 318 and 573 respectively (one length-9
sample is also an extremizer). This is algorithmic verification by one worker,
not an independent referee. See evidence/length8-test.json and
length9-test.json; the full length-9 g2 vector is
 evidence/exact-counts-length9.npy in lexicographic permutation order.

All inherited lengths <=7 are conservatively exploratory. The updated
handoff reports that E was stated before length-7 generation, while the
holdout label and D tests came later. This worker did not independently audit
the underlying event log and makes no claim that E was invented after length
7. That range is already seen for this pass; no blind-test status is relied on. E and D
were frozen without revision before the new length-8 computation; length 9
was separately selected after length 8 passed. Protocol files preserve this
ordering. Finite tests do not establish universal claims.

## Pass 2 candidate: direct-sum formula and separable statistic

Let T(alpha) indicate that the last sum-indecomposable component of nonempty
alpha is decreasing. Let H(beta) indicate that the first component of
nonempty beta is decreasing; singletons qualify. The proposed theorem is

    j(alpha⊕beta)=j(alpha)+j(beta)+T(alpha)H(beta).             (S)

The complete submitted proof is evidence/sum-restriction-proof.md. It
proves the stronger statement that internal good gaps restrict exactly,
and that the join has precisely the stated endpoint criterion. Literal
coordinate clipping with the inserted right permutation fixed is false:
the smallest witness is 213=21 direct-sum 1. The repair clips both site
multisets to the prefix grid but determines the right permutation from the
two points complementary to the induced prefix occurrence. This preserves
synonymity and both strict (C) inequalities. Ascending internal gaps and
the join are handled using the two monotone tracks and their complete
contiguous support. Right triples need not be active or canonical.

Consequences in the candidate scope: the complemented skew-sum rule;
an intrinsic statistic on the maximal sum/skew decomposition tree of every
separable permutation; and equality j=m-1 iff layered for every
sum-decomposable permutation, with the colayered skew analogue. The tree
statistic counts adjacent decreasing children at sum nodes and adjacent
increasing children at skew nodes. No general statistic for permutations
indecomposable in both senses is claimed. The known-gap list for the
submitted proof is empty; fresh mathematical review has not occurred.

New exact verification enumerates all insertion triples, including inactive
right triples, for all 873 permutations through length 6 and 15 larger
structured permutations of lengths 10--12. It checks 3,110 pair/cut cases,
including 1,219 repaired prefix restrictions; 188 change the right pattern.
All checks pass. See evidence/verify_sum_restriction.py and
evidence/sum-restriction-verification.json. The separate executable tree
statistic matches all 52,465 separable permutations in the inherited exact
census through length 9; this is regression evidence, not a blind test.
See evidence/separable_statistic.py and its verification JSON.

The earlier 132,849 direct-sum total checks through length 9 and 2,673
gap checks through length 7 informed S and remain exploratory. No new
holdout claim is made for them. Current bounded comparison, including
Shar's adjacent work on repeated direct sums, is documented in
literature/research-pass2-sources.md. No equivalent composition law was
found in the inspected passages; this is not a priority certification.

One next test: a fresh referee should verify the stated Ray--West track
dependencies, the induced-occurrence clipping/re-pairing proof and all
boundary cases, and the necessity of the join condition, then assess the
composition theorem against the recorded closest literature. This tests
the exact candidate; do not repeat the already passed census tests.

The earlier finite counterexamples to the classical-pattern-count and
standard-statistics determining vectors remain recorded in
 evidence/statistics-test.json. The original Problem 3.7 remains unresolved.
