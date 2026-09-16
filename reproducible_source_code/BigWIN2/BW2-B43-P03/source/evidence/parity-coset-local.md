# Affine parity-cosets and exact local representation

This note continues the exact level-rank reformulation in
`level-rank-lattice.md`.  Its new arithmetic calculation is local; the final
section combines it with a cited asymptotic coset theorem.  It does not prove
that every nonnegative integer is represented over the ordinary integers.

For `a in {1,3}`, fix a binary vector `eps` of weight `a`, put

```
Q_eps(u)=sum_r [6u_r^2+2(r-3)u_r+eps_r(6u_r+r)]-a(a+1)/2,
sum_r u_r=0,
```

and write `d=(-2,-1,0,1,2,3)`.  The target series is the sum of these
six or twenty coset theta series.

## Full affine-isometry reduction

With `x_r=6u_r+3eps_r+d_r`, the domain is the coset

```
b_eps + 6 A_5  in  {sum x_r=3(a+1)},
b_eps,r=3eps_r+d_r,
```

and `6Q_eps=sum x_r^2-C_a`.  Centering the affine hyperplane identifies
the full norm-preserving affine group of its translation lattice with
`Aut(A_5)=+-S_6`.  A coordinate permutation identifies two cosets exactly
when the multisets of their `b` residues modulo 6 agree.  Central negation
acts on those residues by `z -> a+1-z (mod 6)`.  Therefore the sorted residue
multiset, modulo this reflection, is a complete affine-isometry invariant.

The exact enumeration in `parity_coset_local.py` gives 4 orbits for `a=1`,
of multiplicities `2,1,2,1`, and 10 orbits for `a=3`, of multiplicities
`2,2,4,1,1,4,2,2,1,1`.  The output lists every member and its fixed value
parity.  This is the requested symmetry reduction, but the orbits are cosets,
so ordinary lattice genus software cannot silently be applied without its
shift/conductor data.

## Odd-prime universality of every fixed coset

Eliminate `u_6` using `u_6=-sum_{i=1}^5 u_i`.  For every prime `p>=5`,
the quadratic part has matrix

```
6(I_5+J_5),  with determinant 6^6,
```

so it is nondegenerate over `F_p`.  After completing the square, a
nondegenerate quadratic form in five variables over `F_p` represents every
field element at a nonsingular point: it contains a hyperbolic plane (use a
nonzero isotropic vector in dimension at least three), and the zero value also
has a nonzero isotropic representative.  Ordinary multivariable Hensel
lifting then proves that every `Q_eps` represents every element of `Z_p`.

At `p=3`, the derivative with respect to `u_i`, after eliminating `u_6`, is

```
dQ_eps/du_i = 12(u_i-u_6)+2(d_i-d_6)+6(eps_i-eps_6)
             == 2i (mod 3).
```

In particular a derivative is always a 3-adic unit.  The reduction modulo 3
is a nonconstant affine function, so it represents all residues, and Hensel
lifting again proves `Z_3`-universality for every fixed coset.

## Exact dyadic coverage and a two-coset reduction

Let

```
C_eps=sum_r r eps_r-a(a+1)/2.
```

Then `Q_eps=C_eps+2F_eps` for an integral quadratic polynomial `F_eps`.
After eliminating `u_6`, its gradient satisfies

```
dF_eps/du_i == i+eps_i+eps_6 (mod 2),  1<=i<=5.
```

Unless this five-vector vanishes, `F_eps mod 2` is a nonconstant affine
function and hence represents both residues.  Adjusting a coordinate with
unit derivative gives a solution modulo every higher power of 2.  Thus such
a coset represents **every** 2-adic integer congruent to `C_eps mod 2`.
The gradient vanishes only for the two `a=3` patterns `{1,3,5}` and
`{2,4,6}`; there are no singular patterns for `a=1`.

Consequently the all-prime local problem reduces to two explicit cosets for
each charge:

| charge | even target | odd target |
|---|---|---|
| `a=1` | `eps={1}` | `eps={2}` |
| `a=3` | `eps={1,2,3}` | `eps={1,2,4}` |

For each integer `n`, choose the coset in its parity column.  The equation
`Q_eps(u)=n` is then soluble over `Z_p` for every prime `p`: odd-prime coverage
was proved above and dyadic coverage follows from the table.  Equivalently,
after the centering below, that same coset locally represents its norm target
`6n+D_a` at every finite place.  At the real place the target is positive and
the five-dimensional ambient quadratic space represents every positive real
number.  Hence **there is no local obstruction, and the genus of the selected
shifted `A_5` coset represents `6n+D_a`**.  This does not identify an integral
vector in the selected coset.

The script exhaustively checks the orbit bookkeeping, all predicted residues
modulo 32 and 27 for representative nonsingular cosets, and the parity identity
on a finite box.  Those computations audit the formulas; the derivative and
finite-field arguments above supply the all-orders local proof.

## Consequence: both series are almost strictly positive

Center the affine hyperplane by putting

```
y=x-(a+1)/2*(1,1,1,1,1,1).
```

The selected domain is now an integral coset `L+v_eps` in the positive
definite five-dimensional space `sum y_r=0`, where `L=6A_5` and the quadratic
map is `Q(y)=sum y_r^2`.  Here `v_eps` has integral coordinates and coordinate
sum zero, so `L+v_eps` is a free integral `Z`-coset of rank five.  The norm
target equivalent to `Q_eps(u)=n` is

```
sum y_r^2 = 6n+D_a,   D_1=10, D_3=4.
```

Chan--Oh, *Representations of integral quadratic polynomials*,
arXiv:1208.6060v1, Theorem 4.9(1), states that if a nonzero target is
represented by the genus of an `o`-coset on a positive-definite quadratic
space over a totally real number field and the coset has dimension at least
five, then that target is represented by the fixed coset once its field norm
is larger than a constant depending only on the coset.  The frozen primary
source is `bigWin-43-materials/1208.6060.pdf`; exact definitions, locator, and
hypothesis mapping are recorded in
`evidence/chan-oh-theorem-4.9-provenance.md`.

Apply that theorem over `F=Q`, `o=Z` separately to the four explicit cosets in
the parity table.  The all-place argument above says that the positive integer
`6n+D_a` is represented by the genus of the coset selected by the parity of
`n`.  Its field norm is itself and tends to infinity.  Taking the maximum of
the four Chan--Oh constants proves:

> For each `a in {1,3}`, there is an (ineffective here) integer `N_a` such that
> `c_{6,(0,a)}(n)>0` for every `n>=N_a`.

Thus both series are **almost strictly positive**, and any zero coefficients
form a finite set.  In particular, no infinite spinor-exception square class
can obstruct either target union.  This does not prove the original all-degree
claim: Theorem 4.9 does not give a usable value of `N_a`, and the exact finite
enumerator has so far certified only `0<=n<=100`.  Determining an effective
cutoff, or replacing the asymptotic theorem by an explicit universal-coset
argument, is the remaining global gap.
