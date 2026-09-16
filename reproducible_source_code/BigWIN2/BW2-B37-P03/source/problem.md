# Precise problem reading

## Frozen source and provenance

The immutable source is `source.md` (SHA-256
`1a82944067ef730d97a127bb6727cf78951aa8e5e875521b03a2d9ba06777180`).
This reading was prepared for job `win-00037-p03-triage-221ec2e0ffd8`.

## Quantified statement

Decide the truth of

\[
\exists (x_1,\ldots,x_{18})\in\mathbb Q^{18}\quad
\text{such that}\quad
\sum_{j=1}^{18}x_j^2=9,
\quad\sum_{j=1}^{18}x_j^4=\frac{27}{4},
\quad\sum_{j=1}^{18}x_j^6=\frac{45}{8}.
\]

A positive answer requires one displayed 18-tuple of rational numbers and exact
rational verification of all three sums. A negative answer requires a proof
excluding every ordered tuple in \(\mathbb Q^{18}\).

The coordinates need not be distinct or nonzero, and repetitions and arbitrary
signs are allowed. No condition \(|x_j|<1\) is imposed. (The equations themselves
give the weaker bound \(|x_j|\leq(45/8)^{1/6}\).) Permuting coordinates or changing
individual signs preserves the system. If \(y_j=x_j^2\), then each \(y_j\) must be
a square in \(\mathbb Q\); solving only for arbitrary nonnegative rational
\(y_j\) would not settle the source problem.

The normalized target moments are \(1/2,3/8,5/16\), the second, fourth, and
sixth moments of the arcsine/Chebyshev probability measure on \([-1,1]\).
Nevertheless, the source asks only for these three even moments. It does not
require odd-moment exactness, nodes in \([-1,1]\), distinct nodes, or a strict
Chebyshev design.

## Exact equivalent formulations and first construction target

Writing \(T_3(t)=4t^3-3t\), the three equations are equivalent to

\[
\|x\|^2=9,\qquad \langle x,T_3(x)\rangle=0,\qquad
\|T_3(x)\|^2=9,
\]

where \(T_3\) is applied coordinatewise. This follows by expanding the last two
identities, and the implication is reversible.

A sufficient, deliberately restricted construction is to partition the 18
coordinates into nine rational pairs \((a_i,b_i)\) satisfying
\(a_i^2+b_i^2=1\). Then all three source equations hold exactly if and only if

\[
\sum_{i=1}^9(a_i b_i)^2=\frac98.
\]

Thus rational Pythagorean pairs provide a bounded exact first search. Failure of
this restricted ansatz would not imply nonexistence for the original system.

## Status and nearest literature located in triage

Source status: **status-uncertain**. The source reports that its bibliography row
38 proves nonexistence for the analogous 17-variable system, but that bibliography
record is not present in the project, so the claim was not independently verified
in this job.

Searches on 2026-09-06 for the exact constants and for rational Chebyshev-type
degree-seven quadrature found no primary source settling this rational 18-variable
system. This is a search result, not proof that the question is new or open.
Relevant background inspected:

- S. Gilboa and R. Peled, *Chebyshev-type Quadratures for Doubling Weights*,
  arXiv:1507.01505, especially Introduction, equations (1)--(2) and the discussion
  of the Jacobi case \(\alpha=\beta=-1/2\):
  <https://arxiv.org/abs/1507.01505>. It defines equal-weight quadrature and notes
  classical real-node existence for the Chebyshev weight, but does not impose
  rational nodes or settle the displayed system.
- R. Peled, *Simple Universal Bounds for Chebyshev-Type Quadratures*,
  arXiv:0903.4625, Introduction and Section 2.1:
  <https://arxiv.org/abs/0903.4625>. It treats general real equal-weight moment
  matching and does not settle rational-node existence here.

## Triage target

Nearest supplied result: claimed nonexistence for 17 variables (verification
pending). Proposed delta: decide the unrestricted 18-variable rational system,
preferably by an exact construction. Verification route: exact substitution for
a solution, or a complete arithmetic obstruction for nonexistence. The cheapest
next discriminating test is an expanded exact search/parametrization of the
nine-unit-circle-pair condition above.
