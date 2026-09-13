# Fresh citation and claim-support audit

Audit date: 2026-09-09. Release job:
`bigMac-00026-p03-release-22e156271e42`.

## Method and fixed extraction pass

The advisory `citation-check-skill` v2 was explicitly invoked. Its two-pass
method was applied before verification: the following claim list was fixed from
`manuscript/main.tex`, and no claims were added during the verification pass.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Frelih--Hujdurovi\'c--Kutnar derive the displayed difference-set condition, make rank one automatic, characterize rank two, and pose the higher-rank problem. | attribution/existence | Section 1 |
| C02 | There are exactly three irreducible ambient-conjugacy classes in `GL(3,2)`, of orders 7, 21, and 168, and all fail the implication. | statistic/existence | abstract and Theorem 1 |
| C03 | `GL(3,2)` has 168 elements. | statistic | Section 2 |
| C04 | The census contains 179 subgroups in 15 conjugacy classes and passes 30,072 single-adjunction checks. | statistics | Section 2 |
| C05 | The space has seven lines and seven planes, so 14 proper nonzero subspaces are tested per representative. | statistics | Section 2 |
| C06 | The displayed generators close to groups of orders 7, 21, and 168 and each sends `e_1` through every nonzero vector. | statistics/existence | Section 3 |
| C07 | `W={0,e_1}` and `A={0,e_1,e_2}` give `A-A={0,e_1,e_2,e_1+e_2}` and `3>2`. | statistics/existence | Section 3 |
| C08 | The redundant search has 12,288 pairs and 2,184 violations per class; the verifier reports 45,473 product, 30,072 saturation, and 50,400 conjugacy-element checks. | statistics | Section 4 |
| C09 | The decisive arithmetic is exact, with no random sampling or floating-point step. | existence | Section 4 |
| C10 | The inspected weak-EKR source does not state this finite classification; the focused search does not establish priority. | attribution/limitation | Section 4 |
| C11 | Ernst--Schmidt supplies surrounding finite-linear-group transitivity context. | attribution | Section 1 |
| C12 | Zeng--Liu--Ratnavelu--Ong uses exact symmetry-reduced enumeration and independently checked predicates in another finite extremal problem. | attribution | Section 1 |
| C13 | Zeng's fiber-product preprint is cited only as an explicit-generator certification-style comparison. | attribution | Section 1 |

## Verification pass

| ID | Status | Evidence and scope |
|---|---|---|
| C01 | Verified (exact/paraphrase) | The primary arXiv v1 record and full HTML, `arXiv:2608.18594`, give the formula at lines 141--145, Proposition 2.6 at lines 148--171, Corollary 2.7 at lines 172--179, and Problem 2.9 at lines 206--213. Author, title, date, version, and hypotheses match. |
| C02--C09 | Verified (exact) | The accepted evidence snapshot and referee report support the prose without strengthening. A fresh run of `evidence/verify_certificates.py` using the required research interpreter reproduced the stored report digest `a090deb2...` and every displayed count, class ID, order, violation count, and witness. The elementary values in C03, C05, and C07 also follow directly from the displayed calculations. |
| C10 | Verified as a bounded statement | The primary weak-EKR paper poses the higher-rank characterization and does not state the present finite answer. Both manuscript and evidence explicitly disclaim priority; no novelty strengthening is present. |
| C11 | Verified (paraphrase/context only) | Springer DOI `10.1007/s00209-024-03511-x` and arXiv `2209.07927` identify *Transitivity in finite general linear groups* by **Alena** Ernst and Kai-Uwe Schmidt and describe transitivity on flag-like linear-space structures. The initial BibTeX first-name error was corrected before the final build. No theorem from this paper is used. |
| C12 | Verified (paraphrase) | The official Preprints.org record `202608.1658` confirms title, authors, date, finite-library scope, exhaustive symmetry-reduced enumeration, exact predicates, and independent verification. It is used only for that methodological comparison. |
| C13 | Accepted from user record -- external refresh unavailable | `literature/user_bibliography_check.md` records row 45 of the user-designated workbook and its abstract, which supports the narrow explicit-generator comparison. Bounded title/author/venue/DOI searches did not refresh the Zenodo landing record. Per the authority rule, `metadata_basis=user_designated_workbook`; the record is preserved and no weak-EKR or novelty claim is attributed to it. |

No citation is contradicted, no cited source is used beyond its available
support, and no priority claim is made. The PDF contains four resolved
bibliography entries and no placeholder or undefined citation marker.

## Dependency and bibliography scope

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`. Inspection of the TeX source and recorder output
found no local authored `input`, figure, style, or data dependency. The sorted
source list is therefore complete. Both genuinely relevant items selected from
the user's cited Excel list are present and accurately delimited as
methodological comparisons. External metadata refresh was available for the
Preprints record and unavailable in scope for the Zenodo record; workbook
metadata remains authoritative for the latter.

**Verdict: accept.**
