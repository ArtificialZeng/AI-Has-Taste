# Claim ledger

Frozen for Gate 1 on 2026-08-30 (Asia/Shanghai).  “Not located” is bounded
by the sources and queries in `search_log.md`; it is not a universal
nonexistence claim.

| ID | Claim | Type | Status | Primary evidence and locator | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C01 | There are exactly 80 isomorphism classes of STS(15). | exact | verified | Cole–Cummings–White, PNAS 3 (1917), 197–199, DOI 10.1073/pnas.3.3.197; Mathon–Phelps–Rosa (1983), catalogue; DesignTheory.org complete file declares `no_designs="80"`, `pairwise_nonisomorphic="true"`. | 99% | The quotient graph has 80 vertices. |
| C02 | A Pasch switch is the 4-cycle switch displayed in the problem. | exact definition | verified | Grannell–Griggs–Murphy, *Utilitas Math.* 56 (1999), pp. 3–21, definition and Appendix; Kaski–Mäkinen–Östergård, *Graphs Combin.* 27 (2011), pp. 539–546, §3. | 99% | Fixes the adjacency operation. |
| C03 | Exactly one STS(15) class is anti-Pasch. | exact | verified | Grannell–Griggs–Murphy (1999), §3: system #80 is the only 4-cycle-free class; their Appendix row #80 has count 0. | 99% | Exactly one vertex has no switch occurrence. |
| C04 | The other 79 classes form one Pasch-switch component. | exact | verified published baseline | Gibbons thesis (1976), reported and independently recomputed by Grannell–Griggs–Murphy (1999), §3 and complete 4-cycle Appendix; also Kaski–Mäkinen–Östergård (2011), pp. 540–541. | 99% | Known component sizes are 79 and 1. |
| C05 | The 79-component diameter has not previously been published. | bounded novelty report | exact value not located after two passes | Exact-term/full-text searches of Gibbons (metadata), Grannell–Griggs–Murphy (complete PDF), Kaski–Mäkinen–Östergård, Erskine–Griggs 2025/arXiv:2405.07750, TheoremDB snapshot, DesignTheory.org, public-code searches, and second-pass queries for diameter 11, 258 edges, radius 6, and \(M(15,4)\); see `search_log.md`. | 90% | Supports only the bounded wording “not located in the recorded searches.” |
| C10 | The simple quotient has 258 edges, component sizes 79 and 1, and nontrivial-component diameter 11. | certified finite result | independently verified | `certificate/result.json`; no-nauty replay in `code/independent_verifier.py`; standalone `code/verify_bfs.py`. | 99% | Resolves the finite endpoint, conditional only on the classical 80-class completeness theorem. |
| C11 | There are exactly two unordered diameter pairs in the released canonical numbering: V000–V006 and V000–V028. | certified finite result | independently verified | all-pairs BFS rows reconstructed from `certificate/quotient_edges.json`. | 99% | Supplies lower-bound witnesses and a complete extremal classification for this numbering. |
| C06 | TheoremDB’s dated frontier says the sole remainder is the diameter. | author/report status | verified as a dated secondary record, not a proof | TheoremDB P2788/R1156, reviewed 2026-07-31. | 95% | Motivates but does not certify the result. |
| C07 | The DesignTheory.org STS(15) file is a complete exact external catalogue. | exact database assertion | verified | `t2-v15-b35-r7-k3-L1.icgsa.txt.bz2`; page row says content type `a`, 80 designs; XML root asserts 80 and pairwise nonisomorphic; downloaded-stream SHA-256 `11310c7e35330e842938dbcc4bb6e59144bf40576323f22499a809364d50f2c9`. | 99% | Supplies an independent classification cross-check, not trusted graph edges. |
| C08 | The 1999 Appendix contains the full result of every 4-cycle switch in standard class numbering, but gives no diameter. | exact source description | verified by full PDF inspection | Grannell–Griggs–Murphy (1999), pp. 14–15 of article/PDF pages 14–15; source PDF SHA-256 `83a59a7879b1d19a79ca86cb1a50e7a907f8ad7e24f8dd0ce4c86e35c80f0a37`. | 99% | Defines the last published baseline and an independent edge audit. |
| C09 | The 2025 v=19 paper does not settle the STS(15) Pasch diameter. | exact scope | verified | Erskine–Griggs, *J. Combin. Des.* 33 (2025), 195–204, DOI 10.1002/jcd.21975; arXiv:2405.07750. | 98% | Latest directly related paper does not close this endpoint. |

## Frontier after Gate 1

The user’s mathematical boundary is correct: the class count and 79+1
component structure are established prior work.  The strengthened correction
is that a complete per-configuration switch table was already published in
1999; only its graph diameter was not stated or located.  This project must
therefore compute the diameter from two genuinely different inputs: first the
published baseline/table or standard catalogue, then a direct reconstruction
from canonical representatives, with an independent no-nauty verifier.
