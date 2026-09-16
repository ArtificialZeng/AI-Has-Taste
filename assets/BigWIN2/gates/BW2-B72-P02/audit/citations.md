# Fresh citation and bibliography audit

Mode: two-stage search verification with primary-document replay.  Date:
2026-09-08.  Release job: `win-00072-p02-release-4361c535348d`; citation
attempt 2; launch `290cb2e7-d189-431c-9aff-2e62d8391e47`.

## Result

**Accept.**  `audit/citation-claim-ledger.json` froze fifteen substantive
claims before verification.  Its direct-citation union is exactly the four-key
ordinary body-flow citation set in `manuscript/main.tex`.  Each externally
attributed claim is supported by the cited primary source, and the internal
finite claims remain within the accepted mathematical scope and agree with the
frozen exact evidence.  No decorative reference or unsupported strengthening
remains.

The user prohibited subagents for this bounded job, so the required per-key
audit was performed sequentially in the release context.  All applicable
academic title, author, venue, DOI, and arXiv searches were run before the
original text was inspected; search snippets were not used in place of the
primary records.

## Pass 1: fixed claim surface

The attempt-bound UTF-8 schema-version-1 ledger records claims C01--C15 with
substantive text, types, exact current line intervals, and direct citation
keys.  It is bound to accepted mathematical snapshot
`2abe4780cf2ee63a3e3d3d055f8872c214ef674ae76f40ced8f5c85ef8e20c76`
and manuscript digest
`c1970401fc3e0e950de8f57b104464e0a8c30deffb86a2f214e36c70c88552b8`.
No custom cite macro, `\\nocite`, comment-only citation, verbatim citation, or
hidden conditional contributes a key.

## Pass 2: exact primary-source support

| Claims | Key or evidence | Exact primary location and support | Status |
|---|---|---|---|
| C02 | `KotsireasWinterhof2024` | Official arXiv:2212.10953v1 abstract says the authors introduce qLPs and relate them to quaternary Hadamard matrices of order `2l+2` and hence binary Hadamard matrices of order `4l+4`; printed pp. 4--5, Theorem 1, gives the construction.  The Springer DOI record confirms the two authors, chapter title, 2024 volume 86, pp. 289--304, and DOI. | Verified, exact paraphrase and metadata |
| C03--C04 | `Lebedev2026` | Archived official arXiv:2609.04589v1 PDF, printed p. 8, section “An explicit pair whose displayed orientation is not reversible,” says the printed orientation fails reversibility and that an equivalence-class conclusion would require an orbit argument not carried out there.  Appendix A, printed p. 12, gives the two literal length-34 words exactly. | Verified, exact/paraphrase |
| C05 | `BulutogluBaczkowskiYauney2026` | Archived official arXiv:2604.22423v1 PDF, printed pp. 2--3, equations (1.2)--(1.5), defines decimation and displays both the common-decimation and opposite-decimation alternatives for binary LP equivalence.  The arXiv record confirms title, three authors, date, subject, v1, and DOI. | Verified, exact |
| C12 | `ZengEtAl2026Finite` | Official Preprints.org version-1 HTML: the abstract reports exhaustive symmetry-reduced enumeration of 15,056 maximal feasible sets and explicitly calls the results finite-library theorems that do not settle the unrestricted Borsuk or kissing-number questions.  Section 3 describes the orbit enumeration, and Section 7 repeats the scope boundary. | Verified, exact paraphrase |
| C01, C06--C11, C13--C15 | Accepted mathematical audit and frozen exact project evidence | `audit/math.md` independently reconstructs the Gray-map equivalence, the 17-axis obstruction, all generator identities, and the exact scope.  `evidence/orbit_resolution.md`, `evidence/orbit_census_output.json`, and `evidence/orbit_census_verification.json` give the exact counts, digests, implementation separation, and all-checks-passed result stated in the manuscript.  A fresh literal-word replay reproduced all 17 table rows. | Verified against frozen primary evidence |

The selected user-library record was independently checked on its official
version-1 page rather than accepted from registry metadata.  It is cited only
for the narrow finite-enumeration and scope-boundary comparison.  Its title,
authors, DOI, version status, exact supporting locations, and literal current
manuscript context are bound in `audit/user-bibliography-selection.json`.

## Bibliography correctness and coverage

| Final key | Current and official title/source | Action | Key change | Uncertainty |
|---|---|---|---|---|
| `KotsireasWinterhof2024` | *Quaternary Legendre Pairs*; official arXiv and Springer chapter record | Verified; no replacement | None | None |
| `Lebedev2026` | *Quaternary Legendre Pairs of Lengths 42, 46, 52, 58, 66, 72, and 80*; official arXiv v1 | Verified; no replacement | None | None |
| `BulutogluBaczkowskiYauney2026` | *Determining the Group That Sends Each Legendre Pair to an Equivalent Legendre Pair*; official arXiv v1 | Verified; no replacement | None | None |
| `ZengEtAl2026Finite` | *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*; official Preprints.org v1 | Verified; no replacement | None; the scholarly final key intentionally differs from registry key `202608.1658` | None |

Four references were freshly reverified.  The recovery edit changed only the
purely typographic bibliography grouping in `manuscript/main.tex`; it did not
change any claim, citation context, citation key, or BibTeX entry.  The exact
source locators and support were replayed against the current claim ledger.
No retained key changed and no verification blocker remains.

Coverage is complete and proportionate.  The non-library primary sources cover
the qLP origin and Hadamard link, the exact motivating pair and nearest prior
statement, and the binary equivalence formulas.  The one selected library paper
supports a genuine methodological/scope comparison.  The paper's reflection
argument and elementary reindexing are self-contained, so further citations
would be padding.

The bibliography checker reports four cited keys, four BibTeX keys, no missing
or unused entry, and exact equality with the final AUX set.  The converged
`main.log` and `main.blg` contain no undefined citation/reference, missing
database entry, repeated entry, BibTeX warning, LaTeX error, fatal stop,
undefined control sequence, runaway argument, overfull box, or underfull box.
