# Citation audit — pass 2

Audit date: 2026-08-29.  Frozen input: the twelve claims CC01--CC12 in
`audit/CITATION_CLAIMS.md`.  No claim was added during verification.

## Result

All twelve claims are supported.  All three cited BibTeX records resolve to
the stated official DOI metadata, every cited key occurs in both the
bibliography and the final AUX file, and no bibliography key is unused.

| ID | Verification evidence | Verdict |
|---|---|---|
| CC01 | Quispel--Tapley--McLaren--van der Kamp (2023), DOI `10.1088/1751-8121/ace0e9`, and van der Kamp--Quispel--McLaren (2024), DOI `10.1007/s11040-024-09496-7`; the 2025 source introduction independently states the \(3n-2\) and \(n-1\) counts. | verified |
| CC02 | Van der Kamp (2025), DOI `10.1007/s10884-025-10446-2`, Introduction and Sections 3--4, explicitly describes linear changes using independent Darboux polynomials and the induced LV-equivalence. | verified |
| CC03 | Van der Kamp (2025), abstract, Introduction, and Conjecture 12: the conjecture is exactly the nonisomorphic-tree implication and the reported checked range is \(n<9\). | verified |
| CC04 | Van der Kamp (2025), latest arXiv source `2411.18264v4`, Introduction and Section 2: statements concern general/generic classes and special subclasses are excluded. | verified |
| CC05 | Van der Kamp--Quispel--McLaren (2024), DOI `10.1007/s11040-024-09496-7`, gives the tree parametrization and row-equality constraints. | verified |
| CC06 | Van der Kamp (2025), Lemma 2, gives C1--C3 as necessary and sufficient.  In the homogeneous case C1 is automatic, leaving precisely the displayed C2 and C3 conditions. | verified |
| CC07 | Independent standard-library verifier exhaustively enumerated Prüfer words and returned counts `1,1,2,3,6,11,23,47`. | verified |
| CC08 | The same verifier recomputed the circuit-incidence signature from every serialized edge list and found exactly the same number of distinct signatures at every order. | verified |
| CC09 | `tests/test_verifier_rejects.py` completed with `6 fail-closed mutations rejected`: omission, duplication, loop, forged reconstruction, forged circuit signature, and an unexpected field. | verified |
| CC10 | Fresh SHA-256 computation and verifier output both returned `5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6`. | verified |
| CC11 | Exact SymPy computation returned `-(a_p - d_qp)*(a_r - d_qr)*(2*a_q - d_pq - d_rq)`; script SHA-256 is `d25b188589fd01835782e346a9606f958f42782c92826a015ab5b955d5c1cb0c`. | verified |
| CC12 | Code inspection found no floating-point operation; the verifier uses only integer graph data, strings, tuples, sets, counters, and exact comparisons. | verified |

## Bibliography integrity

The three entries were taken from official DOI BibTeX exports preserved under
`literature/sources/doi_*.bib`.  The local database has three cited keys and
no extras.  The final checks returned:

```text
cited_keys: 3
bib_keys: 3
cited_keys_missing_from_bib: 0
bib_keys_not_cited: 0
cited_keys_missing_from_aux: 0
aux_keys_not_cited: 0
```

The clean BibTeX run emitted no warning.  The audit deliberately distinguishes
source-attributed claims (CC01--CC06) from new locally certified claims
(CC07--CC12).
