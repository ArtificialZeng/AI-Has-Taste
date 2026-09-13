# Fresh mathematical referee report

**Verdict: ACCEPT.**  I reviewed the exact frozen `resolution-paper` claim bound
to snapshot
`b2d23954f6d5891b916d9e20169010ea5ff36baf3d2dfde3987fd931199d1d82`.
The submitted argument proves the full statement in `source.md`, including the
entire positive ordered step quadrant and arbitrary finite dimension.  It does
not assert uniqueness.

## Scope and normalization

Writing `h_i=L eta_i` and dividing the objective by `L` correctly reduces to a
1-smooth convex function.  Translation by the selected minimizer, subtraction
of its value, and rescaling by `D=||x_0-x_*||>0` preserve the gradient steps and
reduce to `x_*=0`, `f_*=0`, and `||x_0||=1`.  This reduction is valid for any
chosen minimizer; it does not assume that it is the closest minimizer.

Put

`s=sqrt(2)`, `t=sqrt(9+8s)`, `r=2/(1+t)`, and `C=r^2/2`.

Exact simplification gives

`C=1/(5+4s+t)`,
`b_*=1+r(1+s)=(3+t)/4`, and
`H=(r^(-2)-1)/2=s+b_*`.

Also, for `u_0=s-1` and `v_0=r(1+s)`, one has
`u_0 v_0=r` and `v_0=r(u_0+2)`.  All divisions used below have positive
denominators, and `0<r<1` follows immediately from `t>1`.

## Reconstruction of the global lower bound

For arbitrary positive normalized steps `a,b`, each of the four submitted
one-dimensional functions is admissible: its displayed derivative is
continuous, nondecreasing, and 1-Lipschitz, and its minimizer set is exactly
`{0}`.

1. For the two-sided Huber function with
   `delta=1/(1+2(a+b))`, the iterates remain in its right linear region:
   `x_1-delta=(a+2b)/(1+2(a+b))>0` and
   `x_2-delta=(a+b)/(1+2(a+b))>0`.  Direct evaluation gives
   `f(x_2)=1/(2(1+2(a+b)))`.
2. The quadratic gives `x_2=(1-a)(1-b)` and value
   `((a-1)(b-1))^2/2`.
3. The right-capped quadratic, with `delta=1/(1+a)`, gives
   `x_1=delta` and `x_2=delta(1-b)<=delta`, hence value
   `(b-1)^2/(2(a+1)^2)`.
4. If `a>1`, the left-capped quadratic with
   `delta=(a-1)/(b+1)` gives
   `x_1=-(b+1)delta<-delta` and `x_2=-delta`, hence value
   `(a-1)^2/(2(b+1)^2)`.

These are genuine values of admissible instances, so they are lower bounds on
the supremum defining `R(a,b)`; no PEP relaxation or finite-dimensional
restriction is involved.

To check that these witnesses cover the full open quadrant, suppose
`R(a,b)<C` and set `u=a-1>-1`, `v=b-1>-1`.  The four lower bounds imply

`a+b>H`, `|uv|<r`, `|v|<r(u+2)`, and, when `u>0`,
`u<r(v+2)`.

If `u,v` are not both nonnegative, the applicable capped inequality gives
`u+v<2r` (and this is immediate when both are negative).  But
`H-(2+2r)=(s-1)(1+r)>0`, contradicting `a+b=2+u+v>H`.

It remains that `u,v>=0`.  Suppose first `v>=u`.  If `u<=u_0`, then

`u+v<(1+r)u+2r <= (1+r)u_0+2r=u_0+v_0`.

If `u>u_0`, then `uv<r` and `v>=u` imply
`u<sqrt(r)` and `u+v<u+r/u`.  The function `z+r/z` is decreasing on
`(0,sqrt(r)]`.  Moreover `u_0<sqrt(r)`: indeed
`u_0^2<1/5<1/3<r`, using `7/5<sqrt(2)<2` and `t<5`.
Consequently

`u+v<u_0+r/u_0=u_0+v_0`.

When `u>=v`, the same two subcases with `u,v` interchanged use
`u<r(v+2)` and give the identical conclusion.  Thus in all cases
`a+b<2+u_0+v_0=H`, the final contradiction.  This proves
`R(a,b)>=C` for every ordered pair `(a,b)` in the full positive quadrant.
The proof never divides by `u` or `v` in a zero case.

## Reconstruction of the dimension-free upper bound

At `h_1=s`, `h_2=1+v_0`, let

`I_ij=f_i-f_j-<g_j,x_i-x_j>-||g_i-g_j||^2/2`.

Every `I_ij` is nonnegative for an actual differentiable convex function with
1-Lipschitz gradient.  With indices `(*,0,1,2)`, the six multipliers

- `lambda_*0=s r^2`, `lambda_*1=(2+s)r^2`, `lambda_*2=r`;
- `lambda_01=(1+s)r^2`, `lambda_10=r^2`, `lambda_12=1-r`

are strictly positive.  Expanding the submitted identity gives exactly

`C||x_0||^2-f_2 = sum lambda_ij I_ij
 + ||(r/s)x_0-rg_0-v_0g_1-(1/s)g_2||^2`.

I independently expanded both sides as a formal polynomial in the three
function values and the ten independent Gram entries of
`(x_0,g_0,g_1,g_2)`.  Every coefficient cancels exactly.  This check is
reproducible in `audit/referee_verify.py`; it uses a direct symbolic
inner-product expansion, distinct from the matrix construction in the frozen
verifier.  I also reran `evidence/exact_resolution_verify.py` with the mandated
research interpreter, and it passed all exact radical, balance, and rank-one
PSD checks.

Since the right side is nonnegative in every finite-dimensional Hilbert space,
`f_2<=C||x_0||^2` for every admissible instance at the claimed schedule.
Together with the global lower bound this proves equality of the infimum and
attainment at that ordered schedule.

## Scope attacks and source comparison

- The lower proof treats negative, zero, and positive values of `a-1` and
  `b-1`, so no step region or equality boundary is omitted.
- All witnesses start from the nonminimizer `x_0=1`, have denominator one after
  normalization, and have proper minimizer set `{0}`.
- The upper certificate uses only interpolation inequalities satisfied by the
  actual function samples; it is therefore dimension-free and does not assume
  an SDP optimum, compactness, or attainment of the outer supremum.
- No limiting exchange, adaptive schedule, swapped step order, or uniqueness
  assertion enters the argument.
- The frozen source comparison says the nearest inspected work supplies the
  exact fixed-schedule upper/sharpness result and a numerical global result,
  while the missing delta is the exact lower bound over all positive schedules.
  The submitted four-witness partition supplies precisely that delta.  The
  proof is self-contained and does not invoke a cited theorem.  In accordance
  with the frozen-evidence instruction, I did not open literature files absent
  from the snapshot; this audit therefore certifies the mathematics and the
  contribution relative to the frozen comparison, not an unrestricted priority
  claim.

There is no mathematical or scope gap requiring revision.  The exact frozen
candidate is accepted as a `resolution-paper`, with original status `proved`.
