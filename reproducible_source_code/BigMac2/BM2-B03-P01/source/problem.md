# Precise problem reading

## Provenance and frozen source

- Job: `bigMac-00003-p01-triage-bc510686615c`
- The authoritative original statement is `source.md`, whose SHA-256 at intake is
  `8bd964b5b75c92eacd0c227be016ba78920c6b599f27b2331de2cdea771f4e98`.
- This file records an interpretation; it does not amend the source.

## Quantified statement

For every fixed integer \(q\ge 2\) satisfying \(\gcd(q,6)=1\), and for every
fixed nonempty subset \(R\) of the additive cyclic group
\(G=\mathbb Z/q\mathbb Z\), define, for each positive integer \(N\),
\[
A_N=\{n\in\mathbb Z:1\le n\le N,\ [n]_q\in R\}.
\]
For every finite \(A\subset\mathbb Z\), define
\[
M(A)=\#\{(x,d)\in\mathbb Z^2:d\ne0,\ x,x+d,x+3d\in A\}.
\]
The claim to prove or refute is the conjunction:

1. the limit along positive integral \(N\) exists and satisfies
   \[
   L(q,R):=\lim_{N\to\infty}\frac{M(A_N)}{|A_N|^2}\le \frac13;
   \]
2. for each admissible pair \((q,R)\), equality \(L(q,R)=1/3\) holds if and
   only if there exist an additive subgroup \(H\le G\) and \(c\in G\) such
   that \(R=c+H\).

Thus the parameters \(q\) and \(R\) are held fixed before \(N\to\infty\).
The assertion is not a uniform-in-\(q\) error estimate.

## Counting conventions and boundary cases

- Dilations are signed and ordered: \((x,d)\) and \((x',d')\) are different
  unless both coordinates agree. Negative \(d\) is included.
- Only the integer \(d=0\) is excluded. Dilations with \(d\equiv0\pmod q\)
  but \(d\ne0\) remain included and contribute to the main term.
- Membership of all three displayed points in \(A_N\) supplies every interval
  boundary condition; there is no separate restriction on \(x\) or \(d\).
- Additive-subgroup cosets include singleton residue sets
  (\(H=\{0\}\)) and the full residue group (\(H=G\)).
- Nonemptiness of \(R\) ensures that the denominator is nonzero for all
  sufficiently large \(N\).

## Exact finite formulation suggested by triage

Put \(r=|R|\) and define the modular count
\[
T_q(R)=\#\{(u,v)\in G^2:u,u+v,u+3v\in R\}.
\]
Here \(v=0\) is deliberately included, since it represents all integer
dilations divisible by \(q\), not merely the forbidden dilation \(d=0\).
Residue-class lattice counting in the two triangles cut out by
\(1\le x,x+d,x+3d\le N\) should give
\[
|A_N|=\frac rqN+O_q(1),\qquad
M(A_N)=\frac{T_q(R)}{3q^2}N^2+O_q(N),
\]
because the two signed-dilation triangles have total normalized area \(1/3\).
Consequently the claimed limit is equivalent to
\[
L(q,R)=\frac{T_q(R)}{3r^2},\qquad T_q(R)\le r^2.
\]

There is an elementary candidate route for the finite inequality and equality
case.  The map \((u,v)\mapsto(u,u+v)\) sends every pair counted by \(T_q(R)\)
injectively into \(R^2\), so \(T_q(R)\le r^2\).  Equality is equivalent to
\[
3b-2a\in R\quad\text{for every }a,b\in R.
\]
After translating one element of \(R\) to zero, this says that a finite set
\(S\subset G\) containing zero is closed under \((x,y)\mapsto3y-2x\).
Since multiplication by \(3\) and by \(-2\) are bijections of \(G\) under
\(\gcd(q,6)=1\), this closure appears to force \(S\) to be an additive
subgroup; conversely every subgroup coset has the displayed closure.  This is
a candidate proof route, not yet an independently audited resolution.

## Source status, nearest inspected result, and proposed delta

The cited primary source is Samuel Korsky, *Affine Copies of Three-Point
Patterns in Sets of Integers*, arXiv:2609.02308v1
(https://arxiv.org/abs/2609.02308), inspected 2026-09-06.  Definitions (1.1)--
(1.2) on page 1 agree with the signed count above.  Equations (1.15)--(1.20)
and Theorem 1.4 on page 4 (PDF page index 3) identify the equation
\(2x+z=3y\), give interval density \(1/3\), and prove the general-set upper
coefficient \(47/122\).  The inspected paper does not state the present
fixed-modulus classification.

Triage classification is therefore **new-question / novelty-status-uncertain**,
not a verified open problem.  Nearest prior result \(X\): Korsky's general
\(47/122\) bound and the interval lower coefficient \(1/3\).  Proposed delta
\(Y\): the sharp \(1/3\) upper bound and exact equality classification for all
fixed admissible periodic residue sets.  Verification route \(Z\): rigorously
establish the modular asymptotic above and audit the finite closure argument.
