# Citation and claim verification report

**Mode:** Search verification (two-pass `citation-check-skill` workflow)  
**Document:** `manuscript/main.pdf` and its authored dependencies  
**Checked:** 2026-09-07 (Asia/Shanghai)  
**Overall status:** PASS

## Pass 1: fixed extraction

Extraction was completed before source verification. The external or
scope-sensitive claims requiring citation review were fixed as follows:

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Jan Snellman's 2026 paper has the title, author, arXiv identifier, version, and subject metadata recorded in the bibliography. | Existence + attribution + temporal | Reference [1] |
| C02 | Snellman gives a signed cross-product encoding for iterated commutators of 2-by-2 matrices over characteristic not two and isolates the characteristic-two model as Problem 5, Question 1. | Attribution | Section 1, paragraph 1 |
| C03 | The cited source treats separately the model-existence question and later ideal-theoretic conclusions for the independently defined recursion. | Attribution + existence | Section 1, paragraph 1; Section 4 |
| C04 | The Zeng--Liu--Ratnavelu paper has the title, authors, year, venue/version, DOI, and non-peer-reviewed status recorded in the bibliography. | Existence + attribution + temporal | Reference [2] |
| C05 | Zeng, Liu, and Ratnavelu use exact 2-by-2 rank-one matrices to disprove a distinct Schatten-norm conjecture. | Attribution | Section 1, final paragraph |
| C06 | That comparison paper does not supply results about Lie brackets, exterior squares, cross products, or characteristic two and is used only as a methodological comparison. | Attribution/scope | Section 1, final paragraph |
| C07 | The manuscript's main theorem is exactly the accepted frozen claim and does not strengthen it to the source paper's separate ideal-theoretic questions. | Scope consistency | Abstract, Theorem 1, Section 4 |

Definitions, proof-method descriptions, the assistance disclosure, and
explicitly bounded statements declining a priority claim were not treated as
external factual claims. The mathematical identities in the proof are not
literature-dependent; C07 checks their asserted scope against the accepted
mathematical audit rather than pretending that a web search certifies them.

## Pass 2: verification of the fixed claims

| ID | Status | Primary evidence and exact support | Confidence |
|---|---|---|---|
| C01 | Verified | The official arXiv record for `2609.05386v1` gives Jan Snellman, the title *The coordinate ring of the k-fold iterated commutator locus for 2x2 matrices*, category `math.AC`, and submission time 4 September 2026. The inspected v1 PDF has SHA-256 `a145e011531ca69992b9cb732d3e3035fccb873083cbffe049f1dcc7740b04c8`, matching `source.md`. | exact |
| C02 | Verified | The original v1 PDF, pp. 6--7, gives “Problem 5: characteristic 2” and “Question 1: a twisted-cross-product model in characteristic 2”; it asks for an isomorphism gl2/(FI) to F^3 carrying the induced bracket to E(cross product) for invertible E. Its setup and Theorem 3.1 give the signed cross-product encoding, under the paper's standing characteristic-not-two scope for the subsequent results. | exact |
| C03 | Verified | The source explicitly says its finite-field computations bear only on the second half of Question 1 and cannot settle whether the bracket model exists. The manuscript correspondingly answers only model existence and disclaims the later ideal-theoretic conclusions. | paraphrase |
| C04 | Verified | The official Preprints.org manuscript record `202608.1067` gives Zijian Zeng, Houde Liu, and Kurunathan Ratnavelu in that order; title, version 1, submitted 16 August and posted 17 August 2026; and labels the version not peer reviewed. The DOI displayed there is `10.20944/preprints202608.1067.v1`. The official arXiv record `2608.15558` independently confirms title, authors, and 16 August 2026 submission. | exact |
| C05 | Verified | The official Preprints.org abstract and the arXiv abstract/Theorem 1.1 state that two explicit real 2-by-2 rank-one matrices at p=3/2 disprove the Tang--Zhang conjecture, with an exact rational certificate. | paraphrase |
| C06 | Verified | The comparison paper's title, abstract, keywords, theorem list, and full section structure concern Schatten norms, matrix absolute values, rank-one matrices, and trace inequalities. No result there is invoked for the present bracket proof; the manuscript expressly limits the citation to method. | interpretation (conservative scope check) |
| C07 | Verified | The abstract and Theorem 1 reproduce the quantified field-uniform nonexistence and exact rank-two statement in `claim.json`. Section 4 preserves the accepted limitation. This agrees with `audit/math.json` and `audit/math.md`; the citation audit does not enlarge that mathematical acceptance. | exact scope match |

No numerical value from either cited paper is imported into this manuscript.
Both numbered citations resolve in the extracted PDF, and both bibliography
entries are present in the rendered reference list. There are no undefined
citations and no citation-dependent mathematical step.

## Searches and source access

The academic-citation query templates were run on 2026-09-07 for each entry:
author/year/title words; full title restricted to arXiv/Semantic Scholar;
author/year/venue; DOI where supplied; and arXiv identifier where supplied or
available. Primary pages inspected were:

- `https://arxiv.org/abs/2609.05386` and `https://arxiv.org/html/2609.05386`;
- the original arXiv v1 PDF identified in `source.md`, especially pp. 6--7;
- `https://www.preprints.org/manuscript/202608.1067`;
- `https://arxiv.org/abs/2608.15558` and `https://arxiv.org/html/2608.15558`.

The generic DOI-resolver opens returned an access/tool error during this
bounded audit. This did not leave metadata unsupported: the official
Preprints.org record displays the DOI and complete version metadata, while the
official arXiv record independently confirms the paper and its nearby claim.
No priority inference is drawn from search coverage.

## Dependency and output audit

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`. The clean build recorder (`manuscript/main.fls`)
shows no other project-local authored input: the other local inputs are
generated `.aux`, `.out`, and `.bbl` files. Thus the explicit dependency
scope is complete. The checked-source list in `audit/citations.json` is the
exact sorted `source_files` list. Text extraction and the rendered pages show
references [1] and [2] resolved and legible.

