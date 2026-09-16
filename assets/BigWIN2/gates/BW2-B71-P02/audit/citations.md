# Citation and bibliography audit

## Scope and method

This release audit covers every ordinary body-flow citation in
`manuscript/main.tex`, the canonical `manuscript/references.bib`, the nearby
claims, source existence and metadata, exact supporting passages, bibliography
coverage, and final BibTeX/AUX/log consistency.  Claim extraction was frozen in
`audit/citation-claim-ledger.json`; source-passage verification then used that
fixed ten-claim ledger without adding or dropping claims.  The release job
explicitly prohibited subagents, so the fresh per-record checks were performed
serially in this release context.  This report is bound to citation attempt 2,
launch `c5178861-2c25-4376-abde-08b613edc5e6`, and release job
`win-00071-p02-release-3fccddad94e0`.  Verification date: 2026-09-08.

The ledger contains exactly the six active body-flow keys extracted from the
TeX: `Bott1957`, `HorvathKania2026`, `KlajaRansford2017`, `Laustsen1997`,
`Motakis2024`, and `Zeng2026Lens`.  There are no citation macros, `\nocite`
commands, hidden conditional citations, or cited keys supplied only by
comments.  The union of claim-level key lists is exactly this set.

## Claim-to-source verification

| Claims | Key | Primary record and locator | Nearby support | Status |
|---|---|---|---|---|
| CIT-01 | `Laustsen1997` | N. J. Laustsen, *K-theory for algebras of operators on Banach spaces*, arXiv:math/9701206v1, official abstract and paper introduction, submitted 23 January 1997, <https://arxiv.org/abs/math/9701206> | The paper explicitly studies and computes K-groups of algebras and ideals of operators on Banach spaces.  The manuscript now makes only the supported representative-context claim (“has also been studied; see, for example”). | Verified (paraphrase) |
| CIT-02 | `Motakis2024` | P. Motakis, *Separable Spaces of Continuous Functions as Calkin Algebras*, JAMS 37 (2024), 1–37, DOI 10.1090/jams/1024; official arXiv v2 abstract, <https://arxiv.org/abs/2110.10868> | The abstract states the quantified construction for every compact metric space and identifies the Calkin algebra with `C(K)`. | Verified (exact mathematical content) |
| CIT-03, CIT-05, CIT-07, CIT-08, CIT-09, CIT-10 | `HorvathKania2026` | B. Horváth and T. Kania, *Twisting exponential spectra*, arXiv:2609.05362v1, <https://arxiv.org/abs/2609.05362v1>; archived official PDF `evidence/external/2609.05362v1.pdf`, SHA-256 `5e8416e39b443dd1976edf7353f9d1652decac39873975328f00c42e53d99886` | Official metadata confirms title, authors, version, and 4 September 2026 date.  Theorem 4.1 gives the prescribed-family Motakis space and Schauder basis; Lemma 4.5 gives the matrix lifts; Theorem 5.1 constructs the fixed `S,T` and identifies the Calkin obstruction; Lemma 7.1 and Proposition 7.3 put the class in the first-stabilisation kernel; printed p.23 gives the `Z/2` Calkin component and its limitation upstairs; Question 9.1 on printed p.26 asks exactly for the kernel and order; printed p.2 records the stable-range/Bott calculation. | Verified (exact theorem/page support) |
| CIT-04 | `KlajaRansford2017` | H. Klaja and T. Ransford, *Non-commutativity of the exponential spectrum*, JFA 272 (2017), 4158–4164, DOI 10.1016/j.jfa.2017.02.017; author manuscript arXiv:1510.08109v2, <https://arxiv.org/abs/1510.08109> | The abstract and source theorem identify the noncommutativity example and its nontrivial `pi_4(GL_2(C))` obstruction.  Horváth–Kania printed p.2 explicitly identifies this as the obstruction lifted by their construction. | Verified (paraphrase) |
| CIT-06 | `Zeng2026Lens` | Z. Zeng, *Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds*, Preprints.org version 1, DOI 10.20944/preprints202608.1272.v1, <https://www.preprints.org/manuscript/202608.1272> | The official version-1 abstract and Section 2, Proposition 2, concern spectral-set constants, the sectorial numerical-range reduction, and exact results for restricted operator classes.  The manuscript expressly marks this as a distinct comparison and not a proof dependency. | Verified (paraphrase) |
| CIT-09 | `Bott1957` | R. Bott, *The Stable Homotopy of the Classical Groups*, PNAS 43(10) (1957), 933–935, DOI 10.1073/pnas.43.10.933; theorem on p.933, bibliographic record <https://pubmed.ncbi.nlm.nih.gov/16590113/> | Bott's theorem supplies the stable homotopy periodicity invoked in the displayed stable-range calculation.  Horváth–Kania printed p.2 applies that theorem to obtain the same vanishing, which independently fixes the precise local use. | Verified (exact theorem attribution) |

All title, author, year/version, venue, pagination, DOI/arXiv identifiers, and
URLs retained in `references.bib` agree with the inspected primary records.
No BibTeX replacement or citation-key change was needed.  The official
Horváth–Kania record still exposed version 1 at the checked URL.

## Coverage and relevance

The bibliography is not library-only or decorative.  It cites the problem
origin and closest prior result (`HorvathKania2026`), the underlying Calkin
construction (`Motakis2024`), the original topological obstruction
(`KlajaRansford2017`), the nontrivial topological method (`Bott1957`), and a
representative operator-K-theory source (`Laustsen1997`).  These five natural
non-library sources appear in ordinary body flow.  The one selected active
user-library record (`Zeng2026Lens`, registry row 13) supports a narrow,
explicitly separated operator-theoretic comparison; the other 48 active
records concern materially different problems and were not padded into the
bibliography.  The selection, literal citation context, exact runner attempt,
launch identity, and live registry digests are recorded in
`audit/user-bibliography-selection.json`.

The central Calkin-component lemma is proved self-containedly, so it does not
silently rely on an uncited external theorem.  Its applications and the
closest-prior/open-question comparison are sourced to the exact primary
locations.  No natural primary or method dependency used by the manuscript is
missing from the bibliography.

## Mechanical checks

The final clean `latexmk` run converged.  The bibliography checker reported six
cited keys, six BibTeX keys, zero missing files or keys, zero unused entries,
and exact agreement with the six AUX `\bibcite` keys.  The final `main.log` and
`main.blg` scan found no undefined citation/reference, missing database entry,
duplicate-entry, BibTeX warning, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.  Citation audit verdict:
**accept** (10/10 frozen claims verified; no numerical error, unsupported
strengthening, hallucination, or unresolved citation blocker).
