# Fresh citation audit

## Bound scope and method

This release audit reviewed the complete current manuscript and extracted PDF,
the two files listed in `publication.json`, the accepted mathematical report,
the frozen certificates relevant to numerical statements, and every cited
record.  It is bound to evidence snapshot
`67a9ad102f9c06b2ad1eb8ba87fc50c7e8788ce28044350978f67f60278681dc`,
manuscript digest
`82323397713c1a4e2b0f6cabbf4c9f9b92e0451d318f396c0823c94fcdde45c8`,
and PDF digest
`ff88f4f1cd608d26134d5ed87844085916170e844a65e79d7fa88364cf8396f9`.

The `$citation-check-skill` was explicitly invoked as an advisory two-pass
check.  Extraction was completed before verification.  Searches and primary
record inspections were performed on 2026-09-09.  The user-designated workbook
record documented in `literature/user_bibliography_check.md` is authoritative
for the Zeng--Liu--Ratnavelu--Huat metadata
(`metadata_basis=user_designated_workbook`); the accessible official
Preprints record independently matched it.

## Pass 1: fixed claim extraction

No verification was performed while making this list.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Shallit proposed the displayed five-letter morphic word as a possible word avoiding consecutive factors with equal normalized Parikh vectors. | Attribution + existence | p.1, abstract |
| C02 | Weak abelian terminology is studied by Avgustinovich--Puzynina, and Fici--Puzynina provides general background on abelian combinatorics on words. | Attribution | p.1, Section 1 |
| C03 | Shallit proved a related construction on 16 letters, listed this five-letter morphism as a candidate, and reported being unable to prove it. | Attribution + statistic | p.1, Section 1 |
| C04 | For every starting position and positive lengths of total at most 2745, the two adjacent factors have unequal normalized Parikh vectors; any counterexample has total length at least 2746. | Existence + statistic | pp.1--3, Theorem 1 and proof |
| C05 | The finite word `h^4(0)` has length 38,416, and the exhaustive check completed 38,415 splits and 737,875,320 intervals on each side without a match. | Statistic + existence | pp.1, 3 |
| C06 | Exact finite certificates also occur in explicitly finite discrete-geometric library problems, with Zeng et al. as a methodologically related example. | Attribution + existence | p.3 |
| C07 | The argument supplies no reduction for total lengths above 2745 and does not itself decide the infinite avoidance property. | Existence / scope | p.3, Section 4 |
| C08 | Four named bibliographic records, with the displayed authors, titles, dates, venues or preprint status, and identifiers, exist. | Existence + temporal | p.4, References |

## Pass 2: verification

| ID | Evidence checked | Result | Confidence |
|---|---|---|---|
| C01 | Shallit, arXiv:2609.05780v1, Proposition 1 and Section 5; the local primary PDF gives the literal image `01213101314310` and the cyclic rule. | Verified | exact |
| C02 | arXiv:1302.4359 abstract studies weak abelian periodicity via equal letter frequencies; arXiv:2207.09937 describes itself as a survey of abelian combinatorics on words. | Verified | paraphrase |
| C03 | Shallit's abstract and Theorem 5 prove the 16-letter construction; Section 5 lists the size-5 image and says the candidate cyclic morphisms had not been proved by the author. | Verified | exact |
| C04 | The exact scope is the accepted claim in `claim.json` and `audit/math.md`; `evidence/short_factor_bound.md` proves the global embedding and the frozen exact certificate supplies the finite exclusion. | Verified | exact |
| C05 | `evidence/h4_collinearity.json` records length 38,416, 38,415 completed splits, 737,875,320 intervals per side, and no witness.  The prescribed-interpreter run of `evidence/verify_h4_certificate.py` returned `outcome: verified` with the same totals and word digests. | Verified | exact |
| C06 | Workbook row 9, reproduced in `literature/user_bibliography_check.md`, supplies the metadata.  The official Preprints page for manuscript 202608.1658 states the finite-library scope and exact distance-layer, symmetry-reduced, and maximum-clique certificates. | Verified | paraphrase |
| C07 | The accepted claim and proof stop at the two-level-3-block bound 2745.  The manuscript now says only that this note does not resolve the infinite problem; it makes no current-open-status or priority claim. | Verified | exact |
| C08 | arXiv primary records 2609.05780, 1302.4359, and 2207.09937, the journal/DOI metadata exposed by the latter records and DBLP/author repository records, and the official Preprints page all match the rendered bibliography. | Verified | exact |

## Claim-to-source details

- **Shallit (2026).** The arXiv record confirms Jeffrey Shallit, the title,
  submission date 5 September 2026, version 1, and arXiv identifier.  The local
  primary PDF (SHA-256
  `7b3b9e7193c9ddcf4bcb6efe3f32118bb8dfd05836ab0521a0134ffb803d8288`)
  was inspected at PDF pp.2 and 6--8.  Those pages support the exact geometric
  equivalence, the 16-letter theorem, and the stated five-letter proposal.
- **Avgustinovich--Puzynina (2016).** The arXiv primary record and journal
  metadata agree on authors and title; the journal record is *Theory of
  Computing Systems* 59(2), 161--179 (2016), DOI
  `10.1007/s00224-015-9629-1`.  The abstract directly supports only the
  restrained terminology statement made in the manuscript.
- **Fici--Puzynina (2023).** arXiv:2207.09937v2 and the University of Palermo
  record agree on authors, title, *Computer Science Review* 47, article
  100532, and DOI `10.1016/j.cosrev.2022.100532`.  Its abstract directly
  supports the survey description.
- **Zeng et al. (2026).** The authoritative workbook row and the official
  Preprints page agree on all four authors, title, August 2026 posting,
  preprint status, and DOI `10.20944/preprints202608.1658.v1`.  The citation is
  used only for the finite-certificate methodology actually described by the
  source, not for the weak-abelian theorem or novelty.

The bounded comparison search used each citation's author/year/title, full
title with arXiv/Semantic Scholar filters, author/year/venue, DOI where
available, and arXiv identifier where available.  Separate searches for the
literal morphism, arXiv identifier, and manuscript title found no later
equivalent result, but the manuscript makes no priority or current-open-status
claim, and this negative search is not presented as proof of novelty.

## Dependency and rendered-reference checks

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`.  Inspection of `main.tex` and `main.fls` found no
authored imports, local style files, figures, or other source dependencies.
All four citation keys used in the TeX occur exactly once in the bibliography,
BibTeX generated all four entries without warnings, and the extracted and
rendered PDF contains references [1]--[4] with resolved links and no placeholder
or undefined marker.  No citation is contradicted, misleading, or removable
without also removing its restrained contextual purpose.

## Verdict

**Accept.** All substantive citations and numerical attributions are supported
at the scope used, the user-designated bibliography metadata is preserved, the
publication dependency scope is complete, and no citation limitation remains.
