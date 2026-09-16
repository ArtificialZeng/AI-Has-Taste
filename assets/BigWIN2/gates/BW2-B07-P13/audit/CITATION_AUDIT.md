# Citation and novelty audit

Search cutoff: 2026-08-31 (Asia/Shanghai)  
Status: **pass with bounded novelty wording**

## Source checks

- TheoremDB P2484 was checked at its canonical statement page.  The snapshot
  dated July 24, 2026 states the same problem, reports the prefix through
  \(10^{11}\), and labels the full endpoint open.
- The incumbent certificate was checked at TheoremDB record R560/R563.  Its
  factorization, witnesses, gap, and integer-square-root claims were also
  independently replayed locally.
- Bennett and Ghadermarzi, “Mordell's equation: a classical approach,” was
  checked in the journal PDF, publisher page, DOI metadata, arXiv record
  1311.7077, author-hosted copy, and author data page.  The abstract and
  introduction state the complete \(0<|k|\le10^7\) scope; Proposition 2.1
  supplies the integral-point/Thue correspondence; Sections 3--4 address
  representative enumeration and exact Thue solving; Section 5 identifies
  the full output.
- DOI content negotiation confirmed: Michael A. Bennett and Amir
  Ghadermarzi, *LMS Journal of Computation and Mathematics* 18(1) (2015),
  633--646, DOI 10.1112/S1461157015000182.
- Pocklington's original bibliographic record was checked as H. C.
  Pocklington, *Proceedings of the Cambridge Philosophical Society* 18
  (1914--1916), 29--30.

Exact-title and DOI searches located no correction, retraction, or source
contradicting the claimed Bennett--Ghadermarzi range.

## Novelty boundary

The frozen pre-result and post-result queries are recorded verbatim in
`literature/search_log.md`.  They recovered the source problem, its prefix
sweep, all four integer-square candidates, and the Mordell tables.  They did
not locate a source explicitly deducing the full trillion-range prime result
from those tables.  The paper therefore uses only the dated wording “no
source spelling out this theorem was located”; it does not claim unqualified
priority or that the underlying integral-point computation is new.

## Bibliography checks

- [x] Every citation exists and supports its nearby statement.
- [x] Primary/publisher records were used for the decisive theorem.
- [x] `audit_latex.py` result: `cited=4 bib=4 missing=0 unused=0`.
- [x] No bibliography entry is unused.
- [x] The source problem and the strongest decisive adjacent result are both
      cited.
