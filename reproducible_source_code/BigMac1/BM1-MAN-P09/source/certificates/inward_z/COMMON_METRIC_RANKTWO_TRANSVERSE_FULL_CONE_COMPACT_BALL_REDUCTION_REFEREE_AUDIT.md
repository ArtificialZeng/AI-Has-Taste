# Referee audit: compact-ball reduction of the full transverse rank-two cone

Date: 2026-08-18  
Source audited: `tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md`  
Official verifier audited: `tmp/research/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.py`  
Independent verifier: `audit/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction_referee.py`

## Verdict

**PASS as an exact lossless reduction, with the boundary qualification made
explicit below.**  For every `0<h<=1`, the chart represents every positive
compression in the strict-danger branch, including rank-one compression
boundaries.  Strict danger becomes exactly the open Euclidean unit ball,
and the original Hermitian scalar gate becomes the stated rational
compact-shape quartic in one positive scale.

The theorem does not prove that this quartic is nonnegative.  It is a
finite-dimensional reduction of the full transverse cone, not a
common-metric theorem and not a result on the unrestricted fixed-lens
constant.

The point `h=0` is not part of the inverse chart: it is the separately
proved planar-kernel cone.  Correspondingly, `s=0` in the coefficient
polynomials is a useful formal closure, not a second parametrization of all
planar compressions.

## 1. Forward positivity and the complete inverse chart

For

\[
 C_0=\begin{pmatrix}
 h^2&h(j+ik)\\ h(j-ik)&j^2+k^2+\ell^2
 \end{pmatrix},
\]

the independent verifier uses the direct factorization

\[
 C_0=
 \begin{pmatrix}h&0\\j-ik&\ell\end{pmatrix}
 \begin{pmatrix}h&j+ik\\0&\ell\end{pmatrix}.
\]

Thus `C0>=0` without an appeal only to principal minors, and

\[
 \det C_0=h^2\ell^2.
\]

The case `ell=0` is retained and gives the rank-one boundary.  The
transverse frame is independently reduced modulo
`q^2+h^2-1`, proving that `(r,f_h,n_h)` is orthonormal.  Therefore

\[
 Q=\lambda U_hC_0U_h^*\succeq0,
 \qquad Qn_h=0
\]

for `lambda>0`.

Conversely, let

\[
 C=\begin{pmatrix}u&X+iY\\X-iY&v\end{pmatrix}\succeq0.
\]

Direct multiplication before any chart substitution gives

\[
 \operatorname {Re}(U_hCU_h^*p)_1
 =\frac{\sqrt6}{12}(3vh^2-u)
  +\frac{\sqrt{30}}{30}(-X+3Y)h.
\]

If `u=0`, positivity forces `X=Y=0`, and this expression equals
`sqrt(6) v h^2/4>=0`.  Hence strict danger forces `u>0` exactly as the
source requires.

For `h>0,u>0`, define

\[
 \lambda=\frac{u}{h^2},\qquad
 j=\frac{hX}{u},\qquad k=\frac{hY}{u},\qquad
 \ell=\frac{h\sqrt{uv-X^2-Y^2}}{u}.
\]

The independent calculation reconstructs all three compression entries:

\[
 \lambda h^2=u,qquad
 \lambda h(j+ik)=X+iY,qquad
 \lambda(j^2+k^2+\ell^2)=v.
\]

Thus the map is onto the complete positive compression cone in the
strict-danger chart.  Its inverse is unique after choosing `ell>=0`; if
both signs are allowed, they give the stated two-to-one redundancy.  No
spectral frame, complex phase, eigenvalue ratio, or PSD rank stratum is
lost.

## 2. Exact unit-ball completion

For the normalized shape operator `H=U_h C0 U_h*`, exact multiplication
gives

\[
 \operatorname {Re}(Hp)_1
 =\frac{h^2\sqrt6}{12}
 \left(3W-1+\frac2{\sqrt5}(-j+3k)\right),
 \qquad W=j^2+k^2+\ell^2.
\]

After

\[
 j=\frac{1+5x}{3\sqrt5},\qquad
 k=\frac{-3+5y}{3\sqrt5},\qquad
 \ell=\frac{\sqrt5}{3}z,
\]

the bracket is exactly

\[
 \frac53(x^2+y^2+z^2-1).
\]

All prefactors in `Re(lambda Hp)_1` are positive for `h>0` and
`lambda>0`.  Therefore strict danger is equivalent in both directions to

\[
 x^2+y^2+z^2<1.
\]

The sphere is the zero-danger boundary, not part of strict danger.  It may
be adjoined when proving a closed-domain inequality because there the
negative square vanishes and the original gate is a sum of squared
moduli.  The reflection `z->-z` changes only the sign of `ell`; the
compression itself contains only `ell^2` and is unchanged.

## 3. Reconstruction of the original Hermitian gate

The independent verifier forms the actual `3 by 3` matrix `Q=lambda H`,
then forms `Q^2` before constructing

\[
\begin{aligned}
\Gamma(Q)={}&4a^2|(Qp)_2|^2\\
&+\left|c\overline{(Qp)_1}+a(Qp)_3
 +i\{ac-(Q^2)_{31}\}\right|^2\\
&+\left|c\overline{(Qp)_2}-i(Q^2)_{32}\right|^2
 -32a^2\operatorname {Re}(Qp)_1^2.
\end{aligned}
\]

Independently it constructs

\[
 B_0+\lambda L+\lambda^2M
\]

from `H`, `H^2`, and `Hp`.  Exact polynomial remainder modulo
`q^2+h^2-1` verifies

\[
 \Gamma(\lambda H)
 =\|B_0+\lambda L+\lambda^2M\|^2
  -32a^2\lambda^2d^2.
\]

It then checks all five coefficient identities

\[
\begin{aligned}
A_4&=\|M\|^2,&
A_3&=2\operatorname {Re}\langle L,M\rangle,\\
A_2&=\|L\|^2+2\operatorname {Re}\langle B_0,M\rangle-32a^2d^2,&
A_1&=2\operatorname {Re}\langle B_0,L\rangle,\\
A_0&=\|B_0\|^2=5/36.
\end{aligned}
\]

Both `Q^2` entries and all complex phases are therefore retained.

## 4. Rational coefficients and degree audit

After the affine ball substitution, the independent verifier divides each
positive-lambda coefficient of `36 Gamma` by `h^2`.  It eliminates `q` by
polynomial remainder and converts even powers `h^(2m)` to `s^m` term by
term.  This differs from the official verifier's ordered syntactic
substitution of `h^6,h^4,h^2` and explicitly fails if an odd power of `h`
survives.

The result is

\[
 36\Gamma(\lambda H)
 =5+h^2\sum_{m=1}^4\lambda^mF_m(s,x,y,z),
 \qquad s=h^2,
\]

with every `Fm` over `QQ`.  The independently recovered term counts are

\[
 6,\quad38,\quad69,\quad225.
\]

For each `m`, it checks

\[
 \deg_sF_m\le m-1,
 \qquad \deg_{x,y,z}^{\rm total}F_m\le2m.
\]

It also reproduces

\[
 F_1=\frac{10}{3}(x^2-2x+y^2-6y+z^2+1)
\]

and independently checks that `F4` is exactly the transformed Gram square
`36||M||^2/h^2`.  No positivity of `F2` or `F3`, and no sign of the full
quartic, is inferred from these structural facts.

## 5. The `h=0` boundary and exact scope

At `h=0`, the frame remains the planar orthonormal frame, but the shape
compression above collapses to

\[
 C_0=\operatorname {diag}(0,W).
\]

Consequently the inverse formula `lambda=u/h^2` is unavailable and the
chart is not onto the planar cone.  This is not a gap because the complete
`h=0` planar-kernel cone is a separate previously proved theorem.

Accordingly, the exact equivalence is the union of:

1. the separately treated planar face `h=0`; and
2. the compact-ball chart for `0<h<=1`, open ball, and `lambda>0`.

The polynomial value at `s=0` can be used as a closure in a future
coefficient proof, but it must not be interpreted as the inverse image of
an arbitrary planar compression at fixed finite `lambda`.  Also, the
domain `0<s<=1` is bounded but not itself closed; the word "compact" refers
to the fixed closed shape ball after adjoining harmless boundaries, not to
a new homeomorphism at `h=0`.

## 6. Execution

Both current verifiers pass normally and reject optimized execution before
mathematical work:

- official verifier: normal **PASS**, `python -O` fail-closed;
- independent verifier: normal **PASS**, `python -O` fail-closed.

The source, official verifier, independent verifier, and this report are
control-byte clean.  The independent verifier also passes `py_compile`.

The audited result is an exact equivalent finite-dimensional reduction.
The sign of its compact-ball quartic remains open, as do the common-metric
and fixed crossing-lens problems.

## Superseding snapshot addendum (2026-08-18)

I directionally rechecked the current publication-clean snapshot after the
inline-TeX-only edits.  The mathematical formulas and verifier are unchanged;
the source verifier still passes normally and rejects `python -O` fail-closed,
and the audited source/diff remains control-byte clean.  The PASS verdict and
strict reduction-only scope above therefore bind to the current snapshot.
