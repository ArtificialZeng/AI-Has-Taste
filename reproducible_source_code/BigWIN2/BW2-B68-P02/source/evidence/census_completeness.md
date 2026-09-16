# Exact independent census-completeness argument

This note justifies the two independent algorithms used by
`evidence/scripts/independent_census.py`.  It does not assume the correctness
or completeness of `geng`.

## Canonicalization and automorphism counts

For an input graph, `canonical_small.c` begins with the one-cell ordered
partition of its vertices.  A refinement step replaces the color of each
vertex by the ordered pair consisting of its old cell and its vector of
neighbor counts into all old cells; equal pairs form a new cell, ordered
lexicographically.  This is repeated to stability.  Every isomorphism preserves
these signatures and their order.

If the stable partition is not discrete, the search chooses a smallest
nonsingleton cell, breaking ties by its position in the ordered partition, and
creates one child for every possible vertex individualized from that cell.
There is no pruning.  The choice of cell is isomorphism-invariant, and an
isomorphism maps the complete child set bijectively to the child set of the
image graph.  Induction on the search tree therefore shows that isomorphic
inputs have the same multiset of discrete leaf adjacency strings.  The least
string is consequently a canonical form.

At a discrete leaf the ordered singleton cells give a bijection from the input
vertices to the canonical labels.  Leaves attaining the least string are
exactly the isomorphisms from the input graph to that fixed labeled graph.
They form a torsor for the automorphism group, so their number is
`|Aut(G)|`.  Thus distinct output strings prove nonisomorphism, and the fourth
table column is the exact automorphism-group order.  As implementation checks,
all 208 nonempty NetworkX graph-atlas graphs through order 6 have distinct
outputs, and their reported automorphism orders agree with exhaustive VF2.

## Independent labeled enumeration

Let `F(c1,c2,c3)` be the number of labeled simple completions of any fixed
residual degree sequence containing `ci` vertices of residual degree `i`;
zero-degree vertices can be omitted.  Choose a fixed vertex of maximum positive
residual degree `d`.  After removing it, choose `ki` of the remaining `ci`
vertices of residual degree `i` as its neighbors, subject to
`k1+k2+k3=d`.  There are `product_i binom(ci,ki)` choices, and choosing such a
neighbor moves it from residual degree `i` to `i-1`.  Every simple completion
has one and only one such neighbor choice, yielding the recurrence implemented
in `labeled_cubic_count.py`, with base `F(0,0,0)=1`.  Hence
`L_n=F(0,0,n)` counts all labeled simple cubic graphs on a fixed `n`-element
vertex set.

Let `C_n` count the connected ones and fix label 1.  If its connected component
has order `k`, its other labels can be chosen in `binom(n-1,k-1)` ways, its
graph in `C_k` ways, and the complement in `L_(n-k)` ways.  The component is
unique, so

`C_n = L_n - sum_(2<=k<n) binom(n-1,k-1) C_k L_(n-k)`.

The exact connected counts used in the audit are:

| n | connected labeled cubic graphs |
|---:|---:|
| 4 | 1 |
| 6 | 70 |
| 8 | 19,320 |
| 10 | 11,166,120 |
| 12 | 11,543,439,600 |
| 14 | 19,491,385,914,000 |
| 16 | 50,233,275,604,512,000 |
| 18 | 187,663,723,374,359,232,000 |

For each order, the independently canonicalized census has no duplicate
isomorphism classes, and its exact orbit sum

`sum_(G in census_n) n!/|Aut(G)|`

equals `C_n` (the full integers are in `evidence/independent_census.json`).
Every connected labeled cubic graph belongs to an isomorphism class whose
orbit has the positive size `n!/|Aut(G)|`.  Therefore a missing class would
make the orbit sum strictly smaller than `C_n`.  Equality proves completeness.
This also reconciles the class counts
`1,2,5,19,85,509,4060,41301`, totaling 45,982, without treating the published
counts or the generator's status line as proof.
