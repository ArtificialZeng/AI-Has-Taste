# Citation audit

Status: **PASS**

Searches were run before computation and repeated after the exact result on
2026-08-30 UTC.  Full queries and bounded negative findings are in
`literature/search_log.md`; claim-level provenance is in
`literature/claim_ledger.md`.

## Primary-claim checks

| Manuscript claim | Primary source checked | Exact location/result | Outcome |
|---|---|---|---|
| Definition of NAC and division by two | Clinch et al., DOI 10.1002/jgt.70064 | Definitions 2.1--2.2 | exact |
| Two-family conjecture | Clinch et al. | Conjecture 6.1 | exact |
| Verified through 10 vertices | Clinch et al. | sentence immediately before Conjecture 6.1 | exact author report |
| Counts already computed at 11 and 12 | Clinch et al. | Figure 3 and caption | exact author report |
| Family-A formula (2^p-1) | Clinch et al. | paragraph immediately after Conjecture 6.1 | exact |
| Laman characterization | Laman, DOI 10.1007/BF01534980 | main characterization | exact |
| No-stable-cut characterization | Le--Pfender, DOI 10.37236/2513; Rauch--Rautenbach, DOI 10.37236/13629 | Theorem 5 / repaired Theorem 4 | exact with repair cited |
| Canonical generation software/count | Larsson repository at recorded revision | README command and order-11 table | exact software artifact |
| Independent graph universe | Capco et al., Zenodo 10.5281/zenodo.1245517 | `LamanGraphs11.zip` and description | exact data artifact |

Publisher/Crossref metadata were checked for all journal titles, authors,
years, volumes, pages or article numbers, and DOIs.  The LaTeX audit reports
eight cited keys, eight bibliography entries, no missing keys, and no unused
entries.

## Novelty boundary

The current primary paper remains a conjecture and reports only the family
classification through order 10, although its Figure 3 already gives NAC
count distributions at orders 11 and 12.  Searches by exact title, DOI,
conjecture number, the number 2,039,273, “11 vertices,” and “one open step”
found no primary source certifying the order-11 family classification.  The
manuscript therefore claims the new classification/certificate only and uses
bounded wording about the search; it does not claim that the order-11 NAC
count itself was previously unknown.
