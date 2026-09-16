# Fresh mathematical referee report

Job: `win-00066-p03-referee-60d472323bf3`  
Frozen snapshot: `d248f45250edb03d49215e1294f64340b70c956ded27d975d67ff63b70be30fe`

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`, without
altering its scope. The snapshot hashes of `source.md`, `problem.md`,
`claim.json`, and every listed evidence file agree with `audit/snapshot.json`.
The source fixes a simple undirected graph on vertices 0 through 17 with 27
distinct edges and asks for every five-edge deletion raising the domination
number, followed by the complete classification under the full automorphism
group. The submitted claim answers that entire labelled and orbit-level
question; it is not a restriction or a subsidiary statement.

## Reconstruction of the domination calculation

I rebuilt the graph from the displayed edge list. Direct exhaustion of vertex
subsets gives no dominating set of size 0 through 5 and exactly 297 dominating
sets of size 6, so the base value is exactly \(\gamma(G)=6\).

For the deletion classification I independently examined all
\(\binom{27}{5}=80{,}730\) edge-index subsets. For each deletion I rebuilt the
18 closed neighborhoods and tested the 297 possible six-vertex dominators by
exact bit unions. Restricting this test to base-graph dominators is sound:
deleting edges cannot create a dominating set, and any dominating set of size
at most six can be enlarged to one of size six. Exactly 801 deletions admitted
no such set. Their sorted-mask SHA-256 is
`d84f0d0011e2a07f214f2f80db42aa048ab40f0d452419867ce586c71744c589`,
identical to the frozen certificate.

For every one of those 801 deleted graphs I separately exhausted the 2,826
base-graph dominating seven-sets until finding a seven-vertex witness and
checked that witness against the rebuilt deleted graph. Thus every qualifying
deletion has domination number at most 7. Monotonicity under edge deletion and
the absence of a six-set give the reverse bound, so every value is exactly 7.
This also checks the quantifier over the entire labelled family, rather than
only the orbit representatives.

## Automorphisms, orbits, and stabilizers

I exhaustively enumerated vertex bijections by a fresh adjacency/nonadjacency
preserving backtrack. At each partial bijection all assigned pairs were checked,
and all admissible unused images were explored; hence every completed map is an
automorphism and every automorphism is reached. The result is exactly the six
permutations serialized in the certificate.

Acting with these six maps on the independently recovered 801-set family and
removing complete orbits gives 140 orbits. For each of the 140 records I checked
all of the following directly:

- the edge indices decode to the displayed five unordered edges;
- the representative is lexicographically least among its six group images;
- the listed orbit size equals the number of distinct images;
- the listed permutations are exactly all group elements stabilizing the edge
  set setwise, and their count is the stated stabilizer order;
- the supplied seven-set dominates the corresponding deleted graph, while no
  six-set does.

The resulting distribution is 127 orbits of size 6 with stabilizer order 1 and
13 orbits of size 3 with stabilizer order 2. The orbit sizes sum to
\(127\cdot6+13\cdot3=801\), and the reconstructed orbits partition the full
qualifying family with neither omissions nor duplicates. The referee replay and
its compact output are recorded in `audit/referee_replay.py` and
`audit/referee_replay.json`.

## Source comparison and contribution

I inspected the supplied nine-page primary-source PDF. Its Equation (3.1) gives
the same graph; Proposition 3.2 proves \(\gamma(G)=6\); Propositions 4.1 and 4.2
establish \(b(G)=5\), exhibit one five-edge deletion with domination number 7,
and certify all four-edge deletions. The paper does not enumerate all qualifying
five-edge deletions, compute the automorphism group, or give an orbit/stabilizer
classification. The submitted exact classification is therefore a substantive
full answer to the frozen follow-up problem and a genuine refinement of the
cited result. The accompanying triage search is explicitly limited, and the
claim appropriately makes no broader literature-priority assertion.

I found no unresolved scope, correctness, or evidence gap. In particular, the
checks cover isolated vertices automatically, use setwise rather than pointwise
stabilizers, and do not infer proof from numerical approximation, a successful
build, or the earlier screening totals.

## Verdict

**Accept.** The frozen candidate resolves the original finite classification in
its full stated scope, its exact certificate is complete, and an independent
reconstruction verifies every decisive count and every orbit record.
