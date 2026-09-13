# Scale-cubic reduction of the complex Schur-boundary gate

Date: 2026-08-18.  Status: **strictly smaller exact equivalent gate**.  The
remaining shape inequalities are open; this note is not a universal
positivity theorem.

Use the notation of
`common_metric_tilted_rankone_complex_schur_boundary_polynomial.md`.  Thus

\[
 R=\begin{pmatrix}r&z+iw\\z-iw&t\end{pmatrix}\succ0,
 \qquad \Delta=rt-z^2-w^2>0,
\]

and the Schur-boundary coupling is \(h=(u+iv,s)^T\), with \(s>0\).  Normalize
the coupling direction by writing

\[
                         u=sk,\qquad v=s\ell,
 \qquad                    T=s^2>0.                \tag{0.1}
\]

This separates the direction \((k+i\ell,1)^T\) from its positive scale.

## 1. The branch becomes a half-line

Define

\[
\begin{aligned}
 n&=t(k^2+\ell^2)+r-2(kz+\ell w),\\
 g&=ac\ell-zk-w\ell-t.                             \tag{1.1}
\end{aligned}
\]

Since

\[
 n=(k-i\ell,1)\operatorname {adj}(R)(k+i\ell,1)^T
\]

and \(R\succ0\), one has \(n>0\).  The exact Schur and gate centers are

\[
 q_{\min}=\frac{Tn}{\Delta},qquad q_g=g,           \tag{1.2}
\]

while the boundary residual of the previous note is

\[
                         J=s(Tn-\Delta g).          \tag{1.3}
\]

Consequently the complementary branch is precisely

\[
 T>T_L,qquad
 T_L=\begin{cases}
 0,&g\le0,\\
 \Delta g/n,&g>0.
 \end{cases}                                      \tag{1.4}
\]

The endpoint \(T=T_L\) is included below only as the closure of the strict
branch.

## 2. The exact cubic

Put

\[
\begin{aligned}
 x&=ar+cz,\\
 L&=ak+c,\\
 A&=ac(r+t)+z-w(r+t),\\
 B&=ac-w-z(r+t),\\
 C&=cL+z\ell-wk.                                   \tag{2.1}
\end{aligned}
\]

At the Schur boundary, the residuals in the cleared polynomial become

\[
 R_1=A-T\ell,qquad I_1=B-Tk,qquad R_2=sC,
 \qquad J^2=T(Tn-\Delta g)^2.                      \tag{2.2}
\]

Therefore

\[
 4\Delta^2\mathcal G(Q(q_{\min}))=P(T),            \tag{2.3}
\]

where

\[
\begin{aligned}
 P(T)={}&\Delta^2\Bigl[(A-T\ell)^2+(B-Tk)^2
       -32a^2x^2\\
 &\qquad+T\{4a^2(L^2+a^2\ell^2)+C^2\}\Bigr]
       +T(Tn-\Delta g)^2.                          \tag{2.4}
\end{aligned}
\]

Equivalently,

\[
                         P(T)=C_0+C_1T+C_2T^2+n^2T^3,           \tag{2.5}
\]

with

\[
\begin{aligned}
 C_0={}&\Delta^2(A^2+B^2-32a^2x^2),\\
 C_1={}&\Delta^2\bigl[-2(A\ell+Bk)
       +4a^2(L^2+a^2\ell^2)+C^2+g^2\bigr],\\
 C_2={}&\Delta^2(k^2+\ell^2)-2\Delta gn.           \tag{2.6}
\end{aligned}
\]

All dependence on the positive coupling scale is now contained in one real
variable \(T\).

## 3. Strict convexity on the legal half-line

Since

\[
                         P''(T)=2(C_2+3n^2T),       \tag{3.1}
\]

strict convexity follows directly from the branch endpoint.

If \(g\le0\), then

\[
 C_2=\Delta^2(k^2+\ell^2)-2\Delta gn>0.            \tag{3.2}
\]

Indeed, if \(k=\ell=0\), then \(g=-t<0\), so the second term is strictly
positive; otherwise the first term is positive.

If \(g>0\), then \(T_L=\Delta g/n\), and

\[
 C_2+3n^2T_L
 =\Delta^2(k^2+\ell^2)+\Delta gn>0.                \tag{3.3}
\]

Thus \(P''(T)>0\) throughout \([T_L,\infty)\) in every case.  The full
multivariable sign problem has been reduced to the unique minimum of a
strictly convex cubic on a half-line.

## 4. Finite exact sign gate

Shift \(T=T_L+S\), \(S\ge0\), and write

\[
 P(T_L+S)=g_0+g_1S+g_2S^2+n^2S^3,                 \tag{4.1}
\]

where

\[
 g_0=P(T_L),\qquad
 g_1=P'(T_L),\qquad
 g_2=C_2+3n^2T_L>0.                                \tag{4.2}
\]

If \(g_1\ge0\), the shifted cubic is increasing, so it is nonnegative on
the half-line exactly when \(g_0\ge0\).  If \(g_1<0\), its derivative has
one negative and one positive root, and the positive root is the unique
minimum.  In this branch define

\[
\begin{aligned}
 \mathfrak D={}&18n^2g_2g_1g_0-4g_2^3g_0+g_2^2g_1^2\\
 &-4n^2g_1^3-27n^4g_0^2.                           \tag{4.3}
\end{aligned}
\]

This is the discriminant of the shifted cubic.  The exact necessary and
sufficient condition is

\[
\boxed{\quad
 P(T)\ge0\ \text{for every }T\ge T_L
 \iff
 g_0\ge0\ \text{ and }\
 \bigl[g_1\ge0\ \text{ or }(g_1<0\text{ and }\mathfrak D\le0)\bigr].
\quad}                                              \tag{4.4}
\]

For \(g_1<0\), a positive discriminant gives two nonnegative roots and a
negative interval between them; when \(g_0>0\), both roots are positive.
Zero discriminant is the allowed tangent case.  Formula (4.4) also correctly
rejects \(g_0=0,g_1<0\), for which the roots are zero and a positive number
and the cubic is negative immediately to the right of the endpoint.

## 5. Calibration and scope

For the exact rank-two calibration in the preceding note,

\[
 k=-3,qquad\ell=9,qquad T=\frac1{100}.
\]

Substitution into (2.3) reproduces

\[
 \mathcal G(Q(q_{\min}))
 =\frac{226444674193}{21170250000}>0.
\]

Equations (1.4), (2.5), (3.1)--(3.3), and (4.4) form a strictly smaller
exact gate than the original eight-variable cleared polynomial: after the
active block and coupling direction are fixed, the remaining problem is a
single strictly convex cubic and is decided by finitely many explicit shape
signs.  What remains open is to prove those shape signs uniformly (or to find
a legal shape for which they fail).  No numerical search is used as a proof.

The companion fail-closed verifier reconstructs (2.3) from the original
Hermitian gate, checks every cubic coefficient and curvature identity, and
checks the calibration in exact arithmetic.
