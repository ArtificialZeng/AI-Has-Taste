# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the `resolution-paper` claim frozen by snapshot
`c0f3b8cc7f4b5cbd0788a80b3ffc2fd08ee4d57780f2df030073d31148f8b89a`.
I recomputed the SHA-256 hash of `claim.json` and every evidence file listed in
`audit/snapshot.json`; every file hash and the canonical snapshot digest match.
The reviewed assertion is only the fixed `(n,k)=(4,3)` cell, with
`V=Sym^3(C^4)` and `U=Sym^3(span(e_1,e_2,e_3))`.  It does not assert the
universal form of Question 8.5.

## Reconstruction of the decisive argument

The degree-three monomials in four variables form a basis of `V`, so
`dim V=binom(6,3)=20`.  The monomials with zero `e_4` exponent form a basis of
`U`, so `dim U=binom(5,3)=10` and `dim(V/U)=10`.

The proposed factors are

```
X_1 = [[ 2,  0,  0, -1], [ 1,  0,  0, -2],
       [ 1, -1,  1,  0], [-1, -1,  1, -3]],
X_2 = [[ 2,  1,  2,  2], [ 0, -2,  2, -1],
       [-2, -1,  2, -1], [ 2,  1, -2, -2]],
X_3 = [[ 1,  1,  0,  0], [ 1,  1,  0,  1],
       [ 2,  1, -2,  1], [-2, -2, -1,  0]].
```

Their traces are respectively `0,0,0`; hence they lie in `sl_4(C)`.  With
`m_1=I_V` and `m_2=rho(X_1)rho(X_2)rho(X_3)`, the operator convention makes
`X_3` act first.  Therefore both operators belong to the frozen monoid.

Let `pi:V -> V/U`.  In the ordered bases stated in
`evidence/resolution_argument.md`, direct use of

`rho(X)(e^a)=sum_{i,j} a_j x_ij e^(a-e_j+e_i)`

gives the displayed integer matrix for `pi m_2|_U`.  Its determinant is

`8412259151430144`,

which is nonzero.  Thus `pi m_2|_U` is an isomorphism and
`U+m_2U=V`.  Conversely, the image of a ten-dimensional space under any one
linear operator has dimension at most ten, so one monomial translate cannot
span the twenty-dimensional `V`.  The upper and lower bounds therefore both
equal two.

## Independent certificate checks

I performed the following checks from the frozen definitions and explicit
matrices.

1. Both supplied exact programs ran successfully.  The pure-Python program
   constructs and multiplies the three representation matrices and uses a
   fraction-free determinant.  The second program applies the three
   derivations directly to cubics and uses an exact integer determinant.  Both
   returned the same quotient and spanning determinant
   `8412259151430144`.
2. I separately rebuilt each image as a sparse dictionary of exponent tuples,
   applying the factors in the order `X_3,X_2,X_1`, without constructing the
   supplied representation matrices.  I then used rational Gaussian
   elimination on the freshly constructed `10 x 10` quotient matrix.  This
   again returned the exact integer `8412259151430144`.  The compact JSON
   serialization of that independently reconstructed matrix has SHA-256
   `4b4186e8f53592ffddd50a8448cf0ff7c8dc0658783538aecc48c60f4c126d95`.
   As additional exact nonvanishing checks, the determinant residues modulo
   `101`, `1009`, and `10007` were `29`, `146`, and `7746`, respectively.
3. The first and last reconstructed rows agree with the displayed certificate:
   `[12,2,-10,12,0,-11,16,-12,20,24]` and
   `[0,4,-2,-6,-28,-13,-6,-6,-9,-21]`.  The basis has 20 distinct cubic
   exponent tuples, split into 10 tuples in `U` and 10 quotient tuples.

These computations are exact; no floating-point rank decision is used.

## Quantifier, convention, and source attacks

- The certificate supplies actual matrices rather than a generic-existence or
  bounded-search assertion.  All three factors satisfy the tracelessness
  hypothesis, and the product order used by every check matches the frozen
  right-to-left operator convention.
- The quotient determinant proves the full quantified spanning assertion, not
  merely independence inside a sampled subspace.  There is no division by a
  parameter, limiting argument, compactness step, or unexamined equality case.
- Degenerate monoid elements do not affect the lower bound: every linear image
  of `U`, including a singular or zero one, still has dimension at most 10.
  The identity is explicitly permitted as the empty product.
- The attached primary source, arXiv:2609.03882v1 dated 3 September 2026,
  defines the relevant monomial diameter on PDF page 29, proves the `n=3`
  symmetric-power family in Theorem 8.1, and asks the all-`n,k` higher-rank
  formula in Question 8.5 on PDF page 32.  The frozen result is the single
  specialization `n=4,k=3`, for which the proposed formula is 2.  The claim
  expressly makes no worldwide priority assertion; this review establishes
  the comparison with the frozen cited source, not an exhaustive literature
  search.

## Gaps and verdict

I found no mathematical gap in the frozen claim.  The exact certificate proves
the original fixed-cell existence statement in full, the dimension argument
proves optimality, and the stated scope matches the original frozen problem.
The source comparison supports the claimed delta at its deliberately bounded
scope.

**Verdict: accept.**
