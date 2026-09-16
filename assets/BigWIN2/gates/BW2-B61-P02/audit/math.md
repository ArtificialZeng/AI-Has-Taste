# Fresh mathematical referee report

## Frozen scope and decision

I reviewed the frozen `resolution-paper` claim at snapshot
`2990a8c9ff08f78a3cb4db6300fc504e74dad1d1811797725d7a7d961a21771c`.
The claim is the full finite statement in `source.md`, with the explicit convention in
`problem.md`: for every `0 <= n <= 6`, every simple graph `G` on the common labelled
vertex set is Hall-universal. The asserted census is therefore all-positive, with layer
counts `1,1,2,4,11,34,156` and no negative class.

**Verdict: accept.** The frozen computation covers the stated quantifiers, the decisive
predicates implement the source definition exactly, the independent verifier recomputes
the full certificate by materially different subroutines, and the resulting Hall-feasible
and colorable status arrays coincide everywhere. The result settles the frozen finite
problem; it does not purport to settle the source's unrestricted characterization.

## Reconstruction of the decisive argument

Fix a representative `G` on `V={0,...,n-1}` and a labelled graph `H` on `V`. For a
color `c`, the vertices eligible to receive `c` are

`{v : c in N_G(v)} = N_G(c)`,

where the equality uses that `G` is undirected. Thus, for a vertex subset `U`, the
Hilton--Johnson summand for `c` is exactly

`alpha(H[U intersect N_G(c)])`.

The census code tests

`|U| <= sum_c alpha(H[U intersect N_G(c)])`.

It is enough for the main enumerator to test nonempty connected induced `H[U]`. For a
fixed vertex set, deleting edges from the induced graph can only increase every
independence number, so induced subgraphs are the hardest subgraphs. For a disconnected
induced graph, independence numbers and cardinalities add over its connected components,
so its inequality is the sum of the component inequalities. The independent verifier
nevertheless tests every nonempty `U`, avoiding reliance on this reduction in the
certificate comparison.

For colorability, an admissible map `phi:V -> V` is one satisfying
`phi(v) in N_G(v)`. Associate to it the conflict mask

`Q_phi={uv : phi(u)=phi(v)}`.

Then `phi` properly colors exactly those `H` for which
`E(H) intersect Q_phi` is empty. Enumerating all `n^n` maps therefore gives an exact,
finite colorability test. The main enumerator marks the downward closure of every
admissible conflict mask. The independent verifier instead builds the distinct conflict
masks and tests each `H` directly against them.

Every labelled simple `H` occurs once as an increasing edge mask among the
`2^(n choose 2)` masks. One `G` per isomorphism class suffices: simultaneous relabelling
of the vertices and colors preserves both the Hall inequalities and proper graphic-list
colorability. Completeness of the representative domain is not inferred only from atlas
counts. The verifier enumerates every labelled `G`, applies every vertex permutation,
and proves that the set of canonical masks is exactly the recorded set, deriving the
counts `1,1,2,4,11,34,156`.

Consequently, equality of the two recorded status bits for every pair `(G,H)` proves
Hall-universality of every class.

## Checks actually performed

1. I checked the SHA-256 values of the decisive frozen files against
   `audit/snapshot.json`. The census, representatives, enumerator, verifier,
   classification, manifests, source PDF/text, claim, problem interpretation, and result
   files all match their recorded digests. I also recomputed the snapshot digest from the
   canonical sorted compact JSON serialization of its file mapping and obtained
   `2990a8c9ff08f78a3cb4db6300fc504e74dad1d1811797725d7a7d961a21771c`.

2. I audited `census_numba.py` against the definitions. Its deletion recurrence for
   independence number is exact; adjacency masks represent precisely open
   neighborhoods; the Hall loop uses the correct eligible-vertex set for each color; and
   the conflict-mask downward closure is equivalent to existence of a proper admissible
   assignment. All integer ranges are safe at `n <= 6`: vertex masks are below `64`, edge
   masks below `32768`, independence numbers at most `6`, and the assignment enumeration
   has at most `6^6=46656` maps.

3. I reran

   `python3 evidence/verify_census.py evidence/census_exact.tsv evidence/census_manifest.json evidence/representatives.tsv`.

   It exited successfully after independently verifying every layer `n=0,...,6`. This
   verifier uses brute enumeration of independent submasks instead of the deletion
   recurrence, checks all nonempty `U` instead of connected `U`, directly tests each `H`
   against the assignment conflict list instead of taking downward closures, decodes
   graph6 through NetworkX, and reconstructs the complete canonical `G` domain from all
   labelled graphs.

4. I separately parsed every census row and recomputed the bit counts, implication
   failures, reverse implication failures, witnesses, unused packed-bit padding, row-key
   alignment, row digests, and aggregate digest. There are exactly `209` unique aligned
   representative rows and `5,147,366` canonical-representative/labelled-`H` pairs. The
   exact layer summaries are:

   | n | classes | pair statuses | Hall | colorable | Hall and uncolorable |
   |---:|---:|---:|---:|---:|---:|
   | 0 | 1 | 1 | 1 | 1 | 0 |
   | 1 | 1 | 1 | 0 | 0 | 0 |
   | 2 | 2 | 4 | 2 | 2 | 0 |
   | 3 | 4 | 32 | 12 | 12 | 0 |
   | 4 | 11 | 704 | 392 | 392 | 0 |
   | 5 | 34 | 34,816 | 19,984 | 19,984 | 0 |
   | 6 | 156 | 5,111,808 | 3,597,344 | 3,597,344 | 0 |

   There are also zero colorable-but-non-Hall entries, so the two bit arrays are identical
   on all represented pairs. The recomputed aggregate status digest is
   `12221d88ef732ca8cc7dd655fdf473a3635522b4e64b14fe283cfcc120b88531`.

5. I reran the source-family classifier to `audit/referee_classification.tsv`; its output
   is byte-for-byte identical to `evidence/census_classification.tsv`. It gives `199`
   source-covered classes and exactly ten remaining finite-census classes:
   `DBk, DBw, DB{, E?NW, E?No, E?Nw, E?]o, E?]w, E?^o, E?^w`.
   In `(n,graph6)` order the first is `DBk`, mask `880`. Decoding that mask gives triangle
   edges `23,24,34` and pendant edges `13,04`, so it is the bull graph as asserted.

## Quantifier and edge-case attacks

- For `n=0`, there is one empty `G`, one empty `H`, a vacuous Hall condition, and the
  unique empty coloring. Both exact bits are `1`.
- If `G` has an isolated vertex `v`, no admissible coloring exists, but Hall already fails
  on `U={v}`. Such a `G` is therefore Hall-universal vacuously. This explains, rather than
  hides, the zero Hall and colorability counts at `n=1`.
- Empty lists, repeated colors, disconnected `H`, non-induced subgraphs, and all equality
  cases are covered by the reductions above and by the verifier's redundant all-`U`
  check.
- Packed status ordering is explicit: increasing `H` masks and little-endian bits within
  bytes. The referee-side parse found zero nonzero padding bits and exact agreement of all
  row and aggregate bindings.
- The table heading "labelled `(G,H)` pairs" in `evidence/result.md` should be read more
  precisely as "canonical `G` representative / labelled `H` pairs"; the numbers are
  `classes(G) * 2^(n choose 2)`. This is an editorial label, not a missing quantifier,
  because the complete labelled-`G` orbit check and relabelling invariance cover every
  labelled `G`.

## Source comparison and contribution

The frozen primary-source text defines Hall-universality in Definition 4.1 exactly as used
here. Its discussion states that Hall's condition may be checked on connected induced
subgraphs. Proposition 2.10 supplies the isolated-vertex vacuity; Theorem 4.6,
Proposition 4.9, Theorem 4.11, Theorem 4.16, Theorem 4.19, and Remark 4.12 are the source
families used by the classifier. The source's conclusion asks for the general
characterization and does not state this finite census.

The ten classes not recognized by those families make the finite census more than a mere
aggregation of the cited theorems, while the exact per-`H` arrays and independent verifier
make the full finite claim reproducible. The recorded search is only a limited literature
screen, and neither the claim nor this verdict treats it as proof of priority. The source
PDF/text identify Parikshit Chalise as author although immutable `source.md` says Timothy
Sun; theorem numbering, definitions, and mathematical content match, so this bibliographic
discrepancy does not affect the proof.

No unresolved mathematical gap remains within the frozen scope. The editorial pair-count
heading can be corrected during manuscript preparation without changing the claim or its
decisive evidence.
