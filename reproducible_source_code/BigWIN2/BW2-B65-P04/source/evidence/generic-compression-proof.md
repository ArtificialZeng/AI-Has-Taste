# Generic compression proof for the pure \(C_3/C_4\) family

This note proves the frozen assertion.  All dimension arguments may be made
over an algebraically closed field of characteristic zero.  The final
nonvanishing statement then has a rational, hence real, specialization.

## 1. Symmetric-product theorem

Let \(D=sC_3\sqcup tC_4\) have \(N=3s+4t\) vertices and edges, and let
\(z_1,\ldots,z_N\) be generic vectors in a vector space of dimension \(a\).
Put \(T_a=a(a+1)/2\).

**Theorem.**  If \(N\leq T_a\), then the tensors
\[
             \{z_i\odot z_j:ij\in E(D)\}
\]
are linearly independent in \(\operatorname{Sym}^2 K^a\).

Write \(Z\) for the matrix whose rows are the \(z_i\).  A relation among the
displayed tensors is, up to harmless nonzero factors on off-diagonal entries,
a nonzero symmetric matrix \(C\) supported on the edges of \(D\) such that
\[
                         Z^{\mathsf T}CZ=0.                 \tag{1}
\]
Let \(L_D\) be the \(N\)-dimensional space of all such supported symmetric
matrices.  We show by an incidence-dimension calculation that a generic
\(Z\) satisfies (1) for no nonzero \(C\in L_D\).

### Compression codimension

Fix a symmetric matrix \(C\) of rank \(r\).  After congruence it is
\(\operatorname{diag}(I_r,0)\).  If \(X\) denotes the first \(r\) rows of
\(Z\), equation (1) becomes \(X^{\mathsf T}X=0\).  When \(X\) has rank
\(k\), its column space is a totally isotropic \(k\)-plane in \(K^r\).
The variety of such planes has dimension
\[
                    k(r-k)-\frac{k(k+1)}2,
\]
and, after the plane is chosen, the rank-\(k\) matrices with columns in it
have dimension \(ak\).  The maximum occurs at
\(k=\min(a,\lfloor r/2\rfloor)\).  Consequently the codimension, in the
space of all \(Z\), of (1) for this fixed rank-\(r\) matrix is
\[
c_a(r)=
\begin{cases}
\displaystyle \frac{h(2a-h+1)}2,&r=2h<2a,\\[4pt]
\displaystyle a+\frac{h(2a-h-1)}2,&r=2h+1<2a,\\[4pt]
T_a,&r\geq2a.
\end{cases}                                                \tag{2}
\]

### Rank strata inside the cycle-supported space

A weighted triangle adjacency block has the form
\[
\begin{pmatrix}0&x&z\\x&0&y\\z&y&0\end{pmatrix}.
\]
Its nonzero strata have (rank, affine dimension) equal to \((2,2)\) and
\((3,3)\), since its determinant is \(2xyz\) and rank one is impossible.
A weighted four-cycle block is congruent, after bipartitioning, to
\[
\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad B\in K^{2\times2}.
\]
Its nonzero strata have (rank, affine dimension) \((2,3)\) and \((4,4)\).

Suppose a stratum of \(L_D\) has \(u,v,x,y\) active blocks of these four
types, respectively.  Its matrices have rank and its affine dimension is
\[
r=2u+3v+2x+4y,\qquad
\ell=2u+3v+3x+4y=r+x.                                      \tag{3}
\]
Its projectivization has dimension \(\ell-1\).  We claim
\[
                            \ell-1<c_a(r).                  \tag{4}
\]

If \(r\geq2a\), then \(\ell\) is at most the number of edge parameters in
the active blocks, hence \(\ell\leq N\leq T_a=c_a(r)\).

Let \(r=2h<2a\).  From (3), \(x\leq h\), so \(\ell\leq3h\).  Formula (2)
gives
\[
c_a(2h)-(3h-1)=\frac{h(2a-h-5)+2}{2}.                       \tag{5}
\]
For \(1\leq h\leq a-1\), the numerator in (5) is a concave quadratic in
\(h\), so its minimum is at an endpoint.  The endpoint values are
\(2a-4\) and \((a-2)(a-3)\).  They are nonnegative, with equality only at
\((a,h)=(2,1)\) or \((3,2)\).  Equality in \(\ell\leq3h\) would require
\(x=h\), i.e. respectively one or two active rank-two four-cycle blocks.
Those require 4 or 8 edge parameters, exceeding \(T_2=3\) or \(T_3=6\).
Thus (4) is strict in the two exceptional arithmetic cases as well.

Finally let \(r=2h+1<2a\).  Then \(v\) is odd, so at least one rank-three
triangle block is active and \(x\leq h-1\).  Hence \(\ell\leq3h\).  Now
\[
c_a(2h+1)-(3h-1)
=\frac{2a+h(2a-h-7)+2}{2}>0.                               \tag{6}
\]
Again the numerator is concave in \(h\).  At the endpoints \(h=1,a-1\)
it has the positive values \(4a-6\) and
\((a-2)(a-3)+2\), respectively.  This proves (4).

For a fixed projective rank stratum, the incidence pairs \(([C],Z)\)
satisfying (1) therefore have dimension at most
\[
                  (\ell-1)+(aN-c_a(r))<aN.
\]
There are only finitely many choices of active blocks and ranks.  Their
images cannot cover the space of \(Z\), proving the theorem.

## 2. Passing from generic rows to an admissible Gale matrix

The preceding theorem initially treats unconstrained generic rows.  Here is
the normalization needed for rigidity.  The independence locus is a nonempty
Zariski-open subset of \((K^a)^N\).  Because \(N-1\geq a\) in every case of
the frozen problem, it meets the nonempty open locus on which deleting any
one row leaves rank \(a\).  Choose a rational matrix \(Z\) in this
intersection.

The kernel of \(Z^{\mathsf T}\) is not contained in any coordinate
hyperplane: deleting row \(i\) leaves full rank, so some dependence has a
nonzero coefficient at \(i\).  Over an infinite field, a finite union of
coordinate hyperplanes cannot cover this kernel.  There is therefore a
vector \(c\in\ker Z^{\mathsf T}\) with every \(c_i\ne0\).  After replacing
row \(z_i\) by \(c_i z_i\), one has
\[
                          \sum_i z_i=0,
\]
while every edge tensor is merely multiplied by the nonzero scalar
\(c_ic_j\).  Independence and rank \(a\) are preserved.  Thus this is an
admissible Gale matrix.

Let \(d=N-a-1\).  Choose an \(N\times(d+1)\) matrix \([\mathbf1\ P]\)
whose columns form \(\ker Z^{\mathsf T}\); the rows of \(P\) give an
affinely spanning rational realization in \(K^d\).  The complete-framework
stress matrices are exactly
\[
                          Z\Psi Z^{\mathsf T},
            \qquad \Psi\in\operatorname{Sym}_a.
\]
Restriction of these stresses to a deleted edge \(ij\) is
\(z_i^{\mathsf T}\Psi z_j\).  Hence the transpose of the restriction map
to \(E(D)\) has the independent columns \(z_i\odot z_j\), and the
restriction map is onto.  Surjectivity says precisely that every deleted
row of the complete rigidity matrix lies in the span of the undeleted rows.
Therefore deleting \(D\) preserves the full complete-graph rigidity rank.
Existence of this rational specialization makes the corresponding rigidity
minor a nonzero polynomial, so the same full rank holds generically.

## 3. Application to the frozen assertion

For \(G=\overline{sC_3\sqcup tC_4}\), put \(N=3s+4t\) and let \(a=a_N\)
be least with \(N\leq T_a\).  The exact Maxwell computation in `problem.md`
gives
\[
                         M(G)=N-1-a=d.
\]
Section 1 supplies independent deleted-edge tensors and Section 2 proves
that \(G\) is generically \(d\)-rigid.  Maxwell's necessary count gives the
reverse inequality \(\operatorname{rig}(G)\leq M(G)\).  Consequently
\[
 \boxed{\operatorname{rig}(\overline{sC_3\sqcup tC_4})
       =M(\overline{sC_3\sqcup tC_4})}
\]
for every allowed \(s,t\).  The case \(N=4,d=0\) is included (and also
follows immediately from the zero-dimensional convention).

## 4. Exact sharp-transition exchange

The previous pass asked specifically for the transition
\(2C_3\leadsto2C_3\sqcup C_4\) in dimension \(a=4\).  Keep the two old
triangles
\[
(e_1,e_2,e_3),\qquad(e_1+e_2,e_2+e_3,e_3+e_1),
\]
except that the first vector becomes \(e_1+q e_4\).  Place the new four-cycle
at
\[
(2,-1,2,0),(1,-2,2,-1),(2,-1,0,1),(-1,0,1,-2).
\]
In lexicographic upper-triangular coordinates, the ten edge tensors have
the exact determinant
\[
                              2q(27q+10).                   \tag{7}
\]
Thus moving just one old vector is enough; every \(q\ne0,-10/27\) works.

For the requested leading-coefficient factorization, order the columns as
\(\operatorname{Sym}^2\langle e_1,e_2,e_3\rangle\) followed by
\((e_1e_4,e_2e_4,e_3e_4,e_4^2)\).  The old \(6\times6\) certificate has
determinant \(-1\).  The quotient matrix of the frozen four-cycle has rank
three, and replacing its \(e_3e_4\) column by the exchanged column gives a
\(4\times4\) minor of determinant \(20\).  Hence the leading coefficient
in (7) factors as \((-1)(-20)=20\), old certificate times signed exchange
minor.  The accompanying verifier checks (7), the block factorization, and
an explicit zero-sum Gale scaling.
