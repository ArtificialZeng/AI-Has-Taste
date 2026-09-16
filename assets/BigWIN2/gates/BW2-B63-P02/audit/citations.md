# Citation and bibliography audit

**Verdict:** accept.  **Search date:** 2026-09-07.  The audit used the
required two-stage procedure: `audit/citation-claim-ledger.json` froze six
claim/citation pairs before the source-support pass.  Extraction and
verification were not interleaved.  No subagents were used because this job
explicitly prohibited delegation.

## Claim-level verification

| ID | Key | Status | Exact primary support |
|---|---|---|---|
| CIT-01 | `GodsilMeagher2016` | Verified (paraphrase) | Cambridge's official Chapter 6 page and table of contents identify Chapter 6 as “The Johnson scheme,” with sections on graphs and eigenvalues of the Johnson scheme (pp. 112--120): https://www.cambridge.org/core/books/abs/erdoskorado-theorems-algebraic-approaches/johnson-scheme/340E47D4885572C91710E7645657BDE9 . |
| CIT-02 | `BrouwerEtAl2018` | Verified (paraphrase) | The Elsevier publisher abstract says the paper studies smallest eigenvalues of Johnson distance graphs and, more generally, relations of classical P- and Q-polynomial association schemes: https://doi.org/10.1016/j.jctb.2018.04.005 . |
| CIT-03 | `LuoEtAl2026` | Verified (exact) | The frozen official arXiv v1 PDF `evidence/external/2609.04677.pdf`, p. 3, equations (2.1)--(2.2), gives the Eberlein formula and multiplicities used in manuscript equations (1)--(2). |
| CIT-04 | `LuoEtAl2026` | Verified (exact) | The same PDF, p. 9, Proposition 12, assumes `t^2-t<4r-2` and concludes that for all sufficiently large `r` the smallest eigenvalue of `J(4r+t,2r,r)` is `E_r(2)`. |
| CIT-05 | `LuoEtAl2026` | Verified (exact scope comparison) | Proposition 12 on p. 9 says only “for all sufficiently large r”; it contains no explicit threshold or residual classification. Theorem 13 on p. 10 merely invokes Proposition 12 and does not add one. |
| CIT-06 | `Zeng2026` | Verified (paraphrase) | The official arXiv HTML, Section 4 final paragraph, calls its exact computations “diagnostic only” and says they are not used in the proof; the data statement repeats that no computational output is a premise: https://arxiv.org/abs/2608.18179 . |

Academic-citation searches used the prescribed author/title, full-title,
author/venue, DOI, and arXiv-identifier forms as applicable.  The frozen Luo
PDF has SHA-256
`de3b37a3c87eeeef297382da835922996e804e6b2ab44d1a2e763cc4fa9881f3`,
matching both `source.md` and the accepted evidence snapshot.

## Bibliographic-record audit

All four cited records exist.  Author, title, year/version, venue, volume and
pages where applicable, and DOI/arXiv identifier agree with the primary
records.  The publisher record verifies Brouwer--Cioabă--Ihringer--McGinnis;
Cambridge verifies Godsil--Meagher and its series volume 149; the frozen arXiv
PDF verifies Luo--Cao--Li--Li; and the official arXiv record verifies Zeng.
No key changes or BibTeX replacements were necessary.  The mechanical audit
found 4 cited keys, 4 bibliography keys, no missing or unused entries, and an
exact match with the `.aux` citation set.

## Coverage and relevance

The bibliography is not user-library-only.  It includes the problem-origin
and closest prior theorem (`LuoEtAl2026`), a primary systematic closest-area
paper (`BrouwerEtAl2018`), standard Johnson-scheme background
(`GodsilMeagher2016`), and one active-library item for the manuscript's narrow
verification-method comparison (`Zeng2026`).  Each retained citation has a
specific nearby claim; none is decorative.  No additional source is naturally
required for the manuscript's self-contained trace and exact-arithmetic proof.

The active-library selection is attempt-bound in
`audit/user-bibliography-selection.json` to citation attempt 1 and launch
`397f734f-6cad-482e-8664-3a0198f45d53`.  Row 17 was independently verified at
its primary arXiv record and appears in ordinary body flow as the direct
literal `\cite{Zeng2026}`.  Only one library entry is retained because the
spectrally closer row-10 registry lead could not be verified at an
authoritative primary record; adding it would be citation padding.

## Mechanical checks

- `check_bib_keys.py main.tex --aux main.aux`: 4 cited, 4 present, 0 missing,
  0 unused, and no `.aux` mismatch.
- Final `main.log` and `main.blg`: no undefined citations or references,
  missing database entries, duplicate entries, BibTeX warnings, LaTeX errors,
  fatal errors, or emergency stops.
- Unverified items: none. Blocking issues: none.
