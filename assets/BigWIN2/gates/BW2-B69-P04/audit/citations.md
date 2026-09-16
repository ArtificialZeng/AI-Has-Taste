# Citation and bibliography audit

## Verdict and scope

Accept. For citation attempt 2 of release job `win-00069-p04-release-5a943a0eb78e`, on 2026-09-08 I froze the seven-item claim ledger and then audited it in a separate verification pass against the original publication records and exact cited passages. All seven claims are supported: six directly or by faithful paraphrase and one (the scope limitation attached to Whitehead) by a conservative interpretation of what that source proves. There are no numerical errors, unsupported strengthenings, decorative references, undefined citations, or unresolved bibliographic identities.

The ordinary body-flow citation-key set is exactly `allcock2026arithmetic`, `whitehead2026note`, and `zeng2026finite`. Its union agrees exactly with `audit/citation-claim-ledger.json`. The canonical bibliography contains exactly those three entries; the final `.aux` contains the same three keys.

## Claim-to-source replay

| Claim | Key | Primary passage | Result |
|---|---|---|---|
| C01 | `allcock2026arithmetic` | arXiv v1 HTML line 790 onward, Appendix B.1 face numbering | Verified, paraphrase |
| C02 | `allcock2026arithmetic` | arXiv v1 HTML lines 184–196, Definition 2.1 and the reflective/general-tiling distinction | Verified, paraphrase |
| C03 | `allcock2026arithmetic` | arXiv v1 HTML lines 682–691, Proposition 7.10 | Verified, exact |
| C04 | `allcock2026arithmetic` | arXiv v1 HTML lines 706–710, Conjecture 7.11 | Verified, exact |
| C05 | `whitehead2026note` | arXiv v1 HTML lines 28–57, abstract and Theorems 1–2 | Verified, conservative interpretation: abstract realizability does not certify an embedding in the fixed SW2 chamber tiling |
| C06 | `zeng2026finite` | Official v1 lines 62–65 and 207–240, abstract, certificate architecture, and limitations | Verified, paraphrase |
| C07 | `allcock2026arithmetic` | arXiv v1 HTML lines 660–691, Lemma 7.9 and Proposition 7.10(1)–(2) | Verified, exact |

## Source identities and retained uses

1. Daniel Allcock, Pat Devlin, Anna Felikson, Alex Kontorovich, and Ian Whitehead, *Arithmetic Polyhedra*, arXiv:2609.05349v1. Official record: <https://arxiv.org/abs/2609.05349v1>; passage text: <https://arxiv.org/html/2609.05349v1>. The official record confirms title, five authors, category, version, and 4 September 2026 submission. This is the indispensable non-library primary source for the problem, definitions, closest theorem, dichotomy, block decompositions, and conjecture.

2. Ian Whitehead, *A note on right-angled, ideal hyperbolic polyhedra*, arXiv:2609.05389v1. Official text: <https://arxiv.org/html/2609.05389v1>. The header confirms the author, identifier, category, version, and date; the abstract and Theorem 2 give the stated combinatorial realization characterization. This is a natural non-library source for the manuscript's realization-screen comparison.

3. Zijian Zeng, Houde Liu, Kuru Ratnavelu, and Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org v1, DOI 10.20944/preprints202608.1658.v1. Official record and text: <https://www.preprints.org/manuscript/202608.1658>. The official page confirms all four authors, version 1, submission/posting dates, and the exact symmetry-reduced enumeration, integer-predicate, and finite-library limitation claims. It is the sole gate-selected user-library source and is used in ordinary body flow for a genuine methodological comparison.

No second entry among the active 49-item first-sheet user library is comparably relevant; adding one would pad the bibliography. The two non-library sources occur naturally in ordinary body flow, so the bibliography is not Excel-only or library-only. The manuscript proves its chamber-expansion and exact-geometric lemmas in full and does not depend on an uncited external computational theorem. No retained reference is decorative.

## Mechanical audit

The bibliography checker found one canonical bibliography file, three cited keys, three BibTeX entries, no missing or unused entries, and exact agreement with `main.aux`. A converged BibTeX/LaTeX build produced no undefined citation/reference, missing database entry, repeated entry, BibTeX warning, LaTeX error, fatal error, emergency stop, undefined control sequence, or runaway argument. No citation keys or BibTeX records required replacement.

Audit method: two-stage citation-check protocol (claim extraction frozen first, then sequential primary-source verification), mandatory exact-title/author/venue/identifier searches for each work, direct inspection of original publication text, registry/workbook checksum binding for the selected library item, and the `bib-reference-audit` mechanical key/log checks. Subagents were not used because the bounded job explicitly prohibited spawning them.
