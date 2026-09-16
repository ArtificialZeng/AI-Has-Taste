# Fresh mathematical referee report

Job ID: `win-00084-p01-referee-e6a75b59f64c`  
Frozen snapshot: `f1fbc2d615a95e3ea2b33c1c749fe2d237a9b137b08013ee93c012aff85b2b11`

## Scope and integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for the
labelled graph (K_{3,3}), with the full tube retained, no automorphism
quotient, and flips defined by exchanging one non-full tube, the diameter is
(12). Every digest in `audit/snapshot.json` agrees with the current frozen
file. In particular, `source.md` still has SHA-256
`ad57a7fcb9e8fd4626d17086a4c94e4e25059b2e75d86a8a294ec98015c3c5f1`.

## Reconstruction of the decisive argument

Encode the six labelled vertices by bits (0,ldots,5), with the first three
in one bipartition class. A nonempty induced subgraph of (K_{3,3}) is
connected exactly when it is a singleton or its vertex set meets both
bipartition classes. Thus there are

\[
6+(2^3-1)^2=55
\]

tubes, including the full tube. The full tube is compatible with every tube,
so every inclusion-maximal tubing contains it.

The main verifier enumerates graph search trees recursively: choose the root,
delete it, and independently choose a search tree on every resulting connected
component. This recursion is exhaustive and duplicate-free by induction,
because the root and the component restrictions are uniquely recoverable from
the parent vector. At every generated node the program checks that its child
descendant sets are exactly the connected components of its descendant set
after deleting that node. The resulting descendant sets give 552 distinct
six-tube states.

I separately reconstructed the state set directly from the tube definition,
without importing either submitted implementation. I generated every
pairwise-compatible set of non-full tubes in increasing mask order and tested
inclusion-maximality against all non-full tubes. The numbers of compatible
sets in sizes (0,1,2,3,4,5,6) were respectively

\[
1,54,432,1208,1380,552,0.
\]

Exactly 552 were inclusion-maximal, all of size five; adjoining the mandatory
full tube therefore gives exactly all 552 labelled maximal tubings. Their
canonical state-sequence SHA-256 was
`5621bdc6f16edfc5695d86b208dbc2ec6818d211e5c731fa498e06232b88d314`,
equal to the submitted search-tree census and to the separate Bron--Kerbosch
census.

For edges, I compared every pair of these 552 tubings directly and joined it
exactly when the symmetric difference had size two. This produced 1,380
undirected edges and degree five at every state. Its canonical edge-list
SHA-256 was
`1750eb6fc752dbd8495d2ce7706fefc117376dd98873df794ba6da7d8b1c431c`.
It agrees exactly with both submitted constructions: deletion of a non-full
tube to form a ridge, and direct parent-child search-tree rotation. The
rotation rule is also correct from components: after promoting a child (t)
above its parent (s), an old child-component of (t) joins the component
containing (s) after deleting (t) precisely when it contains a neighbor of
(s). Even without that derivation, the complete symmetric-difference edge
comparison establishes the frozen flip graph directly.

I then ran exact unweighted BFS from every state in this directly constructed
graph. Every source reached all 552 states, so all
(552^2=304{,}704) ordered pairs were covered. The eccentricity histogram was

\[
10:12,\qquad 11:108,\qquad 12:432,
\]

and the row-major distance-matrix SHA-256 was
`19dfb29ade0634468ba84ad496356bef6342f3f553bd11d1384166a7461ddd93`.
Hence every distance is at most 12. State 42,
((1,9,11,15,31,63)), is at BFS distance 12 from state 551,
((32,36,52,60,62,63)), giving the matching lower bound. The recorded path

`42, 6, 0, 1, 4, 5, 127, 130, 131, 263, 273, 275, 551`

has 12 edges, and each consecutive pair is a legal one-tube exchange. The
complete BFS row, rather than the exhibited path alone, certifies that the
endpoint distance is not smaller.

## Checks actually performed

- Recomputed all snapshot file hashes and confirmed exact agreement.
- Audited both Python programs line by line against the frozen definitions.
  Their operations are finite integer/set computations and queue traversal;
  there is no randomness, floating-point inference, or automorphism quotient.
- Reran `independent_search_tree_verifier.py` from scratch. Its complete
  rendered output had SHA-256
  `1ff8e00e363ccdff985108c96b513f08849b51f737c476f7ce58c3d0cd9b791d`,
  exactly the frozen result-file digest.
- Reran the structurally separate maximal-tubing verifier and obtained 55
  tubes, 552 maximal tubings, 1,380 edges, and diameter 12.
- Performed the direct all-compatible-subsets census and pairwise
  symmetric-difference edge construction described above.
- Independently recomputed every BFS from those edges and checked all 552
  captured layer records: source hashes, eccentricities, layer counts, layer
  state-sequence hashes, and distance-row hashes all agree. I also checked the
  complete matrix digest and every step of the recorded witness path.

The fixed labelled domain removes empty-domain and limiting issues. The full
tube convention is respected and does not create a flip. The computation
quantifies over all states and all ordered pairs, not a sample. Hard-coded
expected totals in the principal verifier merely trigger failure after the
census; they do not generate the totals, and the independent reconstruction
above confirms them.

## Source comparison and contribution

The frozen copy of Cardinal--Pournin--Valencia-Pabon gives the same tubing,
flip, search-tree, and rotation definitions; its Theorem 2 gives monotonicity,
its Theorem 8 specializes to
(operatorname{diam}R(SPK_{3,3})=13), and its Question 2 states that the
balanced complete-bipartite range remains unknown there. The frozen copy of
Gargantini--Pastine--Torres gives in Theorem 4.7 the true-twin deletion lower
bound, which here is (13-\binom{3}{2}=10); Corollary 4.8 also specializes to
10. Together with monotonicity this supports the cited prior interval
([10,13]). The latter paper reports exact balanced values only for its
(K_{2,q}) cases, not (K_{3,3}).

The finite computation therefore settles the frozen original assertion in
its full scope and improves the cited interval to the exact value 12. The
candidate appropriately limits its literature statement: this bounded source
comparison does not prove priority. I found no mathematical or scope gap in
the submitted claim. This decision certifies the frozen mathematical scope
only; it is not a manuscript, citation, visual, or publication audit.

## Verdict

**Accept.** The exact exhaustive census, exact edge construction, complete
all-pairs BFS upper bound, and checked distance-12 witness prove
(operatorname{diam}R(K_{3,3})=12) under every convention in the frozen
claim.
