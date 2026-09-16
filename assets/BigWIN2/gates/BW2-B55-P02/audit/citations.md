# Citation and bibliography audit

The extraction-only ledger was frozen before verification.  All fourteen
claims then passed a separate verification pass; the four cited sources were
checked at the primary record or original full text.  The exact claim-to-source
locations are in `audit/source-locations.json`, and the per-claim decisions are
in `audit/citation-verification.json`.

| Key | Nearby use | Primary support | Decision |
|---|---|---|---|
| `ShmoysTardos1993` | matching-based assignment rounding | original article, pp. 461--464 | verified; metadata and DOI agree |
| `WangSitters2016` | simple 11/6 graph-balancing algorithm | publisher-form PDF abstract, p. 723 | verified exactly |
| `Shavit2026` | nondeterminism, Theorem 2 family, Measurement 4 | arXiv v1, pp. 6--7 and 10--11 | verified exactly |
| `ZengEtAl2026` | integer/reconstruction certificate methodology | official version 1, Sections 3, 4, 6 | verified as a paraphrase |

The bibliography is not library-only: it includes the original rounding paper,
the Wang--Sitters algorithm paper, and the closest primary source for the
specific family.  Active user-library row 9 is directly cited in body flow and
is retained only for its genuine method-level relevance.  Screening found no
second library item that could be added without padding.  All four BibTeX
entries match the checked author, title, year/version, venue and identifier
records; no replacement or citation-key change was needed.  The final BibTeX
and AUX sets both contain exactly the same four keys, with no unused entry,
missing entry, duplicate, undefined citation, or unresolved cross-reference.
