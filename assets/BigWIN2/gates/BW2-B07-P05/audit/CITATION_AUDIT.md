# Citation and novelty audit

Audit date: 2026-08-30 UTC.

## Source-by-source checks

| Key | Metadata check | Claim support | Result |
|---|---|---|---|
| ComellasYebra2002 | EJC publisher record; DOI 10.37236/1623; vol. 9 (2002), R6 | pp. 4 and 6 give the local \(n=10\) analysis and exact point table/lower bound | PASS |
| MonjiModirKocuk2025 | arXiv:2512.14505v1; title/authors checked against the primary PDF | pp. 2 and 16--17 state that \(n=10\) has no optimality certificate; Conjecture 1 records the unproved edge pattern | PASS |
| SudermannMerx2026 | arXiv:2603.11107v2, dated 2026-05-22; title/author checked against primary PDF | §7 leaves \(n=10\) certification open; Appendix A, pp. 18--19, gives exact \(n=10\) coordinates | PASS |
| TheoremDB2026 | statement P2798 and public record R376, snapshot date and access date recorded | supports only the prior public disclosure of the ordered-cell theorem; it is not used as a primary source for the 2002 construction | PASS with secondary-source label |

The source paper's displayed \(S_2,S_3\) formulas on p. 4 fail literal
substitution. The manuscript does not quote them as valid identities; it
derives the corrected determinants from the p. 6 point table and flags the
display issue.

## Bibliography integrity

The LaTeX audit reports cited=4, bib=4, missing=0, unused=0. All URLs resolve
to the publisher, arXiv, or the cited public research record. No secondary
summary is used for a mathematical theorem attributed to a primary paper.

## Novelty boundary

Opening and post-result queries are recorded in literature/search_log.md.
They found a public proof claim only on the ordered cell; they did not find the
full-cube theorem. The manuscript therefore says only that no earlier source
was found in the dated searches. It does not claim exhaustive priority.

Citation/novelty gate: **PASS**, subject to the explicitly bounded search
scope.
