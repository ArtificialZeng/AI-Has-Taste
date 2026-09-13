# Proof audit

Audit date: 2026-08-22.  Final status: **PASS for the stated partial
theorems and certified finite computations**.  This project does not prove
or disprove Frankl's conjecture.

## Analytic results

1. **Integer deletion lift — PASS.**  For a Non-FC collection of distinct
   (k)-sets on at most (n) points, every point deletion remains Non-FC.
   Summing the (n) deletion inequalities counts every (k)-set exactly
   (n-k) times and proves
   
   \[
   M_k(n)\le \left\lfloor\frac{nM_k(n-1)}{n-k}\right\rfloor.
   \]
   
   The support-at-most convention and the monotonicity step were checked
   explicitly.

2. **Closed four-set recurrence — PASS.**  Starting with (M_4(8)\le11),
   the residue calculation modulo (7) correctly solves the adjacent-floor
   recurrence as
   
   \[
   M_4(n)\le \left\lfloor\frac{\binom n4+n}{7}\right\rfloor,
   \qquad n\ge8.
   \]
   
   Hence
   (\operatorname{FC}(4,n)\le1+\lfloor(\binom n4+n)/7\rfloor).
   An independent audit initially found erroneous comparison-table entries
   for (n=11,\ldots,15).  Those entries were corrected to
   (53,79,114,159,216), and the corrected table and proof were independently
   rechecked with final status PASS.

3. **Fixed-power no-go construction — PASS.**  For
   
   \[
   \mathcal G_{k,q}=\mathcal P(K)\cup
   \{K\cup\{c_1,\ldots,c_i\}:1\le i\le q\},
   \]
   
   direct incidence counts give
   
   \[
   W_p=k(2^{k-1}+q)^p q+
   \sum_{i=1}^q i^p(2i-2^k-q).
   \]
   
   With (q=2^k), its leading term is
   (-2(2^k)^{p+2}/((p+1)(p+2))), while the remaining contribution has
   lower order for every fixed nonnegative integer (p).  Thus each such
   frequency-power template has a twin-free union-closed counterexample.
   Exact examples for (p=0,\ldots,4) were constructed and checked.

## Computational results

- **Five-point census — PASS.**  The primary enumerator and an independently
  structured replay both enumerated the same (4{,}960^2) trace pairs and
  recovered all (2{,}771{,}104) labelled union-closed families on five
  points, of which (2{,}771{,}102) have nonempty support.  They agree on the
  equality count (202), minimum Frankl margin (0), all size and margin
  histograms, and every ordinary and twin-class weighting aggregate reported
  in the manuscript and JSON certificate.
- **Engineering hardening — PASS.**  An adversarial audit found that optimized
  Python could previously disable assertions and that the independent replay
  did not compare every published aggregate.  The verifiers now fail closed
  when `__debug__` is false, compare the complete aggregate record, and test
  union closure for every power-chain witness, including the 1,597-set
  (p=4) example.  Normal, optimized-mode failure, fast-certificate, and full
  replay checks were repeated successfully.
- All decisions use exact integer arithmetic.  No randomized or
  floating-point branch is part of a certificate.

## Remaining gaps

- Frankl's one-half conjecture remains open; the result concerns local
  Frankl-complete uniform configurations.
- The recorded literature search did not find the displayed adjacent-floor
  closed form, but it is not an absolute priority proof.  A specialist
  MathSciNet/zbMATH and historical-source check remains advisable before
  submission.
- No Lean, Coq, Isabelle, or other proof assistant was used.  The analytic
  proof has been independently read, and the computations have exact replay
  programs, but there is no formal proof object.
