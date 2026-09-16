# Fresh citation and bibliography audit

Mode: two-stage search verification with local primary-document replay.  Date:
2026-09-08.  Release job: `win-00072-p01-release-f1baba1908d6`; citation
attempt 2; launch `571fba5d-0eb9-428e-a63c-3d3229535d02`.

## Result

**Accept.**  `audit/citation-claim-ledger.json` froze fourteen substantive
claims before verification.  The union of its direct citation keys is exactly
the three-key ordinary body-flow citation set in `manuscript/main.tex`.
Every externally attributed claim is supported by the exact primary record or
passage cited below; the remaining finite mathematical claims agree with the
accepted audit and frozen exact reports.  No citation was added decoratively,
and no unsupported strengthening of the accepted theorem appears in the
manuscript.

The audit was performed locally because this bounded job expressly prohibited
subagents.  All applicable academic search templates were run for each of the
three keys, followed by inspection of the primary records rather than reliance
on search snippets.

## Pass 1: fixed claim surface

The attempt-bound UTF-8 schema-version-1 ledger records claim IDs C01--C14,
substantive text, types, exact current line intervals, and direct citation
keys.  It is bound to mathematical snapshot
`aa9d4e9c69acafe43ae93b50277cef413ba72d54831c6cc9c8fd13695634b5bf`
and manuscript digest
`7735ee700248b0c566773dd99d2f8a784acf750b297b2163ba5cf607fc0ee94c`.
No custom citation macro, `\\nocite`, comment-only citation, verbatim citation,
or hidden conditional contributes a key.

## Pass 2: primary-source verification

| Claims | Key or evidence | Exact source location and support | Status |
|---|---|---|---|
| C02--C03 | `GongWangWang2026` | Archived official arXiv v1 PDF, printed pp. 3--4, equations (3.1)--(3.3), derives the two reduced quartics and says coefficientwise equality is equivalent to system (3.3). Printed pp. 4--5, Theorem 3.1, gives `b=(1,16,8,36)`, `a=(4,9,16,32)` and order 61. Printed p. 7, Conclusion, asks for the minimum order and classification of positive solutions, so it supplies neither the lower-layer exclusion nor the layer-61 classification. | Verified, exact/paraphrase |
| C05 | `GongWangWang2026` plus dated search record | The official arXiv record at `https://arxiv.org/abs/2608.17311` lists only v1, submitted 18 August 2026. The fixed searches recorded in `literature/literature_search_2026-09-08.md` and the fresh title/author/identifier searches found no later version or separate exact least-layer treatment. The manuscript explicitly limits this to a dated bounded search and disclaims priority. | Verified as a bounded search report |
| C04 | `ZengEtAl2026FiniteCertificates` | Official Preprints.org v1 page, `https://www.preprints.org/manuscript/202608.1658`, abstract: the Borsuk and kissing-code conclusions are called finite-library theorems and are expressly said not to settle Borsuk's conjecture in dimension 4 or unrestricted kissing numbers in dimensions 5 and 6. This exactly supports the nearby scope-discipline comparison. | Verified, exact paraphrase |
| C10 | `deMouraBjorner2008` | Microsoft Research primary publication record, `https://www.microsoft.com/en-us/research/publication/z3-an-efficient-smt-solver/`, identifies Leonardo de Moura and Nikolaj Bjørner, TACAS, March 2008, and describes Z3 as an SMT solver supporting arithmetic and bit-vectors. DOI `10.1007/978-3-540-78800-3_24`, LNCS 4963, pp. 337--340, agrees with the canonical bibliography. | Verified, exact metadata and paraphrase |
| C01, C06--C09, C11--C14 | Accepted mathematical audit and exact local reports | `audit/math.md` independently reconstructs the composition count, signature equivalence, four ordered witnesses, modular-soundness bounds, solver exhaustion, and permitted orbit. `evidence/signature_join_61.json`, `evidence/z3_bv_verification_61.json`, and `evidence/independent_verifier_comparison.json` give the exact counts, versions, models, bounds, and fail-closed agreement stated in the manuscript. | Verified against frozen primary evidence |

The official arXiv record gives the problem paper's exact authors, title,
subject, date, and v1 status.  Its archived official PDF has SHA-256
`583250e3cb9e80c5177343cc2ad9b1580c050be2caaf9ce0122b97b9df2d4b84`.
The official Preprints.org record gives the selected library paper's title,
four authors, version 1, submission date 21 August 2026, posting date 24 August
2026, and non-peer-reviewed status.  The Microsoft Research record and the DOI
publisher metadata agree on the Z3 title, two authors, venue, year, volume,
pages, and DOI.

## Bibliography audit and coverage

| Final key | Current title | Authoritative title/source | BibTeX replaced | Key changed | Uncertainty |
|---|---|---|---|---|---|
| `GongWangWang2026` | *The Distance Spectrum Does Not Determine Bipartiteness* | Same; official arXiv:2608.17311v1 | No; all retained fields agree | No | None |
| `deMouraBjorner2008` | *Z3: An Efficient SMT Solver* | Same; Microsoft Research/Springer DOI record | No; all retained fields agree | No | None |
| `ZengEtAl2026FiniteCertificates` | *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes* | Same; official Preprints.org v1 record | No; all retained fields agree | No; the final scholarly key intentionally differs from source key `202608.1658` | None |

Bibliographic coverage is proportionate to the paper's actual dependencies.
The Gong--Wang--Wang paper is the non-library primary problem origin and closest
prior result; the de Moura--Bjørner paper is the natural non-library method
source for Z3/SMT; and the selected user-library paper supports the one narrow
finite-domain/ambient-domain comparison.  Elementary stars-and-bars counting
and the manuscript's self-contained signature calculation require no external
source.  Adding further references would not support a currently asserted
dependency.

All 49 active first-sheet registry records were screened.  Row 9 is the single
natural gate-bound selection.  Its DOI, primary record, exact supporting
abstract passage, literal current manuscript context, and ordinary body-flow
`\\cite{ZengEtAl2026FiniteCertificates}` are bound in
`audit/user-bibliography-selection.json`.  A second library record would be
padding: none is otherwise used for the P4/paw origin, least-layer comparison,
or SMT method.

## Mechanical checks

The bibliography checker reports three cited keys, three BibTeX keys, no
missing bibliography file, no missing or unused entry, and exact equality with
the final AUX citation set.  The converged `main.log` and `main.blg` contain no
undefined citation/reference, missing database entry, repeated entry,
BibTeX warning, LaTeX error, fatal stop, undefined control sequence, runaway
argument, overfull box, or underfull box.  No unresolved citation remains.
