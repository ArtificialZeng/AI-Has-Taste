# Exact four-color result for `M_3(C_3)`

Provenance: `win-00050-p03-research-a7565dec9c2e` (research pass 1,
2026-09-07).

## Result

Alice has a winning strategy in the standard vertex-coloring game on the
13-vertex graph `H=M_3(C_3)` fixed in `problem.md` when the common color set has
four colors.  Consequently `chi_g(H)=4`.  No claim is made for `k` other than
3.

For completeness, the lower bound is elementary.  In any hypothetical proper
three-coloring, the base triangle has three pairwise distinct colors, say
`c_0,c_1,c_2` on `v_0^0,v_1^0,v_2^0`.  Each `v_i^1` is adjacent to the other
two base vertices and is therefore forced to have color `c_i`.  Inductively,
if layer `m-1` has colors `c_i` at index `i`, the same adjacency forces layer
`m` to do so.  Thus the three vertices of layer 3 have all three colors, leaving
no color for their common neighbor `omega`, a contradiction.  Hence
`chi(H)>=4`, and therefore `chi_g(H)>=4`.  This agrees with the more general
lower bound in Mou--Sun--Zhang, Theorem 5.1(1); the certified Alice strategy
supplies `chi_g(H)<=4`.

## Exact certificate and proof principle

`solve_game.py` performs integer-only minimax.  A position is a length-13 tuple
whose entries are colors `0,1,2,3` or the empty marker `4`.  It canonicalizes a
position under color renaming and the six simultaneous permutations of the
three indices.  It returns Alice as the winner after visiting 29,161 canonical
minimax states and writes `q4_strategy.json.gz`.

The compressed certificate is a strategy DAG with 22,071 nodes and 61,173
edges.  At every nonterminal Alice node it records one prescribed legal move;
at every nonterminal Bob node it records every raw legal vertex-color move,
including moves with the same canonical child.  Every edge increases the
number of colored vertices by one.  All 400 terminal nodes in this DAG are
fully colored Alice wins.

This is a finite proof by backward induction.  At a terminal certificate node
Alice has won.  At an Alice node she selects the recorded child; at a Bob node
every possible legal reply is recorded.  Induction on the number of remaining
uncolored vertices therefore shows that every certificate node, including the
empty root, is winning for Alice.  Passing to a canonical representative is
sound because graph automorphisms and global color permutations preserve legal
moves and both terminal conditions.

## Independent replay

`verify_q4_strategy.py` imports no solver code.  It reconstructs the graph from
the layer formula, uses NetworkX graph isomorphism to enumerate all graph
automorphisms, and independently obtains six.  For canonicalization it directly
enumerates all 24 color permutations for each graph automorphism rather than
using the solver's first-occurrence normalization.  It then checks:

- 13 vertices, 24 edges, the stated degrees, and every position's properness;
- canonicality of every node and reconstruction of every canonical child;
- legality of every stored move and the terminal condition at every leaf;
- exact completeness, without orbit deduplication, of all 45,761 Bob-response
  edges; and
- the winner condition bottom-up through the entire acyclic strategy.

The run completed with status `verified`; its machine-readable report is
`q4_verification.json`.  The deterministic compressed certificate has SHA-256
`40ff6a4fa5b25e754257d6f538d66f14af76e6c0291d0f4eddb06c0c428aec80`.
Generating it twice at different output paths produced this same digest.

Reproduction from the project root:

```text
python3 evidence/solve_game.py --output evidence/q4_strategy.json.gz
python3 evidence/verify_q4_strategy.py
```

The project-local primary-source copy is `evidence/external/2609.02283.pdf`, with SHA-256
`42a09d9f05b1ab5b3fe51662cab09cb61e3d5e7660703fc9840b4a8e3bc67504`.
