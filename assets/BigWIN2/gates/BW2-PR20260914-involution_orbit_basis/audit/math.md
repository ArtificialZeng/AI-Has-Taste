# Independent mathematical referee report

Verdict: **accept**, at the exact frozen `result-note` scope. The original
Problem 29 remains **unresolved**. This decision includes every assertion in
`claim.json`; no part has been silently weakened or removed.

Referee job: `primary-20260914-involution-orbit-basis-referee-e2f55307d9eb`.
Review date: 2026-09-14. Snapshot digest:
`76c3bd2989246c5cdef363381df3191253a1cb36703b7e0b1db119662841e4bf`.
The proposer job recorded in the claim is different. This is a fresh review
context with separately written verification code, not external peer review
or a claim of statistically independent evidence.

All 19 frozen file hashes and the canonical snapshot digest were checked
before and after the independent computation. They match. The immutable
`source.md` has SHA-256
`07a8d8e1bf2557373b87f38c6dbb4db93eb7fc19477b6d1d6fccbef74722ead8`.
No frozen input was edited. This review read the specified problem, claim,
snapshot, and listed evidence, plus actual primary literature. It did not
consult checkpoint/state files, previous referee reports, or job transcripts.
No additional agents or model processes were used.

The accepted scope is degrees 0, 1, and 2 for all admissible n,a with a>=2
and k=(n-a)/2>=2. It includes the literal source candidate, its stated
off-diagonal standard monomial property for every refinement of the weights
n^2-ij, uniqueness and strict score inequalities in quadratic straightening,
and the complete basis and Hilbert series when a=n-4, n>=6. The exclusions
a<2 and k<2 are material; n>=6 follows from the hypotheses. There is no
accepted assertion about arbitrary higher degrees or a uniform answer to
the original construction problem.

The decisive argument was reconstructed as follows.

1. **The precise quotient.** Let E be the two-element subsets of [n],
   B=Q[y_e:e in E]/(y_e^2, y_e*y_f for intersecting distinct e,f), and
   L=sum_e y_e. The known homogeneous ideal presentation gives symmetry
   and row sums, which eliminate x_ji and x_ii, with
   x_ii=-sum_(j!=i)y_ij. Every row/column quadratic product becomes a
   nonmatching product in B. Conversely, each defining quadratic relation
   of B comes from such a product. The trace relation becomes -2L.
   The remaining generators have degree a+1 or degree greater than k;
   both are at least 3 here. Linear homogeneous substitution preserves
   degree, and homogeneous ideal generation cannot introduce additional
   degree-1 or degree-2 consequences from these higher generators.
   Thus R_1=B_1/QL and R_2=B_2/LB_1 exactly. This works over Q and C;
   the defining relations have rational coefficients, so scalar extension
   does not change these conclusions. The use of characteristic zero,
   including division by 2, is legitimate.

2. **An actual basis, without relying on its predicted cardinality.**
   The vertices of KG(n,2) are E and its edges are H_n. With D the
   signless vertex-edge incidence matrix, the rows of D are precisely
   the relations y_e L. The first three families defining T_n give three
   vertex-disjoint stars covering E. The last three edges connect them
   and create exactly the cycle
   13--24--15--34--25--13. The resulting connected graph has |E| edges
   and |E| vertices. A left-kernel vector for D_T must change sign across
   each edge. Its value vanishes on this odd cycle and hence everywhere.
   Therefore D_T is invertible; leaf removal also gives |det(D_T)|=2.
   Its invertibility makes the map from the relation space to the T_n
   coordinates an isomorphism. Consequently H_n minus T_n is a basis
   of R_2, and the unique straightening matrix is -D_T^{-1}D_H.

3. **Strict weight comparisons, including the potentially equal cases.**
   Put p(ij)=ij and score(uv)=p(u)+p(v). An alternating sum of the
   incidence columns of an odd walk from u to v is e_u+e_v, also when
   the walk repeats an edge. It suffices to span each column h outside
   T_n using only T_n columns of strictly smaller score. The three cases
   in the frozen proof are exhaustive after excluding edges incident
   with vertex 12, which all belong to T_n.

   For h=(1r)(2s), r,s>=4 and r!=s, the walk
   1r--23--15--24--13--2s has scores r+6,11,13,11,2s+3.
   They are strictly below r+2s. The only possible equality at the
   minimum r+2s=13 is (r,s)=(5,4), and that h belongs to T_n.

   For h=(1r)(st), 3<=s<t, with 2 absent and r>=4, use
   1r--23--15--34--12--st. Its scores are r+6,11,17,14,st+2.
   If r=4, disjointness gives r+st>=19; if r=5, equality at 17 occurs
   only for the excluded edge 15--34; if r>=6 the score is at least 18.
   The first and last comparisons are strict as well. The r=3 case
   has score at least 23.

   All other h either have type (2r)(st) or contain neither 1 nor 2.
   Their scores are greater than 22 after excluding 25--34. In the
   first type the relevant lower bounds are 26,23,22,24 for r=3,4,5,
   or r>=6, respectively; equality at 22 is the excluded edge. In the
   second type the minimum is 38. The ten-vertex subgraph T_5 is
   connected, contains the odd cycle, and has maximum score 22.
   Every endpoint of h outside that core attaches by one T_n edge:
   1r to 23, 2r to 13, or ij (i,j>=3) to 12. The selected neighbor
   uniquely minimizes p among disjoint vertices. Because h is not this
   attachment edge, its score is strictly larger. The smaller-score
   subgraph therefore contains the core and the two endpoints, and
   its incidence columns span e_u+e_v.

   These arguments establish the strict comparison for every n in the
   claimed range, rather than extrapolating it from numerical margins.
   Since D_T is invertible, no alternative coefficient representation
   can introduce a larger-score T_n column. Thus a nonzero straightening
   coefficient at h indeed implies score(t)<score(h).

4. **The literal Pieri--RSK candidate.** For support s1<s2<s3<s4, forward
   RSK followed by transposition gives respectively
   [s1 s2; s3 s4], [s1 s3; s2 s4], and [s1 s2 s3 s4] for the three
   pairings stated in the frozen proof. Increasing insertion of unused
   labels is inverse to the source's removal of the horizontal strip.
   For shape (2,2), positivity is equivalent to creating a third row:
   a strip box must be present in column 1, after which the second
   step cannot go below zero and all later columns are strip columns.
   The two cases fail precisely when no unused label lies below s2
   or below s3, respectively, namely s2=2 or s3=3. Their failures are
   exactly 12--ij and 13--2j in T_n.

   For the one-row starting shape (4), increasing insertion bumps only
   original support labels, increasingly, into a second row. Its length
   is the maximum number of disjoint pairs consisting of an unused
   label and a larger support label. Positivity is equivalent to this
   length being at least 2. Two such pairs exist exactly when s3>=4
   and s4>=6: these conditions say that at least one unused label is
   below s3 and at least two are below s4, respectively. They permit
   pairing the first two unused labels with s3 and s4; the same counts
   are necessary for any two pairs. The failures s3=3 give 1j--23.
   The remaining four-element supports contained in [5] give precisely
   15--24, 15--34, and 25--34. Thus the excluded set is exactly T_n.
   The first-row restriction is automatic by Zhu's Corollary 24 since
   d=2<=a. The analogous one-row two-label argument excludes only 12
   in degree 1. The empty matching gives 1 in degree 0.

5. **All claimed term orders and the complete family.** The variable
   weights n^2-ij are positive, with minimum n. For quadratics they
   equal 2n^2 minus score. Every displayed straightening relation has
   unique largest-weight monomial t, so every refinement gives leading
   monomial t. Nonmatching quadratics vanish individually. The number
   of remaining degree-2 monomials equals the established quotient
   dimension, so there are no further degree-2 initial monomials.
   This Hilbert-function argument is valid for any monomial order on
   a homogeneous ideal, without requiring a degree-compatible order.
   In degree 1 the unique largest-weight term of L is y_12.
   For k=2, higher degrees vanish by the source ideal, so the stated
   union is the entire standard monomial basis. Its Hilbert series is
   1+(C(n,2)-1)q+(3C(n,4)-C(n,2))q^2. Its total size is 3C(n,4),
   which agrees with the size of the two-transposition class.

Independent exact computations are saved in `audit/referee-verification.json`
and can be reproduced with `python3 audit/referee_verify.py`. The script
imports none of the proposer's code and does not write frozen evidence.

- Graph verification covers n=6,7,8,9,10,12,15,20. It solves every column
  system by leaf removal and a five-cycle recurrence using integers for
  twice the coefficients, verifies each resulting incidence identity,
  and checks every nonzero coefficient's strict score inequality.
  The minimum margin is 1 in every tested case. This uses a different
  solver from the frozen matrix-inversion experiment.
- Literal inverse tableau verification covers every standard tableau
  for n=6,7,8,9,10 and each relevant even inner shape. The tableaux are
  generated by growing Young diagrams, then the strip and RSK operations
  are reversed. All selections are injective, equal the claimed sets,
  and satisfy the smallest admissible a>=2 first-row bound. Hence all
  admissible a>=2 for these n are covered in degrees 1 and 2.
- Fresh full permutation censuses and exact QQ evaluation ranks give
  graded dimensions through degree 2 of (1,14,30), (1,20,84), and
  (1,27,182) for (n,a)=(6,2),(7,3),(8,2). Candidate augmented ranks
  are 45,105,210, respectively, equal to the full filtered ranks.
  The n=6 calculation includes every original-coordinate monomial of
  degree at most 2, including diagonal, repeated, and overlapping
  products. The other two use all matching monomials together with
  the verified degree-preserving reduction of arbitrary coordinates.
- A fresh `pdftotext -layout` extraction of the frozen EJC PDF is
  byte-identical to its frozen text file (59,453 bytes). The proof's
  relevant definitions and source statements were read directly.

The frozen scripts and recorded results were also inspected; all six large
rank artifacts were parsed for their cases and coverage. Their higher-degree
rank assertions were not independently recomputed and are not needed for
this decision. Successful finite checks are supplementary evidence; the
uniform proof above is what supports the unbounded quantifiers.

The contribution and source comparison pass at this narrow scope. The
nearest problem source is Zhu's [EJC paper](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i2p54),
especially Section 2.5, Definition 5/Equation (4), Proposition 17,
Corollary 24, and the construction following Problem 29. Those passages
give the ideal, count, stability restriction, and candidate; they do not
prove this quadratic candidate or the specified weight order. The frozen
source and its interpretation accurately distinguish the original basis
problem from this particular subsidiary candidate.

The full matching-locus basis and fixed-class characters are prior results
of Liu--Ma--Rhoades--Zhu, Theorems 3.3 and 5.21, checked in the frozen
[primary v1 text](https://arxiv.org/html/2409.06175v1). Their
[published record](https://link.springer.com/article/10.1007/s00209-025-03736-4)
was also checked. Its publisher supplies a preview rather than the complete
article; attempted author-hosted PDF access failed, so no complete
version-of-record comparison is claimed.

The general rank of signless incidence matrices and its interpretation as
degree-1 Lefschetz multiplication are established in Dao--Nair,
[Proposition 3.1, Lemma 3.2, and Theorem 3.3](https://arxiv.org/html/2112.09434v4).
These primary statements were checked and apply in characteristic zero.
They already supply the incidence-rank method. The result-note must not
claim that criterion, the ideal presentation, or the Hilbert dimensions as
new contributions.

The review additionally checked the now-published primary source underlying
Zhu's cited ideal presentation: [Rook placements and orbit harmonics,
Appendix A, Proposition A.7](https://link.springer.com/article/10.1007/s00209-026-04090-9).
Its displayed generators and Proposition A.7 confirm the ideal equality;
Lemma A.3 confirms vanishing above k. This appendix supplies the prior
algebraic input, not the claimed tableau classification or product weights.
The July 2026 publication information should be used when preparing the
bibliography. The complete subscription main text was not inspected.

Fresh searches included combinations of "involution matrix loci" with
"monomial basis", "quadratic", "two transpositions", "Groebner", and
"standard monomial basis", together with Pieri/RSK and Kneser-graph
queries. Primary-domain searches covered arXiv, EJC, and author pages;
the related 2026 rook-placement publication was followed to its relevant
appendix. No equivalent of the exact accepted theorem was found in this
bounded screen as of 2026-09-14. Search results and unavailable source
versions do not establish absence or priority, and secondary summaries
were not used to assert a solution or an equivalent result.

The precise useful delta is the identification of the source's canonical
Pieri--RSK exclusions with this particular connected odd-cycle subgraph,
and the uniform strict comparison for the explicit product weights. This
proves a natural stable part of an existing candidate and gives a complete
normal-form basis for the infinite two-transposition family. That is a
coherent, modest result-note contribution, rather than just another proof
of the incidence-rank criterion or a table of successful small cases. The
classification and order comparison are additional arguments not supplied
by the inspected prior theorems. No separate notes should be split off for
the elementary dimensions or the already-known graph method.

No mathematical gap or counterexample was found in the frozen scope.
No substantive change to the claim or its proof is required for this
decision. The manuscript should retain all quantified restrictions, the
off-diagonal presentation, the convention that larger weight gives the
leading term, proper attribution, and bounded novelty language. The
original uniform construction and higher-degree basis/weight assertions
remain unresolved. Mathematical acceptance here does not certify a future
manuscript's citations, build, visuals, or publication readiness.
