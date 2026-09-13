# Formal statement

## Source-level ambiguity and repair

The user's prose mentions complex matrices, but the displayed relation uses an
order relation on `per(T)^2`; there is no canonical order on the complex
numbers.  Marcus's published/arXiv article formulates its setup and rank-two
theorem over real matrices and states Conjecture 10 with the displayed
ordinary order.  The well-posed source-backed conjecture studied here is
therefore the real one.  No complex analogue is asserted.

## Forced small-order target

For `n=3`, prove or disprove:

> For every `T in R^(3 x 3)` with `rank(T) <= 2`,
> `per([[T,T],[T,T]]) <= 20 per(T)^2`.

The secondary target is the analogous assertion for `n=4`, with coefficient
`binom(8,4)=70`.

## Quantifiers and conventions to be fixed after source verification

- `n` is a positive integer, with the forced target `n in {3,4}`.
- `T` is finite-dimensional and has real entries.
- `rank(T) <= 2` includes ranks zero and one.
- `per` is the unnormalised permanent, `per(A)=sum_sigma prod_i A_{i,sigma(i)}`.
- The `2n x 2n` block matrix has four identical `n x n` blocks equal to `T`.
- No division by `per(T)` is allowed; the case `per(T)=0` is part of the claim.
- Equality and zero cases will be classified only for the finally proved
  endpoint.

## Invariances

Independent row and column scalings send both sides through the same
homogeneous factor squared.  This does not license
division by a zero scale and does not by itself give a compact quotient.

A factorisation `T=UV^T`, with `U,V in R^(n x 2)`, is unchanged by
`(U,V) -> (UG,VG^(-T))` for `G in GL_2(R)`.  Zero rows/columns and repeated
projective factor lines are separate boundary strata.
