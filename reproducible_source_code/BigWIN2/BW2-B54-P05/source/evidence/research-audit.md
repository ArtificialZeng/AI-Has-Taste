# Research audit of the exact value

Audit job: `win-00054-p05-research-e4eaf0774267`  
Date: 2026-09-07

## Lower bound, including every smaller palette

The graph is 4-regular.  In a proper total coloring the color of a vertex and
the colors of its four incident edges are pairwise distinct, so every local
color set has cardinality five.  Palettes of size at most four are therefore
impossible.  With a five-color palette, every local color set is the entire
palette.  In particular the endpoints of every edge have equal local color
sets, contrary to the AVD condition.  Hence every AVD total coloring uses at
least six colors.

## Direct audit of the six-color assignment

Running

```text
python3 evidence/verify_coloring.py
```

returned

```text
PASS: 9 vertices, 18 edges, proper AVD total coloring with 6 colors
```

The assignment was also expanded vertex by vertex.  Each row below gives the
vertex color followed by its four incident-edge colors; each row has five
distinct entries.  The last entry is the unique color missing from the local
set.

| vertex | vertex and incident-edge colors | missing |
|---|---|---|
| 00 | 1; 2, 3, 4, 5 | 6 |
| 01 | 4; 2, 6, 5, 1 | 3 |
| 02 | 5; 3, 6, 2, 1 | 4 |
| 10 | 5; 4, 6, 1, 2 | 3 |
| 11 | 1; 5, 6, 4, 3 | 2 |
| 12 | 6; 2, 1, 4, 3 | 5 |
| 20 | 3; 5, 2, 4, 6 | 1 |
| 21 | 2; 1, 3, 4, 5 | 6 |
| 22 | 4; 1, 3, 6, 5 | 2 |

The missing-color array, written as the three coordinate rows, is

```text
6 3 4
3 2 5
1 6 2
```

Every row and every column has pairwise distinct entries.  Adjacency in
`C3 square C3` is exactly agreement in one coordinate, so adjacent vertices
have different missing colors and hence different five-element local color
sets.  Coverage of all 9 vertices and all 18 graph edges, endpoint vertex
colors, and the palette are checked directly by `verify_coloring.py`; the
five-distinct-entries test simultaneously checks incident vertex-edge and
adjacent-edge constraints.

Together, the lower bound and the serialized assignment prove
`chi''_a(C3 square C3) = 6`.

## Literature limitation

The publisher abstract for Tian--Chen--Shao--Wang (2014), DOI
`10.3934/naco.2014.4.49`, says that the paper determines exact values for
several Cartesian-product classes, including regular graphs.  The full theorem
text was not accessible in this bounded pass, so its hypotheses were not
instantiated and no novelty or priority claim is made here.  This access
limitation does not enter the self-contained lower bound or witness check.
