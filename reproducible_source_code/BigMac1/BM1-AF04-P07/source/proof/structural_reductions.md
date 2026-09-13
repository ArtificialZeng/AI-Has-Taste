# Structural reductions

These reductions are independent of the exhaustive endpoint computation and
record what a hypothetical counterexample would have to look like.

## Leave-graph lemma

Let `P` be a maximal packing of transitive triples in a tournament `T`, and
let `L(P)` be the simple graph on `V(T)` whose edges are the unordered pairs
not used by `P`.

**Lemma.** Every triangle of `L(P)` is oriented cyclically in `T`.
Consequently `L(P)` is `K_4`-free.  If `|V(T)|=11` and `|P|=q`, then

```text
|E(L(P))| = 55 - 3q.
```

**Proof.** If a triangle of `L(P)` were transitive, all three of its arcs
would be unused and it could be added to `P`, contrary to maximality.  If
`L(P)` contained a `K_4`, the tournament induced on those four vertices would
contain a transitive triple: a vertex of maximum internal outdegree has at
least two out-neighbours and is the source of a transitive triple with any
two of them.  This transitive triple would be a triangle of `L(P)`, a
contradiction.  The edge count follows because each packed triple uses three
distinct pairs.  QED.

Thus any putative order-11 tournament with maximum packing at most 14 has a
maximum packing whose leave is a `K_4`-free graph with at least 13 edges.  The
condition is necessary, not sufficient, and is not substituted for the exact
enumeration.

## One-vertex extension reduction

Fix a vertex `v` and a 12-packing `P` in `T-v`.  Let `L` be its leave graph on
the other ten vertices.  Call an edge `ab` of `L` *v-admissible* when the
triple `{v,a,b}` is transitive in `T`.

**Lemma.** The packing `P` extends by three transitive triples through `v` if
and only if the graph of `v`-admissible leave edges contains a matching of
size three.

**Proof.** Three added triples through `v` cannot share a spoke incident with
`v`, so their opposite leave edges have six distinct endpoints and form a
matching.  Conversely, three pairwise vertex-disjoint admissible leave edges
use three previously unused opposite arcs and six distinct spokes at `v`, so
the corresponding triples are arc-disjoint from each other and from `P`.
QED.

This isolates the exact obstruction to the naive deletion argument.  The
fact that a 12-packing leaves nine edges in `K_10` does not by itself force a
3-matching (a nine-edge star is the elementary graph-theoretic obstruction),
and admissibility adds orientation constraints.  Therefore the certified
`n=10` baseline alone does not imply the order-11 target without either a
stronger choice theorem for the 12-packing or the complete order-11 search.
