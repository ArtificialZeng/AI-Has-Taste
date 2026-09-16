# Mathematical referee report

## Frozen scope

I reviewed the exact `result-note` claim bound to snapshot
`85ee0a597a72c51d2de2e96e1502f1a2729b3d4d2119b9528bb1a145de45c816`.
The claim is the finite theorem that every legal graph on at most ten vertices
has B-chromatic index at most nine, with sharpness at `K_{3,3}`.  It explicitly
leaves the original determination of `M_3(4)` unresolved.

## Reconstruction of the decisive argument

It is enough to enumerate connected graphs.  A 4-cycle cannot use two graph
components, so the B-conflict graph of a disjoint union is the disjoint union
of the component B-conflict graphs and its chromatic number is the maximum of
the component chromatic numbers.

For orders at most seven, the NetworkX Graph Atlas supplies one representative
of every simple isomorphism class.  For each subsequent order `n=8,9,10`, the
generator is complete by induction: every connected graph on at least two
vertices has a non-cut vertex; deleting such a vertex leaves a connected
induced graph of order `n-1`; and all three class conditions (maximum degree at
most four, degeneracy at most three, and absence of `K_{3,4}`) are hereditary
under vertex deletion.  After identifying the remaining graph with a generated
representative, restoring the deleted vertex is exactly one of the enumerated
nonempty neighborhoods of size at most four among vertices whose old degree is
below four.  The degree sequence, triangle count, and Weisfeiler--Lehman hash
are used only as isomorphism-invariant buckets.  Within a bucket, every actual
deduplication decision uses an exact graph-isomorphism test, so bucketing cannot
merge nonisomorphic graphs or separate two isomorphic graphs from comparison.

The legality predicates match the definitions.  The maximum core number is at
most three exactly when the graph is 3-degenerate.  A simple graph contains a
`K_{3,4}` subgraph exactly when some triple of vertices has at least four common
neighbors.  In the optimized order-ten extension check, any newly created
`K_{3,4}` must use the new vertex.  If it lies on the four-vertex side, three
members of its neighborhood have three old common neighbors; if it lies on the
three-vertex side, its neighborhood has size four and two old vertices are
adjacent to all four members.  These are precisely the two tested cases.  When
the new degree is at most three, placing the new vertex first extends a
3-degeneracy deletion ordering; degree four is checked by the core-number test.

For distinct edges `uv` and `xy`, the conflict-graph construction adds an edge
exactly when the original edges meet, or, when disjoint, when either pair of
cross edges `ux,vy` or `uy,vx` exists.  This is exactly incidence or opposition
on a simple 4-cycle.  Thus proper nine-colorability of the constructed graph is
equivalent to a nine-color B-coloring.

The SAT encoding gives every conflict-graph vertex exactly one of nine colors
and forbids equal colors at adjacent vertices.  Each returned model is decoded
and checked for a unique assignment and against every conflict edge.  A
separate exhaustive DSATUR backtracker agrees on every class.  The recorded
class counts are 1,918 at order eight, 12,177 at order nine, and 89,299 at order
ten, and no non-nine-colorable class occurs.  Together with the Atlas screen,
this proves the asserted upper bound through order ten.

Sharpness is direct: `K_{3,3}` is legal, has nine edges, and every two of its
edges either meet or are opposite on a 4-cycle, so its B-conflict graph is
`K_9`.  Finally, if any legal graph has B-chromatic index ten, the component
reduction shows that some component has index ten; the finite theorem forces
that component to have at least eleven vertices.

## Checks performed

All files named by the snapshot matched their recorded SHA-256 digests.  I
inspected the generation, legality, conflict-graph, SAT, model-checking, and
backtracking code from the definitions, including the quantifiers in the
optimized `K_{3,4}` test.  I also performed a fresh full run of
`evidence/n10_sat_screen.py`.  It reconstructed all lower-order bases and
reproduced the recorded 933,827 raw legal order-ten extensions, 89,299 exact
isomorphism classes, zero failures of nine-colorability, representative digest
`34cab285445605740c842d5dd18a697e5dd67b96a93b58b11de82980840d998c`,
and checked-coloring digest
`67c759b488d1acdec07b534370b23a355c9cb1504d4172ba8106a2a2f76e209c`.

## Source comparison and remaining limits

The frozen source gives only `9 <= M_3(4) <= 10`.  This candidate does not
silently replace that problem: its precise delta is to exclude all value-ten
witnesses through order ten, thereby raising the minimum possible connected
witness order to eleven.  Exhausting 89,299 top-order classes with exact
generation and checked colorings is a nontrivial finite result, and the lower
bound is directly useful for subsequent witness searches and structural
arguments.  The bounded literature search recorded in `problem.md` is not a
proof of priority, and the exact value of `M_3(4)` remains unresolved; both
limitations are honestly disclosed and do not create a gap in the frozen
finite theorem.

## Verdict

**Accept.**  The scope is exact, the computational exhaustion is complete and
reproducible, the sharpness and component consequence follow, and the partial
contribution is nontrivial without claiming to solve the original problem.
