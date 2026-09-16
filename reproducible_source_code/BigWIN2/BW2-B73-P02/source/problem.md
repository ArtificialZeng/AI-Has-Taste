# Precise problem reading

## Frozen claim and notation

The immutable statement is `source.md` (SHA-256
`482b5d1916aca9fbcae82d4fbaa0069f6313a9c0b1c78e68d713ead991de6c9d`).
Its mathematical reading is as follows.

For an odd prime `p > 3`, identify each element of `F_p` with its canonical
integer representative in `{0,...,p-1}`.  For `A,B in F_p`, write these
representatives as `a,b`, put `w=p^2` and `e=floor(p/2)=(p-1)/2`, and use
truncated subtraction

`u dotminus v := max(u-v,0)`

on nonnegative integers.  Define, entirely in the nonnegative integers,

```
d = (floor((2^(3w) + a*2^w + b)^e / 2^(w*(p-1))) mod 2^w),
r = d mod p,
Nhat_p(A,B) = (p dotminus r)
                + p*(1 dotminus ((4p+1) dotminus r^2)).
```

Here `mod m` is the least nonnegative remainder.  Also define the affine
point count

`N_p(A,B) := #{(x,y) in F_p^2 : y^2 = x^3 + A*x + B}`.

Let `P(p)` be the universal assertion

`for every (A,B) in F_p^2, Nhat_p(A,B)=N_p(A,B)`.

The question is the quantified threshold statement

`for every odd prime p>3, P(p) if and only if p>=17`.

Thus the only lower primes requiring exclusion are `5,7,11,13`.  The count
is affine; the unique projective point at infinity is not included.  Both
singular and nonsingular cubics are in the universal quantifier.  The four
proposed lower-prime witnesses happen to be nonsingular, since
`4A^3+27B^2` is nonzero modulo the corresponding prime.

## Source status and nearest result

The sharp-threshold assertion and the four witnesses are supervisor-generated,
so the source status is **new-question**, not a literature-declared open
problem.  The nearest prior result is Theorem 3, Section 5, equations (4)--(5)
of arXiv:2609.05371v1, whose full arXiv HTML was inspected on 2026-09-08:
<https://arxiv.org/abs/2609.05371v1>.  It states that the displayed term equals
the affine point count for every prime `p>=17` and every parameter pair,
including singular cubics.  Its proof recovers the Frobenius-trace residue
from the coefficient of `x^(p-1)` and uses the Hasse bound to choose between
the two integer lifts.

There is a bibliographic error in `source.md`: the live arXiv v1 record lists
Bogdan Dumitru and Mihai Prunescu as authors, not Arno Fehm and Kurt Girstmair.
The title, theorem number, and formulas do match the linked paper, so this
metadata error does not alter the mathematical reading above.

## Triage target

Nearest prior result X: Theorem 3 proves `P(p)` for every `p>=17`.

Proposed delta Y: prove failure of `P(p)` at each of the four remaining
primes by one explicit nonsingular parameter pair, thereby making 17 sharp.

Verification route Z: evaluate equation (4) with exact integers, independently
expand the relevant coefficient, enumerate all `p^2` affine pairs, and compare
equation (5).  The initial exact replay is in
`evidence/verify_small_primes.py` with captured output in
`evidence/verify_small_primes.txt`.
