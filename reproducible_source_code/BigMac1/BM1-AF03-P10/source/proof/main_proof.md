# Generic Lotka--Volterra tree classes determine their trees

## Theorem

Let \(T_1,T_2\) be finite simple trees of the same order \(n\ge2\), and let
\(LV(T_i)\) be their generic homogeneous Lotka--Volterra tree classes over a
characteristic-zero field, with special parameter subclasses excluded as in
the version-of-record convention.  If the two generic classes are linearly
LV-equivalent (allowing a birational remapping of their \(3n-2\) parameters),
then \(T_1\cong T_2\).

Consequently Conjecture 12 holds for every \(n\ge2\), and in particular for
all 47 unlabeled trees of order nine.

## 1. Generic coordinates for the interaction matrix

For every vertex \(v\), write \(a_v=A_{vv}\).  For every oriented incidence
\(u\to v\) of a tree edge \(uv\), write
\[
d_{u,v}=A_{u,v}.
\]
These \(n+2(n-1)=3n-2\) quantities are the algebraically independent
parameters of the generic tree class.

**Lemma 1.**  If \(i\ne j\), and \(r\) is the neighbor of \(j\) on the unique
path from \(j\) to \(i\), then
\[
A_{ij}=d_{r,j}.
\]

**Proof.**  In the component of \(T-j\) containing \(i\), every edge \(uv\)
has \(j\notin\{u,v\}\).  The defining tree-system relations therefore give
\(A_{uj}=A_{vj}\) along the whole path from \(i\) to \(r\).  The common value
is \(A_{rj}=d_{r,j}\).  This also proves uniqueness of all matrix entries not
chosen as free parameters. \(\square\)

## 2. Classification of all generic linear Darboux polynomials

Let
\[
P=\sum_{i\in I}\alpha_i x_i,\qquad \alpha_i\ne0,
\]
be a nonzero linear Darboux polynomial, with \(I\) its exact support.  The
linear-DP criterion in Lemma 2 of van der Kamp's paper includes
\[
\tag{C2}
A_{ij}=A_{kj}\quad(i,k\in I,\ j\notin I)
\]
and
\[
\tag{C3}
\alpha_i(A_{ij}-A_{jj})
=\alpha_j(A_{ii}-A_{ji})\quad(i,j\in I).
\]

**Lemma 2.**  At the generic point of a tree class, the projective linear
Darboux polynomials are exactly
\[
\mathcal D_T=\{[x_v]:v\in V(T)\}\ \cup\
\{[P_{uv}]:uv\in E(T)\},
\]
where
\[
P_{uv}=(d_{v,u}-a_u)x_u+(a_v-d_{u,v})x_v
\]
up to a nonzero scalar.  In particular \(|\mathcal D_T|=2n-1\).

**Proof.**  The singleton supports give the coordinate DPs.  Suppose first
that \(|I|\ge2\).  If the induced subgraph \(T[I]\) is disconnected, choose
two closest components and vertices \(p,q\in I\) whose connecting path has an
interior vertex \(j\notin I\) and no other vertex of \(I\) between the two
components.  The first neighbors \(r,s\) of \(j\) toward \(p,q\) are
distinct.  Lemma 1 gives
\[
A_{pj}=d_{r,j},\qquad A_{qj}=d_{s,j}.
\]
These are distinct algebraically independent parameters, contradicting
(C2).  Thus \(T[I]\) is connected.

If \(|I|=2\), connectedness says \(I=\{u,v\}\) is an edge.  Condition (C3)
determines a unique projective ratio of its two nonzero coefficients and gives
the displayed \(P_{uv}\), the familiar edge DP.

It remains to exclude \(|I|\ge3\).  The tree \(T[I]\) then contains two edges
\(pq,qr\) with \(p\ne r\).  Put
\[
X=d_{p,q}-a_q,\quad Y=a_p-d_{q,p},\quad
Z=d_{q,r}-a_r,\quad W=a_q-d_{r,q}.
\]
Lemma 1 and (C3), applied respectively to \((p,q),(q,r),(p,r)\), give
\[
\alpha_pX=\alpha_qY,\qquad
\alpha_qZ=\alpha_rW,\qquad
\alpha_pZ=\alpha_rY.
\]
Multiply the first equality by \(Z\), then use the second and third; since
\(\alpha_rY\ne0\) in the rational function field, this forces \(X=W\), or
\[
d_{p,q}+d_{r,q}-2a_q=0.
\]
That is impossible because \(d_{p,q},d_{r,q},a_q\) are algebraically
independent and the field has characteristic zero.  Hence no support of size
at least three occurs generically. \(\square\)

This argument also identifies the excluded boundary: a higher-support DP can
appear only after imposing a proper algebraic relation such as the one just
displayed.  Such special subclasses do not witness equivalence of general
classes.

## 3. The projective DP configuration is a cone-graph configuration

Write an edge DP as
\(P_{uv}=\lambda_{uv,u}x_u+\lambda_{uv,v}x_v\), where both coefficients are
nonzero.  Root \(T\) arbitrarily and choose nonzero scalars \(s_v\)
recursively: set \(s_{v_0}=1\), and for a parent--child edge \(uv\), put
\[
s_v=-\frac{\lambda_{uv,v}}{\lambda_{uv,u}}s_u.
\]
There is no compatibility obstruction because \(T\) has no cycle.  In the
rescaled coordinates \(z_v=s_vx_v\), and after independently rescaling each
projective DP, the configuration \(\mathcal D_T\) becomes
\[
\{[z_v]:v\in V(T)\}\cup\{[z_u-z_v]:uv\in E(T)\}.
\]

Let \(G_T\) be the cone over \(T\): add a new vertex \(0\) and the spokes
\(0v\) for all \(v\in V(T)\).  The displayed vectors are precisely a reduced
oriented incidence representation of \(G_T\), with the row of the cone vertex
deleted.  A set of columns of a reduced incidence matrix is minimally
dependent exactly when the corresponding graph edges form a simple cycle:
a cycle has its signed incidence sum equal to zero, while a forest is
independent by successively eliminating a leaf edge.  Thus the projective
circuits of \(\mathcal D_T\) are the cycles of \(G_T\).

In particular its three-element circuits are exactly
\[
H_e=\{[x_u],[P_{uv}],[x_v]\},\qquad e=uv\in E(T),
\]
because a tree contains no triangle and every triangle of its cone consists
of one tree edge and its two incident spokes.

## 4. The three-element circuits reconstruct the tree

Let \(\mathcal H_T\) be the 3-uniform hypergraph whose ground set is
\(\mathcal D_T\) and whose hyperedges are the three-element projective
circuits \(H_e\).

**Lemma 3.**  The unlabeled hypergraph \(\mathcal H_T\) determines the
unlabeled tree \(T\).

**Proof.**  In \(\mathcal H_T\),
\[
\deg_{\mathcal H_T}([x_v])=\deg_T(v),\qquad
\deg_{\mathcal H_T}([P_e])=1.
\]
Assume \(n\ge3\), and let \(J\) be the hypergraph elements of degree at least
two.  These are exactly the coordinate forms belonging to nonleaf vertices
of \(T\).  No edge of a tree of order at least three joins two leaves.
Therefore every hyperedge meets \(J\) in either two elements (an
internal--internal tree edge) or one element (an internal--leaf tree edge).
Reconstruct a graph by joining the two elements in the first case and by
attaching a fresh leaf to the unique element in the second case.  The result
is exactly \(T\), up to renaming vertices.  For \(n=2\), there is only the
single tree \(K_2\). \(\square\)

## 5. Completion of the proof

An invertible linear conjugacy pulls every linear DP of the target back to a
linear DP of the source, and its inverse gives the reverse map.  By Lemma 2 it
therefore induces a projective bijection
\(\mathcal D_{T_1}\to\mathcal D_{T_2}\).  Invertible linear maps preserve and
reflect linear dependence, so this bijection is an isomorphism
\(\mathcal H_{T_1}\cong\mathcal H_{T_2}\).  Lemma 3 now gives
\(T_1\cong T_2\), proving the theorem. \(\square\)

## 6. Exact finite cross-check for the requested endpoint

The serialized certificate `certificates/trees_n2_n9.json` lists every
unlabeled tree of orders 2 through 9.  For every entry it records two exact,
different invariants:

1. reconstruction from the three-element circuit hypergraph; and
2. the multiset, over all \(2n-1\) configuration elements, of the number of
   cone-graph circuits of every cardinality containing that element.

The second invariant is pairwise distinct for every tree at each order
\(2\le n\le9\).  The no-import verifier independently enumerates every
labeled tree from all Prüfer words, canonicalizes them by the AHU tree code,
checks completeness and uniqueness, recomputes both invariants, and rejects
malformed or incomplete inputs.
