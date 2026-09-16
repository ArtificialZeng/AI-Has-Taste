# Fresh mathematical referee report

## Frozen scope and evidence integrity

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
finite simple graph (G), every (K\subseteq V(G)), every (n\geq |K|), and
every (i\geq0), the group (H_i(\Sigma(G,K,n);\mathbb Z)) is free abelian.
This is stronger than, and therefore would disprove, the frozen existential
assertion for cographs without changing its meaning.

All hashes in `audit/snapshot.json` were recomputed and agree with the current
files.  I also recomputed the snapshot's canonical mapping digest; it is
`1cbfb3e8b6067c7adb8ebefab8352dc54203e27db8fad03a3b3f7b00393c8a2c`.
The immutable `source.md` remained at SHA-256
`ad9eb559516e39382c1707dbcfbc8867593184e4524ebfeaebc43f84edf1ff79`.
Direct extraction of pp. 26--28 of the frozen arXiv PDF confirms that
Definition 4.13 is exactly the labelled-coordinate, collisions-allowed space
used by the proof, and that the source states the integral-torsion question as
open while recording anchored trees and cycles as torsion-free.

## Reconstruction of the decisive argument

Assume first that (G) is connected and (r=|K|\geq1).  For every injection
(f:K\hookrightarrow[n]), let (U_f) fix coordinate (f(k)) at (k) for
each anchor (k).  These subcomplexes cover (\Sigma(G,K,n)): a cell in the
anchored space contains every anchor as a vertex factor, so one can choose a
distinct occurrence for each anchor.  A finite intersection is empty exactly
when two requirements put distinct anchors in one coordinate.  Otherwise, if
(S) is the set of constrained coordinates, the intersection is canonically
(G^{[n]\setminus S}).

The cellular Cech double complex of this finite cover resolves the cellular
chains of the union.  This does not require an open-cover nerve lemma: after
fixing a product cell (c), its horizontal augmented summands are precisely
the augmented simplex on the nonempty set of indices (f) for which
(c\subseteq U_f), hence are exact.  This verifies the augmentation
cell-by-cell and also covers repeated or redundant requirements in an
intersection.

Choose a spanning tree of (G), and let the chords be indexed by a basis of
(L=H_1(G;\mathbb Z)).  The chain map

\[
C_*(G;\mathbb Z)\longrightarrow
H:=\mathbb Z[0]\oplus L[1]
\]

sends every vertex to the same generator, every tree edge to zero, and each
chord to its corresponding basis element.  It is a chain map because both
endpoints of every edge have the same degree-zero image.  On (H_0) it is the
augmentation isomorphism; on (H_1), taking chord coefficients identifies the
fundamental-cycle basis with the chosen basis of (L).  Thus it is an
integral quasi-isomorphism, not merely a field-level replacement.

Tensoring this map over the free coordinates gives a quasi-isomorphism on
every nonempty cover intersection.  The crucial compatibility is strict:
when an intersection inclusion makes a constrained coordinate free, it
inserts an anchor vertex, and every anchor vertex maps to the same degree-zero
unit.  Hence these maps form a map of the complete Cech double complexes.
Both complexes are finite and consist of free abelian groups, so the vertical
filtration proves a quasi-isomorphism on total complexes.

After this replacement the vertical differential is zero.  Splitting each
tensor factor as (\mathbb Z\oplus L[1]), fix the subset (J\subseteq[n]) of
coordinates carrying (L).  Such a summand occurs exactly for compatible
collections of anchor injections whose images avoid (J).  Its horizontal
complex is therefore the simplicial chain complex of the compatibility nerve
(N_{r,n-|J|}), shifted by (|J|), and it is absent when
(|J|>n-r).  This reconstructs the asserted additive decomposition

\[
H_i(\Sigma(G,K,n);\mathbb Z)\cong
\bigoplus_{\substack{J\subseteq[n]\\|J|\le n-r}}
L^{\otimes |J|}\otimes
H_{i-|J|}(N_{r,n-|J|};\mathbb Z).
\]

To check the remaining input, take any tree containing (r) distinguished
vertices and use the same injection cover.  Every compatible intersection is
a product of trees and is contractible; incompatible intersections are empty.
The same cellwise Cech argument identifies the integral homology of its
anchored space with that of (N_{r,m}).  The frozen primary-source PDF
explicitly records torsion-freeness for anchored spaces of trees, and the
evidence identifies the corresponding arbitrary-anchor result as Kozlov,
Definition 2.4 and Theorem 2.5.  Thus every (H_*(N_{r,m};\mathbb Z)) is free.
For (r=1) this can also be seen immediately because the nerve is a simplex.
For (r=0), the space is (G^n), whose homology is free by the integral
Kunneth theorem.  Since (L) is free, every summand above is free.

For disconnected (G=\bigsqcup_aG_a), (G^n) splits as a finite disjoint
union indexed by coordinate-to-component assignments.  The nonempty anchored
part of each piece is, after reordering labelled coordinates,
(\prod_a\Sigma(G_a,K_a,|I_a|)).  The connected case and integral Kunneth
give free homology for every piece, and a finite direct sum preserves
freeness.  The empty graph and zero-coordinate conventions are handled
separately in the proof and also yield only free groups.

## Adversarial checks performed

I checked the injection-cover quantifiers, conflicting versus redundant
coordinate requirements, the direction of every intersection inclusion, the
degree shift in the fixed-(J) splitting, and the cases (K=\varnothing),
(n=|K|), (n=0), disconnected graphs, isolated vertices, and the empty
graph.  None produces a missing summand or changes the conclusion.  No
limiting argument, division, compactness claim, or field-to-integral inference
is used.

As corroboration rather than proof, I reran the independent implementation.
It again passed all boundary-square, cell-count, and predicted-rank checks for
all 167 connected-labelled-graph/one-anchor cases and all 241 two-anchor
cases stated in the evidence, over (\mathbb F_2,\mathbb F_3,\mathbb F_5).
I also reran the exact Smith calculation for
((K_4,\{0,1\},4)): its (323\times432) cycle-coordinate matrix has 311
nonzero invariant factors, all equal to 1, and Betti ranks
((1,12,121)), matching the decomposition.

The finite computations are not used to promote a bounded census to a
universal theorem.  The bounded literature screen supports the source
comparison but does not certify priority; any manuscript should preserve that
limitation and cite the exact primary Kozlov result.  This is a publication
and attribution caution, not an unresolved mathematical gap in the frozen
claim.

## Verdict

**ACCEPT.**  The chain-level argument settles the frozen original assertion in
its full scope (indeed for all finite simple graphs), its decisive integral
steps are valid, the edge cases are covered, and the contribution is a
substantive resolution rather than a finite negative census or a scope
downgrade.
