# Fresh citation and claim-scope audit

## Binding and method

This release audit applies the requested `$citation-check-skill` in search
mode, with a fixed extraction pass followed by a separate verification pass.
The search date is 2026-09-07.  I reviewed the authored dependencies
`manuscript/main.tex` and `manuscript/references.bib`, the extracted text of
the four-page PDF, the accepted claim and mathematical audit, and
`literature/user_bibliography_check.md`.  The manuscript and PDF digests are
those in the current `audit/manuscript-snapshot.json`.

The publication dependency scope is complete.  The TeX file has no imported
local TeX, style, image, or data dependency; its only authored compilation
dependency is `manuscript/references.bib`.  The `.fls` inputs confirm this.
Both cited keys occur in the bibliography and in the resolved `.bbl`, and the
rendered/extracted reference list contains both entries.  There are no
undefined citations.

## Pass 1: fixed claim extraction

The following externally checkable citation claims were frozen before any
source verification.  Definitions, the paper's own methodology, and the
mathematical theorem were not reclassified as literature claims; the latter
was checked instead for exact agreement with the accepted mathematical
scope.

- **C01 (metadata/existence):** Ye (2026), *Diffusion under competing bulk and
  surface stopping mechanisms*, exists as arXiv:2609.05247v1, by Yilin Ye,
  submitted 4 September 2026.
- **C02 (attribution):** Ye's normalization identifies the exponential
  boundary-local-time rate with the Robin parameter when (D=1), and uses
  the two independent exponential stopping mechanisms defining (T,L).
- **C03 (attribution):** Ye's Appendix F gives the displayed affine numerator
  functions \(\xi_1,\xi_2\) for the uniform-start three-ball correlation and
  reports positivity over the parameter range explored there.
- **C04 (attribution):** Ye derives marginal distributions, the joint
  transform, mixed moments, and explicit three-ball formulae.
- **C05 (metadata/existence):** Zeng (2026), *The Distinct-Cycle-Length
  Probability is Strictly Decreasing after 30*, is registered as SSRN
  7380519 with DOI 10.2139/ssrn.7380519 and author Zijian Zeng.
- **C06 (attribution):** That paper combines analytic bounds with exact,
  independently checked finite comparisons in a permutation-cycle problem;
  it supplies no reflected-diffusion result.

No chart, table, empirical statistic, ranking, or direct quotation appears in
the manuscript.  The numerical constants in the proof are mathematical
claims already covered by the accepted audit, not literature statistics.

## Pass 2: verification

- **C01 — Verified (exact).**  The official arXiv record gives the exact
  title, Yilin Ye, category `cond-mat.stat-mech`, arXiv:2609.05247v1, and the
  4 September 2026 submission date:
  <https://arxiv.org/abs/2609.05247>.
- **C02 — Verified (paraphrase).**  The primary HTML states
  \(q=\kappa/D\), an exponential local-time threshold, mutually independent
  exponential thresholds, and the definitions of \(T\) and \(L\).  With
  (D=1), the manuscript's generator and Robin boundary condition have the
  stated normalization; see Sections I--II of
  <https://arxiv.org/html/2609.05247v1>.
- **C03 — Verified (exact/paraphrase).**  Appendix F, equations (116)--(117),
  prints the same \(\xi_1,\xi_2\) numerator and Figure 8; the sentence after
  (117) says the correlation stays positive over the explored range.  The
  manuscript accurately limits this to the explored range and does not
  attribute a full-quadrant theorem to Ye.
- **C04 — Verified (paraphrase).**  The arXiv abstract states that the paper
  derives the marginal distributions, joint Laplace transform, and hierarchy
  of mixed moments, while its abstract and Section III state that explicit
  three-dimensional-ball results are obtained.
- **C05 — Verified for registered metadata, with access limitation.**  The
  supplied workbook row and same-day official Crossref check recorded in
  `literature/user_bibliography_check.md` agree on title, author, year, DOI,
  publisher, abstract, and SSRN target.  All prescribed author/title,
  exact-title repository, venue, and DOI searches were rerun.  Because this
  record was newly deposited, the fresh searches did not surface its landing
  page, and direct SSRN/Crossref endpoints were unavailable in this context.
- **C06 — Verified at abstract level, with the same full-text limitation.**
  The registered/supplied abstract describes analytic coefficient and moment
  bounds, exact integer comparisons for the finite remainder, and an
  independent outward-rounded rational-interval check.  That supports the
  manuscript's explicitly delimited methodological comparison.  The title
  and abstract concern permutation cycle lengths and provide no
  diffusion-specific premise.  The full SSRN PDF was not directly accessible
  during this bounded release audit.

## Accepted scope and verdict

The theorem, exact counterexample, zero-set classification, and variance
statement reproduce the accepted `resolution-paper` scope without
strengthening it.  The manuscript makes no broad novelty or priority claim;
its only comparison with the user-supplied paper is labeled unrelated and
methodological.  Ye is the closest result and is represented accurately.

**Verdict: accept with citation limitations.**  No citation is contradicted,
misquoted, unnecessary, undefined, or used to support the mathematical
resolution.  The sole limitation is direct landing-page/full-text access for
the newly deposited Zeng SSRN record; registered metadata and the narrow
abstract-level claim were checked, and the limitation is immaterial to the
diffusion theorem.
