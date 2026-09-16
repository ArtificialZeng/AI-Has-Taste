# Fresh citation and bibliography audit — attempt 2

## Verdict

Accept. Pass 1 froze 20 claims and their citation keys in
`audit/citation-claims.json` before verification. Pass 2 then checked those
fixed pairs sequentially against the accepted mathematical audit, exact local
artifacts, the immutable Mao PDF, and the official primary records located in
`audit/source-locations.json`. All 20 claims and all eight cited works pass.
No source is decorative, no natural primary dependency is omitted, and the
manuscript makes no comprehensive novelty or priority claim.

## Fixed-claim results

| Claim | Result | Evidence |
|---|---|---|
| C01--C02 | Verified (exact) | `claim.json`, `audit/math.md`, template manifest, coefficient data, and Muirhead certificate support the TP4 scope and every displayed count. |
| C03 | Verified (paraphrase) | The official 1995 Elsevier abstract describes the systematic connection between combinatorics and totally positive matrices. |
| C04 | Verified (exact attribution) | Springer's official 1996 chapter record supplies author/title/venue/pages/DOI; Mao p.1 identifies this chapter's Conjecture 6.10 as the Eulerian-triangle conjecture. |
| C05--C07 | Verified (exact/paraphrase) | Mao Theorem 1.1, Remark 1.2, and the bounded comparison wording support TP3, the unverified 126-case computation, and the closest-inspected-work statement. |
| C08 | Verified (paraphrase) | The original Frobenius record exists; Mao Lemma 3.1 states and attributes the exact negative-zero consequence used. |
| C09 | Verified (paraphrase) | The full PNAS paper exists with matching metadata; its finite Pólya-frequency criterion, as specialized explicitly on Mao p.4, gives the coefficient-Toeplitz claim. |
| C10 | Verified (exact) | Mao Lemma 2.6 is the displayed derivative identity with the manuscript's hypotheses. |
| C11 | Verified (exact) | The frozen template manifest and accepted mathematical audit reproduce all seven survivor counts, their sum, and the 118-plus-one excluded slots. |
| C12--C13 | Verified (paraphrase/exact) | Muirhead Section 1 supports the normalized-majorization inequality; the frozen exact certificate supports the six-template, 18-orbit, supply, and demand figures. |
| C14--C15 | Verified (exact) | The accepted audit checks the Schur summand and boundary case; Mao Theorems 2.5 and 1.1 have the cited scope and hypotheses. |
| C16 | Verified (exact) | Local execution returned Python 3.10.12 and SymPy 1.14.0; the official PeerJ article identifies SymPy as the cited symbolic system. |
| C17--C18 | Verified (paraphrase) | Preprints.org v1, Sections 3--4, directly gives exhaustive finite-family reconstruction, exact integer predicates, and replay verification, while its stated scope is unrelated to Eulerian TP4. |
| C19--C20 | Verified (project record/exact scope comparison) | The process disclosure agrees with the frozen project record, and a line-by-line comparison with `claim.json` and `audit/math.md` finds no unsupported strengthening. |

## Per-reference support and metadata

- `AissenEtAl1951`: author, title, PNAS 37(5), 303--307, year, and DOI match
  the official full record. It supports only the coefficient-Toeplitz input.
- `Brenti1995`: author, title, JCTA 71(2), 175--218, year, DOI, and broad
  systematic-connection claim match the official Elsevier record. It is not
  used for the conjecture's origin.
- `Brenti1996`: Springer confirms the chapter, editors, series volume 359,
  pages 451--473, year, and DOI `10.1007/978-94-015-8674-0_22`. Mao p.1
  confirms the Conjecture 6.10 attribution. The BibTeX now uses this precise
  chapter DOI and URL.
- `Frobenius1910`: the library record and original scan match the author,
  title, year, and pages 809--847; Mao Lemma 3.1 supplies the modern theorem
  wording actually used.
- `Mao2026`: arXiv confirms Jianxi Mao, title, v1 date 29 August 2026, category,
  identifier, and 18-page extent. The inspected immutable PDF contains every
  cited theorem, lemma, remark, and hypothesis.
- `MeurerEtAl2017`: official PeerJ metadata matches title, authors, volume 3,
  e103, year, and DOI; it supports only the SymPy software attribution.
- `Muirhead1902`: Cambridge confirms author, title, volume 21, pages 144--162,
  year, and DOI. Its primary PDF's first section states the normalized
  permutation-sum setup and the inequality theorem used.
- `202608.1658`: Preprints.org confirms all four authors, title, version 1,
  posting date, DOI, and non-peer-reviewed preprint status. Its body directly
  supports only the exact-certificate architecture comparison.

## Coverage, library binding, and BibTeX consistency

The eight-reference bibliography has normal scholarly coverage: Brenti 1995
for broader context, Brenti 1996 for problem origin, Mao for the closest result
and relied-on reductions, Frobenius for Eulerian real-rootedness, Aissen et al.
for the Pólya-frequency criterion, Muirhead for the nontrivial inequality, and
Meurer et al. for SymPy. The single active-library paper supplies a narrow,
directly supported reproducibility comparison and displaces none of these
primary sources; adding a second library item would be padding.

`audit/user-bibliography-selection.json` is bound to runner-issued citation
attempt 2 and launch `01cfaf66-1ad8-4162-8a14-9bb4ca9a0dec`, the active
49-record first-sheet registry, and row 9. The selected item has an ordinary
body-flow direct `\cite{202608.1658}` and only the canonical
`manuscript/references.bib` supplies it.

The bibliography checker found eight cited keys and eight unique BibTeX
entries, with no missing, unused, or `.aux`-inconsistent keys. The converged
`.log` and `.blg` have no undefined citation/reference, missing database entry,
duplicate entry, BibTeX warning, LaTeX error, or fatal diagnostic. No citation
key changed. Verification was serial because the user expressly prohibited
sub-agents and background workers.

Search date: 2026-09-06. Before live-source verification, the required
`literature/crossref-*.json` and `.md` inventory was empty; official publisher,
arXiv, library-scan, and immutable local-primary records were sufficient.
