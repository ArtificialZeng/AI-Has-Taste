# A chain-level reduction of anchored graph spaces to anchored trees

## Theorem

Let (G) be any finite graph, let (K\subseteq V(G)), and let
(n\geq |K|).  Then every group

\[
H_i(\Sigma(G,K,n);\mathbb Z)
\]

is free abelian.  Thus this holds in particular for every cograph, and the
existence assertion frozen in `source.md` is false.

The proof actually gives an additive decomposition.  Suppose first that (G)
is connected, put (r=|K|), and let (L=H_1(G;\mathbb Z)).  For (m\geq r),
define (N_{r,m}) as follows.  Its vertices are the injections
(f:K\hookrightarrow[m]).  A collection of injections is a simplex when their
requirements are compatible: if (f_a(k)=f_b(k')), then (k=k').  Then

\[
H_i(\Sigma(G,K,n);\mathbb Z)\cong
\bigoplus_{\substack{J\subseteq[n]\\ |J|\leq n-r}}
 L^{\otimes |J|}\otimes
 H_{i-|J|}(N_{r,n-|J|};\mathbb Z).                 \tag{1}
\]

This is an isomorphism of abelian groups; no naturality is asserted for the
choice of a basis of (L).

## Proof for connected graphs

For every injection (f:K\hookrightarrow[n]), let

\[
U_f=\{(x_1,\ldots,x_n)\in G^n:x_{f(k)}=k\text{ for every }k\in K\}.
\]

These cubical subcomplexes cover (Sigma(G,K,n)).  A finite intersection is
empty precisely when two of its requirements assign distinct anchors to the
same coordinate.  A nonempty intersection with constrained-coordinate set
(S\subseteq[n]) is canonically a product (G^{[n]\setminus S}).

Fix an order on the finite set of injections.  Form the usual cellular Cech
double complex

\[
D_{p,q}=\bigoplus_{f_0<\cdots<f_p}
C_q(U_{f_0}\cap\cdots\cap U_{f_p};\mathbb Z),       \tag{2}
\]

omitting empty intersections.  The horizontal maps are alternating sums of
inclusions and the vertical maps are cellular boundaries.  Its augmentation
to (C_*(\Sigma(G,K,n);\mathbb Z)) is a quasi-isomorphism.  Here this standard
fact has a direct cellwise verification: for each cubical cell (c) of the
union, the augmented horizontal summands containing (c) form the augmented
simplicial chain complex of the nonempty simplex on
({f:c\subseteq U_f}), and are therefore exact.

We now replace the vertical complexes without changing total homology.  Choose
a spanning tree (T\subseteq G), orient all edges, and enumerate the chords as
(e_1,\ldots,e_b), where (b=\operatorname{rank}H_1(G;\mathbb Z)).  Let

\[
H=\mathbb Z\mathbf 1[0]\oplus
  \bigoplus_{a=1}^b\mathbb Z\ell_a[1]
\]

with zero differential.  There is a cellular chain map
(pi:C_*(G;\mathbb Z)\to H) given by

\[
\pi_0(v)=\mathbf1\quad(v\in V(G)),\qquad
\pi_1(e_a)=\ell_a,
\]

and by (pi_1(t)=0) on every tree edge (t).  The fundamental cycles of the
chords form an integral basis of (H_1(G;\mathbb Z)), so (pi) induces an
isomorphism on (H_1); the augmentation description of (pi_0) gives an
isomorphism on (H_0).  Hence (pi) is a quasi-isomorphism.

On an intersection with free-coordinate set (F), take
(pi_F=\bigotimes_{j\in F}\pi).  These are quasi-isomorphisms because all
complexes are bounded complexes of free abelian groups.  More importantly,
they commute *strictly* with every horizontal map in (2).  Indeed, an
intersection inclusion only inserts constrained anchor vertices into newly
free tensor positions, and every anchor vertex is sent by (pi_0) to the same
element (mathbf1).  Thus the (pi_F) define a map from (D) to a bounded
double complex (E), levelwise a quasi-isomorphism.  The vertical-filtration
spectral sequence shows

\[
H_*(\operatorname{Tot}D)\cong H_*(\operatorname{Tot}E).                \tag{3}
\]

The vertical differential of (E) is zero.  Expand each free-coordinate
tensor product using (H=\mathbb Z\mathbf1\oplus L[1]).  A summand is specified
by a subset (J\subseteq[n]) of coordinates carrying elements of (L).  Such
a summand occurs in an intersection exactly when none of its anchor
requirements uses a coordinate in (J).  Consequently the horizontal
complex for fixed (J) is the simplicial chain complex of
(N_{r,n-|J|}), tensored with (L^{\otimes |J|}), and shifted upward by
(|J|).  Summing these mutually preserved summands proves (1).

It remains only to note that every (N_{r,m}) has free integral homology.  To
see this with no new computation, choose any finite tree (T_r) containing
(r) distinguished vertices and apply the same cover (U_f) to
(Sigma(T_r,K,m)).  Every nonempty intersection is a product of trees and is
contractible.  For completeness, the required nerve comparison follows from
the same cellular Cech double complex, without any openness assumption on the
cover: horizontal augmentation resolves the cellular chains of the union,
while augmenting each connected intersection chain complex to (\mathbb Z) is
a columnwise quasi-isomorphism whose target is precisely the simplicial chain
complex of (N_{r,m}).  Equivalently, this is the subcomplex-cover form of the
Nerve Lemma, and it gives

\[
N_{r,m}\simeq \Sigma(T_r,K,m).                       \tag{4}
\]

For (r\geq2), Theorem 2.5 of Dmitry N. Kozlov, *Stirling complexes*,
J. Appl. Comput. Topol. **7** (2023), 57--74,
<https://doi.org/10.1007/s41468-022-00096-4>, says that the right side is a
wedge of ((m-r))-spheres (with the usual discrete interpretation when
(m=r)).  For (r=1), the compatibility nerve is itself a simplex; for
(r=0), (Sigma(G,\varnothing,n)=G^n) and the integral Kunneth theorem applies
directly.  Equations (1)--(4) therefore show that all homology groups are free.

## Disconnected graphs

Let (G=\bigsqcup_a G_a) be its decomposition into connected components and
put (K_a=K\cap V(G_a)).  The product (G^n) is the disjoint union indexed by
component assignments (alpha:[n]\to\{a\}).  For such an assignment, write
(I_a=\alpha^{-1}(a)).  Its intersection with the anchored space is empty if
some (|I_a|<|K_a|); otherwise, after permuting labelled coordinates, it is

\[
\prod_a \Sigma(G_a,K_a,|I_a|).                       \tag{5}
\]

Every factor in (5) has free homology by the connected case (including the
unanchored and zero-coordinate conventions).  The integral Kunneth theorem
then gives free homology for each product, and a finite disjoint union gives a
direct sum of such groups.  If (G) has no vertices, then (K=\varnothing): the
space is a point for (n=0) and empty for (n>0), so its homology is again free.
This completes the proof for every finite graph.

## Sanity-check ranks

If (G) is connected with (b=\operatorname{rank}H_1(G;\mathbb Z)) and
(d=n-r>0), (1) immediately gives

\[
\operatorname{rank}H_i=\binom ni b^i\quad(0\leq i<d).
\]

For example, with one anchor and (n=3), the ranks are
((1,3b,3b^2)).  With two anchors and (n=4), they are
((1,4b,1+4b+12b^2)).  These formulas agree with the independent integral
Smith computations recorded in `evidence/computation.md`.
