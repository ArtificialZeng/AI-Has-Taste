# Fresh citation and claim-support audit

## Scope and method

This release audit used the explicitly requested `citation-check-skill` as an
advisory two-pass check.  Pass 1 fixed all extracted claims in
`audit/citation-extraction.md` before any verification.  Pass 2 checked that
fixed list against the accepted mathematical snapshot, exact project evidence,
the complete authored dependency list, the rendered/extracted manuscript, and
the cited primary paper.  Search date: 2026-09-09 (Asia/Shanghai).

The complete publication dependency scope is exactly:

1. `manuscript/main.tex`
2. `manuscript/references.bib`

The recorder file confirms that there are no additional project-local TeX,
style, figure, or bibliography inputs.  System TeX packages are the only other
inputs.  Every `\cite` key in the TeX source is defined, the final `.bbl` and
PDF contain reference [1], and no unresolved citation marker appears in the
PDF.

`literature/user_bibliography_check.md` is absent.  I inspected that path and
do not interpret absence as evidence that a record is nonexistent.  The PDF
already includes the one genuinely relevant user-cited paper, Jiang and Yang,
and uses it only for definitions, development, the adjacent construction
range, and the explicitly stated ABAB limitation.  No second paper would
support a claim made here more directly.

## Bibliographic and passage verification

The BibTeX record gives Jianwei Jiang and Chunhua Yang, *Hamilton Starters and
Path Decompositions in Directed Circulants*, 2026,
`arXiv:2609.01256v1`.  This exactly matches:

- the official arXiv record, submitted 1 September 2026, with those authors,
  title, identifier, version, and math.CO classification; and
- the project-referenced 23-page local primary PDF at
  `/Users/mac/4prove-or-disprove-math/batches/literature/bigMac-25/2609.01256v1.pdf`,
  SHA-256
  `1ec8a1fc02a7736128e659f5ea152523a2aae73a2ff1ea621555e3b451e8b63c`.

All applicable citation-skill searches were run: author/year/title words, full
title restricted to arXiv or Semantic Scholar, author/year/venue, and arXiv
identifier.  No DOI query was applicable because the manuscript record does
not assert a DOI.  The official record is
<https://arxiv.org/abs/2609.01256>.

The original PDF supports the nearby prose as follows:

- Definition 2.1 (pp. 2--3) gives exactly the stated layer and balance
  definition and identifies a balanced Hamilton cycle as a balanced Hamilton
  starter.
- Proposition 2.2 and Lemma 2.3 (p. 3) identify the arc orbits and prove that
  the `r` translates by multiples of `q` partition all arcs into Hamilton
  cycles.  Specializing to `q=4,r=3` gives translates by `0,4,8`.
- Theorem 4.7 and its proof (pp. 8--9) give a four-layer starter when
  `r congruent to 1 (mod 4)` and `r >= 9`.
- Section 9 (p. 19) says that the ABAB mechanism fails for
  `r congruent to 3 (mod 4)` and expressly calls this a limitation of that
  construction, not a general existence obstruction.

The manuscript therefore neither overstates the cited paper nor attributes
the new finite obstruction to it.  Its wording "closest inspected
construction" is bounded, and it expressly disclaims literature priority.

## Fixed-list verification results (pass 2)

| Claims | Status | Primary support |
|---|---|---|
| C01, C05, C06 | Verified (exact) | Accepted `claim.json` scope and `audit/math.md`; fresh exact replays also return zero Hamilton cycles. |
| C02, C13 | Verified (paraphrase/exact specialization) | Jiang--Yang Definition 2.1 and Proposition 2.2; `problem.md`; orbit proof in Lemma 3. |
| C03, C04, C14, C15, C17--C20 | Verified (exact) | Fresh runs of `evidence/crosscheck.py` and `audit/referee_recompute.py`: 531441, 1296, 15, histogram `6+6:12`, `4+8:3`, and zero Hamilton cycles; survivor digest `b36456535b5da51566823d0c7781e5d398dd6beb8a4f85ce21a347d181a6f77b`. |
| C07, C08 | Verified (paraphrase) | Jiang--Yang Definition 2.1, pp. 2--3. |
| C09 | Verified (paraphrase) | Jiang--Yang Proposition 2.2 and Lemma 2.3, p. 3. |
| C10 | Verified (paraphrase) | Jiang--Yang Theorem 4.7, pp. 8--9; official abstract. |
| C11 | Verified (paraphrase) | Jiang--Yang Section 9, p. 19. |
| C12 | Verified as a scope disclaimer | No priority assertion occurs in the TeX or extracted PDF. |
| C16 | Verified (exact elementary criterion) | Lemma 4 proof; twelve distinct images make a permutation, whose Hamiltonicity is exactly one 12-cycle. |
| C21 | Verified (exact) | Required interpreter reports `Python 3.12.14`; fresh evidence runs used that executable. |
| C22 | Verified (exact) | All 15 printed rows agree with the canonical degree-survivor set and stated histogram; the accepted referee independently recomputed the same digest. |
| C23 | Verified as a process disclosure | The manuscript and job/evidence history accurately disclose AI-assisted design, implementation, checking, and preparation; no claim of autonomous proof is made. |

There are no numerical errors, contradicted attributions, unsupported novelty
claims, misleading citations, or unverified references in the fixed list.  The
mathematical conclusion remains bounded to the accepted `q=4,r=3` claim.

**Verdict: accept.**

