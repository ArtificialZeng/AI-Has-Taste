# Second triage-timeout recovery handoff — win-00075-p04

This recovery is justified by new exact evidence, not by retrying an unchanged prompt. Both prior triage contexts hit the eight-minute phase ceiling before the runner could import a final result. Preserve `source.md` unchanged (SHA-256 `3ee9ccc12ddcd0cbb40f14d0a3444709b13b398ca02d9176d49d28788c4bc99e`).

## New evidence from the second attempt

The durable event log is `jobs/win-00075-p04-triage-beaafc11903e/events.jsonl`, SHA-256 `0bd573577a7e2a464dd194441d027baf6fa647838b5f895e7f668239c6affebf`. Its final completed command records an exact SymPy calculation:

```text
G-R = 0
limit G = 4*b
num(G-4b) = -2*h*(4*a**2*b + 8*a*b*h - a*b - 2*a + 4*b*h**2 - b*h - h)
den(G-4b) = (a + h)*(2*a*h + a + 2*h**2)
limit Phi/h^2 = pi**2/(3*a)
limit exact L = pi**2*b/3
```

The SHA-256 of that exact final JSONL line is `2631106d9dc01b8d03e2a20f181289c016996e88671c03a219f25fca9f45282f`. The prior handoff `evidence/triage-timeout-handoff-20260909.md` remains at SHA-256 `6446a36edd25b0d2db215c0a414751c2acd209c59ec7421186d27d033937d0da` and already distinguishes a proof-route obstruction from a counterexample to the operator-norm theorem.

## Single decisive recovery test

Reconstruct the unsimplified left-hand side `L_{alpha,b}(p)` of equation (3.38) from the primary source, and independently derive—not merely numerically fit—the right-endpoint limit

`lim_{p downarrow alpha+2} L_{alpha,b}(p) = pi^2 b / 3`.

Then compare `pi^2 b/3` with `B(1+alpha, 2+alpha/2)` throughout the full parameter domain of Theorem 3.4, including an explicit punctured-neighborhood estimate. This must decide whether Corollary 3.5 yields a b-dependent correction, whether an extra condition is needed, or whether only the displayed proof route fails.

On recovery, persist the exact source theorem domain and equation/page locators, the symbolic derivation, and the decision in `problem.md`, `checkpoint.md`, and a standalone evidence script/output. Return promptly once this one test is complete. Do not repeat broad literature searches, do not claim a theorem counterexample without an operator-level witness, and do not create a manuscript at triage.
