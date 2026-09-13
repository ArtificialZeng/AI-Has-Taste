# BibTeX audit

Document: `paper/main.tex`  
Database: `paper/references.bib`  
Date: 2026-08-30 (release rerun)

## Citation surface

Five distinct keys occur in the manuscript:

| key | cited claim | official record | result |
|---|---|---|---|
| `Ball1986` | sharp cube-slicing bound; `d2` global maximum | AMS DOI `10.1090/S0002-9939-1986-0840631-0`, Theorem 4 | verified; key and entry retained |
| `Ambrus2022` | complete `Q4` critical classification | AMS article record and latest arXiv v3; DOI `10.1090/proc/15955`, Theorem 3 | verified; key and entry retained |
| `AmbrusGargyan2024` | Conjecture 1.3, all-`n>=4` construction, selected saddle branch | Elsevier VOR/arXiv v4; DOI `10.1016/j.aim.2024.109524` | verified; key and entry retained |
| `AmbrusGargyan2025` | non-extremality of `k`-diagonals, `3<=k<=n-1` for `n>=4` | Wiley VOR; DOI `10.1112/blms.70157`, Theorem 1.4 | verified; key and entry retained |
| `Pournin2025Erratum` | omitted transverse Hessian term; proper-subdiagonal scope and main-diagonal caveat | Springer VOR; DOI `10.1007/s11854-025-0384-1` | verified; key and entry retained |

## Reconciliation decisions

DOI content negotiation or the official publisher export supplied raw BibTeX
for all five works.  Four records
were converted only to LaTeX-safe ASCII forms (accent macros, `--` page ranges,
and math markup) while retaining the official metadata and the manuscript's
unambiguous keys.  The automatic raw keys (`Ball_1986`, `Ambrus_2024`,
`Ambrus_2025`, `Pournin_2025`) were not adopted, so no cite-key change was
needed.

The Crossref export for `10.1090/proc/15955` is materially wrong/incomplete:
it gives `author={Gergely, Ambrus}`, year 2021, and omits journal, volume,
issue, and pages.  That entry was not copied.  The released `Ambrus2022` entry
uses the AMS article/issue record: Gergely Ambrus, *Proceedings of the American
Mathematical Society* 150(10) (2022), 4463--4474.  This is a documented source
correction rather than an invented field.

For `Ball1986`, the official AMS DOI is retained instead of the secondary
JSTOR DOI.  For `AmbrusGargyan2024`, `109524` is the article number used by
Crossref and the VOR, not a page range.  The two 2025 entries match their
publisher records in authorship, title, journal, volume, issue, pagination,
year, and DOI.  No citation key or `.bib` field required a release change.

Blocked official verifications: **none**.  Direct publisher PDF/export
endpoints occasionally returned anti-automation responses, but every item was
resolved through the publisher-deposited DOI record plus a VOR, official issue
page, or latest corrected arXiv version.

## Mechanical and build checks

Final status: **PASS**.

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` converged
  with an up-to-date `main.pdf`, `main.bbl`, and `main.aux`.
- The required log scan found no undefined citation/reference, missing
  database entry, BibTeX warning, repeated entry, LaTeX error, fatal stop,
  undefined control sequence, runaway argument, package warning, or
  overfull/underfull box in `main.log` and `main.blg`.
- `check_bib_keys.py main.tex --aux main.aux` reports 5 cited keys, 5 database
  keys, 5 auxiliary `bibcite` keys, and zero missing or extra keys in every
  comparison.
- Release citation delta: `paper/main.tex` only.  `paper/references.bib` was
  unchanged.  Key mapping: none; the established manuscript keys were
  retained.  Unresolved official verifications: none.
