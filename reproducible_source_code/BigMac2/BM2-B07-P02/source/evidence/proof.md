# Exact proof certificate for DM07-02

Date: 2026-09-07  
Proposer job: `bigMac-00007-p02-research-b8551e73e224`

This certificate uses exactly the objects and normalization fixed in
`problem.md`.  Put \(S=a+b>0\), and write \(\Gamma=\mathbb Z/5\mathbb Z\).

## Theorem

For every \(a,b\geq 0\), not both zero,

\[
 \operatorname {SDP}_{\rm GL}(G_{a,b})=\psi(G_{a,b})
 =\frac{5\min\{a+2b,2a+b\}}{6(a+b)}. \tag{1}
\]

Regarding a cut as an unordered bipartition (so identifying a subset with
its complement), its complete optimality classification up to \(D_5\) is:

* if \(a>b\), including \(b=0\), precisely the orbit of the adjacent pair
  \(\{0,1\}\);
* if \(b>a\), including \(a=0\), precisely the orbit of the difference-two
  pair \(\{0,2\}\);
* if \(a=b>0\), every nontrivial cut.

Every nonzero translation-invariant GL-feasible semimetric has two positive
distances

\[
 u=d(0,1)=d(0,4),\qquad v=d(0,2)=d(0,3),
\]

and, modulo multiplication by a positive scalar, the complete optimality
classification is:

* if \(a>b\), precisely \(v=2u\);
* if \(b>a\), precisely \(u=2v\);
* if \(a=b>0\), every \((u,v)\) satisfying
  \(u,v>0\), \(u\leq2v\), and \(v\leq2u\).

## 1. Exact cut enumeration

For a subset \(A\), let \(c_i(A)\) be the number of crossing unordered
edges whose difference is \(\pm i\), for \(i=1,2\).  A crossing edge of
type 1 contributes its two directed orientations to the numerator, each
with joint probability \(a/(10S)\); similarly for type 2.  Hence, if
\(k=|A|\),

\[
 N_{a,b}(A)=\frac{a c_1(A)+b c_2(A)}{5S},\qquad
 D(A)=\frac{2k(5-k)}{25},
\]

and therefore

\[
 \psi_{G_{a,b}}(A)
 =\frac{5(ac_1(A)+bc_2(A))}{2S k(5-k)}. \tag{2}
\]

Complementation permits \(k\leq2\).  The dihedral group is transitive on
singletons, while its two orbits on two-element subsets are distinguished
by whether their difference is \(\pm1\) or \(\pm2\).  Direct counting gives

\[
\begin{array}{c|c|c}
A&(c_1,c_2)&\psi_{G_{a,b}}(A)\\ \hline
\{0\}&(2,2)&5/4\\
\{0,1\}&(2,4)&5(a+2b)/(6S)\\
\{0,2\}&(4,2)&5(2a+b)/(6S).
\end{array} \tag{3}
\]

If \(a>b\), the middle entry is strictly below both other entries: its
comparison with the last is equivalent to \(b<a\), and its comparison with
\(5/4\) is also equivalent to \(b<a\).  The symmetric statement holds when
\(b>a\).  If \(a=b>0\), all three entries equal \(5/4\).  This proves both
the cut value in (1) and the asserted exhaustive cut classification,
including \(a=0\), \(b=0\), and \(a=b\).

## 2. Translation averaging loses nothing

Let \(d(x,y)=\|p_x-p_y\|^2\) be an arbitrary GL-feasible semimetric, and
define

\[
 \bar d(x,y)=\frac15\sum_{c\in\Gamma}d(x+c,y+c). \tag{4}
\]

This is translation-invariant by reindexing \(c\).  It remains squared
Euclidean: in the orthogonal direct sum of five copies of the original
Euclidean space, set

\[
 q_x=5^{-1/2}(p_{x+c})_{c\in\Gamma}.
\]

Then \(\|q_x-q_y\|^2=\bar d(x,y)\).  Nonnegativity, symmetry, and zero
diagonal are preserved.  For each \(c\), the triangle inequality for
\((x+c,y+c,z+c)\) holds; averaging these five inequalities gives
\(\bar d(x,z)\leq\bar d(x,y)+\bar d(y,z)\).  Thus \(\bar d\) is
GL-feasible.

Uniform measure is invariant under translation, so finite-sum reindexing
gives

\[
\begin{aligned}
 N_{a,b}(\bar d)
 &=\mathbb E_{x,s,c}d(x+c,x+s+c)=N_{a,b}(d),\\
 D(\bar d)
 &=\mathbb E_{x,y,c}d(x+c,y+c)=D(d).
\end{aligned} \tag{5}
\]

In particular, a positive denominator stays positive and the objective
ratio is unchanged.  Since invariant feasible semimetrics are a subclass of
all feasible semimetrics and (4) maps every member of the larger class into
that subclass with the same objective, the two infima are equal.  This also
proves directly that no non-translation-invariant feasible semimetric can
improve the invariant optimum.

## 3. Fourier/CND cone and the full invariant GL cone

A translation-invariant symmetric hollow function on \(\Gamma^2\) has
circulant distance matrix with first row

\[
 (0,u,v,v,u). \tag{6}
\]

For completeness, a finite symmetric hollow matrix \(D\) is a squared
Euclidean distance matrix exactly when it is conditionally negative
semidefinite (CND):

\[
 z^{\mathsf T}Dz\leq0\quad\text{whenever }\sum_xz_x=0. \tag{7}
\]

The forward implication follows from
\(z^{\mathsf T}Dz=-2\|\sum_xz_xp_x\|^2\).  Conversely, with
\(J=I-\frac15\mathbf1\mathbf1^{\mathsf T}\), condition (7) says that
\(B=-\frac12JDJ\) is positive semidefinite.  Realize \(B\) as a Gram
matrix.  If \(r_x\) is the row mean of \(D\) and \(m\) its grand mean,
then
\(B_{xy}=-\frac12(D_{xy}-r_x-r_y+m)\), whence
\(B_{xx}+B_{yy}-2B_{xy}=D_{xy}\) because \(D_{xx}=D_{yy}=0\).
Thus its Gram vectors realize exactly \(D\).

Let \(\omega=e^{2\pi i/5}\).  The Fourier vectors
\((\omega^{kx})_{x\in\Gamma}\) diagonalize (6).  Its nonconstant
eigenvalues are

\[
 \lambda_k=2u\cos(2\pi k/5)+2v\cos(4\pi k/5),\qquad k=1,2,3,4. \tag{8}
\]

Writing \(\varphi=(1+\sqrt5)/2\), the exact identities
\(2\cos(2\pi/5)=1/\varphi\) and
\(2\cos(4\pi/5)=-\varphi\) give

\[
 \lambda_1=\lambda_4=u/\varphi-\varphi v,
 \qquad
 \lambda_2=\lambda_3=-\varphi u+v/\varphi. \tag{9}
\]

The four Fourier vectors span the real zero-sum subspace (using real and
imaginary parts), so (7)--(9) prove the exact squared-Euclidean/CND
conditions

\[
 u\geq0,\quad v\geq0,\quad
 u\leq\varphi^2v,\quad v\leq\varphi^2u. \tag{10}
\]

Here nonnegativity is included because the object is a semimetric.

Every triangle of three distinct vertices has distance multiset either
\(\{u,u,v\}\) (represented by \(0,1,2\)) or \(\{u,v,v\}\) (represented
by \(0,1,3\)); repeated-vertex triangles are automatic.  Consequently all
triangle inequalities are equivalent to

\[
 u\geq0,\quad v\geq0,\quad v\leq2u,\quad u\leq2v. \tag{11}
\]

Since \(\varphi^2=(3+\sqrt5)/2>2\), (11) implies both nontrivial
inequalities in (10).  Conversely every GL semimetric must satisfy (11).
Thus the full translation-invariant GL cone is exactly (11), not merely a
necessary relaxation.  Its only point with \(u=0\) or \(v=0\) is the zero
semimetric; every nonzero point has \(u,v>0\).

## 4. Exact cone optimization and all equality cases

For (6), direct counting over the two steps and all ordered pairs gives

\[
 N_{a,b}(d)=\frac{au+bv}{S},\qquad
 D(d)=\frac{2(u+v)}5,
\]

so

\[
 R_{a,b}(u,v)=\frac{5(au+bv)}{2S(u+v)}. \tag{12}
\]

On a nonzero ray of (11), put \(r=u/(u+v)\).  The two inequalities in
(11) are exactly \(1/3\leq r\leq2/3\), and

\[
 \frac{au+bv}{u+v}=b+(a-b)r. \tag{13}
\]

If \(a>b\), (13) has the unique projective minimizer \(r=1/3\), namely
\(v=2u\), and (12) equals \(5(a+2b)/(6S)\).  This includes \(b=0\).
If \(b>a\), its unique projective minimizer is \(r=2/3\), namely
\(u=2v\), and the value is \(5(2a+b)/(6S)\); this includes \(a=0\).
If \(a=b>0\), (13) is constant and every nonzero ray of (11) is optimal,
with value \(5/4\).  This proves the complete invariant-semimetric
classification.

The endpoint rays are attained, for example, by translation-averaging cut
metrics: averaging the cut metric of \(\{0,1\}\) yields
\((u,v)=(2/5,4/5)\), and averaging that of \(\{0,2\}\) yields
\((u,v)=(4/5,2/5)\).  More generally every cut metric is GL-feasible
(embed \(x\mapsto1_A(x)\in\mathbb R\)), so always
\(\operatorname {SDP}_{\rm GL}\leq\psi\).  Equations (4)--(13) give the
reverse lower bound equal to the cut value from (3).  Equality (1) follows.

## 5. Boundary audit and source comparison

* \(a>0,b=0\): the value is \(5/6\); only adjacent-pair cuts and the ray
  \(v=2u\) are optimal.
* \(a=0,b>0\): the value is \(5/6\); only difference-two-pair cuts and the
  ray \(u=2v\) are optimal.  Relabeling by multiplication by 2 exchanges
  the two faces.
* \(a=b>0\): the graph is the equally weighted complete graph on five
  vertices; the value is \(5/4\), every nontrivial cut is optimal, and every
  nonzero ray of (11) is optimal.

The primary-source screen was refreshed on 2026-09-07.  Stamoulis,
arXiv:2609.05368v1 (submitted 2026-09-04), Proposition 6.1 proves the two
one-weight cycle faces, and Lemma 4.1 explains why the single regular-pentagon
squared-chord character metric is infeasible.  Theorem 1.1/4.6 requires a
minimizing character with image size at most four, whereas every nontrivial
character of \(\mathbb Z/5\mathbb Z\) has image size five, so that theorem
does not imply the interior two-weight result.  Searches restricted to
primary arXiv records for the exact formula and equivalent combinations of
"Goemans--Linial", weighted \(C_5\), \(\mathbb Z/5\mathbb Z\), and
two-weight Cayley terminology returned no formula-level match.  This is a
limited absence-of-match report, not a priority or novelty proof.

Primary source: <https://arxiv.org/abs/2609.05368v1>.

## Gap list

No mathematical gap is known in the proof above.  The claimed scope still
requires a fresh referee pass under the project workflow.  The literature
screen is necessarily limited by the source's recency and does not certify
novelty.
