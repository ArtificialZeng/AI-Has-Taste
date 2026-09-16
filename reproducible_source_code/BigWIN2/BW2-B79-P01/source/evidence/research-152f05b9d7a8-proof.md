# Endpoint cube rigidity: proposed proof

Research job: `win-00079-p01-research-152f05b9d7a8`.

This file proves the frozen assertion in `source.md`; it is a proposer artifact,
not a referee acceptance or a priority claim.

## Theorem

Let \(P\subset\mathbb H^4\) be a full-dimensional finite-volume convex
hyperbolic polytope with the face lattice of the \(4\)-cube.  If every
dihedral angle is
\(\alpha _0=\arccos(1/3)\), then \(P\) is isometric to the regular ideal
cube whose Klein-model closure is \([-1/2,1/2]^4\).

## Facet normals and the vertex null vectors

Work in \(V=\mathbb R^{4,1}\) with
\(\langle x,y\rangle=-x_0y_0+x_1y_1+\cdots+x_4y_4\).  Label the four
opposite facet pairs by \(F_i^+,F_i^-\), and let \(u_i^\pm\) be their
outward unit spacelike normals, so

\[
 P=\{z\in\mathbb H^4:\langle z,u_i^\pm\rangle\leq0
       \text{ for all }i,\pm\}.
\]

Every two facets from different opposite pairs meet.  The angle formula for
outward normals therefore gives

\[
 \langle u_i^\varepsilon,u_j^\delta\rangle=-\frac13
 \qquad(i\ne j).                                      \tag{1}
\]

For a sign vector \(\sigma\in\{+,-\}^4\), put

\[
 r_\sigma=\sum_{i=1}^4u_i^{\sigma_i}.
\]

The four selected normals have Gram matrix

\[
 H=\frac43I_4-\frac13J_4,
\]

which is positive semidefinite of rank \(3\), with kernel spanned by
\({\bf1}=(1,1,1,1)\).  In particular,
\(r_\sigma^2=0\) and \(r_\sigma\) is orthogonal to all four selected
normals.  It is not zero: if \(q\) is an interior point of \(P\), then

\[
 \langle q,r_\sigma\rangle
   =\sum_i\langle q,u_i^{\sigma_i}\rangle<0.           \tag{2}
\]

The four selected normals are linearly independent.  Indeed, any relation
with coefficient vector \(c\) implies \(Hc=0\), hence
\(c=\lambda{\bf1}\); the relation then reads
\(0=\lambda r_\sigma\), so \(\lambda=0\).

The cube vertex indexed by \(\sigma\) cannot be finite.  If its hyperboloid
representative were timelike, the four independent incident normals would
lie in its positive-definite four-dimensional orthogonal complement, whereas
their Gram matrix \(H\) is singular.  Hyperideal vertices are outside the
scope of the frozen assertion, so this vertex is ideal.  Its future null ray
is the common orthogonal complement of the four selected normals, which is
one-dimensional; consequently it is the ray of \(r_\sigma\).  Equation (2)
shows that \(r_\sigma\) is the future-pointing representative of that ray.

## The opposite entries are forced

Set

\[
 x_i=\langle u_i^+,u_i^-\rangle,\qquad
 d_i=u_i^+-u_i^-,\qquad s_i=u_i^++u_i^-.
\]

Fix the other three signs and compare the two cube vertices obtained by
choosing \(+\) and \(-\) at position \(i\).  Their vectors \(r_+\) and
\(r_-\) are nonproportional future null vectors: the corresponding vertices
are distinct in the cube face lattice.  Hence
\(\langle r_+,r_-\rangle<0\), and

\[
 d_i^2=(r_+-r_-)^2=-2\langle r_+,r_-\rangle>0.         \tag{3}
\]

Direct expansion using (1) gives

\[
\begin{aligned}
 \langle d_i,d_j\rangle&=0 &&(i\ne j),\\
 \langle s_i,d_j\rangle&=0 &&(1\leq i,j\leq4),\\
 d_i^2&=2-2x_i,\qquad s_i^2=2+2x_i,\\
 \langle s_i,s_j\rangle&=-\frac43 &&(i\ne j).          \tag{4}
\end{aligned}
\]

By (3), the four mutually orthogonal vectors \(d_i\) span a positive
four-space \(D\).  Its orthogonal complement in \(V\) is a negative line.
All four \(s_i\) lie on this line.  Write \(s_i=a_i\tau\), where
\(\tau^2=-1\).  The last equation of (4) says
\(a_i a_j=4/3\) for every \(i\ne j\).  Since there are four nonzero
coefficients, these equations force all \(a_i\) to be equal and
\(a_i^2=4/3\).  Therefore

\[
 s_i^2=-\frac43,
 \qquad 2+2x_i=-\frac43,
 \qquad x_i=-\frac53                                      \tag{5}
\]

for every \(i\).

## From the Gram matrix to the oriented polytope

Define the model normals

\[
 w_i^\pm=\left(\frac1{\sqrt3},\ \pm\frac2{\sqrt3}e_i\right).
                                                               \tag{6}
\]

Equations (1) and (5) show that the ordered systems \((u_i^\pm)\) and
\((w_i^\pm)\) have the same \(8\)-by-\(8\) Gram matrix.  Both span \(V\):
for the first system the four \(d_i\) span \(D\) and any nonzero \(s_i\)
spans \(D^\perp\); for the model, the four differences span the spatial
coordinates and a sum spans the time coordinate.

For completeness, equality of these spanning Gram systems really does define
a Lorentz isometry.  Let

\[
 A(c)=\sum c_{i,\pm}u_i^\pm,\qquad
 B(c)=\sum c_{i,\pm}w_i^\pm \quad(c\in\mathbb R^8).
\]

If \(A(c)=0\), Gram equality makes \(B(c)\) orthogonal to every model
normal.  Since the model normals span the nondegenerate space \(V\),
\(B(c)=0\).  Thus \(T(A(c))=B(c)\) is well-defined.  It is a surjective
linear map of \(V\), and Gram equality gives
\(\langle Tx,Ty\rangle=\langle x,y\rangle\); hence
\(T\in O(4,1)\) and \(T(u_i^\pm)=w_i^\pm\).

The map preserves, rather than reverses, time orientation.  Indeed, for the
interior point \(q\) used above,

\[
 \langle Tq,w_i^\pm\rangle=\langle q,u_i^\pm\rangle<0.
\]

Adding the two inequalities for any fixed \(i\), and using
\(w_i^++w_i^-=(2/\sqrt3,0,0,0,0)\), yields
\(-(2/\sqrt3)(Tq)_0<0\), so \((Tq)_0>0\).  A Lorentz isometry that sends
one future timelike vector to the future sheet preserves that sheet.

Finally, for every future hyperboloid point \(z\),

\[
 \langle z,u_i^\pm\rangle\leq0
 \quad\Longleftrightarrow\quad
 \langle Tz,w_i^\pm\rangle\leq0.
\]

Thus \(T\) maps all eight oriented halfspaces, and therefore their complete
intersection \(P\), onto the model intersection.  In Klein coordinates
\(y_k=z_k/z_0\), the two inequalities from (6) are

\[
 y_i\leq\frac12,\qquad y_i\geq-\frac12.
\]

The Klein closure is exactly \([-1/2,1/2]^4\).  Its sixteen Euclidean
vertices have squared norm \(4(1/2)^2=1\), so they are ideal.  This is the
regular ideal equiangular cube \(C^4_{\alpha_0}\), completing the proof.

## Audit boundary

- No disjoint-supporting-hyperplane or nesting lemma is used.  Positivity of
  every \(d_i\) follows instead from two distinct ideal vertex rays.
- The three dependencies among the eight model normals cause no ambiguity:
  the kernel argument defining \(T\) handles every relation.
- Time orientation and all eight inequality orientations are checked above;
  equality of unoriented hyperplanes alone is not used.
- The official source comparison was rechecked on 2026-09-10.  Its
  Proposition 2.3 proves cube rigidity only for
  \(\alpha>\alpha_0\) and explicitly omits the endpoint.  The bounded
  searches recorded in the triage evidence and repeated for this pass found
  no explicit endpoint theorem, but this is not a claim of openness, novelty,
  or priority.
