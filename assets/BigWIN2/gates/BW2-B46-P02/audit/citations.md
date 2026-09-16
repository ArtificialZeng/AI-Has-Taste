# Fresh citation and bibliography audit

## Result

Accepted after one narrow historical-wording repair.  Four citation keys were
verified; none required a BibTeX replacement or key change.  The audit was
performed serially because the job expressly prohibited agents.  The two-pass
claim ledger, detailed verification, source locators, and user-library binding
are in `audit/citation-claim-ledger.json`, `audit/citation-verification.json`,
`audit/source-locations.json`, and `audit/user-bibliography-selection.json`.

| Key | Retained title | Primary record/passage | Nearby support | Action |
|---|---|---|---|---|
| `Bodlaender1991` | On the Complexity of Some Coloring Games | Utrecht University research record and abstract; DOI 10.1142/S0129054191000091 | The 1991 paper formulates coloring-game variants and studies algorithmic questions. | Metadata verified; wording narrowed; BibTeX retained. |
| `MouSunZhang2026` | The Game Chromatic Number of Generalized Mycielski Graphs of Paths and Cycles | arXiv:2609.02283v1, Section 2.1 and Theorem 5.1(1), printed p.14 | Construction/notation and the exact interval for every k>=2. | Metadata and theorem verified; BibTeX retained. |
| `AlagammaiVijayalakshmi2019` | Game Chromatic Number and Game Chromatic Index of the Mycielski Graphs of Some Families of Graphs | Publisher PDF, printed p.262, note after Theorem 2.2; DOI 10.18576/amis/13S128 | Exact one-layer comparison chi_g(mu(C_3))=4. | Metadata and claim verified; BibTeX retained. |
| `ZengLiuRatnaveluOng2026` | Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes | Official Preprints.org v1 page, abstract and Section 6; DOI 10.20944/preprints202608.1658.v1 | Symmetry-reduced finite graph/color certificates and reconstruction-oriented exact checking. | Active-library row 9 verified; BibTeX retained. |

The references form a normal claim-driven bibliography rather than a
user-library-only list: Bodlaender supplies historical/method context,
Mou--Sun--Zhang is the primary problem source and closest general bound,
Alagammai--Vijayalakshmi is the closest one-layer exact result, and the one
selected library paper supplies a genuinely close certificate-method example.
No additional active-library paper was comparably relevant, so adding a second
would be padding.  Every retained key is cited directly in ordinary body flow.

Mechanical checks found four cited keys, four BibTeX entries, no missing or
unused entries, and an identical four-key set in `main.aux`.  The final log and
`.blg` contain no undefined citation/reference, missing database entry,
duplicate-entry, BibTeX warning, or LaTeX error.
