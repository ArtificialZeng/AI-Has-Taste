# Structural progress and exact failure dossier

Job: primary-20260912-ray-west-j-research-6795cc8901c9; 2026-09-12.
This is research evidence, not an accepted manuscript or a novelty claim.

## Dependencies and terminology

Use Ray--West, evidence/external/ray-west-2003.pdf, printed pp. 64, 67,
80--83: active insertion sites and triples, Proposition 8.5, Corollary 8.6,
Theorem 8.7. In particular j counts active **lefthand triples**, not all
pairs of synonymous triples. At most one counted lefthand triple is assigned
to each gap between adjacent entries. Call such a gap good. The two tracks
have increasing row coordinates; their column coordinates move together
in one direction. The track support is a contiguous permutation submatrix.
This terminology restates the known rule; it is not a new formula for j.

## Established special case: every layered or colayered permutation is extremal

Here is an explicit argument using the known active-triple rule. Write
delta_a=(a,a-1,...,1), iota_2=12, and eta_2=21. Grid coordinates below are
one-based, exactly as in the source; repeated coordinates are permitted.

First, for the permutation 21, the two active triples

    (eta_2; R=(1,1), C=(1,1))
    (eta_2; S=(3,3), D=(3,3))

have common insertion value 2143. They form a pattern-(C) synonymity
counted at its only gap. If a consecutive pair of positions has consecutive
decreasing values in a larger permutation, this identity lifts by replacing
that interval with the displayed common insertion. Both source sites remain
active and all strict separations remain true after translating coordinates.
Thus every decreasing bond gives a good gap.

Next consider delta_a direct-sum delta_b, for arbitrary a,b>=1 and m=a+b.
The two triples

    (iota_2; R=(1,a), C=(a+2,m+1))
    (iota_2; S=(a+2,m+1), D=(1,a))

are synonymous. Their common value, with empty ranges omitted, is

    (a+2, a,a-1,...,2, m+2, 1, m+1,m,...,a+3, a+1).

The first site is (1,a+2): neither adjacent original column contains 1.
The second is (a,m+1): the only adjacent original entry is a+1.
Hence the lefthand triple is active. Also max(R)=a<min(S)=a+2 and
max(D)=a<min(C)=a+2, so this is a reflected pattern-(C) configuration.
The gap assignment is the ascent between positions a and a+1, as follows
either by horizontal reflection in Corollary 8.6 or directly from its first
upper-track element, the 1 in position a. The identity and all inequalities
remain valid when a=1 or b=1.

In a layered permutation, each internal gap of a decreasing block is a
decreasing bond. Every remaining gap separates two adjacent decreasing
blocks, whose union is an interval, so the second identity lifts to it.
There is therefore a counted triple at every gap. Distinct gaps give
distinct lefthand triples, and the known upper bound gives j=m-1. For m=1,
the same conclusion j=0 follows directly from g2=6 and B(1)=6.
Value complementation maps layered permutations to colayered permutations
and bijects their sets of containing permutations, preserving j. This
establishes the forward implication in (E) for every m.

This special case alone is not proposed as a new result-note: its value and
possible prior occurrence have not been independently assessed.

## Exact counterexample to pointwise preservation of good gaps

The stronger auxiliary assertion was:

    If neither endpoint of a good gap is deleted, that gap stays good.

It is false. Take beta=246135 and delete position 2, obtaining gamma=25134.
The only good gap of beta is between positions 3 and 4 (values 6 and 1).
The surviving pair becomes the gap between positions 2 and 3 (values 5 and
1) of gamma, whose only good gap is between positions 4 and 5 (values 3,4).
The explicit triples and ambient insertion identities are recorded in
evidence/gap-deletion-test.json. Exhaustive insertion counts separately give
g2(beta)=895, j(beta)=1; g2(gamma)=461, j(gamma)=1. Thus this is not a
counterexample to (D), or to (E), or to the original Problem 3.7.

The gap experiment checked all 873 permutations through length 6, validating
the number of counted gaps against all corresponding original exact counts.
It found 8 failures of pointwise preservation and no failure of the separate
two-good-gaps contraction assertion. A proof of D cannot simply preserve
each individual good gap; it would require a different assignment or argument.
The quantified method obstruction here is only to this literal assignment.

Implementation correction: an initial insertion implementation counted all
synonymity pairs and double-counted the same lefthand triple for 2143.
The final script deduplicates lefthand triples, as the primary source requires.
The initial assertion failure was an implementation failure, not a mathematical
counterexample. No conclusions use the failed implementation.

## New unproved direct-sum rule and minimal proof gap

For a nonempty permutation alpha, let T(alpha) be 1 if its last
sum-indecomposable component is decreasing, and 0 otherwise. Let H(beta)
be the analogous indicator for the first component. A component of size 1
is decreasing. The natural rule suggested by the tracks is

    j(alpha direct-sum beta)
      = j(alpha)+j(beta)+T(alpha)H(beta).                    (S)

The file evidence/sum-rule-test.json tests all 132,849 direct-sum cuts of
all permutations of total length 2
through 9. There are zero discrepancies. This evidence was used to explore
S and is not described as a predeclared holdout for S.

A sufficient structural lemma is stronger: the good gaps within each
summand are precisely its original good gaps; only the join can contribute
an extra gap, and it is good exactly under the displayed endpoint condition.
The gap-level version was separately tested on all 2,673 direct-sum cuts
through length 7, with all 5,913 computed gap counts checked against exact j.
No failure occurred; see evidence/sum-gap-test.json. The full length-8/9
sum-rule test checks totals, not the individual gap correspondence.

One direction is immediate: local configurations in either interval summand
lift by direct sum, and the explicit two-decreasing-block identity supplies
the join whenever T(alpha)H(beta)=1. To finish, rule out new internal good
gaps whose witnessing tracks extend beyond their summand and prove the
necessity of the join condition. A proposed route restricts the two tracks
at the diagonal cut and clips the righthand insertion sites to the smaller
grid. This needs a complete argument preserving both strict pattern-(C)
inequalities and the active lefthand triple in every boundary degeneracy.
That argument has not been completed here. S is therefore unproved.

If S is proved, value complementation gives its skew-sum counterpart.
Together they would compute j recursively on every separable permutation
from its sum/skew decomposition. At a maximal direct-sum decomposition,
equality j=m-1 would force every incident component to be decreasing;
at a maximal skew decomposition it would force increasing components.
Thus S would also settle E on all separable permutations. These are
conditional consequences, not completed new theorems.

## One next test

Prove or refute the sufficient gap-restriction lemma for a direct-sum cut,
especially a configuration whose righthand sites straddle that cut. A proof
must give the exact clipped multisets and verify all degenerate inequalities;
a counterexample must include both insertion triples and its standardized
restriction. This can settle or reject the identified proof route for S,
without repeating the completed length-8/9 tests of D.
