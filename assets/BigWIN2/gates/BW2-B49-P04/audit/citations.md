# Fresh citation and bibliography audit

## Method and scope

I used the required two-stage, non-interactive procedure.  The first pass
extracted and froze five claim/citation pairs in
`audit/citation-claim-ledger.json` without verification.  The second pass used
that fixed ledger and recorded source-level results in
`audit/citation-verification.json`.  No subagents were used because the runner
explicitly prohibited agents and background workers; each reference was
therefore checked serially under the same per-reference protocol.

The audit covers both publication inputs, `manuscript/main.tex` and
`manuscript/references.bib`, and every one of the four cited BibTeX keys.  The
search date was 2026-09-07.  No `literature/bibliography-revision-*.md` or
`literature/crossref-*` captures exist in this project; that absence was
enumerated before manuscript editing.  Live primary pages were available, so
no source is being declared unavailable.

## Fixed claim-to-source verification

| Claim | Key | Exact source location | Result |
| --- | --- | --- | --- |
| C01: two selected cards suffice, and the one-card parent criterion | `Ivanov2026` | Official frozen arXiv PDF, Theorem 2.2 and Proposition 2.4, p. 2 | Verified (paraphrase) |
| C02: the source constructs `J_m` and proves `J_m-pw` identifies it for `m >= 4`, without the all-edge classification | `Ivanov2026` | Official frozen arXiv PDF, Figure 4 and Proposition 5.2, p. 5; concluding scope, p. 6 | Verified (paraphrase) |
| C03: the multiplicity-isolated weighted-core criterion reconstructs proper trees from the chromatic symmetric function | `Zeng2026Multiplicity` | Official arXiv abstract, sentences 3-5 | Verified (paraphrase) |
| C04: Bose and Hurtado treat planar edge flips systematically | `BoseHurtado2009` | Elsevier publisher abstract and record, *Computational Geometry* 42(1), 60-80 | Verified (paraphrase) |
| C05: the finite implementation uses NetworkX 3.4.2 | `HagbergSchultSwart2008` | Primary proceedings paper, pp. 11-15, plus local `networkx.__version__` check | Verified (exact version from runtime; citation supports the software identity) |

The authoritative records are the official arXiv pages for 2609.02389 and
2608.18179, the Elsevier record for DOI
`10.1016/j.comgeo.2008.04.001`, and the authors' SciPy 2008 paper together with
the official NetworkX citation record.  Title, authors, year, venue/version,
and the nearby substantive support all agree with the retained BibTeX.  No
BibTeX replacement or citation-key change was needed.

## Coverage and relevance

The four-reference bibliography is not user-library-only.  Each retained item
has a distinct necessary role:

- Ivanov is the problem-origin and closest-prior-result source, and supplies
  the exact parent criterion and the previously known `pw` witness.
- Bose--Hurtado is the primary survey source for the nontrivial diagonal-flip
  method used to build every rival.
- Hagberg--Schult--Swart documents the NetworkX software used by the disclosed
  exact boundary verification.
- Zeng row 17 is the single genuinely relevant item from the active 49-entry
  user library.  It directly supports the adjacent contrast with invariant
  reconstruction; no second library record supports a natural nearby claim.

The Zeng selection is checksum-bound to the active registry, workbook snapshot,
sheet, row, attempt 1, and launch ID in
`audit/user-bibliography-selection.json`.  Its final key has an ordinary
body-flow direct `\cite{Zeng2026Multiplicity}` at lines 67-72 and resolves only
through `manuscript/references.bib`.  Adding more library items would be
citation padding.

The elementary planar-triangulation facts used inside the self-contained proof
do not require a further specialist source.  The manuscript does not claim
priority: it reports only a bounded search and explicitly distinguishes the
new all-edge classification from Ivanov's single-witness proposition.  The
source supports that comparison.  No unsupported strengthening of the accepted
mathematical statement was found.

## Mechanical consistency

The bibliography checker found four cited keys, four BibTeX entries, no missing
or unused entries, and exact agreement with the final `.aux`.  The converged
`.log` and `.blg` contain no undefined citation, missing database entry,
duplicate entry, BibTeX warning, or unresolved cross-reference.

**Verdict: accept.**  All five fixed claim/citation pairs and all four records
are verified, coverage is appropriate, and there are no unresolved citation
blockers.
