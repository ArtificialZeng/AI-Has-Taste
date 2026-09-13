# Independent audit of the ten-vertex tree-core theorem

## Verdict

```text
PASS
fatal defects: 0
major defects: 0
minor defects: 0
```

The audited conclusion is deliberately structural, not global: every reduced
graph of adjacency rank ten that contains a nonsingular induced ten-vertex
**tree** has at most 62 vertices.  The audit does not infer that every
connected rank-ten graph has such a tree core.

## Frozen objects

```text
work/builder/tree_core_exact_search.json
SHA-256 1bdc9e089030ae02b67042e437fcb5cc9249cd841aeb85fac4cfc4858d4072d4

src/linear_verify_tree_core_family.py
SHA-256 74b88115c292328d5509cf713a17e0213063b0e56f2532f369b5834d4272fd1b

work/linear_extension/tree_core_family_audit.json
SHA-256 f7ccf3e4d5a9500ea6f7c479f78b5a630b8b2ccce2bd47ac92db32eb6d91dbc8

proof/tree_core_theorem.md
SHA-256 33ac44f26b13746ada69af42df1579e27e0e207202e9087f5c5ba4b2d7d7ecb7
```

The verifier rejects a wrong source hash before reading the source JSON or
writing an output.  The bad-hash attack was run and the requested output file
was absent afterwards.

## Definition-level reconstruction

The verifier imports no discovery code.  Its independent reconstruction was
audited as follows.

1. It starts from the one-vertex tree, attaches a new leaf at every vertex of
   every representative, and deduplicates by a separately implemented
   centre-rooted AHU encoding.  Completeness follows inductively because
   deleting a leaf from any tree of order `n` gives a tree of order `n-1`.
   The resulting free-tree counts are

   ```text
   1,1,1,2,3,6,11,23,47,106,
   ```

   and rooting every free representative at every vertex gives

   ```text
   1,1,2,4,9,20,48,115,286,719.
   ```

   These are the standard free- and rooted-tree counts through order ten.
   The verifier parses the 106 frozen source edge lists, checks nine distinct
   edges and connectedness, computes its own canonical code, and verifies
   equality of the complete 106-element isomorphism sets.  It does not trust
   source indices, source AHU strings, or graph6 strings for completeness.

2. Every determinant is recomputed by fraction-free Bareiss elimination.
   Perfect matchings are counted by an independent exact recursion, and all
   106 trees satisfy

   ```text
   det A(T) = -(number of perfect matchings of T)^2.
   ```

   Hence exactly 15 cores are nonsingular, each has determinant `-1` and a
   unique perfect matching; the other 91 are singular.

3. For each nonsingular core `B`, the verifier recomputes every cofactor of
   `adj(B)` and checks both multiplication identities

   ```text
   B adj(B) = det(B) I = adj(B) B.
   ```

   It then enumerates all 1,023 nonzero binary profiles, retains precisely
   those with zero exact quadratic form, identifies and removes the ten core
   columns, and rebuilds every compatibility edge from the integer numerator

   ```text
   v' adj(B) w in {0, det(B)}.
   ```

   Profile counts range from 269 to 382 after removing the core columns, and
   compatibility-edge counts range from 21,809 to 45,042.  Both ranges and
   every per-core value are serialized in the audit JSON.

4. Before the 15 large searches, the target-clique engine is compared with
   literal `2^n` subset enumeration on every labelled graph through order
   five and on 100 deterministic random graphs at each order six through
   nine.  Every target size is checked.  All 1,500 graph tests pass.

5. The large searches use an independently generated tree labelling and an
   additional nonzero cyclic relabelling of each compatibility graph.  Thus
   their branch order is not the discovery transcript.  The colouring step
   partitions the current candidate graph into independent sets, so its
   colour number is an exact upper bound on the size of any continuation;
   only branches below that certified bound are pruned.  The 15 searches make
   760,220 recursive calls and independently return `false` for a target
   clique of size 53 in every nonsingular tree core.

All algebraic and branching decisions use integers.  No numerical eigenvalue
or floating-point spectrum is used as proof.

## Audit of the theorem bridge

Let the adjacency matrix be partitioned around a nonsingular induced
ten-vertex core as

```text
A = [ B  C ]
    [ C' D ].
```

Since `rank(A)=rank(B)=10`, the Schur complement is exactly zero:

```text
D = C' B^{-1} C.
```

Writing `v_u` for the binary core profile of any vertex, including a core
vertex, gives `A_uv=v_u'B^{-1}v_v`.  This proves each required bridge:

- a zero profile gives an all-zero adjacency row and hence an isolated
  vertex;
- equal profiles give equal full adjacency rows and hence equal open
  neighbourhoods;
- reducedness therefore makes all represented profiles nonzero and pairwise
  distinct;
- the profile of core vertex `i` is `b_i=B e_i`, and
  `b_i'B^{-1}v=e_i'v=v_i`, so every core column is compatible with every
  binary profile;
- all vertices outside the core consequently form a clique in the noncore
  compatibility graph.

If `|V(G)|>=63`, there are at least `63-10=53` outside vertices and therefore
a forbidden 53-profile noncore clique.  The exact searches exclude this for
all 15 possible nonsingular ten-vertex tree cores, proving `|V(G)|<=62` in
the stated class.

## Scope and remaining gap

The tree-core hypothesis is essential to the present certificate.  The
separate Wang--Guo result may be cited to obtain a connected nonsingular
induced core of order ten in a connected rank-ten graph, but it does not say
that this core is a tree.  Cores containing cycles are not audited here.
Accordingly this result is a rigorous nontrivial structure-class theorem and
an exact computational certificate, not a solution of the full reduced-graph
rank-ten conjecture.
