# Exact curvature certificates and interior fixed points

All notation and conventions are those frozen in `problem.md`.  This file proves
an exact subsidiary result; it does **not** classify all omega-limit sets of the
flow.

## 1. A three-point primal/dual transport certificate

Let a three-point metric space have points \(x,y,z\) and distances
\[
 D=d(x,y),\qquad X=d(x,z),\qquad Y=d(y,z).
\]
Let the non-lazy transition probabilities from \(x\) to \(y,z\) be
\(p,1-p\), and those from \(y\) to \(x,z\) be \(q,1-q\).  Set
\(\varepsilon=1-\alpha\) and \(A=q-p\).  For all sufficiently small positive
\(\varepsilon\), the following formulas are exact:
\[
 W_1(m_x^{1-\varepsilon},m_y^{1-\varepsilon})=
 \begin{cases}
 D[1-\varepsilon(1+q)]+\varepsilon A Y,&A\geq0,\\[2mm]
 D[1-\varepsilon(1+p)]-\varepsilon A X,&A\leq0.
 \end{cases}                                                    \tag{1}
\]
Indeed, the signed surplus \(m_x^{1-\varepsilon}-m_y^{1-\varepsilon}\)
at \(x,y,z\) is respectively
\[
 1-\varepsilon(1+q),\quad -1+\varepsilon(1+p),\quad
 \varepsilon A.
\]
If \(A\geq0\), send \(\varepsilon A\) from \(z\) to \(y\) and all
remaining surplus from \(x\) to \(y\).  If \(A\leq0\), send
\(-\varepsilon A\) from \(x\) to \(z\) and the remainder from \(x\) to
\(y\).  These are feasible primal plans and have the costs in (1).

For matching dual certificates, normalize \(f(y)=0,f(x)=D\).  In the first
case take \(f(z)=Y\); in the second take \(f(z)=D-X\).  Each is 1-Lipschitz
by the triangle inequalities, and its dual value equals the stated primal
cost.  Thus (1) follows from weak duality, without an asymptotic or numerical
LP step.  Consequently
\[
 \kappa(x,y)=
 \begin{cases}
 1+q-A Y/D,&A\geq0,\\[1mm]
 1+p+A X/D,&A\leq0.
 \end{cases}                                                     \tag{2}
\]

For the edge \(a=23\), oriented from \(2\) to \(3\),
\[
 p={c\over a+c},\qquad q={b\over a+b},\qquad
 A={a(b-c)\over(a+b)(a+c)},                                    \tag{3}
\]
and \((D,X,Y)=(d_a,d_c,d_b)\).  The other two edges follow by cyclic
permutation.  Equations (1)--(3) are explicit primal/dual Kantorovich
certificates in every chamber and on every wall.

## 2. Curvature vector in the four shortest-path chambers

Write \(S=a+b+c\).  In the triangle-inequality chamber, for any edge of raw
length \(e\), let \(M\geq m\) be the other two raw edge lengths.  Substitution
in (2) gives the symmetric formula
\[
 \boxed{\displaystyle
 \kappa_e={e^2+2eM+em+3Mm-M^2\over(e+M)(e+m)}}.                 \tag{4}
\]
This includes the chamber walls.  For example, if \(b\geq c\), (2)--(3)
give
\[
 \kappa_a=1+{b\over a+b}-{b(b-c)\over(a+b)(a+c)},
\]
which is (4); the case \(c\geq b\) is its swap.

In the chamber where \(L\geq u+v\) is the unique possibly long raw edge,
the full vector is
\[
 \boxed{\displaystyle
 \kappa_L={S[L(u+v)+2uv]\over(L+u)(L+v)(u+v)},\qquad
 \kappa_u={S\over L+u},\qquad
 \kappa_v={S\over L+v}.}                                      \tag{5}
\]
The other two long-edge chambers are obtained by permutation.  At
\(L=u+v\), (4) and (5) agree componentwise: after taking \(u\geq v\), the
long component in (4) has numerator
\(2(u^2+4uv+v^2)\), while (5) reduces to the same expression over
\((2u+v)(u+2v)\); either short component reduces to
\(2(u+v)/(L+u)\) or \(2(u+v)/(L+v)\), respectively.  Hence the curvature
vector itself has no jump across any shortest-path wall.

## 3. Complete classification of positive fixed points

**Theorem.** On the normalized open simplex, the fixed-point set of (RF) is
\[
 \left\{(1/3,1/3,1/3)\right\}
 \ \cup\!
 \bigcup_{\sigma\in S_3}
 \left\{\sigma\!\left({r\over r+2},{1\over r+2},{1\over r+2}\right):
 r\geq2\right\}.                                               \tag{6}
\]
(Repeated permutations describe the same three rays.)

**Proof.** Since all weights are positive and sum to one, (RF) vanishes
exactly when the three curvatures are equal.  Sort the raw lengths as
\(L\geq M\geq m>0\).

First suppose \(L\leq M+m\).  Direct subtraction in (4) gives
\[
 \kappa_M-\kappa_m=
 -{2L(M-m)\over(L+M)(L+m)}.                                    \tag{7}
\]
Thus equality of all three curvatures forces \(M=m=x\).  In that case
\[
 \kappa_L={L+2x\over L+x},\qquad
 \kappa_x={2x^2+5Lx-L^2\over2x(L+x)},
\]
and hence
\[
 \kappa_L-\kappa_x={ (L-x)(L-2x)\over2x(L+x)}.                 \tag{8}
\]
Because \(x\leq L\leq2x\), equality occurs only at \(L=x\) or
\(L=2x\).  These give the uniform point and the three wall points with ratio
\(2:1:1\).

Now suppose \(L\geq M+m\).  Formula (5) gives
\[
 \kappa_M={S\over L+M},\qquad \kappa_m={S\over L+m};
\]
their equality forces \(M=m=x\).  Conversely, for every \(L\geq2x\),
formula (5) simplifies to
\[
 \kappa_L={S\over L+x}=\kappa_x.
\]
Normalization yields precisely the three rays in (6), completing the
classification. \(\square\)

## 4. Exact counterexample to uniform convergence

The strictly long-edge metric
\[
 w^0=(a,b,c)=(2/3,1/6,1/6)
\]
lies away from every chamber wall.  Formula (5) gives
\(\kappa_a=\kappa_b=\kappa_c=6/5\), so \(K=6/5\) and the normalized vector
field is exactly zero.  Its (locally smooth, constant) solution therefore has
\[
 \omega(w^0)=\{(2/3,1/6,1/6)\},
\]
not the uniform point.  This disproves the universal uniform-convergence
assertion, while leaving the requested global omega-limit classification for
non-fixed initial data unresolved.
