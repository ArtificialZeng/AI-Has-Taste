# Citation and bibliography audit

Verdict: **accept**.

Audit date: 2026-09-06.  Method: two-pass primary-source manual audit under
`citation-check-skill`, followed by the deterministic BibTeX key checker.  The
explicit job constraint prohibited subagents, so all three keys were checked
serially in this release context.  The frozen extraction is
`audit/citation-claim-ledger.json`; this report is the separate verification
pass and does not re-extract claims.

## Source and passage verification

| Key | Primary record and exact source location | Nearby claims | Result |
|---|---|---|---|
| `GerberNorton2026` | Official arXiv record `https://arxiv.org/abs/2609.03738`; frozen v1 PDF `bigWin-43-materials/2609.03738.pdf`: Section 2.2 and equation (2.1), pp. 12--13; Definition 2.8 and Lemma 2.11, p. 14; Conjecture 3.10, p. 33; Theorem 5.6/Table 2, pp. 42--43; equation (5.3) and its following sentence, p. 44. | C01, C03--C07 | Verified, exact/paraphrase.  Authors, title, date, arXiv identifier, definitions, hypotheses, weighted identity, and the expressly conjectural status of both individual series all match. |
| `ChanOh2012` | Official arXiv record `https://arxiv.org/abs/1208.6060`; frozen v1 PDF `bigWin-43-materials/1208.6060.pdf`: coset/genus definitions in Section 4, pp. 12--13, and Theorem 4.9(1), p. 15. | C02, C08 | Verified, exact/paraphrase.  Part (1) assumes a positive-definite quadratic space over a totally real field, genus representation, and dimension at least five, and concludes fixed-coset representation above a coset-dependent norm bound.  It has no primitivity hypothesis.  The theorem gives existence of a constant, not a usable constant for this application. |
| `Zeng2026MultiplicityArxiv` | Official arXiv record `https://arxiv.org/abs/2608.18179`, especially the final two abstract sentences.  Active user-library row 17 has the same title, author, year, identifier and DOI. | C10 | Verified, paraphrase.  The abstract states that the work supplies a canonical integer-partition model and exact cut-partition implementation while the unrestricted diameter-six case remains open.  The manuscript carefully labels the comparison as a pattern in a different setting. |

The required academic-citation search variants were run for every key: author,
year and title words; full title restricted to arXiv; author/year/venue; and DOI.
The official arXiv records were located in each case.  There were no saved
`literature/crossref-*` captures or `literature/bibliography-revision-*` leads
in this project to parse.  DOI-only evidence was not used for claim support.

## Frozen claim decisions

Claims C01--C08 and C10 are verified by the exact passages above.  C09 is
verified exactly by `evidence/level-rank-lattice-n100.txt` and
`evidence/exact-coefficients-n40.txt`: both zero lists are empty through 100,
and the independent enumerations agree on `0 <= n < 41`.  C11 is a provenance
and method disclosure consistent with the frozen integer-arithmetic scripts;
it is not used as mathematical evidence.  No numerical mismatch,
hallucination, misleading citation, unsupported strengthening, or unresolved
citation was found.

## Bibliography integrity and coverage

The manuscript contains six ordinary body-flow citation occurrences using
three distinct keys.  All keys occur exactly once in
`manuscript/references.bib`, all three entries are used, and the final `.aux`
contains precisely those keys.  Official arXiv records agree with the current
titles, authors, years and identifiers, so no BibTeX replacement or key change
was necessary.

Coverage is adequate without padding.  Gerber--Norton is the primary problem
origin and closest prior status; Chan--Oh is the decisive non-library method
source; Zeng row 17 is the sole relevant active-library item and supports only
the narrow methodological comparison.  The finite-field reduction and Hensel
lifts are displayed as standard proof steps rather than attributed novelty.
No other user-library record naturally supports a manuscript claim.

Mechanical check:

`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py main.tex --aux main.aux`

reported 3 cited keys, 3 bibliography keys, zero missing/unused keys and exact
agreement with the `.aux`.  The final `main.log` and `main.blg` contain no
undefined citation/reference, missing database entry, duplicate entry, LaTeX
error, or fatal diagnostic.

