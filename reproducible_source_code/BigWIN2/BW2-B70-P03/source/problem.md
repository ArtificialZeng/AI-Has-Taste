# Precise problem reading

## Frozen source and status

The immutable statement is `source.md` (SHA-256
`ad9eb559516e39382c1707dbcfbc8867593184e4524ebfeaebc43f84edf1ff79`).
Its primary source is Mamun--Nalikka--Ramos, *Universality in the algebra and
topology of cographs*, arXiv:2609.04554v1 (3 September 2026),
<https://arxiv.org/abs/2609.04554v1>.  The official HTML was re-inspected on
2026-09-08: Definition 4.13 is at lines 576--581, Corollary 4.18 at lines
599--626, and the explicit statement that integral torsion in anchored
configuration spaces is not known at lines 627--630:
<https://arxiv.org/html/2609.04554v1>.

## Objects and conventions

- A graph means a finite simple graph $G=(V,E)$, regarded as its geometric
  realization as a one-dimensional simplicial complex.  A **cograph** is such
  a graph with no induced $P_4$.  Connectedness is not assumed.
- $K\subseteq V$ is an arbitrary anchor set, possibly empty, and
  $r:=|K|$.  Coordinates are labelled.  The integer $n$ satisfies
  $n\in\mathbb Z_{\ge 0}$ and $n\ge r$.
- With the standard product cubical structure on $G^n$,
  
  \[
  \Sigma(G,K,n)=\{(x_1,\ldots,x_n)\in G^n:
       (\forall k\in K)(\exists j\in\{1,\ldots,n\})\ x_j=k\}.
  \]
  
  Equivalently, a product cell $c_1\times\cdots\times c_n$, with every
  $c_j$ a vertex or an open edge of $G$, belongs to this cubical subcomplex
  exactly when, for each $k\in K$, at least one factor is the vertex cell
  \(\{k\}\).  Collisions of coordinates are unrestricted, including away from
  anchors; the anchor condition requires equality with the anchor vertex, not
  merely lying on an incident edge.
- $H_i(-;\mathbb Z)$ is singular homology (equivalently the cellular homology
  of this finite cubical complex), $i\in\mathbb Z_{\ge0}$.  For its finitely
  generated abelian group, \(\operatorname{Tor}H_i\ne0\) means that some
  homology class has finite order $d>1$.
- For $n=0$, the usual empty-product convention is used.  Under $n\ge|K|$
  this case forces $K=\varnothing$, and the space is a point.

## Exact assertion and its negation

The assertion to resolve is

\[
\exists\,G\ \exists\,K\subseteq V(G)\ \exists\,n\ge|K|\ 
\exists\,i\ge0:\quad G\text{ is a cograph and }
\operatorname{Tor}H_i(\Sigma(G,K,n);\mathbb Z)\ne0.
\]

A disproof requires the universally quantified torsion-freeness statement for
every such $G,K,n,i$.  A finite torsion-free census does not prove that
universal negation.  A proof of the existential assertion requires one exact
tuple and a certified nonzero torsion class (not merely a Smith factor of one
boundary matrix).

## Scope exclusions

This is not an ordinary collision-free ordered or unordered graph
configuration space, a sink configuration space, or the generalized anchored
space that requires only $q<|K|$ anchors.  Results about those spaces do not
settle the assertion.  The graph class is precisely cographs; a counterexample
on a non-cograph does not settle it.

## Verified boundary reductions

These elementary reductions hold for every finite graph, not just cographs.

1. If $K=\varnothing$, then \(\Sigma(G,K,n)=G^n\).  Graph homology is free
   abelian and the integral Kunneth theorem gives torsion-free homology for
   $G^n$; hence an example must have $r\ge1$.
2. Every cell in \(\Sigma(G,K,n)\) has at least $r$ distinct coordinate
   factors fixed at the $r$ anchor vertices.  Therefore
   \(\dim\Sigma(G,K,n)\le n-r\).
3. If $n=r$, the space is the discrete set of the $r!$ permutations of the
   anchors (one point when $r=0$).  If $n=r+1$, it is at most
   one-dimensional.  Both cases have torsion-free integral homology.
4. $H_0$ is always free abelian.  Consequently any counterexample must obey
   
   \[
   r\ge1,\qquad n\ge r+2,\qquad 1\le i\le n-r.
   \]

## Nearest primary results and delta

- Kozlov, *Stirling complexes*, J. Appl. Comput. Topol. 7 (2023), 57--74,
  DOI <https://doi.org/10.1007/s41468-022-00096-4>, Theorem 2.5, proves that
  for a tree $T$ and arbitrary vertex subset $K$, the corresponding space
  is homotopy equivalent to a wedge of spheres; its integral homology is free.
- Kozlov, *Homology and Euler characteristic of generalized anchored
  configuration spaces of graphs*, J. Appl. Comput. Topol. 8 (2024),
  1053--1067, DOI <https://doi.org/10.1007/s41468-024-00167-8>, Definition 1.1
  and Theorem 4.4 (with the top group completed via Euler characteristic),
  computes the circle case and yields free integral homology.  The official
  arXiv record is <https://arxiv.org/abs/2309.17149>.
- Mamun--Nalikka--Ramos Corollary 4.18 proves finite generation over pointed
  cographs and a uniform torsion-exponent bound for each fixed
  \((i,r,n)\), but neither produces torsion nor proves torsion-freeness.

Thus the nearest result covers trees and topological circles; the proposed
delta is either one exact torsion example among cographs outside those known
families or a global torsion-free argument.  Exact-phrase and equivalent-term
searches of arXiv and the cited primary papers on 2026-09-08 found no later
resolution; this supports, but cannot certify, current open status or priority.

## Bounded first research test

Implement the integral cubical chain complex directly.  Orient every graph
edge once and every product cell by increasing coordinate position.  The
boundary replaces its $j$-th oriented edge by head minus tail with the
Koszul sign \((-1)^{\#\{\text{earlier edge factors}\}}\); retain the anchored
cells.  Unit-test cell counts, \(\partial^2=0\), and homology against the exact
reductions above and Kozlov's tree/circle formulas.  Then compute exact Smith
normal forms for the smallest connected non-tree, non-circle cographs,
starting with one-anchor $n=3$ cases (including $K_4$), and independently
check any torsion candidate by an explicit cycle/order certificate and rank
jumps modulo every prime divisor.
