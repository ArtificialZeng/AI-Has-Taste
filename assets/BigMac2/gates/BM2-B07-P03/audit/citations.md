# Verification Report

**Mode:** Search and accepted-evidence comparison, using `$citation-check-skill` as an advisory audit.
**Document:** `manuscript/main.tex` and freshly rebuilt `manuscript/build/main.pdf`.
**Overall status:** Accept. All 25 extracted claim groups are supported at their stated scope; no numerical error, contradicted attribution, unsupported strengthening, or undefined citation was found. One DOI uses the designated workbook authority because external refresh is unavailable.

Job: `bigMac-00007-p03-release-81cefd28b28f`. Reviewed: 2026-09-08T01:29:21.569617+00:00.

Evidence snapshot: `cde79d0ffca4c534449707d908f5983ea532054c14cc11a1f03e5d6913fcb0c1`.
Manuscript digest: `01fa45de2f853484308b276235d642c8f28098bd86c264922d2333c9e4dae501`.
PDF digest: `f363137820632afdb2f4d961be62835e867bc9334e9a32269a8566997f37cd4a`.

## Scope and two passes

Pass 1 read the whole manuscript and fixed `audit/citation-extraction.md` before external verification. Pass 2 checked those claims in their recorded order, using primary texts for external attributions and the accepted proof/certificates for the manuscript's own mathematics. No new mathematical acceptance is asserted by this release review. The user's instruction to perform one autonomous bounded job controls over the advisory skill's confirmation pause. No agent or other Codex process was launched.

The sole authored compilation dependency is `manuscript/main.tex`, including its inline bibliography. The fresh recorder lists only that source and generated `main.aux`/`main.out` within the project. No imported TeX, local style, external bibliography or figure is omitted. All four citation keys are defined and cited, and all cross-reference keys resolve. Both tables were compared value by value with the frozen data, and all twelve printed generator arrays agree literally. See `audit/release-content-check.md` for the fresh checks. Rendered citations and references on pages 1–5 agree with the source; no question marks or missing symbols occur.

## Primary-source mapping (search date 2026-09-08)

- **S1, Gagarin–Zverovich:** [arXiv record](https://arxiv.org/abs/1209.1362), [original PDF](https://arxiv.org/pdf/1209.1362), and [author publication list](https://socs.acadiau.ca/~agagarin/results.html). PDF page 1 abstract and page 2 Conjecture 1 support the conservative upper-bound context and the historical inequality. The arXiv journal-reference and related-DOI fields confirm Discrete Mathematics 313 (2013), 796–808 and DOI 10.1016/j.disc.2012.12.018. Its surface-specific bounds are not imported as the present theorem. An HTML endpoint failed; the PDF was accessible.
- **S2, McKay–Piperno:** [original text](https://arxiv.org/html/1301.1493v1), Introduction and Sections 2–3, supports the canonical-labelling/isomorphism attribution. The [ANU publication record](https://researchportalplus.anu.edu.au/en/publications/practical-graph-isomorphism-ii/) confirms both authors, Journal of Symbolic Computation 60, 94–112, January 2014, and DOI 10.1016/j.jsc.2013.09.003. The 2013 arXiv date and 2014 journal year are distinct and correctly used. This reference documents methods; it does not substitute for the actual census.
- **S3, Yavari:** [version-1 primary text](https://arxiv.org/html/2609.04257v1), Theorem 1.2, Section 3, Lemma 2.2 and Appendix A. The theorem and construction support the 18-vertex connected cubic bipartite example with gamma=6 and b=5. Lemma 2.2 supplies the fixed-set bundle criterion; equation (1)'s minimum-set consequence is also proved in the manuscript itself. The source checks its specified graph. The inspected text supplies no smaller-order exhaustive census. The corollary explicitly assumes that cited example; no independent reconstruction of its 18-vertex computation is claimed.
- **S4, Zeng–Liu–Ratnavelu–Ong:** [publisher record and full text](https://www.preprints.org/manuscript/202608.1658), version 1, Sections 3 and 6, supports symmetry reduction and separately implemented exact verification for the finite ternary graph problems. Title, four authors and order, 2026 date, and version agree with `literature/user_bibliography_check.md`. The methodological comparison is relevant to complete finite graph enumeration and certificate checking. It supports no bondage-number theorem, and none is attributed to it.

## User bibliography authority and access limit

Inspected `literature/user_bibliography_check.md`, the project-local transcription of `/Users/mac/Downloads/Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`, `数学主表!A9:F9`. No fresh workbook extraction was performed. The supplied DOI `10.20944/preprints202608.1658.v1` and BibTeX metadata are preserved exactly. **metadata_basis=user_designated_workbook; external refresh unavailable** at the direct DOI endpoint (the browser returned an internal error). Status: **Accepted from user record — external refresh unavailable**. The accessible publisher text independently supports the narrow nearby claim. This record is accepted for this workflow; it is not classified as nonexistent or unverified because the endpoint failed. One genuinely relevant paper from the designated list appears as reference [4]. No misleading extra citation is needed.

## Fixed-claim verification in order

| ID | Finding and evidence | Confidence |
|---|---|---|
| C01 | Exact full statement agrees with claim.json, the accepted math report and its frozen proof. | exact scope |
| C02 | 60 corpus records and 60 confirmations; fresh table/witness transcription checks agree. | exact |
| C03 | S1 PDF abstract and Conjecture 1 support the context and historical inequality. | paraphrase |
| C04 | S3 Theorem 1.2, Section 3 and Appendix A match all named properties. | exact |
| C05 | S3's explicit graph and verifier have that scope; this manuscript's six-order census is in its own frozen evidence. | exact scope |
| C06 | S4 Sections 3 and 6 support only the stated methodological comparison. | paraphrase |
| C07 | Cubicity and integrality give the equivalence; the accepted bounded theorem plus the explicitly assumed example gives the least order. | deduction |
| C08 | The manuscript's argument and accepted proof establish the criterion without extra hypotheses. | deduction |
| C09 | S3 Lemma 2.2 is the fixed-set criterion; the manuscript proves its displayed minimum-set consequence. | paraphrase |
| C10 | Degree counting gives equal parts; simplicity forces m>=3. The six orders agree with the accepted scope. | deduction |
| C11 | Corpus manifest paths and accepted fresh referee executable-version check agree with the printed version. | exact |
| C12 | S2 Introduction and Sections 2–3 support the attribution. | paraphrase |
| C13 | All Table 1 cells and totals recomputed from the manifest agree. | exact |
| C14 | The connected bipartition argument and census completeness are within the accepted mathematical review. | deduction |
| C15 | Manifest actually contains those executable, count, file and individual-line fields. | exact |
| C16 | Every Table 2 cell recomputed from primary_results.json agrees. | exact |
| C17 | Fresh aggregate of all records gives the five printed pairs and multiplicities exactly. | exact |
| C18 | An isomorphism bijects dominating sets and edge-deletion sets, preserving the two minima. | deduction |
| C19 | ZIP has all thirteen frozen evidence files byte-for-byte and the matching README. | exact |
| C20 | Inspected implementations, imports, checks and Python 3.10 syntax parsing support compatibility; no run on every Python minor version is implied. | code inspection |
| C21 | Corpus and accepted theorem end at 16; the cited example is excluded and dependency is explicitly disclosed. | exact scope |
| C22 | S1 arXiv metadata and author list confirm all supplied fields. | exact |
| C23 | S2 ANU publication and BibTeX fields confirm all supplied fields. | exact |
| C24 | S3 primary version header confirms author, title, identifier and year. | exact |
| C25 | S4 publisher metadata and designated workbook transcription agree; DOI accepted from the authoritative record. | exact record |

## Search coverage and limitations

Ran the academic templates for all four references: author/year/first title words; exact full title restricted to Semantic Scholar or arXiv; author/year/venue; DOI where supplied; and arXiv identifier where applicable. Queries and endpoint outcomes are in `audit/citation-search-log.md`. Broad queries returned irrelevant records; no secondary search hit was used as claim support. Direct primary records and texts resolved the substantive checks. The bounded comparison is with the cited work; it is not an exhaustive priority search. The paper expressly makes no priority claim, and the external citations do not certify its new computation. No bibliography or manuscript changes were needed. Mathematical acceptance and all frozen evidence remain unchanged.
