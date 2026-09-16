# Fresh citation and bibliography audit

## Scope and frozen extraction

This release audit used a strict two-stage procedure.  Stage 1 read the complete
canonical manuscript and froze the three ordinary body-flow claim/citation pairs
as C01--C03 in audit/citation-claim-ledger.json.  Its key union is exactly
Chvatal1973, Shan2026, and ZengEtAl2026Certificates.  Comments, nocite,
definitions, hidden conditionals, and custom citation macros contribute no keys.
The canonical bibliography is manuscript/references.bib, and all three
publication sources listed in publication.json were inspected.

## Independent source verification

- C01 — Verified (exact/paraphrase).  V. Chvátal, “Tough graphs and
  hamiltonian circuits,” Discrete Mathematics 5(3), 215--228 (1973),
  DOI 10.1016/0012-365X(73)90138-6.  The Elsevier primary record identifies
  the original article and gives the toughness definition as the largest t for
  which deletion of s vertices leaves a connected graph or at most s/t
  components.  This is algebraically the manuscript's displayed condition.
  Metadata in the retained BibTeX entry matches the publisher record.

- C02 — Verified (exact).  Songling Shan, “Non-Hamiltonian 3/2-Tough Plane
  Triangulations,” arXiv:2609.05414v1.  The arXiv record confirms author, title,
  identifier, math.CO classification, and the 4 September 2026 v1 deposit.
  The supplied byte-bound primary PDF defines tetrahedral replacement on
  printed page 2 with precisely the six attachment edges used here.
  Theorem 1.4(ii), printed pages 2 and 5--6, proves only preservation of
  3/2-toughness.  It does not state the exact value law or the reverse transfer.

- C03 — Verified (paraphrase).  Z. Zeng, H. Liu, K. Ratnavelu, and O. S. Huat,
  “Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem
  and Five-Dimensional Ternary Kissing Codes,” Preprints, version 1, DOI
  10.20944/preprints202608.1658.v1.  The primary version-1 record confirms the
  title, four authors, 24 August 2026 posting, and DOI.  Its abstract and
  Sections 3, 4, and 6 describe exhaustive exact finite enumerations and
  separate independent exact verification; the abstract and Section 7
  expressly limit the conclusions to finite coordinate libraries and deny
  resolution of the unrestricted ambient problems.  This directly supports
  the revised nearby sentence.

Verification was performed on 2026-09-09 UTC using all applicable academic
search variants (author/year/title prefix, exact title with scholarly-domain
restriction, author/year/venue, DOI or arXiv identifier), followed by inspection
of the primary publisher/arXiv records and the locally preserved Shan PDF.
The Elsevier page was access-restricted on direct reopening, but its official
search record exposed the original DOI, bibliographic fields, and definition;
no claim relies on an unavailable passage.

## Coverage and consistency

Bibliography coverage is complete without padding.  Chvátal is the natural
non-library origin source for the definition; Shan is the natural non-library
source for the operation and closest prior theorem; the selected active-library
row 9 is used only for the directly supported computational-method comparison.
No additional primary work is implicitly relied upon by the short elementary
proof.  The selected library item is bound to citation attempt 1 and launch
f623d348-5c10-43c6-a885-d9cac9aaf296 in
audit/user-bibliography-selection.json.

The bibliography checker reports three cited keys, three BibTeX entries, no
missing or unused keys, and exact agreement with the final aux file.  The final
log and blg contain no undefined citation, missing database entry, duplicate
entry, BibTeX warning, LaTeX error, fatal error, emergency stop, undefined
control sequence, or runaway argument.  No BibTeX key or bibliographic record
required replacement.  Overall citation status: PASS.
