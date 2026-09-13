# Completion of the 3+1+1 direction stratum

This note completes the scalar inequality left open in
*three_direction_segments.md*. It proves a local result for Assertion 1,
not either frozen assertion in full and not the seven-atom conjecture.

## A weighted-triangle edge-distance lemma

Let \(r_i>0\), \(\sum_{i=1}^3r_i=1\), and let
\(w_i\in\mathbb C\simeq\mathbb R^2\) satisfy

\[
 \sum_i r_iw_i=0,\qquad V=\sum_i r_i|w_i|^2>0.
\]

If
\(\Gamma=[w_1,w_2]\cup[w_1,w_3]\cup[w_2,w_3]\), then, for every
\(u\in\mathbb C\),

\[
 \operatorname {dist}^2(u,\Gamma)\le
 \begin{cases}
 \dfrac{(V+|u|^2)^2}{4V},& |u|^2\le V,\\[4pt]
 |u|^2,& |u|^2\ge V.
 \end{cases}                                                   \tag{11}
\]

### Proof

First suppose that the triangle is nondegenerate. For the side opposite
\(w_i\), let \(\ell_i\) be its length, \(n_i\) its inward unit normal, and
\(h_i>0\) the distance from \(0\) to its supporting line. Let \(A\) be the
area. The barycentric-coordinate and closed-polygon identities give

\[
 r_i=\frac{\ell_i h_i}{2A},\qquad \sum_i\ell_i n_i=0.             \tag{12}
\]

Put

\[
 Z=\sum_i\frac{r_i}{h_i^2},\qquad
 \alpha_i=\frac{r_i/h_i^2}{Z},\qquad
 H=\frac1Z,\qquad M=\sum_i\alpha_i n_in_i^{\mathsf T}.
\]

Thus \(\sum_i\alpha_i=1\), \(\operatorname {tr}M=1\), and (12) implies

\[
 \sum_i\alpha_i h_i n_i=0,\qquad
 \sum_i\alpha_i h_i^2=H.                                      \tag{13}
\]

There is also the exact identity

\[
                         H=V\det M.                             \tag{14}
\]

Indeed, the weighted variance identity and (12) give

\[
 V=\sum_i r_jr_k\ell_i^2
   =4A^2Zr_1r_2r_3,
 \qquad \{i,j,k\}=\{1,2,3\}.                                  \tag{15}
\]

By the \(2\times3\) Cauchy--Binet formula, and because the two sides of
lengths \(\ell_i,\ell_j\) have sine \(2A/(\ell_i\ell_j)\),

\[
 \begin{aligned}
 \det M
 &=\sum_{i<j}\alpha_i\alpha_j\det(n_i,n_j)^2\\
 &=\frac1{4A^2Z^2}\sum_{i<j}\frac1{r_ir_j}
  =\frac1{4A^2Z^2r_1r_2r_3}
  =\frac1{ZV},
 \end{aligned}
\]

which proves (14).

If \(u\) is inside the triangle, its distance to the boundary is no larger
than the least of its three positive signed distances \(h_i+n_i\cdot u\).
Equations (13)--(14) therefore yield

\[
 \operatorname {dist}^2(u,\Gamma)
 \le \sum_i\alpha_i(h_i+n_i\cdot u)^2
 =V\det M+u^{\mathsf T}Mu.                                    \tag{16}
\]

Write the eigenvalues of \(M\) as \(\lambda,1-\lambda\), where
\(0\le\lambda\le1/2\), and put \(U=|u|^2\). The right side of (16) is at
most

\[
 (1-\lambda)(V\lambda+U).
\]

For \(U\le V\), its maximum on \([0,1/2]\) occurs at
\(\lambda=(V-U)/(2V)\) and equals \((V+U)^2/(4V)\). For \(U\ge V\), its
maximum is \(U\). If \(u\) is outside the triangle, the fact that \(0\)
lies in the triangle gives
\[
\operatorname {dist}(u,\Gamma)
=\operatorname {dist}(u,\operatorname {conv}\{w_i\})\le|u|,
\]
so the same bounds follow. In the degenerate collinear case, one of the
three segments contains \(0\), hence the last inequality holds directly.
This proves (11).

## The local 3+1+1 theorem

Consider a five-label moment system whose directions have exactly three
classes of multiplicities \(3,1,1\). Label the three-label class \(G_1\),
and retain all notation of *three_direction_segments.md*:

\[
 P_k=\sum_{i\in G_k}p_i,\quad r_i=p_i/P_1,\quad
 w_i=z_i-m_1,\quad V_1=\sum_{i\in G_1}r_i|w_i|^2.
\]

Then there is an admissible probability vector \(q\), supported on at most
three labels, for which

\[
                            C(q)\le\frac58E.                     \tag{17}
\]

### Proof

The zero-energy case is immediate. Suppose \(E>0\), write \(V=V_1\), and
put

\[
 x_k=1-2P_k.
\]

The three distinct unit directions and their positive barycentric weights
imply \(x_k>0\) and \(\sum_kx_k=1\). The class-energy identities give

\[
 E=E_m+P_1V,\qquad P_1|m_1|^2=x_1E_m.                            \tag{18}
\]

By the exact attained certificate (3) in
*three_direction_segments.md*, it is enough to bound one of

\[
 A_0=2P_1^2d_*^2,\qquad
 S_g=\frac{x_g}{2P_g}E_m+\frac{2P_1P_g}{x_h}\delta_g^2,
 \quad\{g,h\}=\{2,3\}.                                         \tag{19}
\]

Here \(d_*^2=\min_i|w_i|^2\), and \(\delta_g\) is the distance from
\(-m_1/(2P_g)\) to \(\Gamma\).

Assume \(A_0>(5/8)E\), since otherwise (17) is already attained. Since
\(d_*^2\le V\),

\[
 2P_1^2V>\frac58(E_m+P_1V),                                    \tag{20}
\]

so \(P_1>5/16\). Set

\[
 x=x_1,\qquad y=\max(x_2,x_3),\qquad z=\min(x_2,x_3),
\]

and in (19) choose \(h\) with \(x_h=y\) and \(g\) with \(x_g=z\). Thus

\[
 0<x<\frac38,\qquad y\ge\frac{1-x}{2},\qquad z=1-x-y.            \tag{21}
\]

If \(E_m=0\), the target in \(\delta_g\) is zero. Lemma (11) gives
\(\delta_g^2\le V/4\), and hence

\[
 \frac{S_g}{P_1V}\le\frac{1-z}{4y}
 =\frac{x+y}{4y}<\frac58,
\]

where \(2x<3y\) follows from (21). This proves (17) in that case.

It remains to take \(E_m>0\). Divide all squared response quantities by
\(E_m\), so \(E_m=1\). Inequality (20) becomes

\[
 V>V_0:=\frac{10}{(1-x)(3-8x)}.                                \tag{22}
\]

For the selected target, (18) gives

\[
 U:=\left|\frac{m_1}{2P_g}\right|^2
   =\frac{2x}{(1-x)(1-z)^2}.
\]

Using \(1-z=x+y\ge(1+x)/2\),

\[
 \frac{U}{V}<\frac{U}{V_0}
 \le\frac{4x(3-8x)}{5(1+x)^2}<\frac12.                          \tag{23}
\]

The last inequality is equivalent to
\(5-14x+69x^2>0\), whose discriminant is negative. Applying (11), then
(23), yields

\[
 \delta_g^2\le\frac{(V+U)^2}{4V}
 =\frac V4+\frac U2+\frac{U^2}{4V}
 \le\frac V4+\frac58U.                                        \tag{24}
\]

Substitution into (19) gives

\[
 S_g\le
 \frac{z}{1-z}+\frac{5x}{8y(1-z)}
 +\frac{(1-x)(1-z)}{8y}V.                                     \tag{25}
\]

The coefficient of \(V\) in
\((5/8)(1+(1-x)V/2)-S_g\) is

\[
 \frac{(1-x)(3y-2x)}{16y}>0                                   \tag{26}
\]

by (21). It therefore suffices, using (22), to substitute \(V=V_0\).
After multiplication by the positive denominator
\(8y(x+y)(3-8x)\), the resulting difference has numerator

\[
 N=30x^2-15x-24y+108xy+54y^2-104xy(x+y).                       \tag{27}
\]

Write \(y=(1-x)/2+q\), where \(q\ge0\). Then

\[
 N=\left(\frac32-2x-\frac{21}{2}x^2+26x^3\right)
 +(30-50x)q+(54-104x)q^2.                                     \tag{28}
\]

Both coefficients of \(q,q^2\) are positive for \(0<x<3/8\). Twice the
constant term is

\[
 3-4x-21x^2+52x^3.
\]

For \(0<x\le1/4\), it is at least
\(3-4x-21x^2\ge11/16\). For \(1/4\le x<3/8\), use
\(52x^3\ge13x^2\) to bound it below by
\(3-4x-8x^2\ge3/8\). Thus \(N>0\). Equations (22), (25)--(28) prove

\[
 S_g<\frac58(1+P_1V)=\frac58E.
\]

The exact segment proposition proves that this \(S_g\) is attained by an
admissible selection on at most three labels. Together with the alternative
\(A_0\le(5/8)E\), this proves (17).

## Scope

The argument settles exactly the five-label, three-direction multiplicity
stratum \(3+1+1\). Systems with five distinct directions, with four distinct
directions, and the six-atom/four-point assertion are not addressed here.
