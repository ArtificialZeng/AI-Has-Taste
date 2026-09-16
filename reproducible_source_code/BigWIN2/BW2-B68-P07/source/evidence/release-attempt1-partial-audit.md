# Release attempt 1: substantive partial audit

The fresh release worker `win-00068-p07-release-eadd8e9c81a2` reached the
fixed 15-minute phase ceiling before it could return its structured result.
The attempt nevertheless created decision-relevant evidence after the prior
blocked state:

- it repaired a parser-only TeX incompatibility without changing the accepted
  theorem;
- it rebuilt and refroze the five-page manuscript;
- `manuscript/references.bib` contains seven claim-driven entries and the
  compiled auxiliary file contains exactly the same seven cited keys;
- the final build log has no undefined citations, undefined references,
  BibTeX missing-entry diagnostics, or LaTeX fatal errors;
- every font reported by `pdffonts` is embedded;
- the active user-library validator accepts the one selected library record
  for citation attempt 1, while the six additional bibliography entries are
  ordinary claim-relevant sources;
- the worker rendered all five pages and began the claim-by-claim primary
  source audit, including locating Corollary 5.5 of arXiv:2604.10336 on PDF
  page 23.

Frozen manuscript snapshot:

- manuscript digest:
  `34cf4cefa7e5a40c2841ab0f2ee3574e62a8df18ac6e4cc2ec9b9a7f05facd9f`
- PDF digest:
  `0529eee7bdf32200f1c4030f15348f795e920c6c1473036a411ef116030cbbf8`
- accepted mathematical snapshot:
  `a880303a4e43dbf97139b6534dd02b8dbe50202ac203f9101f52b594b8b30519`

Next decisive test: in one fresh release context, finish the already-started
claim/source ledger, write the citation and visual audit records, execute the
configured pre-publication hook, run `release_gate.py check`, and accept only
if the resulting manifest is bound to the frozen manuscript and PDF hashes.
No mathematical re-research or scope expansion is required.
