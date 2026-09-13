# Discovery note: affine omega tilt beyond the centered danger breakpoint

Date: 2026-08-24. Status: **exact discovery-level certificate candidate, not
a theorem**. No source verifier, independent signed-`z` referee, frozen
manifest, or root promotion has yet been produced.

## 1. Structural obstruction at `X=1/4`

For every moving-sheet recenter whose physical `omega` and `nu` centers
remain bounded independently of `S`,

\[
 D:=1-x^2-y^2-Z
 =\frac35-\frac{13}{5}X-ST
 \longrightarrow \frac35-\frac{13}{5}X
 \quad(S\to0+).
\]

Consequently no such scale-uniform slice can be strictly dangerous for any
`X>3/13`. In particular, reaching `X=1/4` is impossible in the requested
class. This is a geometric legality obstruction, not a negative original
gate and not a counterexample.

## 2. Exact tilted slice

Keep the original radii and scale range unchanged:

```text
0<S<=1/10000,
|M|<=1/1000,
|omega|<=1/100,
|nu|<=1/100.
```

On

```text
1/5<=X<=3/13,
```

use centered variables `omega,nu` but set the physical sheet parameter to

\[
 \omega_{\rm phys}
 =\omega-\frac{10636}{275}\left(X-\frac15\right),
 \qquad
 \nu_{\rm phys}=\nu.
\]

At `X=1/5` this is exactly the old sheet, so the new slice has an exact seam
inside the proved old range and overlaps its `X` interval on
`[1/5,X_*)`. At the new endpoint,

\[
 \omega_{\rm center}(3/13)=-\frac{21272}{17875}.
\]

No centered radius is reduced; the physical center moves.

## 3. Exact legality

Writing `A=1+M`, the danger coefficient is

\[
 T=\frac95+\omega+\frac65\nu-\frac{63}{125A}
   -\frac35X-\frac{10636}{275}\left(X-\frac15\right).
\]

Its maximum over the centered box satisfies

\[
 T_{\max}(3/13)=-\frac1{100}.
\]

For `X<3/13`, if `T<0` then
`D>3/5-(13/5)X>0`. If `T>=0`, monotonicity in `S` reduces to
`S=1/10000`, where the exact worst expression is

\[
 D_{S_{\max}}=
 -\frac{371238348X-85670531}{143000000}>0
 \quad(1/5\le X\le3/13).
\]

At `X=3/13`, every legal parameter has `T<=-1/100`, hence

\[
 D=-ST\ge\frac{S}{100}>0.
\]

Independent interval bounds inside the discovery program give

```text
Z >= 8879008598718934873/15857127000000000000 > 0,
Z <= 8316795197/13013000000 < 1.
```

Thus `lambda>0`, strict danger, positive `Z`, and
`det C=(5/9)SZ>0` all hold throughout this tilted slice. The discovery
quartic is the exact `Z=z^2` evaluator, so it represents both real lifts of
`z`; a fresh definition-level signed-`z` reconstruction is still required
before promotion.

## 4. Certificate comparison

The old absolute-remainder architecture changes from `20/16/947` to

```text
22 quotient terms,
18 higher terms,
1013 centered parameter monomials.
```

Its quadratic core remains strictly positive, but the total termwise
absolute bound gives

\[
 -\frac{
4730327733867621557016642117420201461624703483806715766986130687852693
}{
37515501659750400000000000000000000000000000000000000000
}<0.
\]

This is a failure of that sufficient bound only. It is not a gate value.

Exact comparison under the common legality constraint

\[
 \alpha+\frac65\beta=-\frac{10636}{275}
\]

gave:

| tilt | quotient/higher/monomials | old absolute certificate | exact negative nodes |
|---|---:|---|---:|
| omega only | `22/18/1013` | fails; best ratio | 0/72 |
| equal danger split | `28/24/1443` | fails | 0/72 |
| nu only | `28/24/1404` | fails | 0/72 |

All three retain the same radii and pass the exact legality grid. Omega-only
is the best of these three canonical splits.

## 5. Lossless two-stage Bernstein recovery

For the omega-only candidate, preserve the manifestly nonnegative first layer

\[
 25^8M^2S(1+M)^8(5M^2+14M+14).
\]

For the remaining quotient use the exact recentering

```text
X = 1/5 + (2/65)u,       0<=u<=1,
S = (1/2000)*tau*X,      0<=tau<=1.
```

The `tau` rectangle is a harmless enlargement of the lossless
`sigma=S/X` domain. The remaining polynomial has bidegree `(5,7)` in
`(tau,u)`. Exact power-to-Bernstein conversion produces 48 tensor controls.
Each control is then bounded on the unchanged centered
`(M,omega,nu)` box by exact centered arithmetic.

All 48 lower controls are strictly positive. The minimum occurs at control
`(0,0)` and is

\[
 \frac{2564950982194530478444050838857341987999}
 {31850496000000000000000000000}>0.
\]

This is an exact continuum certificate candidate for the original moving
quartic on the full tilted closed interval. It remains discovery evidence
until a fail-closed source reconstructs the fully conjugated Hermitian gate
and a differently ordered no-cache signed-`z` referee reproduces the same
48 controls and minimum.

## 6. Exact raw-gate falsification

The omega-only script evaluates 72 exact rational seam/interior/endpoint
nodes. All are legal and none has a negative original gate. The minimum is
the old seam node:

\[
 36\Gamma=
 \frac{213355344357890421512795094325969057679}
 {40000000000000000000000000000000000}>0.
\]

At the new endpoint and the worst danger corner,

```text
36 Gamma =
2875017794276661652931485545294665330527919
/262440000000000000000000000000000000000 > 0,

Z = 640272135596701999/1002001000000000000 > 0,
danger = 1/1000000 > 0,
det C = 640272135596701999/18036018000000000000000 > 0.
```

The grid is falsification only; the two-stage Bernstein controls are the
continuum discovery certificate.

## 7. Artifacts and limitations

```text
51d51d98f8e49a286aeedca1d3fed510024421d4b58d6c967ec6ea1aac42075a
tmp/research/compact_ball_positive_z_moving_sheet_affine_omega_tilt_discovery.py

06ff590d9fcf2b45aefcaf19a76f39c42fe73851231df5a3c113ef3e49d018fb
tmp/research/compact_ball_positive_z_moving_sheet_affine_tilt_split_comparison_discovery.py
```

The first script passes normal exact execution and external-cache
`py_compile`. This note does not claim a theorem, a maximal gate-sign
result, a full compact-ball result, a common metric, or a fixed-lens solution.
No CE-046/048/059/060 route, sampled SDP, real-part monotonicity, or dropped
phase is used. No proof assistant was used.

