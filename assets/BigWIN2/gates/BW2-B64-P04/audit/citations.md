# Fresh citation and claim verification report

Mode: search verification with frozen local primary evidence

Document: `manuscript/main.tex` and `manuscript/references.bib`

Generated: 2026-09-07

## Summary

| Metric | Count |
|---|---:|
| Claims frozen in pass 1 | 14 |
| Verified | 14 |
| Numerical error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Citation not found | 0 |

Overall status: **PASS**.  All cited works exist, all retained citations
support their nearby claims, bibliography coverage is adequate and not padded,
and the manuscript does not strengthen the accepted mathematical scope.

## Claim-by-claim verification

| ID | Status | Confidence | Verification |
|---|---|---|---|
| C01 | Verified | exact | Carlet, Chapter 2, Section 2.2.1, printed pp. 48--52 gives the multilinear ANF, existence/uniqueness, and the maximum-support definition of algebraic degree; printed p. 57 treats vectorial functions coordinatewise. |
| C02 | Verified | exact | Lidl--Niederreiter, Chapter 2, Section 3 is expressly devoted to traces, norms, and bases over finite-field extensions. |
| C03 | Verified | exact | Zhang--Zhang v1, p. 11, Definition 11 defines the complete raw polynomial map on all matrix inputs; it is not restricted to invertible basis matrices. |
| C04 | Verified | exact | Zhang--Zhang v1, p. 11 Proposition 12 and p. 14 Theorem 17 prove the two displayed bounds; Section 4.2, pp. 17--18, reports the exact `n=3,4` values. |
| C05 | Verified | exact | The manuscript explicitly limits its comparison to Zhang--Zhang and expressly disclaims a global-priority claim; the source is dated 4 September 2026. |
| C06 | Verified | paraphrase | Zeng--Liu--Ratnavelu v1, Section 3, Lemma 3.1 extracts a coefficient from a permanent and then applies the Combinatorial Nullstellensatz. |
| C07 | Verified | exact | Identical in scope to frozen `claim.json`; the complete proof was accepted in `audit/math.md`. |
| C08 | Verified | exact | Internal Lemma 2 reproduces the accepted trace-hyperplane coefficient proof in `audit/math.md` and the frozen certificate. |
| C09 | Verified | exact | Internal Lemma 3 reproduces the accepted multiplication-matrix contradiction. |
| C10 | Verified | exact | The alternating-path uniqueness and degree argument match the accepted referee reconstruction without stronger hypotheses or conclusions. |
| C11 | Verified | exact | The manuscript states only that its coefficient family proves no leap upper bound; this agrees with `claim.json`, `audit/math.md`, and Zhang--Zhang pp. 17--18. |
| C12 | Verified | exact | A fresh run of `python3 evidence/verify_degree_certificate.py` returned counts 2, 3, 6 and eleven coefficients equal to 1, matching the substantive body of frozen `evidence/verification.txt`. |
| C13 | Verified | exact | The Zeng--Liu--Ratnavelu Data Availability Statement says no computation is used in the proof and separately identifies a companion verifier. |
| C14 | Verified | exact | The assistance paragraph is a process disclosure, and its proof-versus-computation limitation is consistent with the frozen artifacts and accepted audit. |

Detailed primary URLs, source passages, version information, and the
bibliography-coverage rationale are recorded in
`audit/citation-source-verification.md`.

## Bibliography audit

| Final key | Current title | Primary record result | Action | Uncertainty |
|---|---|---|---|---|
| `Carlet2021` | *Boolean Functions for Cryptography and Coding Theory* | Author/title/year/publisher/DOI confirmed; exact Chapter 2 support inspected. | Retained; nearby locator tightened. | None material. |
| `LidlNiederreiter1997` | *Finite Fields* | Authors/title/edition/series/publisher/DOI confirmed; Chapter 2 Section 3 support inspected. | Retained; nearby locator tightened. | Cambridge electronic label is 1996; cited second-edition print issue is 1997. |
| `ZhangZhang2026` | *Representation Redundancy and Structural Complexity in Finite-Field Inversion* | arXiv title/authors/v1/date and exact PDF claims confirmed. | Retained; nearby theorem/page locators tightened. | arXiv DOI is identified by arXiv as pending registration; arXiv identifier and frozen PDF are authoritative. |
| `202608.1194` | *Closing the Permanent-Rank Boundary for the Alon--Jaeger--Tarsi Conjecture* | Publisher title/authors/version/date/DOI and Sections 3/Data Availability support confirmed. | Replaced normalized local entry and old key `ZengLiuRatnavelu2026` with active registry raw BibTeX/key `202608.1194`. | None. |

The per-reference audit was serial because the job expressly prohibited
subagents.  Mechanical checks report four cited keys, four BibTeX entries, no
missing or unused entries, and no AUX mismatch.  The converged `.log` and
`.blg` contain no undefined citation, missing database entry, repeated entry,
LaTeX error, overfull box, or underfull box diagnostic.

