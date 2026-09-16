# Frozen source — win-00040-p02

## Source

Rafael S. González D'León and Michelle L. Wachs, *Weighted bond posets and a new chromatic symmetric function*, arXiv:2608.08692v1 (2026), Section 7.2 and Conjecture 7.3.
Primary text: https://arxiv.org/html/2608.08692v1

## Immutable problem statement

Let `Psi_G(x)` be the symmetric-function analogue of the chromatic polynomial defined from the multiweighted bond posets in the cited paper. For every connected simple graph `G` on exactly eight vertices and every `d>=1`, determine whether

`(Psi_G|degree d)^2 - (Psi_G|degree d-1)(Psi_G|degree d+1)`

is Schur-positive. Equivalently, decide the complete eight-vertex layer of Conjecture 7.3. A disproof must give an explicit graph, degree, partition, and negative exact Schur coefficient; a positive result must cover every isomorphism class by an independently replayable exact computation or proof.

The source reports computational verification only for connected graphs with at most seven vertices. Chordal cases and any cases already implied by source theorems must be separated from genuinely new computation.

