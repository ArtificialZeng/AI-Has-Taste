# Precise problem: exact reverse LCD-LP comparison at `(20,8)`

## Frozen target and status

The immutable input is `source.md` (SHA-256
`0e7fc6f0cd8d29cc431c9bcebf012475d8f6e821a88b9df7c8f421e772bee113`).
Its three mathematical claims, read conjunctively but to be decided separately, are

1. `G_2(20,8,7) != empty`;
2. `M_2(20,8,7) = empty`;
3. `M_2(20,8,6) != empty`.

Here “empty/nonempty” concerns real LP feasible regions, not binary codes. The
named paper reports the associated `(20,8): 7 -> 6` comparison only as a
floating-point screening observation and expressly excludes it from its exact
endpoint claims. Thus the exact conjunction above is not established by the
inspected source. It is treated as a status-uncertain certification problem, not
as a verified open problem or a novelty claim.

## Common notation and baseline

All variables below are real. For `0 <= j,w <= 20`, put

\[
 K_j(w)=\sum_{\ell=0}^j(-1)^\ell
 {w\choose\ell}{20-w\choose j-\ell},
\]

with a binomial coefficient equal to zero outside its natural range. The binary
Hamming LCD baseline in variables `A_0,...,A_20,B_0,...,B_20` is

\[
A_0=B_0=1,\qquad A_w,B_w\geq0,
\]
\[
A_w=0\quad(1\leq w<d),
\]
\[
2^8B_j=\sum_{w=0}^{20}A_wK_j(w)\quad(0\leq j\leq20),
\]
\[
A_w+B_w\leq {20\choose w}\quad(1\leq w\leq20).
\]

The symbols `A_w,B_w` are LP pseudo-weight distributions; integrality is not
imposed.

## Meaning of `G_2(20,8,d)`

For a parity type `tau` in `{O,E}`, define

\[
\Delta_O(8)=0,\qquad \Delta_E(8)=2^8,
\]

and phase sets `B_O(8)={0,2,4,6}` and `B_E(8)={0,4}` in `Z/8Z`.
The dual dimension is `12`, with the same displayed phase sets. For a phase
`beta`, let `(r_beta,i_beta)` for `beta=0,...,7` be

\[
(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),
\]

and let `s_beta=2^4=16` for the even phases used here, so
`R_beta=16r_beta` and `I_beta=16i_beta`.

A branch `(tau,beta,eta)` has `eta` in `{0,1}` and dual parity type `E` if
`eta=1`, otherwise `O`. It is admissible precisely when `(tau,tau_perp)` is
not `(E,E)` and `(20-beta) mod 8` belongs to `B_{tau_perp}(12)`. At `(20,8)`
the eight admissible branches are

\[
(O,0,0),(O,2,0),(O,4,0),(O,6,0),
(O,0,1),(O,4,1),(E,0,0),(E,4,0).
\]

In an admissible branch, impose the common baseline, `A_20=eta`, and

\[
\sum_{w\equiv0\ (4)}A_w=
\frac{2^8+\Delta_\tau(8)+2R_\beta}{4},
\]
\[
\sum_{w\equiv1\ (4)}A_w=
\frac{2^8-\Delta_\tau(8)+2I_\beta}{4},
\]
\[
\sum_{w\equiv2\ (4)}A_w=
\frac{2^8+\Delta_\tau(8)-2R_\beta}{4}.
\]

`G_2(20,8,d)` is the union of these eight branch feasible regions. Therefore
claim 1 has the exact quantifier form: there exist one admissible branch and
rational values for all 42 `A,B` variables satisfying every displayed row with
`d=7`. A rational point is requested even though ordinary nonemptiness is over
the reals.

## Meaning of `M_2(20,8,d)`

Let

\[
I_{20}=\{(a,b,c,e)\in\mathbb Z_{\geq0}^4:a+b+c+e=20\}.
\]

Besides baseline variables `A_w,B_w`, introduce `M_{a,b,c,e}` for every index
in `I_20`. These variables represent the four coordinate-state counts
`00,01,10,11` in a joint enumerator, but remain nonnegative real LP variables.
Impose

\[
M_{a,b,c,e}\geq0,
\]
\[
M_{a,b,c,e}=0\quad\text{if }e\text{ is odd},
\qquad
M_{a,b,c,e}=0\quad\text{if }1\leq c+e<d,
\]
\[
M_{a,0,0,e}=0\quad(e>0),
\]

and, for every `0 <= w <= 20`,

\[
M_{20-w,w,0,0}=B_w,\qquad M_{20-w,0,w,0}=A_w,
\]
\[
\sum_{c+e=w}M_{a,b,c,e}=2^{12}A_w,
\qquad
\sum_{b+e=w}M_{a,b,c,e}=2^8B_w,
\]

where each sum ranges over `I_20`. For every `0 <= j <= 20`, also impose

\[
\sum_{b+c=j}M_{a,b,c,e}={20\choose j}.
\]

Finally set

\[
J(x_0,x_1,x_2,x_3)=\sum_{I_{20}}M_{a,b,c,e}
x_0^ax_1^bx_2^cx_3^e
\]

and require the polynomial identity

\[
J(x)=2^{-20}J(H_4x),\qquad
H_4=\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix}.
\]

This means equality of every degree-20 monomial coefficient; after multiplying
by `2^20`, it is an exact integer linear system obtained by multinomial
expansion. The resulting feasible region is `M_2(20,8,d)`.

Thus claim 2 quantifies universally: no real assignment satisfies all mixed rows
at `d=7`. Claim 3 quantifies existentially: a rational assignment satisfies all
mixed rows at `d=6`. Because increasing `d` only adds zero constraints, claims 2
and 3 together make the mixed LP endpoint exactly 6. They do not assert the
existence or nonexistence of an LCD code. Claim 1 alone likewise does not certify
an exact Gauss endpoint without a separately verified upper exclusion.

## Required exact decision evidence

For each asserted nonempty region, provide a complete rational feasible point.
For asserted emptiness, provide a rational or integer Farkas multiplier whose
row combination has zero left-hand side and a contradictory right-hand side
under a stated canonical equality/inequality convention. Check every witness or
multiplier using exact arithmetic against a separately implemented generator of
all relevant rows, including every coefficient of the joint MacWilliams identity.
If any frozen claim is false, certify the opposite disposition symmetrically; a
solver status, tolerance-based residual, timeout, or missing certificate is not a
mathematical decision.

## Nearest inspected result and proposed delta

Nearest prior result: Kang--Xiong, *Gauss-Phase LP Bounds for LCD Codes*,
arXiv:2609.08662v1 (8 September 2026), Definitions 4.4 and 5.1 on PDF pages
10--12 and the screening report on page 13; local PDF SHA-256
`4d3e6d8a7a3ada9f72131ae9a1a1f088e9f5ef98a04ab3002f3194685bcf95e1`.
Inspected 9 September 2026. Proposed delta: replace its unverified reverse
screening observation by the three exact decisions above. Verification route:
independently generate sparse integer matrices, locate primal/dual objects with
an LP solver, rationally reconstruct them, and replay every row using exact
arithmetic.
