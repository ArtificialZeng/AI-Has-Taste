# Exact resolution of the frozen `8 x 8` target

All coordinates below lie in `Z_8 x Z_8`, represented by `0,...,7` in each
coordinate. Neighbors differ by `1` modulo 8 in exactly one coordinate.

## Leaf-stripping lemma

Let `S` be the initially infected set and let `U=V\S`. At any stage, write
`R` for the vertices still uninfected. A vertex `v in R` has at least three
infected neighbors exactly when its degree in the induced graph `G[R]` is at
most one. Consequently the synchronous three-neighbor process is precisely
simultaneous deletion of all vertices of degree at most one from `G[U]`.
It exhausts `U` if and only if `G[U]` is a forest: a cycle survives every such
deletion, while every nonempty finite forest has a vertex of degree at most
one and repeated deletion exhausts it.

## Lower bound

Suppose `S` percolates and put `k=|S|`, `u=64-k`. By the lemma, `G[U]` is a
forest. For `k<64`, let it have `c>=1` components, so it has `u-c` edges. If
`b` is the number of edges between `S` and `U`, degree counting on `U` gives

`4u = 2(u-c)+b`, hence `b=2u+2c`.

Degree counting on `S` gives `4k=2e(S)+b>=b`. Therefore

`4k >= 2(64-k)+2`, so `6k>=130` and `k>=22`.

## A 22-vertex witness

Take

```
S = {(0,0),(0,1),(0,5),(1,2),(1,4),(1,7),(2,0),(2,5),
     (3,2),(3,4),(3,7),(4,1),(4,3),(4,6),(5,0),(5,5),
     (6,1),(6,3),(6,7),(7,2),(7,4),(7,6)}.
```

The exact synchronous infection layers after `L_0=S` are:

```
L_1  = {(0,2),(0,4),(1,0),(1,5),(2,4),(2,7),(3,3),
        (4,2),(5,1),(6,0),(6,2),(7,1),(7,3),(7,5)}
L_2  = {(0,3),(1,1),(5,2),(7,0)}
L_3  = {(1,3),(5,3),(7,7)}
L_4  = {(0,7),(2,3)}
L_5  = {(0,6),(2,2)}
L_6  = {(1,6),(2,1)}
L_7  = {(2,6),(3,1)}
L_8  = {(3,0),(3,6)}
L_9  = {(3,5),(4,0)}
L_10 = {(4,5),(4,7)}
L_11 = {(4,4),(5,7)}
L_12 = {(5,4),(5,6)}
L_13 = {(6,4),(6,6)}
L_14 = {(6,5)}.
```

These disjoint layers contain `14+4+3+10*2+1=42` vertices, so together with
`S` they cover all 64 vertices. The machine-readable version is
`evidence/22-set-certificate.json`. The dependency-free checker
`evidence/verify_22.py` reconstructs the torus from the coordinate definition
and verifies at every round that the displayed layer equals the full set of
then-uninfected vertices with at least three infected neighbors. It also
independently finds that `S` spans only the edge `(0,0)(0,1)` and that its
42-vertex complement is connected with 41 induced edges, hence is a tree.

Thus `S` percolates, giving `t_3(8,8)<=22`. Together with the lower bound,

`t_3(8,8)=22`.

No assertion is made here about other torus dimensions or about priority in
the literature.
