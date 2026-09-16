# Exact census certificate for the frozen target

## Claim

For the definition in `problem.md`, the least order is

`N = 60`,

and the complete classification at that order is the single divisor set

`D = {2,5}`.

This statement concerns only the frozen `(chi,omega)=(3,2)` target.  It does
not assert that order 60 is minimal among uniquely `k`-colorable integral
circulants with arbitrary `k>omega`.

## Finite domain and exclusion logic

At order `n`, the legal sets are all subsets of the sorted proper-divisor list,
so their number is `2^(tau(n)-1)`.  Consequently there are exactly 2,043 pairs
with `n<60` and 4,091 pairs with `n<=60`.  The programs visit `n` increasingly
and the masks `0,...,2^(tau(n)-1)-1` without a symmetry quotient.  As proved in
`problem.md`, different masks at fixed `n` define different labeled graphs.

For every graph the primary program applies the following exhaustive decision
tree.

1. An edgeless graph cannot have chromatic number 3.
2. A disconnected graph cannot be uniquely 3-colorable.  Indeed, if no
   component has chromatic number 3 then the whole graph is at most
   2-colorable; otherwise a 3-chromatic component uses all three colors and a
   nontrivial color permutation on another component changes the global color
   partition while the 3-chromatic component pins the three global classes.
3. A displayed triangle implies `omega>=3`.
4. A displayed bipartition implies `chi<=2`.
5. In the remaining case the graph is connected, has an edge, is
   triangle-free, and has a displayed odd cycle.  Thus `omega=2` and `chi>=3`.
   Exact exhaustive 3-color search then gives one of: no coloring (`chi>3`),
   two distinct unordered color partitions (not unique), or exactly one
   partition (qualifying).

The primary enumerator represents adjacency rows as arbitrary-precision
integer bit sets.  Its 3-color routine chooses a vertex by DSATUR, breaking all
ties by degree and vertex label, and permits colors only in order of first
introduction.  Vertex choice depends only on the equality pattern of colors,
not their names.  Hence every unordered proper 3-color partition occurs in
exactly one search branch.  The search is complete unless it has already found
two partitions, which is sufficient for the nonuniqueness exclusion.  It runs
to exhaustion for a reported unique partition or absence of a 3-coloring.

Each JSONL record contains the exact domain pair, edge count, SHA-256 digest of
all adjacency rows, and one checkable witness when applicable: components, a
triangle, a bipartition, an odd cycle, two proper color partitions, or the
unique partition.

## Independent replay

`verify_census_sat.py` is a separate implementation.  It constructs the Cayley
graph from allowed difference residues into ordinary Python neighbor sets,
uses union-find for connectivity, set intersections for triangles, and parity
propagation for bipartiteness.  For every connected, triangle-free,
nonbipartite survivor it builds the standard 3-color CNF:

- each vertex receives at least one and at most one of three colors;
- adjacent vertices cannot share a color; and
- vertex 0 is fixed to color 0, which loses no unordered partition.

Its DPLL solver performs exhaustive unit propagation and binary branching.  If
a first model is found, the verifier blocks both labeled models that encode its
same unordered partition (the two swaps of colors 1 and 2 compatible with
`c(0)=0`) and solves again.  Unsatisfiability of the blocked formula is exactly
uniqueness of the unordered partition; a new model is exactly a second
partition.  This verifier also reconstructs every primary graph independently
and validates every primary witness and adjacency digest.

The independent run checked all 4,091 pairs, agreed on every classification,
and reported no witness error.  The aggregate counts through order 60 are:

| exclusion/result | count |
|---|---:|
| edgeless | 60 |
| disconnected | 677 |
| triangle | 3,228 |
| bipartite | 91 |
| not 3-colorable | 17 |
| nonunique 3-colorable | 17 |
| qualifies | 1 |

Below order 60 the corresponding total is 2,043, with no qualifier.  At order
60 the only qualifier is `{2,5}`.  Its unique partition is the three residue
classes modulo 3, and the primary certificate includes the odd 5-cycle

`4, 2, 0, 14, 9, 4`.

Thus this graph has `chi=3` and `omega=2`, all orders below it are excluded,
and no other divisor set qualifies at order 60.

## Reproduction

From the project root, using Python 3 with only the standard library:

```sh
python3 evidence/enumerate_icg.py \
  --records evidence/census-primary.jsonl \
  --summary evidence/census-primary-summary.json
python3 evidence/verify_census_sat.py \
  --primary evidence/census-primary.jsonl \
  --records evidence/census-independent.jsonl \
  --audit evidence/census-audit.json
```

Two immediate clean replays reproduced the record files byte for byte.  The
decisive digests are:

- `census-primary.jsonl`:
  `2e07ea9bb95406bbe504b7bad544db66f060e3989a5899bb16a56872408a524c`;
- `census-independent.jsonl`:
  `a6eab70b7dba7b16d4e277c381c3ea1701862a44f95c0d9490430fb0e5a9408a`;
- copied primary-source PDF:
  `eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2`.

## Evidence status and gap list

The theorem above is an exact finite computational result, not floating-point
evidence.  The local primary-source PDF establishes the previously known
order-60 family and provides the literature comparison; the census supplies
the new finite minimum and classification.  No mathematical gap is presently
known in the stated frozen scope.  Priority beyond the bounded literature
comparison in `problem.md` is not claimed and remains for citation review.
