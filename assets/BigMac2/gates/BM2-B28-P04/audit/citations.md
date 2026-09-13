# Fresh citation audit

## Scope and method

This release audit is bound to evidence snapshot
`6103d3338e01807a90cdcdf1de4d1dcd19827711615d8f91d115fe1dbc0e6640`,
manuscript digest
`0497ba06c140c8bf1dd752e62348ce9084e8ae2f27e7f003e4c2a209d9b95183`,
and PDF digest
`e3f58a99faa9a912351ae3d80ac81dd4f128e4595759e1444ec4d0f391103386`.
The audit used the explicitly invoked citation-check skill in two passes.  The
fixed extraction is `audit/citation_claims.md`; this report is the separate
verification pass.  The method was
`citation-check-skill-search-plus-primary-source-manual`, searched on
2026-09-09.

Both publication dependencies were inspected in full.  `main.tex` imports no
authored TeX fragments, figures, data files, or custom styles; its only local
authored dependency is `references.bib`.  The generated `.aux`, `.bbl`, and
`.out` files are build products, not authored dependencies.  Thus the sorted
`publication.json` source list is complete.

`literature/user_bibliography_check.md` is absent.  Consequently there is no
user-designated workbook record to refresh or override.  The bibliography
contains two genuinely relevant primary preprints, both independently
refreshed from their official arXiv abstract and HTML pages and also preserved
as frozen HTML in the accepted evidence:

- Henry Shin, *Iterated-sumset spectra: The complete exponent law and its rank
  geometry*, arXiv:2609.01690v1, submitted 1 September 2026.  The official
  record confirms author, title, date, category, and version.  The full text
  immediately before Corollary 10.5 defines `nu(h,4)` and states
  `nu(h,4)=N(h,4)-1`; Theorem 10.3 gives the displayed formula for
  `D_h^max`; Corollary 10.5 gives the exact two-sided bound used in the paper.
- Enkai Zhang, *Sharp order-preserving integer models for short additive
  equalities*, arXiv:2609.08915v1, submitted 8 September 2026.  The official
  record confirms author, title, date, category, and version.  Remark 5.2
  distinguishes the rank/weak-type quantities, and Question 12.5 explicitly
  formulates Shin's all-`h` label-level endpoint question and says the weak-type
  theorem does not answer it.

The bounded comparison phrase "closest inspected sources" is accurate only
for this disclosed inspection; the manuscript expressly makes no priority or
exhaustive-literature claim.

## Fixed-claim verification

| Claim | Status | Basis |
| --- | --- | --- |
| C01 | Verified (exact) | Shin v1, Theorem 10.3 and Corollary 10.5. |
| C02 | Verified (paraphrase) | Zhang v1, Remark 5.2 and Question 12.5. |
| C03 | Verified (bounded comparison) | These are the two primary sources actually inspected; no global ranking is asserted. |
| C04 | Verified (exact) | Substitution `h=4` in Shin's displayed formula and bound gives 15 and 16 exactly. |
| C05 | Verified (exact) | Accepted mathematical audit plus fresh ordered-product replay of all endpoint subsets. |
| C06 | Verified (exact) | Fresh replay checked 1820 and 2380 sets, equal to the two binomial coefficients. |
| C07 | Verified (exact) | Fresh replay, decisive certificate, and independent earlier certificate agree entry-for-entry. |
| C08 | Verified (exact) | Stars-and-bars count `binom(7,3)=35`; the certificate lists exactly those 35 vectors. |
| C09 | Verified (exact) | Shin v1, text immediately preceding Corollary 10.5. |
| C10 | Verified (paraphrase) | Definition, monotonicity, and Shin's endpoint upper bound; also checked in the accepted math audit. |
| C11 | Verified (exact) | Every displayed table entry matches the decisive JSON and the fresh ordered-product replay. |
| C12 | Verified (exact) | Frequency sums are exactly 1820 and 2380. |
| C13 | Verified (exact) | Direct ordered-product recomputation gives 35 for `{0,1,11,15}`. |
| C14 | Verified (exact) | Fresh release replay used all 256 ordered tuples for every one of the 4200 endpoint subsets. |
| C15 | Verified (exact) | The nondecreasing-tuple program and JSON contain both stated supports. |
| C16 | Verified (exact) | All three inspected implementations use finite integer/set operations and no solver or floating point. |
| C17 | Verified (exact) | All named ancillary and archived source files exist and have the stated contents. |
| C18 | Verified (exact scope) | The theorem, proof, abstract, and accepted frozen claim are restricted to `(h,k)=(4,4)`. |

There are no numerical errors, contradicted attributions, unsupported novelty
claims, undefined citation keys, removable citations, or unverified
references.  The rendered bibliography resolves both entries and gives the
correct metadata.  Citation verdict: **accept**.
