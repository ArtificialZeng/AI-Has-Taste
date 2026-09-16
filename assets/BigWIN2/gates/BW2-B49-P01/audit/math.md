# Fresh mathematical referee report

## Verdict

**Accept.** The frozen `resolution-paper` claim is correct in its full stated
scope. The exact 36-edge graph has 276 five-edge sets that raise its domination
number, those sets form the eight claimed orbits under the full 48-element
abstract automorphism group, the claimed representatives and stabilizers are
correct, and every post-deletion domination number is nine.

This report is bound to snapshot
`a1fca3e5a49575bed7d42baff4bd66546a7fb342e920d4d7d9c11aeaa474fd68`
and referee job `win-00049-p01-referee-2668a4fb5d64`.

## Frozen scope and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and each
file enumerated by the snapshot. I recomputed every enumerated SHA-256 value;
all matched. I also recomputed the canonical digest of the snapshot file map and
obtained the displayed digest. The immutable `source.md` retained SHA-256
`98806a13e69ebf1aca43c4dba43f65a04a6006fb72ed6b5d2aafd59302ec7b1e`.

The review used the separately written `audit/referee_verify.py`. It neither
imports nor executes the candidate verifier. It uses a different family-census
organization and a custom exhaustive automorphism backtracker rather than
NetworkX/VF2. Its reproducible summary is
`audit/referee-verification.json`.

## Reconstruction and exact checks

From the 36 displayed unordered pairs I independently checked simplicity,
connectedness, and degree three at all 24 vertices. A set of at most five
vertices cannot dominate because each closed neighborhood has size four.
Exhaustive integer-mask enumeration at sizes six, seven, and eight returned
respectively (0,0,1767) dominating sets. Thus \(\gamma(T)=8\), independently
agreeing with the primary source.

For a dominating eight-set \(D\) and \(x\notin D\), define

\[
 C(D,x)=\{xy\in E(T):y\in D\}.
\]

The set \(D\) fails to dominate after deleting \(F\) if and only if
\(C(D,x)\subseteq F\) for some \(x\notin D\). Vertices of \(D\) still dominate
themselves, while an outside vertex fails precisely when every edge from it to
\(D\) was deleted. This proves that the test covers all and only the possible
failures of every minimum dominating set.

The independent program indexed the 1-, 2-, and 3-edge bundles by bitsets of
the eight-sets they destroy, then iterated all
\(\binom{36}{5}=376{,}992\) five-edge subsets. Exactly 276 destroyed all 1,767
eight-sets, and their ordered edge tuples matched
`evidence/minimum-bondage-sets.txt` entry for entry. As a separate replay, for
each of the other 376,716 edge sets it directly checked an eight-set that still
dominates after deletion; for each accepted edge set it directly retested all
1,767 eight-sets and found none surviving. Hence there is neither an omitted
five-edge set nor a false member in the reported family.

I independently enumerated abstract graph automorphisms without a graph
library. The search exhausts all 24 possible images of vertex 0 and all six
bijections from its three neighbors to the neighbors of the image, then extends
each partial map by exhaustive adjacency- and distance-preserving backtracking.
Every automorphism occurs under one such seed, and the pruning conditions are
necessary invariants, so the enumeration is complete. It returned 48 distinct
edge-preserving permutations. The three frozen generators are among them and
their closure is exactly this 48-element set.

Acting with those 48 permutations on the independently recomputed 276-set
family gave eight disjoint exhaustive orbits. In the lexicographic convention
of `problem.md`, the representatives matched all eight frozen representatives.
The orbit sizes were

\[
 24,48,12,48,48,24,48,24,
\]

and the corresponding setwise stabilizer sizes were

\[
 2,1,4,1,1,2,1,2.
\]

Thus every row satisfies orbit size times stabilizer size \(=48\), and the orbit
sizes sum to 276. Direct inspection of every member also verified that it
contains the complete three-edge star at at least one vertex.

For every member of the 276-set family, absence of a dominating eight-set gives
\(\gamma(T-F)\geq9\). The eight recorded nine-vertex witnesses were independently
checked against the graph with exactly the representative's five edges removed,
so each representative has \(\gamma(T-F)\leq9\). Automorphism invariance carries
this equality through every orbit. Therefore \(\gamma(T-F)=9\) for all 276
members. For every nonmember a surviving eight-set and monotonicity under edge
deletion give \(\gamma(T-F)=8\).

## Source comparison and contribution

The frozen arXiv v1 PDF gives the identical 24-vertex, 36-edge graph, proves
\(\gamma(T)=8\) and \(b(T)=5\), enumerates 1,767 dominating eight-sets, checks
all 58,905 four-edge sets, and supplies the single witness
\(\{02,14,15,26,27\}\) with post-deletion domination number nine. Its theorem,
proof, reproducibility section, and included pseudocode do not count all
five-edge bondage sets or classify their automorphism orbits.

The candidate therefore supplies the exact full classification requested in
the immutable source and strictly extends the cited baseline rather than merely
rephrasing its one witness. The frozen literature screen reports that no
equivalent classification was found, while explicitly treating this only as a
limited negative search. The claim likewise disclaims literature-wide priority
and any general bondage theorem, so the remaining global priority uncertainty
does not overstate or invalidate the scoped mathematical contribution.

## Attacks and remaining gaps

I tested the full quantified family rather than a subgroup-reduced sample,
computed the full abstract automorphism group rather than assuming geometric
symmetry, checked the strict-increase condition on both members and nonmembers,
verified the canonical representatives and orbit-stabilizer identities, and
checked rather than assumed that the increase is exactly one. There are no
empty-domain, division, limiting, probabilistic, floating-point, or cited-lemma
hypotheses in the decisive finite argument.

No mathematical or frozen-scope gap remains. The bounded literature screen is
not proof of priority, but no such priority is claimed. Acceptance certifies the
frozen classification and its honestly bounded contribution, not journal
acceptance or literature-wide novelty.
