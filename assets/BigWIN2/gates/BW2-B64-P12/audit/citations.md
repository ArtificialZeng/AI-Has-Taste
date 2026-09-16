# Fresh citation and claim verification report

Mode: search verification with frozen local primary evidence

Document: `manuscript/main.tex` and `manuscript/references.bib`

Generated: 2026-09-07

## Summary

| Metric | Count |
|---|---:|
| Claims frozen in pass 1 | 18 |
| Verified | 18 |
| Numerical error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Citation not found | 0 |

Overall status: **PASS**.  Every frozen claim and every retained citation was
checked.  One contextual sentence was narrowed during verification so that it
describes the positive-limit criterion only as a sufficient case within Jay's
Q-order framework.  The final source was then rebuilt and the affected checks
were repeated.

## Claim-by-claim result

| IDs | Status | Confidence | Verification |
|---|---|---|---|
| C01--C02 | Verified | exact | arXiv record and v1 PDF pp. 2--4 state CTM and general order six; the counterexample scope equals accepted `claim.json` and `audit/math.md`. |
| C03 | Verified | paraphrase | Wiley's original Schulz record and the Petković article establish the historical multiplication-based matrix-inversion context. |
| C04, C06 | Verified | exact | Elsevier abstract and article formula give residual-polynomial hyperpower methods and explicit multiplication-reducing factorizations. |
| C05 | Verified | exact | Cordero--Torregrosa v1 equations (1.4), (2.1), and (2.4) match the manuscript update and residual convention. |
| C07 | Verified | interpretation | Jay p. 425 places positive two-sided quotient bounds within exact Q-order; the manuscript's positive finite limit implies those bounds and is expressly called a sufficient case. |
| C08--C13 | Verified | exact | These are the accepted theorem and displayed exact proof; `evidence/verify_identities.py` was rerun successfully. |
| C14--C16 | Verified | exact | Cordero--Torregrosa Theorem 2.1 and PDF p. 4 support the hypotheses and exact two proof passages; `audit/math.md` accepts the comparison. |
| C17 | Verified | paraphrase | Preprints.org Section 2 and equations (11)--(18) exhibit a 2-by-2 matrix counterexample certified by strict rational inequalities. |
| C18 | Verified | exact | The verifier returned `all exact symbolic identities verified`; its role agrees with the assistance disclosure and accepted evidence. |

Detailed URLs, source locations, bibliographic records, and the coverage rationale
are in `audit/citation-source-verification.md`.  The audit was serial because the
job expressly prohibited subagents.

## Bibliography audit

| Final key | Primary record | Nearby support | Action | Uncertainty |
|---|---|---|---|---|
| `CorderoTorregrosa2026` | arXiv:2609.04433v1 | CTM, Theorem 2.1, equations (1.4), (2.1), (2.4), (2.7) | retained | none |
| `Schulz1933` | Wiley DOI record | original reciprocal-matrix iteration | retained | full publisher PDF unavailable, but the conservative historical claim is corroborated by the adjacent primary hyperpower source |
| `PetkovicPetkovic2015` | Elsevier DOI record | hyperpower polynomial factorization reduces products | retained | none |
| `Jay2001` | Springer DOI record and article text | exact Q-order framework and sufficient quotient-bound case | retained; prose narrowed | none material |
| `ZengLiuRatnavelu2026` | Preprints.org v1 and arXiv:2608.15558 | exact 2-by-2 matrix counterexample and rational certificate | retained | none |

There were no key changes.  The mechanical checker reports five cited keys,
five BibTeX entries, no missing or unused entries, and exact AUX agreement.  The
converged `.log` and `.blg` contain no undefined citation/reference, database
miss, repeated entry, LaTeX error, overfull box, or underfull box diagnostic.
