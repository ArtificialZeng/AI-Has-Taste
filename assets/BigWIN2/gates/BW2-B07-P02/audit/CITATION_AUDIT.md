# Citation audit

Status: PASS (searches and metadata checks completed 2026-08-30 UTC).

## Claim-to-source checks

- The cycle-index product and the complete root-of-unity expansion are
  supported by Flajolet--Fusy--Gourdon--Panario--Pouyanne, Section 3 and
  Proposition 1.  The manuscript does not promote that paper's finite
  experiment \(|R_n|\le22\) to a global theorem.
- The leading asymptotic attributed to Greene and Knuth is the asymptotic
  quoted and sharpened in the inspected full text of Flajolet et al.; the
  cited book is the original source identified there.
- Lehmer's reciprocally weighted partitions paper exists with DOI
  `10.4064/aa-21-1-379-388` and supports the historical weighted-partition
  context, not the new monotonicity theorem.
- OEIS A007838 supports the sequence identification and bibliography only;
  no theorem-level dependency is assigned to the database entry.
- TheoremDB P2540 is the literal problem source.  Its page and inline R197
  artifact support only the reported exact prefix through 5000 and its
  public open status at the inspected snapshot.

## Metadata and novelty boundary

- EJC metadata for Flajolet et al. was checked at the journal endpoint and
  DOI `10.37236/1129`.
- Greene--Knuth metadata was checked against the Springer record and the
  bibliography of Flajolet et al.; the manuscript cites the 1981 edition
  actually named by that paper rather than silently replacing it by a later
  edition.
- Lehmer metadata was checked against the IMPAN/DOI record.
- Pre-result and post-result exact-title, exact-formula, sequence-ID, and
  factorization-fingerprint searches are recorded in
  `literature/search_log.md`.  No prior proof, counterexample, correction, or
  stronger monotonicity theorem was found within that dated search boundary.
  The manuscript consequently makes no unbounded claim of priority.

## Bibliography integrity

`audit_latex.py` reports `cited=5 bib=5 missing=0 unused=0`.  Every reference
is cited at the claim it supports.  URLs and DOI fields point to the inspected
records, and there are no undefined or unused bibliography keys.
