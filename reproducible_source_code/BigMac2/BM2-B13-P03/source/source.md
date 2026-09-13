# bigMac-00013-p03 — Exact Lipschitz constant of an explicit one-dimensional Brenier map

## Immutable source statement

Let `gamma_1` be standard Gaussian measure on the real line, let

`d nu_L(t) = Z_L^(-1) exp(L|t|) d gamma_1(t)`, `L>0`,

and let `T_L` be the monotone transport from `gamma_1` to `nu_L`. Prove or
disprove, for every `L>0`,

`Lip(T_L) = T_L'(0) = Z_L = 2 exp(L^2/2) Phi(L)`,

where `Phi` is the standard Gaussian distribution function. If true, include
the resulting sharp large-`L` logarithmic asymptotic and determine the full
set of essential derivative maximizers.

## Primary boundary

Maja Gwóźdź, *Caffarelli Estimates under Lipschitz Perturbations*,
arXiv:2609.04052v1, Theorem 1.1 and Remark 5.7, pp. 2 and 25--26. The source
computes `T_L'(0)=Z_L` and uses it only as a lower bound on `Lip(T_L)` to
show quadratic-order necessity; it does not assert the global equality.

Primary PDF: `batches/literature/bigMac-13/2609.04052v1.pdf`  
PDF SHA-256: `1077982c0ecae8d89b231058b6b2485fe317ce8b0eee8777f9bcef58d78b0086`

## Permitted contribution boundary

A proof of the exact equality for all `L>0`, an exact counterexample with a
corrected maximization formula, or a genuinely sharp nontrivial parameter
range. Plotting or floating-point maximization alone is evidence only.
