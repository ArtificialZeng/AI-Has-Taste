# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in
`audit/snapshot.json`: among connected simple 4-regular graphs on 16 vertices
with a cut vertex, the maximum Eulerian-orientation count is 9216, there is one
maximizer up to ordinary isomorphism, its canonical graph6 string is
`Osc??KF@wKK?W@W@b@?oP`, and hence the proposed upper bound 9147 is false.

I recomputed the SHA-256 of every file in the snapshot and the canonical digest
of the file mapping. All file hashes matched, and the recomputed snapshot digest
was `742b93162211e835fe67ffd8e2ed442a562f83e734d6b3030d5534c3dd21d7f5`.
The recomputed hash of immutable `source.md` was
`f635a0fbcb060dd89f7ed8adf0d38bee9abbb48b3ff2c14e890671132e0df4ad`.

## Reconstruction of the argument

Let (v) be any cut vertex and let (C) be a component of (G-v). If
(d(C)) is the number of edges from (C) to (v), then

\[
4|C|=2|E(G[C])|+d(C).
\]

Thus every (d(C)) is a positive even integer. Their sum is 4, so there are
exactly two components, each joined to (v) by two edges. For each component,
the induced graph on that component together with (v) is connected, has the
root (v) of degree 2, and has every other vertex of degree 4.

Conversely, gluing the unique degree-2 roots of two connected simple graphs of
this degree type gives a connected simple 4-regular graph with a cut vertex.
The converse does not hide a connectivity assumption: deleting the root from
one rooted block cannot leave two or more components, because every resulting
component has a positive even number of incident root edges while the root has
only two edges in total. A component has at least five vertices. For fewer than
four vertices degree 4 is impossible, while for four vertices every nonroot
vertex would be adjacent to the root, forcing root degree 4. Since the two
component orders sum to 15, the only unordered size pairs are
((5,10),(6,9),(7,8)).

For any Eulerian orientation, summing outdegree minus indegree over either
component cancels internal edges and forces its two edges to (v) to point in
opposite directions. If (b(H)) denotes the number of orientations of a rooted
block in which every vertex has half its incident edges outgoing, restriction
and gluing are inverse operations, so

\[
e(G)=b(H_1)b(H_2).
\]

This factorization applies for every choice of a cut vertex. Multiple cut
vertices therefore create possible repeated representations, not an omitted
case or an assumption of uniqueness.

The block generator uses nauty `geng` with connectedness, minimum degree 2,
maximum degree 4, exact edge count (2k+1), and order (k+1), then retains
exactly one degree-2 vertex and (k) degree-4 vertices. Since the degree-2
vertex is unique, an unlabelled isomorphism class is also one rooted
isomorphism class. I checked the implementation of this filter and the graph6
decoder. The regenerated retained block counts for component orders 5 through
10 were respectively

\[
1,2,7,28,126,719,
\]

and the independently recounted maxima were

\[
24,40,64,112,192,384.
\]

The primary exact-cover counter makes each vertex choose exactly half of its
incident edges as outgoing and enforces that exactly one endpoint chooses each
edge. Its leaves are therefore in bijection with Eulerian orientations. The
separate verifier instead enumerates signed incidence vectors for two halves of
the edge set and matches opposite vectors; omitting one balance coordinate is
valid because every signed incidence vector has coordinate sum zero. This
second method regenerated all 883 retained blocks and matched every recorded
stream hash, count, maximum, and maximizing graph.

The resulting partition bounds are

\[
24\cdot384=9216,\qquad 40\cdot192=7680,\qquad
64\cdot112=7168.
\]

Hence every target graph has at most 9216 Eulerian orientations. Equality
forces the size pair ((5,10)), then forces both blocks to attain their
individual maxima. Each of those block maximizers is unique, so their root
gluing gives exactly one graph isomorphism class.

## Computational and equality checks

Using the required research interpreter, I freshly ran
`evidence/enumerate_blocks.py`, `evidence/verify_census_mitm.py`,
`evidence/enumerate_merged_graphs.py`,
`evidence/verify_merged_census.py`, and
`evidence/verify_extremizer.py`. All exited successfully.

The target census regenerated all 1167 block pairs, and both `labelg`
canonicalization and the separate `shortg` reduction returned 1167 isomorphism
classes. The canonical-stream hash was
`be334db156193ddbf59e5a676d990a32a97090e5f18a5ad1de00d0629df37a7c`,
with multiplicity histogram `{1: 1167}`. Structural checks confirmed order 16,
32 edges, degree 4 at every vertex, connectedness, simplicity, and a cut vertex
for every merger.

For `Osc??KF@wKK?W@W@b@?oP`, independent graph6 decoding and round trip gave
order 16, size 32, degree sequence (4^{16}), and articulation vertices 0 and
10. The full edge-constraint counter returned 9216. Exhausting all (2^{11})
and (2^{21}) orientations of the two blocks returned 24 and 384, and the
signed-incidence meet-in-the-middle recount independently returned 9216. The
two articulation blocks were isomorphic to the unique recorded order-5 and
order-10 block maximizers.

Finally, exact integer exponentiation verified
((4\cdot9147)^7<48^{19}<(4\cdot9148)^7), so the stated floor is 9147, and
(9216-9147=69).

## Source comparison and limitations

Within the frozen evidence, `problem.md` identifies Bartzos--Samaris,
arXiv:2609.06701v1, as the nearest inspected source and reports that its
exhaustive table stops at 15 vertices and its stated equality construction
does not include order 16. The source PDF itself is not among the frozen
evidence files authorized for this review, so I do not certify a global
priority claim or independently restate more of that paper. This does not
leave a gap in the frozen mathematical resolution, and the submitted claim
expressly makes no global priority claim. Any later manuscript attribution or
novelty wording should receive the separate citation review required by the
release workflow.

## Verdict

**Accept.** The frozen scope is the full original order-16 problem; the
structural reduction covers every admissible graph, the exact generation is
isomorph-free and reproducible, the counting algorithms are exact and
independently cross-checked, and the equality classification and counterexample
graph6 data are complete. I found no unresolved mathematical gap in the stated
claim.
