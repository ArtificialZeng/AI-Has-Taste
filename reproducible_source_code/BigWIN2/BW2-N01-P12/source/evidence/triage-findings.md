# Bounded exact test and decision

Job: `newwin-00001-p12-triage-3ebebbace8a4`, 2026-09-12.
Decision: advance; candidate_kind=none; original_status=unresolved.

The source is a precise k=3 instance of the cited product conjecture.
No correction was required. The exact loops in `triage_symbolic.py`
enumerate 55 shape pairs: 14 have mu=0 and one is the maximal shape,
leaving 40 outside those two established k=3 families. The script evaluates
all 144 permutation pairs for each shape, 7,920 shape/permutation checks.

For each surviving pair it constructs the supports of L E_0 R and L E_1 R,
where L is the SE sigma-augmented matrix and R the NW pi-augmented matrix
from Definitions 4.12/4.23. In one-based notation E_0(t,t)=1 and
E_1(t+1,t)=1 for 1<=t<=3. The pivot positions in the two slices are
(sigma(pi(j)),j) and (sigma(pi(j)+1),j). A forbidden pivot excludes the
permutation pair. Otherwise h counts forbidden entries having nonempty
generic support, and the recorded exponent is inv(sigma)+inv(pi)-h.

Boolean support is intended to be exact here: each factor entry is 0, 1,
or a distinct variable; variables of the left and right factors are
disjoint. Two different intermediate indices cannot contribute the same
nonconstant monomial, and the permutation pivots allow at most one
constant term. Thus no characteristic-dependent cancellation should alter
support. The next pass must explicitly verify this implementation bridge
and the use of the cited counting theorem before promoting the observation.

All 55 computed integer coefficient vectors equal the corresponding
products of six q-integers. Coefficients in the JSON are in ascending degree.
It includes every surviving permutation pair, its inversion count, h,
and exponent. No finite-field evaluations or interpolation were used.

Selected checks:

- Empty shape: coefficient vector [1,5,13,23,30,30,23,13,5,1], 144 terms.
- lambda=(1,1,0), mu=(1,0,0): [1,5,11,14,11,5,1], 48 terms.
- Maximal shape: [1], one term.

These are exact finite symbolic observations from one implementation.
The output has not received an independent mathematical or computational
audit. It is not a resolution-paper candidate or a novelty certificate.
There is no manuscript.

Nearest prior result X: the established all-q permutation sum and two
known k=3 shape families. Proposed delta Y: a complete, reproducibly
certified k=3 product evaluation for all 55 shapes, covering the remaining
40. Verification route Z: check explicit entry polynomials and their
elimination against Corollary 4.19 and Theorem 4.29, then verify every
coefficient identity. This is a bounded and potentially nontrivial full
special-case contribution; publication value still needs assessment.

One next test: independently rebuild the 144 augmented pairs with explicit
sparse polynomials, verify their forbidden-entry elimination and exponent
histograms for all 55 shapes over arbitrary characteristic, and compare
against `triage_symbolic.json`. A discrepancy would invalidate the
computational bridge; a successful mathematical derivation would justify
preparing the exact original-claim candidate for fresh review.

Reproduction: `python3 evidence/triage_symbolic.py` from the project root.
