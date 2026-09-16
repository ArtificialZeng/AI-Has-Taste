# Complete `K_7`-free 13-layer periods cannot beat the target

Provenance: `win-00044-p02-research-d843add8341e`  
Date: 2026-09-06

## Exact statement

Consider a cyclic 13-layer weighted base graph in which every layer is a
clique, consecutive layers are completely joined, and there are no other
edges.  Suppose every layer is nonempty and the base graph is `K_7`-free.
If every base vertex has weighted open-neighborhood at least one, then the
total weight in a period is at least

```text
39/8.
```

Equality is attained by taking three vertices of weight `1/8` in every layer.
Therefore this entire complete-layered class cannot provide the strict
inequality `S<39/8` needed by a 13-step periodic disproof construction.

## Reduction to a finite exact calculation

Write `c_i` and `A_i` for the cardinality and total weight of layer `i`.
Because every consecutive union is a clique and layers are nonempty,
`K_7`-freeness is exactly

```text
1 <= c_i <= 5,                 c_i+c_(i+1) <= 6.
```

For a vertex of weight `w` in layer `i`, its weighted degree is
`A_(i-1)+A_i+A_(i+1)-w`.  The largest weight in that layer is at least
`A_i/c_i`; conversely, equal weights attain that value.  Hence the exact
layer-total feasibility constraints are

```text
A_(i-1) + (1-1/c_i) A_i + A_(i+1) >= 1,       A_i >= 0.
```

Increasing a cardinality weakens these constraints.  Thus it suffices to
check cardinality patterns maximal in the coordinatewise order.  A pattern
is maximal precisely when every `c_i<5` lies on an adjacent pair summing to
six.  Integer enumeration gives 12,426,742 admissible labeled patterns,
3,836 maximal labeled patterns, and 178 maximal representatives after cyclic
shift and reflection.

For each representative, `evidence/complete_layered.py` solves the 13-variable
layer-total LP only to discover a dual vector.  It reconstructs that vector as
exact rational numbers and checks `y>=0`, `B^T y<=1`, and `sum(y)>=39/8` using
`fractions.Fraction`.  These are exact lower-bound certificates.  The unique
equality representative among the 178 is `(3,3,...,3)`, for which the direct
positive primal witness has `A_i=3/8` and individual weights `1/8`.

This is an exhaustive theorem for complete layered periods, but it does not
cover incomplete same/consecutive-layer joins such as a `3+4` junction with
selected missing edges, nor nonlayered base graphs.
