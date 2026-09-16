# Proof audit

Status: PASS (mathematical gate), 2026-08-30.

## Statement reconstruction

- The source and formal statements both ask for the least maximum word length
  of a nonzero element of the unital free algebra on `X,Y` that vanishes on all
  ordered pairs in `M_3(F_2)`.
- The coefficient field, empty word, evaluation order, inhomogeneous terms, and
  universal quantifier are explicit.

## Upper bound

- The support contains 18 distinct words, including twelve of length seven, so
  the polynomial is formally nonzero and has degree seven.
- The independent verifier enumerates integers `0..511` in each matrix slot,
  a bijective encoding of all binary 3-by-3 matrices.
- Exact result: 262144 ordered pairs checked; 0 violations.
- A second multiplication formula agrees on all 262144 individual matrix
  products. No floating-point value or timeout is used.

## Lower bound

- The basis through degree six contains 127 words, including the empty word.
- Fifteen serialized pairs yield 135 scalar rows. The selected square minor is
  all 126 scalar rows from the first fourteen pairs plus entry 3 of the last.
- The verifier reconstructs this minor and obtains GF(2)-rank 127.
- A polynomial vanishing universally must vanish on this restriction; full
  column rank therefore forces all 127 coefficients to be zero. This proves all
  degrees at most six simultaneously.

## Adversarial checks

- An independent standard-library search with a different pair schedule and
  opposite pivot convention recovered the same 18-word degree-seven relation.
- A well-formed altered support was rejected at encoded pair `(1,0)`.
- Parser tests reject wrong degrees and duplicate minor rows.
- Zero, singular, scalar, commuting, and noncommuting cases are covered by the
  exhaustive domain rather than genericity assumptions.

## Conclusion

The endpoint `d_{3,2}=7` is proved. All fatal and major mathematical gaps are
closed. No proof assistant was used.
