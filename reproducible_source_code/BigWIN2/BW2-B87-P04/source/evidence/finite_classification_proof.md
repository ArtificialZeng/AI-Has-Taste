# Exact edge-subset proof dossier

Date: 2026-09-11  
Research job: `win-00087-p04-research-4d7b5b5d25ee`

## Claim proved by the finite computation

For the definitions and scope fixed in `source.md` and `problem.md`, the four
parts of the frozen classification all hold.  This is a computer-assisted
finite proof, not a structural theorem for larger graphs or arbitrary
matroids.  The complete exact certificate is
`evidence/subset_closure_census.json`; the generating and checking program is
`evidence/independent_subset_check.py`.

## Why the computation covers the stated domain

For each `n=1,...,5`, the program visits all
`2^(n choose 2)` edge masks.  It tests connectedness by union--find, then
canonicalizes every connected mask under all `n!` vertex permutations.  For
each canonical representative it also computes its automorphism count and
checks that the sum of orbit sizes equals the number of connected labeled
graphs.  The resulting audit is

```text
n   all labeled   connected labeled   classes   orbit-size sum
1       1                 1               1             1
2       2                 1               1             1
3       8                 4               2             4
4      64                38               6            38
5    1024               728              21           728
```

Thus the 31 rows are exactly all connected simple graph isomorphism classes in
the frozen range.  Relabeling vertices permutes edges, flats, and flat-basis
coordinates and intertwines every `L_e` and `D`; consequently the Hilbert
vectors are constant on these isomorphism classes.

## Why each row implements the frozen mathematics

For a graph with `m` edges, the checker visits all `2^m` edge subsets `A`.
Union--find determines the components of `(V,A)`, and the checker sets

```text
cl(A) = {uv in E : u and v have the same union--find root}.
```

This is exactly the closure in `problem.md`.  The fixed points are therefore
exactly the graphic flats, and `n` minus the number of roots is their matroid
rank.  The code additionally checks extensivity, idempotence, and rank
preservation of closure for every visited subset.  It finds covers by the
literal condition that no enumerated flat is strictly intermediate; on
adjacent rank layers it checks that this agrees with proper inclusion.

Starting with the unit vector at the top flat, suppose the stored exact row
basis spans `C_j` in rank layer `k`.  For every basis vector the checker applies
all edge operators and the radial operator.  Its matrix entries, for
`X lessdot Y`, are respectively

```text
1[e in Y-X],                 k * |Y-X| / (m-|X|),
```

and are zero otherwise.  These are precisely the frozen formulas because
`k=r(Y)` and `m-|X|=|E-X|`.  Exact Gaussian elimination over
`fractions.Fraction` then returns a basis of
`D C_j + sum_e L_e C_j = C_(j+1)`.  Induction over all rank layers proves that
the recorded basis sizes are the desired Hilbert coefficients.  Every sparse
rational echelon basis, every flat layer, and every coordinate ordering is
serialized in the JSON certificate.

The extension is computed afresh after adjoining a new vertex and a single
pendant edge.  That edge is a bridge and hence a coloop, so its cycle matroid
is `M(G) direct-sum U_(1,1)`.  No flat-product identity is assumed.

## Exact results

All 31 independently computed triples `(H,Hplus,Delta)` agree with the
supervisor-supplied partition-flat census (SHA-256
`151aad4a7e4ec0d3f7a2582e7ca604078b65b8cddb8375d7e5891f78328f14d0`).
There are no mismatches.  The seven and only seven nonzero rows are:

| complement type | edges of G | H | Hplus | Delta |
|---|---:|---|---|---|
| `P5` | 6 | `(1,6,11,6,1)` | `(1,7,19,19,7,1)` | `2q^2+2q^3` |
| `P4+P1` | 7 | `(1,7,13,7,1)` | `(1,8,22,22,8,1)` | `2q^2+2q^3` |
| `P3+P2` | 7 | `(1,8,15,7,1)` | `(1,9,25,24,8,1)` | `2q^2+2q^3` |
| `P3+2P1` | 8 | `(1,9,16,8,1)` | `(1,10,26,26,9,1)` | `q^2+2q^3` |
| `2P2+P1` | 8 | `(1,9,20,8,1)` | `(1,10,33,28,9,1)` | `4q^2` |
| `P2+3P1` | 9 | `(1,10,22,9,1)` | `(1,11,36,31,10,1)` | `4q^2` |
| `5P1` | 10 | `(1,11,25,10,1)` | `(1,12,40,35,11,1)` | `4q^2` |

Every row of order at most four has zero difference.  On five vertices, the
listed complement types are exactly all integer partitions of five realized
as disjoint unions of paths, so the nonzero condition is exactly that the
complement is a linear forest.

Among these types only `P5` has four complement edges, hence only `K5-P5` has
six graph edges; all other failures have at least seven.  It is unique up to
isomorphism because `P5` is.  The theta graph with endpoints `0,1` and paths

```text
0-1,   0-2-1,   0-3-4-1
```

has complement path `0-4-2-3-1`, proving the asserted
`K5-P5 = Theta(1,2,3)` identification.  The checker also tests this
isomorphism by exhaustive canonicalization.

As a source-level sanity check, the complete-graph row gives
`H=(1,11,25,10,1)`, agreeing with Sinclair's Example 3.2.

## Reproduction and hashes

The decisive run was

```text
python3 evidence/independent_subset_check.py \
  --reference /home/ailab/4math-open-problems/batches/inbox/bigWin-87-materials/04_radial/exact_census.json \
  --output evidence/subset_closure_census.json
```

It reported 31 classes, 0 mismatches, 7 nonzero cases, and one six-edge
failure.  An isolated-mode rerun with `PYTHONHASHSEED=739` produced an
identical certificate byte for byte.  Final hashes before handoff were

```text
1aa804077490ab32df467d8ff9848d0361d7101d9a00fa1ed6e44b2dbcf96d72  evidence/independent_subset_check.py
bdf7220c271156dc2a8526facab718bc6d24d982f5d10a54e4aa2db6f24834a3  evidence/subset_closure_census.json
d197b76f2478dc8bab3245b76621f36d9552d19c75502e0a19cfd41a7bd8077d  source.md
```

## Scope and gap list

Known mathematical gaps in the frozen finite argument: none.  Required fresh
referee review has not yet occurred, so this dossier is a proof candidate, not
an acceptance record.  The result says nothing about graphs on six or more
vertices, disconnected or nonsimple graphs, arbitrary matroids, or a general
formula for matroid operations.  The bounded literature search in
`literature/triage_sources.md` did not locate this classification, but that is
not a claim of novelty or priority.
