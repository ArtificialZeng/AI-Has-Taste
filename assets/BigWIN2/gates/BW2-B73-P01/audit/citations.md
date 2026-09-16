# Citation and bibliography audit

## Scope and two-stage method

This is the verification-only pass for release job
win-00073-p01-release-01fed9f3c856, citation attempt 5, launch
e477c158-be49-4389-99b4-b4f1bd9260d5. The six claim/citation pairs were first
frozen without verdicts in audit/citation-claim-ledger.json; verification then
proceeded sequentially against primary or authoritative records on 2026-09-08
UTC (2026-09-09 in the project timezone).
The user prohibited sub-agents, so no delegated citation checks were used. The
audit is bound to accepted mathematical snapshot
d45fcb7c5650dd0813cf983a7a09999aa5cb3852cd9f976ff3d0de93e478e261,
manuscript digest
eefbb5faf2ae39e4b61b7433540b0bebb3969dfe3483cffb1df0ddc8fdc0b471,
and PDF digest
aad4cb571a7d5e63278d7c9102f318db6a6384d6b685ce5c6724a61426bcf23d.

## Claim-to-source verification

| Claim | Key(s) | Exact source location inspected | Status |
|---|---|---|---|
| C01 | SpectorStockdale | Primary arXiv v1 HTML, equation (1.10) at lines 134--138 and equation (1.11) at lines 138--143: definition of $A_s$, its $N$-fold power, and the same exterior square function. | Verified (exact) |
| C02 | SpectorStockdale | Primary arXiv v1 HTML, definition of the comparison notation at line 48 and Theorem 1.3 at lines 163--173: the hidden constant is dimension-free, and the theorem has dimension at least three, a finite positive atomic measure, cap-kappa partial balayage, and the stated square-root-$N$ bound. This directly supports the parser-safe form with an absolute constant $C$. | Verified (exact paraphrase) |
| C03 | GustafssonSakai | Elsevier's authoritative article record confirms the 1994 title, authors, journal, volume 22(10), pages 1221--1245, and DOI. The authors' later open primary exposition, Section 5, explicitly describes partial balayage to a prescribed density, its density bound, and the equivalent obstacle problem while identifying the 1994 paper as the foundational source. | Verified (paraphrase) |
| C04 | NIST; Watson | NIST DLMF 10.32.10 at lines 163--171 gives the identical $K_\nu$ integral after algebraic rearrangement. DLMF Section 10.32 at lines 31--38 identifies Watson (1944), pp. 79, 80, 172, and 181--183, as a source; Cambridge records confirm the cited second-edition metadata. | Verified (exact formula; authoritative cross-reference) |
| C05 | NIST | NIST DLMF 5.11.12 at lines 294--305 states $\Gamma(z+a)/\Gamma(z+b)\sim z^{a-b}$; $a=3/2$, $b=0$, $z=N$ gives the manuscript's asymptotic exactly. | Verified (exact specialization) |
| C06 | ZengLens | Primary Preprints.org v1 lines 65--69 state that its sharp-constant results use exact rational certificates and that every computer-assisted assertion has an exact rational verifier; lines 756--761 and 1741--1745 describe rational positivity, reconstruction, and independent exact checks. Title, author, date, version, and DOI match the registry and final BibTeX. | Verified (paraphrase) |

No claim is numerically rounded from a cited source. There are no
hallucinations, citation-not-found results, contradictions, misleading
strengthenings, or unsupported uses of a source. The exact Abel formula is
clearly described as supervisor-generated rather than attributed to Spector and
Stockdale, and no publication-priority claim is made.

## Bibliography coverage and user-library decision

The union of ledger keys is exactly the five ordinary body-flow citation keys.
The bibliography is not user-library-only: Spector--Stockdale is the primary
problem source and closest general estimate; Gustafsson--Sakai supplies the
partial-balayage context; NIST and Watson supply the special-function
representation and asymptotic background. Active-registry row 13 is retained
only for the narrow exact-verification method comparison. All 49 first-sheet
registry records were screened; no second record naturally supports a nearby
claim, so adding one would be padding. No retained citation is decorative and
no literature-dependent body claim lacks its natural source.

## Bibliographic and mechanical checks

All five records exist and their author, title, year, and venue or publisher
fields agree with the authoritative records inspected. No BibTeX block or
citation key needed replacement. The bibliography checker reports five cited
keys, five BibTeX entries, no missing or unused entries, and exact agreement
with the five bibcite keys in main.aux. The converged clean-build main.log and
main.blg contain no undefined citation or reference, missing database entry,
duplicate entry, BibTeX warning, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.

## Authoritative sources consulted

| Key | Authoritative record | Nearby use |
|---|---|---|
| SpectorStockdale | https://arxiv.org/html/2609.05377v1 | Abel-power definition, square function, closest general bound. |
| GustafssonSakai | https://www.sciencedirect.com/science/article/abs/pii/0362546X94901074 | Classical partial-balayage context. |
| NIST | https://dlmf.nist.gov/10.32#E10 and https://dlmf.nist.gov/5.11#E12 | Bessel integral and Gamma-ratio asymptotic. |
| Watson | https://books.google.com/books/about/A_Treatise_on_the_Theory_of_Bessel_Funct.html?id=WNoIAQAAIAAJ | Classical Bessel-function compendium corroborated by DLMF. |
| ZengLens | https://www.preprints.org/manuscript/202608.1272 | Gate-selected exact-rational verification comparison. |

The citation and coverage audit accepts the current manuscript.
