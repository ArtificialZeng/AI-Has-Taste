# Citation and novelty audit

Search cutoff: 2026-08-30

Status: PASS for submission with the stated bounded-search novelty caveat.

## Source verification

- **Simanjuntak--Siagian--Vetr\'ik (2017), arXiv:1711.00225.**  Definition,
  paths as the dimension-1 graphs, and nonexistence of dimension 2 checked in
  the primary preprint.
- **Hafidh et al. (2019), arXiv:1908.05879.**  Full text checked.  Theorem 1 is
  the tree (n-2) bound; Conjecture 2 is exactly
  (md(T)\le n-\operatorname{diam}(T)+1), sharp; the following paragraph gives
  the subdivided-claw equality family; Table 1 gives orders through 10.
- **Kono--Zhang (2021), DOI 10.47443/dml.2021.0042.**  Full journal PDF
  checked.  Proposition 2.1 is the necessary (2^r) short-arm capacity
  condition.  The paper proves selected sufficient starlike families, not the
  general converse or the diameter corollary stated here.
- **Hakanen--Yero (2024), DOI 10.3233/FI-242185.**  Journal record/full text
  checked for equivalence of multiset dimension and ID-number.
- **Albejani et al. (2026), arXiv:2607.08128.**  Conjecture 2 repeats the frozen
  diameter bound as open.
- **Allikvere (2026), arXiv:2607.28813.**  Theorem 1.1 resolves the older
  general-graph extremal conjecture but does not resolve the frozen tree
  conjecture.
- **Aho--Hopcroft--Ullman (1974).**  Bibliographic data and the standard
  rooted/center tree-isomorphism encoding attribution checked.

## Priority controls

- Simanjuntak's public MCCCC 32 slides (2018) state one-, two-, and three-stem
  classifications for multiset dimension 3.  Preliminary three-leaf and
  double-Y observations were therefore rejected as novel and are not used as
  manuscript contributions.
- The main fingerprint searched after the proof was: capacity is sufficient
  for all starlike trees; canonical binary arm patterns resolve; and the set
  meets (n-\operatorname{diam}(T)+1).
- Exact queries under “multiset dimension,” “ID-number,” “ID-coloring,”
  “starlike,” binary/capacity terms, the Kono--Zhang title, and Proposition 2.1
  recovered the 2021 necessary result but no matching converse or diameter
  theorem.
- Both July 2026 surveys and the later July 30 primary paper were checked.

The negative novelty finding is necessarily database-bounded.  The manuscript
therefore credits the nearest necessary result precisely and does not make an
absolute claim that no unpublished or unindexed work exists.

## Bibliography-to-text check

Every entry in `paper/references.bib` is cited in `paper/main.tex`; every
in-text citation has a bibliography entry.  No placeholder, fabricated DOI,
or unsupported theorem attribution remains.

## Continuation literature pass

- The full proof of Hafidh et al.'s Theorem 1 was reread.  It uses
  center/eccentricity reconstruction in a one-step (n-2) argument and does
  not claim an iteration to (D-1) omitted vertices.
- Targeted searches under multiset-dimension and ID-coloring terminology for
  landmark hull deletion, rooted depth profiles, attachment generating
  polynomials, and the exact (n-D+1) fingerprint found no matching primary
  result.
- The negative result is database-bounded and recorded as such in queries
  33--40 of `literature/search_log.md`.
- The continuation results are not added to the manuscript and are not used
  to make a stronger novelty claim.  The accepted paper and bibliography are
  unchanged.

Continuation citation status: PASS with the same bounded-search caveat.
