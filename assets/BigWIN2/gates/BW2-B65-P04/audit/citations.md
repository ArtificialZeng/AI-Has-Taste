# Citation and bibliography audit

**Mode:** search verification, strict two-pass citation audit  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Search date:** 2026-09-07  
**Release job:** `win-00065-p04-release-91b9962de931`  
**Citation attempt / launch:** `2` / `b125cb45-d2b8-4585-816d-677b4499e99a`

## Summary

Pass 1 froze eleven substantive and bibliographic claim statements before this
attempt's verification. The union of `claims[].citation_keys` is exactly the
five ordinary body-flow citation keys extracted from the canonical manuscript.
Pass 2 verified the fixed claims sequentially against original papers, official
publisher/preprint records, and exact primary passages. All eleven claims are
verified; there are no numerical errors, unsupported citations, misleading
strengthenings, decorative references, or blockers.

The user explicitly prohibited agents, so the per-key checks were performed
sequentially by this release worker. All applicable academic search templates
(author/title, exact title, author/venue, DOI, and arXiv identifier where
present) were run before primary records were inspected. Before verification,
`literature/bibliography-revision-*.md` and
`literature/crossref-*.(json|md)` were enumerated; neither set exists in this
project.

## Fixed claim-to-source verification

| Claims | Key | Exact source location and support | Status |
|---|---|---|---|
| C01--C02 | `Maxwell1864` | Taylor & Francis DOI record `10.1080/14786446408643668` gives J. Clerk Maxwell, *On the calculation of the equilibrium and stiffness of frames*, series 4, volume 27, issue 182, pp. 294--299 (1864). The original scanned text on p. 294 gives the three-dimensional `3s-6` displacement count; Haslegrave--Michaeli--Nixon, primary HTML/PDF, Introduction and Section 2 (PDF pp. 1 and 4), states the cited modern `dn-binomial(d+1,2)` Maxwell formulation. | Verified (paraphrase) |
| C03--C04 | `AsimowRoth1978` | The AMS primary record and article identify Leonard Asimow and Ben Roth, *The Rigidity of Graphs*, *Transactions of the AMS* 245 (1978), 279--289, DOI `10.1090/S0002-9947-1978-0511410-9`. Its generic/regular framework theorem equates rigidity with maximal rigidity-matrix rank. Haslegrave--Michaeli--Nixon Section 2, PDF p. 4, reproduces the precise hypothesis `n >= d+1` and rank `dn-binomial(d+1,2)`. | Verified (paraphrase) |
| C05--C07 | `HaslegraveMichaeliNixon2026` | Official arXiv record 2609.05058 confirms the title, three authors, 4 September 2026 submission and identifier. Primary HTML lines 68--73 (Theorem 1.4 and following paragraph; PDF p. 2) exclude `C3` and `C4` and call the exclusion a limitation of the argument. Lines 75--84 (Corollary 1.5; PDF p. 3) define `sigma` and state `rig(G) >= M(G)-ceil(sigma(complement G)/2)`; for `sC3 disjoint-union tC4`, `sigma=s+t`, exactly yielding (1.3). The local PDF SHA-256 is `e5a603ed64fc286ceb56f1a009d559bb4a27ac2f5bc63ac02977a2800cd842be`. | Verified (exact/paraphrase) |
| C08--C09 | `GortlerHealyThurston2010` | Official arXiv 0710.0926 v5 confirms title, authors and *American Journal of Mathematics* 132(4), 897--939 (2010); the primary-author repository copy gives DOI `10.1353/ajm.0.0132`. Primary HTML Definitions 1.7 and 1.9 (lines 93--126) define equilibrium stress vectors, equilibrium stress matrices, and their kernels. This directly supports the manuscript's limited statement that these are standard rigidity tools; the manuscript proves its own needed local passage. | Verified (paraphrase) |
| C10--C11 | `ZengEtAl2026ExactPositivity` | Primary SSRN record 7348478 confirms the exact title, five authors, August 2026 date, 31-page preprint and DOI `10.2139/ssrn.7348478`. The abstract's final two sentences state that all sign decisions use exact rational/algebraic arithmetic and independent definition-level verification programs and limit the result to partial scalar-gate theorems. The manuscript expressly limits the comparison to methodology in a different matrix problem. | Verified (paraphrase) |

## Bibliography coverage and integrity

All five BibTeX records have accurate titles, authors, years, venue/preprint
types, pages where applicable, and DOI/arXiv identifiers. No record or key
required replacement. Every database record has an ordinary direct body-flow
citation, and there are no uncited entries.

Coverage is not user-library-only. Maxwell is the historical count source;
Asimow--Roth is the foundational generic rank source;
Haslegrave--Michaeli--Nixon is the problem origin and closest prior theorem; and
Gortler--Healy--Thurston is the natural stress-matrix method source. Active
user-library row 29 supports only the narrow, expressly different-subject exact
verification comparison. The other 48 active titles were screened; row 10 is
superficially closer in graph subject, but the registry has no abstract or
keywords for it and no exact primary passage was available for a nearby claim.
No second library citation was padded.

The bibliography checker found five cited keys, five database keys, zero
missing or unused entries, and exact agreement with the final `.aux`. The
converged `.log` and `.blg` contain no undefined citation/reference, missing
database entry, repeated entry, BibTeX warning, or rerun request.

## Primary records consulted

- Taylor & Francis: <https://doi.org/10.1080/14786446408643668>
- American Mathematical Society: <https://www.ams.org/journals/tran/1978-245-00/S0002-9947-1978-0511410-9/>
- arXiv 2609.05058: <https://arxiv.org/abs/2609.05058>
- arXiv 0710.0926: <https://arxiv.org/abs/0710.0926>
- Harvard primary-author repository copy: <https://dash.harvard.edu/bitstreams/7312037d-ce52-6bd4-e053-0100007fdf3b/download>
- SSRN 7348478: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7348478>

## Verdict

**Accept.** Citation existence, metadata, exact nearby support, user-library
binding, bibliography coverage, body-flow use, and mechanical consistency pass.

