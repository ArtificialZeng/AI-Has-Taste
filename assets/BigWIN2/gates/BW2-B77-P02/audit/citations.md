# Citation and bibliography audit

## Scope and method

This release used a non-interactive two-stage search-verification audit.  Stage
one froze every ordinary body-flow claim/citation pair in
`audit/citation-claim-ledger.json`; its key union is exactly
`Brindle2025`, `Hoffman2000`, `Mozgovoy2026`, `Takeyama2013`, and
`ZengEtAl2026`.  Stage two checked those frozen claims against original full
text and primary publication records on 2026-09-09 UTC.  No `\nocite`, custom
cite macro, commented citation, verbatim citation, or conditional citation is
present.

## Claim-level findings

| Ledger claim | Key | Primary passage checked | Finding |
|---|---|---|---|
| CIT-01 | `Hoffman2000` | arXiv `math/9907173`, PDF p. 2, equation (1) and Theorem 2.1 | Verified exactly: the unit rule and three-term recursion specialize to the displayed product. |
| CIT-02 | `Mozgovoy2026` | arXiv `2609.04424v1`, Section 3.2, Theorem 3.5 | Verified exactly: the theorem states (Z(\tau u)=Z(u)). |
| CIT-03 | `Mozgovoy2026` | Same source, Conjecture 3.6 | Verified exactly: the canonical surjection is conjectured to be an isomorphism.  The abstract was corrected to say that Mozgovoy *records* the conjecture, avoiding an unsupported attribution of origin. |
| CIT-04 | `Brindle2025` | arXiv `2511.07302v1`, abstract and pp. 2--5 | Verified as a conservative paraphrase: the paper treats the formal SZ-qMZV stuffle/duality quotient and proves only partial structural cases. |
| CIT-05 | `Takeyama2013` | SIGMA 9 (2013) 061, PDF p. 2 | Verified exactly: the reported computer experiment reaches “up to weight 7” for modified qMZVs using double shuffle and resummation duality. |
| CIT-06 | `ZengEtAl2026` | Preprints.org version 1, Section 6 | Verified as a methodological paraphrase: generated certificates are checked by reconstruction and separate exact implementations using integer predicates. |

Primary records consulted were the [Hoffman arXiv source](https://arxiv.org/pdf/math/9907173),
[Mozgovoy versioned HTML](https://arxiv.org/html/2609.04424v1),
[Brindle versioned PDF](https://arxiv.org/pdf/2511.07302v1),
[Takeyama's journal PDF](https://sigma-journal.com/2013/061/sigma13-061.pdf),
and the [Preprints.org version-1 record](https://www.preprints.org/manuscript/202608.1658).
Titles, authors, dates/versions, venues, and available DOI/arXiv identifiers
agree with `manuscript/references.bib`.

## Coverage and consistency

All five retained references support a nearby substantive claim; none is
decorative.  The four non-library sources cover the quasi-shuffle method, the
problem source and closest qMZV comparisons.  Registry row 9 is the only
selected user-library item and is naturally used for the independent exact
verification architecture; a second library item would be unrelated padding.
The active 49-record registry, its source workbook, DOI, official version-1
page, and exact manuscript context were checked.  The hook-compatible selection
validator accepts `audit/user-bibliography-selection.json` for citation attempt
1 and launch `4ad9444d-06f5-4837-b854-500544ad58b2`.

The bibliography-key checker reports five cited keys, five bibliography keys,
no missing or unused entry, and exact agreement with the final `.aux` file.
There were no key changes and no officially unverified item.  The final LaTeX
and BibTeX logs contain no undefined citation, missing database entry, repeated
entry, or bibliography warning.

**Verdict: accept.**
