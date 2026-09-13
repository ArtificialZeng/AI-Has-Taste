# Exact diamond computation at one anchor and three labeled coordinates

This directory is a reproducible integer certificate for the two pointed
diamond graphs required by `problem.md`.  Run from the project root:

```text
python3 evidence/diamond_n3.py
```

The graph has vertices `a,b,c,d`, oriented edges
`[a,c],[a,d],[b,c],[b,d],[c,d]`, and product cells are ordered
lexicographically using vertices first and then those oriented edges.  The two
anchor representatives are `a` (degree two) and `c` (degree three).

For either anchor, the chain ranks are

```text
rank C0 = 37,  rank C1 = 105,  rank C2 = 75.
```

The files `B0.tsv`, `B1.tsv`, and `B2.tsv` give the ordered bases, while
`d1.tsv` and `d2.tsv` give the boundary matrices (rows are target cells and
columns are source cells).  Direct integer multiplication gives `d1*d2=0`.

Scanning `B1` in order gives a spanning tree with 36 edges.  The 69 remaining
edges are chords.  For each oriented chord `e`, the corresponding column of
`kernel_basis.tsv` is `e` minus the oriented tree path with the same boundary.
These fundamental cycles are a `Z`-basis of `ker(d1)`: deleting their chord
coordinates leaves a tree-supported cycle, necessarily zero.  Consequently,
the coordinates of any cycle in this basis are exactly its chord coefficients.
The matrix `relations.tsv` consists of the chord rows of `d2`; exact
multiplication verifies

```text
d2 = kernel_basis * relations.
```

The retained Smith certificate satisfies

```text
smith_U * relations * smith_V = smith_D.
```

For anchor `a`, `det(smith_U)=det(smith_V)=-1`; for anchor `c`, the two
determinants are `1` and `-1`.  Thus both transformations are unimodular.
In both cases `smith_D` has exactly 63 nonzero diagonal entries, all equal to
one, and is zero off the diagonal.  The elementary row and column operations
are also retained in `smith_operations.json`.

It follows, exactly (not numerically), that both pointed spaces have

```text
H0 = Z,   H1 = Z^6,   H2 = Z^12,
```

and no other homology.  In particular neither anchor orbit of the diamond is a
torsion witness.  This finite computation does not settle the frozen
existential cograph problem.

Each anchor subdirectory has a `summary.json` and a hash/size `manifest.json`.
The combined result is `summary.json`; the generating and self-checking source
is `../diamond_n3.py`.
