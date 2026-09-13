# Formal statement (research endpoint, frozen before Gate 1 search)

## Objects and quantifiers

Let
\[
Q_n=[-1/2,1/2]^n\subset\mathbb R^n,\qquad n\in\mathbb Z_{\ge1}.
\]
For every unit vector \(v\in S^{n-1}\), define
\[
\sigma_n(v)=\mathcal H^{n-1}(Q_n\cap v^\perp),
\]
where \(\mathcal H^{n-1}\) is Euclidean \((n-1)\)-dimensional Hausdorff
measure on the linear hyperplane \(v^\perp=\{x:\langle v,x\rangle=0\}\).

A direction is an antipodal class \([v]=\{v,-v\}\).  It is *diagonal* if
there is a nonempty set \(I\subseteq\{1,\dots,n\}\) and a number \(c>0\)
such that \(|v_i|=c\) for \(i\in I\) and \(v_i=0\) for \(i\notin I\).
For a unit normal this forces \(c=|I|^{-1/2}\).  Thus, modulo signed
coordinate permutations, diagonal directions are
\[
d_k=(\underbrace{1,\dots,1}_{k},0,\dots,0)/\sqrt{k},
\qquad 1\le k\le n.
\]

A direction \([v]\) is a local maximum (respectively local minimum) if
there is a relative neighbourhood \(U\) of \(v\) in \(S^{n-1}\) such that
\(\sigma_n(v)\ge \sigma_n(w)\) (respectively \(\le\)) for every \(w\in U\).
Equality is allowed: “local extremum” is not assumed strict.  This definition
is invariant under the antipodal identification.

## Primary endpoint for this project

Classify every local maximum and local minimum of \(\sigma_5\) on \(S^4\),
including non-smooth and boundary strata, up to the hyperoctahedral action
(coordinate permutations and independent sign changes).  In particular,
decide the precise \(n=5\) instance
\[
\forall v\in S^4:\quad [v]\text{ locally extremal }
\Longrightarrow [v]\text{ diagonal}.
\]
If the implication is false, an adequate disproof must give an exact
non-diagonal direction and an exact proof of local maximality or minimality;
a definite floating-point Hessian is discovery evidence only.  If it is true,
the proof must also treat support-deficient normals, subset-sum walls, and
degenerate Hessians; merely classifying smooth chamber-interior critical
points does not prove the stated endpoint.

## Critical points and Hessians

At a point where \(\sigma_5\) is differentiable, “critical” means that the
differential restricted to \(T_vS^4=v^\perp\) vanishes.  Where it is twice
differentiable, the Hessian is the intrinsic quadratic form on \(T_vS^4\).
“Indefinite” means that this tangent quadratic form takes both positive and
negative values.  At a subset-sum wall or a zero-coordinate stratum, local
extremality is defined by the neighbourhood inequality above and is not
replaced by a formal Hessian test.

## Symmetry normalization and exact slice formula

Signed coordinate permutations preserve \(Q_5\), so each orbit has a
representative
\[
a_1\ge a_2\ge\cdots\ge a_5\ge0,\qquad \sum_i a_i^2=1.
\]
For a nonzero vector \(a\in\mathbb R^s_{>0}\), let \(A=\sum_i a_i\).  The
scale-invariant central-section function on its support is
\[
F_s(a)=\frac{\|a\|_2}{(s-1)!\prod_{i=1}^s a_i}
\sum_{S\subseteq[s]}(-1)^{|S|}
\left(\frac A2-\sum_{i\in S}a_i\right)_+^{s-1}.
\]
For a unit vector with exactly \(s\) nonzero coordinates,
\(\sigma_n(a,0)=F_s(a)\); the unused cube coordinates contribute a unit
factor.  The formula is to be independently derived and source-checked before
use as a proved lemma.  Its polynomial pieces are separated by the
subset-sum hyperplanes
\[
\sum_{i\in S}a_i=\sum_{i\notin S}a_i.
\]

## Compactness, endpoints, and degeneracies

The domain \(S^4/\{\pm1\}\) is compact and \(\sigma_5\) is continuous, so
global extrema exist.  The classification must include supports
\(s=1,2,3,4,5\), equal-coordinate faces of the ordered Weyl chamber,
subset-sum hyperplanes (including coincident walls), and their intersections.
Limits as one or more coordinates tend to zero must agree with the
lower-support section volume.  No division by a coordinate or a subset-sum
linear form is permitted unless its nonvanishing has been established in the
case under discussion.

## Publication/novelty convention

The mathematical endpoint above is independent of novelty.  “New” will mean
only “not found in the primary-source searches recorded in
`literature/search_log.md` through 2026-08-29”; discovery of an existing public
solution stops originality claims but does not alter the theorem's meaning.
