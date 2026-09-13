# Writing evidence

Job: `bigMac-00006-p03-write-8f1871c215ee`.

The writing precondition `release_gate.py check-math` passed. The accepted
claim, mathematical audit, and all frozen evidence were inspected. The central
claim is unchanged: the exact coefficient 25056 disproves only the frozen
k=2 congruence at n=1. The source's k=4 conjecture is unaffected. No claim of
priority or exhaustive literature coverage is made.

Both original coefficient programs were executed successfully. The sparse
program's full output is saved in `evidence/write-coefficient-check.txt`.

## Bibliography basis and citation limits

`literature/user_bibliography_check.md` is now present. It supplies the
authoritative workbook entry from `数学主表!A40:F40`, including the DOI
10.2139/ssrn.7380519, and a narrow methodological relevance assessment.
The supplied BibTeX record is retained verbatim in `manuscript/references.bib`.
It is cited only for the comparison of generating-function coefficient analysis
with independent exact finite diagnostics. No partition identity, congruence,
monotonicity theorem, threshold, or proof method beyond that supplied relevance
assessment is attributed to it. The proof of the counterexample is self-contained.

On 2026-09-08, web refresh requests to the DOI resolver, Crossref API, and SSRN
landing page did not return usable records. An exact-title search returned no
relevant record. Status: **external refresh unavailable**. This does not alter
the authoritative supplied metadata or imply that the article is nonexistent.
The earlier Crossref match dated 2026-09-07 is recorded in the supplied check;
it was not independently reproduced in this writing job. The complete paper
was not available for inspecting stronger attributions.

The motivating paper's arXiv abstract and version-1 HTML were accessible:

- https://arxiv.org/abs/2609.03926
- https://arxiv.org/html/2609.03926v1

The arXiv record confirmed the authors, title, and initial submission date.
Version-1 equation (1.2) and Conjecture 7.1 were inspected directly and agree
with the accepted audit; the latter lists the k=4 congruence. The bibliography points specifically to version 1, avoiding ambiguity
with the later version linked by the unversioned abstract page.

The bibliography uses installed biblatex/Biber. Its article entry is rendered
with the generic bibliography driver to avoid inventing a journal for the
workbook's SSRN record; the source entry type and all supplied fields are kept.

## Build and handoff

A clean four-command build (pdflatex, Biber, pdflatex twice) succeeded with
all return codes zero. The exact commands and complete transcript are saved in
`evidence/write-build-commands.json` and `evidence/write-build-transcript.txt`.
The final TeX and Biber logs contain no warnings, undefined citations, missing
references, overfull boxes, or underfull boxes. No package was installed.

The final PDF is `manuscript/main.pdf` (three pages). Text was extracted to
`evidence/write-pdf-text.txt`; every page was rendered under
`evidence/write-render/` and visually inspected during this writing job.
The proof, parameter caveat, author details, assistance disclosure, both
bibliography entries, and DOI are legible without clipping or overlap.
The first two pages contain the statement and proof; the third contains the
assistance disclosure and complete references. The authoritative workbook entry
was compared verbatim with the BibTeX source. All frozen input hashes still
match the accepted mathematical snapshot.

`publication.json` enumerates the TeX source, BibTeX database, generated BBL
input, and final PDF path. `evidence/write-validation.json` records the writing
self-check and PDF hash. These are writing checks, not a fresh release audit.
`release_gate.py freeze-manuscript` succeeded. Its exact output is in
`evidence/write-freeze-result.json`, and the generated binding is in
`audit/manuscript-snapshot.json`. The next step is a separately assigned
citation/build/visual release review; no released-deliverable verdict is
asserted by this writing job.
