# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim in `claim.json`, bound to snapshot
digest `9b7a224fffc2c65f6a4c12157a0f856e260deaf605ab42c528631b327d162ada`.
The claim is the full universal statement in `source.md`, not a restriction or
subsidiary assertion. **Verdict: accept.** The reduction covers the full stated
domain, the finite certificate covers every eligible census-edge pair, and the
listed cycles are exact witnesses.

## Reconstruction of the decisive argument

Let `(H,s,t)` satisfy the hypotheses. Since `dist_H(s,t)>=3`, `st` is not an
edge. Adding `st` preserves simplicity and connectedness and raises precisely
the two degree-2 terminals to degree 3. Thus it gives a connected simple cubic
graph `G` on 12 vertices with a marked edge `st`. Conversely, deleting an edge
`st` from such a `G` gives a graph of the required degree sequence, and it is
in the original domain exactly when the deletion is connected and its terminal
distance is at least 3. Addition and deletion are inverse operations. An
isomorphism from any `G` to a census representative maps its marked edge to an
edge of that representative. Testing all undirected edges therefore covers all
objects; the two terminal orientations do not affect cycle existence.

The frozen census contains 85 connected simple cubic graphs, each with 18
edges. For each census graph and each edge, the certificate retains exactly the
deletions for which the endpoints remain connected and are at distance at least
3. It then lists a simple 4- or 8-cycle avoiding the deleted edge. Therefore the
listed cycle is a cycle of `H=G-st`; exhaustive pair coverage proves the
universal claim.

## Checks actually performed

- Recomputed every SHA-256 listed in `audit/snapshot.json`; every frozen file
  matched. I also recomputed the canonical snapshot digest and obtained the
  recorded digest above. The immutable `source.md` retained SHA-256
  `e0696f682554b3b51d04c3ce8601d9778a1a30a06b2cb7de02681361f21db681`.
- Inspected the supplied generator and verifier rather than relying on the
  recorded success log. The verifier independently parses all 85 graphs,
  checks the vertex set, cubicity, symmetry, edge count and connectivity,
  reconstructs eligibility, validates witness edges and simplicity, rejects
  missing/extra/duplicate records, and enumerates edge subsets to recompute the
  lexicographically least cycle.
- Re-ran `verify_cycle_certificate.py` on the frozen inputs. It returned
  `VERIFIED`, with 85 census graphs, 1,530 graph-edge pairs, 1,526 connected
  deletions and 1,110 eligible pairs, and confirmed all witnesses valid and
  lexicographically least.
- Wrote and ran a fresh in-session checker without importing either supplied
  program. It independently parsed and validated the adjacency lists, used BFS
  after each edge deletion, enumerated simple 4- and 8-cycles by vertex DFS,
  normalized both orientations, selected the lexicographic minimum avoiding
  the deleted edge, and compared the resulting full mapping to the JSON. All
  1,110 records agreed exactly. The fresh check found 551 chosen 4-cycles and
  559 chosen 8-cycles; eligible-distance counts were 598, 377, 101, 21, 10 and
  3 at distances 3 through 8 respectively.
- As a census sanity check, performed exact graph-isomorphism comparisons for
  all 3,570 pairs of the 85 entries; no duplicate representatives were found.
- Checked edge cases in the logic: `s!=t` and distance at least 3 prevent an
  added loop or parallel edge; endpoint reachability after deleting their edge
  is equivalent to connectivity of the deletion because the original graph is
  connected; witnesses have distinct vertices and do not use the deleted edge.
  No division, limiting argument, numerical tolerance or random computation is
  involved.

## Source comparison and contribution

The frozen Garcia PDF states in Proposition 6.2(2) the corresponding
two-attachment counts at orders 4, 6 and 8 and a distance-at-least-3
nonexistence result at order 10. It does not state the order-12 assertion.
Definition 3.1 supplies the neighboring attachment-gadget framework. Thus the
accepted scope is a genuine order-12 extension of the cited statement, and the
claim correctly avoids asserting publication priority. The broad results in
the PDF do not replace the certificate, since a cycle in the cubic completion
could use the added edge.

## Dependencies and remaining limitations

The proof depends on the cited completeness of Meringer's official connected
cubic census and on the frozen file being the cited census; the file hash is
exactly the one named in the problem, its 85 entries validate, and they are
pairwise nonisomorphic. I did not regenerate the full cubic census from first
principles. This is an explicit external finite-classification dependency, not
a hidden scope gap. A SAT cross-check was described as preferable in the source,
not mandatory; the supplied edge-subset verifier and the fresh vertex-DFS check
already give algorithmically independent witness validation. I found no
unresolved mathematical gap in the frozen resolution claim.
