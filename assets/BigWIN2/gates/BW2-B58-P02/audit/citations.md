# Citation and bibliography audit

**Verdict: accept.** Search verification was performed on 2026-09-07 after
freezing the eight citation-bearing claim pairs in
`audit/citation-claim-ledger.json`. Verification did not alter that claim set.
The user prohibited agents, so the six keys were checked serially in this
release context. All applicable author/title/venue, title, DOI/arXiv, and
identifier search templates were run; primary publisher, repository, or paper
text was then inspected. There is no `literature/` directory in this project,
so no supervisor bibliography-revision or saved Crossref capture was available.

## Claim-to-source verification

| Claim | Key | Primary location | Status | Confidence |
|---|---|---|---|---|
| C01 | `HaeuplerShahrasbi2017` | arXiv:1704.00807, abstract and introduction; STOC 2017, pp. 33--46 | Verified: the authors introduce synchronization strings for efficiently handling insertions and deletions through indexing. | paraphrase |
| C02 | `ChengEtAl2019` | SIAM publisher abstract, final paragraph; SODA 2019, pp. 2185--2204, DOI 10.1137/1.9781611975482.132 | Verified: four symbols are constructed for some constant parameter and binary strings are excluded at arbitrary length. | exact |
| C03 | `XuEtAl2026` | arXiv:2609.04122v1, abstract and Theorem 1.5, p. 5 | Verified: the ternary case and the computer-assisted 54/952 refinement with weak gap 1/227 are stated exactly. | exact |
| C04 | `SollamiEtAl2016` | Journal of Integer Sequences 19 (2016), Article 16.6.7, abstract and construction; also Xu et al., Proposition D.1, p. 32 | Verified: construction of a special 54-Brinkhuis 952-triple and square-free substitution property. | exact |
| C05 | `XuEtAl2026` | Lemma D.2, p. 32; Lemma D.5, p. 34; Appendix E | Verified: fragment-aware conditional point mass and the event-volume bound are the cited framework. | paraphrase |
| C06 | `ErdosLovasz1975`, `XuEtAl2026` | Erdős--Lovász bibliographic record, Infinite and Finite Sets 10 (1975), pp. 609--627; Xu et al., Theorem 2.3 and Lemma D.6/Proposition D.7, pp. 35--36 | Verified with divided support: the 1975 item supports local-lemma provenance, while Xu et al. supports the exact asymmetric charge implication and constant 109. | paraphrase |
| C07 | `XuEtAl2026` | Lemmas D.3--D.4, p. 33; Proposition D.7, pp. 35--36 | Verified: the old odd and even shell exclusions are codebook statements, with the exact published totals used nearby. | exact |
| C08 | `ZengEtAl2026` | Preprints.org manuscript 202608.1658v1, Section 6, Certificate Architecture and Reproducibility | Verified: the paper explicitly separates discovery from certification, reconstructs finite objects with a standard-library verifier, and uses integer/rational decisive comparisons. | exact |

Primary URLs and source locations are frozen in
`audit/citation-source-locations.json`. Exact numerical claims match their
sources; there are no numerical errors, misquotations, unsupported
strengthenings, or source contradictions.

## Bibliographic metadata and coverage

All six cited works exist. Author lists, titles, years, venues/repository
records, page spans, and the four supplied DOI/arXiv identities match the
primary records. No BibTeX replacement or citation-key change was needed.
Mechanical extraction finds six cited keys, six canonical entries, no missing
or unused entry, and identical source and `.aux` key sets.

Coverage is proportionate rather than quota-driven: Haeupler--Shahrasbi covers
the object's origin; Cheng et al. covers the closest pre-ternary alphabet
frontier; Xu et al. is the problem origin, closest quantitative result, and
method source; Sollami et al. supplies the codebook; Erdős--Lovász supplies
local-lemma provenance; and Zeng et al. is the single genuinely relevant item
from the active 49-record user library, used only for an exact-verification
design comparison. The last citation is an ordinary body-flow
`\cite{ZengEtAl2026}` and is bound to attempt 1 and launch
`f1370303-57b1-4cb1-9471-cf1f98e2b105` in
`audit/user-bibliography-selection.json`. A second library item would be
decorative, so none was added. The bibliography is neither Excel-only nor
user-library-only, and no retained citation is decorative.

The manuscript's bounded-search sentence is explicitly not a priority claim.
The primary Xu v1 record proves 1/227, whereas this accepted scoped manuscript
proves 1/226 in the same fixed framework; no claim of least denominator or
global optimality appears.

## Mechanical checks

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reports six
cited keys, six bibliography keys, no missing bibliography, no missing or
unused key, and no source/aux discrepancy. Final `main.log` and `main.blg`
contain no undefined citation/reference, missing database entry, repeated
entry, BibTeX warning, LaTeX error, fatal error, or runaway/undefined-control
diagnostic.
