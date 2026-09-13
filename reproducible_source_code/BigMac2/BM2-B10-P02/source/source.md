# bigMac-00010-p02 — Sharp N^(3/2) consensus-time constant

## Immutable source statement

Use exactly the asynchronous with-replacement model of arXiv:2609.04468v1 and
the monotone rule

`f(x1,x2,x3) = x1 OR (x2 AND x3)`.

Let `T_N` be absorption time and `E_s` expectation conditional on `S_0=s`.
Determine whether

`C_* = lim_{N->infinity} N^(-3/2) max_{1<=s<N} E_s[T_N]`

exists; if it does, give an exact integral or standard-special-function
expression and determine the limit set of maximizing `s/sqrt(N)`.

## Primary boundary

Mossel, *Consensus times for monotone aggregation dynamics*,
arXiv:2609.04468v1, Theorem 1(iii), Proposition 13, and Sections 2.6--2.7.  The
source proves only order `Theta(N^(3/2))` for this residual-minterm size.

Primary PDF: `batches/literature/bigMac-10/2609.04468v1.pdf`  
PDF SHA-256: `97409d22628a2f5693a518d5ee5b17f675693c8d1ccac2e9d36e64e26073225b`

## Permitted contribution boundary

A uniform asymptotic theorem for the exact finite birth--death chain.  Numerical
fits may identify the candidate constant but are not a proof of the limit or of
maximizer convergence.

