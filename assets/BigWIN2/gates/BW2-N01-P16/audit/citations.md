# Verification Report

**Verdict: accept.** Search verification with a frozen, non-interactive extraction
followed by a separate claim-by-claim source-support pass. Job:
`newwin-00001-p16-release-699cf5c87937`; citation attempt 1; launch
`8ef96029-3d83-44c7-b577-288f686f0cac`. Verified on 2026-09-12 UTC.

| Metric | Count |
|---|---:|
| Extracted substantive claims or certificate blocks | 27 |
| Claims verified in their stated scope | 27 |
| Distinct cited works | 5 |
| Gate-selected library works | 1 |
| Ordinary non-library primary works | 4 |
| Numerical errors, unsupported claims, misleading citations | 0 |
| Undefined, missing or unused bibliography keys | 0 |

The final claims are in `audit/citation-claim-ledger.json`; their extraction-only
copy is `audit/citation-extraction-final.json`. Verification decisions and exact
source locators are in `audit/citation-verification.json` and
`audit/source-locations.json`. Definitions and process disclosures were not
treated as external research results; the assertion about perfect numbers was
separately extracted as C27. Original mathematical claims were compared with the
accepted mathematical audit and the displayed proof. This release pass does not
replace that mathematical review or claim journal peer review.

## Primary-source findings and bibliography coverage

| Key | Verified nearby claim and source location | Why retain it |
|---|---|---|
| `Zelinsky2026` | [Publisher paper](https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.pdf), Conjecture 1 and Theorem 2, p. 2; Lemma 4, p. 4; product-loss step in the proof of Lemma 9, pp. 6–7. The frozen primary PDF/text and live publisher record agree. | Problem origin, closest inspected three/four-prime result, the general bound, and an already-used elementary method. |
| `Dickson1913` | [Original journal record](https://www.jstor.org/stable/2370405) confirms the 1913 article; its author's contemporaneous announcement in Bulletin AMS 19(6), p. 285, is reproduced in [Celebratio, entry 218](https://celebratio.org/Dickson_LE/article/79/), lines 5366–5374. It explicitly gives finiteness for odd primitive non-deficient integers at fixed number of distinct prime factors. | Historical finiteness context at fixed radical size. This attribution uses the original author's announcement, not the title alone. |
| `Cohen1983` | [Publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C3E55991ACF52C8895A6AAD10D934CE0/S1446788700019819a.pdf/on-primitive-abundant-numbers.pdf), Lemma 1 and Theorem 1, printed p. 124; Remark 1, p. 125. These discuss abundancy under divisibility and primitivity in relation to divisor-sum excess and components. | Prior component/primitivity work and the natural context for a prime-quotient argument. The manuscript does not quote an OCR-derived formula from this paper. |
| `AmatoEtAl2019` | [Published record and abstract](https://www.sciencedirect.com/science/article/pii/S0022314X19301039), [author-deposited arXiv v2](https://arxiv.org/pdf/1802.07178), abstract p. 1 and Section 3, p. 6 onward. The enumeration fixes the number of prime factors counted with multiplicity. The inspected [author copy](https://www.sci.unich.it/~amato/papers/jnt2019.pdf) also discusses this in Section 3. | Closely related arithmetic enumeration, with an explicit distinction between fixed total multiplicity and the unbounded exponents here. |
| `ZengEtAl2026` | [Version 1 primary full text](https://www.preprints.org/manuscript/202608.1658/v1), Section 3, paragraphs after Lemma 2, especially HTML lines 155–157; Section 6 confirms the same separation. A verifier reconstructs configuration coverage and checks stored colorings. The [publisher's subject listing](https://www.preprints.org/subject/browse/computer-science-and-mathematics/computational-mathematics), lines 142–167, binds the matching title, four authors, posting date and DOI. | A concrete methodological comparison for separating exhaustive coverage from witness checks. It is used only in the verification paragraph, not as a number-theoretic predecessor or proof of a geometric result. |

All five retained entries match the authoritative title, authors, year, venue,
pages or version, and DOI where present. Cohen's print date is 1983, distinct
from its 2009 online digitization date. Amato's journal date is 2019, distinct
from its 2018 arXiv version. Zeng et al. is explicitly a preprint, version 1,
posted 24 August 2026. No bibliography entry or key was replaced. Official
BibTeX-export requests did not return usable blocks, so no purported official
BibTeX was manufactured; the existing entries were retained after field-level
verification. `audit/sources/retrieval-log.json` records local request failures.

The normal bibliography is not library-only: four body-flow non-library primary
references supply the problem, predecessor, historical, and enumeration context.
Every retained reference has the substantive use shown above. The prime-power
formula, product inequality, factor identity, trial-division criterion and search
cutoffs are explained or proved in the note; no unmentioned nontrivial theorem
or software package supplies the finite certificate. There is no reference quota
and no gratuitous extra source.

## Library and attempt integrity

The active registry and manifest were read; all 49 first-sheet titles were
screened. None directly concerns primitive non-deficient numbers. Row 9 has the
specific verified methodological use above. One such comparison suffices; a
second library citation would not supply another needed step. Its exact title,
source key `202608.1658`, DOI, row identity and dynamic workbook/registry hashes
are bound in `audit/user-bibliography-selection.json`. The selected final key is
`ZengEtAl2026`; its direct ordinary citation appears at main.tex lines 261–264.
The context is the smallest citation-bearing sentence and excludes equation or
label commands. `verified_at` was obtained with `date -u +%F`.

The installed `bigwin_user_bibliography.validate_selection` passed against the
exact runner-issued attempt and launch; see `audit/selection-validation.json`.
The union of the ledger's direct keys is exactly the five active body keys.
There are no citations supplied only by comments, inert macros, hidden
conditionals, verbatim text or nocite. The configured pre-publication hook was
not invoked. No agents or other model processes were used, because the user
explicitly prohibited them; the same source-verification protocol was applied
locally and non-interactively.

## Source access and novelty limits

The required bibliography-revision, handoff and Crossref globs were enumerated
before editing. There were no revision files or saved Crossref captures. The sole
intake handoff's immutable-source and primary-file hash predicates hold. Its
historical spreadsheet/conversation comparison was not adopted. No fast-completion
handoff existed.

All applicable author/year/title, title/database, author/year/venue, DOI and
arXiv-ID search templates were run. Exact DOI searches and fresh five-prime
component searches supplemented them. Queries and source responses are retained
under `audit/sources/`. Some results were irrelevant, and the indexed old arXiv
summary of Zelinsky's conjecture still used the obsolete R bound; the current
publisher's 2R statement controls. No inspected primary source provided a covering
five-prime result. This supports only the manuscript's bounded statement about
the sources inspected through 12 September 2026, not exhaustive priority.

The local network denied direct downloads and Crossref exports, while the web
tool supplied the primary publisher/author texts. The Dickson journal scan and
AMS announcement PDF did not load. His exact contemporaneous announcement was
instead read in its attributed Celebratio reproduction, with the full article's
identity independently checked at JSTOR. The manuscript uses only the announced
finiteness statement; no claim about Dickson's proof was verified or imported.
Cohen's PDF text was inspected, but a requested screenshot did not yield a usable
image; no source-page visual review is claimed. These access limits do not erase
the actual inspected support and are not mathematical results.

## Scope, numerical evidence and build

Theorem 1 has exactly five distinct odd prime factors, arbitrary positive
exponents, and includes sigma(n)=2n. There is no added claim for six primes, a
stronger R bound, or an exhaustive historical search. All 16 protected input
hashes, including every file in the accepted snapshot and checkpoint.md, remain
unchanged.

The canonical parser initially rejected the two external input commands. The
tables were inlined without changing any mathematical entry, and their two
length assignments were replaced by standard longtable centering. The selected
optional citation note was moved after the direct citation. No mathematical
repair or bibliography rewrite occurred. `audit/release-check.py` verifies the
exact inlining, all thirteen factor rows, all 95 small divisors, the six ordered
pairs and their compositeness factors, all displayed cutoff products, and the
937-value direct cross-check. The public-source claims were verified separately
from these internal numerical checks.

A clean pdfLaTeX/BibTeX build converged successfully. The final TeX and BibTeX logs
contain no undefined citations/references, warnings, or over/underfull boxes.
The BibTeX key checker found five cited keys, five database keys and five aux
entries, with no missing or unused entries. The recorder confirms the complete
local publication inputs: main.tex, references.bib and build/main.bbl. All five
rendered pages were actually inspected; the separate build and visual reports
bind to the same current manuscript/PDF snapshot.
