# Fresh citation audit

## Binding and method

This release audit is bound to mathematical snapshot
`413f5c03360234d737d20f93f903d94a9e4c26eeddf3b27781609cb6e3077d6d`,
manuscript digest
`4a1028cc3fd0bec2bc05b44680917562548a3cf013a2a1ebc9353989ce504004`,
and PDF digest
`56d56ae31af8c465b707fb7a624bff35e8feafdb58bdbb3939ed5197fa0702e2`.
I explicitly applied `$citation-check-skill` as an advisory two-pass check.  The
user-designated workbook record remains authoritative where an external refresh
is unavailable; the skill does not override that record.

## Pass 1: fixed citation-dependent claims

- **C1 (Section 1):** Ascoli et al. give general vertex-minor Ramsey bounds and
  a related polynomial-growth conjecture.
- **C2 (Section 1 and abstract):** Bae proves
  `R_vm(5) >= 13`, conjectures `R_vm(5)=15`, and supplies the convention under
  which the present witness yields `R_vm(5) >= 14`.
- **C3 (Section 1):** the dated, targeted searches found no equivalent explicit
  construction; this is expressly neither priority nor an exhaustive review.
- **C4 (Section 4):** Zeng--Liu--Ratnavelu--Ong is cited only as an unrelated
  methodological example using exact finite certificates and independent
  integer verification.
- **C5 (Section 4):** Zeng's eight-vertex whiskered-graph work is cited only as
  an unrelated methodological example using canonical graph enumeration,
  graph6 representatives, and a separate verifier.

No other bibliography-dependent claim was extracted.  The theorem and exact
counts are bound to the accepted mathematical evidence rather than inferred
from bibliography entries.

## Pass 2: verification

| Claim | Source and check | Result |
|---|---|---|
| C1 | Current arXiv record `2602.09049v2`, checked 2026-09-09, gives the authors/title/version, defines `R_vm(k)`, proves the stated general bounds, and states the polynomial-growth conjecture. | Verified; the manuscript paraphrase is narrower than the abstract. |
| C2 | Current arXiv record `2604.13434v1`, checked 2026-09-09, gives Ji Ho Bae/title/version and explicitly states `R_vm(5) >= 13` and the open question whether `R_vm(5)=15`.  The lower-bound consequence is also stated conservatively and is consistent with the accepted claim. | Verified. |
| C3 | `evidence/literature_registry_check.md` records the date, searched primary records, notation/string/code queries, and the limitation.  The PDF repeats the limitation and makes no priority claim. | Supported at its explicitly bounded scope. |
| C4 | `literature/user_bibliography_check.md`, extracted from the user-designated worksheet `数学主表`, supplies the title, authors, year, venue, DOI, abstract-level method description, and relevance boundary.  DOI refresh was unavailable in this bounded context. | Accepted from user record; nearby prose stays within the supplied method description. |
| C5 | The same user-designated workbook extraction supplies the title, author, year, publisher, DOI, method description, and relevance boundary.  DOI refresh was unavailable in this bounded context. | Accepted from user record; nearby prose stays within the supplied method description. |

The metadata basis for C4--C5 is
`metadata_basis=user_designated_workbook`; external refresh unavailable in
scope.  This is not treated as evidence for the vertex-minor theorem, novelty,
or priority.  The two direct arXiv records were freshly reachable and their
displayed metadata and abstracts support C1--C2.  All four numbered references
appear in the extracted PDF and all in-text references resolve.

`publication.json` lists the sole compiled authored dependency
`manuscript/main.tex`.  Its bibliography is inline, and inspection of the TeX,
compiler recorder, extracted PDF, and absence of imported local figures/styles
found no omitted authored compilation dependency.  There are no undefined
citations or cross-references.  Verdict: **accept**.
