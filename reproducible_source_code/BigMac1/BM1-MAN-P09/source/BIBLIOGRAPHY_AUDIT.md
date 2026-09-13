# Bibliography audit for v16

Scope: every citation key in `main.tex` and every record in `references.bib`.
The mechanical audit found five cited keys, five BibTeX records, no missing
key, no unused record, and five resolved `\\bibcite` entries after the clean
BibTeX build.

## Per-key verification

| key | primary records | metadata verdict | claim-context verdict |
|---|---|---|---|
| `MR2223270` | [Springer](https://link.springer.com/article/10.1007/s00013-005-1533-5), [DOI](https://doi.org/10.1007/s00013-005-1533-5) | Title, authors, journal, volume 86, issue 4, pages 352--355, year 2006, and DOI match. | The paper is specifically a lenticular von Neumann inequality, so the cited lens-reduction context is direct. |
| `Crouzeix_2003` | [Springer](https://link.springer.com/article/10.1007/s00013-003-0569-7), [DOI](https://doi.org/10.1007/s00013-003-0569-7) | Title, authors, journal, volume 81, issue 5, pages 559--566, November 2003, and DOI match. | The official abstract treats norm estimates for analytic functions of strip or sectorial operators, exactly the context cited. |
| `MR2449098` | [AIMS](https://www.aimsciences.org/article/doi/10.3934/cpaa.2009.8.37), [DOI](https://doi.org/10.3934/cpaa.2009.8.37) | Title, authors, journal, volume 8, issue 1, pages 37--54, year 2009, and DOI match. | The official abstract proves a configuration-independent bound, for fixed number of disks, for intersections of spherical disks. |
| `MR2047592` | [Springer](https://link.springer.com/article/10.1007/s00020-002-1188-6), [DOI](https://doi.org/10.1007/s00020-002-1188-6) | Title, author, journal, volume 48, issue 4, pages 461--477, year 2004, and DOI match. | The official abstract studies uniform bounds for analytic matrix functions under numerical-range containment, directly supporting the cited perspective. |
| `Crouzeix_2016` | [SIAM](https://epubs.siam.org/doi/10.1137/15M1020411), [DOI](https://doi.org/10.1137/15M1020411) | Title, author, journal, volume 37, issue 1, pages 420--442, year 2016, and DOI match. | The official abstract concerns constants related to numerical ranges and their open problems, matching the cited context. |

The stable keys were retained.  The publisher/DOI metadata differ from the
existing records only in harmless normalization such as journal abbreviation,
URL form, page-dash encoding, publisher/month fields, or capitalization.
MathSciNet-only `MRCLASS` and `MRREVIEWER` fields were not used to support any
claim and were not independently re-exported in this audit.

## Final mechanical gate

Run from the release root:

```sh
python3 audits/check_bib_keys.py \
  --bib references.bib --aux main.aux main.tex
```

Required result: `cited_keys=5`, `bib_keys=5`,
`cited_keys_missing_from_bib=0`, `bib_keys_not_cited=0`,
`aux_bibcite_keys=5`, and no AUX mismatch.  The final release build log must
also contain no undefined citation, missing database, duplicate-entry, or
BibTeX format warning.
