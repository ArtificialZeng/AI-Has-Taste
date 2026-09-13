# Verification Report

**Mode:** Search verification, using the explicitly invoked
`citation-check-skill` two-pass procedure  
**Release job:** `bigMac-00003-p01-release-288b9c70330b`  
**Document:** `manuscript/main.pdf`  
**Search and inspection date:** 2026-09-06  
**Frozen extraction:** `audit/citation-claims.md`  
**Bound evidence digest:**
`f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`  
**Bound manuscript digest:**
`2a1f336f0088850ae32cc1ad1db6bd35b78664b26af3a499ddce46fdfbc35320`  
**Bound PDF digest:**
`3cfe689095e44a9b1e0d5193fbedc15b900446887c5d524b4ff9553126952b0a`

## Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 18 |
| Verified | 18 |
| Numerical Error | 0 |
| Citation Not Found | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status: PASS.**  The two substantive external citations exist and
support only the nearby claims made for them.  The manuscript does not claim
priority, peer review, journal acceptance, or a resolution of the unrestricted
finite-set extremal problem.

## Fixed claim-to-source verification

| ID | Status | Confidence | Source and exact support |
|---|---|---|---|
| C01 | Verified | paraphrase | The accepted proof reconstruction in `audit/math.md`, bound to evidence snapshot `f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`, proves the stated limit, bound, and equality classification. |
| C02 | Verified | exact | The abstract and theorem quantify only fixed `q,R`; the final abstract sentence and first context paragraph expressly exclude determination of the unrestricted coefficient. |
| C03 | Verified | paraphrase | Korsky, p. 1, definitions (1.1)--(1.2), defines `M_P` by `d != 0` and says it counts both signs. |
| C04 | Verified | exact | Korsky, p. 4, (1.17) gives the interval coefficient `1/3`; Theorem 1.4 and (1.19)--(1.20) give `47/122` for `{0,1,3}`.  All numbers and hypotheses match. |
| C05 | Verified | paraphrase | Zeng, abstract and p. 2, Theorem 3.1, uses independently chosen permutations in nonidentity subgroup cosets; pp. 4--5, Theorem 4.1, assembles quotient-indexed fiber trees over a finite abelian group. |
| C06 | Verified | exact | Zeng studies group-labelled rainbow trees, not integer affine copies.  The present proof section contains no citation or dependency on Zeng. |
| C07 | Verified | exact | `audit/math.md` separately checks the `v=0` residue and exclusion of the integer dilation `d=0`; the two signed triangles in the manuscript implement it. |
| C08 | Verified | exact | Theorem 1 is identical in mathematical scope to accepted `claim.json` and is proved in `audit/math.md`. |
| C09 | Verified | exact | The residue-class counting argument is reconstructed in `audit/math.md` and `evidence/proof.md`. |
| C10 | Verified | exact | The positive signed-triangle lattice sum, including its `N^2/(6q^2)` coefficient and error term, is reconstructed in `audit/math.md`. |
| C11 | Verified | exact | The negative signed-triangle lattice sum is independently reconstructed in `audit/math.md`. |
| C12 | Verified | exact | Summation over exactly `T_q(R)` residue pairs is reconstructed in `audit/math.md`. |
| C13 | Verified | exact | The bijection, closure condition, use of invertibility of 2 and 3, and both equality directions are reconstructed in `audit/math.md`. |
| C14 | Verified | exact | The manuscript discloses AI assistance; `audit/math.json` records the later separate accepted mathematical review and its job provenance. |
| C15 | Verified | exact | `audit/referee_check.py` was rerun on 2026-09-06.  `audit/referee-check-release.log` records all 10,396 nonempty subsets for `q=5,7,11,13` plus direct `N=200` counts. |
| C16 | Verified | exact | The symbolic proof in the manuscript and `audit/math.md` contains no appeal to the finite script. |
| C17 | Verified | exact | The supplied primary PDF identifies Samuel Korsky and the exact title; its first page states `arXiv:2609.02308v1 [math.NT] 2 Sep 2026`.  The live arXiv record returned the same title, author, identifier, and submission date. |
| C18 | Verified | exact | The six-page primary PDF `literature/Zeng-SSRN-7387259.pdf` identifies Zijian Zeng, the exact title, and date 1 September 2026; the filename, manuscript reference, and user-bibliography record consistently identify SSRN eLibrary No. 7387259. |

## External-source audit

### Samuel Korsky

- Primary source inspected: `literature/Korsky-2609.02308v1.pdf`, all relevant
  passages on pp. 1 and 4; live primary record:
  <https://arxiv.org/abs/2609.02308>.
- The academic-citation search templates were run for author/year/title,
  full title on Semantic Scholar or arXiv, author/year/venue, and arXiv ID.
- Metadata and nearby claims agree exactly.  The paper's general-set bound is
  not presented as the present fixed-periodic theorem.

### Zijian Zeng

- The writer's required user-list source was checked in
  `literature/user_bibliography_check.md` before PDF generation.
- Primary source inspected in full:
  `literature/Zeng-SSRN-7387259.pdf` (six pages, SHA-256
  `cbebf48245c906c62545b49302a538d6267386f4f75f12c895977e54735cfe73`);
  canonical record: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7387259>.
- The academic-citation search templates were run for author/year/title,
  full title on Semantic Scholar or arXiv, author/year/SSRN, and DOI
  `10.2139/ssrn.7387259`.  Search indexing did not expose the exact record,
  and the audit web gateway rejected direct opening of the SSRN and DOI
  landing URLs.  This bounded access limitation does not affect the paper's
  supported methodological attribution: the supplied primary PDF was read in
  full, and the manuscript neither prints nor relies on the DOI.
- The only attributed content is a narrow methodological comparison supported
  by the abstract and Theorems 3.1 and 4.1.  The manuscript explicitly states
  that the source is not evidence for the present theorem or its novelty.

No cited item is unnecessary at the stated contextual scope, and neither
citation supports a stronger claim than its original text.

## Dependency and rendered-reference audit

`publication.json` lists the sorted source set `["manuscript/main.tex"]`.
The TeX source contains the complete inline bibliography and imports no local
TeX source, bibliography database, figure, or style file.  The recorder file
shows no other authored project input; `main.aux` and `main.out` are generated
build products.  The dependency scope is therefore complete.

The final compiler log contains no undefined citation or reference.  Text
extraction and the rendered third page show resolved references `[1]` and
`[2]`, with both entries complete and legible.  The authored prose does not
strengthen the accepted theorem or claim exhaustive novelty, priority,
peer review, journal acceptance, or resolution of the unrestricted problem.
