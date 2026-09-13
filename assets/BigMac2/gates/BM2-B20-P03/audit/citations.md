# Fresh citation audit

## Binding and method

- Release job: `bigMac-00020-p03-release-c9a19d6ffd27`
- Evidence snapshot: `ba716a810c205d214da52cc5b993cc6650f9d7be715542223f01b7730d054ed1`
- Manuscript snapshot: `bd015dc13f52987325070cf4e693b435b741af53cfb4ca39b5833614c783acac`
- PDF SHA-256: `26b9137506abf8974f01d8805d27f89cd4d89d54d67312fbb31aabe629b8257c`
- Generated: `2026-09-09T03:34:33+08:00`

The requested `$citation-check-skill` was applied as an advisory two-pass
search audit. The pass-1 extraction below was fixed before pass 2. The audit
also inspected the user-designated hash-matching arXiv v1 PDF directly.

## Pass 1: fixed claim extraction

| ID | Claim | Type | Location |
| --- | --- | --- | --- |
| C01 | Jones and Kinnersley introduced the directional localization game. | Attribution / existence | p. 1, abstract and section 1 |
| C02 | They proved \(\zeta_d(Q_n)\in\{n,n+1\}\) for every positive integer \(n\). | Attribution | p. 1, abstract and section 1 |
| C03 | They asked for the exact directional localization number of hypercubes. | Attribution | p. 1, abstract and section 1 |
| C04 | Corollary 3.9 implies \(\zeta_d(Q_3)\ge 3\). | Attribution / exact inference | p. 2 |
| C05 | The three-dimensional case is the first slice not already decided in the cited paper. | Comparative / existence | p. 1 |
| C06 | The computations cover 255 nonempty beliefs, 512 ordered actions, and 3,472 replayed strategy-answer fibers, with six unresolved transitions. | Statistics / existence | p. 3 |

## Pass 2: claim-to-source verification

| ID | Status | Evidence and support | Confidence |
| --- | --- | --- | --- |
| C01 | Verified | The official arXiv record and the local v1 title page/abstract state that the paper introduces this game. | exact |
| C02 | Verified | Corollary 3.9 on supplied PDF page 15 states the bracket for every positive integer \(n\); the partial-feedback parameter and hypotheses match. | exact |
| C03 | Verified | Question 6.1 on supplied PDF page 29 asks for \(\zeta_d(Q_n)\). | exact |
| C04 | Verified | Substitution of \(n=3\) in Corollary 3.9 yields the cited lower bound. | interpretation |
| C05 | Verified | The proof of Corollary 3.9 gives \(\zeta_d(Q_1)=1\), Proposition 2.2(iii) gives \(\zeta_d(Q_2)=\zeta_d(C_4)=2\), and Question 6.1 leaves the general hypercube value open. | interpretation |
| C06 | Verified | `evidence/solver_report.json` and `evidence/replay_report.json` contain the exact displayed counts; the accepted mathematical audit records the same values. | exact |

Summary: 6 claims extracted; 6 verified; 0 numerical errors; 0
unverified, hallucinated, or misleading claims.

## Bibliography, search, and dependency findings

- The designated primary PDF has SHA-256
  `1f1ac4c3c0a1313003b326c5c98cad06253482beaecfdbd14f7f0fd6c2a67d58`,
  matching `source.md` and `literature/user_bibliography_check.md`. Its title
  page confirms John Jones, William B. Kinnersley, the title,
  `arXiv:2609.01745v1 [math.CO]`, and 1 September 2026.
- The official arXiv record corroborates the authors, title, identifier,
  category, date, and v1 status. Metadata basis is
  `metadata_basis=user_designated_bibtex_and_source_record`, corroborated by
  that refresh and the primary PDF. The supplied record has no DOI, so none
  was invented.
- All applicable academic search templates were run: author/year/title words;
  exact title restricted to Semantic Scholar or arXiv; author/year/venue; and
  the arXiv identifier. A DOI query was inapplicable. The bounded search does
  not establish priority, and the manuscript makes no exhaustive priority
  claim.
- The immutable source's page-14 locator for Corollary 3.9 is one page early:
  the corollary starts on supplied PDF page 15. The manuscript cites the
  theorem label rather than the incorrect page, so no manuscript repair is
  needed.
- Sorted `publication.json` sources are exactly `manuscript/main.tex` and
  `manuscript/references.bib`. Both were checked in full. The recorder and
  BibTeX evidence show no undeclared authored TeX, style, figure, or database
  dependency. The rendered PDF has two resolved in-text citations and one
  readable reference entry; there is no undefined key.
- The sole bibliography entry is genuinely relevant and supports only the game
  context, hypercube bracket/lower bound, and open-question provenance. The
  new \(Q_3\) strategy is proved directly rather than attributed to it.

## Verdict

**ACCEPT.** Citation existence, supplied and refreshed metadata, exact nearby
support, bounded comparison language, dependency scope, and rendered references
pass. No citation-access limitation remains.
