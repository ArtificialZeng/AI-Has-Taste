# Citation and bibliography audit

## Method and scope

Search-verification mode was used on 2026-09-07.  Stage 1 extracted and froze
all seven manuscript claim/citation pairs in `audit/claim-ledger.json` before
any source verification.  Stage 2 used that fixed ledger and checked the exact
source passages, bibliographic identities, and nearby support.  The audit was
performed serially because the job explicitly prohibited subagents.  The
source tree contains no `literature/bibliography-revision-*.md` or saved
`literature/crossref-*.json`/`.md` captures; live authoritative pages and the
frozen local source PDF were therefore used.

## Fixed-claim verification

| ID | Key | Primary record and exact location | Nearby support | Status |
|---|---|---|---|---|
| C01 | `ThejithaFathima2026` | arXiv:2609.03926v1, equation (1.2), PDF p. 2; Conjecture 7.1 and its preceding computational-evidence sentence, PDF p. 22 / arXiv HTML Section 7 | Gives the manuscript's generating function and states exactly `bbar^4_{4,2}(5n)=0 mod 5` for all `n>=1` as a computation-based conjecture. | Verified, exact |
| C02 | `ChaconSellers2026` | arXiv:2606.21780v1, abstract; Section 3, Corollary 3.2 and Theorem 3.3; Section 4, e.g. Theorem 4.2 | Establishes generating-function congruences for the overcubic `k`-tuple family.  Its one-parameter overcubic family is distinct from the manuscript's `(r,s)=(4,2)` specialization. | Verified, paraphrase |
| C03 | `Newman1959` | Morris Newman, *Proc. London Math. Soc.* (3) 9 (1959), 373--387, DOI 10.1112/plms/s3-9.3.373, Theorem 1 and surrounding construction on pp. 374--376 | Supplies the classical eta-product modularity congruence conditions to which the manuscript attributes its standard criterion. | Verified, paraphrase |
| C04 | `Ligozat1975` | Ligozat, *Courbes modulaires de genre 1*, Memoire 43 (1975), Section 5.2, Proposition 5.2.8, scan p. 30 (printed p. 54) | Gives the valuation of an eta product at a cusp in terms of the eta exponents; it specializes to the formula displayed in the manuscript. | Verified, paraphrase |
| C05 | `AtkinLehner1970` | Atkin--Lehner, *Math. Ann.* 185 (1970), 134--160, Section 2, equation (2.2), printed p. 138 | Defines `U_q` for primes `q` dividing the level and treats it as an operator on the fixed-level modular-form space, supporting the `U_5` preservation claim. | Verified, paraphrase |
| C06 | `Sturm1987` | Sturm, *On the Congruence of Modular Forms*, LNM 1240 (1987), Theorem 1, p. 276, DOI 10.1007/BFb0072985 | Gives the coefficient congruence bound `k[SL_2(Z):Gamma]/12`; the manuscript's exact arithmetic `60*36/12=180` is correct. | Verified, exact theorem plus exact calculation |
| C07 | `ZengEtAl2026` | DOI 10.20944/preprints202608.1658.v1, official Preprints.org full text, Section 6, “Certificate Architecture and Reproducibility” | Explicitly separates discovery from certification and describes exact standard-library verifiers and integer/rational decisive comparisons.  This supports only the narrow methodological comparison made nearby. | Verified, paraphrase |

Authoritative records used were the two arXiv abstract/full-text pages, Wiley's
DOI record for Newman, NUMDAM's complete Ligozat scan and exported metadata,
Springer Nature's records for Atkin--Lehner and Sturm together with the cited
original-text locations, and the official Preprints.org full text for the
user-library item.  Titles, author lists, years, venues, pagination, arXiv IDs,
and DOIs in `manuscript/references.bib` agree with those records.  No BibTeX key
change or entry replacement was needed.

## Coverage and relevance

The bibliography is not library-only.  It includes the problem-origin preprint,
the closest overcubic antecedent, primary sources for the Newman eta criterion,
Ligozat cusp orders, the level-dividing `U_p` operator, and Sturm's congruence
bound.  The exact Euler-product verifier is described by the manuscript and
included in `publication.json`, so it needs no external software-method citation.
The retained user-library item is row 9 of the active 49-record first-sheet
registry; it is cited directly in ordinary body flow as `\cite{ZengEtAl2026}`.
No second library record naturally supports a claim in this paper, so adding one
would be padding.  The exact attempt binding and claim-level justification are
in `audit/user-bibliography-selection.json`.

No decorative citation, unsupported strengthening, numerical discrepancy,
undefined key, duplicate entry, or missing natural primary source was found.
The bibliography checker reports 7 cited keys, 7 database keys, and identical
source/auxiliary key sets.
