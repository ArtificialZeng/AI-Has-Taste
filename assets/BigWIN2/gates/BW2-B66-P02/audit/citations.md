# Citation and bibliography audit

Verdict: **accept**. This was a non-interactive two-stage search-mode audit.
It is bound to release job `win-00066-p02-release-7cbcf9ae4463`, citation
attempt 4, and launch `5e4ead91-a246-4c94-8cdb-59a0cc51b30f`.
Stage 1 read the complete manuscript and froze the four claim/citation pairs in
`audit/citation-claim-ledger.json` before any verification. Stage 2 checked only
that frozen set, sequentially, against primary records and exact passages. No
agents were used because the release job explicitly prohibited agents and other
Codex processes.

## Claim-level verification

| ID | Key | Nearby claim | Primary location | Status |
|---|---|---|---|---|
| CIT-001 | `Stamoulis2026` | exponent-at-most-four exactness; the ten-vertex seed has SDP value `3/4` and cut value `4/5` | arXiv:2609.05368v1, Corollary 4.7, pp. 11--12, and Section 6.4, pp. 18--19 | Verified, exact |
| CIT-002 | `DorsiEtAl2025` | low-degree Abelian Cayley work gives a `(1+epsilon)` sparsest-cut approximation and spectral structure, not this finite classification | official DROPS abstract and Section 1.1.3/Theorem 9, pp. 16:6--16:7 | Verified, paraphrase |
| CIT-003 | `Schoenberg1938` | a squared Euclidean semimetric is of negative type, after which the manuscript performs the finite cyclic Fourier diagonalization | *Transactions AMS* 44 (1938), Section 3, pp. 525--526 | Verified, paraphrase |
| CIT-004 | `Zeng2026Multiplicity` | a canonical exact cut-partition computation occurs in a different graph-reconstruction setting | arXiv:2608.18179v1 abstract, final sentence | Verified, paraphrase |

The detailed decisions and source locators are in
`audit/citation-source-verification.json` and `audit/source-locations.json`.
There are no Numerical Error, Hallucination, Misleading, Citation Not Found, or
Unverified outcomes.

## Bibliographic records and coverage

All four records exist and their final BibTeX author, title, year/version,
venue, pages, and DOI or arXiv identifier agree with the primary records. The
official DROPS BibTeX was used to compare the full d'Orsi--Jones--Ruotolo--Vadhan--
Zhang metadata. The frozen Stamoulis PDF supplies the cited version-1 record and
exact passages; the primary Schoenberg PDF/AMS record and the official arXiv
record for Zeng agree with the retained entries. No key or BibTeX field required
repair.

Coverage is not library-only. Stamoulis is the problem-origin and closest exact
source, d'Orsi et al. is the closest prior Abelian-Cayley algorithmic work, and
Schoenberg is the non-library primary method source for the negative-type step.
The single active-library paper, registry row 17, has an ordinary body-flow
direct `\cite{Zeng2026Multiplicity}` and supports only its narrow nearby method
comparison. A second library record would be padding; none of the other 48
entries is as close to the Cayley-cut problem or that specific verification
claim. The manuscript makes only a bounded literature comparison and explicitly
disclaims a broader priority assertion.

The canonical TeX has exactly four ordinary body-flow citation keys, the
canonical BibTeX has the same four entries, and the final AUX has exactly those
four keys. `check_bib_keys.py` reports zero missing bibliography files, missing
keys, unused entries, or AUX discrepancies. The final log scan reports no
undefined citation/reference, missing database entry, repeated entry, BibTeX
warning, or LaTeX fatal diagnostic.

No `literature/bibliography-revision-*.md`, `literature/crossref-*.json`, or
`literature/crossref-*.md` file exists in this project. The failed live WSL
`curl` attempt was not treated as source unavailability: primary material was
inspected through the web verifier and the preserved authoritative PDF.
Search date: 2026-09-07.
