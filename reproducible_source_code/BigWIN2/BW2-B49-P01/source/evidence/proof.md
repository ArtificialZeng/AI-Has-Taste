# Exhaustive classification certificate

Provenance: `win-00049-p01-research-4e797619dfe8` (research pass 1,
2026-09-07).  This document records a computational proof for the exact
labeled graph and conventions in `problem.md`.  The executable certificate is
`evidence/verify_classification.py`; its deterministic output is
`evidence/classification.json` and its complete 276-line family listing is
`evidence/minimum-bondage-sets.txt`.

## Result

For the graph (T) in `problem.md`,

\[
 |\mathcal M(T)|=276.
\]

The full abstract automorphism group has order 48, and the 276 sets form the
following eight orbits.  Edges within each representative are in lexicographic
order, as required by the canonical convention in `problem.md`.

| canonical representative | orbit size | stabilizer size | \(\gamma(T-F)\) |
|---|---:|---:|---:|
| (0,1), (0,2), (0,3), (1,4), (1,5) | 24 | 2 | 9 |
| (0,1), (0,2), (0,3), (1,4), (4,9) | 48 | 1 | 9 |
| (0,1), (0,2), (0,3), (2,6), (2,7) | 12 | 4 | 9 |
| (0,1), (0,2), (0,3), (2,6), (8,14) | 48 | 1 | 9 |
| (0,1), (0,2), (0,3), (5,10), (5,11) | 48 | 1 | 9 |
| (0,1), (0,2), (0,3), (5,10), (8,14) | 24 | 2 | 9 |
| (0,1), (0,2), (0,3), (6,11), (6,12) | 48 | 1 | 9 |
| (0,1), (0,2), (0,3), (6,11), (7,13) | 24 | 2 | 9 |

Thus every minimum bondage set contains the three-edge star at some vertex;
the table gives all possibilities for the other two edges up to the full
abstract automorphism group.  The orbit sizes sum to 276.

## Why the finite test proves the result

The script first checks directly from the displayed 36-edge list that (T) is
simple, connected, and 3-regular on 24 vertices.  It enumerates every vertex
subset of each size from 0 through 8, using 24-bit closed-neighborhood masks.
The counts of dominating sets at these sizes are

\[
 (0,0,0,0,0,0,0,0,1767).
\]

In particular this independently proves (gamma(T)=8) and reproduces the
primary source's count of 1,767 dominating eight-sets.

For such an eight-set (D) and a vertex (x\notin D), put

\[
 B(D,x)=\{xy\in E(T):y\in D\}.
\]

Because (D) dominates (T), each bundle (B(D,x)) is nonempty.  After a set
(F) of edges is deleted, (D) fails to dominate exactly when some outside
vertex (x) loses all of its edges to (D), equivalently
(B(D,x)\subseteq F) for some (x\notin D).  Consequently (F) raises the
domination number exactly when this bundle-containment condition holds for
every one of the 1,767 dominating eight-sets.  This equivalence loses no
possible eight-set: any set dominating the subgraph (T-F) also dominates its
supergraph (T).

The script constructs all \(\binom{36}{5}=376{,}992\) five-edge masks, filters
them by that exact condition for all 1,767 eight-sets, and then replays every
accepted mask against the un-reordered list of eight-sets.  Exactly 276 masks
remain.  The family file lists every one, in deterministic lexicographic order;
its SHA-256 is
`022713d0503d082917dd27f6c445a9db7cb016afbdc5ce4e8a098fe387e47be8`.
The published witness \(\{02,14,15,26,27\}\) is also checked to occur in this
family.

The script next uses NetworkX 3.4.2's exact VF2 graph-isomorphism enumeration
on the same adjacency relation.  It obtains 48 distinct vertex permutations.
For every returned permutation it independently checks bijectivity and equality
of the complete image edge set with (E(T)).  A greedy closure calculation
extracts the three displayed permutation generators in
`evidence/classification.json` and verifies that they generate all 48 returned
permutations.  The induced action on the 36 labeled edges is then applied to
all 276 masks.  Each orbit stays inside the accepted family, the orbit union is
disjoint and exhaustive, each displayed representative is the lexicographically
least member of its orbit, and every row satisfies

\[
 |\operatorname{Orb}(F)|\,|\operatorname{Stab}(F)|=48.
\]

Finally, absence of a dominating eight-set gives
(gamma(T-F)\geq 9) for every accepted (F).  For each orbit representative,
the script searches nine-vertex subsets in lexicographic order and records an
explicit dominating nine-set in `evidence/classification.json`.  It rechecks
each witness after precisely the representative's five edges are deleted.
This gives the opposite bound, so every table entry has
(gamma(T-F)=9); automorphism invariance gives the same value throughout its
orbit.

All decisive domination, bundle, group-action, orbit, stabilizer, and witness
tests use exact integers and finite iteration.  There is no floating-point,
random, heuristic acceptance, or untested symmetry reduction.  Sorting the
bundle families changes only the order in which impossible five-edge masks are
discarded, not the quantified domain.

## Scope and remaining audit

This settles the finite classification stated in `source.md` and `problem.md`,
conditional only on ordinary execution semantics and the completeness of the
exact isomorphism iterator used for the 24-vertex graph.  The copied primary
source `evidence/external/2609.02477.pdf` establishes the nearest published
baseline and contains no all-five-set orbit classification.  The literature
screen was limited, so this proof does not assert literature-wide priority.
The next required step is a fresh mathematical referee pass that independently
recomputes the 276-set family and the full automorphism orbits, preferably with
a separately implemented automorphism routine.
