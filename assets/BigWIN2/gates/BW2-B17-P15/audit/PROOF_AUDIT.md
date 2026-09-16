# Proof audit

- Formal theorem matches the corrected finite target and does not claim the
  global infimum is known.
- Feasibility: 65,536 canonical nonnegative integer heights, positive sum.
- Reduction: proved from triangular cell convolutions; endpoint and zero-cell
  cases covered.
- Exactness: all 131,071 coefficients recovered under five NTT primes; the
  checker proves its CRT modulus exceeds an a priori coefficient bound.
- Strictness: integer cross-product margin
  `329582828384544626350460026614125 > 0`.
- Independent tests: 2,741 direct-integration identities over 163 small cases;
  verifier small cases use separate naive big-integer convolution.
- The breaker's three-prime objection was valid and is preserved; the released
  verifier repairs it with five primes and a checked range guard.

Verdict: PASS for the stated certified finite result. No proof assistant used.

Status: not yet run.
