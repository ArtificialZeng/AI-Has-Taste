# Citation and bibliography audit

## Verdict

**Accept.** The two-stage audit first froze eight claim/citation pairs in
`audit/citation-claim-ledger.json` and then verified that fixed ledger in
`audit/citation-verification.json`. All eight are supported; there are no
numerical errors, misleading attributions, hallucinated citations, or
unverified retained items.

The user expressly prohibited subagents, so the four per-key checks were
performed serially in this release context using the same claim-level
protocol. Required author/title/year/venue or version searches were run for
each source. Original or authoritative text was inspected rather than relying
on DOI existence alone.

## Claim-to-source and bibliography coverage

| Key | Nearby claims | Primary verification | Why retained | Result |
|---|---|---|---|---|
| `LewisWon2026` | definitions and origin; values through eight; layered conjecture and Proposition 3.15; matching/permanent identity | arXiv v1 HTML, Sections 2 and 3.4, Question 3.13, Conjecture 3.14, Proposition 3.15 | This is the problem-origin and closest-prior-result source. | Verified |
| `HarrisEtAl2020` | NumPy supplies the implementation's fixed-width arrays | Nature 585 (2020), 357--362, DOI `10.1038/s41586-020-2649-2`, plus direct code inspection | The actual exact enumerator imports and uses NumPy arrays. | Verified |
| `LamPitrouSeibert2015` | Numba compiles the integer algorithm for speed | ACM DOI `10.1145/2833157.2833162` and official Numba citation/documentation pages, plus direct code inspection | The enumerator uses Numba; the paper does not ascribe mathematical correctness to the compiler. | Verified |
| `Zeng2026SSRN7374858` | limited comparison to proof-carrying complete enumeration with independently implemented verification | Official Crossref deposited metadata and abstract in the exact recovery file | Genuinely relevant to the reproducibility method only; the adjacent sentence excludes support for crossword grids, 28549, coverage, and maximizers. | Verified within deposited abstract scope |

The bibliography is not Excel-only or user-library-only. Lewis--Won supplies
the domain definitions, problem origin, lower bound, and closest comparison.
The software sources support the tools actually used. The user-library source
is one limited methods comparison and does not replace the domain source.
No additional general permanent citation is required because the manuscript
states and proves its exact subset recurrence rather than invoking an external
theorem. Adding unrelated user-library items would be padding.

## Recovery evidence audit

Before assessing availability, all `literature/crossref-*.json` and
`literature/crossref-*.md` files were enumerated. The SHA-256 of
`literature/crossref-row20-postblocker-2026-09-06.json` was independently
recomputed as
`15f74f3590fe5719b86db8ef7cdf36993ab5974ee5d60595b9b4eb74f7085957`,
exactly the supplied value. JSON parsing confirms `status=ok`,
`message-type=work`, `source=Crossref`, DOI
`10.2139/ssrn.7374858`, the title, sole author Zijian Zeng, issued year 2026,
and posted-content/preprint type. The companion supervisor record identifies
the official Crossref endpoint, HTTP status 200, and retrieval timestamp; the
recovery request binds the byte-identical post-blocker file.

The deposited abstract supports the limited methods sentence: it reports
independent complete enumerations, two independent enumerators, checked LRAT
certificates, perfect-matching classification, and independent reconstruction.
It does not mention crossword grids and cannot support the theorem. The exact
audit binding is in `audit/recovery-evidence.json`.

## BibTeX and body-flow checks

All four `\cite` keys in `manuscript/main.tex` exist exactly once in the
canonical `manuscript/references.bib`; all four bibliography entries are cited.
The selected row-20 item has the ordinary body-flow direct citation
`\cite{Zeng2026SSRN7374858}` at lines 216--220. No cite key changed. The
Crossref `posted-content` record is represented as `@misc` so BibTeX does not
misstate a journal; its registry title, author, year, publisher, DOI, URL, and
final key are retained.

The mechanical checker reports four cited keys, four bibliography keys, zero
missing keys, zero unused entries, and exact agreement with `main.aux`. The
converged `main.log` and `main.blg` contain no undefined citations, missing
database entries, repeated entries, BibTeX warnings, LaTeX errors, or undefined
cross-references.

Search and verification date: 2026-09-06.
