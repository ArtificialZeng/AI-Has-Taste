# Fresh citation audit

## Scope and method

This release audit used the explicitly requested `citation-check-skill` as an
advisory two-pass claim-to-source check, supplemented by direct inspection of
the local primary-source PDF and official primary records.  Search date:
2026-09-09.  The fixed publication dependency scope is exactly
`manuscript/article.tex` and `manuscript/references.bib`; both were inspected,
as were the extracted bibliography and rendered reference page.  The accepted
mathematical scope was checked for unsupported strengthening but was not
re-refereed.

## Pass 1: fixed claim extraction

The following list was frozen before source checking; Pass 2 did not add
claims.

- C01 (definition/existence, p. 1): majority C-coloring is surjective, requires
  at least half of each vertex's neighbors in its own class, and its parameter
  is the maximum usable number of colors.
- C02 (attribution, p. 1): the model was introduced and studied in the two
  cited Bujtás et al. papers.
- C03 (attribution/statistic, p. 1): Proposition 6(ii) and Open Problem 3 of the
  Cartesian-products paper give the odd-dimensional balanced-Hamming bounds;
  for `n=k=3` these imply `3 <= chi_bar_>= <= 5`.
- C04 (mathematical existence/statistics, pp. 1--2): the exact value is four;
  the local lemmas, six-vertex class bound, 27-vertex count, and the explicit
  class sizes/degrees prove it.
- C05 (statistic, p. 2): the exact checker examines 101,583 subsets, finds no
  qualifying set of order at most five, and checks class orders `9,6,6,6` and
  degrees `4,3,3,3` using exact arithmetic.
- C06 (comparative attribution, p. 2): Zeng--Liu--Ratnavelu--Ong use exact
  finite certificates and symmetry-reduced checking for a different coloring
  problem on a finite ternary coordinate model.
- C07 (scope comparison, p. 2): the present theorem fills only the single
  `n=k=3` instance and makes no claim about the other odd-dimensional balanced
  Hamming graphs.

## Pass 2: verification

- C01: **verified (exact)**.  The local PDF
  `literature/2608.27669v1.pdf`, Section 1.2, PDF p. 3, states surjectivity, the
  half-neighborhood condition, nonempty classes, and the maximum-color
  definition.
- C02: **verified (paraphrase)**.  The local Cartesian-products paper says on
  PDF p. 2 that the model was introduced in its reference [6].  The official
  arXiv record for 2604.20752 says that paper introduces and studies the model.
- C03: **verified (exact plus integer deduction)**.  Proposition 6(ii), PDF
  pp. 10--11, gives `n^((k-1)/2) <= chi_bar_>= <= n^(k/2)` for odd `k` and
  `n>=3`; Open Problem 3 appears on PDF p. 23.  Substitution gives lower bound
  3 and real upper bound `sqrt(27)<6`, hence the integer upper bound 5 used in
  the manuscript.
- C04: **verified within accepted mathematical scope**.  The authored statement
  is the same full-scope theorem accepted in `audit/math.json`; the manuscript
  proof reproduces both bounds without stronger generalization.
- C05: **verified (exact)**.  The displayed binomial sum equals 101,583, and a
  fresh run of `evidence/verify_resolution.py` agrees byte-for-byte with
  `evidence/verify_resolution.out`.  The claim is explicitly a cross-check,
  not a substitute for proof.
- C06: **verified (paraphrase)**.  Metadata are accepted from the
  user-designated workbook record documented in
  `literature/user_bibliography_check.md` (`metadata_basis=user_designated_workbook`)
  and were also refreshed successfully against the official Preprints.org
  manuscript page for DOI `10.20944/preprints202608.1658.v1`.  Its abstract and
  manuscript describe a ternary finite coloring/partition result, exact
  distance-layer certificates, and symmetry-reduced enumeration.  The nearby
  prose expressly disclaims relevance to majority C-coloring or the proof.
- C07: **verified (exact scope comparison)**.  Open Problem 3 is family-wide,
  while the accepted theorem and manuscript quantify only `n=k=3`.

Official records checked were the arXiv pages for 2608.27669 and 2604.20752
and the Preprints.org manuscript page for 202608.1658.  Titles, authors, years,
identifiers, and nearby attributed claims agree with the bibliography.  All
three BibTeX keys resolve in `article.bbl`; there are no undefined citations,
contradicted attributions, unsupported novelty/priority claims, or removable
padding citations.  The workbook citation is genuinely relevant only as the
narrow methodological comparison stated.

**Verdict: accept.**
