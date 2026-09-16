# Citation and bibliography audit

## Result

**PASS.**  Release attempt 3 used a two-pass search-mode audit: five claim
instances were frozen before verification, with no re-extraction during the
second pass.  All five are supported by inspected primary records or exact
source passages.  The union of their direct keys is exactly the four ordinary
body-flow keys in `manuscript/main.tex`; all four resolve in
`manuscript/references.bib` and in the converged `.aux`/`.bbl` output.

| Claim | Key | Nearby assertion | Primary support | Status |
|---|---|---|---|---|
| CIT-001 | `Garcia2026` | two-attachment results at orders 4, 6, 8, and 10 | arXiv:2609.04686v1, printed p. 7, Proposition 6.2(2) | Verified, exact |
| CIT-002 | `Meringer1999` | orderly generation and canonicity testing | Publisher record and author-hosted journal PDF, abstract and Sections 1--3 | Verified, paraphrase |
| CIT-003 | `Meringer1999` | exactly 85 connected cubic graphs on 12 vertices | Journal PDF, Table 1, row `n=12`, `k=3`, `Graphs=85` | Verified, exact |
| CIT-004 | `MeringerCensus` | official adjacency-list census | Official Bayreuth `12_3_3` census page and its adjacency-list link | Verified, exact |
| CIT-005 | `ZengEtAl2026` | independent reconstruction outside the generator trust boundary | Preprints.org version 1, Section 6 | Verified, paraphrase |

## Bibliographic records

All four cited works exist.  Author, title, year/version, venue or resource
type, and the available DOI/arXiv/URL identifiers agree with the primary
records.  The verified Wiley DOI was added to `Meringer1999`; no entry or cite
key was changed, and `manuscript/main.tex` required no edit.  The canonical
bibliography has four cited entries, no uncited entries, no duplicates, and no
undefined keys.  The selected user-library entry is registry row 9 and retains
the final key `ZengEtAl2026`; its DOI and primary Preprints.org record were
verified independently of registry metadata.

## Coverage and relevance

The bibliography is not library-only.  Garcia is the problem-origin and
closest-prior gadget source.  Meringer's journal paper is the primary method and
count source, and his official census page is the finite-classification data
source.  The one selected user-library paper has a narrow methodological use in
ordinary body flow.  A second library paper would be decorative, so the bound
selection remains one item with an explicit explanation in
`audit/user-bibliography-selection.json`.  The paper asserts no publication
priority; its order-12 comparison is bounded to the inspected Garcia source.

The manuscript's own theorem, reduction, certificate counts, and verifier
description are supported by the frozen accepted mathematical evidence rather
than being attributed to external literature.  Census exhaustion remains
openly identified as an external classification dependency.

## Dependency and build checks

The complete authored publication dependency set is
`manuscript/main.tex` and `manuscript/references.bib`; there are no imported
figures, local styles, or included TeX files.  The rendered PDF contains all
four numbered references and resolved in-text citations.  The final clean
BibTeX build and the key checker report zero missing, unused, or `.aux`-mismatched
keys.  Source locations and structured second-pass results are preserved in
`audit/source-locations.json` and `audit/citation-verification.json`.

The academic-citation search templates were run for each paper, including
author/year/title, exact-title, author/year/venue, and DOI or arXiv identifier
queries where applicable.  The user prohibited agents and background workers,
so the per-reference audit was completed serially under the same primary-source
protocol.  No official-verification blocker remains.
