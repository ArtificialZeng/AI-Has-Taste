# Verification Report

**Mode:** Search verification for external claims; exact-artifact verification
for new mathematical claims  
**Document:** `paper/main.tex`  
**Generated:** 2026-08-30 CST  
**Frozen extraction:** `audit/CITATION_CLAIMS_PASS1.md`

## Summary

| Metric | Count |
|---|---:|
| Total claims extracted | 12 |
| Verified | 12 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status:** PASS: all frozen claims verified.

## Verified claims

| ID | Claim | Source/evidence | Location | Confidence |
|---|---|---|---|---|
| M01 | Krasko--Omelchenko proved the displayed EGF for labelled simple chord diagrams. | Publisher PDF | Theorem 4.3, equation (17), printed p. 13 | exact |
| M02 | A278992 has the stated combinatorial name and EGF. | Live OEIS entry | NAME and FORMULA | exact |
| M03 | OEIS labels the exact recurrence conjectural on the access date. | Live OEIS entry | FORMULA; Mathar attribution dated 2020-01-27 | exact |
| M04 | Universal recurrence, range, and both initial blocks. | `proof/main_proof.md`; standard-library certificate verifier | theorem, coefficient conversion, formal initials | exact |
| M05 | The order-2 and order-1 piece annihilators. | Exact state-system derivation; direct differentiation | proof equations (2)--(3); direct test | exact |
| M06 | Row identity and order-3 annihilator. | Certificate reconstruction and direct differentiation | check `state_system_to_L3` | exact |
| M07 | Ore product and order-5 annihilator. | Independent Leibniz-rule implementation and direct differentiation | checks `ore_left_product_to_L5`; direct test | exact |
| M08 | ODE-to-recurrence coefficient conversion. | Falling-factorial table and independently reconstructed lags | check `L5_to_recurrence` | exact |
| M09 | Coefficients a0 through a6. | Formal square-root/exponential series reconstruction; publisher/OEIS terms for a1 onward | verifier; KO17 Theorem 4.3; OEIS list | exact |
| M10 | Verifier independence and fail-closed behavior. | Code inspection; four mutation tests | `certificates/verify_certificate.py`; `tests/test_certificate.py` | exact for documented mutations and strict parser |
| M11 | Direct ODE checks and exhaustive counts for n=1..7. | Separate direct-expression script and complete matching generator | both tests print PASS | exact |
| M12 | No proof assistant was used. | Project dependency/code audit; disclosure | no Lean/Coq/Isabelle artifact or invocation; only exact Python/SymPy scripts | exact |

## Mandatory academic citation searches

All five applicable templates were run for Krasko--Omelchenko:

1. `Krasko 2017 Enumeration of Chord`;
2. exact full title restricted to Semantic Scholar or arXiv;
3. `Krasko 2017 Electronic Journal of Combinatorics chord diagrams`;
4. `doi:10.37236/6037`;
5. `arxiv:1601.05073`.

The publisher record, publisher PDF, arXiv record, Crossref, DBLP, and zbMATH
agree on title and authors.  The publisher/Crossref publication date is
2017-09-08.  The arXiv record has v1 dated 2016-01-19 and supplies the journal
reference.  The bibliography uses the formal journal publication.

For M02--M03, direct live OEIS inspection was supplemented by exact NAME, EGF,
and conjecture-string searches restricted to A278992.  Exact text and numbers
match the manuscript; there is no rounding.

## Sources

| ID | Citation | Type | URL | Used for |
|---|---|---|---|---|
| S1 | Krasko and Omelchenko, EJC 24(3), P3.43 (2017) | primary journal article | https://www.combinatorics.org/ojs/index.php/eljc/article/view/v24i3p43 | M01, M09, bibliography metadata |
| S2 | Publisher PDF for P3.43 | primary full text | https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p43/pdf/ | M01, M09 |
| S3 | OEIS A278992 | primary sequence record for the claimed OEIS state | https://oeis.org/A278992 | M02, M03, M09 |
| S4 | arXiv:1601.05073 | primary preprint/version record | https://arxiv.org/abs/1601.05073 | version and journal cross-check |
| S5 | DOI 10.37236/6037 | publisher resolver | https://doi.org/10.37236/6037 | bibliography metadata |

## Numerical and visual audit

Every number in the frozen claims matches its source or exact certificate.
The manuscript has one coefficient table, not an empirical chart: every entry
is recomputed symbolically by the verifier.  There are no axes, units, error
bars, or graphical proportions to audit.
