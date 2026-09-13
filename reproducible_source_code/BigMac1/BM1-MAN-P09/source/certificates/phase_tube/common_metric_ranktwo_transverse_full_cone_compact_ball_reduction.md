# A compact-ball chart for the full transverse rank-two cone

Date: 2026-08-18.  Status: **exact lossless reduction; the compact-ball
quartic sign remains open**.

This note replaces the unbounded variables in the full off-diagonal
compression cone by one positive scale and a fixed Euclidean ball.  It
keeps both complex phases and both entries of \(Q^2\).  The result is an
equivalent compact-shape quartic, not a proof of its sign.

Keep

\[
 a=\frac1{\sqrt6},\qquad c=\sqrt{\frac56},\qquad
 \zeta=\frac{4+3i}{5},\qquad p=(a,0,c)^T,
\]

and, for \(0\le h\le1\), put

\[
\begin{aligned}
 n_h&=(c\sqrt{1-h^2},h,a\sqrt{1-h^2}\,\zeta)^T,\\
 r&=(-a,0,c\zeta)^T,\\
 f_h&=(-ch,\sqrt{1-h^2},-ah\zeta)^T,\qquad U_h=(r\ f_h).
                                                               \tag{0.1}
\end{aligned}
\]

Thus the columns of \(U_h\), together with \(n_h\), are orthonormal.

## 1. The lossless Cholesky chart

Let \(h>0\), \(\lambda>0\), \(j,k\in\mathbb R\), and \(\ell\ge0\).  Set

\[
 W=j^2+k^2+\ell^2,
 \qquad
 H=U_h
 \begin{pmatrix}
 h^2&h(j+ik)\\ h(j-ik)&W
 \end{pmatrix}U_h^*,
 \qquad Q=\lambda H.                              \tag{1.1}
\]

The middle matrix is positive semidefinite because its determinant is
\(h^2\ell^2\).  Hence \(Q\succeq0\), \(Qn_h=0\), and it has rank two when
\(\ell>0\).

Conversely, write an arbitrary positive compression in the basis
\((r,f_h)\) as

\[
 C=\begin{pmatrix}u&X+iY\\X-iY&v\end{pmatrix},
 \qquad u,v\ge0,\qquad X^2+Y^2\le uv.             \tag{1.2}
\]

Strict danger forces \(u>0\).  The unique inverse chart, apart from the
irrelevant sign of \(\ell\), is

\[
 \lambda=\frac{u}{h^2},\qquad
 j=\frac{hX}{u},\qquad k=\frac{hY}{u},\qquad
 \ell=\frac{h\sqrt{uv-X^2-Y^2}}{u}.              \tag{1.3}
\]

Indeed, (1.3) gives

\[
 \lambda h^2=u,\qquad
 \lambda h(j+ik)=X+iY,\qquad
 \lambda W=v.                                    \tag{1.4}
\]

Therefore (1.1) represents every member of the full transverse positive
compression cone in the strict dangerous chart, with no spectral-frame or
phase restriction.

## 2. Danger is exactly a unit ball

Direct multiplication gives

\[
 \operatorname {Re}(Qp)_1
 =\frac{\lambda h^2\sqrt6}{12}
 \left\{3W-1+\frac2{\sqrt5}(-j+3k)\right\}.       \tag{2.1}
\]

Introduce affine coordinates

\[
 j=\frac{1+5x}{3\sqrt5},\qquad
 k=\frac{-3+5y}{3\sqrt5},\qquad
 \ell=\frac{\sqrt5}{3}z.                         \tag{2.2}
\]

Then the expression in braces in (2.1) is exactly

\[
 \frac53(x^2+y^2+z^2-1).                         \tag{2.3}
\]

Consequently strict danger is equivalent to

\[
                       x^2+y^2+z^2<1.             \tag{2.4}
\]

Because only \(\ell^2\) occurs in (1.1), allowing both signs of \(z\)
merely gives a two-to-one parametrization.  Thus the shape domain is the
fixed closed unit ball, with strict danger its interior.

## 3. The compact-shape quartic

Let \(\xi=Hp\) and define

\[
\begin{aligned}
 B_0&=(0,iac,0)^T,\\
 L&=(2a\xi_2,\ c\overline{\xi_1}+a\xi_3,
                         c\overline{\xi_2})^T,\\
 M&=(0,-i(H^2)_{31},-i(H^2)_{32})^T,\\
 d&=\operatorname {Re}\xi_1.
                                                               \tag{3.1}
\end{aligned}
\]

Substitution into the original Hermitian scalar gate, without replacing
\(H^2\), gives the exact identity

\[
 \boxed{\quad
 \Gamma(\lambda H)
 =\|B_0+\lambda L+\lambda^2M\|^2
       -32a^2\lambda^2d^2.\quad}                  \tag{3.2}
\]

Hence this is a real quartic in the sole unbounded variable \(\lambda\):

\[
\begin{aligned}
 \Gamma(\lambda H)={}&A_4\lambda^4+A_3\lambda^3
                      +A_2\lambda^2+A_1\lambda+A_0,\\
 A_4={}&\|M\|^2,\\
 A_3={}&2\operatorname {Re}\langle L,M\rangle,\\
 A_2={}&\|L\|^2+2\operatorname {Re}\langle B_0,M\rangle
                   -32a^2d^2,\\
 A_1={}&2\operatorname {Re}\langle B_0,L\rangle,\qquad
 A_0=a^2c^2=\frac5{36}.                           \tag{3.3}
\end{aligned}
\]

Put \(s=h^2\) and use (2.2).  Exact cancellation of all square roots gives

\[
 \boxed{
 36\Gamma(\lambda H)
 =5+h^2\sum_{m=1}^4\lambda^mF_m(s,x,y,z),}
                                                               \tag{3.4}
\]

where

\[
 F_m\in\mathbb Q[s,x,y,z],\qquad
 \deg_sF_m\le m-1,\qquad \deg_{x,y,z}F_m\le2m.  \tag{3.5}
\]

For example, the linear coefficient is the short polynomial

\[
 F_1=\frac{10}{3}
 (x^2-2x+y^2-6y+z^2+1).                           \tag{3.6}
\]

The remaining coefficients are reconstructed from (3.1)--(3.3) by the
standalone verifier.  Formula (3.4), rather than their expanded 38-, 69-,
and 225-term forms, is the auditable defining representation.  Its leading
coefficient is the Gram square \(36\|M\|^2/h^2\ge0\).

Thus the full transverse problem for \(h>0\) is equivalent to one precise
compact problem:

> prove the quartic (3.4) nonnegative for
> \(0<s\le1\), \(x^2+y^2+z^2<1\), and \(\lambda>0\).

The omitted face \(h=0\) is exactly the already proved full cone over the
sharp planar kernel.  Therefore no geometric member of the transverse
cone is lost by treating that face separately.

## 4. Scope

This note is a lossless invariant reduction of the full complex
off-diagonal transverse compression cone to a compact unit-ball shape and
one positive scale.  It is stronger than a fixed Bloch-frame chart, but it
does not prove the sign of (3.4), cover arbitrary kernel paths, establish
the full common-metric theorem, or determine the fixed crossing-lens
constant.

Run
`tmp/research/verify_common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.py`
for the fail-closed symbolic reconstruction.
