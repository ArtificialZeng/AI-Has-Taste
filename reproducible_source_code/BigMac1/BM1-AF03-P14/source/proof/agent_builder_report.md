# Proof-builder report: exact reduction for central sections of \(Q_5\)

Date: 2026-08-29 (Asia/Shanghai)  
Role: proof builder  
Status: structural reduction and a certified symmetric sub-class; **not** a
complete solution of the \(Q_5\) classification.

## 1. Provenance and conventions

The truncated-power formula below is derived from the definition, not imported
from a discovery computation.  For the \(n=4\) baseline I compared the
derivation with G. Ambrus, *Critical central sections of the cube*,
[arXiv:2107.14778](https://arxiv.org/abs/2107.14778), especially Theorems 1--3
and equations labelled `(a1a2)`, `(caseA)`--`(caseD)` in its TeX source.  That
paper uses \([-1,1]^n\); this report uses the problem's cube
\(Q_n=[-1/2,1/2]^n\).  Directions are unchanged, while section volumes and
their Hessians are rescaled.

All symbolic factorizations stated below have rational coefficients.  The
calculations used to find them were re-expanded and checked symbolically, but
no floating-point root or optimizer output is used as proof.  In particular,
the two computer-algebra assertions left informal in the published \(n=4\)
argument are replaced below by elementary one-variable factorizations.

## 2. Section volume from coarea and inclusion--exclusion

Let \(a=(a_1,\ldots,a_s)\in\mathbb R_{>0}^s\), put

\[
 R=\|a\|_2,\qquad A=\sum_i a_i,\qquad a_S=\sum_{i\in S}a_i.
\]

Let \(U_i\) be independent uniform random variables on \([-1/2,1/2]\),
and \(Z=\sum_i a_iU_i\).  The coarea formula gives

\[
 f_Z(t)=\int_{[-1/2,1/2]^s}\delta(t-a\cdot x)\,dx
       ={1\over R}\mathcal H^{s-1}
          \bigl(Q_s\cap\{a\cdot x=t\}\bigr).
\tag{2.1}
\]

After translating, \(Y_i=a_i(U_i+1/2)\) is uniform on \([0,a_i]\) and
\(Z=\sum_iY_i-A/2\).  Inclusion--exclusion on the simplex gives

\[
 \Pr\!\left(\sum_iY_i\le x\right)
 ={1\over s!\prod_i a_i}
 \sum_{S\subseteq[s]}(-1)^{|S|}(x-a_S)_+^s.
\]

Differentiating (the identity also holds at knots by continuity) and using
(2.1) at \(t=0\) yields the exact scale-invariant formula

\[
 \boxed{
 F_s(a)={R\over (s-1)!\prod_i a_i}
 \sum_{S\subseteq[s]}(-1)^{|S|}
       \left({A\over2}-a_S\right)_+^{s-1}.}
\tag{2.2}
\]

If a normal in \(Q_n\) has exactly \(s\) nonzero coordinates, its section is
the product of the corresponding section of \(Q_s\) with a unit cube, so its
volume is exactly \(F_s\).  This proves the support convention in the formal
statement.

The expression is homogeneous of degree zero.  Hence Euler's identity gives
\(a\cdot\nabla F_s=0\) wherever it is differentiable.  Consequently an
interior point is critical on the sphere if and only if its ordinary Euclidean
gradient (of the scale-invariant extension) vanishes.

For \(s=5\), the function \(x\mapsto x_+^4\) is \(C^3\), so (2.2) is
\(C^3\) throughout the positive orthant, including every subset-sum wall.
Thus every full-support local extremum satisfies the ordinary critical
equations and has a well-defined Hessian.  This statement does not apply
unchanged across zero-coordinate strata; those are handled by restriction to
their support.

If \(a_1\ge\sum_{i>1}a_i\), direct parametrization of the section by
\((x_2,\ldots,x_s)\) gives

\[
 F_s(a)={\|a\|_2\over a_1}.
\tag{2.3}
\]

In the strict dominant region this has no full-support spherical critical
point.  At the equality wall it is still differentiable for \(s=5\), and its
tangential derivative is nonzero unless all other coordinates vanish.
Therefore every full-support critical point for \(Q_5\) obeys the strict
balance inequality

\[
 a_i<\sum_{j\ne i}a_j\quad(1\le i\le5).
\tag{2.4}
\]

## 3. Exact reconstruction of the \(n=4\) baseline

### 3.1 Piecewise polynomial and critical equations

Take \(0<a\le b\le c\le d\), assume \(a^2+b^2+c^2+d^2=1\), and use
the strict balance \(d<a+b+c\).  Set \(T=(a+b+c+d)/2\).  Pairing a subset
with its complement in (2.2) gives

\[
 P_4=T^3-\sum_{q\in\{a,b,c,d\}}(T-q)^3
 +|T-a-b|^3+|T-a-c|^3+|T-a-d|^3,
\qquad
 F_4={P_4\over6abcd}.
\tag{3.1}
\]

(The norm factor is one on the displayed sphere; off the sphere it is
\(R P_4/(6abcd)\).)  The first two absolute-value arguments in (3.1) are
nonnegative by the ordering; only \(T-a-d=(b+c-a-d)/2\) changes sign.

For completeness, the direct integration of the triangular density of
\(b_3X_3+b_4X_4\) gives the following four exact comparison equations.  Here
\(0<b_1\le b_2\), \(0<b_3\le b_4\), and unequal \(b_1,b_2\) are assumed
when the common factor \(b_2-b_1\) has been cancelled:

\[
\begin{array}{ll}
\mathrm A:&(b_1+b_2+b_3-b_4)^2(1+b_1b_2)
 =8b_1b_2b_3(b_1+b_2),\\[2mm]
\mathrm B:&(b_2^2-b_1^2)(1+b_2^2-2b_2(b_3+b_4))
 =(1-b_2^2)(b_3-b_4)^2,\\[2mm]
\mathrm C:&b_1+b_2-b_4-b_1b_2^2-b_1^2b_2-b_1b_2b_4=0,\\[2mm]
\mathrm D:&8b_1b_3b_4(1-b_2^2)
 -(b_1-b_2+b_3+b_4)^2
 (b_1+b_2-b_1^2b_2-b_1b_2^2)=0.
\end{array}
\tag{3.2}
\]

These identities can also be obtained by differentiating the two polynomial
pieces of (3.1).  They therefore do not require a probabilistic regularity
assumption beyond the already proved \(C^2\) regularity of (3.1).

### 3.2 Exact solution of the full-support equations

If \(a+d\le b+c\), the three Case-C substitutions used in the source give,
when \(b,c,d\) are distinct,

\[
 (b-c)^2+(b-d)^2+(c-d)^2=-2a^2,
\]

which is impossible.  If \(b=c<d\), (3.2C) gives
\(d(1-2b^2-bd)=0\); normalization turns the second factor into
\(a^2+d(d-b)>0\), again impossible.  Hence \(c=d\).  Equation (3.2B)
then forces \(a=b\) (the alternative is
\(a^2+2(b-c)^2=0\)).  Finally (3.2C) gives either \(a=c\), or

\[
 1-ac-2c^2=0.
\]

Together with \(2a^2+2c^2=1\), the latter is \(a(2a-c)=0\), so \(c=2a\).

If \(a+d\ge b+c\), subtracting pairs of Case-D equations gives

\[
 (a+b+c-d)^2(a-b)\bigl(d(a+b+d)-1\bigr)=0
\tag{3.3}
\]

and its analogues for the three pairs among \(a,b,c\).  Balance makes the
first factor nonzero.  If \(a,b,c\) were all distinct, (3.3) would equate
three different pair sums, a contradiction.  Thus at least two are equal.

Suppose exactly two are equal.  By the symmetry of these three equations,
write \(a=b=x\), \(c=y\), \(d=z\).  Then

\[
 z(x+y+z)=1,\qquad 2x^2+y^2+z^2=1.
\tag{3.4}
\]

Put \(r=y/x>0\).  Subtracting (3.4) gives
\(z/x=(r^2+2)/(r+1)\).  After this substitution, Case A is equivalent,
up to a strictly positive denominator, to

\[
 r(r-2)\bigl(10r^4+7r^3+15r^2-5r+4\bigr)=0.
\tag{3.5}
\]

The quartic factor is positive for \(r>0\), since
\(10r^4+7r^3>0\) and \(15r^2-5r+4>0\) (negative discriminant).
Thus \(r=2\), and (3.4) gives \(z=y=2x\).

If \(a=b=c=x\), put \(r=d/x\).  Ordering and balance give
\(1\le r<3\).  The remaining Case-D equation is equivalent to

\[
 (r-1)\bigl(r^4-5r^3+6r^2-3r-3\bigr)=0.
\tag{3.6}
\]

The second factor is negative on \([1,3)\): on \([1,2]\), writing
\(t=r-1\in[0,1]\) makes it
\(t^4-t^3-3t^2-2t-4<0\); on \([2,3)\) it is
\(r^2(r-2)(r-3)-3(r+1)<0\).  Hence \(r=1\).

This supplies an exact replacement for the two unrecorded CAS eliminations in
the source proof.  Together with the lower-support \(n\le3\) classification,
the complete list is therefore the diagonal directions and

\[
 p={1\over\sqrt{10}}(1,1,2,2)
\tag{3.7}
\]

up to signed permutations.

### 3.3 Exact Hessian at the non-diagonal point

The point (3.7) lies on two pair-sum walls.  Since \(|x|^3\) is \(C^2\)
and its second derivative vanishes at zero, either adjacent polynomial gives
the same Hessian.  In the coordinate order \((1,1,2,2)/\sqrt{10}\), the
ambient Hessian of the scale-invariant \(F_4\) is

\[
 \sqrt{10}\begin{pmatrix}
 -1/8&7/24&-1/24&-1/24\\
 7/24&-1/8&-1/24&-1/24\\
 -1/24&-1/24&-1/2&13/24\\
 -1/24&-1/24&13/24&-1/2
 \end{pmatrix}.
\tag{3.8}
\]

Its radial eigenvalue is zero.  On the orthonormal tangent vectors parallel
to

\[
 (1,-1,0,0),\qquad(0,0,1,-1),\qquad(2,2,-1,-1),
\]

the eigenvalues are, respectively,

\[
 -{5\sqrt{10}\over12},\qquad
 -{25\sqrt{10}\over24},\qquad
 {5\sqrt{10}\over24}.
\tag{3.9}
\]

Thus the non-diagonal critical direction is rigorously a saddle.  At the
4-diagonal direction the tangent Hessian is \(-4/3\) times the identity.
At the 3-diagonal direction the Hessian vanishes, but along the scale-free
path \((1+u,1+u,1-2u)\) the section volume is

\[
 {3\sqrt3(2u+1)\sqrt{2u^2+1}\over4(1+u)^2}
 ={3\sqrt3\over4}+{3\sqrt3\over2}u^3+O(u^4),
\tag{3.10}
\]

so opposite signs of small \(u\) prove it is a saddle.  The 1-diagonal and
2-diagonal directions are the known global minimum and maximum, respectively.

## 4. Full-support chamber reduction for \(Q_5\)

Use signed permutations to arrange

\[
 a_1\ge a_2\ge a_3\ge a_4\ge a_5>0,
 \qquad S=\sum_i a_i^2,qquad T={1\over2}\sum_i a_i,
\]

and impose balance (2.4).  Define

\[
 L_{ij}=T-a_i-a_j,qquad
 \psi(x)=\operatorname{sgn}(x)x^4=x|x|^3,\quad \psi(0)=0.
\]

Pairing complementary subsets in (2.2) gives the global positive-orthant
formula

\[
 \boxed{
 P=T^4-\sum_{i=1}^5(T-a_i)^4+\sum_{1\le i<j\le5}\psi(L_{ij}),
 \qquad
 F_5(a)={\sqrt S\,P\over24\prod_i a_i}.}
\tag{4.1}
\]

Here \(\psi\in C^3\), with
\(\psi'(x)=4|x|^3\), \(\psi''(x)=12x|x|\), and
\(\psi'''(x)=24|x|\).  Thus (4.1) is also an exact formula on the walls.

In a strict chamber let

\[
 N=\{ij:a_i+a_j>T\}=\{ij:L_{ij}<0\}.
\]

Then

\[
 P_N=T^4-\sum_i(T-a_i)^4+\sum_{i<j}L_{ij}^4
      -2\sum_{ij\in N}L_{ij}^4.
\tag{4.2}
\]

There are exactly six possible strict chambers in the ordered balanced cone:

\[
 \boxed{
 \varnothing,\quad
 \{12\},\quad
 \{12,13\},\quad
 \{12,13,14\},\quad
 \{12,13,14,15\},\quad
 \{12,13,23\}.}
\tag{4.3}
\]

Proof: ordering makes \(N\) a shifted family of two-subsets (replacing an
index by a smaller index cannot decrease the pair sum).  Two disjoint pairs
cannot both lie in \(N\), because their four coordinates would sum to more
than \(2T=\sum_i a_i\), while the fifth coordinate is positive.  A shifted,
pairwise-intersecting family of edges is either an initial star
\(\{12,13,\ldots,1k\}\) or the triangle \(\{12,13,23\}\).  This gives
(4.3), including the empty star.  Wall strata are obtained by replacing any
of the strict pair inequalities by equalities and taking compatible
intersections of the closures.

Let \(P_i=\partial_iP\) and \(P_{ij}=\partial_i\partial_jP\), computed from
(4.1) on walls or from (4.2) in a chamber.  The full-support critical equations
are the homogeneous degree-six polynomial equations

\[
 \boxed{G_i:=a_iS P_i+(a_i^2-S)P=0\quad(1\le i\le5).}
\tag{4.4}
\]

One equation is dependent by homogeneity.  Thus an exact chamber computation
may set, for example, \(a_5=1\), solve four equations, and retain only positive
solutions satisfying that chamber's exact linear inequalities.  No division
by a wall form occurs in (4.4).

At a critical point, the intrinsic Hessian is the restriction to
\(a^\perp\) of \(F_5 M\), where

\[
 M_{ij}={\delta_{ij}\over S}-{2a_ia_j\over S^2}
       +{P_{ij}\over P}-{P_iP_j\over P^2}
       +{\delta_{ij}\over a_i^2}.
\tag{4.5}
\]

Equations (4.1)--(4.5) are an exact finite algebraic reduction of the
full-support problem.  On a fixed chamber, derivatives can be reconstructed
term by term from

\[
 \partial_i(c\ell^4)=4c\ell^3\partial_i\ell,qquad
 \partial_{ij}(c\ell^4)=12c\ell^2
   (\partial_i\ell)(\partial_j\ell)
\]

for its linear forms \(\ell\).  At a wall the corresponding first and second
derivatives vanish, consistently from either side.

## 5. Exact theorem for all full-support two-value directions

This section is a complete, non-numerical sub-classification.

Let a direction have \(m\) copies of a larger value \(r\) and \(5-m\)
copies of \(1\), with \(r\ge1\) and \(1\le m\le4\).  Scaling has been fixed
only for the calculation.  Put \(q=5-m\), \(S_m=mr^2+q\), and let
\(P_m(r)\) be (4.1)'s polynomial.  Since coordinates inside each block have
equal gradient by symmetry, Euler homogeneity shows that this direction is a
full critical point if and only if

\[
 E_m(r):=rS_mP_m'(r)-m\bigl((m-1)r^2+q\bigr)P_m(r)=0.
\tag{5.1}
\]

Direct expansion in the indicated exact chambers gives:

\[
\begin{array}{c|c|c|c}
m&\text{range}&P_m(r)&E_m(r)\\ \hline
1&1\le r\le2&\frac{r(3r^3-16r^2+128)}8
 &\frac32r^4(r-3)(r-1)\\
1&2\le r<4&-\frac{r^4-16r^3+96r^2-256r+64}{8}
 &-\frac12h_1(r)\\
2&1\le r\le\frac32&
 \frac{16r^4-96r^3+216r^2-24r+3}{8}
 &\frac34(r-1)h_2(r)\\
2&r\ge\frac32&\frac{3(32r-13)}4
 &\frac32(13r^2-48r+39)\\
3&1\le r\le2&
 \frac{3r^4-24r^3+216r^2-96r+16}{8}
 &\frac34(r-1)h_3(r)\\
3&r\ge2&2(9r^2-2)&-12(r^2-2)\\
4&r\ge1&\frac{128r^3-16r+3}{8}
 &-\frac32(r-1)(3r-1),
\end{array}
\tag{5.2}
\]

where

\[
\begin{aligned}
h_1&=r^6-12r^5+51r^4-96r^3+96r^2-64,\\
h_2&=16r^5-48r^4+40r^3-8r^2-9r+3,\\
h_3&=3r^5-9r^4-8r^3+40r^2-48r+16.
\end{aligned}
\]

The balance endpoint \(r<4\) in the \(m=1\) row comes from (2.4).
The chamber-wall values agree because (4.1) is \(C^3\).

For auditability, exact Sturm sign vectors for the only three unresolved
intervals in (5.2) are

\[
\begin{array}{c|c|c|c|c}
\text{polynomial}&[u,v]&\operatorname{sgn}\mathcal S(u)&
\operatorname{sgn}\mathcal S(v)&V(u)-V(v)\\ \hline
h_1&[2,4]&(+, +, -, +, +, +, +)&(+,0,-,-,-,+,+)&2-2=0\\
h_2&[1,3/2]&(-,-,+,+,-,-)&(-,-,+,+,-,-)&2-2=0\\
h_3&[1,2]&(-,-,+,+,-,-)&(-,-,+,+,-,-)&2-2=0.
\end{array}
\tag{5.3}
\]

Here \(\mathcal S\) is the standard Sturm chain \((h,h',-\mathrm{rem},\ldots)\).
To make (5.3) independently reconstructible, convenient positively rescaled
chains are listed next (multiplying an entire entry by a positive rational
does not change any sign):

\[
\begin{aligned}
\mathcal S_1={}&\bigl(
h_1,
6r(r-4)^2(r^2-2r+2),
3r^4-20r^3+32r^2-64r+64,\\
&-{4\over3}(5r^3+40r^2-272r+320),
-{144\over5}(19r^2-92r+100),
{16\over361}(379r-540),
{30982464\over143641}\bigr),\\[1mm]
\mathcal S_2={}&\bigl(
h_2/16,
(80r^4-192r^3+120r^2-16r-9)/16,\\
&(44r^3-60r^2+57r-12)/100,
25(468r^2-548r+153)/1936,\\
&-121(1849r-522)/684450,
-3042038025/6618798736\bigr),\\[1mm]
\mathcal S_3={}&\bigl(
h_3/3,
(15r^4-36r^3-24r^2+80r-48)/3,\\
&4(47r^3-132r^2+180r-64)/75,
100(1419r^2-1700r+876)/6627,\\
&-70688(6871r-1968)/151017075,
-795490832400/104288305969\bigr).
\end{aligned}
\tag{5.4}
\]

It follows from (5.2)--(5.4) that, besides \(r=1\), the sole two-value
full-support critical orbit is

\[
 \boxed{
 \alpha={24+\sqrt{69}\over13},\qquad
 v_\alpha={1\over\sqrt{2\alpha^2+3}}
             (\alpha,\alpha,1,1,1).}
\tag{5.5}
\]

Indeed, the other root \((24-\sqrt{69})/13\) of the quadratic in the
\(m=2\) row is below \(3/2\), whereas \(\alpha>3/2\).  The point (5.5) lies
strictly in chamber \(N=\{12\}\).

The Hessian at (5.5) is also exact.  Under the stabilizer
\(S_2\times S_3\), the tangent space splits into the large-block difference
(dimension 1), small-block differences (dimension 2), and the block-contrast
line (dimension 1).  With \(S_\alpha=2\alpha^2+3\), the corresponding
eigenvalues are

\[
\begin{aligned}
\lambda_L&=-{3\sqrt{S_\alpha}\over32\alpha^4}
 (16\alpha^4-32\alpha^3+37\alpha^2-32\alpha+13),\\
\lambda_S&=-{\sqrt{S_\alpha}\over16\alpha^2}
 (5\alpha^2-16\alpha+14)\quad\text{(multiplicity 2)},\\
\lambda_B&={\sqrt{S_\alpha}\over32\alpha^4}
 (32\alpha^3-65\alpha^2+96\alpha-117).
\end{aligned}
\tag{5.6}
\]

All three parenthesized quantities are positive.  Reduction by
\(13\alpha^2-48\alpha+39=0\) gives, respectively,

\[
 {4099726+473008\sqrt{69}\over28561},\qquad
 {599+32\sqrt{69}\over169},\qquad
 {188646+33168\sqrt{69}\over2197}.
\]

Thus \(\lambda_L,\lambda_S<0<\lambda_B\): the sole non-diagonal critical
point in the complete two-value class is an exact saddle, not a local
extremum.

## 6. Support strata and the diagonal points in \(Q_5\)

Restriction gives a useful exact obstruction: if a point of \(S^4\) is a
local extremum, then its restriction to the coordinate subsphere determined
by its support is a local extremum of the corresponding \(F_s\).  The
\(s\le4\) classification above therefore proves:

\[
 \boxed{\text{Every non-diagonal local extremum of }Q_5,
 \text{ if one exists, has full support.}}
\tag{6.1}
\]

The embedded support-four non-diagonal point remains a saddle because its
support-tangent Hessian already has both signs by (3.9).

For reference, the diagonal strata behave as follows.

* \(d_1\) is a global minimum and \(d_2\) a global maximum (the classical
  cube-section extremal theorems).
* \(d_3\) is a saddle by the exact support-three path (3.10).
* \(d_4=(1,1,1,1,0)/2\) is a saddle in \(Q_5\).  It has decreasing tangent
  directions by the \(-4/3\) support Hessian, while the transverse path
  \((1,1,1,1,t)\), \(t>0\), has

  \[
  F_5(1,1,1,1,t)
  ={\sqrt{t^2+4}(3t^3-16t^2+128)\over192}
  ={4\over3}+{t^3\over32}+O(t^4),
  \]

  and therefore increases for all sufficiently small positive \(t\).
* At \(d_5=(1,1,1,1,1)/\sqrt5\), direct use of the all-positive-pairs
  polynomial gives the ambient Hessian with diagonal entries
  \(-\sqrt5/8\) and off-diagonal entries \(\sqrt5/32\).  Its radial
  eigenvalue is zero and all four tangent eigenvalues are
  \(-5\sqrt5/32\).  Thus \(d_5\) is a strict local maximum.

Hence, if the target conjecture is true, the final list of local extrema in
\(Q_5\) will be exactly \(d_1,d_2,d_5\) up to signed permutations.

## 7. Remaining proof gaps and next exact test

The original \(Q_5\) problem is not solved by this report.  The unresolved
set is now sharply delimited:

1. solve (4.4) for full-support normals with three, four, or five distinct
   coordinates in the six strict chambers (4.3);
2. solve all compatible pair-wall intersections, including coincident walls
   caused by repeated coordinates;
3. certify every real solution by rational/algebraic isolating data and exact
   chamber inequalities;
4. prove an indefinite Hessian for every non-diagonal solution, or, for a
   degenerate Hessian, decide the local inequality from the first nonzero
   higher-order piece.

The next discriminating exact computation is to set \(a_5=1\), construct the
four independent equations (4.4) for each of the six \(P_N\), saturate by
\(P\prod_i a_i\) and by the strict wall forms appropriate to the chamber,
and compute a rational univariate representation.  Discovery output alone is
not a certificate: a second verifier must reconstruct the polynomials from
(4.2), check the elimination identity, isolate all real roots, and reject any
root failing the order, positivity, balance, or chamber signs.

No Lean, Coq, Isabelle, or other proof assistant was used in this builder
work.
