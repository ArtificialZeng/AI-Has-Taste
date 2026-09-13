# Builder notes: exact low-degree reductions

Role: proof builder (Gates 2--3).  This file deliberately distinguishes proved
statements from the two residual cases.  No floating-point experiment is used
in a proof below.

## 1. Normalizations and the boundary test

Multiplication of the polynomial by a nonzero scalar and precomposition by a
rotation preserve the assertion.  We may therefore put a self-inversive
polynomial in the Hermitian coefficient form

\[
        a_k=\overline {a_{n-k}}.                                      \tag{1.1}
\]

For even degree the middle coefficient is then real.  The particular
input/output rotations used below preserve the Hermitian convention and put
the selected pair in the stated phase; no broader arbitrary-phase claim is
needed.

Put \(\Omega=P(\mathbb D)\).  The following elementary test is repeatedly
used.

**Lemma 1 (boundary preimages; proved).**  If \(w\in\partial\Omega\), then
every zero of \(P-w\) has modulus at least one, and at least one zero has
modulus one.  Thus \(w=P(z)\) for some \(|z|=1\), and every zero of

\[
             \frac{P(x)-P(z)}{x-z}                                  \tag{1.2}
\]

has modulus at least one.

**Proof.**  A zero in \(\mathbb D\) would make \(w\) an interior point of
the image by the open mapping theorem.  If every zero had modulus strictly
greater than one, the finite root multiset has positive separation from the
unit circle, and that separation persists under sufficiently small changes
of \(w\) (equivalently, use Rouch\'e on \(|z|=1\)).  This would make \(w\)
an interior point of the omitted set.  Both alternatives
contradict \(w\in\partial\Omega\).  Dividing out a unit-modulus zero gives
the last assertion. \(\square\)

For later use, if \(w=0\) is a boundary point, (1.1) and Lemma 1 imply that
**all** zeros of \(P\) lie on the unit circle: an outside zero would have an
inside reciprocal-conjugate mate.  Consequently, unless all zeros of \(P\)
are unimodular, \(0\in\Omega\) and is not a boundary point.
Conversely, if all zeros are unimodular, then \(0\notin\Omega\) but radial
approach to any such zero shows \(0\in\partial\Omega\).

We use the following form of one step of the Schur algorithm.

**Lemma 2 (Schur reduction; proved).**  Let
\(H(y)=h_0+h_1y+\cdots+h_my^m\) have all its zeros in
\(\overline{\mathbb D}\).  If \(|h_0|<|h_m|\), then

\[
 {\mathcal S}H(y)=\frac{\overline {h_m}H(y)-h_0H^\#(y)}{y},\qquad
 H^\#(y)=\sum_{j=0}^m\overline {h_{m-j}}y^j,                         \tag{1.3}
\]

has degree \(m-1\) and all its zeros in \(\overline{\mathbb D}\).  If
\(|h_0|=|h_m|\), all zeros of \(H\) are unimodular and
\({\cal S}H\equiv0\).

**Proof.**  The product of the root moduli is \(|h_0/h_m|\).  If no root lies
on the unit circle, then \(|H^\#|=|H|\) there, and strict Rouch\'e comparison
of the two numerator terms in (1.3), followed by removal of the zero at the
origin, gives the result.  In the boundary case, move every unit-circle root
radially inward while keeping the leading coefficient fixed.  The strict
result applies to these approximants; coefficient convergence and continuity
of roots put every zero of the limiting transform in
\(\overline{\mathbb D}\).  Its leading coefficient
\(|h_m|^2-|h_0|^2\) is nonzero, so the degree remains \(m-1\).  Equality of
the product with one forces every root modulus to be one, and coefficient
reversal then shows that the numerator vanishes identically. \(\square\)

Finally, if a polynomial \(P\) has leading coefficient \(a_n\), then

\[
             B(a_0,|a_n|)\subset P(\mathbb D).                       \tag{1.4}
\]

Indeed, if \(|w-a_0|<|a_n|\), the product of the moduli of the roots of
\(P-w\) is \(|a_0-w|/|a_n|<1\).  This proves every case in which an endpoint
coefficient realizes \(A\).

In degree one, self-inversiveness says \(|a_0|=|a_1|=A\), and
\(P(\mathbb D)=B(a_0,A)\).  Thus degree one is settled with equality.

## 2. Degree two

**Theorem 3 (proved: \(n=2\)).**  Every self-inversive quadratic has the
required covering disk.

**Proof.**  In the normal form

\[
             P(z)=r+bz+rz^2,\qquad r>0,\quad b\in\mathbb R,           \tag{2.1}
\]

we may replace \(z\) by \(-z\) and assume \(b\ge0\).  If \(r\ge b\), use
(1.4).  If \(b\ge r\), then for \(|z|=1\)

\[
 z^{-1}\{P(z)-2r\}=b+r(z-z^{-1})=b+2ir\sin t,qquad z=e^{it}.       \tag{2.2}
\]

Thus \(|P(z)-2r|\ge b\) on the unit circle.  Moreover the two roots of
\(P(z)-2r=rz^2+bz-r\) have product \(-1\), and for \(b>0\) exactly one is
in \(\mathbb D\).  Rouché's theorem now gives
\(B(2r,b)\subset P(\mathbb D)\).  (The only degenerate value \(b=0\) was
already covered by \(r\ge b\).) \(\square\)

This proof also includes repeated and unimodular zeros.  It proves the target
constant, but does not claim that the displayed disk is always an inball.

## 3. Degree three

If an endpoint coefficient realizes \(A\), use (1.4).  Otherwise an exact
input/output rotation and scaling put the polynomial in the form

\[
             P(z)=\overline d+z+z^2+dz^3,qquad |d|\le1,             \tag{3.1}
\]

with \(A=1\).  For example, starting from the Hermitian form with positive
endpoint modulus and \(a_1=e^{i\phi}\), use
\(z=e^{2i\phi}u\) and multiply the output by \(e^{-3i\phi}\).

Let \(|z|=1\), \(w=P(z)\ne0\), and suppose \(w\in\partial\Omega\).  The
reciprocal of the quadratic in (1.2) is

\[
 H_z(y)=d+(dz+1)y+(dz^2+z+1)y^2.                                   \tag{3.2}
\]

Its zeros are in \(\overline{\mathbb D}\).  Its nominal leading coefficient
cannot vanish, since then the unreversed quotient in (1.2) would have the
zero \(0\in\mathbb D\), contrary to Lemma 1.  Direct expansion gives the
exact Schur identity

\[
       {\mathcal S}H_z(y)=\frac{P(z)}{z^2}\{1+(1+z)y\}.              \tag{3.3}
\]

The equal-product branch of Lemma 2 is impossible: it would make the left
side of (3.3) identically zero, whereas \(P(z)\ne0\).  Hence the reduced
linear polynomial is stable and Lemma 2 implies

\[
                         |1+z|\ge1.                                 \tag{3.4}
\]

Choose the principal \(t\in[-\pi,\pi]\) with \(z=e^{it}\).  Then (3.4)
means \(x=\cos(t/2)\in[1/2,1]\).  With

\[
                         C=\frac12+2\overline d,                    \tag{3.5}
\]

the \(d\)-terms in \(z^{-3/2}(P(z)-C)\) are purely imaginary, and hence

\[
\begin{aligned}
 |P(z)-C|
 &\ge 2\cos(t/2)-\tfrac12\cos(3t/2)\\
 &=\tfrac72x-2x^3\ge\tfrac32.                                      \tag{3.6}
\end{aligned}

The last cubic is concave on the interval at its only interior critical
point, so its minimum is the common endpoint value \(3/2\).

There remains the possible isolated omitted value \(w=0\).  If all zeros of
\(P\) are unimodular, Gauss--Lucas puts both roots of

\[
                         P'(z)=1+2z+3dz^2                            \tag{3.7}
\]

in \(\overline{\mathbb D}\).  Lemma 2 applied to (3.7) gives

\[
 |d|\ge\frac13,qquad |6\overline d-2|\le9|d|^2-1.                 \tag{3.8}
\]

Writing \(r=|d|\), the second inequality yields

\[
 \Re d\ge \frac{1+18r^2-27r^4}{8}.                                \tag{3.9}
\]

Since \(r\in[1/3,1]\),

\[
 |C|^2=\frac14+4r^2+2\Re d
 \ge\frac12+\frac{17}{2}r^2-\frac{27}{4}r^4
 \ge\frac{49}{36}.                                                 \tag{3.10}
\]

The last expression is concave as a function of \(r^2\), so it is enough to
check the two endpoints.  Equality in (3.10) is attained by
\(P=(1+z)^3/3\).

To verify that the center (3.5) is in the image, put

\[
 P_s(z)=s\overline d+z+z^2+sdz^3,
 \qquad C_s=\tfrac12+2s\overline d,
 \qquad 0\le s\le1.
\]

At \(s=0\), the equation \(P_0(z)=C_0\) has the root
\((\sqrt3-1)/2\) in the disk.  The number of roots of \(P_s-C_s\) in
\(\mathbb D\) is locally constant whenever no root lies on the unit circle
(including for small positive \(s\), where the third root enters from
infinity).  Thus loss of membership would have a first unit-circle crossing
and would make \(C_s\) a boundary value.  It cannot be a nonzero boundary
value by (3.6), and it cannot be zero: a zero boundary value would force all
roots to be unimodular, when (3.10), applied to \(sd\), would give
\(|C_s|\ge7/6\).  Hence \(C\in\Omega\).

**Theorem 4 (proved: \(n=3\)).**  In the non-endpoint normal form (3.1),

\[
                         B(C,1)\subset P(\mathbb D).                 \tag{3.11}
\]

Indeed every nonzero boundary point is at distance at least \(3/2\) from
\(C\), while the only possible zero boundary point is at distance at least
\(7/6\); a segment from \(C\) to an omitted point of the displayed disk
would have to meet the boundary inside it.  Together with (1.4), this
completely proves the covering assertion in degree three.  In fact the
non-endpoint proof gives \(B(C,7/6)\) when all roots are unimodular, and it
gives \(B(C,3/2)\) when they are not all unimodular.

## 4. Degree four: exact reduction and one residual stratum

After (1.1), write

\[
 P(z)=\overline d+\overline b z+c z^2+bz^3+dz^4,qquad c\in\mathbb R. \tag{4.1}
\]

Assume the endpoint is not maximal, scale so that

\[
       A=\max\{|b|,|c|\}=1,qquad |d|\le1.                          \tag{4.2}
\]

At a nonzero boundary value \(w=P(z)\), \(|z|=1\), the reciprocal of (1.2)
has coefficients

\[
 H_z=[d,\ dz+b,\ dz^2+bz+c,\ dz^3+bz^2+cz+\overline b].             \tag{4.3}
\]

Exact expansion of (1.3) gives

\[
 {\mathcal S}H_z=\frac{P(z)}{z^3}K_z,\qquad
 K_z=[b,\ bz+c,\ bz^2+cz+\overline b].                             \tag{4.4}
\]

Thus \(K_z\) is Schur-stable.  Put

\[
       u=bz,qquad S=c+u+\overline u\in\mathbb R.                   \tag{4.5}
\]

The leading coefficient of \(K_z\) is \(zS\), so stability first gives
\(|S|\ge|b|\).  A second Schur step has, up to unit phases, constant
coefficient \(cS+u^2\) and leading coefficient \(S^2-|b|^2\).  Hence

\[
        |cS+u^2|\le S^2-|b|^2.                                     \tag{4.6}
\]

The first reduction has exact degree two, so \(S\ne0\).  The reverse
triangle inequality in (4.6) gives

\[
 |c|\,|S|-|b|^2\le S^2-|b|^2,
 \quad\hbox{hence}\quad |S|\ge|c|.                                \tag{4.7}
\]

Combining the two bounds, \(|S|\ge A\).  Finally, on the unit circle,

\[
 z^{-2}\{P(z)-2\overline d\}
   = S+\bigl(dz^2-\overline d z^{-2}\bigr),                         \tag{4.8}
\]

and the term in parentheses is purely imaginary.  Therefore every nonzero
boundary point obeys

\[
                  |P(z)-2\overline d|\ge A.                         \tag{4.9}
\]

For completeness, use

\[
 P_s(z)=s\overline d+\overline b z+c z^2+bz^3+sdz^4,
 \qquad C_s=2s\overline d.
\]

At \(s=0\), \(P_0(0)=C_0\).  Exact degree gives \(d\ne0\), so
\(C_s\ne0\) for \(s>0\), and (4.9) prevents the first unit-circle crossing
that a loss of membership would require.  Thus
\(2\overline d\in\Omega\).  We obtain the following exact statement.

**Theorem 5 (proved partial degree-four theorem).**  If a self-inversive
quartic either has an endpoint coefficient of modulus \(A\), or has at least
one zero off the unit circle, then its image contains a disk of radius \(A\).
In the second case (4.9) gives explicitly

\[
                  B(2\overline d,A)\subset P(\mathbb D)             \tag{4.10}
\]

in the normalization (4.1).  If all roots are unimodular, the still-proved
statement is

\[
        B(2\overline d,A)\setminus\{0\}\subset P(\mathbb D).        \tag{4.11}
\]

For clarity, (4.11) follows because the endpoint homotopy first puts the
nonzero center \(2\overline d\) in the image, the punctured disk is path
connected, and (4.9) excludes every nonzero boundary point from it; Lemma 1
says that zero is the only boundary value not covered by (4.9).

Consequently the all-unimodular case is also solved whenever
\(2|d|\ge A\).

**Open builder gap Q4-U.**  The only case not closed by this argument is an
all-unimodular quartic with a non-endpoint maximum and \(2|d|<A\).  The model
\((1+z)^4/6\), for which \(A=1\), \(d=1/6\), shows that the puncture really
lies inside the disk in (4.10), although that particular polynomial does
contain a radius-one disk (center 1).  Thus simply ignoring the isolated
point is invalid.

## 5. Degree five: exact reduction and one residual stratum

Write

\[
 P(z)=\overline d+\overline b z+\overline c z^2+c z^3+bz^4+dz^5.    \tag{5.1}
\]

Assume \(|d|<A\), and scale so that
\(A=\max\{|b|,|c|\}=1\).  At a nonzero boundary value the first Schur
reduction of the reciprocal quotient is, up to the nonzero scalar
\(P(z)/z^4\),

\[
 K_z=[b,\ bz+c,\ bz^2+cz+\overline c,
          \ bz^3+cz^2+\overline c z+\overline b].                   \tag{5.2}
\]

Set

\[
 B=bz^{3/2},\qquad C=cz^{1/2},\qquad
 S=B+C+\overline C+\overline B\in\mathbb R.                         \tag{5.3}
\]

After a unit rotation of its variable and multiplication by a scalar,
\(K_z\) is

\[
       L(y)=B+(B+C)y+(B+C+\overline C)y^2+Sy^3.                     \tag{5.4}
\]

Stability gives \(|S|\ge|B|=|b|\).  The first Schur transform of (5.4) has
constant coefficient \(SC+B^2\) and leading coefficient
\(S^2-|B|^2\).  Exact degree gives \(S\ne0\), and therefore

\[
 |S|\,|C|-|B|^2\le|SC+B^2|\le S^2-|B|^2,
 \qquad |S|\ge|C|=|c|.                                             \tag{5.5}
\]

Thus \(|S|\ge A\).  On \(|z|=1\),

\[
 z^{-5/2}\{P(z)-2\overline d\}
  =S+\bigl(dz^{5/2}-\overline d z^{-5/2}\bigr),                    \tag{5.6}
\]

so every nonzero boundary point is at distance at least \(A\) from
\(2\overline d\).

**Theorem 6 (proved partial degree-five theorem).**  If a self-inversive
quintic either has an endpoint coefficient of modulus \(A\), or has at least
one zero off the unit circle, then its image contains a disk of radius \(A\).
For an all-unimodular quintic, the explicit homotopy

\[
 P_s(z)=s\overline d+\overline b z+\overline c z^2
       +cz^3+bz^4+sdz^5,
 \qquad C_s=2s\overline d,
\]

starts from \(P_0(0)=C_0\), and the nonzero-boundary estimate prevents a
first loss for \(s>0\).  Therefore the exact punctured inclusion is

\[
 B(2\overline d,A)\setminus\{0\}\subset P(\mathbb D).             \tag{5.7}
\]

Consequently the full radius-\(A\) disk follows when \(2|d|\ge A\).

**Open builder gap Q5-U.**  The remaining case is all roots unimodular, a
non-endpoint maximum, and \(2|d|<A\).  No numerical observation is asserted
as a theorem.  The exact reductions (5.2)--(5.6) show that this is solely an
isolated-puncture problem, not an uncontrolled external-boundary problem.

## 6. Equality and degeneracy audit

* Degree two: equality in (2.2) occurs at \(z=\pm1\); the product argument
  covers repeated roots and the endpoint tie \(b=r\).
* Degree three: the scalar lower bound used in (3.6) equals \(3/2\) at
  \(t=0\) and \(t=\pm2\pi/3\); equality in the modulus additionally requires
  the discarded imaginary part to vanish (in particular
  \(\operatorname{Im}d=0\) at those points).  Equality \(|C|=7/6\) in the
  isolated-hole estimate is attained by \((1+z)^3/3\).  Although Theorem 4
  states only the target radius one, the audited non-endpoint argument gives
  radius \(7/6\) in the all-unimodular case.
* Schur equal-product cases were not divided through: Lemma 2 separates them
  explicitly.  In (4.4) and (5.2), a nonzero boundary value and a nonzero
  interior maximal coefficient force the displayed reduced polynomial to
  have its stated exact degree.
* No compactness or generic simplicity assumption is used.  Boundary zeros,
  repeated zeros, and critical boundary preimages are included by the closed
  disk version of Lemma 2.
* No proof assistant was used.  The factor identities have been independently
  expanded symbolically in `src/builder_symbolic_checks.py`.
