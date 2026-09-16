# win-00064-p12 — Exact counterexample to claimed sixth-order norm-accelerated CTM convergence

Audit the norm-accelerated CTM inverse-matrix iteration defined in Cordero–Torregrosa, arXiv:2609.04433v1, Section 2, especially Theorem 2.1 and equations (2.4)–(2.7). Decide whether its asserted local order six is valid for general matrices rather than only scalar or isotropic residuals.

The first exact test to reproduce is `A=I_3`, Frobenius norm, residual `R=t diag(1,2,3)`, and `X=I-R`. Direct substitution is reported to give `nu=||R^2||_F^2/||R||_F^2=7t^2` and

`R_next = t^4 diag(-6,-12,18) + 7 t^6 diag(1,16,81)`.

Independently derive this identity from the source update. If correct, prove that the nonzero quartic direction is not a one-step artifact and determine the actual asymptotic order on an explicit small initial interval; identify the exact invalid implication in the published convergence proof. If the calculation uses the wrong residual/update convention, reject it rather than adapting the theorem. A resolution-paper claim must distinguish refuting the stated general theorem from analyzing only this diagonal family.

Primary evidence: `batches/inbox/bigWin-64-materials/2609.04433.pdf`, SHA-256 `0b2d8edbed7c6b69ef0f9edd7e106e919c7a2f5976f845e16b3758528a32fe2c`, PDF pp.3–4.
