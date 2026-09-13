# Referee record

Date: 2026-08-30.  Reconstructed from definitions rather than Builder
intuition.

## Scope

The statement concerns the simple quotient on isomorphism classes.  It does
not count loops or parallel Pasch occurrences as graph edges.  The isolated
component's diameter is defined as zero.

## Dependency audit

- Pasch switching preserves pair coverage because the two four-block sides
  cover exactly the same 12 pairs.
- Relabeling commutes with switching, so one representative per class is
  sufficient.
- The verifier proves validity and pairwise nonisomorphism of the released
  representatives.  Exhaustion relies on the published 80-class
  classification; equality with the complete DesignTheory.org catalogue is
  an exact cross-check.
- Edge completeness is established by exhaustive cycle enumeration and
  exact isomorphism maps, not by canonical hashes.
- Diameter 11 has both sides: an 11-edge geodesic/layer-11 lower bound and
  79 all-pairs BFS rows for the upper bound.

## Novelty audit

The 1999 paper already contains the complete switch outcome table and must
receive clear priority.  Two recorded search passes located no publication
that states the diameter 11.  Acceptable wording is only “not located in the
recorded searches,” not an absolute priority claim.

## Final verdict

Mathematical endpoint: pass as a certified finite result. Proof assistant:
none used. Citation/BibTeX checks, clean LaTeX convergence, metadata,
page-by-page PDF inspection, source packaging, and manifest verification all
pass. The release is suitable for expert review, subject to the explicitly
bounded priority claim and the classical classification dependency.
