# Exact singular-value asymptotics for Sylvester Example 6

## Immutable source statement

For `0<delta<=1`, set

`A=diag(1,4,7)`, `B_delta=diag(10,1-delta,20)`,

and let `X_delta` be the unique solution of `A X-X B_delta=C`. Thus `X_delta=C circ R_delta`, where

```
R_delta = [ -1/9    1/delta      -1/19
            -1/6    1/(3+delta)  -1/16
            -1/3    1/(6+delta)  -1/13 ].
```

For each of the four fixed right-hand sides used in Example 6,

`C_1=I+E_12`, `C_2=ones(3)`, `C_3=ones(3)-E_12`, and `C_4=I`,

determine the exact leading asymptotic constant and exponent of the spectral condition number `kappa_2(X_delta)` as `delta->0+`. For the two bounded cases, determine the exact finite limit. Give rigorous error terms or explicit two-sided bounds valid for all sufficiently small positive `delta`; if feasible, strengthen them to the full interval `(0,1]`.

## Quantifiers and scope

- The four matrices and the spectral 2-norm condition number are fixed exactly as above.
- The required leading constants must be exact algebraic numbers or exact formulas, not decimal fits.
- Rank loss at a parameter value must be treated explicitly; `kappa_2` uses the source convention based on the smallest nonzero singular value only if rank deficiency actually occurs.
- General classification for arbitrary `C` is optional and cannot replace resolution of all four frozen cases.

## Primary source and nearest result

- Froilán M. Dopico, Enrique S. Quintana-Ortí, and Paul Van Dooren, *Conditioning of solutions to the Sylvester equation*, arXiv:2609.04050v1 (2026), https://arxiv.org/abs/2609.04050.
- Local PDF: `batches/inbox/bigWin-56-materials/2609.04050.pdf`.
- SHA-256: `dcb0d9a0b6643986f4b56a623e853e82d8d88da667386e872c5414eb33ba2972`.
- Locators: vectorized Sylvester operator and `kappa_2`, PDF pp.2--3; diagonal Cauchy representation in Section 6; Example 6 and Figure 3, pp.21--22.
- Nearest result: Example 6 reports from 30 floating-point values that the four orders are respectively `delta^-2`, `delta^-1`, bounded, and bounded. It does not state exact constants or prove those asymptotics.

## Proposed contribution boundary

A minimal complete contribution is an exact proof of the four source examples. A stronger minors/compound-matrix classification for arbitrary fixed `C` is welcome only if fully proved and separately scoped. Do not advertise the already explicit bounded-input ill-conditioning families elsewhere in the source as new.

## Cheapest decisive test and certificates

Form `X_delta^*X_delta` over `Q(delta)`, derive its characteristic polynomial, and isolate its three positive roots as Laurent/Puiseux series with exact remainder control. Exterior-power minors may determine the valuations more cheaply. Cross-check exact formulas against arbitrary-precision interval arithmetic at held-out rational deltas. Floating-point slopes alone are not a proof.

## Provenance

Prepared on 2026-09-07 from the primary PDF during the authorized fallback after the exact Chrome target could not be attached. This file freezes the four-case problem.
