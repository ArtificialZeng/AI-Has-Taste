# Verification Report

**Mode:** Search verification with the explicitly invoked `citation-check-skill`  
**Document:** `manuscript/article.pdf` and its complete authored source set  
**Generated:** 2026-09-07T12:31:08+08:00

## Summary

| Metric | Count |
|---|---:|
| Total fixed claims extracted | 5 |
| Verified | 5 |
| Numerical Error | 0 |
| Citation Not Found | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Unverified | 0 |

**Overall status: PASS.** All cited or attributed claims are supported at their
stated scope. The manuscript makes no priority claim and does not promote the
finite computation to a theorem for arbitrary \(n\).

## Pass 1: fixed claim extraction

This list was frozen before source verification; Pass 2 did not add claims.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Nagy--Vajda formulate the displayed Kasami cyclic-additive conjecture with \(|\Delta|=2^{n-1}\) and triple count \(2^{2n-3}\). | Attribution + statistic | p. 1, Context and scope |
| C02 | Nagy--Vajda prove the classes \(k\equiv\pm1,\pm2\pmod n\), verify every admissible case through \(n\le13\), and prove the \(k\leftrightarrow n-k\) Frobenius transfer. | Attribution + existence | p. 1, Context and scope |
| C03 | At \(n=14\), the admissible residues are \(1,3,5,9,11,13\); the prior results cover \(1,13\) and pair \(3\leftrightarrow11\), \(5\leftrightarrow9\), so the two tested representatives complete the next finite layer relative to that source. | Derived comparative + statistic | p. 1, Context and scope |
| C04 | Zeng--Liu--Ratnavelu separate an exact finite-field boundary theorem from a companion exact-arithmetic verifier in an unrelated permanent-rank problem. | Attribution + comparative | p. 1, Context and scope |
| C05 | Nagy--Vajda's \(n\le13\) verification and structural reductions are the closest technical comparison actually used in this manuscript. | Comparative | p. 4, Limitations |

The theorem, certificate dimensions, field encoding, direct-check parameters,
and exact counts elsewhere in the note are statements of the accepted frozen
result rather than literature attributions. They agree with `claim.json` and
the accepted report `audit/math.md`; no unsupported strengthening was found.

## Pass 2: source verification

| ID | Status | Primary-source support | Confidence |
|---|---|---|---|
| C01 | Verified | Nagy--Vajda, arXiv:2608.18584v2, Conjecture 1.1 (PDF pp. 1--2), states the same hypotheses, set, ordered-triple relation, and exact count. | exact |
| C02 | Verified | Theorem 7.1 and Corollary 11.12 prove \(\pm1\) and \(\pm2\); Lemma 3.5 proves Frobenius transfer; Section 12/Table 1 and Theorem 13.1(6) give exhaustive coverage for every admissible \((n,k)\) with \(n\le13\). | paraphrase |
| C03 | Verified | The residue list follows exactly from \(\gcd(k,14)=1\); Theorem 7.1 and Lemma 3.5 give the stated coverage and pairings. The conclusion is expressly relative to Nagy--Vajda's coverage, not a global priority assertion. | interpretation |
| C04 | Verified | The official Preprints.org record gives the finite-field boundary theorem, separates the permanent-rank cases, and its Data Availability Statement identifies an exact-arithmetic companion verifier; it also confirms authors, version 1, posting date 18 August 2026, and non-peer-reviewed status. | paraphrase |
| C05 | Verified | The cited source contains the immediately preceding form of the same conjecture, character reduction, finite verification boundary, and Frobenius transfer. A bounded exact-phrase search on 2026-09-07 found no equivalent cyclic-additive \(n=14\) report; the manuscript nevertheless disclaims priority. | interpretation |

The academic-citation search templates were run for both entries: author/year
and title-fragment, full title constrained to scholarly archives, author/year
and venue, DOI, and arXiv identifier where applicable. The arXiv abstract cache
temporarily displayed only the older v1 history, but the current authoritative
PDF itself is marked `arXiv:2608.18584v2 [math.CO] 4 Sep 2026` and contains the
passages checked above. Direct DOI opening was unavailable in this environment;
the official arXiv and Preprints.org records supplied the same metadata and full
claim text, so this bounded access limitation does not leave an unsupported
claim.

## Sources consulted

| Source | Type | URL | Used for |
|---|---|---|---|
| G. P. Nagy and A. Vajda, *On a conjecture on the Kasami APN function*, arXiv:2608.18584v2 (2026) | Primary manuscript and official record | https://arxiv.org/pdf/2608.18584 | C01--C03, C05 |
| Z. Zeng, H. Liu, and K. Ratnavelu, *Closing the Permanent-Rank Boundary for the Alon--Jaeger--Tarsi Conjecture*, v1 (2026) | Official publisher full text | https://www.preprints.org/manuscript/202608.1194 | C04 |
| `literature/user_bibliography_check.md` | User-list selection audit | local project artifact | confirms that the second paper came from the user's cited Excel list and fixes its deliberately narrow use |

## Citation and dependency scope

The extracted PDF has two numbered references, both resolved and legible; the
BibTeX keys in `article.aux` resolve to those two entries, with no undefined
citations. The final bibliography now correctly labels Nagy--Vajda as v2.

`publication.json` lists, in sorted order, `manuscript/article.tex` and
`manuscript/references.bib`. Inspection of the TeX source, BibTeX transcript,
and recorder file found no authored `\\input`, imported figure, local style, or
other local publication dependency. The remaining recorder inputs are generated
auxiliary files or system TeX resources. The declared dependency scope is
therefore complete.
