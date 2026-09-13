# Inward-\(Z\) affine-omega sheet: exact source-certificate candidate

Date: 2026-08-25. Status: **exact source candidate, pending a genuinely
independent definition-level referee**. This file records a discovery and
source certificate only. It does not modify the frozen v12 result, any
ledger, manuscript, release, or submission package.

## 1. Literal candidate and seam

Keep

```text
0<S<=1/10000,                 3/13<=X<=1/4,
|M|<=1/1000,                 |omega|,|nu|<=1/100,
A=1+M,                       lambda=A/S,
y0=12/(25A)+nu,
omega_phys=omega-(10636/275)(X-1/5),
b=(45M+18)/(25A)-(3/5)X+omega_phys,
x=-1/5+X,                    y=3/5+S*y0,
Z=3X-X^2-3(X-3/13)+S*b-S^2*y0^2.
```

Equivalently,

\[
 Z=\frac9{13}-X^2+Sb-S^2y_0^2.
\]

At \(X=3/13\), the new term \(-3(X-3/13)\) vanishes identically.
Thus this candidate has an exact parameter-by-parameter seam with the frozen
v12 affine-omega sheet at its right endpoint. The claim is about a second
sheet joined along that seam, not one enlarged global chart.

## 2. Reconstruction from the original gate

The source program starts from the compact-ball transverse frame, constructs
the signed-\(z\) compression, \(H=UCU^*\), \(Q=\lambda H\), and every
entry of \(Q^2\). It evaluates the literal fully conjugated scalar

\[
\begin{aligned}
 \Gamma(Q)={}&4a^2\xi_2\overline{\xi_2}
 +\bigl(c\overline{\xi_1}+a\xi_3
       +i(ac-(Q^2)_{31})\bigr)
  \overline{\bigl(c\overline{\xi_1}+a\xi_3
       +i(ac-(Q^2)_{31})\bigr)}\\
 &+\bigl(c\overline{\xi_2}-i(Q^2)_{32}\bigr)
  \overline{\bigl(c\overline{\xi_2}-i(Q^2)_{32}\bigr)}
 -32a^2(\operatorname{Re}\xi_1)^2,
\end{aligned}
\]

where \(\xi=Qp\), and separately reconstructs the same expression by a
reordered Gram-vector formula. The two expressions agree exactly before the
candidate map is substituted. The signed lift is retained by checking the
compression modulo \(z^2-Z\); both signs give the same \(Z\)-dependent gate.

## 3. Exact legality on the continuum

On the complete parameter box,

\[
 -\frac{69948}{50875}\le b\le-\frac{299011}{500500}<0,\qquad
 \frac{46999}{100100}\le y_0\le\frac{16333}{33300}.
\]

The monotonic directions are checked symbolically. They give

\[
 \frac{9984760329129934873}{15857127000000000000}
 \le Z<\frac{108}{169}<1.
\]

Writing \(T=(6/5)y_0+b\), the old affine sheet has
\(T_{\max}(3/13)=-1/100\), and \(T\) strictly decreases with \(X\).
The new inward displacement changes danger to

\[
 D=1-x^2-y^2-Z
   =\frac25\left(X-\frac3{13}\right)-ST
 \ge\frac25\left(X-\frac3{13}\right)+\frac S{100}>0.
\]

Also \(A\ge999/1000\), hence \(\lambda=A/S>0\), and

\[
 \det C=\frac59SZ>0.
\]

Thus every datum is strictly dangerous and rank-two legal, for both signed
\(z\) lifts.

## 4. Exact 72-node falsification gate

The program evaluates the original rational raw gate at

```text
S in {1/1000000, 1/20000, 1/10000},
X in {3/13, 25/104, 1/4},
(M,omega,nu) at all eight centered corners.
```

All 72 points are legal and have \(36\Gamma>0\). The smallest gate value is

\[
 \frac{
 182249907370437372958214245586018359494715888079}
 {16726464040000000000000000000000000000000000}>0
\]

at

```text
(S,X,M,omega,nu)=(1/10000,3/13,-1/1000,1/100,-1/100).
```

The smallest nodal danger is \(10^{-8}\), at the \(X=3/13\) seam and
smallest tested scale. These 72 values are falsification tests, not the
continuum proof.

## 5. Exact continuum Bernstein source certificate

Let \(G=36\Gamma\). Sparse substitution into the definition-level gate gives

\[
 \hat Q=(25A)^8S^3G.
\]

Unlike v12, the inward displacement changes the asymptotic leading order:
the cleared polynomial has minimum \(S\)-degree zero, so the old global
\(S^2\) cancellation must not be asserted. The new normalized quotient has
32 \((S,X)\) terms, bidegree \((7,4)\). It is split exactly as

\[
 \hat Q=
 S^3 25^8M^2A^8(5M^2+14M+14)+Q_{\mathrm{core}},
\]

where

\[
 5M^2+14M+14=5\left(M+\frac75\right)^2+\frac{21}{5}>0.
\]

The remainder still has 32 \((S,X)\) coefficients and 1,581 centered
\((M,\omega,\nu)\) monomials. Use the lossless rectangle enlargement

\[
 X=\frac3{13}+\frac{u}{52},\qquad
 S=\frac{13}{30000}\tau X,\qquad 0\le u,\tau\le1.
\]

Because \(S/X\le(1/10000)/(3/13)=13/30000\), this covers the
physical box. The tensor Bernstein degree of \(Q_{\mathrm{core}}\) is
\((7,9)\), giving 80 controls. Exact centered arithmetic on the original
radii proves:

- controls \((0,0),(0,1),(1,0)\) are identically zero polynomials;
- all other 77 lower controls are strictly positive;
- the smallest strict lower is control \((2,0)\), with reserve

\[
 R_*=\frac{
 10071067674014002577317165966399410637259618083}
 {128416777961472000000000000000000000000000000}>0.
\]

The three zeros lie only in the artificial \(\tau=0\) closure. On the
physical domain \(S>0\), hence \(\tau>0\), the total Bernstein weight of
the rows \(i\ge2\) is exactly

\[
 W(\tau)=1-(1-\tau)^7-7\tau(1-\tau)^6
 =\sum_{i=2}^7\binom7i\tau^i(1-\tau)^{7-i}>0.
\]

For \(0<\tau<1\), its \(i=2\) summand is strictly positive; at
\(\tau=1\), \(W(1)=1\). Summing over the \(u\)-Bernstein basis gives

\[
 Q_{\mathrm{core}}\ge R_*W(\tau)>0.
\]

The first layer is nonnegative and the clearing factor \((25A)^8S^3\) is
strictly positive. This is an exact source-level continuum positivity
certificate for the stated sheet.

## 6. Reproduction, limitations, and next gate

Run only with the project environment:

```text
.venv/bin/python tmp/research/compact_ball_inward_z_tilt_discovery.py
```

The successful source run used Python 3.11.15 and SymPy 1.14.0. The source
hash at freeze time is

```text
6ee91b88c1835f44183a8da833239c817cdd6d079d73cd5b9e9c42428661f6ca
```

The dependencies inspected for the reconstruction were frozen at

```text
4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3
  tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md
bd127112e0cd59e9f0ed8c565480a612c2c75ba83edd979c3552896b18395067
  tmp/research/common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.md
```

The one next discriminating test is an independent no-import referee that
starts again from signed-\(z\) Gram columns, reconstructs the fully conjugated
\(Q,Q^2\) gate in a different component order, obtains the 80 controls by
an independently ordered Bernstein transform, and checks the three exact
closure zeros plus the 77 strict lowers and \(R_*\). Until that audit passes,
this remains a source candidate.

No sampled SDP, dropped phase, real-part monotonicity, or route
CE-046/048/059/060 is used. No proof assistant was used. This result does not
cover the full compact ball, arbitrary common metrics, the fixed-lens
constant, arbitrary dimensions, or arbitrary nodes, and it must not be
presented as any of those results.
