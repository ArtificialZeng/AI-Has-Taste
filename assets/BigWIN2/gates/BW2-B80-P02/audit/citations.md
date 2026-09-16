# Citation and bibliography audit

## Scope and method

Release job `win-00080-p02-release-a55bfbfd3569`, citation attempt 4, launch `ea59b2bf-9329-4d2c-bb32-325366642be9`, was audited on 2026-09-10 UTC using the two-pass citation-check protocol. Pass 1 froze the five ordinary body-flow claim/citation pairs in `audit/citation-claim-ledger.json`. Pass 2 independently checked that fixed list against exact passages in primary records, the active row-18 user-library record, and the local primary Gómez--Venegas PDF. The union of ledger keys is exactly the five active body citation keys extracted from `manuscript/main.tex`.

The primary-source audit used author/year/title, exact-title, venue, DOI, and arXiv queries where applicable. Official publisher, arXiv, EMS, and Figshare records were opened, and the exact nearby support was inspected. The Gómez--Venegas theorem and its standing hypothesis were additionally checked in the frozen v1 PDF. No `literature/crossref-*.json` or `.md` captures exist.

## Pass-2 results

| Claim | Citation | Exact source locator | Status | Confidence |
|---|---|---|---|---|
| CIT-01: introduction and definition of ozone groups | `ChanGaddisWonZhang2024` | Official OUP abstract and record | Verified | paraphrase |
| CIT-02: Bera--Mukherjee center result under primitive order at least five | `BeraMukherjee2026` | arXiv:2503.21170v1, p. 1 standing assumptions and p. 14, Theorem 9.2; publisher record for final metadata | Verified | paraphrase |
| CIT-03: Gómez--Venegas formula under the same restriction | `GomezVenegas2026` | arXiv:2609.04919v1, p. 5, Section 3.2 and pp. 7--8, Theorem 3.7 | Verified | exact |
| CIT-04: related type-B2 root vectors and PBW presentation | `AndruskiewitschDumas2008` | author-hosted/EMS chapter, Section 3.1.2 | Verified | paraphrase |
| CIT-05: exact residual checks and verification separated from discovery | `Zeng2026UMTC` | official Figshare item description, second substantive paragraph | Verified | paraphrase |

No source contradicts or only partially supports its nearby sentence. The manuscript correctly limits the two closest center/ozone results to `m>=5` and expressly does not claim publication priority for the cubic case. The new theorem is supported by the accepted mathematical audit and displayed proof, not by an external citation.

## Bibliographic record audit

All five cited works exist. Author, title, date/version, venue, pages, arXiv identifier, and DOI fields present in `manuscript/references.bib` agree with the primary records. Bera--Mukherjee's final publisher record is Communications in Algebra 54(9), 3273--3290 (2026), DOI 10.1080/00927872.2025.2595540. Chan et al.'s record is IMRN 2024(7), 5689--5727, DOI 10.1093/imrn/rnad235. The exact metadata checks found no erroneous field requiring replacement and no key change.

The bibliography has normal claim coverage rather than a library-only list: four natural non-library primary sources cover terminology, the closest center theorem, the closest ozone theorem, and the type-B2 presentation. Active user-library row 18 supplies one narrow, direct method comparison and is bound in `audit/user-bibliography-selection.json`; adding a second library item would be decorative. Every retained entry has one direct ordinary body citation, and there are no unused entries.

## Mechanical checks

The bibliography checker reports 5 cited keys, 5 BibTeX keys, zero missing keys, zero unused entries, and exact AUX agreement. The final `.log` and `.blg` scan found no undefined citations, undefined references, missing database entries, duplicate entries, BibTeX warnings, LaTeX errors, fatal errors, or runaway/undefined-control failures. The rendered bibliography was also inspected on PDF pages 5--6.

Overall citation status: **PASS** (5/5 claim/citation pairs verified; no numerical errors, hallucinations, misleading claims, or unresolved citation blockers).
