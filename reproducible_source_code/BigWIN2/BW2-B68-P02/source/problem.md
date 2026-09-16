# Precise problem statement

## Frozen input and mathematical universe

The immutable statement is `source.md` (SHA-256
`6ce58a7ef27abff3de2371ca219430179879b43f26e8da5e94927a140aa70a75` at
triage). No correction or weakening is proposed.

All graphs below are finite, simple, undirected, connected, and considered up
to isomorphism. A graph is *cubic* when every vertex has degree 3. Thus an
eligible order `n=|V(G)|<20` is even, and simplicity and cubicity force
`n in {4,6,8,10,12,14,16,18}`. Such a graph has `3n/2` edges and `5n/2`
elements in `V(G) union E(G)`.

A proper 4-total coloring is a function

`phi: V(G) union E(G) -> {1,2,3,4}`

such that (i) adjacent vertices, (ii) edges sharing an endpoint, and (iii) an
edge and either endpoint have different colors. Write

* `A(G)` for “there exists a proper 4-total coloring of `G`”; and
* `E(G)` for “there exists such a coloring whose four color-class cardinalities
  differ pairwise by at most 1.”

Since every cubic graph has total chromatic number at least 4, `G` is Type 1
exactly when `A(G)` holds. The frozen claim is therefore the finite sentence

`for every eligible isomorphism class G, A(G) implies E(G)`.

Equivalently, the counterexample search asks whether any eligible `G` satisfies
`A(G) and not E(G)`. Both `A` and `E` are existential coloring assertions; in
particular, the claim does **not** say that every proper 4-total coloring is
equitable.

## Exact equitable bounds

Put `T=5n/2`, `q=floor(T/4)`, and `r=T-4q`. Equitability is equivalent to
exactly `r` color classes having size `q+1` and the other `4-r` having size
`q`. The required multisets are:

| `n` | `T` | equitable color-class sizes |
|---:|---:|:---|
| 4 | 10 | `(3,3,2,2)` |
| 6 | 15 | `(4,4,4,3)` |
| 8 | 20 | `(5,5,5,5)` |
| 10 | 25 | `(7,6,6,6)` |
| 12 | 30 | `(8,8,7,7)` |
| 14 | 35 | `(9,9,9,8)` |
| 16 | 40 | `(10,10,10,10)` |
| 18 | 45 | `(12,11,11,11)` |

The cited paper's Lemma 3.1 gives a useful equivalent representation. If `S_i`
is the set of vertices of color `i` and `M_i` the set of edges of color `i`,
then the `S_i` partition `V(G)` into independent sets, the `M_i` partition
`E(G)`, and `M_i` is a perfect matching of `G-S_i`. Moreover `|S_i|` is even
and the total color-class size is `(n+|S_i|)/2`. Hence an equitable coloring
has vertex-profile multiset, in the same order table,
`(2,2,0,0)`, `(2,2,2,0)`, `(2,2,2,2)`, `(4,2,2,2)`,
`(4,4,2,2)`, `(4,4,4,2)`, `(4,4,4,4)`, or `(6,4,4,4)`.
This equivalence is a possible independent encoding/check, not a relaxation.

## Scope of a resolution

The census must contain one canonical graph6 representative of every eligible
isomorphism class. The authoritative counts to reproduce are

| `n` | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| classes | 1 | 2 | 5 | 19 | 85 | 509 | 4,060 | 41,301 | 45,982 |

For a positive resolution, each graph must carry either a directly checked
equitable coloring (witnessing `E(G)`) or a replayed UNSAT proof for `A(G)`
(showing the antecedent false). For a negative resolution, every least-order
counterexample must carry a proper 4-total coloring and a replayed UNSAT proof
for `E(G)`. Enumeration completeness, graph properties, graph6 decoding,
canonicalization/no duplicates, CNFs, solver/verifier versions, commands,
seeds, ordering, and hashes are part of the required evidence. SAT/solver exit
codes alone do not resolve either assertion.

The order-20 reformulation is used exactly as in Question 7.1: the cited prior
work states that its graph `R` is Type 1 with equitable total chromatic number
5, and cubic graphs have equitable total chromatic number at most 5. Under
those cited facts, the frozen claim is equivalent to `R` having minimum order
among Type 1 cubic graphs with equitable total chromatic number 5. The project
does not assert anything at orders 20 or higher, nor does it resolve the
stronger already-disproved statement that every 4-total coloring below order
20 is equitable.

## Prior result and proposed contribution

Nearest prior result: Adauto, de Figueiredo, Sasaki, and Schneider,
arXiv:2609.05259v1 (submitted 2026-09-04), Question 7.1 on PDF page 13, asks
the frozen assertion and proposes a systematic catalogue computation via
integer programming or SAT. Its Lemma 3.1 and Corollary 3.2 give the structural
encoding above; Theorem 4.1 proves the stronger every-coloring property at
orders 6, 8, 10, and 14; Section 7 states that the displayed order-12, -16,
and -18 non-equitable examples also have equitable colorings. As inspected on
2026-09-07, this source presents Question 7.1 as unresolved, not as a theorem.

Proposed delta: resolve that exact finite question with a complete canonical
census and independently replayable positive/UNSAT certificates. Verification
route: reproduce the census by a documented isomorph-free generator and an
independent count, encode `A(G)` and `E(G)` with derived cardinality bounds,
directly verify all witnesses, replay proof-producing UNSAT cases against the
hashed CNFs, and audit coverage by joining result rows to the canonical census.

