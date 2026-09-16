# Exact global certificate for degree two

Set $k:=\kappa$, $g:=\gamma$, and write

\[
u(x)=u_0+a x+c x^2,\qquad q(x)=b_0+b x+d x^2.
\]

The coefficient $u_0$ is the known unused null direction.  On the ordered
effective coordinates $z=(a,c,b_0,b,d)$, direct expansion of the form in
`problem.md` (with $\gamma_D=30$) gives $a^{(2)}_{k,g}=z^T H_2(k,g)z$,
where

\[
H_2(k,g)=
\begin{pmatrix}
1+g&-1&0&-g&0\\
-1&\frac43+g&0&0&-g\\
0&0&30&30k-1&30k^2-2k\\
-g&0&30k-1&g+30k^2-k&30k^3-2k^2\\
0&-g&30k^2-2k&30k^3-2k^2&g+30k^4-\frac83k^3
\end{pmatrix}.
\]

This is the requested exact $5\times5$ matrix.  The following congruence is
a PSD certificate on the full interval, not merely a determinant test.

Make the invertible change of coordinate

\[
y=q(k)=b_0+kb+k^2d,
\]

and put $\alpha=(a,c)^T$, $\beta=(b,d)^T$.  With

\[
U=\begin{pmatrix}1&-1\\-1&4/3\end{pmatrix},\qquad
C(k)=\begin{pmatrix}
k-1/30&k^2-k/15\\
k^2-k/15&\frac43k^3-\frac2{15}k^2
\end{pmatrix},
\]

completion of the boundary square gives

\[
a^{(2)}_{k,g}
=30\left(y-\frac{b+2kd}{30}\right)^2
+\alpha^TU\alpha+g\lVert\beta-\alpha\rVert^2
+\beta^TC(k)\beta.
\]

At the proposed value $g_0=1/26$, let $P=U+g_0I$.  Exact arithmetic gives

\[
P=\begin{pmatrix}27/26&-1\\-1&107/78\end{pmatrix},\qquad
\det P=\frac{287}{676}>0,
\]

and

\[
P^{-1}=\begin{pmatrix}2782/861&676/287\\676/287&702/287\end{pmatrix}.
\]

Completing the $\alpha$-square yields

\[
\alpha^TP\alpha-2g_0\alpha^T\beta
+\beta^T(C+g_0I)\beta
=(\alpha-g_0P^{-1}\beta)^TP(\alpha-g_0P^{-1}\beta)
+\beta^TS(k)\beta,
\]

where the exact $2\times2$ Schur complement is

\[
S(k)=\begin{pmatrix}
\dfrac{2870k+1}{2870}&
\dfrac{4305k^2-287k-15}{4305}\\[5pt]
\dfrac{4305k^2-287k-15}{4305}&
\dfrac{2(2870k^3-287k^2+75)}{4305}
\end{pmatrix}
\]

with

\[
\det S(k)=
\frac{k(4305k^3+6k^2+32k+444)}{12915}.
\]

For every $k\ge0$, $S_{11}(k)>0$ and $\det S(k)\ge0$.  Equivalently,

\[
\beta^TS\beta
=S_{11}\left(b+\frac{S_{12}}{S_{11}}d\right)^2
+\frac{\det S}{S_{11}}d^2\ge0.
\]

Together with $P\succ0$ and the boundary square, this proves
$H_2(k,1/26)\succeq0$ for all $0\le k\le1$.  It is positive definite on
the five effective coordinates whenever $k>0$, because then
$\det S(k)>0$.

For completeness, necessity at the limiting cut is also visible from the
same congruence without invoking a floating-point eigenvalue.  At $k=0$
and arbitrary $g>0$, $P_g=U+gI\succ0$, and the corresponding Schur
complement $S_g(0)$ satisfies

\[
\det S_g(0)=
\frac{g(26g-1)}{30(3g^2+7g+1)}.
\]

Thus $H_2(0,g)$ is indefinite for every $0<g<1/26$.  For each such fixed
$g$, continuity makes it indefinite for all sufficiently small positive
$k$.  Since the ghost matrix is PSD, feasibility is monotone in $g$, so
$\liminf_{k\to0+}\tau_2(k)\ge g$.  Letting $g\uparrow1/26$, and using the
global upper certificate, proves

\[
\lim_{k\to0+}\tau_2(k)=\Gamma_2=\frac1{26}.
\]

For every interior $k>0$, positive definiteness at $g_0$ and continuity
in $g$ allow $g$ to be decreased slightly, hence
$\tau_2(k)<1/26$.  The same uniform continuity argument around $k=1$
shows that the $k\to1-$ limit is also strictly below $1/26$.  Therefore
there is no interior maximizer, and the unique limiting maximizer is
$k\to0+$.
