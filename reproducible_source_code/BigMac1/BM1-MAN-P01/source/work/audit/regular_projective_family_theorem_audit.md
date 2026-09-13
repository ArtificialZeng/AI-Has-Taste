# Referee audit: regular projective polygon `F_A` theorem

## Verdict

PASS: 0 fatal, 0 major, 0 minor mathematical findings.

## Statement and scope

The audited statement concerns only the family

`A_n[i,j]=cos(pi(i-j)/n)`, `n>=3`.

It asserts an exact permanent and the complete spectrum of the associated
`F_A`.  It does not claim the full real conjecture, the full real rank-two
case, or a finite-dimensional exclusion through order 15.

## Line-by-line checks

1. **PSD and rank.**  The displayed vectors in `R^2` have Gram matrix `A_n`.
   The first two non-collinear vectors show rank exactly two.
2. **Symmetric-tensor normalization.**  Expansion in a normalized basis of
   `Sym^m(C^2)` gives the factor `m!/2^m` and the reciprocal binomial weight.
3. **Full permanent.**  For the complete set of `n`th roots of unity, only
   elementary symmetric coefficients `e_0` and `e_n` survive, giving
   `n!/2^(n-1)`.
4. **Deleted-root identity.**  The recursion
   `e_k(all)=e_k(excluding i)+q_i e_(k-1)(excluding i)=0` yields
   `e_k(excluding i)=(-q_i)^k` for every `0<=k<=n-1`.
5. **Phase and reality.**  The deleted row/column phase is
   `exp(i(theta_j-theta_i))`.  Pairing `k` with `n-1-k` and using
   `exp(2in delta)=1` proves the minor expression is real; no unjustified
   numerical real-part operation is used.
6. **Formation of `F_A`.**  Multiplication by `cos(delta)` and the exact
   product-to-sum identity give the claimed circulant first row.
7. **Fourier spectrum.**  The coefficient at frequency `s` is
   `c_s+c_(s-1)`, with `c_k=1/binom(n-1,k)`, and symmetry removes the apparent
   factor-of-two ambiguity in the cosine transform.
8. **Top eigenvalue.**  The constant mode has coefficient 2.  Every other
   mode has strictly smaller coefficient; the maximum nonconstant modes are
   `s=1,n-1`, giving ratio `n/(2(n-1))`.
9. **Nontriviality.**  The cycle of consecutive Gram lines has positive
   adjacent signs except for its closing edge, so its sign product is
   negative.  Therefore no diagonal sign switching makes every entry
   nonnegative.

## Independent definition-level reconstruction

`src/verify_regular_projective_family.py` imports no discovery code.  For
orders 3 through 8 it constructs `2A` in `Q[t]/(t^n+1)`, computes the full
permanent and every required minor by subset dynamic programming, then reduces
identities modulo the cyclotomic polynomial `Phi_(2n)`.  Formal Fourier
substitution returns exactly the theorem's integer-scaled spectrum.  Wrong
phase, wrong scale, and wrong-binomial attacks are all rejected.

The finite reconstruction is an audit of the general symbolic proof, not the
logical basis for extending a numerical pattern to all `n`.
