# Verification Report

**Mode:** Search, with the user-designated bibliography authority override  
**Document:** `manuscript/main.tex` and its rendered `manuscript/main.pdf`  
**Generated:** 2026-09-08 (Asia/Shanghai)  
**Method:** `$citation-check-skill` v2, two-pass claim extraction and verification

## Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 15 |
| Verified | 15 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status:** PASS. The bibliography authority override described below
is a disclosed metadata basis, not evidence for the new theorem.

## Pass separation and dependency scope

Pass 1 read the entire authored text and froze the exhaustive applicable claim
list in `audit/citation-extraction.md` before any verification. Pass 2 used that
fixed list. The complete authored dependency scope is exactly
`manuscript/main.tex` and `manuscript/references.bib`, matching the sorted
`publication.json` `source_files`. There is no imported authored TeX, figure, or
local style file. The final `.bbl`, extracted PDF text, and rendered references
contain both cited keys; the final compiler and BibTeX logs contain no undefined
citation, missing-entry, or duplicate-entry diagnostic.

## Claim-to-source findings

| Claim | Status | Support checked |
|---|---|---|
| C01 | Verified (paraphrase) | Xie--Zhou primary arXiv abstract and model statement. |
| C02 | Verified (exact) | Manuscript Lemma 2 and the accepted reconstruction in `audit/math.md`. |
| C03 | Verified (exact) | Bernoulli construction and strong-law step in the manuscript and accepted audit. |
| C04 | Verified (exact) | Pathwise statistic identity plus subsequence argument in the manuscript and accepted audit. |
| C05 | Verified (exact) | Equality of observed-range denominators; no clock-rate normalization is used. |
| C06 | Verified (exact) | Xie--Zhou Theorem 1, equations (16)--(17), and the displayed iterated limits. |
| C07 | Verified (exact) | Xie--Zhou Theorem 1 and the manuscript's regular-variation calculation. |
| C08 | Verified (exact scope) | Every exclusion is explicit in the theorem/abstract/scope section; no stronger limit is asserted. |
| C09 | Verified (exact) | Xie--Zhou model equation (4), Theorem 1, and Proposition 2, including loop deletion and tails. |
| C10 | Verified (exact) | Standard iid Bernoulli strong law applied with mean `1-rho`; no external numerical datum. |
| C11 | Verified (exact) | Quotient of the paired Xie--Zhou asymptotics gives `2^gamma`. |
| C12 | Verified (exact) | At `rho=1`, every Bernoulli refresh indicator is zero, so the skeleton has one label. |
| C13 | Verified (authority override; interpretation) | The workbook record supplies the exact title and subject; `literature/user_bibliography_check.md` permits only this broad deterministic-graph contrast. |
| C14 | Verified (scope) | The proof and dependency set use no result from the Zeng preprint; the manuscript expressly disclaims such input. |
| C15 | Verified (process statement) | The proof is analytic and the manuscript has no computational certificate, simulation, data, or figure dependency. |

## Substantive citations

1. **Jiansheng Xie and Yechi Zhou, arXiv:2609.05290v1.** The primary
   arXiv record and full HTML text were checked on 2026-09-08 at
   <https://arxiv.org/abs/2609.05290> and
   <https://arxiv.org/html/2609.05290>. They verify the title, authors,
   submission date, version, `math.PR` category, arXiv DOI, iid model,
   observed-range definitions, endpoint convention, all four asymptotics in
   Theorem 1, loop-deleted fixed-degree and tail convergence in Proposition 2,
   and the dependent-sequence open direction. The manuscript imports no claim
   beyond that scope and makes no priority claim.

2. **Zijian Zeng, DOI 10.5281/zenodo.22294612.** Metadata basis is
   `metadata_basis=user_designated_workbook`, specifically the workbook record
   documented with SHA-256 and row number in
   `literature/user_bibliography_check.md`. Status: **Accepted from user record
   — external refresh unavailable**. The bounded web queries and direct landing
   page refresh did not expose a primary record in scope. The supplied title,
   author, date, and DOI are therefore preserved as authoritative. The nearby
   prose makes only the locally authorized broad deterministic-graph contrast
   and explicitly says this source supplies no probability or
   regular-variation input. No theorem here depends on it.

No contradicted attribution, unsupported novelty statement, numerical mismatch,
undefined citation, or unresolved useful citation limitation remains. The
citation verdict is therefore `accept`, not a claim of independent bibliographic
priority or mathematical certification.
