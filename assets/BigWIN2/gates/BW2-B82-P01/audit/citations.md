# Citation and bibliography audit

Release job: `win-00082-p01-release-b749192a753f`  
Citation attempt: `3`  
Launch: `0ede2023-8f2b-4b61-a904-e2b05518a3c4`  
Checked in UTC: `2026-09-09`

## Frozen extraction (pass 1)

The complete canonical `manuscript/main.tex` was read before source
adjudication.  The extraction frozen in `audit/citation-claim-ledger.json`
contains six uniquely identified citation-bearing claims.  Its key union is
exactly the five ordinary body-flow keys extracted from the manuscript:
`coven1999`, `gregor2024`, `hiltgen1996`, `zeng2026rainbow`, and `zhou2026`.
Comments, `\nocite`, verbatim material, macro definitions, and hidden
conditionals supply no key.  `manuscript/references.bib` is the sole active
bibliography.

## Independent verification (pass 2)

Pass 2 used the frozen claim list without re-extraction.  Exact source
locations and URLs are recorded in
`audit/citation-source-verification.json`.

| Claim | Key | Primary passage checked | Result |
|---|---|---|---|
| CIT-01 | `hiltgen1996` | The indexed original abstract says the class is introduced; the DOI/institutional record fixes the publication, and Schwartz--Etzion's later IEEE article gives the cyclic-column-shift plus adjacent-row definition and attributes it to Hiltgen et al. | Verified (paraphrase) |
| CIT-02 | `gregor2024` | Springer version of record, Theorem 4.5 and proof: coprime `n,k`, an `n`-symmetric one-track balanced Hamilton cycle in `J_{n,k}`, with the columns cyclic shifts. | Verified (exact) |
| CIT-03 | `zhou2026` | Local unchanged arXiv v1, Definition 1.1 (p. 1), independent-shift clarification and complement symmetry (p. 2), Theorems 1.3--1.4 (p. 2), higher-uniformity open statement (p. 3), and Conjecture 7.1 (p. 9). | Verified (source facts exact; first-case statement is a direct finite inference) |
| CIT-04 | `zhou2026` | Local arXiv v1, Lemma 2.2 (p. 3), compared hypothesis-by-hypothesis with the manuscript's reproduced coordinate-count lemma. | Verified (exact) |
| CIT-05 | `zeng2026rainbow` | SSRN 7387259 record/PDF abstract: subgroup-coset extensions and quotient-fiber composition over finite abelian groups. | Verified (paraphrase; analogy only) |
| CIT-06 | `coven1999` | Elsevier/arXiv abstract and opening definition: structural study of tiling the integers by disjoint translates of one finite set. | Verified (paraphrase; background only) |

No numerical mismatch, contradiction, omitted source hypothesis, decorative
use, or unsupported strengthening was found.  The paper's theorem remains
bound to the accepted mathematical audit; citation verification is not being
used as proof.

## Bibliographic identity and coverage

All five entries were checked against primary publication records or the
authoritative preprint record.  Author, title, year/version, venue, pages,
DOI/arXiv identifier, and the nearby use agree.  There are five cited keys,
five unique BibTeX entries, no missing entry, no uncited entry, and all five
keys occur in the converged AUX file.  No key or BibTeX replacement was
needed.  The active registry's source export labels the SSRN item as an
`@article`; the canonical bibliography's `@misc` classification more
accurately describes the same SSRN preprint, without changing any identity
field or DOI.

Coverage is complete for the manuscript's actual dependencies: Zhou is the
problem-origin and closest-result source; Gregor--Merino--Mütze supports the
stronger adjacency comparison; Hiltgen--Paterson--Brandestini supports the
terminology; Coven--Meyerowitz supplies the explicitly limited tiling
context; and Zeng is the single genuinely relevant active user-library item,
used only for the stated coset/fiber analogy.  The finite two-point tiling
classification, coordinate calculation, and exact enumeration are proved or
described self-containedly and do not silently rely on an uncited theorem.
Four natural non-library sources occur in ordinary body flow, so the
bibliography is neither library-only nor padded.

The 49-record active first-sheet registry was screened by title and abstract.
Row 36 is the only natural library match.  Its live registry/workbook hashes,
row metadata, direct body citation, compact literal citation context, and UTC
verification date are bound in `audit/user-bibliography-selection.json`.

## Mechanical checks

The bibliography checker reported five cited keys, five BibTeX keys, zero
missing bibliography files, zero missing cited keys, zero uncited entries,
and exact AUX agreement.  Scans of `manuscript/main.log`,
`manuscript/main.blg`, and `audit/build.log` found no undefined citation,
undefined reference, missing database entry, repeated entry, LaTeX error,
fatal error, emergency stop, undefined control sequence, or runaway argument.

Overall status: **PASS** (6/6 frozen claims verified; 0 numerical errors, 0
hallucinations, 0 misleading claims, 0 unverified claims).
