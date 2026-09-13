# Proof dependency graph

- **T1 scalar all-precision disproof**
  - L1: midpoint identity `RN_even(2^p+1)=2^p`.
  - L2: exact Algorithm 1 trace gives `x_0=0`.
  - L3: exact Algorithm 2 transition maps `0` to `0`.
  - L4: induction gives `x_k=0` for all `k`.
  - L5: exact feasibility and scalar condition numbers equal one.
  - L6: exact backward error at zero equals one and `eta/epsilon=2^p`.
- **T2 2x2 embedding**
  - T1 coordinate trace.
  - L7: exact singular values of two positive diagonal matrices.
  - L8: `epsilon*kappa_A, epsilon*kappa_B -> 0`.
- **L3 structural denominator range**
  - Common invariant subspace `ker(v^T)` gives scale-ratio bounds.
  - Spectral-radius bounds for `BA^-1` and `AB^-1`.
- **L4 denominator-error reduction**
  - Exact Sherman--Morrison multiplication.
  - Rank-one identity `R^2=lambda R`.
- **P5 conditional recurrence**
  - Exact residual identity `r_{k+1}=-f_k+c_k-Bs_k`.
  - Triangle inequality and geometric-series summation.

Independent machine checks: `verification/verify_stagnation.py` and
`verification/verify_stagnation_2x2.py`; independent hardware trace:
`verification/verify_stagnation_hardware.c`.
