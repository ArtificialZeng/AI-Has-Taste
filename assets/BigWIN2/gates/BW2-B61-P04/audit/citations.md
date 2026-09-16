# Citation and bibliography release audit

## Summary

Search-mode verification was performed in two non-interactive stages.  Stage 1
froze 20 manuscript claims and seven claim/citation pairs in
`audit/claim-ledger.json`, bound to current manuscript SHA-256
`5f7a948a1665214a5f6b501410e14ee6448c6b3dda6b094b09405a1d8ee79fad`.
Stage 2 independently checked only those fixed pairs and is recorded in
`audit/citation-verification.json`.

All 20 claims and all seven citation pairs are supported.  There are no
numerical errors, hallucinations, misleading attributions, unverified claims,
undefined citation keys, or blocked bibliography records.  The bibliography
checker found five cited keys, five canonical BibTeX entries, and identical
source/AUX key sets.  No BibTeX entry or citation key required replacement.

The bibliography audit was performed by the primary worker because the user
expressly prohibited agents, other Codex processes, and background workers.

## Claim-to-source verification

| Key | Nearby claim | Primary source and exact location | Result |
|---|---|---|---|
| `Hwang2026` | Definition, quandle-isomorphism/Frobenius-similarity equivalence, sufficient coefficient bound, and the ell=3 example. | arXiv `2609.02278v1`; local primary PDF: Definition 2.4 p.3, Theorem 4.2 and Proposition 4.1 p.12, Corollaries 4.3 and 4.5 pp.13-14, Example 4.9 p.15. | Verified, exact. |
| `Nelson2003` | Hwang's rigidity proof builds on the finite Alexander-quandle classification. | Official Topology Proceedings reprint, Theorem 2.1, printed p.247 (web-extracted PDF lines 83-89); Hwang explicitly recalls it as Proposition 4.1 and writes that it yields Theorem 4.2. | Verified, exact. |
| `Hasse1936` | The elliptic trace satisfies `|a_E| <= 2 sqrt(5)`. | Official De Gruyter record, DOI `10.1515/crll.1936.175.193`, pp.193-208; Hwang's Theorem 4.4 proof states the Hasse-Weil coefficient bound whose `g=1,q=5` specialization is the displayed inequality. | Verified, paraphrase. |
| `Tate1966` | Equality of Frobenius characteristic polynomials is equivalent to finite-field isogeny. | Original article, Theorem 1(c1)-(c2), printed p.139 (PDF p.6), web-extracted lines 186-213; DOI `10.1007/BF01404549`. | Verified, exact. |
| `ZengEtAl2026Certificates` | A human-readable proof separated from an exact executable verifier parallels a certificate architecture. | Official Preprints.org version-1 full text, Section 6, web-extracted HTML lines 207-218; DOI `10.20944/preprints202608.1658.v1`. | Verified, paraphrase; methodological only. |

The manuscript's new ell=2 and ell=7 counterexamples are supported by its
self-contained calculations, the accepted mathematical audit, and the two
exact verification programs, not by outside citations.  Both programs were
rerun successfully during release.

## Coverage and relevance

The bibliography is scholarly rather than library-only.  It includes the
direct problem source and closest prior result, the finite Alexander-quandle
classification on which rigidity depends, the trace-bound origin, Tate's
finite-field isogeny theorem, and one genuinely relevant active-library item
for a narrowly worded methodological comparison.  Each retained source has an
ordinary body-flow citation and supports its adjacent claim.

Only active-library row 9 was selected.  No second one of the remaining 48
records supports this paper's Frobenius-quandle, isogeny, or rational-canonical-
form claims, and adding a merely generic finite-field or exact-computation item
would be decorative padding.  The exact active-registry binding and runner-issued
citation attempt 2 / launch ID `2cac7964-8892-47dd-a23d-83cd624c1155` are
recorded in `audit/user-bibliography-selection.json`.

A bounded search for the exact ell=2 and ell=7 delta located no separate
treatment.  The manuscript correctly limits this to a search report and makes
no absolute priority claim.
