# bigMac-00012-p04 — Logarithmic almost-sure threshold in a critical Pearson walk

## Immutable source statement

Work on one product probability space.  For every integer `d>=2`, let
`X_d~Ber(d^(-1/2))`; let `U_1^(d),U_2^(d)` be independent uniform directions
on `S^(d-1)`; and require the triples
`(X_d,U_1^(d),U_2^(d))` to be mutually independent across `d`.  Set

`L_1^(d)=1`,

`L_2^(d)=sqrt(d)(log d)^(-α)X_d`,

and, in the source's notation,

`Y_d=|S_(d,2)|_2^2-|L^(d)|_2^2`.

Determine exactly for which real `α` one has `Y_d -> 0` almost surely.  The
endpoint `α=1/2` is part of the statement.

## Primary boundary

Bignamini, Casini, and Martinelli, *Asymptotic Behaviour for Isotropic
Pearson Random Walks*, arXiv:2609.05195v1, Example 6.5, pp. 10--11.  For
`L_2^(d)=d^βX_d`, the source proves failure of almost-sure convergence at
`β=1/2` and gives a sufficient theorem covering `β<1/2`.  It does not state
the logarithmically damped critical threshold frozen here.

Primary PDF: `batches/literature/bigMac-12/2609.05195v1.pdf`  
PDF SHA-256: `1ceef2b47efc66235d08f814a56b7006b21d3948423c2432f5f91841c16535b8`

## Permitted contribution boundary

An if-and-only-if theorem in `α`, including an exact endpoint argument, or a
precisely scoped partial result that closes at least one nontrivial side plus
the endpoint.  Tail asymptotics must be strong enough for the relevant
probability series; simulations and convergence in probability do not prove
almost-sure convergence.
