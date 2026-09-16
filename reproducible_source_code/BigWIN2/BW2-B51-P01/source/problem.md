# Precise problem reading

## Frozen target

Work over `C`.  Put `W = C^4` with ordered basis
`e_1,e_2,e_3,e_4`,

`V = Sym^3(W)`, and `U = Sym^3(span(e_1,e_2,e_3)) <= V`.

Thus `V` has the monomial basis
`e_1^a e_2^b e_3^c e_4^d` with nonnegative integers
`a+b+c+d=3`, while `U` is the span of those basis monomials with
`d=0`.  Hence

`dim(V) = binom(6,3) = 20` and `dim(U) = binom(5,3) = 10`.

For `X=(x_ij) in sl_4(C)`, the derived natural action is

`rho(X)(e_1^a e_2^b e_3^c e_4^d)
 = sum_{i,j=1}^4 x_ij e_i partial/partial(e_j)
   (e_1^a e_2^b e_3^c e_4^d)`.

Here `sl_4(C)` means all `4 x 4` complex matrices of trace zero.  Define

`mon(rho(sl_4(C))) = {I_V} union
 {rho(X_1)...rho(X_r) : r>=1 and every X_i in sl_4(C)}`.

The displayed multiplication order is operator order: in
`rho(X_1)...rho(X_r)v`, the factor `rho(X_r)` acts first.

The quantified question is exactly:

> Does there exist an integer `r_1>=0`, an integer `r_2>=0`, and traceless
> complex matrices `X_{1,1},...,X_{1,r_1},X_{2,1},...,X_{2,r_2}` such that,
> for `m_i=rho(X_{i,1})...rho(X_{i,r_i})` (with the empty product equal to
> `I_V`), one has `m_1 U + m_2 U = V`?

A positive answer requires an explicit exact certificate: the factors and their
order, a fixed basis, and a nonzero exact determinant of the `20 x 20` matrix
whose columns are the images under `m_1,m_2` of a basis of `U`.  A negative
answer requires a proof that every such pair has sum of rank at most `19`.

Since each `m_i U` has dimension at most `10`, one summand cannot span the
20-dimensional `V`.  Therefore existence of such a pair is equivalent to
`diam_+^{sl_4(C),mon}(V,U)=2`, the `(n,k)=(4,3)` cell of Question 8.5.  It does
not settle any other `(n,k)` cell or the universal question.

## Source status and nearest prior result

The source status at triage is **open-supported in the cited source, with a
positive exact certificate found during this triage but not yet refereed**.
Jezernik--Spenko, arXiv:2609.03882v1 (submitted 2026-09-03), defines the
monomial diameter on PDF p. 29, proves in Theorem 8.1 (PDF pp. 30--32) the
analogous optimal formula for `sl_3(C)` on `Sym^k(C^3)` relative to a plane,
and asks the formula for all `n>=3,k>=1` in Question 8.5 (PDF p. 32).
The earlier arXiv:2504.07573v2, Question 6.6, asks whether all irreducible
representations have optimal monomial Lie-additive diameters.  Exact-assertion
and equivalent-phrase web searches on 2026-09-07 found no separate primary
source treating this fixed `(4,3)` cell; this is a bounded search result, not a
claim of priority.

Nearest prior result `X`: Theorem 8.1 for ambient dimension `n=3` and every
degree `k`.  Proposed delta `Y`: decide the first fixed higher-rank cubic cell
`(n,k)=(4,3)`.  Verification route `Z`: reproduce the exact determinant in
`evidence/triage_exact_certificate.py`, then have a fresh referee audit the
action convention, multiplication order, and determinant independently.
