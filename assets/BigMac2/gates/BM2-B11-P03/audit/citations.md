# Verification Report

**Mode:** Search verification (citation-check-skill, two-pass)
**Document:** `manuscript/main.tex`, `manuscript/references.bib`, and the
three-page rendered `manuscript/main.pdf`
**Checked:** 2026-09-07

## Pass 1: fixed claim extraction

The complete manuscript was read before verification.  The following claims
meet the skill's extraction rules; definitions and the assistance-methodology
paragraph were excluded by those rules.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | The 2026 ECA paper records the molecular-species double-coset decomposition for products `X^n/H`. | Attribution/existence | p. 1, first paragraph |
| C02 | arXiv:2609.05010v1 distinguishes the independent-row `K_alpha` family, asks for its product coefficients, and says the full subgroup lattice replaces the cyclic divisor lattice. | Attribution/existence | p. 1, first paragraph |
| C03 | The earlier paper's related convention differs when equal parts repeat. | Comparative | p. 1, convention paragraph |
| C04 | `H=< (12),(34) >` has the four displayed elements and is isomorphic to `C_2^2`. | Existence/statistic | pp. 1-2 |
| C05 | `K_(2,2) x K_(2,2)` is the disjoint union of two `K_(2,2)` terms and `K_(1,1,1,1)`, with coefficient vector `(0,0,2,0,1)`. | Existence/statistic | abstract and Theorem 1 |
| C06 | The five species, and separately their five cycle indices, have no nonzero integral relation. | Existence | Theorem 1 |
| C07 | The normalizer of `H` is the displayed two-block stabilizer and has order 8. | Existence/statistic | p. 2 |
| C08 | The normalizer consists of two four-element double cosets, each with intersection stabilizer `H`. | Existence/statistic | p. 2 |
| C09 | For `r=(23)`, the displayed conjugate intersects `H` trivially and `HrH` has 16 elements. | Existence/statistic | p. 2 |
| C10 | The three displayed double cosets exhaust `S_4` and yield stabilizers `H,1,H`. | Existence/statistic | p. 2 |
| C11 | The five displayed stabilizers are pairwise nonconjugate. | Existence | p. 2 table and following paragraph |
| C12 | The displayed cycle-index coefficient matrix has determinant exactly `1/24`. | Statistic | p. 3 |
| C13 | The displayed `Z_H` formula and exact internal-product identity hold. | Existence/statistic | p. 3 |
| C14 | The two bibliography records have the stated authors, titles, dates/versions, journal data, article number, and DOI/arXiv identifier. | Attribution/temporal/existence | p. 3 references |

This extraction was fixed before the checks below; no claims were added during
verification.

## Pass 2: verification

| ID | Status | Source and check | Confidence |
|---|---|---|---|
| C01 | Verified | Primary full text of arXiv:2604.10336v1, Proposition 2.2(2), gives exactly the `H\\S_n/K` decomposition with intersection subgroup; the official ECA volume listing confirms publication as 6(3), S2R19. | paraphrase |
| C02 | Verified | Primary full text of arXiv:2609.05010v1, Remark 3.2 and Open Problem 5.1, explicitly defines `K_alpha=X^n/G_alpha`, independent row shifts, and subgroup-lattice inversion. | paraphrase |
| C03 | Verified | Definition 3.3 of arXiv:2604.10336v1 groups equal-length cycles diagonally (so repeated 2-parts use the cyclic generator `(12)(34)`), whereas arXiv:2609.05010v1 Remark 3.2 defines the independent-row companion. | paraphrase |
| C04-C13 | Verified | They reproduce the accepted frozen statement and its proof without strengthening.  `audit/math.md` independently reconstructs the group argument and exact cycle-index calculation.  A fresh run of `evidence/s4_certificate.py` produced a byte-identical certificate (SHA-256 `49c3629f84c0369b1ebdf469fca48d2277201f9f2aecd0a3c717fa5a57ec7f8b`).  Every integer and rational value matches exactly. | exact |
| C14 | Verified, with provenance limitation | arXiv records confirm both preprints' author/title/version metadata; the official ECA volume listing confirms 6(3), Article S2R19 and DOI `10.54550/ECA2026V6S3R19`.  The cited theorem/remark/open-problem text was inspected directly. | exact |

Applicable academic-citation query templates were run for each title, first
author/year/title prefix, venue, DOI, and arXiv identifier.  Primary records
consulted were:

- <https://arxiv.org/abs/2609.05010> and
  <https://arxiv.org/html/2609.05010v1>;
- <https://arxiv.org/abs/2604.10336> and
  <https://arxiv.org/html/2604.10336v1>;
- <https://ecajournal.haifa.ac.il/Volumes.html> and DOI
  <https://doi.org/10.54550/ECA2026V6S3R19>.

Both citations are necessary and support only the nearby contextual claims.
There is no novelty or priority claim.  Citation keys `[1]` and `[2]` resolve
in the extracted PDF and the final bibliography matches the database.

## Dependency and limitation audit

`publication.json` lists `manuscript/main.tex` and
`manuscript/references.bib`.  Inspection of the TeX and recorder file found no
authored `input`, included figure, local style, or other local source
dependency.  The list is complete.

The required `literature/user_bibliography_check.md` is absent.  The two cited
papers are genuinely relevant and their metadata and claim-level support are
verified above, but this release context cannot verify that either record came
from the user's cited Excel list.  This is a bounded source-provenance access
limitation only; it is not an unsupported citation or mathematical claim.

## Summary

All 14 extracted claim groups are verified, with no numerical error,
contradiction, undefined citation, unsupported strengthening, or hallucinated
reference.  Verdict: **accept with the disclosed citation-provenance
limitation**.
