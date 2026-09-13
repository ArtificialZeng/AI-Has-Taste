# Fresh mathematical audit

Referee job: `bigMac-00007-p03-referee-88ed8063fbe9`  
Frozen snapshot digest: `cde79d0ffca4c534449707d908f5983ea532054c14cc11a1f03e5d6913fcb0c1`

## Frozen scope and verdict

The candidate is a `resolution-paper` whose exact asserted theorem is:

> Every finite connected cubic bipartite simple graph (G) with
> ‎\(|V(G)|\le 16\) has (b(G)\le 4).

I reviewed that full universal statement, not a restricted family or a sample.
The verdict is **accept**: scope, mathematical correctness, evidence, and the
claimed contribution all pass.  The minimum-order sentence involving the
cited 18-vertex graph is a corollary conditional on that cited result, as the
candidate dossier itself states; it is not used to prove the frozen theorem.

## Snapshot and integrity checks

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and every
file listed by the snapshot.  Recomputed SHA-256 values of all 17 frozen files
agree with `audit/snapshot.json`, including the source hash
`aa5cfef62d4af44d15307e47d6e6f0808902ac43328762ed19018762a3a3361e`.
The snapshot digest is the value recorded above.

The installed generator programs resolve to the recorded Homebrew nauty 2.9.3
paths.  Their fresh SHA-256 values agree with the manifest:

- `genbg`: `638224266e86d68d1cd720f18e8b7904d3571849f3da8c6130b1d0e58f515f83`;
- `shortg`: `b56794218706095371e44d8a33cef429628775f349f45a09d79a0d9980e801b7`;
- `labelg`: `0be70bdbe1c24030b1ed80652026c8284fff8700fb0a0a9331742d593a514bca`.

The executable version output is `Nauty&Traces version 2.9301 (32 bits)`;
the manifest identifies the enclosing Homebrew release as 2.9.3 and also
records the executable paths and byte hashes, so the toolchain is unambiguous.

## Reconstruction of the finite domain

Let (X\mathbin{\dot\cup}Y) be a bipartition.  Cubicity gives
(3|X|=|E|=3|Y|), hence ‎\(|X|=|Y|=m\).  Simplicity and degree three force
(m\ge 3).  Therefore the only orders at most 16 are
(2m=6,8,10,12,14,16), with (m=3,\ldots,8).  This also disposes of empty
and smaller boundary cases.

For each such (m), the literal generator options
`-d3:3 -D3:3 m m 3m:3m` impose degree exactly three on both colour classes;
`-c` imposes connectedness.  `genbg` supplies bicoloured isomorphism-class
representatives.  A connected bipartite graph has a unique bipartition up to
swapping its two parts.  Applying `shortg -q` with no colour partition thus
collapses precisely the remaining identifications caused by forgetting the
two colours, and `labelg -q -g` gives uncoloured canonical graph6 strings.
Consequently the pipeline covers every uncoloured isomorphism class in the
frozen scope and does not rely on an assumed labelling of the parts.

I freshly ran both the all-graph and connected literal `genbg` invocations and
streamed the connected output through the recorded uncoloured/canonical
pipeline.  The independently observed triples

| order | all bicoloured | connected bicoloured | connected uncoloured |
|---:|---:|---:|---:|
| 6 | 1 | 1 | 1 |
| 8 | 1 | 1 | 1 |
| 10 | 2 | 2 | 2 |
| 12 | 7 | 6 | 5 |
| 14 | 16 | 15 | 13 |
| 16 | 51 | 48 | 38 |

agree with the manifest.  After byte sorting, every regenerated order corpus
has exactly the frozen SHA-256 value.  Thus the decisive corpus contains
(1+1+2+5+13+38=60) representatives and was reproduced without rewriting
any frozen file.

## Reconstruction and attack of the certificates

For a fixed graph and a four-edge set (F), it is enough to establish
‎\(\gamma(G-F)>\gamma(G)\): the definition then immediately gives
(b(G)\le |F|=4).  Deleted graphs may be disconnected and may contain
isolated vertices; direct closed-neighbourhood enumeration continues to count
those vertices correctly.  No limiting, probabilistic, or floating-point
step occurs.

The bundle criterion used by the primary program is sound.  Edge deletion
cannot decrease domination number.  A minimum dominating set (D) ceases to
dominate after deleting (F) exactly when some (x\notin D) loses every edge
from (x) to (D), equivalently (B_G(D,x)\subseteq F).  Hence destroying
every original minimum dominating set is equivalent to strict increase.  The
primary program additionally recomputes the deleted domination number rather
than relying only on that equivalence.

I did not rely on the bundle criterion for the decisive fresh check.  I
separately decoded each graph6 string, reconstructed its lexicographically
indexed edge list, checked simplicity, connectedness, bipartiteness, degree
three, and equal part sizes, and then enumerated vertex subsets by cardinality.
For both the original graph and the graph after its recorded four-edge
deletion, a subset was accepted only when the union of its closed
neighbourhoods was the full vertex set.  All 60 edge lists and witnesses agree
with `primary_results.json`, and every recomputed deleted domination number is
strictly larger.  The exact distribution of fresh pairs
‎\((\gamma(G),\gamma(G-F))\) is

- ‎\((2,3)): 2 graphs;
- ‎\((3,4)): 2 graphs;
- ‎\((4,5)): 30 graphs;
- ‎\((4,6)): 11 graphs;
- ‎\((5,6)): 15 graphs.

For an audit checksum, the compact JSON serialization of the 60 freshly
recomputed rows `(graph_id, gamma, deleted gamma, deletion indices, first
minimum mask before, first minimum mask after, number of minimum sets before,
number after)` has SHA-256
`35d546201df6d60476d7857f558fd53718b46c5353434a593870759d5f206082`.
This agrees in substance with, but was computed without importing, either
frozen verifier.  I also inspected the two frozen implementations.  The
second imports no primary code, reparses graph6 independently, and enumerates
all (2^n) vertex masks directly; its frozen output records `status=pass` and
60 confirmations.

The quantifier attack therefore leaves no uncovered order or isomorphism
class, and every class has an exact four-edge witness.  It follows that the
frozen universal assertion is proved.

## Source comparison and contribution

Within the permitted frozen source material, the nearest identified result is
Yavari, arXiv:2609.04257v1, Theorem 1.2/Lemma 2.2/Appendix A: it supplies and
checks one 18-vertex cubic bipartite graph with (b=5), but the inspected
comparison reports no assertion of minimality and no exhaustion through order
16.  The dossier appropriately labels broader literature status as uncertain
and makes no unconditional priority claim.  The present result is not a toy
restriction or a sample: it exactly resolves the original bounded universal
problem with a reproducible complete corpus and per-class certificates.  This
is a nontrivial, usable minimum-order refinement, subject to ordinary later
citation verification for the attributed 18-vertex premise.

## Final verdict

**Accept.**  Scope passes, correctness/evidence passes, and contribution
passes.  There is no mathematical gap requiring revision.  Later manuscript
work should retain the current careful wording that the 18-vertex
minimum-order corollary uses the cited Yavari result and that the literature
search does not establish priority.
