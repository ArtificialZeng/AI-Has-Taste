# Citation and bibliography audit

## Method and result

Search verification was performed in two non-interleaved recorded stages. Pass 1 is the fixed claim/citation ledger in `audit/citation-claim-ledger.json`; pass 2 is `audit/citation-verification.json`, with exact passages indexed in `audit/source-locations.json`. Agent delegation was not used because this bounded job explicitly prohibited agents and other Codex processes.

All eleven extracted claims passed. All three citation keys were found in their primary records, their title/author/year/venue or repository metadata match the bibliography, and each source supports the exact nearby claim. There are no citation-not-found, misquotation, misleading-context, numerical-error, hallucination, or unverified findings.

## Claim-to-source conclusions

- `Paffenholz2015Faces`: the Electronic Journal of Combinatorics publisher record verifies Andreas Paffenholz, the title, 2015 date, volume 22 issue 1, article P1.67, and DOI 10.37236/4499. Its abstract directly supports the restrained statement that faces of Birkhoff polytopes are an established study area and also states the permutation-matrix convex-hull definition.
- `PenaWirth2026`: the official arXiv record and the frozen arXiv v1 PDF verify the title, authors, year, identifier, definition, and exact bound. Definition 2.1 on p.2 gives the complement-hull formulation; Example 6.4 on pp.10--11 gives only `Phi(B_n) >= 1/sqrt(n^2-1)`, hence `1/sqrt(8)` at `n=3`, with no exact `B_3` computation.
- `ZengEtAl2026FiniteCertificates`: the official Preprints.org v1 record verifies the title, four authors, date, DOI, and preprint status. Its abstract and Section 6 directly document exact symmetry-reduced finite enumeration and deterministic exact verification. The manuscript limits the comparison to architecture and makes no result-transfer or priority claim.

## Coverage and mechanical consistency

The three-reference bibliography is small but complete for the paper's actual external dependencies: problem definition/nearest facial-distance bound, Birkhoff-face context, and the narrowly invoked finite-certificate comparison. The proof of the new finite result and its rational KKT checks are self-contained and bound to accepted exact evidence, so adding unrelated user-library or generic optimization references would be padding. Active user-library row 9 is bound to citation attempt 1 and launch `e6ddf61a-1c58-409f-9242-e813f2278d3e` in `audit/user-bibliography-selection.json`, and appears through the ordinary body-flow direct citation `\cite{ZengEtAl2026FiniteCertificates}`.

The BibTeX audit found three cited keys, three bibliography entries, no missing or unused entries, no key changes, and no entries requiring replacement. Final build/log checks are recorded separately in `audit/build.md` and `audit/build.json`.
