# Citation and bibliography release audit

## Verdict

Accept.  The final manuscript has three cited sources and three bibliography
entries.  Every source exists, every body citation resolves, and every nearby
claim is supported at the stated scope.  `audit/citation-claim-ledger.json`,
`audit/source-locations.json`, and `audit/citation-verification.json` record
the two-pass audit.

## Claim-to-source map and coverage

- `FokamSouopBitjoka2026` is necessary for the definition, exact difference
  criterion, product bound, order-20 construction, and closest reported exact
  grid value.  The inspected PDF passages are recorded page-by-page.
- `HagbergSchultSwart2008` is the natural primary software citation for
  NetworkX.  The manuscript does not attribute its new counts to that paper.
- `Zeng2026Figshare33318282` is the single genuinely relevant active-library
  work.  Its official description supports only the narrow methodological
  comparison; the manuscript expressly says it provides no premise.

The bibliography is not Excel-only: the problem origin and closest result are
cited to the primary arXiv paper, and the verification tool is cited to its
original proceedings paper.  Elementary regularity, the handshake lemma,
finite abelian classification in these three small orders, and the manuscript's
fully given counting reductions do not naturally require further citations.
A second library citation would be padding.

## Bibliographic consistency

The original manuscript source had three keys; the final source also has
three.  The citation repair changed `Zeng2026SSRN7374858` to
`Zeng2026Figshare33318282` because the former could not be independently
opened or located through the mandatory searches, while the latter has a
directly accessible authoritative primary page and exact nearby support.  The
arXiv entry was corrected from version 1 to the actually inspected version 2.
No other key changed.  The canonical file is `manuscript/references.bib`.

The BibTeX checker reports 3 cited keys, 3 database entries, no missing or
unused entries, and exact agreement with the final AUX file.  The final log
has no undefined citations, missing database entries, duplicate entries, or
BibTeX warnings.

Search date: 2026-09-07.  The audit ran the required author/title/venue and DOI
queries for each academic source.  No `literature/bibliography-revision-*.md`
or `literature/crossref-*` capture existed in this project.
