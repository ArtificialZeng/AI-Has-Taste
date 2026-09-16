# Fresh mathematical referee report

Job: `win-00050-p03-referee-03c41a648316`  
Frozen snapshot: `2b62378c51eb110d8aa3005927115c82e5148ea81297d36a3963e896a425734c`

## Scope reviewed

The frozen candidate is a `resolution-paper` claim for exactly the graph
`H=M_3(C_3)` defined in `problem.md`: Alice wins the standard proper
vertex-coloring game with four colors, and therefore
`chi_g(H)=4`. No claim for another value of the layer parameter is included.
This is the full scope of the original finite dichotomy in `source.md`, not a
subsidiary or weakened statement.

All eleven hashes in `audit/snapshot.json` were recomputed before review and
match the snapshot. In particular, the immutable `source.md` has SHA-256
`c0d0c081d5a1c93fc6ff6d0ce06f2d863e7eae66def156bda26d1cd85a0f6b1c`,
and the compressed certificate has SHA-256
`40ff6a4fa5b25e754257d6f538d66f14af76e6c0291d0f4eddb06c0c428aec80`.

## Reconstruction of the target and lower bound

From the graph formula there are twelve vertices `v_i^m`, with
`0<=m<=3` and `i` modulo 3, together with `omega`. The base layer is a
triangle. Between each pair of consecutive layers, `v_i^m` is joined to
`v_j^(m+1)` exactly when `i!=j`, and `omega` is joined to all three vertices
of layer 3. Direct reconstruction gives 13 vertices, 24 edges, nine vertices
of degree 4 and four of degree 3.

The ordinary chromatic lower bound in `evidence/research.md` is correct. In a
hypothetical three-coloring, write the three distinct colors on the base
triangle as `c_i` on `v_i^0`. The vertex `v_i^1` is adjacent to the other two
base vertices, so its only possible color is `c_i`. The identical argument
propagates from layer `m-1` to layer `m` for `m=2,3`. The three neighbors of
`omega` in layer 3 then use all three colors, a contradiction. Thus
`chi(H)>=4`, hence `chi_g(H)>=4`.

## Reconstruction and audit of the four-color strategy proof

The certificate uses the fixed vertex order
`v0_0,v0_1,v0_2,...,v3_2,omega`, colors `0,1,2,3`, and `4` as the empty
marker. Its root is the all-empty position. It prescribes Alice's first move
as color 0 on `v0_0`; at the ensuing Bob node it explicitly contains all 44
raw legal vertex-color pairs, including distinct pairs that canonicalize to
the same child.

The proof principle is finite backward induction on the number of uncolored
vertices. At each Alice node the certificate supplies one legal move. At each
Bob node it supplies every raw legal move, without orbit deduplication. Every
edge adds exactly one colored vertex. A leaf is accepted only when all thirteen
vertices are properly colored; a position with an uncolored vertex seeing all
four colors is instead a Bob terminal. Therefore, if every child appearing at
an Alice node and every child forced by complete Bob branching is already
certified for Alice, that node is certified for Alice. Induction from the
leaves to the root proves the claimed strategy.

Symmetry reduction is sound here. Each simultaneous permutation of the three
indices preserves every edge, and every global color permutation preserves
properness, legal moves, turn parity, and both terminal conditions. There are
exactly six graph automorphisms: `omega` is the unique degree-3 vertex with
three degree-3 neighbors and is fixed; distance from `omega` then fixes each
layer set; a permutation of the base triangle determines all higher layers
because between consecutive layers the equal-index pair is the unique
nonedge. Thus the six simultaneous index permutations are the full group.
Using a canonical representative cannot change the winner, and a prescribed
move can be transported back along the same graph/color symmetry in an actual
play.

I performed three reproducible checks:

1. `evidence/verify_q4_strategy.py`, which imports no solver code and uses
   NetworkX to enumerate graph automorphisms plus all 24 color permutations,
   replayed the frozen certificate successfully. Its fresh report is
   `audit/referee_replay.json`.
2. I wrote and ran `audit/referee_verify.py`, which imports neither supplied
   program, reconstructs the edge set directly, explicitly verifies each of
   the six used vertex maps preserves it, and exhausts all 24 color
   permutations. It additionally checks the declared vertex order and that
   every stored node is reachable from the root. Its report is
   `audit/referee_independent_verification.json`.
3. Fresh execution of the supplied exact solver to
   `audit/referee_regenerated_strategy.json.gz` returned Alice and produced a
   byte-for-byte identical SHA-256 digest to the frozen certificate.

Both replay paths agree on 22,071 root-reachable canonical nodes, 61,173
edges, 45,761 raw Bob-response edges, and 400 terminal nodes. The terminals
are all fully colored Alice wins. The independent replay checked properness
and canonicality of every node, legality and exact canonical child of every
edge, strict depth increase, complete raw Bob branching with multiplicity,
terminal conditions, full reachability, and backward induction. It certifies
Alice at the empty root.

## Source comparison and contribution

The frozen primary PDF was inspected directly. Its generalized Mycielski
formula yields exactly the graph reviewed above. Theorem 3.1 gives the general
five-color upper bound. Theorem 5.1(1) states only
`4<=chi_g(M_k(C_3))<=5` for `k>=2`; it does not give the exact `k=3` value.
Proposition 2.1 concerns the classical one-layer construction. Thus the
candidate's exact 13-vertex result is a genuine strict delta from the nearest
result documented in the frozen source.

The frozen literature report records exact-assertion and equivalent-language
searches dated 2026-09-07 and reports no exact `M_3(C_3)` result. That negative
search is not proof of priority, and the candidate appropriately avoids
claiming either that the source authors posed this instance as open or that
priority is established. This bounded novelty language is acceptable for the
claimed resolution.

## Gaps and verdict

No mathematical or frozen-scope gap remains. The ordinary three-color lower
bound and the exhaustive four-color Alice certificate together establish
`chi_g(M_3(C_3))=4` for exactly `k=3`. The computational result meets the
source requirement of a complete replayable strategy DAG with legal-move,
terminal-condition, color-renaming, graph-automorphism, and exhaustive
opponent-branch checks.

**Verdict: accept.**
