# Exact obstruction for the variable-weight 13-layer repair

Provenance: `win-00044-p02-research-d843add8341e`  
Date: 2026-09-06

## Model and scope

Take the specialization to `r=3` of the 13-layer period in the Chen--Chen
even construction.  Its numbers of base vertices per layer are

```text
(1,4,2,1,3,3,1,2,4,1,3,4,3).
```

Let the maximal periodic layered base graph have all edges inside a layer and
all edges between consecutive layers, including the last-to-first period
boundary, and no other edges.  Give its 32 vertices arbitrary nonnegative
rational weights `w_v`.  Normalizing the required weighted minimum degree to
one gives the linear inequalities

```text
sum(w_v : uv is an edge) >= 1                 for every base vertex u.
```

Allowing zero weights only relaxes the positive-weight blow-up problem.
All consecutive layer unions have at most six vertices except layers 10--11
and 11--12 (zero-based), each of which has `3+4=7`.  Consequently every
`K_7`-free subgraph must omit some edge `e_1` from the first seven-vertex
union and some edge `e_2` from the second.

For each of the `21*21=441` choices `(e_1,e_2)`, retain every other edge and
solve

```text
min 1^T w  subject to A w >= 1 and w >= 0.
```

This is sufficient for all subgraphs: deleting any further edges only makes
the weighted-degree constraints stronger.

## Exact result

The minimum over all 441 supergraphs is

```text
122/25 = 4.88 = 39/8 + 1/200.
```

Thus no `K_7`-free edge-deletion repair of this fixed 13-layer vertex-count
pattern, even with completely variable individual weights and layer totals,
has normalized period mass below `39/8`.

The accompanying script uses floating-point linear programming only to
discover primal and dual vectors.  It converts every used vector to
`fractions.Fraction` and verifies exactly that each of the 441 dual vectors is
nonnegative, satisfies `A^T y <= 1`, and has objective at least `122/25`.
It also checks an exact feasible primal vector of total `122/25`, establishing
equality.  Running

```text
python3 evidence/junction_lp.py
```

prints the exact optimum, the `1/200` gap, the best rational primal vector,
and the distribution of the 441 verified dual objectives.  This is a proved
obstruction only for the displayed vertex-count pattern and layered
same/consecutive-edge architecture; it is not a result about arbitrary
`K_7`-free graphs.
