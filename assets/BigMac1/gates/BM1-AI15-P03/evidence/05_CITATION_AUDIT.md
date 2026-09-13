# Citation and claim verification report

**Mode:** Search verification, strict academic precision  
**Document:** `paper/main.tex` and rendered five-page PDF  
**Generated:** 2026-08-29 (Asia/Shanghai)

## Summary

| Metric | Count |
|---|---:|
| Fixed claims extracted in pass 1 | 10 |
| Verified | 10 |
| Numerical error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status: PASS.**  The search-scope novelty sentence is classified as
an interpretation, not as an absolute priority claim.  The new theorem is
verified by the exact internal proof and independent certificates rather than
by an external citation.

## Fixed pass-1 claim list and pass-2 decisions

| ID | Claim | Type/location | Status | Evidence and exact location | Confidence |
|---|---|---|---|---|---|
| C01 | A383733 counts proper three-colourings of the generalized chorded cycles used here. | Attribution, Introduction | Verified | OEIS A383733, title, COMMENTS, and executable Maple/Mathematica edge construction. | exact |
| C02 | Lopez-Bonilla et al. derived an odd-order closed form and used transfer-matrix methods. | Attribution, Introduction | Verified | DOI 10.9734/jamcs/2025/v40i102060, abstract and Theorem 3.4; arXiv:2509.05845 abstract. | paraphrase |
| C03 | The published table contains zeros at 7, 8, 12, 16 but does not prove absence of later zeros. | Attribution/existence, Introduction | Verified | DOI paper, Table 2 and Section 6.  The paper's later Conjecture 6.3 is internally inconsistent (it wrongly includes 11), so the manuscript deliberately makes only the weaker table statement. | exact for the four displayed zero entries; paraphrase for the limitation |
| C04 | The SciNet artifact checks the proposed zero set through n=3000. | Statistic/attribution, Introduction | Verified | SciNet finding a760d2f8, Claims 1 and 4: bigint-exact to 400 and two-prime nonzero certification thereafter to 3000; pinned GitHub commit b873c297e21bcd6ac973f1190a82a857010f8556. | exact as an author/computational report |
| C05 | SciNet posed the all-order classification separately. | Attribution/existence, Introduction | Verified | SciNet problem 69d6d14f, lines 14--19 and state ACTIVE at the audit date; the finite finding says the exact all-order proof is a companion problem. | exact |
| C06 | No prior all-order proof or counterexample was found in the recorded search scope through 2026-08-29. | Temporal/existence, Introduction | Verified within stated scope | Two recorded search passes in `literature/search_log.md`: OEIS, arXiv, DOI/Crossref, OpenAlex, SciNet, GitHub, and exact final-wording/block queries.  The manuscript expressly disclaims a global-priority guarantee. | interpretation |
| C07 | At n=6 the offset-three edges coincide with the diameters. | Attribution/statistic, Section 2 | Verified | OEIS A383733 EXAMPLE and executable definition explicitly list (0,3), (1,4), (2,5) for both edge types and note the coincidence. | exact |
| C08 | The four displayed colour-word families cover every n>=6 outside 7,8,12,16. | Original existence claim, Proposition 3.1 | Verified | Human proof checks the only two local seams, the alternating family, coordinatewise diameter pairs at n=20, and all k>=6; independent direct-edge verifier checks through n=10000. | exact proof |
| C09 | The four exceptional graphs are not three-colourable. | Original nonexistence claim, Proposition 4.2 | Verified | Difference-word equivalence, cyclic run bound, and discrete half-window intermediate-value proof; two independent exact enumeration programs reproduce the zeros. | exact proof |
| C10 | The archived diagnostic reports PASS, 9,991 constructed orders, and 128/256/4096/65536 sign words exhausted. | Statistic, Section 5 | Verified | Re-run of `certificates/verify_builder_construction.py --max-n 10000`; JSON record `results/builder_verifier_10000.json`; counts equal 2^7, 2^8, 2^12, 2^16 exactly. | exact |

## Mandatory search templates executed

For the journal citation, all applicable academic templates were run:

1. `Lopez-Bonilla 2025 Chromatic Polynomials C n 3 Graphs`
2. exact full title restricted to `arxiv.org` or `journaljamcs.com`
3. first author, year, and journal title
4. `doi:10.9734/jamcs/2025/v40i102060`

For the database/problem/artifact records, exact official-domain queries were
run for OEIS A383733, SciNet problem 69d6d14f, SciNet finding a760d2f8, and
the pinned GitHub artifact.  Direct official records were then inspected.

## Sources consulted

| ID | Source | Type | URL | Used for |
|---|---|---|---|---|
| S1 | OEIS A383733 | official sequence record | https://oeis.org/A383733 | C01, C07 |
| S2 | Lopez-Bonilla et al. (2025) | publisher/DOI journal article | https://doi.org/10.9734/jamcs/2025/v40i102060 | C02, C03 |
| S3 | arXiv:2509.05845v1 | original preprint record | https://arxiv.org/abs/2509.05845 | C02, historical cross-check only |
| S4 | SciNet problem 69d6d14f | official problem record | https://api.scinet.pub/p/69d6d14f-32c0-4de4-933e-9d4b4ab99e2a | C05, C06 |
| S5 | SciNet finding a760d2f8 | official finding record | https://api.scinet.pub/f/a760d2f8-717e-4d44-b3b9-86f30957a285 | C04, C05 |
| S6 | SciNet math-combinatorics commit b873c297 | public code artifact | https://github.com/scinet-ai/math-combinatorics/commit/b873c297e21bcd6ac973f1190a82a857010f8556 | C04 |
| S7 | Local exact proof and three verifiers | primary project evidence | `proof/`, `certificates/`, `verification/`, `verifier/` | C08--C10 |

## Citation hygiene

`audit_latex.py` reports `cited=4 bib=4 missing=0 unused=0`.  All four
bibliography records exist, metadata for the journal item agree with the DOI
landing page (volume 40, issue 10, pages 79--98, publication 2025-11-01), and
each nearby statement is no stronger than its source.  No verbatim quotation
from a source is used in the manuscript.
