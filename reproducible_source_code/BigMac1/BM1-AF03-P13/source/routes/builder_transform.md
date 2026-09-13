# Proof-builder route: the Ehrhart transform and the radius-six disk

## Scope and outcome

This note uses only the stated Ehrhart transform, the proved fixed integer
roots and functional equation, and the new real-negative-rootedness of

\[
  h(z)=h^*(\mathbf w;z).
\]

It does **not** use any output of a counterexample-search route.  There are
two conclusions.

1. For a word of length (10), the complete non-fixed-root question reduces
   exactly from a degree-(24) polynomial in (t) to a degree-(5)
   polynomial in (y=(t+7)^2).  Its target disk is (|y|\le 36).
2. Palindromicity and real-negative-rootedness of (h), even together with
   integrality and actual lattice-polytopal realizability, do not by
   themselves imply the desired Ehrhart disk.  Thus the Braun--Jal theorem
   cannot close the conjecture without additional snake-specific input.

The second conclusion is an obstruction to a proposed proof method, not a
counterexample to the generalized-snake conjecture.

## 1. General shift, fixed factor, and parity reduction

Put

\[
 d=2m+4,\qquad r=m+4,\qquad s=m+1,
\]

so that (r) is the codegree and (s) is the degree of (h^*).  Let

\[
 A_m(t)=\prod_{j=1}^{m+3}(t+j),\qquad x=t+\frac r2.
\]

Theorem 2.9 of Lee--Vindas-Mel\'endez--Wang gives (A_m\mid L) and

\[
 L(t)=L(-r-t).
\]

Consequently

\[
 \ell(x):=L\left(x-\frac r2\right)
\]

is even.  Moreover,

\[
 a_m(x):=A_m\left(x-\frac r2\right),\qquad
 a_m(-x)=(-1)^{m+3}a_m(x).
\]

The quotient (q_m(x)=\ell(x)/a_m(x)) has degree (s=m+1), and exact
polynomial division plus the last two displays gives

\[
 q_m(-x)=(-1)^{m+1}q_m(x).
\]

Thus, with

\[
 \epsilon\equiv m+1\pmod 2,\qquad \epsilon\in\{0,1\},
\]

there is a real polynomial (R_m) of degree

\[
 \deg R_m=\left\lfloor\frac{m+1}{2}\right\rfloor
\]

such that

\[
 q_m(x)=x^\epsilon R_m(x^2).                                      \tag{1}
\]

The fixed roots have shifted coordinates

\[
 x=\frac r2-j,\qquad 1\le j\le r-1,
\]

and hence already satisfy

\[
 |x|\le \frac r2-1=\frac{m+2}{2}.
\]

For every (y\in\mathbb C), each square root (x^2=y) has

\[
 |x|^2=|y|.
\]

It follows from (1), without a numerical-root argument, that the original
closed-disk assertion is equivalent to

\[
  \text{every zero (y) of (R_m) satisfies }
  |y|\le \left(\frac{m+2}{2}\right)^2.                            \tag{2}
\]

Zeros at (x=0) supplied by the parity factor in (1) are automatically
inside the disk.

## 2. Exact length-10 factorization

For (m=10), one has (d=24,r=14,s=11) and (x=t+7).  The fixed factor is

\[
 A_{10}(x-7)=\prod_{j=1}^{13}(x-7+j)
            =x\prod_{j=1}^{6}(x^2-j^2).                           \tag{3}
\]

The quotient is odd and has degree (11).  Therefore there is a quintic

\[
 \widehat R(y)=\sum_{k=0}^{5} C_k y^k\in\mathbb Z[y]
\]

such that the following identity holds:

\[
 24!\,L(x-7)
 =x^2\prod_{j=1}^{6}(x^2-j^2)\widehat R(x^2).                     \tag{4}
\]

The factor (24!) is only a denominator-clearing normalization and has no
effect on roots.  In particular, the length-(10) endpoint is equivalent to

\[
 \boxed{\text{all five roots of \(\widehat R\), with multiplicity, lie in
 \(|y|\le36\).}}                                                  \tag{5}
\]

Equation (4) also exposes all forced multiplicities.  The root (x=0)
(that is, (t=-7)) has multiplicity at least two.  The roots
(x=\pm1,\ldots,\pm6) are the fixed integer roots; (x=\pm6), or
(t=-1,-13), are on the target boundary.  If (widehat R(0)=0), the
central multiplicity increases by an even number.  If
(widehat R(j^2)=0), the multiplicities at the corresponding fixed pair
(x=\pm j) increase.  No cancellation is possible in (4).

## 3. Incorporating real-negative-rootedness of (h^*)

Because (h) has degree (11), is palindromic with constant and leading
coefficient (1), and has only negative real roots, its reciprocal roots can
be paired.  There are (c_1,\ldots,c_5\ge0) such that

\[
 h(z)=(1+z)\prod_{i=1}^{5}\bigl((1+z)^2+c_i z\bigr).              \tag{6}
\]

Indeed, a reciprocal root pair (-a,-a^{-1}), (a>0), contributes

\[
 (z+a)(z+a^{-1})=(1+z)^2+(a+a^{-1}-2)z,
\]

and (a+a^{-1}-2\ge0).  The unpaired root is (-1).  Repeated roots,
including repeated roots at (-1), are allowed by taking repeated (c_i),
including (c_i=0).

Equivalently, write the gamma expansion

\[
 h(z)=\sum_{j=0}^{5}\gamma_j z^j(1+z)^{11-2j},\qquad
 \sum_{j=0}^{5}\gamma_j u^j=\prod_{i=1}^{5}(1+c_i u).             \tag{7}
\]

Thus (gamma_0=1), and the (gamma_j) are the elementary symmetric
functions of the nonnegative (c_i).  Exact expansion of

\[
 L(t)=\sum_{i=0}^{11}h_i\binom{t+24-i}{24}
\]

followed by division by (3) gives the following coefficient map.  The order
is from the constant coefficient to the leading coefficient:

\[
\begin{aligned}
C_0={}&16128(2740660\gamma _0-834491\gamma _1+356608\gamma _2
             -221256\gamma _3+214200\gamma _4-381150\gamma _5),\\
C_1={}&8(2175454336\gamma _0-452668640\gamma _1+118802560\gamma _2
          -34304036\gamma _3+192028\gamma _4+51208609\gamma _5),\\
C_2={}&2(786959360\gamma _0-82210048\gamma _1+2538752\gamma _2
          +5387408\gamma _3-3776812\gamma _4-5317285\gamma _5),\\
C_3={}&42(1160192\gamma _0+7424\gamma _1-20224\gamma _2
           +1568\gamma _3+5084\gamma _4+3203\gamma _5),\\
C_4={}&2(281600\gamma _0+35072\gamma _1-64\gamma _2
          -2224\gamma _3-1108\gamma _4-415\gamma _5),\\
C_5={}&2(1024\gamma _0+256\gamma _1+64\gamma _2
          +16\gamma _3+4\gamma _4+\gamma _5).
\end{aligned}                                                     \tag{8}
\]

This is an integer identity, not a fitted numerical relation.  It can be
reconstructed directly by expanding the six basis numerators in (7), using
the binomial-basis definition of (L), multiplying by (24!), and carrying
out exact division by (3).  As a quick independent check on the leading
coefficient, (8) gives

\[
 C_5=h(1)=\sum_{j=0}^{5}\gamma_j2^{11-2j},
\]

which is exactly the normalized-volume numerator required by the Ehrhart
transform.

The signs in (8) show why gamma nonnegativity alone is not a direct
coefficient proof of (5).

## 4. Exact obstruction: real-rootedness alone does not imply the disk

Take

\[
 h(z)=(1+z)^{11}.
\]

This polynomial is monic, integral, palindromic, and all eleven of its roots
are the negative real number (-1).  In (7), it corresponds to

\[
 (\gamma_0,\gamma_1,\ldots,\gamma_5)=(1,0,0,0,0,0).
\]

After removing the positive content (1024), (8) produces the primitive
quintic

\[
 R_0(y)=2y^5+550y^4+47586y^3+1537030y^2+16995737y+43165395.       \tag{9}
\]

Exact integer evaluation gives

\[
 R_0(-145)=-243867470<0,
 \qquad
 R_0(-144)=31803075>0.                                            \tag{10}
\]

Hence the intermediate value theorem supplies a real root
(y_0\in(-145,-144)).  The two corresponding roots of the Ehrhart quotient
are

\[
 x=\pm i\sqrt{-y_0},\qquad |x|>12>6.
\]

This is already an exact disproof of the implication

\[
 \text{palindromic and real-negative-rooted (h)}
 \Longrightarrow \text{radius-six Ehrhart disk}.
\]

The example is not merely a formal numerator.  Let
(C_{11}=\operatorname{conv}(\pm e_1,\ldots,\pm e_{11})).  Counting integer
vectors by their (\ell^1)-norm gives

\[
 \sum_{t\ge0}L_{C_{11}}(t)z^t=\frac{(1+z)^{11}}{(1-z)^{12}}.
\]

Each lattice-pyramid operation divides the Ehrhart series by (1-z) and
leaves (h^*) unchanged.  The thirteenth iterated lattice pyramid over
(C_{11}) is therefore a (24)-dimensional lattice polytope with Ehrhart
series

\[
 \frac{(1+z)^{11}}{(1-z)^{25}},
\]

exactly the dimension, (h^*)-degree, codegree, and Ehrhart transform used
above.  Thus even lattice-polytopal realizability is insufficient.  This
polytope is not asserted to be a generalized-snake order polytope.

## 5. Exact certification of the quintic disk

The following two-stage verifier is sufficient for each actual snake word.
It avoids floating-point roots completely.

### 5.1 Fast strict-interior branch: Schur reduction

Scale the disk to the unit disk by setting

\[
 p_0(z)=\widehat R(36z)=\sum_{k=0}^{5}C_k36^kz^k\in\mathbb Z[z].
\]

For a real polynomial (p(z)=\sum_{k=0}^{n}b_kz^k), with
(alpha=b_0) and (eta=b_n), put

\[
 p^\#(z)=z^np(1/z),\qquad
 \mathcal S(p)(z)=\frac{\beta p(z)-\alpha p^\#(z)}{z}.             \tag{11}
\]

The numerator in (11) has zero constant term.  The exact Schur reduction
says that all roots of (p) lie in (|z|<1) if and only if

\[
 \beta^2-\alpha^2>0
\]

and all roots of (mathcal S(p)) lie in (|z|<1).  Iterating (11) five
times therefore yields a compact strict certificate consisting only of five
integer coefficient vectors and five strict integer inequalities.  A
verifier must recompute every successor vector; it must not accept vectors
supplied only by discovery code.

If a difference (eta^2-\alpha^2) is zero, this branch is inconclusive.
Zero must not be interpreted as a certified boundary root: reciprocal
inside/outside pairs can also make a Schur step singular.  Since the target
disk is closed, every singular case must go to the next branch.

### 5.2 Closed-disk and boundary branch: Sturm/RUR isolation

First compute the exact square-free factorization

\[
 \widehat R=\prod_j f_j^{e_j}\quad\text{in }\mathbb Q[y].
\]

For each factor, isolate all real roots by a Sturm sequence.  Each isolating
interval must lie in ([-36,36]); exact evaluations at (36) and (-36)
separately classify real boundary roots.

For nonreal roots, write (y=u+iv), (s=v^2), and

\[
 \widehat R(y)=a_0+a_1y+\cdots+a_5y^5.
\]

For (v\ne0), the two equations
(operatorname{Re}\widehat R(u+iv)=0) and
(operatorname{Im}\widehat R(u+iv)=0) are exactly

\[
\begin{aligned}
E(u,s)={}&a_0+a_1u+a_2(u^2-s)+a_3(u^3-3us)\\
         &+a_4(u^4-6u^2s+s^2)
          +a_5(u^5-10u^3s+5us^2)=0,\\
F(u,s)={}&a_1+2a_2u+a_3(3u^2-s)+a_4(4u^3-4us)\\
         &+a_5(5u^4-10u^2s+s^2)=0,
\end{aligned}                                                     \tag{12}
\]

with (s>0).  A rational-univariate representation or a standard exact CAD
for (12) gives finitely many algebraic pairs ((u,s)).  For each pair, the
sign of

\[
 D(u,s)=1296-u^2-s                                             \tag{13}
\]

is determined exactly by Sturm--Tarski sign evaluation:

* (D>0): the conjugate pair is strictly inside;
* (D=0): the pair is on the allowed boundary;
* (D<0): the word is an exact counterexample.

A serialized certificate can consist of the square-free factors, a rational
univariate representation, rational isolating intervals for its primitive
element, and exact sign data for (s) and (13).  The independent verifier
must check the RUR identities modulo the defining polynomial, denominator
nonvanishing, all Sturm interval claims, and the degree count

\[
 \sum_j e_j\bigl(#\text{ real roots of }f_j
              +2\#\text{ nonreal conjugate pairs of }f_j\bigr)=5. \tag{14}
\]

Equation (14) is the fail-closed check against a missed repeated root or a
missed isolating box.  Applying the procedure factor by factor records the
algebraic multiplicity (e_j).  No floating-point approximation is part of
the certificate.

## 6. Boundary and multiplicity classification for the final endpoint

For an actual word, (5) proves the **closed** target disk.  The following
stronger classifications must not be conflated:

* If every root of (widehat R) has modulus strictly less than (36), the
  only boundary roots forced by the general theory are (x=\pm6), i.e.
  (t=-1,-13).
* A root (y) of (widehat R) with (|y|=36) produces two additional
  boundary roots (x^2=y), counted with the multiplicity of (y).
* If (y=0) has multiplicity (e), then (x=0) has multiplicity
  (2+2e) in (L(x-7)).  For nonzero (y) of multiplicity (e), each of
  its two square roots has multiplicity (e).  Overlap with one of the
  fixed values (y=j^2) adds to the simple multiplicity from (3).

Thus repeated roots and equality cases are completely visible after the
quintic reduction; none may be discarded as numerical tolerance events.

## 7. Proven endpoint of this route and remaining gap

Proved here:

* the general parity reduction (1)--(2);
* the exact length-(10) factorization (4) and quintic equivalence (5);
* the exact gamma-to-quintic map (8);
* the exact lattice-polytopal obstruction (9)--(10) showing that
  (h^*)-real-rootedness alone is insufficient;
* a finite exact Schur/Sturm/RUR certification route that handles strict
  interior roots, boundary roots, repeated roots, and failure cases.

Not proved here:

* that the quintics arising from all length-(10) generalized snake words
  satisfy (5);
* any snake-specific inequality on the (c_i) or (gamma_i) strong enough
  to imply the Schur inequalities uniformly;
* any reversal quotient (none was used in this note).

Accordingly, this proof-builder route is a rigorous structural reduction,
not by itself a proof of the finite universal endpoint.  No Lean, Coq,
Isabelle, or other proof assistant was used.
