# Fresh citation and claim-to-source audit

## Scope and method

This release audit used the requested `citation-check-skill` as an advisory
two-pass check, followed by manual comparison with the frozen mathematical
evidence.  Pass 1 fixed the claim inventory below before any source verdicts
were assigned.  Pass 2 checked every item against the accepted referee report,
the enumerated source/log dependencies, primary web records where accessible,
and the user-designated bibliography record.  Search date: 2026-09-09.

The audit covers the complete dependency list in `publication.json`, the
rendered and extracted references in `manuscript/main.pdf`, all citation keys,
the scope of every attribution, the manuscript's bounded comparison language,
and all substantive numerical or existence assertions.  It does not claim a
global novelty search or independent peer review.

## Pass 1: fixed extraction

| ID | Claim extracted from the manuscript | Type and location |
|---|---|---|
| C01 | Every simple graph with degree sequence `(5,3^23)` has a cycle of length 4, 8, or 16. | Existence; abstract and Theorem 1 |
| C02 | The unrestricted 24-vertex minimum-degree-three problem remains unresolved, and this argument omits `(4,4,3^22)` and larger excess. | Existence/scope; abstract and Section 5 |
| C03 | The Erdos--Gyarf\'as conjecture asks whether every minimum-degree-three graph has a power-of-two cycle. | Attribution/existence; Section 1 |
| C04 | Garcia proves that every such graph on at most 23 vertices has a 4- or 8-cycle. | Attribution; Section 1 |
| C05 | Garcia records the 24-vertex cubic boundary arising from Markstr\"om; the cited results do not settle the noncubic part at order 24. | Attribution/comparative; Section 1 |
| C06 | Excess two has precisely the two sequences `(5,3^23)` and `(4,4,3^22)`. | Exact finite fact; Section 1 |
| C07 | Deleting the degree-5 vertex and its neighbourhood gives the three matching cases and the stated residual degrees and edge counts. | Mathematical existence/numerical; Lemma 2 |
| C08 | The converse attachment construction recovers every graph in each matching case. | Mathematical existence; Lemma 2 |
| C09 | Gadget relabelling leaves exactly 945, 420, and 45 attachment representatives without omissions. | Statistic/existence; Section 2 |
| C10 | nauty 2.9.3 `geng` generates the specified nonisomorphic simple graphs; `-f`, `-d2`, and `-D3` impose the stated restrictions and omission of `-c` permits disconnected graphs. | Product/existence; Section 3 |
| C11 | Residual target cycles persist under attachment, and every surviving attachment representative was tested. | Mathematical/method fact; Section 3 |
| C12 | Table 1 gives the exact three residual, survivor, attachment, and rejection rows, and every row balances. | Statistics; Table 1 |
| C13 | The complete enumeration and reduction imply Theorem 1. | Causal/mathematical; proof completion |
| C14 | The production parser, orbit enumerator, and least-vertex cycle detector have the described behavior. | Existence; Section 4 |
| C15 | Exhaustive labelled attachment enumeration agreed at 945, 420, and 45 representatives. | Statistics/comparative; Section 4 |
| C16 | The independent cycle detector agreed in 57,234 comparisons, including all 32,768 six-vertex labelled graphs for the C4 test. | Statistics/comparative; Section 4 |
| C17 | The graph6 parser agreed with `showg -a`, including a 35,063-graph shard. | Statistic/comparative; Section 4 |
| C18 | A clean rebuild and three complete reruns reproduced every table count, returned exhaustion, and produced no witness. | Existence/comparative; Section 4 |
| C19 | The verifier returns 20 on exhaustion and 10 on a witness; the named source and logs accompany the article. | Statistic/existence; Section 4 |
| C20 | Zeng separates an analytic tail from exact, independently reproduced finite checks in a cycle-length probability problem. | Attribution; Section 4 |
| C21 | No literature citation is a premise of the proof, no global priority is asserted, and the result is not an UNSAT certificate for the original problem. | Scope/existence; Sections 1 and 5 |
| C22 | The PDF bibliography contains the stated author/title/year/venue or identifier metadata for all four entries. | Bibliographic existence; references |

## Pass 2: verification

| IDs | Evidence and exact check | Status |
|---|---|---|
| C01, C07--C09, C11--C19 | `audit/math.md` reconstructs the reduction, clean-builds the frozen programs, reruns all three streams, reproduces every displayed count, and separately checks the parser, detector, and attachment enumeration.  The frozen C++ sources and three logs in `publication.json` match `audit/manuscript-snapshot.json`. | Verified, exact |
| C02, C21 | The accepted claim and referee explicitly preserve `original_status=unresolved` and identify the untouched `(4,4,3^22)` and larger-excess families.  The manuscript never strengthens the accepted scope and expressly disclaims global priority and an original-problem UNSAT certificate. | Verified, exact |
| C03 | Garcia's official arXiv v1 HTML, Introduction and abstract, gives this conjecture with minimum degree at least 3 and power-of-two cycle lengths. | Verified, paraphrase |
| C04 | Garcia, arXiv:2609.04686v1, Theorem 2.1 states exactly that every minimum-degree-at-least-three graph on at most 23 vertices has a cycle of length 4 or 8. | Verified, exact |
| C05 | Garcia's Introduction states `f(3)=24` from Markstr\"om, reports the cubic search through 28 vertices for lengths 4, 8, or 16, and Corollary 2.2 records four cubic 24-vertex graphs without 4- or 8-cycles.  Its reference list gives Markstr\"om's title, venue, volume, year, and pages.  The manuscript's claim is deliberately only a bounded comparison with those cited results. | Verified, paraphrase |
| C06 | The degree excess is a sum of nonnegative integers totalling 2; its only partitions are 2 and 1+1, giving the displayed sequences. | Verified, exact derivation |
| C10 | The official nauty and Traces site identifies release 2.9.3 and says `geng` generates nonisomorphic graphs.  The version 2.9.3 User's Guide, pp. 101--102, says `geng` generates all graphs in a specified class and documents `-f` as 4-cycle-free, `-d#` as a lower minimum-degree bound, `-D#` as an upper maximum-degree bound, and `-c` as the connected-only option. | Verified, exact/paraphrase |
| C20 | `literature/user_bibliography_check.md` is the user-designated authoritative workbook extraction.  Its supplied abstract expressly describes an analytic range and remaining exact finite checks verified by exact integer arithmetic and independent outward-rounded rational intervals.  The nearby manuscript sentence is no broader. | Verified from user-designated record, paraphrase |
| C22 | Garcia metadata and v1 date were checked on official arXiv; McKay--Piperno metadata and DOI were checked on official arXiv, the authors' nauty site, and the journal record exposed by DBLP; Markstr\"om metadata is reproduced in Garcia's primary reference list and agrees with the available article record.  `Zeng2026SSRN7380519` uses `metadata_basis=user_designated_workbook` from worksheet `\u6570\u5b66\u4e3b\u8868`, row 40.  Mandatory title/author/venue/DOI searches were attempted; direct DOI/Crossref refresh was unavailable in scope, so the workbook DOI and BibTeX remain authoritative as instructed. | Verified; user-record authority applied to Zeng |

No extracted claim was contradicted, numerically rounded away from its evidence,
or left unsupported.  The Zeng citation is relevant only to proof architecture;
it is not used for the graph theorem, finite boundary, software behavior, or
priority.  The inability to refresh its optional metadata endpoint therefore
does not create an unverified citation under the designated-authority rule.

## Bibliography and key integrity

The source contains the four keys `Garcia2026`, `Markstrom2004`,
`McKayPiperno2014`, and `Zeng2026SSRN7380519`.  All four occur in the final
`.aux`, all four have `\bibitem` entries in the final `.bbl`, and all four render
legibly on PDF page 4.  BibTeX reports four entries and zero `warning$` calls.
There are no undefined or unused manuscript citations and no unsupported
attribution or novelty claim requiring repair.

## Publication dependency scope

The sorted source list checked was:

1. `evidence/attachment_orbit_crosscheck.cpp`
2. `evidence/cycle_detector_crosscheck.cpp`
3. `evidence/geng_excess2_search.cpp`
4. `evidence/graph6_parser_dump.cpp`
5. `evidence/pass2_A_m0.log`
6. `evidence/pass2_A_m1.log`
7. `evidence/pass2_A_m2.log`
8. `literature/user_bibliography_check.md`
9. `manuscript/citation_notes.md`
10. `manuscript/main.tex`
11. `manuscript/references.bib`

This is exactly the sorted `publication.json` `source_files` array.  The TeX
recorder confirms that the only authored compilation inputs are `main.tex` and
`references.bib`; the remaining listed files are the cited computational
supplement, exact logs, and bibliography/citation provenance.  Generated TeX
auxiliaries and system packages are not authored dependencies.  Dependency
scope is complete.

## Sources consulted

- Daniel Garcia, official arXiv abstract and v1 HTML:
  `https://arxiv.org/abs/2609.04686` and
  `https://arxiv.org/html/2609.04686`.
- Brendan D. McKay and Adolfo Piperno, official arXiv record:
  `https://arxiv.org/abs/1301.1493`.
- Official nauty and Traces site and version 2.9.3 User's Guide:
  `https://users.cecs.anu.edu.au/~bdm/nauty/` and
  `https://users.cecs.anu.edu.au/~bdm/nauty/nug29.pdf`.
- The designated workbook extract in
  `literature/user_bibliography_check.md`, plus the bounded search attempts
  recorded above.

## Verdict

**Accept.**  Citation keys, metadata basis, claim scope, rendered references,
and complete publication dependencies pass.  The workbook authority rule was
applied exactly: `metadata_basis=user_designated_workbook`; external refresh
unavailable in scope; nearby prose independently remains supported by the
available workbook abstract.
