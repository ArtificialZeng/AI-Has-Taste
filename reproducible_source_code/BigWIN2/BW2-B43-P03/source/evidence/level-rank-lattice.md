# Exact level-rank lattice description for the two `e=6` series

This note records an exact reformulation, not a proof of strict positivity in
every degree.  It uses the level-rank map in Section 2.2 and the fact after
Definition 2.8 of Gerber--Norton that an `e`-core is carried to the empty
`e`-partition with some charge.

## Inverting level-rank duality

Write a source position as `k=6m+r`, where `1<=r<=6`.  For source level two,
the paper's map

`(k,j) -> (2(floor((k-1)/6)+1)-j+1, (k-1) mod 6+1)`

sends this position in row `j` to row `r` and to column `2m+2` for `j=1`, or
column `2m+1` for `j=2`.  The beta set in row `r` of the empty six-partition
with charge `t_r` consists of all columns at most `t_r`.  Consequently, the
two beta sets of its inverse image have the exact descriptions

```
B_1(t) = union_{r=1}^6 {6m+r : m <= floor((t_r-2)/2)},
B_2(t) = union_{r=1}^6 {6m+r : m <= floor((t_r-1)/2)}.
```

For a set `B={6m+r:m<=M_r}`, its charge is `sum_r(M_r+1)`: the charge-zero
vacuum has cutoff `M_r=-1` in every residue.  Write uniquely

`t_r=2u_r+eps_r`, with `u_r in Z` and `eps_r in {0,1}`.  The charges of
`B_1(t),B_2(t)` are then

`(sum_r u_r, sum_r u_r + sum_r eps_r)`.

It follows that the empty six-row charge vectors which map back to source
charge `(0,a)`, for `a=1` or `3`, are **exactly**

```
t_r=2u_r+eps_r,   sum_r u_r=0,   sum_r eps_r=a.
```

Equivalently, `sum_r t_r=a`, with exactly `a` odd coordinates.  This is a
bijection because level-rank duality is a bijection and its empty-six-row
abaci are exactly the six-cores.

## Exact size formula

For the same cutoff beta set, define its regularized energy by positive beads
minus nonpositive holes.  The contribution of residue `r` is

`F_r(M_r)=(M_r+1)(3M_r+r)`

for every integer cutoff `M_r`.  For a beta set of charge `s`, this energy is
`|lambda|+s(s+1)/2`; this follows either by moving its beads from the vacuum,
or directly from `beta_i=lambda_i-i+1+s`.  Substitution of the two cutoff
vectors above gives

```
Q_a(u,eps)
 = sum_{r=1}^6 [6u_r^2 + 2(r-3)u_r + eps_r(6u_r+r)]
   - a(a+1)/2,
```

on `sum u_r=0`, `sum eps_r=a`.  Therefore the exact theta decomposition is

```
c_{6,(0,a)}(q)
 = sum_{eps in {0,1}^6, sum eps=a}
     sum_{u in Z^6, sum u=0} q^{Q_a(u,eps)}.                 (LR)
```

Each of the `binomial(6,a)` inner sums is a theta series of a translate of a
positive-definite rank-five `A_5` lattice.  Formula (LR) makes nonnegativity
manifest, but it does **not** make strict positivity in every degree manifest:
one must still prove that the union of the cosets represents every natural
number.

There is also a six-square form useful for the remaining representation
problem.  Put

`x_r=3t_r+r-3=6u_r+3eps_r+r-3`.  Then

```
sum_r x_r = 3(a+1),
sum_r x_r^2 = 6Q_a(u,eps)+C_a,
C_1=16,  C_3=28,
x_r == r-3 (mod 3),
#{r : x_r-(r-3) is odd}=a.
```

Thus strict positivity is equivalent to solving this constrained six-square
system for every right-hand side `6n+C_a`.  This equivalence is only to the
strict source-backed target in `problem.md`, not to the literal automatic
nonnegative reading in the immutable `source.md`.

## Reproducible checks and limitations

`level_rank_lattice.py` enumerates (LR) with an exhaustive coordinate bound
coming from the six-square identity.  It also reconstructs both partitions,
checks their total size and the nested beta-set criterion, and compares with
the independent bipartition enumeration in `exact-coefficients-n40.txt`.
The saved run in `level-rank-lattice-n100.txt`:

- agrees coefficientwise with the earlier nested-beta enumeration for
  `0<=n<=40` for both charges;
- has no zero coefficient for either series for `0<=n<=100`;
- exhaustively finds every residue class modulo every `m` with `2<=m<=24`
  among values of each `Q_a` (using `u` modulo `m`).

The last item rules out only a periodic congruence obstruction with one of
those moduli.  It is not a local-global theorem and gives no all-orders
positivity result.

