# Fresh mathematical referee report

**Referee job:** `win-00050-p02-referee-1bc3e6cb8a76`  
**Frozen snapshot:** `80dc45be7a9a5aeb0056d6e99c6c8f58fd4127f10735f766f8a80c62dc4485b3`  
**Candidate scope:** the exact `resolution-paper` statement in `claim.json`  
**Verdict:** **accept**

## Scope assessed

I assessed the full frozen assertion, without weakening it: under the explicitly
fixed two-item cyclic-Gray-code convention, every connected unlabeled loopless
simple graph on two through six vertices has Hamiltonian acyclic-orientation
flip graph if and only if its acyclic signature is zero.  The asserted census is
142 graph classes, split into 125 positive and 17 negative cases, with the exact
order counts and negative graph6 identifiers stated in `claim.json`.

The candidate also claims the full certificate requested by the immutable
source: every graph, orientation, and flip edge is serialized; every positive
case has a cycle; and there are no zero-signature negative cases requiring a
separate non-Hamiltonicity certificate.

## Reconstructed argument

1. For a graph on (n\leq 6), enumerate every one of the
   (2^{\binom n2}) labeled simple graphs.  Connectedness is an exact finite
   test.  Quotienting by all (n!) vertex permutations and choosing the least
   graph6 encoding gives respectively (1,2,6,21,112) classes for
   (n=2,3,4,5,6), hence 142 total.  This proves both coverage and uniqueness
   of the finite graph domain once the resulting identifier set agrees with the
   serialized atlas.

2. For each representative with lexicographically ordered edges, enumerate all
   orientation masks.  An exact directed-cycle test selects precisely the
   acyclic masks.  Two selected masks are adjacent precisely when their XOR has
   one set bit.  Thus exhaustive reconstruction of the selected masks and these
   pairs verifies the complete vertex and edge set of every serialized
   (AO(G)).

3. Mask-weight parity bipartitions every flip graph, because a flip changes
   exactly one bit.  The difference between the two part sizes is
   
   \[
     \sum_{A\text{ acyclic}}(-1)^{\operatorname{rk}_{D_0}(A)},
   \]
   
   whose absolute value is σ(G).  A spanning cycle alternates between the
   two parts and therefore forces equal part sizes.  Consequently each of the
   17 reconstructed nonzero-signature cases is rigorously non-Hamiltonian;
   solver failure is not used.

4. For every one of the remaining 125 cases, the serialized cyclic list is an
   exact positive certificate.  It is enough to check that the list is
   repetition-free, equals the independently reconstructed full acyclic-mask
   set, and has Hamming distance one at every consecutive pair including the
   closing pair.  Those checks pass.  The sole two-entry witness is `A_`
   (​(K_2)​), and its entries differ on its unique edge, exactly as allowed by
   the convention frozen in `problem.md` and by the cited paper's literal cycle
   definition.

These four points prove both directions of the claimed equivalence and exhaust
every quantified graph.  They also show that the listed 17 cases are all and
only the negative cases, while no zero-signature counterexample exists in the
frozen domain.

## Independent checks actually performed

I wrote and ran `python3 audit/referee_check.py`.  This fresh checker imports
neither NetworkX nor OR-Tools and imports no candidate module.  It manually
decodes graph6, independently enumerates the connected labeled graph domain and
its permutation orbits, uses a DFS directed-cycle test rather than the
candidate's Kahn/NetworkX checks, reconstructs every orientation and flip edge,
recomputes every signature, and checks every cycle directly from the edge
lists.  It reported:

```text
fresh referee replay PASS
domain_counts {2: 1, 3: 2, 4: 6, 5: 21, 6: 112}
connected_labelled {2: 1, 3: 4, 4: 38, 5: 728, 6: 26704}
sigma_zero {2: 1, 3: 2, 4: 5, 5: 18, 6: 99}
sigma_nonzero {4: 1, 5: 3, 6: 13}
totals {'orientations': 19716, 'flips': 52423}
positive {2: 1, 3: 2, 4: 5, 5: 18, 6: 99} cycle_vertices 17130
negative_graph6 C] DFw DLs D]{ E?~o E@vg E@vo EBj? EBjW EBjg EBz_ EBzw EB~o EJeg EJnW ELvg E]~o
atlas_sha256 1410c140c3954d6cb023c023a54e6f0d62b13c41c8f94d095fb8a7b3ba500a86
cycles_sha256 fb67d29884f8312d6f240a5caef2dd180fb32f5b43f52cd05d1ba16a89ef412a
```

I also checked the frozen SHA-256 values of every decisive input used here
against `audit/snapshot.json`.  In particular, the immutable `source.md`,
`problem.md`, `claim.json`, atlas, cycle witness, proof, verification programs
and reports, and cited PDF match their recorded digests.  I did not use the
owner checkpoint or any prior verdict or confidence statement.

I specifically attacked the boundary and quantifier issues.  There are no
empty orders or disconnected graphs in scope; loops and multiple edges are
excluded by construction; all orientation masks are finite exact integers;
there is no numerical approximation, limiting exchange, or division; closure
of every cyclic witness is checked; and no incomplete positive search is
converted into a negative result.  The (K_2) convention is explicit rather
than silently relying on a competing simple-cycle convention.

## Source comparison and contribution

The frozen primary PDF has the recorded SHA-256
`fc43647a3fd3beb1173645f93504570e546cb99edb531b62bee6319b0e6abaaf`.
Its Formulations 1--3 pose the broader classification, Definition 2.8 defines
the acyclic signature, and Lemma 2.9 gives exactly the parity obstruction used
above.  Appendix D says that it studies 22 graphs from a named-graph database;
Table 5 includes several unknown outcomes and is not a complete connected
atlas through six vertices.  Thus the candidate's complete 142-class atlas is
a concrete finite resolution beyond that cited table.  The contribution is
substantial enough for the frozen resolution scope: it includes exhaustive
domain data, 125 explicit spanning cycles, and exact parity certificates for
all remaining cases.  The bounded literature comparison is honest and makes
no unrestricted priority claim.

## Gaps and verdict

I found no mathematical or certificate gap in the exact frozen scope.  Every
positive case has a directly replayable witness and every negative case has a
proof independent of search infeasibility.  The classification answers the
immutable finite problem in full.  Therefore the mathematical verdict is
**accept**.

