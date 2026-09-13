# Proof dependency graph

Terminal finite claim: the radius-seven exchange optimum around the specified
Appendix C code is exactly 334.

1. **D0: serialized primary data.** Two invertible binary generators and
   9+26+68 rank-three representatives are fixed in
   `data/appendix_c_333.json`.
2. **D1: baseline reconstruction.** The generated orbits are disjoint, have
   lengths 1, 2, and 4 with the declared census, and contain 333 distinct
   planes of pairwise distance at least four.
3. **D2: ambient completeness.** Canonical RREF enumeration gives exactly
   29,212 subspaces with layer census
   1,127,2667,11811,11811,2667,127,1.
4. **D3: blocker equivalence.** A candidate can coexist with the retained
   baseline precisely when all of its blockers are removed.
5. **D4: normalization lemma.** Unused removals may be restored, so an optimum
   removal set is the union of blockers of its additions.
6. **D5: union completeness.** The verifier independently closes all relevant
   blocker sets under unions of cardinality at most seven, obtaining 2,561,563
   normalized sets.
7. **D6: exact local optimization.** For every normalized set, every subset of
   the eligible graph (at most 15 vertices) is tested; the maximum values by
   removal size are 334,333,333,333,334,333,333,333.
8. **D7: attainment.** The empty removal plus the full space has size 334 and
   minimum distance four.
9. **Conclusion.** D0--D7 prove that the radius-seven exchange optimum is 334.

Global non-dependency: neither the published SDP bound 388 nor the timed-out
constant-dimension MILP is used in this finite theorem.
