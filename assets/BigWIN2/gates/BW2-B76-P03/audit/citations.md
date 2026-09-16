# Fresh citation and bibliography audit

Mode: two-stage search verification with direct inspection of primary publication
records and local publication inputs.  UTC verification date: 2026-09-08.
Release job: `win-00076-p03-release-f17ba9de4d6f`; citation attempt 4;
launch `6bfc80ef-a9bd-476c-8a7c-44d824a1ff72`.

## Result

All five ordinary body-flow citation keys exist, their bibliographic identities
are accurate, and their sources support the seven frozen nearby claims.  There
are no undefined citations, unused bibliography records, stale auxiliary keys,
or decorative references.  The bibliography contains natural non-library
primary sources as well as one directly relevant active user-library paper.
Citation verdict: **accept**.

The audit was performed locally because the user expressly prohibited agents
and other workers for this bounded job.

## Pass 1: fixed claim surface

`audit/citation-claim-ledger.json` freezes seven substantive claim/citation
pairs, with precise line intervals, before the verification decision.  The
union of their keys is exactly
`Fuglede1978`, `Ishihara1979`, `MeurerEtAl2017`,
`NicolussiGoloPinamontiWarhurst2026`, and
`ZengLiuRatnavelu2026`, which is also the complete ordinary body-flow citation
set extracted from `manuscript/main.tex`.  Comments, `\nocite`, inert macros,
verbatim text, and hidden conditionals supply no citations.

## Pass 2: claim-level verification

| Claim | Key(s) | Primary record and exact support | Status |
|---|---|---|---|
| CIT-01 | `Fuglede1978`, `Ishihara1979` | The Centre Mersenne version-of-record page for Fuglede gives the title, author, *Annales de l'Institut Fourier* 28(2), 107--144 (1978), DOI `10.5802/aif.691`, and an abstract establishing the harmonic-morphism characterization.  Ishihara's DOI `10.1215/kjm/1250522428` resolves to the paper *A Mapping of Riemannian Manifolds Which Preserves Harmonic Functions*, *Journal of Mathematics of Kyoto University* 19(2), 215--229 (1979).  The official arXiv:2609.04299v1 introduction, lines 127--132, identifies the two papers as the foundational Fuglede--Ishihara characterization. | Verified (paraphrase) |
| CIT-02 | `NicolussiGoloPinamontiWarhurst2026` | Official arXiv:2609.04299v1, Definition 8.2 and equations (57)--(60), HTML lines 631--645, introduce the horizontal and vertical modular characters and their modular mismatch for a polarized Lie algebra with a complement. | Verified (exact) |
| CIT-03 | `NicolussiGoloPinamontiWarhurst2026` | The same primary source, Theorem 10.5 (HTML lines 892--908), Theorem 10.7 and equation (97) (938--949), and Section 10.2 (959--964), states exactly the sufficient-versus-necessary gap and Question 1 used in the manuscript.  Definition 8.2 gives the displayed balance conditions with the same hypotheses. | Verified (exact theorem-level support) |
| CIT-04 | `NicolussiGoloPinamontiWarhurst2026` | Official arXiv HTML lines 962--964 asks whether a complement can satisfy the vertical trace condition although no modularly balanced complement exists.  The manuscript's accepted theorem proves precisely this existence clause; it makes no claim about the question's second sentence. | Verified (exact source boundary plus accepted theorem) |
| CIT-05 | `NicolussiGoloPinamontiWarhurst2026` | Lemma 10.6, HTML lines 910--935, defines every graph complement as `q_Psi={Z-Psi Z}` and supplies the projected-trace transformation.  The manuscript uses its elementary codimension-one specialization and independently proves uniqueness by normalization of the nonzero `z` coordinate. | Verified (exact method locator) |
| CIT-06 | `MeurerEtAl2017` | The PeerJ Computer Science version of record and DOI `10.7717/peerj-cs.103` identify Meurer et al., *SymPy: Symbolic Computing in Python*, 3:e103 (2017); its abstract describes SymPy as an open-source computer-algebra system for symbolic computation.  `evidence/verify_witness.py` was inspected and rerun under SymPy 1.14.0, producing the exact traces and remainder recorded in the manuscript. | Verified (primary software source plus local execution) |
| CIT-07 | `ZengLiuRatnavelu2026` | The official Preprints.org version-1 full text for DOI `10.20944/preprints202608.1067.v1`, Section 2, equations (11)--(18), displays seven positive rational differences separating the attained ratio from the conjectured bound; its reproducibility statement says the certificate requires no numerical linear algebra.  The decimals are explicitly declared nonessential. | Verified (exact) |

Author, title, year, venue/version, pagination or article number, and persistent
identifier were checked for every retained entry.  The SymPy author metadata
was corrected to preserve the diacritics in Štěpán Roučka.  No citation key
changed.  No retained source contradicts or only partially supports its nearby
claim.

## Coverage and user-library gate

The primary source arXiv:2609.04299v1 supplies the problem origin, exact
definitions, closest results, complement graph chart, and open-question
boundary.  Fuglede and Ishihara are the natural primary historical sources.
The PeerJ article is the natural source for the symbolic-computation tool.
The proof itself is self-contained, so no classification theorem or external
Lie-algebra theorem is silently imported.

All 49 active first-sheet library records were screened through the checksum-
bound registry.  Row 2, *A Counterexample to the Tang–Zhang Schatten Norm
Conjecture and Sharp Positive Results*, is the single natural selection because
its exact rational separation certificate directly supports the modest method
comparison at manuscript lines 175--179.  The official Preprints.org full text
was inspected rather than relying on registry metadata.  Adding a second
library record would be padding: none of the other 48 entries concerns modular
balance or gives a closer source for the exact-arithmetic comparison.  The
attempt-bound selection and literal manuscript context are recorded in
`audit/user-bibliography-selection.json`.

The bibliography is not library-only.  Four non-library primary or method
sources occur naturally in ordinary body flow, so the selected library paper
does not substitute for the source question, closest results, classical
origin, or computational tool.

## Mechanical checks and sources

The bibliography checker reports five cited keys, five database keys, no
missing or unused entry, and exact agreement with `main.aux`.  The final
`main.log` and `main.blg` contain none of the requested undefined-citation,
undefined-reference, missing-database-entry, duplicate-entry, LaTeX-error, or
fatal-error patterns.

Primary records inspected:

- https://aif.centre-mersenne.org/articles/10.5802/aif.691/
- https://doi.org/10.1215/kjm/1250522428
- https://peerj.com/articles/cs-103/
- https://arxiv.org/abs/2609.04299v1 and https://arxiv.org/html/2609.04299v1
- https://www.preprints.org/manuscript/202608.1067 and https://arxiv.org/abs/2608.15558

No bibliography-revision handoff, release handoff, or saved Crossref capture
exists in this project.  On 2026-09-08 UTC, live academic-search templates were
freshly run for each source; the DOI/title/author/venue and, where applicable,
arXiv-ID queries gave consistent records.  The exact arXiv HTML passages at
Definition 8.2, equations (57)--(60), Theorem 10.5, Lemma 10.6, Theorem 10.7,
and Question 1 were replayed, as were the Preprints.org Section 2 rational
certificates and the PeerJ software record.  There are no unresolved citation
blockers.
