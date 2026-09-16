# Citation and bibliography release audit

## Result

**Accept.**  A noninteractive two-pass audit first froze fourteen claims in
`audit/citation-claim-ledger.json`, then verified that fixed ledger in
`audit/citation-source-verification.json`.  All fourteen claims passed; there
were no numerical errors, hallucinations, misleading citations, or unverified
claims.  The audit was performed serially because the release prompt expressly
prohibited subagents.

## Claim-to-source mapping

| Claims | Retained source | Exact support and why needed |
|---|---|---|
| C02 | Brändén--Huh (2020) | Annals abstract states the Hessian one-positive-eigenvalue property; this is the foundational Lorentzian-polynomial context. |
| C03 | Huang--Huh--Soskin--Wang (2025) | Abstract, Theorem B, Definition 1.8, and Conjecture 1.9 support bounded ratios, cut-cone duality, normalization, and the proposed bound 2; this is the conjecture-origin source. |
| C04 | Deza--Laurent (1997) | Chapter 29, especially Sections 29.3--29.6 (print pp. 472--486), treats validity, roots, facets, separation, and proofs for clique--web inequalities; this is the standard cut-cone source.  The manuscript locator was corrected from Section 30.6 to Sections 29.3--29.6 before the final freeze. |
| C05--C08, C13 | Baldi--Kummer (2026) | Abstract and Section 3, equations (1)--(3), Lemma 3.2, and the final display on PDF pp. 3--4 support the CW7 construction, objective, exact feasibility conditions, and point `(284,701,20)` with value about 2.01638.  The complete five-page source ends after that witness and does not state the sharp restricted-family supremum, nonattainment, or sequence.  This is the originating and closest-prior source. |
| C09 | Zeng--Liu--Ratnavelu (2026) | Official Preprints.org abstract, Theorem 1, and Sections 3--5 support an exact sharp permanent ratio on normalized rank-two real correlation matrices through a low-dimensional phase minimization.  It is the closest active user-library methodological comparison; the manuscript explicitly separates that PSD permanent problem from the Lorentzian problem. |
| C01, C10--C12 | Accepted mathematical audit | `audit/math.md` independently reconstructs the criterion, both branches, strict gap, and exact extremal sequence. |
| C14 | Job provenance and accepted audit | The recorded research, writing, checking, and release workflow supports the assistance disclosure; the proof is exact and self-contained. |

The primary records checked on 2026-09-07 were the Annals article page,
arXiv records 2510.25030 and 2609.03934 (including the frozen local v1 PDF),
the Springer DOI record and Chapter 29 text for the cut-cone book, and the
official Preprints.org manuscript page for 202608.1346v1.  Author, title,
year, venue/version, DOI/eprint, hypotheses, and nearby passages agree with
the five BibTeX entries.  No key change or BibTeX replacement was needed.

## Coverage and consistency

The bibliography is not user-library-only: it includes the originating and
closest bounded-ratio sources, the foundational Lorentzian source, and the
standard cut-cone source, as well as one verified user-library comparison.
Each retained item supports an ordinary body-flow citation and a specific
nearby claim; no unused or decorative entry remains.  Only one user-library
paper was selected because the other 48 active records lack a comparably
close combination of normalized matrix families, exact sharp ratios, and
low-dimensional reduction, so adding a second would be padding.

The bibliography checker found five cited keys and five BibTeX entries, with
zero missing, unused, AUX-only, or source-only keys.  The final `main.log` and
`main.blg` contain no undefined citation/reference, missing database entry,
repeated entry, BibTeX warning, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.

Limit: the audit verifies the stated comparison against the closest known and
cited sources; it does not assert exhaustive literature priority or journal
acceptance.
