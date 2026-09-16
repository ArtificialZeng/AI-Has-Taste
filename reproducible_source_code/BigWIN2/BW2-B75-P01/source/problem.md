# Precise problem reading

## Frozen statement

The immutable input is `source.md` (SHA-256
`4e6e2e3de083a5cf9118c7523491bdbd8f9ab1396f841a238fe0ef2e5f8061e1`).
No correction or weakening is proposed.

For every integer \(m\geq 1\), put \(q=2^m\).  Let
\(\mathbb F_q\) be the unique field of order \(q\), let
\(\mathbb F_{q^2}\) be its quadratic extension, and put
\[
 U_{q+1}=\{x\in\mathbb F_{q^2}^{\times}:x^{q+1}=1\}.
\]
For each coefficient \(a\in\mathbb F_q\), define the number of **distinct**
roots
\[
 N_m(a)=\#\{x\in U_{q+1}:x^7+a x^4+a x^3+1=0\},
\]
and, for \(j\in\{1,3,5\}\), define
\[
 M_j(m)=\#\{a\in\mathbb F_q:N_m(a)=j\}.
\]
Define the integer sequence for all \(m\geq1\) by
\[
 c_1=1,\qquad c_2=-3,\qquad
 c_m=c_{m-1}-2c_{m-2}\quad(m\geq3),
\]
and set \(d_m=-2+(-1)^m+c_m\).  The claim to prove or disprove is the
simultaneous universal assertion
\[
 M_5(m)=\frac{q+d_m}{8},\qquad
 M_3(m)=\frac{q-d_m}{4},\qquad
 M_1(m)=\frac{5q+d_m}{8}
 \quad\text{for every }m\geq1.
\]
The scope is only the coefficient slice \(a\in\mathbb F_q\), not coefficients
in all of \(\mathbb F_{q^2}\).  The claim concerns cardinalities of root sets,
so multiplicities are not counted.

## Exact reduction

For \(a\in\mathbb F_q\), characteristic two gives
\[
x^7+a x^4+a x^3+1=(x+1)
 (x^6+x^5+x^4+(a+1)x^3+x^2+x+1).
\]
Thus \(x=1\) is always a root.  If \(x\in U_{q+1}\setminus\{1\}\), set
\(y=x+x^{-1}\).  Then \(y\in\mathbb F_q^\times\), and division of the
second factor by \(x^3\) shows that it vanishes exactly when
\[
 y^3+y^2=a+1.
\]
The map \(x\mapsto x+x^{-1}\) is two-to-one from
\(U_{q+1}\setminus\{1\}\) onto
\[
 S_m=\{y\in\mathbb F_q^\times:
       \operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(1/y)=1\}.
\]
Indeed, its inverse fibre is the pair of roots of
\(X^2+yX+1\); this quadratic is irreducible over \(\mathbb F_q\) precisely
when \(\operatorname{Tr}(1/y^2)=\operatorname{Tr}(1/y)=1\), and its two
conjugate roots then have norm one.

Put
\[
 R_m(a)=\#\{y\in S_m:y^3+y^2+1=a\}.
\]
Then \(N_m(a)=1+2R_m(a)\).  Moreover \(R_m(a)\leq2\): if three distinct
nonzero roots exhausted \(Y^3+Y^2+(a+1)\), then (unless \(a+1=0\), when
there is only one distinct nonzero root) their reciprocal sum would be zero.
Taking absolute traces would give \(1+1+1=0\) in \(\mathbb F_2\), a
contradiction.  Consequently \(N_m(a)\in\{1,3,5\}\) for every coefficient.

There is a single decisive counting target.  Let \(D_m\) be the number of
ordered pairs \((y,z)\in S_m^2\) with \(y\ne z\) and
\(y^3+y^2=z^3+z^2\).  Equivalently,
\[
 D_m=\#\{(y,z)\in(\mathbb F_q^\times)^2:y\ne z,
 y^2+yz+z^2+y+z=0,\ \operatorname{Tr}(1/y)=
 \operatorname{Tr}(1/z)=1\}.
\]
Since \(|S_m|=q/2\), the three proposed formulas are jointly equivalent to
\[
 D_m=\frac{q+d_m}{4}
     =\frac{q-2+(-1)^m+c_m}{4}.
\]
Indeed \(D_m=2M_5(m)\), while
\(M_3(m)+2M_5(m)=q/2\) and
\(M_1(m)+M_3(m)+M_5(m)=q\).

## Literature boundary and proposed delta

The nearest inspected primary source is M. Xiong and H. Yan, *The
Cross-Correlation Distribution of the Niho-Type Decimation
\(d=4(2^m-1)+1\)*, arXiv:2609.04683v1 (retrieved 2026-09-09),
https://arxiv.org/abs/2609.04683.  Its PDF p.16, Theorem 18 and equation (6),
sets \(a\in\mathbb F_{q^2}\) and uses
\(x^7+a x^4+\bar a x^3+1\); Theorems 22 and 26 give parts of the resulting
distribution over all \(q^2\) coefficients.  Those statements do not give
the conditional distribution on the fixed subfield \(a=\bar a\in\mathbb F_q\).
Exact-assertion and equivalent-form searches located no separate primary
source for that subfield distribution.  This is only a bounded search result,
not evidence of openness or priority, so the source status is
`status-uncertain` / apparently a new conditional question.

Nearest prior result X: the full \(\mathbb F_{q^2}\)-coefficient distribution
in Xiong--Yan.  Proposed delta Y: the exact \(\mathbb F_q\)-coefficient slice
above.  Verification route Z: evaluate \(D_m\) by an exact additive-character
or Artin--Schreier curve count, including diagonal, zero, pole, and points at
infinity, and determine whether the remaining Frobenius trace is the sequence
\(c_m\).
