# Fresh citation and bibliography audit

## Result

Accepted.  The required two stages were kept separate: `audit/citation-claim-ledger.json`
freezes 20 claims before verification, and `audit/citation-verification.json` records the
verification-only pass.  Four distinct citation keys (six body occurrences) were checked
serially because this job expressly prohibited agents.  No BibTeX entry or citation key
required replacement.  Exact source locators are in `audit/source-locations.json`.

| Key | Primary record and passage | Nearby support | Action |
|---|---|---|---|
| `Erickson2010` | Open Problem Garden, problem page, author/date and problem statement | Erickson posed the stated grid achievement game. | Retained; metadata and wording verified. |
| `Randjelovic2025` | arXiv:2401.16768v2, abstract and Theorem 1 | The first player wins for every `n >= 4`. | Retained; author/title/version/DOI and theorem verified. |
| `Guan2026` | arXiv:2608.13501v1, Theorem A, Sections 5--7, Table 2 and Conjecture 14 | The `2n+3` upper bound; fixed-strategy checks at `n=4,5,6`; optimality conjecture and faster-strategy caveat. | Retained; all nearby claims and metadata verified. |
| `ZengEtAl2026` | Official Preprints.org v1, Sections 3 and 6 | Exact finite certificate checking reconstructs the finite objects, constraints and symmetry action before accepting stored certificates. | Retained; active-library row 9 and DOI verified. |

The bibliography has normal claim-driven coverage rather than an Excel-only list:
Erickson is the primary problem origin, Randjelovic is the first-player-win result, Guan is
the closest prior length result and direct source of the upper bound, and the selected
library item supplies the narrow methodological comparison.  All 49 active first-sheet
records were screened; row 9 was the closest genuine methodological match.  A second
library item would be decorative, so none was added.  Every retained source supports its
nearby body claim, and every selected library item has an ordinary direct `\cite{FinalKey}`.

The arXiv and Preprints records were found under all applicable author/title/venue/DOI or
arXiv-id search forms.  The local Guan PDF agreed with the live v1 record.  No project
`literature/bibliography-revision-*.md` or `literature/crossref-*` capture existed to inspect.
The novelty comparison remains deliberately bounded to these sources and does not claim
absolute priority.

Mechanical checks found four cited keys, four bibliography entries, no missing or unused
entries, and identical source/aux key sets.  The converged log and `.blg` contain no
undefined citation/reference, missing database entry, repeated entry, BibTeX warning or
LaTeX error.  The release-hook selection validator accepted the exact issued citation
attempt and launch binding.

