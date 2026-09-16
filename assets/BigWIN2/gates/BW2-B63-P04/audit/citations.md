# Citation and claim verification report

Mode: search verification with local primary-PDF checking. Search date: 2026-09-07. Pass 1 was frozen first in `audit/citation-claim-ledger.json`; this report is the separate verification pass. Subagents were not used because the job expressly prohibited agents.

## Result

All eight cited works exist, their retained metadata is consistent with the authoritative, publisher, repository, or library-scan records inspected, and each is needed for a nearby historical, methodological, criterion, count, or comparison claim. No citation is decorative. The bibliography is not user-library-only: it includes the original graph-polynomial paper, the closest stability paper and current spider result, the primary free-tree generator, both original sources underlying the Routh--Hurwitz criterion, and the independent census table. The single selected user-library work is narrowly identified as methodological context and is not used for its mathematical conclusion.

| Key | Manuscript claim | Exact source location inspected | Status |
|---|---|---|---|
| `GutmanHarary1983` | first definition in this form | Combinatorial Press, *Utilitas Mathematica* vol. 24 contents, pp. 97--106; Brown--Cameron PDF p. 2 states that Gutman--Harary first defined it in 1983 | verified (historical attribution corroborated) |
| `BrownCameron2018` | closed-LHP terminology; alpha at most 3; far-right tree roots; computation through 20 | EJC publisher PDF, p. 2 lines 38--52; Proposition 2.1, pp. 3--4; p. 7 lines 353--355; Proposition 4.1, pp. 15--16 | verified, exact/paraphrase |
| `ZhangTu2026` | all spiders have roots in the open LHP | frozen arXiv v1 PDF `evidence/external/2609.04694.pdf`, Theorem 4, p. 3 and proof pp. 6--7 | verified, paraphrase |
| `WrightRichmondOdlyzkoMcKay1986` | once-per-class free-tree generation | SIAM publisher abstract for DOI 10.1137/0215039: all nonisomorphic fixed-size trees, without repetition; vol. 15(2), 540--548 | verified, paraphrase |
| `OEISA000055` | order-21 total is 2,144,505 | OEIS A000055 list, row n=21 | verified, exact |
| `Routh1877` | recursive stability test and sign-variation method | Routh, *A Treatise on the Stability of a Given State of Motion*, Chapters I--III; public-domain Macmillan scan and Library of Congress/Open Library record | verified, primary source |
| `Hurwitz1895` | determinant criterion for roots with negative real parts | Göttingen digitization and Springer DOI 10.1007/BF01446812, *Math. Ann.* 46 (1895), 273--284 | verified, primary source; paired with Routh for the manuscript's tabular formulation |
| `Zeng2026Whiskered` | 6,021 classes, exact integer witnesses, reconstructing verifier | SSRN authoritative abstract for 10.2139/ssrn.7385138, posted 3 Sep 2026 | verified, exact/paraphrase |

## Fixed-claim decisions

Claims C01--C05, C07--C08, C12, and C15 are supported by the cited passages above. Claims C06, C09--C11, C13--C14, and C16 are manuscript/evidence claims rather than literature claims; they trace to the accepted exact audit and frozen computational artifacts. All exact numerical values agree: 20, 21, 2,144,505, 43, 430, 6,021, 7, and 12. No rounding or unit mismatch occurs.

The comparison is appropriately bounded: the manuscript says Brown--Cameron *reported* a computation through order 20 and expressly disclaims an absolute priority claim. No unsupported strengthening of the accepted order-21 theorem was found.

## Sources inspected

- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p46/pdf/
- https://www.combinatorics.org/ojs/index.php/eljc/article/view/v25i1p46
- https://combinatorialpress.com/um/vol24/
- https://arxiv.org/abs/2609.04694 and the frozen v1 PDF
- https://epubs.siam.org/doi/abs/10.1137/0215039
- https://oeis.org/A000055/list
- https://archive.org/details/atreatiseonstab02routgoog
- https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0046/LOG_0026.pdf
- https://doi.org/10.1007/BF01446812
- https://papers.ssrn.com/sol3/Delivery.cfm/7385138.pdf?abstractid=7385138

Bibliographic key consistency was checked with `check_bib_keys.py`: 8 cited keys, 8 BibTeX keys, no missing or unused keys, and final AUX agreement. Primary-source verification was performed serially because the job expressly prohibited subagents.
