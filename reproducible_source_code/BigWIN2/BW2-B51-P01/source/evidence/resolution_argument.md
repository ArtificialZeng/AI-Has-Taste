# Exact positive resolution of the frozen `(n,k)=(4,3)` cell

## Claim

With the notation and action convention of `source.md` and `problem.md`, put

`m_1=I_V` and `m_2=rho(X_1)rho(X_2)rho(X_3)`,

where

```
X_1 = [[ 2,  0,  0, -1], [ 1,  0,  0, -2],
       [ 1, -1,  1,  0], [-1, -1,  1, -3]],
X_2 = [[ 2,  1,  2,  2], [ 0, -2,  2, -1],
       [-2, -1,  2, -1], [ 2,  1, -2, -2]],
X_3 = [[ 1,  1,  0,  0], [ 1,  1,  0,  1],
       [ 2,  1, -2,  1], [-2, -2, -1,  0]].
```

Then `m_1 U+m_2 U=V`. Consequently

`diam_+^{sl_4(C),mon}(Sym^3(C^4),Sym^3(C^3))=2`.

This is only the single frozen `(n,k)=(4,3)` cell; it does not settle the other
cases in Question 8.5.

## Exact certificate

The diagonal sums of `X_1,X_2,X_3` are respectively
`2+0+1-3`, `2-2+2-2`, and `1+1-2+0`, hence all three factors are in
`sl_4(C)`.  The operator product is read right to left, so `X_3` acts first,
then `X_2`, then `X_1`.

Order the basis of `U` by the exponent tuples

```
(0,0,3,0), (0,1,2,0), (0,2,1,0), (0,3,0,0), (1,0,2,0),
(1,1,1,0), (1,2,0,0), (2,0,1,0), (2,1,0,0), (3,0,0,0),
```

and order the monomial basis of the quotient `V/U` by

```
(0,0,0,3), (0,0,1,2), (0,0,2,1), (0,1,0,2), (0,1,1,1),
(0,2,0,1), (1,0,0,2), (1,0,1,1), (1,1,0,1), (2,0,0,1).
```

Direct application of

`rho(X)f=sum_{i,j=1}^4 x_ij e_i partial(f)/partial(e_j)`

gives the following integer matrix for the composite
`U -> V -> V/U`, where the first arrow is `m_2` and its columns and rows use
the two displayed orders:

```
[[  12,   2, -10,  12,   0, -11,  16, -12,  20,  24],
 [  24, -46,  22,  -6, -38,  56, -18,  90, -40, -72],
 [ -54,   5, -24, -12,  77, -37,  -4, -84,  20,  72],
 [ -12,  -4, -12,   6,  -4,   9,  40,  20,  28, -36],
 [-102, -10, -30,-114,  34,   4, -46, -38,  -8,  72],
 [   0, -18, -24, -87,   0,   3,  -5, -16,  24,  12],
 [ -12, -10,  12,   6,  -4,   3,  12,  -2,  54, 138],
 [-108,   6,  14,   6,  12,  -9, -20,  14, -36, -96],
 [   0, -16,  -6,  24, -26, -17,  -2, -18,  -2,  18],
 [   0,   4,  -2,  -6, -28, -13,  -6,  -6,  -9, -21]].
```

Its exact determinant is

`8412259151430144`,

which is nonzero.  Equivalently, in the full lexicographic exponent basis of
`V`, the `20 x 20` matrix whose first ten columns are this ordered basis of
`U` and whose last ten columns are its images under `m_2` has the same exact
determinant.

## Proof

Let `pi:V -> V/U` be the quotient map.  The displayed determinant proves that
`pi o m_2|_U:U -> V/U` is an isomorphism.  Therefore every coset modulo `U`
has a representative in `m_2U`, so `U+m_2U=V`.  Since `m_1=I_V` and `m_2` is
a finite product of three elements of `rho(sl_4(C))`, both belong to the
specified monoid.  This proves the requested existence.

Finally, `dim V=20` and `dim U=10`.  Every single monomial image of `U` has
dimension at most ten, so one summand cannot span `V`.  Together with the
constructed pair, the diameter is exactly two.  There are no unproved
mathematical dependencies in this argument.

## Reproducibility and source scope

- `triage_exact_certificate.py` constructs the three `20 x 20` representation
  matrices entrywise and uses a pure-Python fraction-free Bareiss determinant.
- `research_independent_certificate.py` instead differentiates the cubics
  directly, applies `X_3,X_2,X_1` sequentially, and uses SymPy's exact integer
  determinant routine.  It reproduces both the quotient and full determinants.
- `external/2609.03882.pdf`, SHA-256
  `e8c327173640c56f21510418e4cfc329b138ba83b82d9e666361f082377ed849`,
  defines the monomial diameter on PDF page 29, proves only the `n=3` family in
  Theorem 8.1 on pages 30--32, and states the all-`n,k` Question 8.5 on page 32.

