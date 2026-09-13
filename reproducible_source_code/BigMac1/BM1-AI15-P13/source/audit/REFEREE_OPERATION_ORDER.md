# Independent source-order referee audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS.** The referee reconstructed the operation graph directly from
`sources/2510.01696_src/manuscript.tex`, without relying on the project paper's
description.

## Algorithm 1

The source lines 85--88 specify, in order:

1. solve `A y = b` for `y_hat`;
2. solve `A z = u` for `z_hat`;
3. compute `alpha = v^T y_hat` and `beta = 1 + v^T z_hat`;
4. compute `theta = alpha/beta` and output `x_hat = y_hat-theta z_hat`.

The detailed floating-point table at source lines 324--340 fixes the scalar
roundings as dot product, dot product followed by addition for `beta`, division,
`theta*z`, then subtraction. The strict verifier follows exactly this graph.
For `A=u=b=1`, `v=2^53`, it independently reconstructs

`y=z=1`, `alpha=2^53`, `beta_exact=2^53+1`,
`beta_hat=2^53`, `theta=1`, `x_0=0`.

## Algorithm 2 residual

Algorithm 2 line 108 writes

`r = b - A*x_hat - (v^T*x_hat)*u`.

The residual lemma at source lines 512--533 supplies the actual rounding graph:

1. `p_hat = fl(b-fl(A*x_hat))`;
2. `q_hat = fl(fl(v^T*x_hat)*u)`;
3. `r_hat = fl(p_hat-q_hat)`.

`verification/verify_stagnation.py` implements this graph. At `x_hat=0`, every
product is exact zero and the residual is exact one. The referee additionally
checked right association, explicitly formed `B`, and ordinary fused evaluation;
all give exact residual one on this instance.

## Correction and final addition

Source lines 109--111 specify the `A`-solve, `alpha_r=v^T y_r`, reuse of the
initial `beta` and `z`, and the expression

`w_hat = x_hat + y_r - theta_r*z`.

The source does not fix the final floating-point parentheses. The verifier uses
the literal left association

`fl(fl(x+y_r)-fl(theta_r*z))`

and separately checks the correction-first association

`fl(x+fl(y_r-fl(theta_r*z)))`.

At the fixed point, `x=0`, `y_r=1`, `theta_r=z=1`; both expressions, other
ordinary associations, and ordinary FMA contraction return exact zero. Thus the
induction `T(0)=0` is independent of this source-level ambiguity.

## Scope verdict

The exact instance refutes the original broad condition-number-only conjecture
under its natural uniform interpretation. A simple `beta_hat != 0` no-breakdown
guard and ordinary FMA do not exclude it. It does not contradict the source
paper's conditional theorem at lines 544--570, and it does not settle a repaired
conjecture that imposes a scale/lost-addend/contraction guard, extra precision,
or a stable fallback. Such genuinely repaired versions remain open.

No proof assistant was used in this referee audit.
