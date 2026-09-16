# Citation verification report

Release job: `win-00082-p02-release-3a87cc6567a1`  
Citation attempt: 1  
Launch: `11f32c73-3c59-4edc-a5c0-45876cb21250`  
Verification date: 2026-09-09 UTC  
Mode: primary-source search verification, with local exact evidence for the finite audit

## Stage 1: frozen extraction

The citation-bearing claims were extracted from the complete canonical manuscript before the support decisions were recorded. The frozen extraction is `audit/citation-claim-ledger.json`. Its four unique claims cover exactly the three ordinary body-flow keys parsed from `manuscript/main.tex`: `AlistePrietoDeMierZamora2021`, `KirillovEtAl2026`, and `Zeng2026Multiplicity`. Comments, bibliography commands, cross-references, and inert text supplied no keys.

## Stage 2: claim-level primary-source verification

| Claim | Status | Primary source and exact locator | Support decision |
|---|---|---|---|
| CIT-01 | Verified (paraphrase) | Kirillov--Nenashev--Shapiro--Vaintrob, arXiv:2609.07728v1, Section 9.3, equation (9.26) and Conjecture 9.10; <https://arxiv.org/html/2609.07728v1> | The source defines the displayed specialization and states injectivity for every `g >= 3` on rooted trees of fixed order. The manuscript preserves that scope. |
| CIT-02 | Verified (exact) | Same source, Remark 9.12 and Theorem 9.14 | Remark 9.12 says the automatic range is `g >= N` and reports exhaustive verification through 13 vertices. Theorem 9.14 proves the cited component/branch-size-restricted regime. No unrestricted result is attributed. |
| CIT-03 | Verified (paraphrase) | Aliste-Prieto--de Mier--Zamora, arXiv:2002.08186v1, Section 3, Theorem 9; <https://arxiv.org/html/2002.08186v1> | The theorem states that all rooted trees are reconstructible from the rooted U-polynomial. The repository publication record confirms the 2021 Discrete Mathematics metadata and DOI 10.1016/j.disc.2020.112255. |
| CIT-04 | Verified (paraphrase) | Zeng, arXiv:2608.18179v1, Lemma 2.2, Section 3, and Section 4; <https://arxiv.org/html/2608.18179v1> | Lemma 2.2 identifies leading and next star-basis coefficient data; Section 3 reconstructs multiplicity-isolated weighted cores; Section 4 canonically encodes each height-at-most-two branch of a diameter-six tree by an integer partition. |

The selected user-library entry is registry row 17. The active arXiv record independently confirms its title, author, submission date, identifier, DOI, abstract, and the exact supporting passages. The library source key `Zeng2026MultiplicityArxiv` is represented in the canonical bibliography by the unique final key `Zeng2026Multiplicity`; this is a key/formatting choice, not a different work. No bibliography or citation-key replacement was needed in this release pass.

## Bibliographic identity and coverage

| Key | Identity check | Why retained |
|---|---|---|
| `KirillovEtAl2026` | Title, four authors, 2026 date, arXiv:2609.07728v1, and math.CO agree with the authoritative arXiv record. | Primary origin of the polynomial, conjecture, computational boundary, and closest branch-size result. Natural non-library source. |
| `AlistePrietoDeMierZamora2021` | Title, three authors, Discrete Mathematics 344(3), article 112255, 2021, and DOI 10.1016/j.disc.2020.112255 agree with arXiv and the institutional repository record. | Primary source for reconstruction by the fully pointed rooted U-polynomial. Natural non-library source. |
| `Zeng2026Multiplicity` | Title, author, 2026 date, arXiv:2608.18179v1, math.CO, and DOI 10.48550/arXiv.2608.18179 agree with arXiv. | Directly supports the nearby comparison with multiplicity-isolated cores and height-two branch encodings; selected active-library source. |

This is a claim-driven scholarly bibliography rather than an Excel-only bibliography: the problem-origin/closest-result paper and the rooted-U method paper are both primary non-library sources in ordinary body flow. Every retained item supports a nearby sentence; no decorative reference was found. The three cited keys are present exactly once in `manuscript/references.bib`, appear in the final AUX/BBL, and have no undefined or unused entry.

Applicable deterministic searches used author/year/title, exact full title on arXiv, author/year/venue, DOI, and arXiv-identifier forms. The authoritative arXiv HTML/full text and the institutional publication record were inspected, not merely search-result snippets. The supplied local copy of arXiv:2609.07728v1 has the expected SHA-256 digest and agrees with the live primary record. No online-source unavailability was asserted; the project contains no `literature/crossref-*` capture.

## Other auditable factual assertions

The finite-audit statement at manuscript lines 174--186 is project-generated rather than literature-derived. A fresh exact run of `python3 evidence/audit_height_two.py --max-n 14 --max-g 14` was byte-for-byte identical to `evidence/audit_height_two.json`; its declared ranges are `N=1..14` and `g=3..14`, and its status is `pass`. Definitions and methodology descriptions were excluded under the citation-check extraction rules. The theorem and proof scope remain exactly the mathematically accepted claim; computation is explicitly described only as finite corroboration.

## Verdict

Accept. All citation-bearing claims are supported at their stated strength, bibliographic identities are verified, coverage is natural and complete for the manuscript's contextual dependencies, and there are no undefined citations or unsupported priority/open-status assertions.
