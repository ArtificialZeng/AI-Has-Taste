# Proof audit

Status: passed for the exact finite endpoint `L_8=94` on 2026-08-30.

- Formal statement/source match: passed, with repairs explicitly logged.
- Target count/convention: Möbius derivation plus two exact generators passed.
- Lower-bound dependency: occurrence ordering -> dummy assignment -> exact
  dual value 146 -> length 94; reconstructed by Referee.
- Upper-bound dependency: literal length-94 binary word -> all 30 factors;
  direct substring and rolling-window checks passed.
- Exact certificate: all 930 dual inequalities passed using Python integer and
  string operations.
- Independent computation: integer Hungarian optimum 146 passed and was
  regression-tested against 72 exhaustive small assignments.
- Fail-closed tests: seven expected rejection/pass outcomes behaved as
  specified.
- Fatal/major gaps: none open in `proof/gap_ledger.md`.
- Numerical evidence: discovery only, excluded from proof dependencies.
- Proof assistant: none used.
