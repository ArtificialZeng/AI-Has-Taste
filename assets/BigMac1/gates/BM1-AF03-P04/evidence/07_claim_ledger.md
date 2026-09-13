# Claim ledger

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | The cited paper exists with authors Arkady Berenstein, Jacob Greenstein, and Jian-Rong Li. | exact, verified | arXiv:2602.02342v2 | arXiv metadata, title page | high | Source attribution is sound. |
| C02 | The latest public arXiv version as of 2026-08-29 is v2, dated 2026-02-08. | exact, verified | arXiv abstract/version history | lines 8, 21, 23--27 of the HTML record | high | The current statement must use v2 numbering. |
| C03 | The general transitive-array statement is Conjecture 1.4 in v1. | exact, verified | arXiv:2602.02342v1 | p. 5, Conjecture 1.4 | high | The user's numbering is historically correct for v1. |
| C04 | The same statement is Conjecture 1.5 in v2. | exact, verified | arXiv:2602.02342v2 | p. 5, Conjecture 1.5 | high | Record a version correction without changing the mathematics. |
| C05 | The transitive CYBE is the three-commutator identity for \(c'\in\{c,c''\}\). | exact, verified | arXiv:2602.02342v2 | equation (1.5); source lines 259--266 | high | Fixes the relation ideal used in proof and verification. |
| C06 | \(\mathbf r^{(a)}\) is obtained by formula (1.2), \(\sum_{i,j}r^{(a_{ij})}_{j,i+n}\). | exact, verified | arXiv:2602.02342v2 | equation (1.2); source lines 191--198 | high | Fixes all transpose/index conventions. |
| C07 | Version 2 explicitly reports verification for \(n\le4\) for the general-\(C\) conjecture. | author report, verified as a report | arXiv:2602.02342v2 | p. 5, immediately before Conjecture 1.5 | high | \(n=5\) is the first dimension not covered by the paper's stated check. |
| C08 | The paper has a formal journal DOI/publication by 2026-08-29. | not found | Crossref title/author query; OpenAlex W7127541625 | search log S05--S06 | medium | Cite the versioned arXiv preprint; do not claim journal publication. |
| C09 | A later public paper or posted solution proves/disproves this conjecture. | not found in two recorded search passes | OpenAlex cited-by count; exact-title/exact-conjecture web searches; MathDB | search log S07--S20 | medium-high | A new proof appears novel in the searched record; all novelty wording remains database-bounded. |
| C10 | Public source code is linked to the arXiv record or found by exact-ID/title searches. | not found | arXiv code/data panel; GitHub/web exact searches | search log S11--S13 | medium | Reproduction must be implemented independently. |
| C11 | The source assumes a fixed characteristic-zero base field. | exact, verified | arXiv:2602.02342v2 | \S2.1, source line 634 | high | Formal statement adopts characteristic zero. |
| C12 | The displayed count of color-relabeling types follows from Proposition 3.14: \(5,39,379,4573\) for \(n=2,3,4,5\). | exact local reproduction completed | arXiv:2602.02342v2 and exact certificate | Proposition 3.14; `logs/clean_verify.log` | high | Supplies a finite baseline/enumeration checksum, not the main proof. |
