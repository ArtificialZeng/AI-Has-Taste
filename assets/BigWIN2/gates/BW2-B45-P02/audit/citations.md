# Citation and bibliography release audit

Verdict: **accept**. Search date: 2026-09-06. The reviewed manuscript is
`manuscript/main.tex`; its canonical bibliography is
`manuscript/references.bib`.

## Method and frozen extraction

Pass 1 read the complete TeX source and PDF and froze twelve checkable claims
in `audit/claim-ledger.json` and `audit/claim-ledger.md` before any claim was
verified. Pass 2 used that fixed list only. The audit was non-interactive as
required by the runner. The bibliography skill's normal subagent delegation was
not used because the job explicitly prohibited agents; each of the four keys was
instead checked serially under the same source protocol.

The applicable author/title/year, full-title, author/venue, DOI, and arXiv-ID
search templates were run. Primary hosts were used: arXiv and the supplied
source PDF, Annals of Mathematics, Elsevier's article record, and Preprints.org.
The project contains no `literature/bibliography-revision-*.md` or
`literature/crossref-*.json`/`.md` captures. No source-access failure was treated
as evidence for a mathematical or bibliographic conclusion.

## Frozen claim verification

| ID | Status | Confidence | Verification and exact source location |
|---|---|---|---|
| C01 | Verified | exact | `audit/math.md`, reconstruction and verdict; the proof in `main.tex:92-186`. |
| C02 | Verified | paraphrase | Vishnyakova, arXiv:2608.03723v1, Definition 1.4 (printed p. 5) defines exactly the displayed linear map; the arXiv record confirms author, title, version, and date. |
| C03 | Verified | paraphrase | Official Annals abstract states that Borcea--Branden characterize linear operators on polynomial spaces preserving zero-location properties, including the real line; pp. 465-492, vol. 170(1), DOI 10.4007/annals.2009.170.465. |
| C04 | Verified | exact | Vishnyakova Definition 1.4 gives the transform; Open Problem 1.9 (printed p. 7) asks the all-$a$ product-closure question verbatim in the relevant notation. |
| C05 | Verified | exact | Vishnyakova Theorem D (printed p. 7) states closure for $L_1$ and attributes it to D. G. Wagner [14]; her bibliography identifies Wagner's 1992 JMAA paper and DOI. Elsevier's primary record independently confirms author, title, journal, date, volume, issue, pages, DOI, and the polynomially interpolated totally-positive Toeplitz Hadamard-product result. |
| C06 | Verified | exact | The accepted theorem quantifies one transformed degree-one factor and arbitrary finite $n$; no statement in the manuscript claims closure when both degrees are at least two. |
| C07 | Verified | paraphrase | Official Preprints.org v1 abstract states exact rational matrix certificates and treatment of a palindromic quadratic family; Theorems 2-7 and Section 12 exhibit restricted quadratic spectral-set families and exact certificates. |
| C08 | Verified | exact | `audit/math.md` independently reconstructs the full theorem and accepts the precise all-$n$ scope. |
| C09 | Verified | exact | `source.md` itself designates degree $(1,2)$ as the first nontrivial low-degree case; $n=2$ is the theorem's immediate specialization. |
| C10 | Verified | exact | `audit/math.md` recomputes the basis identity, partial fractions, residue signs, exterior roots, and compact limit; `evidence/research_check.py` was rerun successfully as a transcription check. |
| C11 | Verified | exact | The exact cubic agrees term-by-term with frozen `source.md`; `evidence/research_check.py` reproduced it symbolically. |
| C12 | Verified | exact | The accepted compact-limit argument covers $r=0,1$, repeated roots, and roots at both endpoints without degree loss, for each arbitrary fixed $a>0$. |

Counts: 12 claims verified; 0 numerical errors; 0 hallucinations; 0
misleading claims; 0 unverified claims.

## Per-key bibliographic audit

| Key | Current/official title | Primary record and claim support | Action | Uncertainty |
|---|---|---|---|---|
| `BorceaBranden2009` | *Pólya--Schur Master Theorems for Circular Domains and Their Boundaries* | https://annals.math.princeton.edu/2009/170-1/p14, abstract and metadata | Retained; author, title, 2009, volume 170(1), pp. 465-492 and DOI match. | none |
| `Vishnyakova2026` | *Polynomially Deformed Normalized Pochhammer Sequences Having Generating Functions With Only Real Non-positive Zeros* | https://arxiv.org/abs/2608.03723 and supplied SHA-256-identified v1 PDF, Definition 1.4, Theorem D, Open Problem 1.9 | Retained; author, title, year, arXiv ID, class and DataCite DOI match. | preprint, v1; correctly labelled as such |
| `Wagner1992` | *Total Positivity of Hadamard Products* | https://www.sciencedirect.com/science/article/pii/0022247X9290261B, official abstract/metadata; exact $L_1$ formulation cross-checked at Vishnyakova Theorem D | Retained; author, title, journal, 1992, volume 163(2), pp. 459-483 and DOI match. | none |
| `Zeng2026Lens` | *Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds* | https://www.preprints.org/manuscript/202608.1272, v1 abstract, Theorems 2-7 and Section 12 | Retained; final key differs intentionally from registry key `202608.1272`; author, title, host, year and DOI match. | non-peer-reviewed preprint; manuscript uses it only as a methodological example |

No BibTeX replacement or cite-key edit was needed. Mechanical checks found four
cited keys, four canonical entries, no missing or unused entries, and exact
agreement between TeX and AUX citation sets.

## Coverage and relevance

The bibliography is not user-library-only. Vishnyakova is the primary problem
source and nearest stated baseline; Wagner is the original $a=1$ result;
Borcea--Branden is a primary structural reference for zero-preserving linear
operators. The proof itself is elementary and self-contained, so it does not
depend on an uncited nontrivial theorem or computational-proof technique.

The active 49-entry user library was checksum-bound and screened. Row 13 is the
only close entry: it directly supports the nearby claim about exact certificates
for restricted quadratic spectral-set operator families. Its ordinary body-flow
`\cite{Zeng2026Lens}` occurs at `main.tex:68`, and the DOI is in the canonical
bibliography. Adding a second library item would be decorative. The exact
selection and attempt identity are recorded in
`audit/user-bibliography-selection.json`.

Overall status: **PASS**. All retained citations exist, match their bibliography
records, support their nearby claims, and form a natural non-padded coverage set.
