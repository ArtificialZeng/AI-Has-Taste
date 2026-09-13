# Checkpoint

- **Job:** `bigMac-00026-p04-research-f70a71689c5e` (research pass 1).
- **Frozen source:** `source.md` remains byte-for-byte unchanged with SHA-256
  `1efd3272605a0ddd96cd34a45bf78160b90be3800af825d2344e60f87737acb6`.
- **Status / candidate:** Affirmative resolution candidate.  The graph6 string
  ``LlthgsL`mEkLkL`` decodes to the 39-edge Paley graph \(P(13)\), and exact
  computation gives \(\beta(P(13))=4\).
- **Complete orbit evidence:** `evidence/lc13_search.cpp` performs labeled BFS
  from the candidate, applies all 13 local-complement moves at every state, and
  compares complete 78-bit adjacency keys.  The queue closes with 711,440
  states.  `evidence/paley13_lc_orbit.bin` stores every state in BFS order plus
  a parent and move; it is 10,671,616 bytes with SHA-256
  `6ee96dec3a2e4c2dcbd4424366e3499b611024c5911b8f20c7d54dca1eb73d02`.
- **Independent exact check:** Using the required research interpreter,
  `evidence/verify_paley13.py` independently decoded the graph6 input (also
  cross-checking NetworkX), verified all 711,439 reachability-tree edges, key
  uniqueness, and all 9,248,720 orbit-closure moves.  It then tested all 1,287
  five-subsets of every orbit state: all 915,623,280 exact mask checks contain
  an edge.  It also found an independent four-set at orbit record 834, so the
  result is exactly \(\beta=4\), not only an upper bound.  The machine-readable
  output is `evidence/paley13_verification.json`; the certificate explanation
  and reproduction commands are in `evidence/paley13_certificate.md`.
- **Literature / registry:** The local registry had no candidate.  On
  2026-09-09, arXiv:2604.13434 was still v1 and described whether
  \(R_{\rm vm}(5)=15\) as the next open problem; targeted primary-source and
  code/witness searches found no explicit 13-vertex witness.  Search scope and
  limitations are recorded in `evidence/literature_registry_check.md`; this is
  not proof of priority.
- **Obstacle encountered:** The first independent-verifier run rejected a
  malformed 7-character/8-byte magic constant.  The format was corrected to
  the unambiguous 8-byte `LC13ORB2`, the orbit was regenerated from scratch,
  and the independent verifier then passed.  No failed run is used as evidence.
- **Remaining gate:** This researcher result is not mathematical acceptance;
  the exact frozen scope, implementations, and artifacts require a fresh
  referee audit.
- **Next test:** In a fresh referee context, recompute the graph6 edge set,
  inspect the two independent LC/independence implementations, rerun
  `verify_paley13.py` on the SHA-256-bound orbit artifact, and try to falsify
  the claimed reachability, closure, or no-independent-five assertions before
  accepting `claim.json`.
