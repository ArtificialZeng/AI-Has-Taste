# Proof audit

Date: 2026-08-30 UTC

Scientific scope: the arbitrary-tree conjecture remains open.  The audit
passes the starlike partial theorem, the sharpness family, and the exact finite
verification through order 15.  The continuation audit additionally passes a
general hull-center deletion lemma and an exact refutation of its first local
iteration.

Status: PASS for those stated results.

## Frozen conventions

- Finite, simple, undirected trees; diameter is measured in edges.
- A resolving set is an ordinary subset, and representations are unordered
  integer multisets with multiplicity.
- The finiteness hypothesis is part of the conjecture.
- Equality of multisets is checked through shell-count vectors or literal
  sorting; these encodings are exactly equivalent.

## Main theorem reconstruction

1. **Capacity necessity.**  Two arms of length at most (r) with the same
   padded membership word make their depth-one vertices collide.  The argument
   remains valid when the arm lengths differ.
2. **Pattern feasibility.**  Ordering the arms and assigning the 1-bit
   positions of (i-1) is valid because capacity gives
   (l_i\ge\lceil\log_2i\rceil).
3. **Strict modular range.**  For
   (G_q(s)=\sum_{a\in S_q}\min(s,a)),
   (G_q(s)\le\sum_{a\in S_q}a\le q\le m-1<K_m).  The strict final
   inequality includes the (m=3) center adjustment.
4. **Depth recovery.**  Equal representations imply equal distance sums,
   hence (K_m(s-t)=2(G_q(s)-G_{q'}(t))).  Oddness of (K_m) and the strict
   range force equal depth; no converse use of distance sums occurs.
5. **Arm recovery.**  At fixed depth the correction polynomials
   (z^{|s-a|}-z^{s+a}) are linearly independent.  Choosing the largest
   active (a) gives an uncancellable term of degree (s+a), including when
   (a>s).
6. **Center.**  Equality with a noncentral vertex would force
   (K_ms=2G_q(s)), then (G_q(s)=0) and (s=0), impossible.
7. **Budget arithmetic.**  The block-sum identity and initial-binary-word
   popcount bound were recomputed.  Power-of-two boundaries and
   (m=5,6,7,8) are handled explicitly.  The failure of the generic budget at
   (m=4) is not hidden.
8. **Four arms.**  For (l_4\ge3), all equal distance-sum groups are listed
   and split by exact multisets.  For (l_4\le2), the capacity condition leaves
   exactly three length tuples, and every representation is tabulated.
9. **Diameter identity.**  The two longest arms give
   (n-D+1=2+\sum_{i=1}^{m-2}l_i).

Conclusion: the capacity condition is necessary and sufficient, and the
diameter conjecture holds for every finite-dimensional starlike tree.

## Sharpness and finite verification

- Arm lengths ((1,1,n-3)) give the source equality family.  The constructed
  upper bound is 3; the standard nonpath/no-dimension-2 lower bound makes the
  value exact.
- Two independent exhaustive implementations agree through order 15.  Their
  completeness arguments and exact outputs are recorded in
  `REPRODUCIBILITY_AUDIT.md`.

## Remaining fatal gap

No step above controls interactions among rooted branches attached at two or
more branching vertices.  Nothing in this audit proves the original
conjecture for arbitrary trees.

## Continuation reconstruction

The referee separately reconstructed `proof/hull_center_deletion.md`.

1. Every leaf of the minimal landmark hull is a landmark.
2. Removing the hull center leaves a farthest hull leaf available for every
   projection point.
3. The maximum surviving shell index is the attachment depth plus hull
   eccentricity.
4. Subtracting the hull radius recovers the minimum distance to the center;
   the deleted contribution is one value or two consecutive values.
5. This is a per-vertex reconstruction and covers vertices inside the hull,
   outside it, in equal or different attachments, and across the hull
   boundary.

Thus the arbitrary-complement hull-center deletion lemma is proved.  It cannot
self-iterate because its deletion does not change the hull.

The proposed local repair is refuted on (P_7): after the global and local
center deletions, vertices 2 and 4 both have code
(\{\!\{0,2,2,4\}\!\}).  Independent labeled-tree enumeration through
order six proves minimality.  Separate exact witnesses cover a nonpath
equality case, repeated rooted branches, and two branching vertices.

The diametral rooted-attachment shell identity and the necessary pairwise
distinct rooted-branch profile lemma are exact.  They do not give a
sufficiency theorem: cross-attachment polynomial cancellation remains fatal
gap G09.

Continuation decision: PASS for the stated structural lemma and exact method
counterexample; OPEN AFTER SEARCH for the arbitrary-tree conjecture.
