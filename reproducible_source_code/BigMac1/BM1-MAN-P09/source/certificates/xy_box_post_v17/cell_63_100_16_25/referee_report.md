# Independent referee audit: `[63/100,16/25]` compact-ball xy-cell

## Verdict

**PASS.** Fatal: **0**. Major: **0**. Minor: **0**.

The independently reconstructed certificate proves only

\[
 \frac{63}{100}\le x\le\frac{16}{25},\qquad
 |y|\le\frac1{100},\qquad Z=\frac18,
 \qquad 0<S\le1,\qquad \lambda>0,
\]

for both signed lifts of `z`. It does not prove the whole compact ball,
arbitrary `Z`, arbitrary transverse compressions, a common-metric theorem,
an arbitrary-node theorem, or the fixed crossing-lens constant.

## Opaque bindings and independence

The current source and source manifest were used solely as opaque byte strings
for SHA-256 verification. They were never opened, parsed, imported, executed,
or used to obtain coefficients, controls, minima, or seam tensors:

- source: `da611b4325ce935c6e9857a2867d92a51a3426a07cb4a1ae1db4f12bc53088cc`;
- source manifest: `dd0d83483d0b8f8c3e6d4f2626dcf89398ff992b5900463811eef70016aa0022`.

The preceding `[627/1000,63/100]` source/referee/report/manifests and the
full-cone reduction dependencies were independently hash-bound. All seam
objects were reconstructed from the original formulas rather than copied.

## Definition-level reconstruction and legality

The referee rebuilt the signed compact frame, `C`, `H`, `Q`, and `Q^2`. It
assembled the signed-`z` Gram column before the mixed column, checked direct
compression entry-by-entry, and verified all 9/9 entries of `Q^2` using the
independent multiplication order `(1,0,2)`.

The fully conjugated literal raw/cyclic gate equals the vector gate exactly;
radical elimination in the order `h,z,q` gives a real polynomial. Both signed
lifts agree. Throughout the cell,

\[
 1-x^2-y^2-Z=\frac78-x^2-y^2
 \ge \frac{4653}{10000}>0,
 \qquad \frac{\det C}{S}=\frac5{72}>0.
\]

Thus danger, both signs, and rank two are strictly legal. Every positive
`S` clearing is preceded by an exact polynomial-divisibility assertion.

## Exact 531-control certificate

The referee independently derived

\[
 36\Gamma=\sum_{k=0}^{4}C_k(S,x,y)\lambda^k
\]

and used

\[
 x=\frac{63}{100}+\frac{v}{100},\qquad
 y=-\frac1{100}+\frac{u}{50},\qquad 0\le u,v\le1.
\]

Its dense exact power-to-Bernstein transform yielded the groups
`1/9/50/147/324`; all **531/531** controls are present and strictly positive.
In the referee order `(S,v_x,u_y)`, the unique global minimum is

\[
 C_3[(0,0,6)]=\frac{66774911}{121500000}>0.
\]

The coefficient and complete control tables have hashes

- `b11348d029f2b1fd6bcbf4dfe3ff789f1f5e67a0846f2a83041e7af62bd9497f`;
- `e454c503ecf14e61e605f562c49859fa85bd580d23eb5966d51f7a6f183a6b0a`.

The full control-table involution verifies the alternative `(S,u_y,v_x)`
index convention. The 81 exact nodes are diagnostics only; the controls are
the proof.

## Four-layer predecessor seam

At `x=63/100`, the referee independently verified:

1. endpoint parameter equality;
2. entrywise equality of the Hermitian parameter matrices;
3. identity of the fully conjugated raw gates;
4. equality of all five Bernstein boundary faces, totaling
   `1+3+10+21+36=71/71` controls.

The seam signature SHA-256 is
`641abe2196970879b1bb1c358dc62b5c8d17aeb2645d911c87531a16c94b37a1`.

## Fail-closed and replay audit

Syntax, literal-free scout, formal normal, root replay, and fresh isolated
replay all exited zero. Fifteen actual mutations exited one at their intended
gates: optimized Python, bad source, bad manifest, bad predecessor, bad
normalization, invalid `S` clearing, dropped `Q^2`, broken conjugation,
omitted minus-`z` lift, flipped danger, corrupted coefficient, dropped
control, broken parameter seam, broken Hermitian seam, and broken control
seam.

The audit rejects numerical evidence as proof, preserves the cyclic phase,
conjugations, every `Q^2` term, and both signed lifts, does not turn chart
illegality into raw negativity or maximality, and does not reuse
CE-046/048/059/060.

## Classification

- Fatal findings: **0**.
- Major findings: **0**.
- Minor findings: **0**.

The local `[63/100,16/25]` theorem is independently certified within the
exact scope above.
