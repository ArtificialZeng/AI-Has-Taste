# Fresh citation and dependency audit

## Scope and method

This release audit used the advisory `citation-check-skill` in two separate
passes: claim extraction followed by search verification.  The search date was
2026-09-08.  I read both authored dependencies in `publication.json`, the
extracted PDF text, and the rendered reference list.  I also checked the local
user-bibliography report and the primary web records identified below.  The
mathematical proof was already accepted separately and is not certified by this
citation audit.

Bindings checked in this report:

- evidence snapshot: `541d34c4cdaca83b4396c9302a0418af32ffe4cc1fedd99b0f6b17a06c273718`;
- manuscript snapshot: `eb00feeb1d21ef170e521b805881d769bca7fc11dd6ea8211719eadb6a32d36b`;
- PDF: `a4d13aa84c9372f466abb5f6b0d4a4127e11b4f3499b010b68708784c29f59d9`.

## Pass 1: fixed claim extraction

The following list was fixed before source verification.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Liu and Chen's 2026 arXiv v1 paper is the originating finite-support quantum-walk source for this continuum operator. | existence / attribution | p.1, context |
| C02 | Liu and Chen proved `lambda(u)=1-(pi^2/4)u+o(u)` and left higher-order endpoint analysis for future work. | attribution / mathematical statistic / temporal | p.1, Eq. (2) and following sentence |
| C03 | The finite-interval Fourier-cutoff setting has a broad time--frequency-limiting antecedent in Slepian and Pollak (1961). | attribution / comparative context | p.1, context |
| C04 | Zeng (2026) uses solvable constrained operator/model classes to certify spectral-constant bounds, but concerns spectral sets rather than the present heat kernel. | attribution / comparative context | p.1, context |
| C05 | A Python calculation evaluated the trial quotient and Robin comparison at five decreasing values of `u`; those numbers are not used in the proof. | statistic / existence | p.5, assistance disclosure |

## Pass 2: verification

| ID | Status | Evidence and exact support check |
|---|---|---|
| C01 | Verified (paraphrase) | The primary arXiv v1 HTML record gives the exact title, authors, version/date, derives the near-front continuum operator in Section V, and identifies the Gaussian kernel in Eqs. (45)--(48): <https://arxiv.org/html/2609.01970>. |
| C02 | Verified (exact for the displayed expansion; paraphrase for scope) | Liu--Chen Eq. (59), proved in Appendix A.5, is exactly `lambda(u)=1-(pi^2/4)u+o(u)`.  Their Section IX labels Eq. (69) conditional and states that higher-order analysis is left for future work.  The hypotheses and the same scaling function are the ones cited by the manuscript. |
| C03 | Verified (interpretive comparison) | The publisher record for Slepian--Pollak describes bandlimited functions orthogonal on a finite interval and gives the exact 1961 journal metadata, volume 40, pp. 43--63, DOI `10.1002/j.1538-7305.1961.tb03976.x`: <https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1961.tb03976.x>.  The manuscript claims only a broad tradition and imports no theorem from it. |
| C04 | Verified (paraphrase) | `literature/user_bibliography_check.md` fixes the workbook metadata and permitted narrow use.  The official Preprints.org v1 page independently matches title, author, August 2026 date and DOI and states sharp results for constrained square-zero/model classes and explicit certificates: <https://www.preprints.org/manuscript/202608.1272>.  The manuscript explicitly excludes support for the Gaussian theorem or priority. |
| C05 | Verified (exact local reproduction) | Re-running `python3 evidence/numerical_sanity.py` produced five rows at `u=0.04, 0.01, 0.0025, 0.000625, 0.00015625`, agreeing exactly with `evidence/numerical_sanity.txt`.  The theorem and proof contain none of these computed values. |

The Zeng metadata basis remains the user-designated workbook
(`metadata_basis=user_designated_workbook`), as required by the workflow.  An
external refresh was available in this audit and agreed with that record; it
did not override it.

## Bibliography and dependency checks

- All three cited keys in `manuscript/article.aux` resolve to distinct entries
  in `manuscript/article.bbl`; the extracted PDF shows references `[1]`--`[3]`
  and no question marks or unresolved citation markers.
- Names, titles, year/version, venue and pages agree with the primary records
  above.  The workbook DOI and BibTeX fields for `202608.1272` were preserved.
- The manuscript makes no global novelty or priority claim.  Each contextual
  sentence is narrower than the available support, and none is used in the
  proof.
- The sorted dependency scope is exactly `manuscript/article.tex` and
  `manuscript/references.bib`.  The TeX file has no imported authored TeX,
  figures, data or custom styles; the bibliography database is explicitly
  listed.  Generated `.aux`, `.bbl`, `.out`, log and PDF files are not authored
  source dependencies under the contract.

**Verdict: accept.**  No undefined citation, contradicted attribution,
unsupported novelty statement, unverified bibliography record, or incomplete
authored dependency was found.
