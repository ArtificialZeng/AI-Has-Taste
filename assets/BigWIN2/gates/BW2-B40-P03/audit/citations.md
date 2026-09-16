# Citation and claim audit

**Mode:** search verification, with accepted frozen evidence for the paper's new
mathematics  
**Document:** `manuscript/main.tex` and the four-page `manuscript/main.pdf`  
**Search date:** 2026-09-06  
**Method:** citation-check-skill two-pass review, performed serially because the
job explicitly prohibited subagents

## Pass 1: fixed claim extraction

Extraction was completed before source verification. Definitions, proof-step
descriptions, hypotheticals, and the assistance disclosure were excluded under
the skill's extraction rules.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | The dimension-four Hypercube inequality has sixteen nonnegative weights, degree eight, and is unresolved on the full orthant. | statistic, existence | abstract; lines 29--31; 65--66 |
| C02 | The inequality holds when the weights take at most two values. | existence | abstract; Theorem 1 |
| C03 | All nine coefficients are nonnegative for each of 32767 canonical bipartitions. | statistic | abstract; Proposition 2 |
| C04 | Any strict counterexample must use at least three distinct weights. | causal consequence | abstract; lines 183--185 |
| C05 | Averkov--von Dichter--Soprunov introduced the formulation, proved the preceding d=3 case, and left d at least 4 unresolved. | attribution | lines 68--70 |
| C06 | The d=2 square identity used in that induction appeared in the earlier Averkov--Soprunov proof. | attribution | lines 70--73 |
| C07 | The two-entry auxiliary-row reduction in the source is different from two-valued final vertex weights. | comparative attribution | lines 73--76 |
| C08 | The literature comparison is limited and makes no priority claim. | scope statement | lines 78--79 |
| C09 | Direct substitution gives equations (1)--(3) and an integer bivariate expansion. | existence | lines 88--118 |
| C10 | Coefficientwise nonnegativity is sufficient on each two-parameter cone. | causal | lines 119--120 |
| C11 | Every canonical nonempty U omitting (1,1,1,1) has nine nonnegative coefficients. | existence | Proposition 2 |
| C12 | The certificate uses exact integer arithmetic and enumerates 4368 five-subsets. | statistic | lines 127--131 |
| C13 | The normalized-volume counts are 1360, 2672, 320, and 16 for volumes 0, 1, 2, and 3. | statistic | lines 132--136 |
| C14 | 294903 coefficients were tested; 0 were negative, 2040 were zero, and the least positive value was 1. | statistic | lines 138--146 |
| C15 | The weighted volume sum is 3360 and the all-ones invariant is 3014656. | statistic | lines 148--153 |
| C16 | The calculation is exhaustive integer computation, not floating-point search. | comparative | lines 154--161 |
| C17 | Complement pairing covers every exactly-two-valued assignment. | existence | lines 164--171 |
| C18 | Setting a=b covers constant assignments. | existence | lines 173--175 |
| C19 | The proof does not claim coefficientwise positivity in sixteen variables and leaves three-or-more-valued weights untreated. | scope statement | lines 180--185 |
| C20 | A separate exact implementation reproduced the output using a different ordering, determinant algorithm, and facet expansion. | attribution | lines 187--192 |
| C21 | Zeng--Liu--Ratnavelu--Ong use an integer compatibility predicate, exhaustive finite computation, and an independently reconstructed implementation. | attribution | lines 194--198 |
| C22 | That cited work treats different finite models and does not address the Hypercube inequality. | comparative scope | lines 198--200 |

## Pass 2: verification

| ID(s) | Status | Evidence and exact support |
|---|---|---|
| C01, C05 | Verified (paraphrase) | Averkov--von Dichter--Soprunov, arXiv:2608.14909v1, eq. (2), Theorem 5.1, Section 6, and Section 7.5. The primary text defines the d-dimensional formula, proves d=3, and says d at least 4 remains open. |
| C06 | Verified (paraphrase) | Averkov--Soprunov, Springer version, Remark 7 and the reduction ending in the nonnegative square; the later arXiv source explicitly identifies this as the earlier d=2 identity used in its Section 6 induction. |
| C07 | Verified (paraphrase) | arXiv:2608.14909v1, Section 4.2 reduces auxiliary matrix rows to entries in {0,1}; the variables x remain the grouped final weights in Section 4.4, so the manuscript's distinction is accurate. |
| C08, C19, C22 | Verified (exact scope) | These are conservative limitations. The accepted mathematical audit leaves the unrestricted problem unresolved, and the inspected Preprints.org work is about ternary Borsuk and kissing-code finite models rather than the Hypercube polynomial. |
| C02--C04, C09--C18, C20 | Verified (exact/recomputed) | Frozen claim and accepted report `audit/math.md`; `evidence/two_level_certificate.py` rerun on 2026-09-06 reproduced all stated counts and digest `cd479d1e958d79bcd9580697f4c4fa2a932f18448174226026ecdeffcfdbbd19`. C20 is also explicitly documented in the accepted referee reconstruction. |
| C21 | Verified (paraphrase) | Zeng--Liu--Ratnavelu--Ong, Preprints.org v1, Section 4, Lemma 3 and Proposition 1: integer compatibility, exhaustive exact clique search, and a separate list-based implementation reconstructing the graph. |

No numerical errors, hallucinations, misleading claims, or unverified extracted
claims remain. The full d=4 statement remains unresolved exactly as stated.

## Claim-to-source and bibliography audit

| Key | Current and official title | Primary source | Nearby claim supported | Action |
|---|---|---|---|---|
| `AverkovVonDichterSoprunov2026` | *On the Log-Submodularity for Zonoids: From Mixed Volume Inequalities to the Hypercube* | https://arxiv.org/html/2608.14909v1 | Formula, d=3 result, Section 4.2 distinction, d=4 open status | Metadata and scope verified; retained |
| `AverkovSoprunov2026` | *An Algebraic-Combinatorial Proof of a Bézout-Type Inequality for Mixed Volumes of Three-Dimensional Zonoids* | https://doi.org/10.1007/s00454-025-00745-2 | Earlier algebraic-combinatorial square reduction underlying the d=2 identity | Metadata, issue year, pages, DOI, and scope verified; retained |
| `202608.1658` | *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes* | https://www.preprints.org/manuscript/202608.1658 | Narrow finite-certificate methodology comparison only | Official registry BibTeX copied without field edits; direct body citation added; limitation stated |

The two domain-primary sources cover the problem's origin, nearest established
dimension, open status, and the only cited nontrivial precursor method. The one
user-library source is additional and method-specific, not a substitute for
domain literature. No decorative or unused bibliography entry remains.

Live shell content negotiation was unavailable at the WSL network boundary.
Before drawing any availability conclusion, all `literature/crossref-*.json`
and `literature/crossref-*.md` paths were enumerated; none exist for this
project. Verification instead succeeded against the three primary public pages
above. The two existing domain entries agree in author, title, venue/version,
year, pages where applicable, and DOI/identifier with those official records.

## Mechanical consistency

The canonical bibliography is `manuscript/references.bib`. There are three
distinct cited keys, three bibliography entries, no missing or unused key, and
the converged AUX file contains exactly the same keys. No custom or indirect
citation macro was found. The rendered PDF contains all three reference entries.
