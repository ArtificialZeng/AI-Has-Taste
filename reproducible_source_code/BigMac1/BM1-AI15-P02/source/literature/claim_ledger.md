# Claim ledger — NOVELTY_LOCK pass 1

Search cutoff: 2026-08-29 (Asia/Shanghai). “Not found” below is bounded by
the databases and exact queries recorded in `search_log.md`.

| ID | Frozen claim | Type | Status | Primary evidence and location | Confidence | Consequence |
|---|---|---|---|---|---:|---|
| C01 | A321614 counts order-four rectangle-symmetry orbits of maximum \(2n\)-king placements on \(4\times2n\). | exact/source | verified, with convention repair | OEIS A321614, definition, offset and comments; the values \(a(1)=4,a(2)=23\) distinguish the Klein-four convention from the full square group | 0.99 | Fixes the mathematical object and the \(n=2\) exception. |
| C02 | The maximum number of nonattacking kings on a \(4\times2n\) board is \(2n\). | exact | verified | Wilf, *The Problem of the Kings*, DOI 10.37236/1197, abstract and first reduction; also OEIS A321614 comment | 0.99 | Equality forces one king in every cell of a fixed \(2\times2\) partition. |
| C03 | Colin Barker posted the displayed generating function and order-ten recurrence in 2018 as conjectures. | exact/source | verified | OEIS A321614, FORMULA section, “Conjectures from Colin Barker, Dec 22 2018” | 0.99 | Exact target and attribution fixed. |
| C04 | The OEIS b-file has values \(n=0,\ldots,21\), ending at 665017743665. | exact/data | verified | OEIS `b321614.txt`, lines 1–22 | 0.99 | Regression target only, not a theorem. |
| C05 | A 2026 SciNet artifact verifies the recurrence and computed minimality through \(n=5000\), but explicitly does not prove all \(n\). | author report/data | verified as report, not independently adopted | SciNet finding 4d13cbaa, summary/claims/method, especially the explicit limitation | 0.98 | Establishes prior computational frontier and its limitation. |
| C06 | Wilf’s 1995 paper treats labeled maximum king placements on fixed even-width boards and proves a general asymptotic theorem. | exact/adjacent theorem | verified | Electronic Journal of Combinatorics 2 (1995), R3; DOI 10.37236/1197 | 0.99 | Prior transfer-state foundation; it does not state this free-count recurrence. |
| C07 | A321614 equals the diagonal entry \(A231145(2n+1,2n)\) in the free 2-by-2 tile table. | exact/cross-reference | verified as database identity | OEIS A321614 FORMULA and A231145 definition/table | 0.98 | Independent combinatorial cross-check, not needed for the proof. |
| C08 | An all-\(n\) proof of Barker’s exact order-ten recurrence was already publicly available by the cutoff. | novelty | not found in two recorded search passes | OEIS still labels both formulas conjectures; SciNet explicitly leaves proof open; two arXiv/DOI/exact-formula passes in `search_log.md` returned no such proof | 0.94 | The exact proof is new relative to the bounded recorded search frontier; no absolute priority claim is made. |

## Theorem frontier frozen before proof search

- Exact known source data: \(a(0),\ldots,a(21)\) and Barker’s conjectured
  rational generating function.
- Strong prior adjacent result: Wilf’s fixed-width transfer formulation and
  asymptotic theorem for labeled maximum placements.
- Strong computational result: exact agreement and Berlekamp–Massey
  minimality through \(n=5000\), explicitly finite.
- Target not found: a finite exact matrix certificate proving the free-count
  rational generating function for every \(n\).
