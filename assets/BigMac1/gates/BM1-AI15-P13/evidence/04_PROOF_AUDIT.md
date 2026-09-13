# Proof audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS -- terminal result `DISPROVED` is certified for the precise
uniform, condition-number-only formulation in `problem/formal_statement.md`.**

## Independent reconstruction

The proof-builder, counterexample-hunter, and referee/certifier roles worked
from the source algorithm and produced separate records in `notes/`. The
referee did not assume the discovery argument and reconstructed the decisive
binary64 trajectory operation by operation. The referee's verdict is that the
nonzero-denominator fixed point is valid, that it refutes the standard uniform
interpretation of the conjecture, and that it does not contradict the source
paper's conditional one-step theorem. The final source-line reconstruction is
recorded in `audit/REFEREE_OPERATION_ORDER.md`: it separately checks the
residual graph from Algorithm 2 and its residual lemma, as well as both natural
parenthesizations of the correction addition.

## Fatal-step checklist

- **Quantifiers:** the source prose is not closed because “safely” and the
  stability constant are unquantified. The release theorem uses the standard
  precision-parametric meaning: `epsilon_p*kappa -> 0` and a stability
  constant independent of precision and data. A concrete binary64 corollary
  also violates the source experiment's `5 epsilon` threshold.
- **Rounding:** at precision `p`, the adjacent floats at `2^p` are `2^p` and
  `2^p+2`; midpoint parity proves `RN_even(2^p+1)=2^p`. The exact rational
  verifier reconstructs this decision without host floating point.
- **Operation graph:** the trace uses the source's split representation of
  `B=A+uv^T` and reuses the initially computed `z_hat,beta_hat`. The stored
  fixed point is unchanged by the ordinary associations of the update because
  every relevant value is zero or one.
- **No exceptional arithmetic:** every decisive input and intermediate is
  finite and normal; `beta_hat=2^p` is nonzero. The disproof does not use
  overflow, underflow, subnormals, NaNs, infinities, or division by zero.
- **All iterations:** the exact transition sends zero to zero. Determinism
  plus induction, rather than a finite simulation horizon, proves stagnation
  for every iteration.
- **Backward error:** at zero and nonzero `b`, the normwise and componentwise
  relative backward errors are exactly one. Matrix-only backward error is not
  finite because `(B+Delta B)0=b` is impossible.
- **Hidden constants:** `eta/epsilon_p=2^p` is unbounded, so no
  precision-independent `O(epsilon_p)` constant can absorb the example.
- **Scalar degeneracy:** the exact 2-by-2 embedding has
  `epsilon_p*kappa_2(A_p) -> 0` and
  `epsilon_p*kappa_2(B_p) -> 0`, yet preserves the same fixed point and error.
- **Condition-number calculation:** both matrices are positive diagonal in
  the 2-by-2 family, so their singular values and stated condition numbers are
  exact. The binary64 values are certified as rationals.
- **Structural lemmas:** the denominator-range lemma follows from a nonzero
  vector in `ker(v^T)`, singular-value comparisons, and the exceptional
  eigenvalues of `BA^{-1}` and `AB^{-1}`. The reused-denominator propagation
  identity follows by direct multiplication and gives `lambda=1` here.
- **Positive route:** the displayed `rho<1` recurrence is an exact conditional
  consequence of residual bookkeeping. The counterexample proves that its
  contraction hypothesis does not follow from the two condition numbers.

## Executable audit

The following independent checks all passed from serialized inputs:

1. `verification/verify_stagnation.py`: exact integers and `Fraction`;
   certificate SHA-256
   `28c6865ee1d22bf1def7565758fc3ddb254563be31ef69d3e1578a8180366eea`;
   verifier SHA-256
   `49c359401a23ca036108667e1ea22802c6266641498330b9daa88c7102467385`.
2. `verification/verify_stagnation_2x2.py`: exact rational condition numbers,
   safety margins, transition, and backward error; certificate SHA-256
   `662374272407d01b56fd18c86153d7fdfc69508a1cbbab0a51026524948c6e9a`;
   verifier SHA-256
   `0969a71fb3e8f6579557b565f648ddf94f03d818cf7545c25cd22d6b1d9be2dd`.
3. `verification/verify_stagnation_hardware.c`: separately compiled IEEE
   binary64 hardware trace with rounding-sensitive optimization disabled.
4. `notes/agent_builder_verify.py` and `breaker_main_verify.py`: independent
   scalar and 2-by-2 reconstructions both passed.
5. `breaker_verify.py`: an independent secondary scalar fixed point with zero
   computed residual also passed; it is supporting evidence, not needed for
   the terminal theorem.

The main verifiers reject duplicate keys, unknown or missing keys, nonexact
types, and nonstandard JSON constants before doing mathematics. The root
tamper suite gave nonzero exits for all six required attacks and six additional
attacks. An independent hostile audit also rejected 132 automatically generated
drop/extra/type mutations and coordinated semantic mutations. Full commands
and outcomes are in `audit/TAMPER_AUDIT.md`.

No fatal or major mathematical gap remains for the stated disproof. The
remaining limitation is semantic rather than mathematical: only the broad
condition-number-only conjecture is refuted. A repaired algorithm or theorem
with a genuinely scale-sensitive lost-addend/contraction guard, extra-precision
recomputation, or stable fallback remains open and is outside the claim.

## Formal methods disclosure

No proof assistant, SAT/SMT solver, CAD system, or computer algebra proof was
used. Numerical search was used only for discovery. The release proof rests
on exact arithmetic, finite serialized certificates, direct identities, and
induction.
