# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`61f6dc730b3ea36fedbd93fdf04c6faeed529e32b860fa10d989d8e60959ac0c`.
The SHA-256 digest of every frozen file agrees with `audit/snapshot.json`.
The submitted scope is the full question in `source.md` and `problem.md`: determine
which player wins the four-color game on the specified ten-vertex graph. It is
not a subsidiary or weakened claim.

## Reconstruction of the decisive argument

Write the vertices of the three layers as (A_i,B_i,C_i), for
(i\in\{1,2,3\}), and write the root as (w). Reconstructing the graph from
`problem.md` gives the triangle on the (A_i), all (A_iB_j) with (i\ne j),
all (B_iC_j) with (i\ne j), and the three (C_iw). This is an 18-edge graph
with degree sequence (4,4,4,4,4,4,3,3,3,3), as encoded in both the certificate
and the checkers.

The lower bound does not need to be accepted as an unexplained solver output.
In any proper three-coloring, the triangle (A_1A_2A_3) uses all three colors.
For each (j), the vertex (B_j) is adjacent to the two (A_i) with (i\ne j),
so (B_j) is forced to have the color of (A_j). The identical argument then
forces (C_j) to have the color of (B_j). The root is adjacent to all three
(C_j), which now use all three colors, a contradiction. Hence
(\chi(M_2(C_3))\ge4), and therefore (\chi_g(M_2(C_3))\ge4).

For the upper bound, `evidence/strategy.json` is a finite Alice strategy DAG.
At an Alice node it records one legal move; at a Bob node it records every raw
legal vertex-color pair. Simultaneous permutations of the three indices preserve
the graph because they preserve equality and inequality of indices, and color
permutations preserve legality and terminal status. Thus a move prescribed at a
canonical representative transports back to every state in its orbit. Every edge
adds exactly one colored vertex. Every reachable leaf is fully colored, so
backward induction on the number of uncolored vertices proves that the strategy
wins from the empty state.

## Checks actually performed

1. I reran the separately implemented certificate verifier. It checked all
   1,020 canonical nodes and 2,467 certificate edges, including exact coverage
   of 1,809 raw Bob moves, one strategy move at each of 658 nonterminal Alice
   nodes, and 36 fully colored canonical leaves. It found no dead leaf. Its
   independently computed certificate SHA-256 is
   `9d0333fe6d418d3635906381d663f2edfeb2a02ab35ac9ff5b0c00217b48a521`,
   matching both the frozen snapshot and `evidence/verification.json`.
2. I wrote and ran a fresh transport-level replay in the referee session. It
   did not merely traverse the canonical DAG: for each actual state it found an
   explicit index/color action taking that state to its canonical representative,
   transported Alice's certified move back, and expanded every legal Bob move in
   the unquotiented game. This reached 17,857 actual states through 37,728 edges,
   referenced all 1,020 canonical nodes, and ended in 1,014 fully colored actual
   leaf states and zero dead states.
3. As a separate cross-check, I implemented exact memoized minimax directly on
   unquotiented ten-tuples, without importing either submitted Python program or
   using symmetry reduction. It evaluated 19,741 states and returned that Alice
   wins from the empty state.
4. I independently exhaustively tested three-colorability and found no proper
   three-coloring, agreeing with the forced-color proof above.

These checks address turn parity, move legality, all opponent replies, terminal
semantics, graph construction, and the soundness of transporting the canonical
strategy. The replay, rather than the solver's outcome bit, is the decisive
upper-bound evidence.

## Source comparison and contribution

Within the frozen source comparison, Mou--Sun--Zhang gives only
(4\le\chi_g(M_k(C_3))\le5) for (k\ge2), while the adjacent one-layer value is
reported as 4. The present certificate selects the lower endpoint for the exact
two-layer instance, so its delta is precisely the full resolution requested in
the frozen problem. The dossier correctly describes this as a new finite question
rather than a numbered open problem and explicitly avoids a priority claim. I did
not broaden that bounded literature conclusion beyond the sources and search
limits recorded in `problem.md`.

## Gaps and verdict

I found no mathematical or scope gap requiring revision. The exact finite
certificate, exhaustive opponent-branch replay, independent unquotiented replay,
and elementary lower bound establish

\[
\chi_g(M_2(C_3))=4.
\]

**Verdict: accept.**
