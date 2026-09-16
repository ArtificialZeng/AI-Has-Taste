# Citation and bibliography audit

**Mode:** search verification.  **Search date:** 2026-09-07.  **Result:** pass.

The extraction pass was frozen first in `audit/citation-claim-ledger.json`.
Verification then used only claim identifiers C01--C04.  No subagents were used
because the job prompt expressly prohibited agents and background workers.

| Claim | Key | Result | Exact source support |
|---|---|---|---|
| C01 | `JezernikSpenko2025` | Verified (paraphrase) | The arXiv record identifies Urban Jezernik and Špela Špenko, submission 10 April 2025, title *Additive diameters of group representations*. Its abstract defines the group-representation diameter and says the paper investigates analogous Lie-representation notions; Sections 1.5.4 and 6 give those notions. |
| C02 | `JezernikSpenko2026` | Verified (exact) | The arXiv record identifies both authors, submission 3 September 2026, and the stated title. The original v1 PDF, pp. 29--32, defines the monomial Lie-additive diameter in Section 8, proves the `sl_3` symmetric-power formula in Theorem 8.1, and asks the all-`n,k` formula in Question 8.5. |
| C03 | `ZengEtAl2026Certificates` | Verified (paraphrase) | The Preprints.org primary page identifies the four authors, title, version 1, posting date 24 August 2026, and DOI `10.20944/preprints202608.1658.v1`. Section 4 uses an integer compatibility predicate and a separate exact implementation reconstructing the graph; Section 6 lists separate standard-library and independent exact verifiers. |
| C04 | `JezernikSpenko2026` | Verified (interpretation) | Question 8.5 in the original v1 PDF quantifies over all higher-rank `n,k`, while the manuscript proves only the displayed `(4,3)` instance. The non-resolution sentence is therefore a direct scope comparison. |

## Primary records and source locations

- `JezernikSpenko2025`: <https://arxiv.org/abs/2504.07573>; current arXiv
  HTML, abstract and Sections 1.5.4 and 6.  Submitted 10 April 2025; current v2
  revised 3 September 2026.
- `JezernikSpenko2026`: <https://arxiv.org/abs/2609.03882>; attached original
  v1 PDF `evidence/external/2609.03882.pdf`, pp. 29--32, Section 8, Theorem 8.1,
  Question 8.5.  The attached file has the frozen source SHA-256.
- `ZengEtAl2026Certificates`:
  <https://www.preprints.org/manuscript/202608.1658>; Sections 4 and 6 and the
  article header.  The DOI, author list, title, version, and posting date match
  `manuscript/references.bib`.

## Bibliography coverage and mechanics

All three retained sources are needed.  The two Jezernik--Špenko papers are the
primary source for the definition/problem and the closest earlier treatment;
the active user-library paper supports the nontrivial verification-architecture
comparison.  No source is decorative, and no other primary literature is
naturally required for the elementary linear-algebra proof.  The bibliography
is therefore neither user-library-only nor padded.

The ordinary body flow directly cites all three final keys.  The key checker
found 3 cited keys, 3 database keys, no missing or unused entries, and an exact
match with the final AUX citations.  Final `main.log` and `main.blg` contain no
undefined citation, missing database entry, repeated-entry, LaTeX error, or
cross-reference warning.  No BibTeX key or manuscript citation needed repair.
