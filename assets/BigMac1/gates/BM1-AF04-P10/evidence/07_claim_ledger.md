# Claim ledger — frozen Gate 1 list

Claims were frozen before the dated search. “Exact” below means a literal
claim to be checked, not that this project has independently proved it.

| ID | Claim | Type | Status at 2026-08-30 (Asia/Shanghai) | Primary/source evidence | Location | Confidence | Consequence |
|---|---|---|---|---|---|---:|---|
| C01 | The problem uses all linear subspaces of \(\mathbb F_2^7\) and the stated subspace distance. | exact | verified | Honold–Kiermaier–Kurz, DOI 10.3934/amc.2016033; specialist table | definitions | 99% | fixes the optimization domain |
| C02 | \(\mathbb F_2^7\) has exactly 29,212 subspaces. | exact | verified algebraically and by two exact RREF enumerators | Gaussian-binomial sum \(2(1+127+2667+11811)\); baseline replay and independent verifier | formal statement / certificates | 100% | fixes graph order |
| C03 | There is a 333-word constant-dimension \((7,333,4;3)_2\) code. | exact | verified from primary paper | Heinlein–Kiermaier–Kurz–Wassermann, DOI 10.3934/amc.2019029, Theorem 2 and Appendix C; arXiv:1708.06224v5 | pp. 2, 16–18 | 99% | baseline lower construction |
| C04 | Adding the whole 7-space to that 333-plane code yields a mixed code of size 334. | inference from exact theorem | verified by \(d_S(U,V)=7-3=4\) | C03 plus the distance formula | direct | 100% | \(A_2(7,4)\ge334\) |
| C05 | \(A_2(7,4)\le388\). | exact | verified as a published theorem; this project has not re-certified the floating/SDP computation | Heinlein–Ihringer, DOI 10.3934/amc.2020034, Theorem 1.1; arXiv:1809.09352v2 | p. 2 | 98% | published upper frontier |
| C06 | The currently displayed specialist interval remains 334–388. | dated exact | verified on current table and 2026-07-28 TheoremDB snapshot; fresh searches found no contrary primary result | Subspace Codes table; TheoremDB P2796/R502 | table cell / record | 96% | original problem remains open within searched sources |
| C07 | Any feasible 335-word code is a strict new lower record. | dated inference | supported, conditional on C06 and search coverage | C03–C06 | inferred | 95% | breaker success threshold |
| C08 | The published 333-plane code has exactly one compatible outside subspace, namely \(V\). | author/replay report | independently verified locally in addition to public R497/R503 | baseline replay, radius verifier, TheoremDB R497/R503 | exact ambient enumeration | 99% | direct extension cannot exceed 334 |
| C09 | Deleting at most five published planes and adding arbitrary compatible subspaces cannot beat 334. | author/replay report | independently strengthened and verified locally through radius seven | radius-six/seven certificates; TheoremDB R497/R504 | exhaustive bounded scope | 99% | radius 8 is now the first unclosed exchange radius |
| C10 | Full invariance under the fixed order-127 Singer action caps a mixed code at 255. | author/replay report | verified only as a public exact replay record; not used or independently rerun here | TheoremDB R497, R506 | external exhaustive bounded scope | 94% | full Singer compression cannot improve 334 if the external replay is accepted |
| C11 | Latest arXiv versions are v5 (2019-03-22) for the 333 construction and v2 (2020-10-30) for the 388 bound. | exact metadata | verified | arXiv abstract pages/API | version histories | 100% | pins versions used |
| C12 | No public 335 construction or later upper bound below 388 was found by the recorded 2026-08-30 searches. | bounded negative search | verified only within logged databases/queries | search log | logged queries | 92% | bounded novelty lock, not proof of absence |
| C13 | Journal DOIs are 10.3934/amc.2019029 (2019, 13(3), 457–475) and 10.3934/amc.2020034 (2020, 14(4), 613–630). | exact metadata | verified | publisher, Crossref, arXiv; zbMATH ID 7076474 for first paper | metadata records | 100% | bibliography correctness |
| C14 | Public code/data directly linked by the primary papers is sufficient to replay the 333 construction. | public-code availability | partly verified: Appendix C is explicit; no primary-paper GitHub repository found | arXiv source, publisher, code-link searches | Appendix C / search log | 90% | project must build a transparent replay |
| C15 | The exact radius-seven exchange optimum around the specified Appendix C 333-plane code is 334. | new finite theorem | verified twice by independent exact algorithms | `proof/finite_theorem.md`; `certificates/radius7_verification.json` | full serialized enumeration | 99% | excludes 335 within that neighborhood only |
| C16 | No prior public closure of radius six or seven for this baseline was found. | bounded post-result novelty search | supported only within logged databases and queries; TheoremDB records radius five and proposes radius six | search log Pass 3; TheoremDB R500/R504 | dated search | 93% | supports bounded novelty wording, not absolute priority |

## Frontier correction

The phrase “已有 334-word construction” is correct only for a mixed-dimension
code. The published construction itself contains 333 three-dimensional
subspaces; its 334th word is the whole seven-dimensional space. No correction
to the numerical interval was found.
