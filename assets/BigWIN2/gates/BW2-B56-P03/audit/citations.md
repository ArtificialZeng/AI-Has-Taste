# Citation and bibliography audit

## Result

**Accept.** The final manuscript has six body-flow citation keys and six
canonical bibliography entries. Every key resolves in the final `.aux`; there
are no uncited entries, undefined citations, duplicate entries, or BibTeX
warnings. The audit used the mandated two stages: the 13 claim groups were
first frozen in `audit/citation-claim-ledger.json`, then verified without
re-extraction in `audit/citation-verification.json` against the exact source
locations in `audit/citation-source-locations.json`.

The user explicitly prohibited subagents, so the normally delegated
per-reference checks were performed serially in this fresh release context.
Searches used title, author/year/venue, DOI or arXiv identifier, and the exact
claim terms on 2026-09-07. Primary publisher, repository, arXiv, DOI, and SSRN
records were preferred. The frozen Rezaee--Saberi PDF was independently parsed
and checked at the cited theorem/family locations.

## Claim-to-source findings

| Key | Nearby claim | Exact source location | Status |
|---|---|---|---|
| `Rezaee2025` | conjectural necessary/sufficient criteria; colength-15 candidate and predicted dimension 81 | abstract; Conjectures A/B, pp. 4--5; Conjecture F, p. 9; table row 15, p. 10 | verified |
| `AscottRezaeeZhou2026` | exact stratum maxima 45, 69, 81 and bounded comparison | arXiv v2, Section 1.1 table, HTML lines 89--113, especially 101--102; Appendix A lines 114--121 | verified |
| `RezaeeSaberi2026` | theorem for three degree families and the uncovered length 15 | local primary PDF, families (0.1)--(0.3), pp. 2--3; Theorem 5.1, p. 17 | verified |
| `Taylor1966` | pairwise Taylor presentation relations | 1966 University of Chicago dissertation; displayed differential is stated explicitly and its use was reconstructed in the accepted math audit | verified |
| `EliahouKervaire1990` | stable-ideal presentation | Journal of Algebra 129 (1990), 1--25, DOI 10.1016/0021-8693(90)90237-I | verified |
| `Zeng2026SSRN7385138` | exhaustive canonical input, exact arithmetic, independent reconstructor in another finite monomial-algebra problem | official SSRN abstract, DOI 10.2139/ssrn.7385138 | verified |

The negative comparison for Ascott--Rezaee--Zhou is bounded correctly: the
paper prints the length-15 numerical entries, while its appendix prints an
illustrative length-35 call; it does not print a complete length-15 atlas or
all equality cases.

## Coverage and repairs

The bibliography covers the problem-origin conjecture, the closest exact
computational comparison, the nearest theorem, both nontrivial presentation
methods, and one directly relevant active-library verification analogue. It is
therefore neither Excel-only nor user-library-only. No retained source is
decorative.

Two release repairs were made: `Taylor1966` was added at the method claim, and
the library key `Zeng2026WLP` was normalized to the registry source key
`Zeng2026SSRN7385138`. The final SSRN entry is formatted as a preprint so the
plain BibTeX style converges without an empty-journal warning.

Mechanical audit command:

`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux`

Result: 6 cited keys, 6 bibliography keys, zero missing, zero uncited, and
exact agreement with the final auxiliary file.

Scope: the cited literature supports the stated origin, closest comparisons,
and methods. The new maximum and equality classification are supported by the
accepted frozen mathematical audit rather than by literature. No priority
claim beyond the bounded comparison, and no non-Borel conclusion, is made.
