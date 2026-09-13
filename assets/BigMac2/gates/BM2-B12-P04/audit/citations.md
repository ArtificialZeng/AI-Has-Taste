# Citation and claim-verification audit

**Mode:** Search verification, using the explicitly invoked
`citation-check-skill` two-pass procedure.  **Search date:** 2026-09-07.
**Document:** `manuscript/article.pdf` (3 pages).

## Pass 1: fixed claim extraction

Extraction was completed before source verification. Definitions and descriptions
of the authors' own procedure were excluded under the skill rules.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | For each fixed real alpha, almost-sure convergence holds exactly for alpha greater than 1/2. | Existence/statistic | Abstract; Theorem 1, p. 1 |
| C02 | At alpha=1/2 the exceedance series converges exactly for epsilon greater than 2. | Existence/statistic | Abstract; Theorem 1, pp. 1, 3 |
| C03 | A scaled spherical coordinate has density (2) and the stated two-sided polylogarithmic moderate tail. | Existence | Lemma 1, p. 2 |
| C04 | Expansion and independence give the exact probability reduction (4). | Causal/existence | pp. 2--3 |
| C05 | The two Borel--Cantelli implications yield the almost-sure classification. | Causal | p. 3 |
| C06 | Bignamini, Casini, and Martinelli study high-dimensional isotropic Pearson walks in a general framework. | Attribution | p. 1 |
| C07 | Their Example 6.5 treats the family with second length d^beta X_d and proves failure at beta=1/2. | Attribution/statistic | p. 1 |
| C08 | Zeng's cited 2026 SSRN item studies a different combinatorial-probability monotonicity question. | Attribution/temporal | p. 3 and reference [2] |

## Pass 2: verification

| ID | Status | Evidence and scope |
|---|---|---|
| C01--C05 | Verified | These are the paper's proved mathematical claims, not imported citation claims. They match the accepted frozen claim and `audit/math.md`; the release read found no strengthening beyond that scope. |
| C06 | Verified (paraphrase) | The official arXiv record for arXiv:2609.05195v1 gives the exact title, three authors, 2026-09-04 submission date, math.PR category, and abstract describing the general high-dimensional Pearson-walk framework. |
| C07 | Verified (exact) | The original 11-page v1 PDF, SHA-256 `1ceef2b47efc66235d08f814a56b7006b21d3948423c2432f5f91841c16535b8`, states in Example 6.5 on pp. 10--11 that the second length is d^beta X_d and proves nonconvergence at beta=1/2; the preceding text also identifies beta<1/2 as the sufficient range for Theorem 5.6. |
| C08 | Unverified citation access | The supplied bibliography audit records a Crossref match for DOI 10.2139/ssrn.7380519, title, author Zijian Zeng, year 2026, and SSRN target. Fresh title/author/venue/DOI searches found no primary record, direct Crossref network resolution failed, and one browser attempt timed out. The prose was narrowed to the title-level topic and expressly uses no result from the source. |

The required academic search templates were run for both records: author/year/title,
full title with arXiv/Semantic Scholar (and SSRN for the supplied record),
author/year/venue, DOI, and arXiv identifier where applicable. The authoritative
arXiv HTML record and original PDF were inspected. The fresh SSRN limitation is
bounded and disclosed rather than converted into verification.

## Publication and reference integrity

`publication.json` lists the complete authored dependency set:
`manuscript/article.tex` and `manuscript/references.bib`. The TeX source imports no
figures, local style files, or other authored TeX fragments; generated `.aux`,
`.bbl`, and `.out` files are build products. Both citation keys occur in the final
`.bbl` and render as references [1] and [2]. The clean final compiler log has no
undefined citation or reference diagnostics. The manuscript makes no novelty or
priority claim, and reference [2] is not used as mathematical evidence.

## Verdict

**Accept with citation limitations.** No contradicted attribution, undefined key,
unsupported mathematical dependence, or incomplete publication dependency was
found. The sole limitation is fresh online resolution of the supplied SSRN record.

