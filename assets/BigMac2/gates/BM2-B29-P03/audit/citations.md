# Fresh citation and claim-support audit

## Bound artifact

- Release job: `bigMac-00029-p03-release-c1fda9dfb459`.
- Evidence snapshot: `742b93162211e835fe67ffd8e2ed442a562f83e734d6b3030d5534c3dd21d7f5`.
- Manuscript snapshot: `e5e03004830aff9dab501eb34a552ddcc086782f9fb316694afae43b5ddcf856`.
- PDF: `09e3f5ce396a5ad4c2127b40e9d26512f5c0fb27fb87c6a3da73d2e9732a2819`.
- Search and inspection date: 2026-09-09 (Asia/Shanghai).

I explicitly applied `citation-check-skill` v2 as an advisory search-mode
check.  Its extraction and verification passes were kept separate.  The
user-designated workbook remains authoritative for the metadata it supplies.

## Pass 1: frozen extraction

The following citation-dependent or externally checkable claims were fixed
before verification.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Bartzos and Samaris study bounds and exact data for Eulerian orientations of classes of 4-regular graphs. | attribution/existence | p. 1, context |
| C02 | Their inspected arXiv v1 exhaustive table ends at order 15. | attribution/temporal | p. 1, context |
| C03 | Their Conjecture 1 gives the order-16 value `floor(48^(19/7)/4)=9147`. | attribution/statistic | p. 1, context |
| C04 | Their equality construction concerns orders congruent to 4 modulo 7 and does not settle order 16. | attribution | p. 1, context |
| C05 | McKay--Piperno is an appropriate source for the nauty graph-isomorphism/canonical-generation software used by the census. | attribution/existence | pp. 2--4 |
| C06 | The user-designated bibliography contains an unrelated fixed-order line-graph manuscript devoted to exact verification. | attribution/existence | p. 2 |
| C07 | The present theorem is only a finite-order refinement relative to the inspected source; no global priority is claimed. | comparative/scope | p. 1 |
| C08 | All three citations and bibliography records resolve inside the compiled PDF. | existence | pp. 1--2 and 5 |

The theorem, exact census data, graph6 string, and arithmetic claims were also
checked for consistency with the accepted frozen claim and evidence.  They are
not presented as consequences of the bibliography.

## Pass 2: verification

| ID | Status | Evidence and finding |
|---|---|---|
| C01 | Verified (paraphrase) | The title page, abstract, and introduction of arXiv:2609.06701v1 identify Evangelos Bartzos and Michalis Samaris and describe bounds, exact computations, and separable 4-regular graphs. |
| C02 | Verified (exact) | Table 1 in the primary PDF lists orders 5 through 15, and the surrounding text says the exhaustive computation covers all simple 4-regular graphs with at most 15 vertices. |
| C03 | Verified (exact) | Conjecture 1 states `|E(G)| <= 2^-2 48^((n+3)/7)`.  Substitution `n=16` gives `48^(19/7)/4`; exact integer comparison gives floor 9147. |
| C04 | Verified (exact) | Theorem 5 states `n = 4 (mod 7)` and gives the equality-family count.  Since 16 is not 4 modulo 7, the manuscript's qualification is correct. |
| C05 | Verified (paraphrase) | McKay and Piperno, *Practical Graph Isomorphism, II*, J. Symbolic Computation 60 (2014), 94--112, DOI `10.1016/j.jsc.2013.09.003`, describes nauty and canonical graph-isomorphism methods.  Metadata agrees across the arXiv primary record (1301.1493), DOI-indexed record, and BibTeX. |
| C06 | Accepted from user record -- external refresh unavailable | `literature/user_bibliography_check.md` records workbook `Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`, worksheet row `数学主表!A12:F12`, its SHA-256, title, author, year, DOI, and URL.  Searches by author/title, full title, venue/topic, and DOI did not return the designated record.  Under the explicit authority override, `metadata_basis=user_designated_workbook`.  The prose was narrowed before the final build to the title-level exact-verification comparison and expressly disclaims uninspected methodological detail. |
| C07 | Verified as bounded wording | The primary source stops at order 15; the manuscript resolves order 16 and expressly avoids a global priority claim.  No broader novelty assertion appears. |
| C08 | Verified (exact) | The final Biber run found all three keys.  Extracted PDF text contains citations `[1]`, `[2]`, `[3]` and complete bibliography entries; the final compiler log has no undefined citation or reference. |

Applicable academic search templates were run for each record: author/year/title
terms, quoted full title with arXiv/Semantic Scholar restriction, author/year/
venue terms, DOI where supplied, and arXiv identifier where supplied.  The
primary Bartzos--Samaris PDF at
`/Users/mac/4prove-or-disprove-math/batches/literature/bigMac-29/2609.06701v1.pdf`
was inspected directly, including Table 1, Theorem 5, and Conjecture 1.

## Dependency and scope checks

`publication.json` declares exactly `manuscript/article.tex` and
`manuscript/references.bib`.  Inspection of the TeX source and recorder file
found no authored `input`, `include`, local style, figure, or other undeclared
dependency.  The PDF is not listed as a source, and the build log is separately
bound by the build audit.  Every citation key in the TeX source exists once in
the BibTeX database.  The references visible on page 5 agree with the final
database.  The abstract, theorem, proof, and equality classification do not
strengthen the accepted mathematical claim.

## Verdict

**Accept.**  Citation keys and nearby claims are supported at their stated
scope.  The inaccessible refresh of the user-designated workbook record is
recorded without treating that record as nonexistent; the manuscript makes no
claim beyond the supplied metadata and title-level relevance.
