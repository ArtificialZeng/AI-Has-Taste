# Exact logarithmic threshold

## Theorem

In the probability model frozen in `source.md` and interpreted in
`problem.md`, for each fixed real `alpha`,

`Y_d -> 0` almost surely if and only if `alpha > 1/2`.

More precisely, for `epsilon > 0` and
`E_d(epsilon) = {|Y_d| > epsilon}`,

- if `alpha < 1/2`, then `sum_d P(E_d(epsilon))` diverges for every
  `epsilon > 0`;
- if `alpha = 1/2`, then that series converges exactly when `epsilon > 2`;
- if `alpha > 1/2`, then that series converges for every `epsilon > 0`.

Thus the endpoint `alpha = 1/2` is excluded.

## Spherical-coordinate tail lemma

Let `V_d` be one coordinate of a uniform point on `S^(d-1)` and put
`Z_d = sqrt(d) V_d`. Its density is

`h_d(z) = a_d (1-z^2/d)^((d-3)/2) 1_{|z|<sqrt(d)}`,

where

`a_d = Gamma(d/2)/(sqrt(pi*d) Gamma((d-1)/2))`.

Stirling's formula gives `a_d -> (2*pi)^(-1/2)`; in particular, `a_d` is
bounded above and bounded away from zero for all sufficiently large `d`.
Fix constants `c>0` and `gamma>0`, and set
`t_d=c(log d)^gamma`. Then

`P(|Z_d|>t_d) asymp t_d^(-1) exp(-t_d^2/2)`,                 (1)

where the two comparison constants may depend on `c,gamma` but not on `d`.

Here is a direct proof. Since `t_d` is polylogarithmic,
`t_d^2/d -> 0` and `t_d^4/d -> 0`. For `d>=4`,
`log(1-u) <= -u` gives

`P(|Z_d|>t_d)`
` <= 2 a_d integral_(t_d)^infinity exp(-(d-3)z^2/(2d)) dz`
` <= C t_d^(-1) exp(-t_d^2/2) exp(3t_d^2/(2d))`
` <= C' t_d^(-1) exp(-t_d^2/2)`.

For the reverse bound, integrate only over
`[t_d,t_d+1/t_d]` (eventually `t_d>=1`). On this interval, put
`u=z^2/d`. Eventually `u<=1/2`, and the elementary inequality
`log(1-u) >= -u-u^2` yields

`(1-z^2/d)^((d-3)/2) >= exp(-z^2/2-z^4/(2d))`.

Also `z^2 <= t_d^2+3` and `z^4/d=o(1)` throughout the interval. Its length
is `1/t_d`, and the lower bound on `a_d` now proves the reverse inequality
in (1).

If instead `t_d` remains bounded, then `P(|Z_d|>t_d)` is bounded below by
a positive constant whenever `t_d` is eventually bounded above: integrate
`h_d` over any fixed nonempty interval lying strictly above that upper bound.
The same density estimates make the resulting lower bound uniform in large
`d`.

## Classification of the probability series

Let `V_d=<U_1^(d),U_2^(d)>`. Rotational invariance gives the coordinate law
used above. The exact identity in `problem.md`, together with independence of
`X_d` from the directions, gives

`P(E_d(epsilon))`
` = d^(-1/2) P(sqrt(d)|V_d| > (epsilon/2)(log d)^alpha)`.    (2)

For `alpha<=0`, the threshold on the right of (2) is eventually bounded.
The final part of the tail lemma and the trivial upper bound therefore give

`P(E_d(epsilon)) asymp d^(-1/2)`,

so the series diverges.

Now suppose `alpha>0`. Apply (1) with
`t_d=(epsilon/2)(log d)^alpha`. Then

`P(E_d(epsilon)) asymp`
` d^(-1/2) (log d)^(-alpha)`
` exp(-(epsilon^2/8)(log d)^(2alpha))`.                    (3)

If `0<alpha<1/2`, the exponential factor is `d^(-o(1))`.
For example, it is eventually at least `d^(-1/4)`, while the logarithmic
factor is eventually at least `d^(-1/8)`. The lower bound in (3) then
dominates a constant multiple of `d^(-7/8)`, so the series diverges.

If `alpha>1/2`, then for every fixed `epsilon>0` the exponential factor in
(3) is eventually at most `d^(-1)`. The upper bound in (3) is then summable.

At `alpha=1/2`, (3) becomes the sharp comparison

`P(E_d(epsilon)) asymp`
` d^(-1/2-epsilon^2/8) (log d)^(-1/2)`.                    (4)

The standard power/logarithm series test shows that (4) is summable exactly
when `1/2+epsilon^2/8>1`, namely `epsilon>2`. At `epsilon=2` it is comparable
to `1/(d sqrt(log d))`, whose series diverges; it also diverges for every
`0<epsilon<2`.

## Almost-sure conclusion

For fixed `alpha`, the events `E_d(epsilon)` are independent over `d`, since
each is measurable with respect to the mutually independent triple
`(X_d,U_1^(d),U_2^(d))`.

If `alpha>1/2`, the first Borel--Cantelli lemma applied for every threshold
`epsilon=1/m`, `m>=1`, shows on one probability-one event that, for each
`m`, eventually `|Y_d|<=1/m`. Hence `Y_d->0` almost surely.

If `alpha<1/2`, take `epsilon=1`; if `alpha=1/2`, also take `epsilon=1`
(or any `epsilon<=2`). The corresponding series diverges, so the second
Borel--Cantelli lemma gives `|Y_d|>epsilon` infinitely often almost surely.
Consequently `Y_d` cannot converge to zero. This proves the theorem.

## Gap list

Empty. The proof uses only the exact model interpretation in `problem.md`,
the elementary spherical-coordinate density, and the two Borel--Cantelli
lemmas. No novelty or priority claim is made.
