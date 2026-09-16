# Fresh mathematical referee report

Verdict: **accept** the exact frozen `result-note` scope.  The argument proves
eventual strict positivity for each of the two charged-core series.  It does
not prove positivity in every degree, and therefore leaves the original
Gerber--Norton `e=6` problem unresolved, exactly as `claim.json` states.

## Frozen scope and integrity

I reviewed the statement in `claim.json` against the snapshot with digest
`b7c5d42b73c68f8c73938516bd64f3e6bf60a13c94764f8cd4b27f99aeb4fd56`.
Fresh SHA-256 calculations matched every digest in `audit/snapshot.json`.
The literal inequalities in immutable `source.md` are non-strict, while
`problem.md` records the source-backed strict-positivity correction.  The
candidate does not purport to resolve either reading silently: it is expressly
a partial theorem for the strict problem, namely finiteness of the exceptional
degrees.

## Reconstruction of the lattice identity

For the paper's level-rank map at source level two and `e=6`, write a source
position as `k=6m+r`, with `1<=r<=6`.  A bead in source row 1 maps to column
`2m+2` of target row `r`, and a bead in source row 2 maps to column `2m+1`.
The empty target row of charge `t_r` has every column at most `t_r` occupied.
Thus its inverse has residue cutoffs

```
M_{1,r}=floor((t_r-2)/2),   M_{2,r}=floor((t_r-1)/2).
```

Writing uniquely `t_r=2u_r+eps_r`, with `eps_r` binary, gives
`M_{1,r}=u_r-1` and `M_{2,r}=u_r+eps_r-1`.  The charge of a six-residue cutoff
row is `sum_r(M_r+1)`.  Consequently the inverse has charge `(0,a)` exactly
when

```
sum_r u_r=0,   sum_r eps_r=a.
```

This is a genuine bijective parameterization: Gerber--Norton Definition 2.8
identifies charged `6`-cores with inverse images of empty six-partitions under
level-rank duality, and their equation (2.1) preserves total charge.

For a cutoff `M` in residue `r`, the regularized beta-set energy is
`(M+1)(3M+r)`.  A beta set of charge `s` has energy
`|lambda|+s(s+1)/2`.  Substitution in the two rows yields exactly

```
Q_eps(u) = sum_r (6u_r^2 + 2(r-3)u_r
                   + eps_r(6u_r+r)) - a(a+1)/2.
```

Hence the coefficient of `q^n` counts the pairs `(u,eps)` satisfying the two
displayed constraints and `Q_eps(u)=n`.  This also confirms that different
cosets are combined with their correct multiplicities.

As a second algebra check, set `d=(-2,-1,0,1,2,3)` and
`x=6u+3eps+d`.  Then `sum x_r=3(a+1)` and direct expansion gives

```
sum x_r^2 = 6 Q_eps(u) + C_a,   C_1=16, C_3=28.
```

After centering by `(a+1)/2` times the all-ones vector, the relevant integral
coset is

```
M+v_eps,  M=6A_5,  Q(y)=sum y_r^2,  sum y_r=0,
```

and

```
Q(6u+v_eps)=6Q_eps(u)+D_a,   D_1=10, D_3=4.
```

The four displayed shift vectors in the provenance note are integral, have
coordinate sum zero, and agree with this formula.

## Local representation checks

Eliminate `u_6=-sum_{i=1}^5 u_i`.  At every prime `p>=5`, the homogeneous
quadratic matrix is `6(I_5+J_5)`, whose determinant is `6^6`; it is therefore
nondegenerate modulo `p`.  After completing the square, a nondegenerate
five-variable quadratic form over `F_p` contains a hyperbolic plane and
represents every residue, including zero at a nonsingular nonzero isotropic
vector.  Multivariable Hensel lifting consequently makes every fixed
`Q_eps` universal over `Z_p`.

At `p=3`, direct differentiation gives

```
partial Q_eps / partial u_i
 = 12(u_i-u_6)+2(i-6)+6(eps_i-eps_6)
 = 2i (mod 3).
```

Thus the reduction is a surjective affine function and at least one partial
derivative is a unit, so every 3-adic target lifts.

For `p=2`, put
`C_eps=sum r eps_r-a(a+1)/2`, so `Q_eps=C_eps+2F_eps` with integral
`F_eps`.  Its reduced gradient is the constant vector

```
(i+eps_i+eps_6)_{i=1}^5 (mod 2).
```

For the four selected cosets this vector is nonzero.  Therefore `F_eps`
represents both residues modulo 2 with a unit partial derivative and lifts to
every element of `Z_2`.  The selections

```
a=1: eps={1} for even n, eps={2} for odd n;
a=3: eps={1,2,3} for even n, eps={1,2,4} for odd n
```

have `C_eps` of the stated parity.  Thus, for every nonnegative integer `n`,
the parity-selected fixed coset represents `6n+D_a` at every finite place.
At the real place the five-dimensional positive-definite ambient space
represents every positive real target.  These statements are precisely genus
representation in Chan--Oh's Definition 4.1 and the definition immediately
above Corollary 4.8.

## Global theorem and quantifiers

I checked the cited primary PDF directly.  Chan--Oh Theorem 4.9(1) applies to
an integral coset on a positive-definite quadratic space over a totally real
field, assumes genus representation, and in dimension at least five gives
representation by the fixed coset once the field norm of the nonzero target
exceeds a coset-dependent constant.  It has no primitive-representation
hypothesis; that additional hypothesis occurs only in part (2).

Here `F=Q`, `o=Z`, `M=6A_5` is free of rank five, the shifts are integral,
and the targets `6n+10` or `6n+4` are positive nonzero integers tending to
infinity.  Applying the theorem separately to the even- and odd-`n` cosets for
each charge, then taking the maximum of the four constants, yields integers
`N_1,N_3` such that `Q_eps(u)=n` has an integral solution for the selected
coset whenever `n>=N_a`.  Via the exact level-rank bijection this proves
`c_{6,(0,a)}(n)>0` for all `n>=N_a`.

There is no illicit exchange of limits or inference from finite computation:
the finite calculations only audit the identities.  I reran
`parity_coset_local.py`, which confirmed the four coset choices modulo 32 and
27 and the parity gradients, and reran `level_rank_lattice.py` through degree
40, obtaining exact agreement with the independent nested-beta enumeration.
The all-orders conclusion instead comes from the proved local statements and
Chan--Oh Theorem 4.9(1).

## Source comparison, contribution, and remaining gap

The Gerber--Norton PDF states that the two individual `e=6` series are only
"conjecturally yes" and reports computer support; equation (5.3) controls only
their weighted sum.  The accepted theorem is a nontrivial strict refinement:
it rules out infinitely many exceptional degrees and reduces the original
problem to a finite, currently ineffective range.  This is useful progress on
the exact source question rather than a toy restriction or routine consequence
of equation (5.3).  The candidate makes no priority claim.  Within the frozen
source set, Gerber--Norton is the nearest stated result and Chan--Oh supplies
the asymptotic local-to-global input.

The unresolved gap is explicit and substantive: Chan--Oh's constant is not
made effective here, so the computation through degree 100 cannot be joined
to the asymptotic theorem to settle all degrees.  No value of `N_a` is claimed.
This gap prevents a resolution-paper verdict but does not affect the exact
finite-exception theorem submitted as a result-note.

**Final verdict: accept.**
