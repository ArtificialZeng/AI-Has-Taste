# Claim ledger

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | A278992 counts simple chord-labelled chord diagrams and has offset (1,4). | verified exact | OEIS A278992 | NAME/OFFSET, accessed 2026-08-30 CST | high | Fixes the native sequence indexing. |
| C02 | OEIS gives the displayed EGF. | verified exact | OEIS A278992 | FORMULA, accessed 2026-08-30 CST | high | Defines the sequence analytically/formally. |
| C03 | OEIS labels the displayed four-step relation “Conjecture D-finite with recurrence,” credited to R. J. Mathar, 2020-01-27. | verified exact | OEIS A278992 | FORMULA, accessed 2026-08-30 CST | high | This is the precise open-status claim addressed here. |
| C04 | Krasko--Omelchenko prove the same EGF and list coefficients (a_1=0,a_2=1,a_3=1,a_4=21,a_5=168,a_6=1968). | verified exact | Krasko--Omelchenko (2017) | Theorem 4.3, equation (17), pp. 13--14 (PDF pages 14--15) | high | Supplies the last known baseline and initial data. |
| C05 | The paper is a formally published journal article, DOI 10.37236/6037, EJC 24(3), P3.43, published 2017-09-08. | verified exact | EJC publisher page; Crossref; zbMATH | article metadata; Crossref DOI record; Zbl 1369.05112 | high | Replaces the prompt's arXiv-only citation with the formal publication. |
| C06 | arXiv:1601.05073 has only version v1, submitted 2016-01-19, and points to the 2017 journal article. | verified exact | arXiv abstract/version page | submission history and journal reference | high | There is no later arXiv revision to privilege over v1. |
| C07 | The 2017 paper proves the EGF but does not state the Mathar 2020 four-step recurrence. | verified bounded absence | Full 23-page publisher PDF plus chronology | Theorem 4.3 and full-text recurrence inspection | high | The EGF is prior art; the requested recurrence derivation is not in that source. |
| C08 | No later source proving this exact A278992 recurrence was found in the recorded searches. | not found in bounded search | OEIS; Crossref; OpenAlex; Semantic Scholar; zbMATH; web exact-formula searches | search log S08--S13 | medium-high | Supports a carefully bounded novelty statement, never an absolute priority claim. |
| C09 | No public GitHub repository specifically matching A278992 or the exact paper title was found. | not found in bounded search | GitHub repository API and web search | search log S14--S15 | medium | No public code baseline was available to reproduce. |
| C10 | Citation-index counts disagree (Crossref 2, OpenAlex 1, Semantic Scholar 14); index counts are not mathematical evidence. | verified exact metadata | Crossref/OpenAlex/Semantic Scholar APIs | DOI 10.37236/6037 records, 2026-08-30 CST | high | All 14 Semantic Scholar citing-record titles/abstracts were screened instead of trusting a count. |
| C11 | The formal EGF has (a_0=0), although OEIS begins at (n=1). | verified exact derivation | Direct substitution (F(0)) and exact series expansion | formal statement; certificate to be added | high | Repairs the (n=4) boundary without inventing a negative index. |
| C12 | The stated EGF coefficients satisfy the displayed recurrence for every integer n at least 4. | proved exact | This project | `proof/main_proof.md`; exact certificate and two independent checks | high | Resolves the mathematical problem. |
| C13 | The initial block is (a0,a1,a2,a3)=(0,0,1,1), or in OEIS-native form (a1,a2,a3,a4)=(0,1,1,21). | verified exact | This project; prior terms in KO17/OEIS | formal expansion in verifier; KO17 Theorem 4.3 | high | Specifies the complete starting data and index convention. |

## Frozen claim scope

The externally sourced finite Gate 1 list is C01--C11.  “Not found” is
restricted to the databases, versions, queries, and access date recorded in
`search_log.md`.  C12--C13 are project results, entered only after independent
certification and the second-pass novelty search S16--S20.
