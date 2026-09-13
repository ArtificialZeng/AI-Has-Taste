# Proof audit

Status: PASS.  Date: 2026-08-30 CST.

## Statement and scope

- The formal theorem defines the square-root branch, formal EGF coefficients,
  exact recurrence, universal range, and both initial-index conventions.
- The proved endpoint matches the user's recurrence.  The sole boundary
  clarification is explicit: define (a_0=F(0)=0) to include (n=4), or use
  the OEIS offset and start at (n=5).
- No claim of minimal ODE order, a new EGF, a re-proof of the combinatorial EGF,
  or the OEIS asymptotic is made.

## Dependency reconstruction

1. (s^2=1-2t), (s(0)=1) implies (s'=-1/s).
2. The basis ((E,E/s,G)) is closed under differentiation over
   (mathbb Q(t)); the state matrix is derived explicitly.
3. The componentwise row identity proves (L_3(F)=0).
4. Exact right-normal Ore multiplication proves (M\circ L_3=L_5).
5. Exact EGF extraction at (t^{n-4}/(n-4)!) gives the target recurrence.
6. Formal expansion gives the initial block.

No step divides by a formal series with zero constant term.  At (n=2) the
recurrence's leading coefficient vanishes, so that index is not used for
initialization.  No negative-index coefficient is used.

## Independent routes

- Builder derivation: `proof/main_proof.md` and `src/derive_annihilator.py`.
- Breaker: branch, singularity, index, Leibniz-rule, and factorial attacks;
  complete independent enumeration for (1\le n\le7).
- Certifier: standard-library rational-function verifier importing no discovery
  code; exact formal Taylor reconstruction.
- Referee: reconstruction from definitions plus direct differentiation of the
  literal radical/exponential EGF.

All four roles were executed serially as required.

## Executed tests

```text
python3 certificates/verify_certificate.py certificates/annihilator_certificate.json
  VERIFIED: five exact checks
python3 tests/test_certificate.py
  PASS: valid certificate accepted; 4 corruptions rejected
python3 tests/enumerate_small.py
  PASS: n=1..7 = 0,1,1,21,168,1968,26094
python tests/direct_symbolic_check.py
  PASS: L3(F)=L5(F)=0
python src/derive_annihilator.py
  PASS: exact L3 and M o L3 coefficients reproduced
```

Certificate SHA-256:
`8d31bebf230f3a3eda53d881f5094573d6fcee8406619e27878fbffa95b3a1ba`.

Verifier SHA-256:
`86232f3821c5d37b6c7c6b40729b34faf98418d24eaa69829ceadf440e958982`.

## Verdict

No fatal, major, local, or expository mathematical gap remains.  The terminal
mathematical status is `PROVED`.  No proof assistant was used.
