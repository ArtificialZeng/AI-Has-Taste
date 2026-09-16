# Root proof audit

Audit date: 2026-09-01. Verdict: PASS for the stated certified upper bound.

- Re-ran the dependency-free Python verifier on the final 65,536-cell witness.
  It parsed all entries as canonical nonnegative integers, recovered the
  complete 131,071-term convolution, and returned `PASS_STRICT_TARGET`.
- The exact outputs agree with the manuscript: sum
  `65535999999999705`, maximum coefficient
  `49241903898054382405913729558`, first argmax `24997`, and strict
  cross-product margin `329582828384544626350460026614125`.
- Checked the five NTT moduli for pairwise coprimality and independently
  recomputed that their product exceeds the proved coefficient bound by more
  than eleven orders of magnitude.
- Compared 256 deterministic convolution coefficients, including the stated
  maximum and both neighbors, against direct arbitrary-precision summation.
  Every selected coefficient agreed with the five-modulus reconstruction.
- Re-ran 2,741 direct rational interval-integration identities over 163 small
  cases. All agreed with the anti-diagonal coefficient formula and the affine
  interpolation claim.
- Re-ran the verifier's fail-closed self-tests. The C++ alternative was not
  compiled because this WSL installation has no C++ compiler; no C++ build
  claim is made, and the released dependency-free Python verifier is the
  executable reference.

The construction proves a strict upper bound only. It does not determine the
global infimum or classify extremizers. No proof-assistant formalization was
used.
