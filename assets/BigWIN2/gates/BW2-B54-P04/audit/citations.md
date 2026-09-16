# Citation and claim verification report (pass 2)

**Mode:** citation-check-skill two-pass primary-source verification  
**Document:** `manuscript/main.tex`  
**Search date:** 2026-09-07  
**Fixed input:** the 24-item ledger in `audit/citation-claim-ledger.md`  
**Verdict:** **accept**

The user prohibited subagents, so the four keys were verified sequentially.
Pass 2 did not re-extract claims. The frozen local source text and authoritative
publisher/arXiv records, rather than registry metadata or search snippets alone,
determined the conclusions.

| Metric | Count |
|---|---:|
| Claims in frozen ledger | 24 |
| Verified | 24 |
| Numerical errors | 0 |
| Misquoted / misleading / hallucinated | 0 |
| Unverified | 0 |
| Citation keys verified | 4 |
| BibTeX replacements or key changes | 0 |

C01--C03 and C08--C19 agree exactly with the accepted reconstruction in
`audit/math.md`. C20--C22 agree exactly with the stored checker output. C04--C07
and C24 are supported at the primary-source locations frozen in
`audit/citation-source-evidence.md`; C23 is the correct, conservative limitation
of finite computation. In particular, 995, the range 2--7, both values for
`K_2`, and NetworkX 3.4.2 all match their evidence exactly.

All four retained citations are necessary. Bessy et al. supports the burning
convention and metric formulation; Cockayne et al. supports the Roman
domination definitions; Pastorek supplies the exact origin and finite-survival
limitation; registry row 9 supports the explicit finite-certificate comparison.
The bibliography is therefore neither Excel-only nor padded. The proof is
self-contained, so it relies on no omitted prior theorem. The manuscript makes
no priority or open-status claim.

The active registry selection is bound to citation attempt 1 and launch
`2c49141d-b018-4e5f-be57-776e81c68945` in
`audit/user-bibliography-selection.json`; the selected work has the ordinary
body-flow direct citation `\cite{ZengEtAl2026}`. Mechanical checking found four
cited keys and four entries, with no missing, unused, or AUX-inconsistent key.
The final log scan found no undefined citation/reference, missing database
entry, repeated entry, BibTeX warning, LaTeX error, fatal error, emergency stop,
undefined control sequence, runaway argument, or overfull box. No citation
blocker remains.
