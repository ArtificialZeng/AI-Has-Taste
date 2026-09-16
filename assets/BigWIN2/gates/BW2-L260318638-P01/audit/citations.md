# Citation and bibliography audit

Verdict: **accept**.

This audit is bound to release job `lit-260318638-p01-release-5d1f71735d61`, citation attempt 3, launch `1ea1d811-4fa9-44ad-98fe-7948e10e102b`, accepted mathematical snapshot `1da216e17f600af5b3e7cd608dee41b0b7705ffc99ad85271bf205274989b640`, manuscript digest `297be95a6b49fbc13d480f090b229c5d3b90a7a89e50cd4f401173a6ff21d50f`, and PDF digest `edbcd7c26bc7bf3acf798cf17c166ce4aae16a75ee7a0ff99c9d110d5726beb6`.

## Method and scope

The audit used two non-interactive stages. First, every substantive citation-bearing claim in the complete canonical `manuscript/main.tex` was extracted into `audit/citation-claim-ledger.json` before independent source checking. The ledger contains nine uniquely identified claims with precise line locations; the union of their keys is exactly the four ordinary body-flow citation keys. Second, each claim was checked against a primary record and an exact supporting passage, independently of the first-stage extraction. The passage-level results are recorded in `audit/citation-verification.json`.

The user explicitly prohibited sub-agents, so the four per-reference checks were performed sequentially in this release context under the same claim-level protocol.

All three publication source files were reviewed: `manuscript/main.tex`, `manuscript/references.bib`, and `manuscript/verify_c45_domino_layer.py`. The bibliography and auxiliary file contain the same four keys as ordinary body flow. There are no undefined citations, unused entries, hidden-only citations, decorative references, or omitted publication dependencies.

For each reference, every applicable academic search template was replayed after the attempt-3 claim ledger was frozen: author/year/title, exact title on a primary domain, author/year/venue, DOI where present, and arXiv identifier where present. Official arXiv, Springer, Cambridge University Press, and Preprints.org records were used for bibliographic identity and version status. Exact passages were checked in the official full text or a stable primary-text copy. The two locally preserved primary PDFs were independently hashed. No bibliography metadata repair or citation-key change was necessary.

No `literature/` directory or supervisor-supplied `bibliography-revision`, `handoff`, or Crossref-capture file exists in this project. This was checked before declaring the source set complete. A failed WSL retrieval of one book-copy URL was not treated as evidence of absence: the official Cambridge record and the already indexed primary-text copy were checked instead.

## Claim-level findings

- **Eldridge et al. (2026), arXiv:2603.18638v1.** PDF page 1 supports the definitions and conventions in C01. Equation (2.1) on page 6 and Table 2 on page 12 support C03. Lemma 2.1 on page 7 supports C04. Theorem 1.2 and Table 1 on page 2 support the 17-tile construction in C07. The official arXiv record confirms title, authors, date, identifier, and that version 1 is current. Local source: `evidence/external/2603.18638.pdf`, SHA-256 `a58c8695b3be38b3e4aa8cb492f509d3d6cb565170fa38dd3bf87721d7d910df`.

- **Malen, Roldán, and Toalá-Enríquez (2023).** Section 6 and Theorem 6.4 of the official Springer full text support C02, C05, and C06: the initial domino and layer construction are defined there, and the relevant members are uniquely extremal up to symmetry/isometry. Springer confirms the journal record, pages 169--209, online publication date, and DOI. Local source: `evidence/external/2109.05331.pdf`, SHA-256 `5db9c997ea993a03d535ce7e58548cf45992b2e179f8d1b72a05e5214911adfe`.

- **Humphreys (1990).** Chapter 5, Section 5.3 and Corollary 5.4 support C08's method attribution: they construct the geometric representation of a Coxeter group and establish its faithfulness. Cambridge University Press confirms the monograph metadata, series, volume, year, and DOI.

- **Zeng et al. (2026), Preprints version 1.** Sections 6--7 of the official full text support the narrow methodological comparison in C09. They separate exact replay of finite certificate data from broader ambient mathematical questions. The official record confirms the version, authors, posting date, and DOI.

## User-library coverage and bibliography coverage

The active 49-record first-sheet user library was reviewed in full. Registry row 9, Zeng et al., is the only entry with a natural claim-level use and is selected in `audit/user-bibliography-selection.json`. Its smallest active citation-bearing sentence exactly matches ordinary body flow at lines 250--252 and passed the hook-compatible selection validator. Adding a second library record would pad the paper.

The library citation is not used as a substitute for primary subject literature. Ordinary body flow also cites the source paper for the problem and construction (Eldridge et al.), the closest prior extremal-animal theorem (Malen et al.), and the Coxeter-representation method source (Humphreys). Thus the bibliography is scholarly coverage of the claims actually made, rather than an Excel-only or library-only list.

## Outcome

All nine ledger claims are supported in the cited locations. All four retained bibliography records are real, correctly identified, and used for a nearby claim. The citation audit accepts with zero unsupported claims, zero undefined citations, zero metadata repairs, and zero citation-key changes.
