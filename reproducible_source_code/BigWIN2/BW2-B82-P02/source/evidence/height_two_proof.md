# Height-two injectivity: exact proof dossier

Provenance: `win-00082-p02-research-dbf7b6159313` (research pass 1,
2026-09-09).

## Theorem (scope frozen by `source.md`)

For every integer `g >= 3` and every `N >= 1`, the polynomial
`Psi_{H,g}` distinguishes rooted trees on `N` vertices whose root height is at
most two.

## Normal form

For `N >= 2`, remove the root.  Its `r` components are rooted stars.  Write
their orders as `b_1,...,b_r`, and put `d_i=b_i-1`.  Thus `d_i` is the number
of leaves at depth two in branch `i`,

\[
 b_i\geq 1,\qquad d_i\geq0,\qquad \sum_i b_i=N-1.
\]

The multiset of branch orders determines and is determined by the rooted
isomorphism type.

## Coefficient-extraction lemma

For `0 <= k <= floor((N-1)/2)`, set

\[
 A_k=[z_gz_2^kz_1^{N-1-2k}]\Psi_{H,g}.
\]

Then

\[
 A_k=e_k(d_1,\ldots,d_r).
\tag{1}
\]

Also, for `N >= 2`,

\[
 B=[z_{g+1}z_1^{N-2}]\Psi_{H,g}=r.
\tag{2}
\]

### Proof of (1)

In every summand of `Psi`, the factor contributed by the root component has
subscript `g-1+|R_J|`, which is at least `g`.  The target monomial in (1) has
only subscripts `1`, `2`, and `g`; because `g >= 3`, its root-component factor
must therefore be exactly `z_g`.  Hence `|R_J|=1`: every edge incident with
the root is absent.

Consider the detached star in branch `i`.  If exactly `q` of its `d_i` leaf
edges are selected, its center component has order `q+1`, while each
unselected leaf is a singleton.  The target monomial permits only nonroot
component orders one and two, so `q` must be zero or one.  A branch with
`q=1` contributes one component of order two and the selected leaf edge can
be chosen in exactly `d_i` ways.  Consequently a forest contributing the
target monomial is specified uniquely by a set `S` of `k` branches and one
of the `d_i` leaf edges in every branch `i in S`.  Its count is

\[
 \sum_{|S|=k}\prod_{i\in S}d_i=e_k(d_1,\ldots,d_r),
\]

including `k=0`, where the empty forest is the unique contributor.  This
also proves there are no hidden monomial collisions.

### Proof of (2)

The target monomial in (2) has only the subscripts `1` and `g+1`.  Its root
factor, whose subscript is at least `g`, must be `z_{g+1}`.  The root
component therefore has order two.  All other components are singletons, so
the selected edge set consists of exactly one edge incident with the root.
Conversely, each of the `r` root edges selected alone gives the target
monomial.  Thus its coefficient is `r`.

## Reconstruction

Let `m` be the number of positive `d_i`.  Every such branch has order at
least two, so

\[
 m\leq\left\lfloor\frac{N-1}{2}\right\rfloor.
\]

It follows from (1) that all coefficients, including the leading nonzero
one, of

\[
 Q_H(t)=\sum_{k=0}^{\lfloor(N-1)/2\rfloor}A_kt^k
       =\prod_{i=1}^r(1+d_it)
\tag{3}
\]

are available from `Psi`.  The nonconstant linear factors of this normalized
integer polynomial recover the multiset of positive `d_i` uniquely (equivalently,
its nonzero-factor roots, with multiplicity, are `-1/d_i`).  Equation (2)
recovers `r`, so appending `r-m` zeros recovers the full multiset
`{d_1,...,d_r}`.  Adding one recovers `{b_1,...,b_r}`, hence the rooted tree.

If two polynomials in the frozen claim are equal, all the displayed
coefficients agree and the reconstruction gives the same branch-order
multiset.  For `N=1`, there is only the one-vertex rooted tree (and
`Psi=z_g`), so the assertion is immediate.  This proves the theorem for all
quantified parameters.

## Exact finite audit (not used as proof)

`evidence/audit_height_two.py` independently constructs every height-two
rooted type from every integer partition of `N-1`, enumerates every subset of
the `N-1` graph edges, computes forest components by union-find, and builds
`Psi` from the definition.  It does not use (1) or (2) to obtain the tested
coefficients.  Its committed run covers every `1 <= N <= 14` and every
`3 <= g <= 14`: 373 rooted types, 1,324,435 edge subsets, 26,952 checks of
(1), 4,464 checks of (2), and 4,476 complete-polynomial injectivity checks.
All pass; see `evidence/audit_height_two.json`.

Reproduction command:

```text
python3 evidence/audit_height_two.py --max-n 14 --max-g 14
```

## Dependencies and gap list

Dependencies: only the definition in `source.md`, elementary component
counting in a forest, and uniqueness of factorization for one-variable
polynomials.  Known proof gaps: none.  The computation is corroboration over
a declared finite range and is not invoked to extend the proof beyond it.
