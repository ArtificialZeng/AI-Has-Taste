# Proof dependency graph

## E0: exact rank-10 baseline

- `src/build_standard_extremal.py` constructs the order sequence
  \(2,6,14,30,62\) by four applications of Construction (a) from \(K_2\).
- `certificates/standard_rank10_order62.json` contains the full labelled
  adjacency matrix.
- `src/exact_graph_verifier.py` checks binary symmetry, zero diagonal,
  nonzero and pairwise-distinct rows, the nonzero principal minor on indices
  `[0,1,2,4,6,12,14,28,30,60]` with determinant \(-1\), and all 3,844
  entries of \(A=X^{\mathsf T}B^{-1}X\). Hence its rank is exactly 10.
- This is an order-62 equality example, not a counterexample.

## E1: exact one-vertex maximality test for the standard family

- `src/build_rank10_extremal_family.py` constructs the five standard
  operation words `aaaa`, `caaa`, `ccaa`, `ccca`, and `cccc` from \(K_2\).
- Every member passes the exact principal-core verifier at order 62 and rank
  10.
- For each fixed member, `src/root_one_vertex_extensions.py` enumerates all
  \(2^{10}=1024\) binary core columns \(v\). A rank-preserving new vertex
  must satisfy exactly
  \(v^{\mathsf T}B^{-1}v=0\) and
  \(X^{\mathsf T}B^{-1}v\in\{0,1\}^{62}\).
- In all five cases, the only binary candidates that survive are the 62
  existing core columns plus the zero column; therefore no fixed member has a
  reduced rank-preserving one-vertex extension.
- Scope: this does **not** exclude a different 63-vertex rank-10 graph.

## R1: connected full-rank-core reduction

- For a disconnected reduced rank-10 graph, the component adjacency ranks
  are integers at least two and sum to ten.
- Applying the externally known rank-at-most-nine order bounds to all eleven
  partitions of ten gives order at most 32; see
  `proof/connected_reduction.md`.
- Hence every order-at-least-63 counterexample is connected.
- The external Wang--Guo theorem then supplies a connected nonsingular
  induced ten-vertex subgraph.  Thus the remaining global search may be
  restricted to connected nonsingular ten-vertex principal cores.
- This node depends on published small-rank bounds and the Wang--Guo theorem;
  those inputs are not new results of this project.

## E2: induced-matching-core theorem (known structural class)

- `proof/induced_matching_core_theorem.md` proves that a reduced rank-`2m`
  graph containing an induced `mK2` has order at most `2^(m+1)-2`, with
  Construction (a) attaining equality.
- `work/linear_extension/induced_matching_theorem_audit.md` independently
  reports `0 fatal / 0 major / 0 minor`.
- At rank ten this closes the induced-`5K2` class, but this is an independent
  reconstruction of the known Haemers--Peeters theorem, not a novelty claim.

## E3: radius-one theorem around the starlike core

- Let `T_*=S(1,2,2,2,2)` be the nonsingular ten-vertex tree core in E0.
- The distance-zero case is closed by the exact fixed-core clique theorem.
- `work/builder/core_single_toggle_exact.json` enumerates all 45 one-edge
  toggles.  Nine are singular.  For each of the other 36, the independent
  no-import integer verifier reconstructs every profile and compatibility
  edge and exactly excludes a clique of 53 noncore profiles.
- Therefore any reduced rank-10 graph containing a nonsingular induced core
  at edge distance at most one from `T_*` has order at most 62; see
  `proof/single_toggle_radius_one_theorem.md`.
- The frozen family audit is
  `work/linear_extension/single_toggle_family_audit.json`, SHA-256
  `b3363fa92066919e128582842daf1ddda8f89596e663aeb59bcf58d22028e39b`.
- Scope: R1 guarantees some connected nonsingular ten-vertex core, but does
  not guarantee that it lies in this radius-one family.

## E4: all nonsingular ten-vertex tree cores

- Canonical leaf extension, cross-checked by rooted-tree multiset generation,
  enumerates all 106 nonisomorphic ten-vertex trees.
- Exactly 15 have nonsingular adjacency matrix; every determinant is `-1`.
- For every one of those 15 cores, all 1,023 nonzero binary profiles and all
  compatibility edges are rebuilt with integer arithmetic, and an exact
  target search excludes a clique of 53 noncore profiles.
- The source replay verifies all 882,626 deterministic branch nodes.  A
  separately implemented no-import engine changes the tree representatives,
  cyclically relabels the compatibility graphs, and independently excludes
  the targets in 760,220 calls after 1,500 brute-force small-graph tests.
- Four corrupted inputs fail closed.  Therefore every reduced rank-10 graph
  containing a nonsingular induced ten-vertex tree core has order at most 62;
  the standard 62-vertex graph shows sharpness in this class.
- Canonical theorem source: `proof/tree_core_theorem.md`.  Frozen discovery:
  `work/builder/tree_core_exact_search.json`, SHA-256
  `1bdc9e089030ae02b67042e437fcb5cc9249cd841aeb85fac4cfc4858d4072d4`.
- Scope: R1 guarantees a connected nonsingular core, not necessarily a tree;
  cyclic and denser connected cores remain open.

## E5: all nonsingular connected unicyclic and bicyclic ten-vertex cores

- Two complete canonical routes enumerate 657 connected unicyclic cores;
  exactly 136 are nonsingular and all exclude a 53-clique of noncore profiles
  under independent integer audits.
- Two further complete routes enumerate 2,678 connected bicyclic cores:
  345 dumbbells, 514 figure-eights and 1,819 theta types.  Exactly 719 are
  nonsingular, and all exclude target 53 under both the discovery engine and
  a separately written no-import generator, adjugate reconstruction and
  relabelled target search.
- Five corrupted bicyclic sources fail closed.  A certified reduced rank-ten
  graph of order 62 contains a nonsingular bicyclic ten-core, so the class
  bound is sharp.
- Canonical theorem source: `proof/bicyclic_core_theorem.md`.  Frozen source:
  `work/builder/bicyclic_core_exact_search.json`, SHA-256
  `286465529d9e1b65716790ac01e87b68f8a7593a5dadd3a415c247bc2f74c3df`.
- Scope: combining E4 and E5 closes connected nonsingular full-rank cores
  with at most eleven edges.  Cores with twelve or more edges remain open.

## Open dependencies

- D01 must find a connected nonsingular ten-vertex core with at least twelve
  edges whose compatibility graph has a clique of at least 53 noncore
  profiles, or prove an upper bound for a broader complete core class.
- P01 remains open globally: E4--E5 close tree, unicyclic and bicyclic cores,
  not every connected nonsingular ten-vertex core.
- A01 is closed through the bicyclic layer by independent integer-adjugate
  reconstruction, exact clique replay, changed-order audits, small-graph
  brute-force comparisons, and fail-closed checks.
