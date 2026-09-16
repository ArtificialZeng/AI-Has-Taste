# Fresh citation and bibliography audit

## Verdict

Accept. Release job `win-00042-p04-release-9bc7d7004a0e` used the requested
citation checker in two distinct passes, followed by the bibliography
consistency checker. All 24 fixed claims and all four retained references
passed. No citation is decorative, no natural primary source is omitted for a
manuscript-dependent claim, and no novelty or priority claim is made.

## Claim-to-source mapping

- `ETV2026` exists as arXiv:2609.03799v1, submitted 3 September 2026. The
  title and authors match. Its title page spells the second author "Lực Ta";
  the bibliography uses the permitted accurate ASCII transliteration "Luc
  Ta." The immutable local PDF has SHA-256
  `173a741c72a01f5a890897613279db100c41cef21d72617d01461f8d9e5230bb`.
  Lemma 6.2 and Theorem 6.3 on pp.10--11 support the exact fixed-parameter
  character/idempotent equivalence and congruence restriction; Corollary 6.4
  on p.12 supports the outside-class statement; the introduction supports the
  `(37,18)` example. It is the primary problem-origin source.
- `Dickson1935` matches the official JSTOR issue record: L. E. Dickson,
  *Cyclotomy, Higher Congruences, and Waring's Problem*, *American Journal of
  Mathematics* 57(2), 391--424 (1935), DOI 10.2307/2371217. It supports only
  the historical cyclotomy sentence; Rong--Li--Li also attribute their
  order-six lemma to this paper.
- `RongLiLi2023` matches the official AIMS record and PDF: Jianying Rong,
  Fengwei Li, Ting Li, *AIMS Mathematics* 8(7), 15317--15331 (2023), DOI
  10.3934/math.2023783. Section 2, p.15319 gives the same definition and states
  the explicit order-six lemma under `p congruent 1 (mod 24)`. The manuscript
  correctly says these formulas do not cover the other residue class.
- `202608.1658`, active user-library row 9, matches Preprints.org version 1,
  posted 24 August 2026, DOI 10.20944/preprints202608.1658.v1. Sections 4 and
  6 explicitly describe reconstructing the finite universe, exact integer
  predicates, and standard-library verification. The nearby text expressly
  limits the citation to certificate architecture and disclaims relevance to
  quandles or character sums.

## Coverage and relevance

The bibliography covers the fixed-parameter source and closest prior result,
classical cyclotomy, the precise order-six evaluation comparison, and the
finite-certificate technique. The Jacobi/Gauss identities are proved
self-contained in the manuscript, so they do not depend on an uncited external
theorem. The one user-library item is a minimum-coverage item, not a substitute
for the three natural primary sources. A second library item was not added:
row 40 was only a lead and could not be authoritatively verified, and the other
records were less relevant. The supervisor-supplied
`literature/bibliography-revision-2026-09-06-02.md` was read before editing and
its two metadata corrections are satisfied. No saved Crossref capture exists
in this project.

The user-library selection is bound to citation attempt 2 and launch
`9646371c-68e2-4af8-9aec-5cc11c140592`; its ordinary body-flow direct
`\cite{202608.1658}` and canonical `manuscript/references.bib` entry pass the
offline selection validator.

## BibTeX consistency

Four citation keys were checked; all four occur in the bibliography and final
auxiliary file, none is unused, and there are no duplicate or missing entries.
No key was changed. The final log and `.blg` contain no undefined citation,
undefined reference, missing-database-entry, repeated-entry, or BibTeX warning.
No retained citation is removable without deleting its nearby contextual or
methodological claim.

Search date: 2026-09-06. Relevant primary URLs and exact source locations are
recorded in `audit/source-locations.json`.
