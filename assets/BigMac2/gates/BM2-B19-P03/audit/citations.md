# Fresh citation audit

## Scope and method

I reviewed the complete authored dependency set in `publication.json`, namely
`manuscript/main.tex` and `manuscript/references.bib`, and compared the
rendered reference list with the citations in the text. This audit used the
requested `$citation-check-skill` advisory workflow in two separate passes.
The search date was 2026-09-09.

## Pass 1: fixed claim extraction

- **C01 (existence/attribution, page 1):** Garcia's 2026 paper defines the
  window-calculus setting and relates the deposited `AGL(1,29)` base to the
  stated incident-edge orientation problem.
- **C02 (temporal/attribution, page 1):** Garcia reported the `p=29,31,37`
  orientation instances undecided; a bounded search on 2026-09-09 found no
  later version or separate exact resolution under the searched identifiers.
- **C03 (existence/attribution, pages 3--4):** Garcia's data archive is cited
  at DOI `10.5281/zenodo.22180583` and contains the fixed graph used by the
  checker.
- **C04 (attribution, page 1):** the Zeng record is used only for the narrow
  comparison that it separates non-finite reasoning from exact finite
  comparisons in a cycle-length problem.

The numerical theorem and certificate claims are not outsourced to these
citations. They are derived in the manuscript and bound to the accepted exact
evidence and mathematical audit.

## Pass 2: verification

- **C01--C02 — verified, paraphrase.** The current arXiv primary record for
  Daniel Garcia, arXiv:2609.04686v1, matches the author, title, date,
  identifier, subject, and DOI in the bibliography. Its abstract explicitly
  describes the exact window calculus and names the accompanying archive.
  The frozen primary-source screen in
  `evidence/literature_screen_2026-09-09.md` records inspection of Section 5,
  Lemma 5.2 and the following paragraph, including the statement that the
  `p=29,31,37` instances were left undecided. All required identifier/title,
  author/venue, DOI, and arXiv-ID searches were repeated in this release pass.
  The manuscript confines the novelty sentence to this bounded search and
  expressly disclaims priority and exhaustive coverage.
- **C03 — verified with disclosed access limit.** Garcia's arXiv record
  explicitly names DOI `10.5281/zenodo.22180583` as the archive for graphs,
  scripts, and certificates. Direct refresh of the Zenodo landing-page
  metadata was unavailable in this bounded context. The graph-member and
  archive bindings are checked locally against the frozen source and exact
  evidence; the manuscript makes no claim that depends on refreshed Zenodo
  metadata.
- **C04 — accepted from user record; external refresh unavailable.** The
  authoritative metadata basis is the user-designated workbook
  `Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`, as transcribed with workbook
  digest, sheet and row provenance in `literature/user_bibliography_check.md`.
  Searches by author/title, full title, venue, and DOI did not retrieve the
  exact external record. Under the user's authority rule, the supplied DOI
  and BibTeX fields are preserved (`metadata_basis=user_designated_workbook`).
  The workbook abstract supports only the narrow methodological comparison
  actually made. The text explicitly says this work supplies no premise for
  the theorem and is not prior work on the graph instance.

All three citation keys are defined and used. Biber found three citekeys; the
final PDF renders three complete numbered references with resolved links and
no missing-key marker. No attribution is contradicted, no unsupported
strengthening or priority claim remains, and both source files are necessary
and sufficient authored dependencies for this PDF.

## Verdict

**ACCEPT.** Citation scope is conservative and supported at the level used.
The unavailable metadata refreshes are disclosed; the user-designated
workbook controls the Zeng metadata and no unverified-citation exception is
needed solely for that failed refresh.
