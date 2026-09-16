# Citation audit

The two-pass claim ledger and verification results are recorded in
`audit/claim-citation-ledger.json` and `audit/citation-verification.json`.
All five extracted claim/citation pairs were verified against primary or
publisher sources on 2026-09-07:

- C01, C02, C04: Lewis--Won arXiv:2609.03081v1, PDF Sections 2 and
  Question 2.2 (pp. 3 and 5).
- C03: Cambridge University Press book record and contents, Chapter 7.
- C05: Zeng et al. version-1 publisher text, Sections 3, 4, and 6.

Metadata, source locations, and claim-level support appear under
`audit/sources/`. The active-library item is row 9, cited directly as
`202608.1658` and bound to attempt 1 / launch
`25b124ba-0f73-4854-9e6a-995a8312cf53` in
`audit/user-bibliography-selection.json`. The previous unrelated
correlation-matrix reference was removed. The three retained references cover
the primary problem source, permanent background, and the specifically cited
finite-verification comparison without decorative padding.

BibTeX key and final AUX checks pass for all three keys. Verdict: accept.
