# Verification Report

Mode: Search, with authoritative user-workbook metadata and local certificate evidence.
Document: manuscript/main.tex and the current four-page manuscript/main.pdf.
Date: 2026-09-08. Method: $citation-check-skill, advisory, two separate passes.

## Summary

The 14 fixed items in audit/citation-extraction.md were checked in their recorded order. Twelve are supported by the accepted proof, exact replay, or refreshed primary text; two (C10 and C14) are accepted from the designated workbook and its supplied abstract. There are no numerical errors, contradicted attributions, undefined citations, or unsupported priority claims. External refresh of the workbook record is unavailable; its bibliographic fields remain authoritative for this workflow. Verdict: accept.

## Claim-to-source checks (Pass 2)

| ID | Finding and decisive evidence | Status |
| --- | --- | --- |
| C01 | Theorem 1 and proof match claim.json, evidence/proof.md, and the accepted audit/math.md: cost 16 and relative dimension 2 at the full frozen scope. | Supported by accepted proof |
| C02 | The three displayed orders match the accepted upper certificate exactly; fresh replay checks all covering requirements and cost 16. | Verified, exact |
| C03 | There are 8 elements; direct pair classification gives 19 comparable and 9 incomparable unordered distinct pairs, hence 8+19+18=45. Matches the checker. | Verified, exact |
| C04 | Lemma 2 uses only nonnegative weights and finite double summation, precisely as in the accepted argument. | Supported by accepted proof |
| C05 | Six weights of 1/3, twelve of 2/3, three of 2: 21 nonzero entries, sum 16. Matches evidence/dual_certificate.json and fresh replay. | Verified, exact |
| C06 | Lemma 3 matches the accepted universal proof: a cycle excludes two heavy orientations, and the two q cases bound every load. The empty case is explicit. | Supported by accepted proof |
| C07 | Source [1], Sections 1.3-1.4, defines PLEs, nonvacuous pair coverage, relative frequency, and relative dimension. The manuscript's diagonal condition and induced-subposet formulation agree. | Verified, paraphrase |
| C08 | Source [1], Figure 1 and Section 3.4, has exactly the three displayed orders. The proof of Theorem 5 explicitly uses the B3 upper bound 2. | Verified, exact |
| C09 | Source [1]'s Figure 1 caption describes dimension 2, while its proof supplies the upper witness. No matching finite lower certificate was found in that version. The manuscript claims only that certificate comparison, not first assertion of the value or global priority. | Supported, bounded comparison |
| C10 | The workbook's row-35 abstract describes certified bounds for counting finite posets, integral arithmetic, and independent endpoint evaluators. This supports the manuscript's modest bibliographic-context sentence. No relative-dimension claim is attributed to it. | Accepted from user record |
| C11 | Fresh audit/release-verification.txt matches evidence/verification.json byte-for-byte: 1323 PLEs, size counts 8,37,114,240,348,336,192,48; 109600 partial permutations. Every table entry was checked individually against the output and rendered page 4. | Verified, exact |
| C12 | Fresh exact replay checks the two enumerations agree, 1324 constraints including empty, 45 requirements, and dual value 16. It exits successfully without an optimizer. | Verified, exact |
| C13 | Source [1]'s arXiv record confirms all five authors, title, 2026, v1, and math.CO. | Verified, exact |
| C14 | Direct workbook extraction confirms Zijian Zeng, exact title, SSRN identifier 7385118 and DOI 10.2139/ssrn.7385118. The manuscript makes no claim that this author is the present author. | Accepted from user record |

## Sources and search scope

[1] [Relative Dimension of Posets, arXiv:2609.05166v1](https://arxiv.org/abs/2609.05166v1); [primary full text](https://arxiv.org/html/2609.05166v1). Refreshed on 2026-09-08. Relevant passages: Sections 1.3-1.4 and 3.4, Figure 1, proof of Theorem 5; the latter corresponds to page 8 in the frozen primary boundary. Sections 2 and 4 were also checked for scope. The comparison is version-specific, not proof of global priority.

[2] The user-designated workbook is /Users/mac/Downloads/Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx, SHA-256 93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427. Inspected literature/user_bibliography_check.md, then read the workbook itself. Sheet1 row 35 contains the BibTeX record and abstract; matching records and provenance notes occur in sheet4 row 5 and sheet5 row 43. The exact relevant cells are saved in audit/workbook-record.txt. metadata_basis=user_designated_workbook. Status: Accepted from user record — external refresh unavailable. DOI and SSRN page opens returned tool internal errors, not evidence of nonexistence. Full text was not refreshed; the supplied abstract supports the limited contextual use. The workbook flags author identity linkage as unconfirmed; no identity linkage is asserted in the article.

Bounded queries run: Duerrschnabel 2026 Relative Dimension of Posets; exact full title restricted to Semantic Scholar/arXiv; Duerrschnabel 2026 arXiv; arxiv:2609.05166; Zeng “Certified Bounds for”; exact Zeng title restricted to Semantic Scholar/arXiv; Zijian Zeng SSRN 7385118; doi:10.2139/ssrn.7385118; exact Zeng full title; “relative dimension” “B_3”; “rdim(B_3)”. Year was omitted from the Zeng templates because the manuscript gives none. No distinct relevant competing result emerged from this bounded search; irrelevant search hits were not used as evidence. No further metadata endpoint was needed after workbook verification.

## Dependencies and rendered citation scope

publication.json source_files is exactly ["manuscript/main.tex"]. The entire input was read: bibliography is inline, with two bibitems and three cite occurrences. There are no imported TeX files, databases, images, or local styles. The clean compiler recorder lists only main.tex plus generated main.aux/main.out outside system TeX inputs; those generated files were removed before rebuilding. Thus the declared authored dependency scope is complete. Both keys resolve to [1] and [2] in extracted text and rendered pages. References, accents, identifiers and DOI are legible. No unnecessary numerical or novelty attribution was added to satisfy the workbook citation requirement. One genuinely relevant workbook paper is included.

No manuscript source repair was necessary; frozen mathematics and source.md were preserved.
