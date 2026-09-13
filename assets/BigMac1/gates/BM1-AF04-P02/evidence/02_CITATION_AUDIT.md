# Verification Report

**Mode:** Search  
**Document:** `paper/main.tex` (frozen claim set C01--C14)  
**Generated:** 2026-08-30 (Asia/Shanghai)

## Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 14 |
| Verified | 14 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Citation Not Found | 0 |

**Overall Status:** PASS: all frozen claims are verified at the stated scope.

The audit deliberately treats C04 as a bounded search-process statement: it
verifies that the recorded searches did not locate a prior statement of the
diameter.  It does **not** assert universal nonexistence of such a statement.

## Verified claims

| ID | Frozen claim | Evidence | Location | Confidence |
|---|---|---|---|---|
| C01 | There are 80 isomorphism classes of STS(15). | Cole--Cummings--White; Mathon--Phelps--Rosa; official DesignTheory.org complete catalogue | PNAS 3 (1917), 197--199; *Ars Combin.* 15 (1983), 3--110; database row `2,15,35,7,3,1`, content `a`, count 80 | exact |
| C02 | Gibbons obtained the 79-class Pasch-connected component, and Grannell--Griggs--Murphy verified it and published the switch table. | Gibbons thesis metadata; Grannell--Griggs--Murphy primary PDF | thesis record; 1999 paper pp. 3--6 and Appendix | paraphrase |
| C03 | The anti-Pasch class is unique. | Grannell--Griggs--Murphy primary PDF | Section 3: system 80 is the only 4-cycle-free STS(15); Appendix count 0 | exact |
| C04 | No stated diameter was located in the recorded literature search. | Two-pass query log plus full-text searches | `literature/search_log.md`, entries 1--21; 1999 PDF searched for `diameter` and `radius` | exact as bounded process claim |
| C05 | The reconstructed simple quotient has 80 vertices, 258 edges, components 79+1, diameter 11 on the large component, and radius 6. | Independent exact replay and graph-only BFS | `certificate/result.json`; `code/independent_verifier.py`; `code/verify_bfs.py` | exact |
| C06 | The released 80 representatives canonically equal the official catalogue. | Catalogue cross-check using independently downloaded data | `certificate/catalog_crosscheck.json`, `canonical_sets_equal=true`; compressed SHA-256 `11310c7e...f2c9` | exact |
| C07 | Discovery used nauty 2.9.3 canonical labelling. | Executable/version provenance and upstream nauty source | `certificate/discovery_provenance.json`; McKay--Piperno (2014); nauty site reports 2.9.3 | exact |
| C08 | A 4-cycle in the two-point cycle graph gives a Pasch switch. | Grannell--Griggs--Murphy; Kaski--Mäkinen--Östergård | 1999 paper, pp. 3--4; 2011 paper, switching definition | exact |
| C09 | The representatives contain 1,390 Pasch occurrences, and all 80 point-Pasch signatures are distinct. | No-nauty independent enumerator and exact serialized replay | `certificate/result.json`; verifier stdout and signature checks | exact |
| C10 | There are 83 self-switch occurrences and 258 deduplicated nonloop edges, each witnessed in both directions. | Full occurrence replay and witness consistency tests | `certificate/switch_occurrences.json`; independent verifier | exact |
| C11 | Exactly two diameter pairs occur; the displayed path has length 11 and the displayed layer sizes are correct. | All-pairs BFS from serialized edge list | `certificate/result.json`; independent and standalone BFS verifiers | exact |
| C12 | Six specified corruptions are rejected while the unmodified certificate is accepted. | Fail-closed mutation suite | `certificate/negative_tests.json`, all six `rejected=true`, `baseline_accepted=true` | exact |
| C13 | Erskine--Griggs (2025) has a different endpoint concerning order 19. | Publisher version and arXiv abstract | DOI 10.1002/jcd.21975; arXiv:2405.07750 | exact |
| C14 | Certification uses no nauty, floating point, randomness, optimizer, or proof assistant. | Source inspection, import inspection, and disclosed commands | `code/independent_verifier.py`; `code/verify_bfs.py`; manuscript computational disclosure | exact |

## Numerical errors

None.

## Hallucinations

None.

## Unverified claims

None at the bounded scope used in the manuscript.

## Misleading claims and corrections made

The draft phrase “the smallest nontrivial Steiner trade” was not needed for
the result and was removed because the cited sources were being used for the
cycle-switch definition, not for a minimal-trade theorem.  The Mathon--Phelps--
Rosa bibliography entry was augmented with its published erratum.

## Sources

| ID | Citation | Type | URL | Used for |
|---|---|---|---|---|
| S01 | Cole, Cummings, White (1917), *The Complete Enumeration of Triad Systems in 15 Elements* | primary journal article | https://pmc.ncbi.nlm.nih.gov/articles/PMC1091209/ | C01 |
| S02 | Mathon, Phelps, Rosa (1983), *Small Steiner Triple Systems and Their Properties* | primary journal article/catalogue | https://combinatorialpress.com/ars/vol15/ | C01 |
| S03 | Gibbons (1976), *Computing Techniques for the Construction and Analysis of Block Designs* | doctoral thesis record | https://library-archives.canada.ca/eng/services/services-libraries/theses/Pages/item.aspx?idNumber=15826048 | C02 |
| S04 | Grannell, Griggs, Murphy (1999), *Switching Cycles in Steiner Triple Systems* | author-hosted primary PDF | https://grannell.net/Papers/SWITCH2.pdf | C02, C03, C04, C08 |
| S05 | Kaski, Mäkinen, Östergård (2011), *The Cycle Switching Graph of the Steiner Triple Systems of Order 19 Is Connected* | institutional metadata and author PDF | https://researchportal.helsinki.fi/en/publications/the-cycle-switching-graph-of-the-steiner-triple-systems-of-order-/ | C02, C08 |
| S06 | McKay, Piperno (2014), *Practical Graph Isomorphism, II* | journal article / arXiv | https://arxiv.org/abs/1301.1493 | C07 |
| S07 | DesignTheory.org, t-design database | official exact catalogue | https://webspace.maths.qmul.ac.uk/l.h.soicher/designtheory.org/database/t-designs/ | C01, C06 |
| S08 | Erskine, Griggs (2025), *Cycle Switching in Steiner Triple Systems of Order 19* | publisher version / arXiv | https://onlinelibrary.wiley.com/doi/10.1002/jcd.21975 | C04, C13 |

## Search-template compliance

For every academic citation, the audit ran all applicable queries required by
the citation-check gate: first-author/year/title prefix; full title restricted
to Semantic Scholar or arXiv; first-author/year/venue; DOI when present; and
arXiv identifier when present.  Search-engine misses were followed by direct
primary, publisher, institutional-repository, or official-database inspection.
The 1999 paper was inspected in full rather than accepted from metadata alone.
