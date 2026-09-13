# Precise problem statement

## Frozen reading of the two assertions

Let \(s\in\mathbb N\). A labelled finite moment system is a family
\[
(p_i,t_i,z_i)_{i=1}^s
\]
such that
\[
p_i>0,\qquad \sum_{i=1}^s p_i=1,\qquad
t_i,z_i\in\mathbb C,\qquad |t_i|=1,
\]
and
\[
\sum_{i=1}^s p_it_i=0,\qquad
\sum_{i=1}^s p_iz_i=0,\qquad
\sum_{i=1}^s p_i\overline{t_i}z_i=0.
\]
No pairwise-distinctness of the labelled atoms \((t_i,z_i)\) is assumed. Define
\[
E=\sum_{i=1}^s p_i|z_i|^2\ge 0.
\]

A probability vector on these labels means
\[
q=(q_1,\ldots,q_s)\in\Delta_{s-1}
 :=\{q_i\ge0:\textstyle\sum_iq_i=1\},
\qquad \operatorname{supp}q:=\{i:q_i>0\}.
\]
For such \(q\), put
\[
\mu(q)=\sum_iq_it_i,\qquad
\nu(q)=\sum_iq_iz_i,\qquad
\lambda(q)=\sum_iq_i\overline{t_i}z_i.
\]
Call \(q\) admissible when \(|\mu(q)|<1\). Then
\(D(q):=1-|\mu(q)|^2>0\), the defining matrix is invertible, and
\[
a(q)=\frac{\nu(q)-\mu(q)\lambda(q)}{D(q)},\qquad
b(q)=\frac{\lambda(q)-\overline{\mu(q)}\nu(q)}{D(q)},
\]
so, equivalently,
\[
C(q)=|a(q)|^2+|b(q)|^2
=\frac{|\nu-\mu\lambda|^2+|\lambda-\overline\mu\nu|^2}
       {(1-|\mu|^2)^2}.
\]

The source is read literally as the conjunction of these two independent universal assertions:

1. **Five-atom / three-point assertion.** For every integer \(s\) with
   \(1\le s\le5\), and every labelled moment system of size \(s\), there
   exists an admissible probability vector \(q\) with
   \[
   |\operatorname{supp}q|\le3,
   \qquad C(q)\le\frac58E.
   \]
2. **Six-atom / four-point assertion.** For every integer \(s\) with
   \(1\le s\le6\), and every labelled moment system of size \(s\), there
   exists an admissible probability vector \(q\) with
   \[
   |\operatorname{supp}q|\le4,
   \qquad C(q)\le\frac14E.
   \]

The existential quantifier is part of the frozen claim. In particular, it is
not silently replaced by the weaker statement
\(\inf_{q\ \mathrm{admissible}} C(q)\le cE\): the admissible set is open along
\(|\mu|=1\), so equality of an infimum can in principle occur only as a
nonattained boundary limit.

If only one assertion is proved or disproved, that conclusion is a local
result about that assertion alone. Neither assertion, separately or together,
is to be represented as a resolution of the full seven-atom formulation of
Conjecture 7.8.

## Boundary cases and normalizations

- The condition \(\sum_i p_it_i=0\) rules out a one-direction system and
  guarantees that an admissible probability vector exists: positive weight on
  any two distinct directions gives \(|\mu|<1\). Thus an empty admissible
  domain is not a counterexample. (Consequently no size-one moment system
  actually satisfies the hypotheses.)
- If \(E=0\), positivity of every \(p_i\) forces every \(z_i=0\). Then
  \(C(q)=0\) for every admissible \(q\), so both assertions are trivial.
  Research may therefore restrict the nontrivial branch to \(E>0\), and the
  homogeneity \(z_i\mapsto cz_i\) permits the normalization \(E=1\).
- A disproof of either assertion requires an exact admissible moment system in
  the stated size range and a proof that every admissible \(q\) within the
  support budget violates the stated inequality. Numerical optimization alone
  is not such a proof.

## Nearest verified source result and proposed delta

The cited primary source is Guangjian Zhang, *Exact Recovery Thresholds for
Weighted Data Selection in Vector-Valued Linear Regression*,
arXiv:2608.30254v1 (31 August 2026), Section 7:
<https://arxiv.org/html/2608.30254v1> (inspected 6 September 2026).

Its Conjecture 7.8 is stated using infima over admissible selections and asks
for the constants \(5/8\) at support budget three and \(1/4\) at support budget
four for all finite moment systems. Proposition 7.9 reduces those infimum
claims to at most seven atoms. Section 7.6.5 records the already covered finite
layers: the three-point inequality for at most four atoms (indeed \(C\le E/2\)
in infimum form), and the four-point inequality for at most five atoms (indeed
\(C\le2E/9\) in infimum form), together with special classes.

Thus the proposed local deltas are:

- extend the three-point result from \(s\le4\) to \(s=5\), while resolving the
  literal attainment requirement above;
- extend the four-point result from \(s\le5\) to \(s=6\), again resolving
  attainment rather than merely a boundary infimum.

Until the attainment issue is proved equivalent to the source's infimum
formulation, the frozen assertions should be classified as strengthened local
questions whose status is unresolved, not as verbatim subcases already posed
by Conjecture 7.8.
