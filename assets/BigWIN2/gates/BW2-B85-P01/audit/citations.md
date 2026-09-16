# Fresh citation and bibliography audit

Release job: `win-00085-p01-release-dc2c5030af7e`  
Citation attempt: `2`  
Launch UUID: `b277ee91-fbb3-465b-9a75-44ac98868e1c`  
Verification date: 2026-09-09 UTC

## Scope and two-stage method

Pass 1 froze the four ordinary body-flow claim/citation pairs in
`audit/citation-claim-ledger.json`, before source verification.  The union of
its keys is exactly the four-key body-flow citation set extracted from
`manuscript/main.tex`; comments, bibliography commands, and non-body material
were not counted.

Pass 2 independently checked each frozen pair against the primary publication
record and the exact source passage.  Search verification used the academic
query templates (author/year/title fragment, full title, venue, DOI, and arXiv
identifier where applicable), then inspected the original arXiv, APS, Caltech,
or Preprints.org record rather than relying on snippets.  Bibliographic
author/title/year/venue/identifier data were compared with
`manuscript/references.bib`.  The accepted mathematical audit and the two exact
programs were used only to check that the authored theorem was not strengthened;
they were not treated as external citation evidence.

## Frozen claims and primary-source verification

| Claim | Key | Primary source and exact locator | Result |
|---|---|---|---|
| CIT-01 | `Gottesman1997` | Daniel Gottesman, *Stabilizer Codes and Quantum Error Correction*, arXiv `quant-ph/9705052`, Chapter 3, Section 3.2: the stabilizer is an Abelian Pauli subgroup and the coding space is its fixed space; the displayed definition gives the simultaneous `+1` eigenspace and excludes `-1`/nontrivial scalar phases. The arXiv record and CaltechTHESIS record confirm author, title, 1997 PhD status, and institution. <https://arxiv.org/html/quant-ph/9705052> | **Verified (paraphrase).** The nearby sentence is a faithful compact definition. |
| CIT-02 | `Mahmoud2026` | Ali Assem Mahmoud, *Minimal Counterexamples of the MacWilliams Extension Theorem for Stabilizer Codes*, arXiv `2607.26214v1`, Theorem 5.3(ii),(iii) and Question 5.4. The theorem displays exactly the four generator triples, states the five-qubit pair's weight isometry and lack of monomial equivalence, and gives the six-qubit pair with its common enumerator in the same counterexample context; the paragraph after the theorem and Question 5.4 state that general product-unitary-plus-permutation equivalence of both pairs was unknown. <https://arxiv.org/html/2607.26214v1> | **Verified (paraphrase).** The source-origin and open-question claims match the stated scope. |
| CIT-03 | `VanDenNestEtAl2004` | Maarten Van den Nest, Jeroen Dehaene, and Bart De Moor, *Local invariants of stabilizer codes*, *Physical Review A* 70, 032323 (2004), Eq. (14) and its surrounding paragraph. Eq. (14) identifies a degree-two LU invariant with the dimension of the binary stabilizer subspace whose supports lie in a prescribed coordinate set; the APS issue record confirms authors, title, article number, date, and DOI. <https://arxiv.org/html/quant-ph/0404106v2> and <https://journals.aps.org/pra/abstract/10.1103/PhysRevA.70.032323> | **Verified (paraphrase).** Hypotheses and the prior-art boundary are retained. |
| CIT-04 | `ZengEtAl2026ExactFinite` | Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org version 1, Section 6. The official record says that ancillary files separate discovery from certification, describes exact integer/rational checking, a standard-library verifier, and an independent exact implementation. <https://www.preprints.org/manuscript/202608.1658/v1> | **Verified (paraphrase).** The manuscript uses it only for a method analogy and expressly disclaims dependence of the stabilizer proof on that work. |

All four cited works exist.  No source contradicts or materially qualifies its
nearby claim.  There are no direct quotations and no externally sourced rounded
statistics.  The finite counts and rank profiles in the paper are internal
mathematical claims supported by the displayed certificate, accepted audit, and
exact programs rather than by these citations.

## Bibliography correctness and coverage

The canonical bibliography contains four used entries and no unused entries.
Each entry's title, authors, year, venue/type, DOI or arXiv identity, and cited
version agree with a primary record.  No BibTeX or citation key was changed.
The entry `ZengEtAl2026ExactFinite` is active-library row 9 and its DOI exactly
matches the registry-bound selection.

Coverage is complete without padding:

- `Mahmoud2026` is the primary problem-origin and closest-prior-result source.
- `VanDenNestEtAl2004` is the primary source for the nontrivial LU invariant.
- `Gottesman1997` supports the standard stabilizer-code definition.
- `ZengEtAl2026ExactFinite` supports the narrow reproducibility-method analogy
  and is the single genuinely relevant active user-library paper.

Thus the body contains three natural non-library sources as well as the required
library source.  An Excel-only or library-only bibliography was not used.

The mechanical audit reported 4 cited keys, 4 BibTeX keys, no missing or unused
keys, and exact agreement with the final `.aux`.  The converged build log and
`.blg` contain no undefined citations, missing database entries, repeated
entries, LaTeX errors, or fatal diagnostics.  The audit was performed directly
in this release context because the user expressly prohibited spawning agents.

## Verdict

**ACCEPT.** All frozen citation claims are supported by the cited primary
passages, bibliographic identities are correct, coverage is natural and
complete for the manuscript's actual dependencies, and no unsupported
strengthening of the accepted mathematical scope was found.
