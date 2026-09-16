# A six-letter counterexample to the multiset interlacing assertion

Research candidate, 2026-09-13. No fresh referee acceptance is asserted.

## Statement and relation to the original

Use Alexandersson--Jal--Quemener (AJQ), *Real-rootedness of rook-Eulerian
polynomials*, arXiv:2502.05939v1, Definitions 5, 8, 9 and Section 3.3.
The complete primary text is archived, byte for byte, in
`evidence/external/ajq-2502.05939v1.html`. The original assertion remains
unchanged in `source.md`, with its precise reading in `problem.md`.

For a nondecreasing row-length sequence lambda and fixed content alpha,
let W(lambda,alpha) consist of words w of that content satisfying
1 <= w_r <= lambda_r. Write asc(w) for the number of indices
1 <= r < n with w_r < w_(r+1). There is no endpoint sentinel. Define
R_j(t) as the sum of t^asc(w) over such words whose first letter is j,
and R(t) as the sum over all such words.

**Counterexample.** For

    lambda = (3,3,3,3,4,4),   alpha = (2,2,1,1),

the descending first-entry sequence (R_3,R_2,R_1) is not interlacing in
AJQ's Definition 9. Thus the second clause of AJQ Conjecture 28 is false,
which disproves the frozen conjunction of its two clauses. The universal
real-rootedness of the total polynomial is not decided by this result.
In this particular example, all three refinements and the total are
real-rooted.

## Verification of hypotheses and completeness

There are n=6 rows and k=4 letters. The row lengths are positive and
nondecreasing, the content has positive integer entries summing to 6, and
the board is a left-justified Ferrers board with no removed cells. There
are different row lengths and repeated letters, so it is neither the
rectangular nor the distinct-letter case. Columns may contain multiple
rooks under the multiset definition. A staircase restriction lambda_r>=r
from the nonattacking setting is not part of this definition; AJQ's own
Examples 25 and 26 use lambda=(2,2,2,3,3). All refinements used below
are nonzero, so no zero-polynomial convention affects the counterexample.

The unique letter 4 must occupy position 5 or 6. Deleting it leaves a
permutation v of 11223. Conversely, each such v gives exactly two legal
words, v_1 v_2 v_3 v_4 4 v_5 and v_1 v_2 v_3 v_4 v_5 4. This construction
is invertible, since the inserted 4 is unique. There are

    5 * binomial(4,2) = 30

bases: choose the position of 3, then the two positions of 1; the other
two positions contain 2. Thus the construction covers exactly 60 legal
words without duplication. There are 12 bases starting with 1, 12 starting
with 2, and 6 starting with 3, giving 24, 24 and 12 refined words.

## Exact enumeration

The accompanying `evidence/research-base-insertions.tsv` lists every one
of the 30 bases and the ascent counts for both insertions. The counts can
also be checked from the formulas

    asc(v_1 v_2 v_3 v_4 4 v_5)
       = 1 + sum_{r=1}^3 [v_r < v_(r+1)],
    asc(v_1 v_2 v_3 v_4 v_5 4)
       = 1 + sum_{r=1}^4 [v_r < v_(r+1)].

Here [P] is 1 if P holds and 0 otherwise. The first formula follows because
v_4<4 and 4>v_5; the second because v_5<4. Grouping the complete table gives:

| First letter | 4 in position 5 | 4 in position 6 |
| --- | --- | --- |
| 1 | 5t^2+7t^3 | 2t^2+8t^3+2t^4 |
| 2 | t+9t^2+2t^3 | 6t^2+6t^3 |
| 3 | 2t+4t^2 | t+4t^2+t^3 |

Therefore, by addition and factorization,

    R_3(t) = t^3+8t^2+3t = t(t^2+8t+3),
    R_2(t) = 8t^3+15t^2+t = t(8t^2+15t+1),
    R_1(t) = 2t^4+15t^3+7t^2 = t^2(t+7)(2t+1).

The standard-library-only verifier `evidence/research-verify-six-letter.py`
generates the bases by these position choices. As a separate domain check,
it visits all 6! labeled orders, erases equal-letter labels, and filters
the row restrictions. The resulting sets agree. The verifier also checks
every word, first letter and ascent count in the inherited 60-row
`evidence/six-letter-words.tsv`, without rewriting that file. It imports
neither earlier enumerator. The symbolic root argument below, not a
program Boolean or a floating-point approximation, proves failure.

## Exact root obstruction

For f preceq g, AJQ Definition 8 orders roots a_i of f and b_i of g
in descending order, with multiplicity, and requires

    ... <= a_3 <= b_3 <= a_2 <= b_2 <= a_1 <= b_1 <= 0.

It permits deg(g)=deg(f) or deg(g)=deg(f)+1. In the latter case the
smallest root of g must be no greater than the smallest root of f.
Definition 9 requires f_i preceq f_j for every pair i<j in the sequence,
so Conjecture 28's displayed sequence requires R_3 preceq R_1.

The roots, with multiplicity, are

    roots(R_3) = {-4-sqrt(13), -4+sqrt(13), 0},
    roots(R_1) = {-7, -1/2, 0, 0}.

Both have positive leading coefficient and only nonpositive real roots;
3 < sqrt(13) < 4. Their degrees are 3 and 4, respectively. But

    minroot(R_3) = -4-sqrt(13) < -7 = minroot(R_1),

where the strict inequality follows from 13>3^2. This contradicts the
necessary first inequality for R_3 preceq R_1. Hence (R_3,R_2,R_1) is
not an interlacing sequence. The remaining refinement is itself
real-rooted: its nonzero roots are (-15 +/- sqrt(193))/16, both negative
since 0<193<15^2. Thus this is a root-order failure even though each
individual refinement is real-rooted.

## The total in the witness is real-rooted

Summing the three refinements gives

    R(t) = 2t^4+24t^3+30t^2+4t = 2t q(t),
    q(t) = t^3+12t^2+15t+2.

The following exact integer values suffice:

| x | -11 | -10 | -2 | -1 | 0 |
| --- | --- | --- | --- | --- | --- |
| q(x) | -42 | 52 | 12 | -2 | 2 |

The intermediate value theorem gives a root in each of the three disjoint
intervals (-11,-10), (-2,-1), and (-1,0). Since q has degree three, these
exhaust its roots, each simple and negative. Also q(0)=2, so the additional
root 0 of R is simple. This establishes the advertised scope limitation
without relying on a computer algebra root-isolation routine.

## Dependencies and limits

The mathematical argument uses only the cited definitions, complete finite
counting, factorization, the inequality 13>9, and the intermediate value
theorem for the optional total-polynomial check. No known mathematical gap
remains in this fixed-witness argument. No result about minimal size, larger
search ranges, the earlier joint-content induction, or the truth of the
universal total real-rootedness clause is included. The triage census is
not a dependency. The candidate is a disproof of a conjunction by a false
conjunct, not a claim that both conjuncts are false.

Current primary-source comparisons and bounded priority limitations are
recorded in `literature/research-screen-20260913.md`. Novelty and exact scope
remain subject to the runner's fresh referee. No manuscript was prepared.
