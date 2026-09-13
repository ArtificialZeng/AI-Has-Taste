# Proof audit

Audit date: 2026-08-22.

Terminal status: **partial theorem**.

## Dependency check

| Node | Claim | Evidence | Verdict |
|---|---|---|---|
| P1 | affine cofactor sign vector | determinant expansion; independent script | pass |
| P2 | four points convex iff orientation product is positive | P1 plus Radon partition; two exact enumerators | pass |
| P3 | x-ordered four-sign sequence changes at most once; four clauses are minimal | proof plus exhaustive implicate cover | pass |
| P4 | factored ternary half-reification is exact in its asserted direction | proof plus complete 32-assignment truth table | pass |
| P4a | four clauses are minimal for the half relation and eight for full equivalence, modulo one-change | exhaustive exact-cover calculation over all 242 local clauses | pass |
| P5 | every nonconvex finite set has a nonconvex four-subset | triangulation argument | pass |
| T1 | geometric counterexample implies SAT; UNSAT implies upper bound | P2--P5 | pass |
| T2 | exact 33-point formula counts | two programmatic derivations and hand formulas | pass |
| C1 | `F_(9,5)` is UNSAT | checked DRAT and independently checked LRAT | pass |
| P6 | the unanchored `F_(17,6)` is UNSAT | exact reduction to Szekeres--Peters Theorem 2 | pass |
| C2 | extreme-normalized direct 17-point formula is UNSAT | exhaustive 61-cube cover; 61 checked DRAT files; 61 checked LRAT files | pass |

The final release entry point `python3 code/run_all_verifiers.py` completed
successfully after reconstructing the 1,024-case cover and rerunning both
independent checkers on all 61 proof leaves.  It reported 288,562,058 DRAT
bytes and 871,234,978 LRAT bytes checked.

## Major-gap audit

There is no unresolved major gap in T1 or T2.  The global conjecture still has
two mutually exclusive missing endpoints: no complete UNSAT result and
independently checked proof trace for the unanchored 33-point formula (or a
sound strengthening), and no realizable rational 33-point counterexample.
The paper states these omissions explicitly.

## Adversarial conclusion

The reduced five-point relaxation was shown incomplete in an unanchored
benchmark and was excluded from the main theorem's consistency block.  No
claim relies on interpreting its SAT model geometrically.  The 120-unit
extreme-point normalization is used only for the geometric certificate; the
paper does not assert that it is equisatisfiable over all abstract signotopes.
