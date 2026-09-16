# Citation and bibliography audit

Verdict: **accept**.  Eight frozen claim/citation pairs using four bibliography
keys were verified against primary records and exact passages.  The source
locations and individual decisions are recorded in `source-locations.json` and
`citation-verification.json`.  The source `.tex` contains exactly four cited
keys; the canonical `.bib` contains the same four entries, with no missing or
unused entry.  The final AUX file contains all four keys.

Bibliographic metadata agree for author, title, year/version, venue, pages, and
identifier.  A single repair added Elsevier DOI
`10.1016/S0167-5060(08)70743-X` to the 1977 entry.  No citation key changed.
The active-library row 9 paper is cited directly as
`\cite{ZengEtAl2026Certificates}` in ordinary body flow and supports the nearby
methodological claim.  Only one library item is retained because the other 48
active records do not concern scheduling, this DP, or its exact-check method;
a second would be padding.

Coverage is scholarly rather than library-only: Tellache--Azerine is the problem
origin and closest boundary result, Lenstra--Rinnooy Kan--Brucker is the exact
historical hardness source being distinguished, Hefetz--Adiri is the closest
resource-free unit-time result, and Zeng et al. supports the verification-method
comparison.  The proof of the new DP is self-contained.  The negative literature
search remains explicitly bounded and makes no priority claim.

Mechanical check:
`check_bib_keys.py main.tex --aux main.aux` reported 4 cited keys, 4 BibTeX keys,
zero missing files or keys, zero unused entries, and exact AUX agreement.  The
final log scan found no undefined citation, undefined reference, missing database
entry, repeated entry, BibTeX warning, or LaTeX fatal diagnostic.
