# Citation and bibliography audit

Search verification date: 2026-09-07.  The two-stage audit used the frozen
pass-1 ledger `audit/citation-claim-ledger.json`; no claims were added during
verification.  Sub-agents were not used because the job explicitly prohibited
agents and background workers.

## Claim-level verification

| ID | Key | Source location checked | Result |
|---|---|---|---|
| C01 | `Bodlaender1991` | Utrecht University institutional publication record and archived primary technical-report PDF, abstract and opening description; DOI `10.1142/S0129054191000091` | Verified (paraphrase).  The 1991 paper exists with the stated author, title, journal, volume, issue, pages, year, and DOI.  It studies alternating proper graph-coloring games, including the version in which player 1 wins exactly when all vertices are colored.  The later target source also explicitly attributes the game chromatic number to Bodlaender. |
| C02 | `MouSunZhang2026` | arXiv:2609.02283v1, PDF page 3, Section 2.1, displayed vertex and edge construction | Verified (exact mathematical match after the harmless change from indices `1,2,3` to `0,1,2`).  Setting `G=C_3` and `k=3` yields exactly the manuscript's 13 vertices and 24 edges. |
| C03 | `MouSunZhang2026` | arXiv:2609.02283v1, PDF page 14, Theorem 5.1(1) | Verified (exact).  The theorem states `4 <= chi_g(M_k(C_3)) <= 5` for `k >= 2`; it gives no exact selection for `k=3`.  The manuscript's bounded novelty wording is therefore supported and does not assert priority. |
| C04 | `ZengEtAl2026Certificates` | Preprints.org version 1, abstract; Section 3 proof of Theorem 1; Section 6 certificate architecture | Verified (paraphrase).  The source reports exhaustive symmetry reduction, an explicit finite certificate, independent re-enumeration/reconstruction, and exact checking.  It is explicitly identified as a non-peer-reviewed preprint in the authoritative record. |
| C05 | `HagbergSchultSwart2008` | Authors' publication page, official citation/BibTeX; SciPy 2008 proceedings paper, pages 11--15 | Verified (paraphrase).  The record identifies NetworkX as a graph/network algorithms package.  Project source `evidence/verify_q4_strategy.py`, lines 19 and 50--51, confirms that this manuscript's checker uses `networkx.algorithms.isomorphism.GraphMatcher(...).isomorphisms_iter()`. |

## Bibliographic-record audit

All four body-cited records were checked against primary or authoritative
records.  The titles, authors, years, and venues in `manuscript/references.bib`
agree with those records.  The DOI and pages for Bodlaender, the arXiv identifier
and version date for Mou--Sun--Zhang, and the DOI/version date for Zeng et al.
match exactly.  The NetworkX authors' official BibTeX confirms pages 11--15 and
the current entry; its later DOI `10.25080/tcwv9851` is optional metadata and its
absence does not make the retained record false or ambiguous.  No key change or
BibTeX replacement was required.

The compiled citation surface contains four unique keys in five body-flow cite
occurrences.  Every key exists in the canonical `manuscript/references.bib`, all
four appear in the final `.aux` and `.bbl`, and there are no uncited database
entries, duplicate keys, undefined citations, or unresolved references.

## Coverage and relevance

Coverage is complete for the manuscript's actual external dependencies:

- Bodlaender is the primary origin record for the graph-coloring game.
- Mou--Sun--Zhang supplies the target construction and closest prior bound.
- Hagberg--Schult--Swart identifies the software used for graph-isomorphism
  enumeration.
- Zeng--Liu--Ratnavelu--Ong is a directly relevant recent methodological example
  of exact, symmetry-reduced, independently checked finite certification and is
  active user-library row 9.

No additional user-library paper supports a natural nearby claim, and adding
one would pad the bibliography.  Conversely, the bibliography is not
user-library-only: it contains the three non-library primary sources naturally
required by the paper.  No retained citation is decorative or removable without
losing origin, closest-prior-result, implementation, or method context.

## Verdict

Accept.  Five claim/citation pairs are verified, bibliography coverage is
scholarly and proportionate, and no citation or scope defect remains.
