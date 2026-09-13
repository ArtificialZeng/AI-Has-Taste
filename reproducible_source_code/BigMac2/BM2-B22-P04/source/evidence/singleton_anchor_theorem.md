# Singleton anchors are torsion-free for every finite graph

## Statement

Let `G` be any nonempty finite graph, not necessarily connected, let `k` be a
vertex, and let `n>=1`.  Write `c` for the number of connected components of
`G` and `beta=rank H_1(G;Z)=|E|-|V|+c`.  Then every integral homology group of

```text
Sigma(G,{k},n) = {(x_1,...,x_n) in G^n : x_i=k for at least one i}
```

is free abelian.  More precisely, for `0<=q<=n`,

```text
rank H_q(Sigma(G,{k},n);Z)
  = binom(n,q) beta^q (c^(n-q) - (c-1)^(n-q)),
```

with the usual convention `x^0=1`; the displayed rank is zero at `q=n`.
All groups in degrees greater than `n` vanish.

## Proof

For a based space `(X,x_0)`, put

```text
F_n(X,x_0) = {(x_1,...,x_n) in X^n : some x_i=x_0}.
```

This construction preserves based homotopies.  Indeed, if
`H:X times I -> Y` is a based homotopy, then the coordinatewise homotopy
`H^n` maps `F_n(X,x_0) times I` into `F_n(Y,y_0)`: a coordinate equal to
`x_0` remains equal to `y_0` throughout the homotopy.  It follows in
particular that a based homotopy equivalence induces a homotopy equivalence on
these subspaces.

Choose a maximal tree in every component of `G`, with the tree in the
component of `k` containing `k`, and collapse each tree to a vertex.  This is a
based homotopy equivalence from `(G,k)` to a graph `(W,*)` that is a disjoint
union of `c` bouquets of circles; the distinguished vertex `*` is the bouquet
vertex of the component containing `k`.  Altogether `W` has `c` zero-cells and
`beta` loop one-cells.  Therefore

```text
Sigma(G,{k},n) = F_n(G,k)  ~=  F_n(W,*).
```

Give `W^n` its product CW structure.  The subspace `F_n(W,*)` is exactly the
subcomplex of product cells having at least one factor equal to the zero-cell
`*`.  Every loop one-cell of `W` has cellular boundary zero, so the cellular
boundary of every product cell is zero.  Hence the integral homology of this
subcomplex is its cellular chain group and is free.

A `q`-cell is counted by choosing its `q` loop coordinates, choosing one of
the `beta` loops in each of them, and filling the other `n-q` coordinates with
vertices so that at least one is `*`.  These choices number

```text
binom(n,q) beta^q (c^(n-q) - (c-1)^(n-q)),
```

which proves the formula and the theorem.

## Consequences for the frozen problem

The case `K=empty` is also torsion-free because it is simply `G^n`, whose
integral homology is free by the graph case of the Kunneth theorem.  The theorem
eliminates every singleton anchor, for every graph and every `n`, rather than
only the two diamond instances at `n=3`.

If `r=|K|`, each cell of `Sigma(G,K,n)` has at least `r` distinct zero-cell
factors, so its dimension is at most `n-r`.  A complex of dimension at most one
has torsion-free integral homology.  Consequently any witness to the frozen
cograph existence assertion must satisfy

```text
|K| >= 2  and  n >= |K|+2.
```

The first computational layer not eliminated by these arguments is therefore
`|K|=2,n=4`, not `|K|=1,n=3`.

## Exact finite cross-check and literature limit

The independently generated cellular certificates under
`evidence/diamond_n3/` agree with the connected formula: the diamond has
`c=1,beta=2`, so at `n=3` the ranks are `1,6,12`.  Both anchor-orbit Smith
certificates give exactly those ranks and no torsion.

A bounded search on 2026-09-09 compared the statement with D. N. Kozlov,
*Homology and Euler characteristic of generalized anchored configuration
spaces of graphs*, J. Appl. Comput. Topol. 8 (2024), 1053--1067,
<https://doi.org/10.1007/s41468-024-00167-8>, and with the 2026 primary source
bound in `source.md`.  The former advertises an Euler-characteristic formula
for arbitrary connected graphs and complete homology for circle graphs; the
latter leaves integral torsion open in general.  Searches for the exact
singleton/fat-wedge reduction did not locate an explicit equivalent theorem.
This limited negative search is not a novelty or priority claim; a fresh
referee must inspect the full literature before treating the result as
publishable.
