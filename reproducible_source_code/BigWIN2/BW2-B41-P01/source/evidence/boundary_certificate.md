# Exact RP certificate for the boundary and Hamiltonian reduction below it

This note proves the frozen assertion.  Put \(L=\ell\).

## 1. The boundary \(m=2L+3\)

Let
\[
 D=(L+2)(3L+4),\qquad A=3L+4,
\]
and give the seven edge orbits of \(J_{2L+3,L}\) the following rational
marginals:
\[
\begin{array}{c|ccccccc}
\text{orbit}&BB&aX&b_i x_i&UU&Ua&UB&UX\\ \hline
x_e&\displaystyle {3L^2+9L+8\over2(L+1)D}&
\displaystyle {3L+5\over D}&1-{1\over D}&
\displaystyle {1\over D}&\displaystyle {1\over D}&
\displaystyle {1\over D}&\displaystyle {1\over L+2}.
\end{array}
\tag{1}
\]
Here `BB` means an edge between two \(b\)'s, `UU` an edge between two
\(u\)'s, and similarly for the other columns.  All entries are positive.
Direct substitution, with \(m=2L+3\), gives
\[
 x(E)=2m+L=|V|-1.                                      \tag{2}
\]
The incident sums at \(a\), at every \(b_i\), at every \(x_i\), and at
every \(u_j\), respectively, are
\[
 2-{1\over D},\qquad 2-{1\over D},\qquad
 2-{1\over L+2},\qquad 2-{1\over D}.                  \tag{3}
\]
Thus it remains only to check the spanning-tree-polytope rank inequalities.

For a proper vertex subset \(S\) of size at least two, write
\[
 \alpha=\mathbf 1_{a\in S},\quad
 k=|S\cap B|,\quad h=|S\cap X|,\quad z=|S\cap U|,
\]
and let \(d\) be the number of indices with both \(b_i,x_i\in S\).  Then
\[
\begin{split}
x(E[S])={}&{3L^2+9L+8\over2(L+1)D}{k\choose2}
 +{3L+5\over D}\alpha h+\left(1-{1\over D}\right)d\\
&+{1\over D}\left[{z\choose2}+z\alpha+zk\right]
 +{1\over L+2}zh.                                     \tag{4}
\end{split}
\]
For fixed \(\alpha,k,h,z\), this is largest when
\(d=\min(k,h)\), a value which is attainable.  Put
\[
 P={3L^2+9L+8\over2(L+1)}
\]
and let \(\Phi=D(|S|-1-x(E[S]))\) after this worst-case substitution.
If \(k\le h\), then
\[
 \Phi=D(\alpha+h+z-1)-P{k\choose2}-(A+1)\alpha h
 -{z\choose2}-z\alpha-zk-Azh+k,                       \tag{5}
\]
whereas if \(h\le k\), then
\[
 \Phi=D(\alpha+k+z-1)-P{k\choose2}-(A+1)\alpha h
 -{z\choose2}-z\alpha-zk-Azh+h.                       \tag{6}
\]

Here is a complete endpoint check.  In (5), the coefficient of \(h\) is
\[
 D-(A+1)\alpha-Az\ge A-1>0,
\]
so its minimum occurs at \(h=k\), except that the lower size boundary
\(|S|=2\) can force \((k,h)=(0,1)\) or \((0,2)\).  In (6), the coefficient
of \(h\) is \(1-(A+1)\alpha-Az\).  It is positive only when
\(\alpha=z=0\), giving \(h=0\); otherwise it is negative, giving \(h=k\).
The only exception is the deleted full-set point, where the adjacent value
\((k,h)=(m,m-1)\) must also be checked.

On the diagonal \(h=k\), (5)--(6) are concave quadratic functions of
\(k\).  On the exceptional branch \(\alpha=z=h=0\), (6) is also concave
in \(k\).  Hence only interval endpoints occur.  At either resulting
endpoint the expression is concave in \(z\).  The lower size boundary and
the omitted full set add only their adjacent lattice points.  After removing
duplicates, the endpoint values that are not visibly larger copies are the
following.  This table is also a record of all boundary exceptions.

\[
\begin{array}{c|c|c}
\text{case}&\text{conditions when needed}&\Phi\\ \hline
(\alpha,z,k,h)=(0,0,1,1)&&1\\
(0,0,0,2)&&D\\
(0,0,2,0)&&\displaystyle{6L^3+23L^2+27L+8\over2(L+1)}\\
(1,0,0,1)&&3L^2+7L+3\\
(0,1,0,1),(0,1,1,1),(1,0,1,1)&& (L+1)(3L+4)\\
k=0,z=2,\alpha=0&L\ge2&D-1\\
k=0,z=L,\alpha=0&L\ge2&\displaystyle{(L-1)(6L^2+19L+16)\over2}\\
k=0,z=1,\alpha=1&&D-1\\
k=0,z=L,\alpha=1&&\displaystyle{L(2L+3)(3L+5)\over2}\\
k=h=m,z=0,\alpha=0&&\displaystyle{(L+1)(L+2)(6L+7)\over2}\\
k=h=m,z=L,\alpha=0&&(L+1)(3L+7)\\
k=h=m,z=0,\alpha=1&&\displaystyle{L(2L+3)(3L+5)\over2}\\
k=h=m,z=L-1,\alpha=1&&(L+1)(3L+7)\\
\alpha=1,z=L,\ (k,h)=(m-1,m-1)\text{ or }(m,m-1)
&&(L+1)(3L+4).
\end{array}                                                    \tag{7}
\]
Every entry in (7) is at least one for \(L\ge1\) (the two rows marked
\(L\ge2\) only occur in that range).  The unique smallest displayed value
comes from \(S=\{b_i,x_i\}\).  Consequently every proper nontrivial
subset satisfies
\[
 x(E[S])\le |S|-1-{1\over D}<|S|-1.                    \tag{8}
\]
Equations (2), (8), and positivity put (1) in the relative interior of the
spanning-tree polytope.  Its incident sums (3) are all strictly below two.
The spanning-tree characterization in the frozen problem therefore proves
that \(J_{2L+3,L}\) is RP.

## 2. The range \(m\le2L+2\)

In fact, every \(J_{m,L}\) in this smaller range has a Hamiltonian cycle.
Here are explicit constructions.  Think first of the cyclic list
\[
 c_0=a,c_1=u_1,\ldots,c_L=u_L,c_0.
\]
When \(L=1\), its two directed positions are treated as the two internally
disjoint arcs between \(a\) and \(u_1\).

If \(m=2r\), where \(1\le r\le L+1\), replace any \(r\) successive cyclic
positions \(c_{j-1}c_j\) by
\[
 c_{j-1},x_{2j-1},b_{2j-1},b_{2j},x_{2j},c_j,          \tag{9}
\]
and retain the other positions.  Every consecutive pair in the resulting
cyclic list is an edge of \(J_{m,L}\), and every vertex occurs once.

If \(m=2r+1\), then \(1\le r\le L\).  For \(L=1\) (necessarily \(m=3\))
use
\[
 a,x_1,b_1,b_2,b_3,x_3,u_1,x_2,a.                     \tag{10}
\]
For \(L\ge2\), replace the position \(c_0c_1\) by
\[
 c_0,x_1,b_1,b_2,b_3,x_3,c_1,
\]
replace \(c_1c_2\) by \(c_1,x_2,c_2\), and replace any
\(r-1\) of the remaining cyclic positions by the pair blocks (9), using
the still unused consecutive index pairs \((4,5),(6,7),\ldots,(2r,2r+1)\).
Retain all other cyclic positions.  This is again a Hamiltonian cycle.

Finally, if a graph on \(n\) vertices has a Hamiltonian cycle, uniformly
delete one of its \(n\) edges.  The resulting distribution on spanning
paths has expected degree \(2-2/n<2\) at every vertex.  Mixing it with an
arbitrarily small positive multiple of the uniform distribution on all
spanning trees gives full support while preserving all strict degree
inequalities.  Thus every Hamiltonian graph is RP.  This handles
\(m\le2L+2\), and Section 1 handles the remaining boundary.

## Reproducibility

`exact_boundary_verify.py` checks (1)--(4) with exact rational arithmetic,
enumerates every subset descriptor (including every feasible value of
\(d\)) for a stated finite regression range, and confirms the minimum rank
slack.  The infinite-family proof is the endpoint argument (5)--(7), not the
finite regression.
