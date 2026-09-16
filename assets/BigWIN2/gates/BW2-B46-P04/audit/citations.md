# Citation and claim audit

## Verdict

Accept.  This was a non-interactive two-pass search-mode audit on 2026-09-06.
Pass 1 froze 20 claims in `audit/claim-citation-ledger.json` (SHA-256
`68ee9c5349e773b43cb7164fd9012ea0ebb784e1cfacdbe62c423c38adade6b4`)
before pass-2 source verification.  No claims were added during pass 2.  The
explicit job prohibition on agents required the primary worker to verify the
six keys serially.

All 20 claims are verified at their stated scope: C01--C04, C06--C07, C09,
C12, C17, and C18 against the sources below; C05, C10--C11, C14--C16, and
C20 against the accepted frozen mathematical audit and exact evidence; C08
and C13 by the displayed exact derivations; and C19 by inspection of the
frozen scripts.  There are no numerical errors, hallucinations, misleading
citations, citation-not-found results, or unverified claims.

## Claim-to-source verification

| Key | Retained nearby claim | Exact source location and verification | Status |
|---|---|---|---|
| `DefantEtAl2026` | Definitions; data only through 43 with `D(43)=7`; Proposition 3.1 and Corollaries 4.1--4.2; 3-core criterion; beta-number computation and regression target. | arXiv:2608.27718v1, HTML Introduction lines 83--102; Proposition 3.1 lines 163--183; Section 4 lines 191--301; Section 8.2 lines 483--501.  The arXiv record confirms title, four authors, 2026 date, version 1, and identifier. | Verified (exact/paraphrase) |
| `MartinDuro2026` | Question 4.17 is the source of the finite problem. | Version-of-record Springer page confirms Diego Martín Duro, title, *Ramanujan Journal* 69, article 37 (2026), DOI `10.1007/s11139-025-01311-3`.  arXiv:2306.12408v2, Proposition 4.15 and Question 4.17, HTML lines 269--285, state the reduction and ask for the pattern of integers for which every nontrivial column has a zero. | Verified (paraphrase) |
| `Murnaghan1937` | Historical primary source for the Murnaghan--Nakayama rule. | *American Journal of Mathematics* 59(4) (1937), 739--753; title and author match the volume-59 issue record and modern mathematical reference records.  Defant et al., Section 2, HTML lines 137--140, states the recursive rim-hook rule used by the manuscript. | Verified (record exact; attribution corroborated) |
| `Nakayama1940` | Historical primary source for the Murnaghan--Nakayama rule. | J-STAGE official article record: Tadasi Nakayama, exact title, volume 17 (1940), 411--423, DOI `10.4099/jjm1924.17.0_411`.  The retained citation is joint historical attribution for the standard rule, whose exact modern statement is in Defant et al., Section 2. | Verified (record exact; attribution corroborated) |
| `Macdonald1995` | Frobenius characteristic expansion and Jacobi--Trudi identity. | OUP official book record confirms I. G. Macdonald, second edition, 30 March 1995, OUP/Clarendon metadata and DOI `10.1093/oso/9780198534891.001.0001`.  Inspected text: Chapter I, formula (3.4), PDF pp. 41--42 (viewer pp. 51--52), gives `s_lambda=det(h_{lambda_i-i+j})`; Chapter I, Section 7, formulas (7.2), (7.5), and (7.7), PDF pp. 113--115 (viewer pp. 123--125), give the characteristic-map character/power-sum expansion. | Verified (exact) |
| `Zeng2026MultiplicityArxiv` | Exact integer cut-partition dynamic programming, independent small-order enumeration, and diagnostic-only use. | arXiv:2608.18179v1 official record confirms title, Zijian Zeng, 18 August 2026, and DOI `10.48550/arXiv.2608.18179`.  Section 4, HTML lines 90--98 (PDF p. 4), states all three elements of the nearby claim; Data and code availability, lines 111--113, reiterates that no computational output is a theorem premise. | Verified (near-exact paraphrase) |

The active 49-entry first-sheet user library is bound in
`audit/user-bibliography-selection.json` to citation attempt 1 and launch ID
`efc082e7-3499-4501-8c7c-cdb03737ed73`.  Row 17 is cited directly in ordinary
body flow.  It is the only library entry close enough to an actual claim; a
second would be padding.

## Bibliography coverage and mechanics

The bibliography is not user-library-only: it includes the primary problem
paper, the closest prior problem/result, both historical sources named by the
standard rule, the standard symmetric-functions monograph used for the
certificate, and the one justified library method comparison.  Each retained
source has a nearby supported claim; none is decorative.  Searches for
`ZF(44)`, `D(44)` with zero-free columns, the paper title with 44, and `S_44`
with zero-free character columns found no equivalent primary answer on the
search date.  This is bounded search coverage, not a priority claim.

The citation-key checker reports six cited keys, six bibliography entries, no
missing or unused key, and exact agreement with `main.aux`.  The converged log
and `.blg` have no undefined citations, missing database entries, repeated
entries, or BibTeX warnings.  No key or bibliography replacement was needed.

Authoritative URLs inspected:

- https://arxiv.org/html/2608.27718v1
- https://link.springer.com/article/10.1007/s11139-025-01311-3
- https://arxiv.org/html/2306.12408v2
- https://www.jstor.org/stable/i340740
- https://www.jstage.jst.go.jp/article/jjm1924/17/0/17_0_411/_article
- https://academic.oup.com/book/52932
- https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf
- https://arxiv.org/html/2608.18179v1

