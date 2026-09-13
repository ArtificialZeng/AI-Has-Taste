# Fresh citation and claim audit

**Verdict:** ACCEPT  
**Method:** `citation-check-skill` v2, search mode, strict academic precision,
two passes  
**Search date:** 2026-09-06 (Asia/Shanghai)  
**Document:** `manuscript/main.pdf` (SHA-256
`c48cda58c31b61f1df7183905c97bd3978ef96eba6a129238c4a90efedec2941`)

Pass 1 is frozen in `audit/citation-claims.md`.  Pass 2 used that list without
adding or deleting claims.  All 30 extracted claims are verified within their
stated scope: 30 verified, 0 numerical errors, 0 unverified, 0 hallucinations,
and 0 misleading claims.

## Claim-to-source mapping

| Claims | Status | Evidence and exact support |
|---|---|---|
| C01, C06, C09, C14, C23 | Verified (exact/paraphrase) | Akbari--Hu--Liu, arXiv:2609.04069v1, local PDF pp. 2--6: Lemma 2.4 gives deletion; Corollary 3.2 gives the non-strict triangle mass; Theorem 3.4 gives the two-connected noncycle bound and the restricted/triangle-free strict clause. The arXiv record confirms authors, title, date, version, and scope. |
| C05, C29 | Verified (exact) | Liu--Tang--Zhang, arXiv:2607.18031v1, abstract and main-theorem record: every connected order-\(n\) graph satisfies exactly \(\min\{s^+,s^-\}\ge n-1\); authors/title/date match the bibliography. |
| C02--C04, C07--C08, C10--C13, C15 | Verified (exact scope) | The displayed manuscript proof matches the accepted claim and reconstruction in `audit/math.md`; the evidence snapshot is unchanged. No hypothesis, inequality direction, or conclusion is strengthened beyond the accepted theorem. |
| C16--C19, C25--C26 | Verified (exact) | `evidence/enumerate_n4_n8.py` and `evidence/enumeration_n4_n8.json`. A fresh 2026-09-06 rerun returned the frozen JSON byte-for-byte (SHA-256 `fe2f26ccaf120205fb7fae21beb0932f42c146d75d236ea7ee66620836e22f82`). The order rows, totals, 80-digit precision, threshold 1.01, ten exact certificates, generator, and software names/versions all match. |
| C20--C21, C30 | Verified (paraphrase, user-supplied record) | `literature/user_bibliography_check.md` records the exact author/title/year and says its workbook abstract supports integer characteristic polynomials and Sturm root counts for the finite order-nine study, but not the theorem here. The final bibliography transparently labels this an unpublished manuscript. |
| C22 | Verified (logical limitation) | Both manuscript and frozen enumeration evidence explicitly distinguish finite corroboration from the all-orders proof. |
| C24 | Verified (exactly bounded) | Fresh searches for the exact strict formula, two-connected/noncycle equality, and the source title returned the Akbari--Hu--Liu non-strict theorem and adjacent square-energy work, not the present universal strict theorem. The manuscript expressly says the search is bounded, non-exhaustive, and makes no priority claim. |
| C27 | Verified (project record) | The disclosure matches the documented workflow and correctly says the mathematical proof, unlike the finite screen, does not depend on floating-point or model output. |
| C28 | Verified (exact) | The official arXiv:2609.04069 record and frozen v1 PDF match all reference metadata. |

## Citation repair and metadata limitation

The preliminary draft described Zeng's item as an SSRN paper and supplied DOI
`10.2139/ssrn.7386040`.  All applicable title/author/venue/DOI searches found
no authoritative record for that identifier, and a direct resolution attempt
did not yield verifiable metadata.  The release audit therefore removed the
unsupported DOI, publisher, and SSRN assertions.  The final text makes the
checkable narrower claim: the **user-supplied bibliography describes** those
two exact methods, and the reference is explicitly an unpublished manuscript
with user-supplied metadata.  It is a genuinely relevant methodological
comparison from the user's cited list and is not used for the theorem.

## Searches and primary sources

For each academic item, the applicable skill templates were run: author/year
plus initial title words; full title restricted to Semantic Scholar or arXiv;
author/year/venue; arXiv identifier; and DOI query where a DOI had been
supplied.  Novelty checks also searched the exact formulas \(s^+(G)>n\) and
\(s^+(G)=n\) with “2-connected”, “noncycle”, “strict”, and “equality”.

1. S. Akbari, Fu-Tao Hu, Ya-Yang Liu, *Positive and Negative Square
   Energies of 2-Connected Graphs*, arXiv:2609.04069v1,
   <https://arxiv.org/abs/2609.04069>, and frozen local PDF
   `literature/Akbari-Hu-Liu-2609.04069v1.pdf`.
2. Yinchen Liu, Quanyu Tang, Shengtong Zhang, *The Positive and Negative
   Square-Energy Conjecture*, arXiv:2607.18031v1,
   <https://arxiv.org/abs/2607.18031> and its official arXiv HTML full text.
3. `literature/user_bibliography_check.md`, the project record of the
   user-supplied workbook entry for Zijian Zeng's unpublished manuscript.

Every `\cite` key in `manuscript/main.tex` is defined exactly once in
`manuscript/references.bib` and appears in `manuscript/main.bbl`.  No citation
is unnecessary for the role assigned to it, and there are no undefined
citations.  Both declared publication source files were inspected.
