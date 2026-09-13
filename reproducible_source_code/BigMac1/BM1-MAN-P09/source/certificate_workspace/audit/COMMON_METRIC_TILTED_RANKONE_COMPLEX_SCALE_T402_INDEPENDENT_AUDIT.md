# Independent adversarial audit: active-block `t` radius `1/402`

Date: 2026-08-23.  Verdict: **PASS as an exact computer-assisted partial
theorem, with the scope stated below**.  No exact legal negative original
gate was found.  The unrestricted complex Hermitian gate, the common-metric
theorem, and the fixed crossing-lens constant remain open.

Audited statement:

```text
tmp/research/common_metric_tilted_rankone_complex_scale_t402_enlargement.md
```

Independent verifier:

```text
audit/verify_common_metric_tilted_rankone_complex_scale_t402_independent_audit.py
```

The verifier imports neither the source verifier nor discovery code.  It
uses exact `sympy.Rational` arithmetic and keeps CPU work single-process.  It
reconstructs the seven theorem-relevant `t=4` Bernstein tensors itself;
historical `N_D` controls are not imported into the proof.

## 1. Formal endpoint audited

Fix

```text
a=3/5, c=4/5,
ell in [8,10],                 w in [-31/100,-29/100],
k in [-301/100,-299/100],     z in [-101/100,-99/100],
r in [99/100,103/100],        t in [1607/402,1609/402].
```

For `T>0`, set `tau=sqrt(T)` and

```text
Delta = r*t-z^2-w^2,
n     = t*(k^2+ell^2)+r-2*(k*z+ell*w),
g     = (12/25)*ell-z*k-w*ell-t,

Q = [[r,                 tau*(k+i*ell), z+i*w],
     [tau*(k-i*ell),     T*n/Delta,     tau],
     [z-i*w,             tau,           t]].
```

The audited conclusion is strict positivity of the original scalar gate on
the complete complementary legal scale branch

```text
T>0                    if g<=0,
T>Delta*g/n            if g>0,
```

together with positivity on its closure endpoint `T=0` for `g<=0` and
`T=Delta*g/n` for `g>0`.  The endpoint at `g=0,T=0` is a closure point of
the strict completion branch, not an omitted case.

## 2. Definition-level reconstruction

The audit rebuilt the fully conjugated gate from

```text
a^2 |xi_2|^2
+ (1/4)|c*conj(xi_1)+a*xi_3+i(ac-(Q^2)_31)|^2
+ (1/4)|c*conj(xi_2)-i(Q^2)_32|^2
- 8a^2 Re(xi_1)^2,                         xi=Q(a,0,c)^T.
```

It separately multiplied `Q*Q` and checked all nine entries against

```text
(Q^2)_11 = r^2+T(k^2+ell^2)+z^2+w^2,
(Q^2)_12 = tau*((r+q)(k+i ell)+z+i w),
(Q^2)_13 = (r+t)(z+i w)+T(k+i ell),
(Q^2)_21 = conjugate((Q^2)_12),
(Q^2)_22 = T(k^2+ell^2+1)+q^2,
(Q^2)_23 = tau*((k-i ell)(z+i w)+q+t),
(Q^2)_31 = conjugate((Q^2)_13),
(Q^2)_32 = conjugate((Q^2)_23),
(Q^2)_33 = z^2+w^2+T+t^2,
```

where `q=T*n/Delta`.  This check retains the cyclic cross phase and would
fail if either Hermitian conjugate were replaced by a transpose.

The active `(1,3)` block has determinant `Delta`.  The exact Schur value of
the middle coupling is `T*n/Delta`, so its Schur complement is zero and
`det(Q)=0`.  Since `r>=99/100`, and the audited reserves give
`Delta,n>0`, `Q` is Hermitian PSD of rank two for every `T>0`.  At `T=0`,
the active block stays positive definite and the zero middle row/column
again gives rank two.  Thus no singular denominator, rank-zero, or hidden
indefinite branch is used.

With a free middle entry `q`, the imaginary part of the last residual is
exactly `-tau*(q-g)`, while

```text
q_min-g = (T*n-Delta*g)/Delta.
```

This proves the displayed legal half-line and its endpoints without scale
sampling.

## 3. Independent scale cubic and terminal dependency DAG

Starting from the definition-level gate, the audit first proved that every
power of `tau` is even and then replaced `tau^(2j)` by `T^j`.  It obtained

```text
4 Delta^2 G(Q) = P(T) = C0+C1*T+C2*T^2+n^2*T^3,
C2 = Delta^2(k^2+ell^2)-2 Delta*g*n.
```

A second expansion from the two complex residual squares reproduced the
same cubic.  At `T_L=Delta*g/n`, it independently recovered

```text
P(T_L)  = N0/(15625*n^2),
P'(T_L) = N1/(625*n),
C2+3n^2*T_L = Delta^2(k^2+ell^2)+Delta*g*n.
```

The complete terminal DAG is:

```text
danger, Delta, n                         -> legality
Delta, n, C0, C1 + C2 identity          -> g<=0 branch
Delta, n, N0, N1                        -> g>0 endpoint value/derivative
Delta, n + endpoint-curvature identity  -> g>0 strict convexity
```

There is no `N_D` node or edge.

- If `g<=0`, `C0,C1>0` and
  `C2=Delta^2(k^2+ell^2)-2Delta*g*n>0`.  Here `ell>=8`, so strictness also
  holds at `g=0`.  Every coefficient of `P` is positive, including the
  leading `n^2`, hence `P(T)>0` for all `T>=0`.
- If `g>0`, `Delta,n,N0,N1>0` give positive endpoint value and derivative.
  The displayed endpoint curvature is strictly positive.  Since
  `P''(T)=2(C2+3n^2T)` has positive slope `6n^2`, `P''`, then `P'`, then
  `P` remain positive on the complete half-line `T>=T_L`.

This exhausts `g<0`, `g=0`, and `g>0`, including `T=0` and the finite
positive endpoint.  No cubic branch, critical point, tangent root, or
degenerate denominator is left for a discriminant test to control.

## 4. Both stitched center cells and all fourteen reserves

For each of the seven sign polynomials, the verifier substituted `t=4`,
formed the exact five-axis rational node tensor, inverted independent
Bernstein collocation matrices on all five axes, checked every control, and
then reconstructed every node.  It checked `40,595` controls on each cell:

```text
r_low  = [99/100,101/100],
r_high = [101/100,103/100].
```

The common seam `r=101/100` is contained in both closed cells.  There is no
stitching gap or half-open endpoint convention.

Independently, the audit differentiated the six-variable polynomials in
`t` and computed the absolute power-monomial majorant `M` on
`399/100<=t<=401/100`.  The following are the exact recomputed
`m-M/402` reserves:

| cell | sign | exact reserve |
|---|---|---:|
| low | danger | `93/500` |
| low | `Delta` | `713861/251250` |
| low | `n` | `1170138811/4020000` |
| low | `C0` | `83805326319665374729/251250000000000000` |
| low | `C1` | `118150790449310782759/125625000000000000` |
| low | `N0` | `53549445496650257669039960758536579907/128640000000000000000000000` |
| low | `N1` | `3602140976554567042623930779/21440000000000000000` |
| high | danger | `87/500` |
| high | `Delta` | `733961/251250` |
| high | `n` | `1170219211/4020000` |
| high | `C0` | `89430329249926227001/251250000000000000` |
| high | `C1` | `124761587551841297659/125625000000000000` |
| high | `N0` | `57259476117655354712509684456016821507/128640000000000000000000000` |
| high | `N1` | `3804850025578919595098706779/21440000000000000000` |

All fourteen are strictly positive.  The cellwise minima reproduce the
seven reserves displayed in the candidate statement.

The exact interval is

```text
[4-1/402,4+1/402] = [1607/402,1609/402].
```

It lies inside `[399/100,401/100]` and strictly contains both the `1/403`
and `1/500` layers.

## 5. `N_D` classification

For the predecessor's eight-sign certificate package, the exact audited
lower-cell derivative lower bound at radius `1/402` is

```text
-54657263927145682718521091555313864896870775497413042370594307870877001
 /20582400000000000000000000000000000000000000000000 < 0.
```

This is `m-M/402`, not `N_D` evaluated at a legal parameter tuple.  It is
also not `P(T)`, `G(Q)`, or any original common-metric separator.  The
audit found no exact legal negative gate.  Because Section 3 exhausts the
terminal proof without `N_D`, this negative lower bound is only a failure of
the older eight-sign derivative certificate at that radius.

## 6. Nonredundancy and phase integrity

After quotienting common active-block scale, the invariant
`(r+t)/sqrt(Delta)` has `t` derivative with numerator

```text
r*t-r^2-2(z^2+w^2).
```

The audit proves its exact lower bound `461/625>0` on the wider derivative
box.  Hence `t` is not the coupling scale `T` or a hidden common rescaling.

At

```text
ell=9, w=-31/100, k=-301/100, z=-101/100,
r=103/100, t=2001/500, T=1,
```

the witness is strictly inside the new `t` interval, is PSD rank two, lies
strictly in the legal branch, and has danger `-19/100`.  Direct evaluation
from the original gate gives

```text
G(Q)=414461983319631411704949/112939929245000000000 > 0,
4(G(Q)-G(Re Q))
 = -585660171418319979/375732500000000 < 0.
```

The two imaginary coordinates have product `-279/100`.  Thus both complex
phases are live, and real-part monotonicity or a same-sign phase cone cannot
be a hidden premise.

## 7. Fail-closed and reproducibility record

Final successful commands were run from the checkpoint root with the
checked-in Python 3.11.15 environment and SymPy 1.14.0.

```text
/usr/bin/time -p .venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t402_independent_audit.py
```

Exit `0`; `real 69.32`, `user 67.58`, `sys 0.50`.  It printed all five PASS
lines.  Its two independently reconstructed center-statistics digests were

```text
6b97b62de2c59f8df62620baa3519c436d6ebf66cd908a769868544fc4f02611
65ca5bd6e6d2f0746452b0f24a10e366ed0021620e143153195aee889f669d0f
```

The untrusted source verifier was run only as a post-audit comparison:

```text
.venv/bin/python -B \
  tmp/research/verify_common_metric_tilted_rankone_complex_scale_t402_enlargement.py
```

Exit `0`; its reported conclusion agrees with the independent verifier.

Three deliberate corruption tests failed closed:

```text
.venv/bin/python -O -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t402_independent_audit.py
# exit 1: optimized Python rejected

T402_AUDIT_TEST_BAD_DEPENDENCY=1 .venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t402_independent_audit.py
# exit 1: dependency hash mismatch rejected

T402_AUDIT_TEST_DROP_SIGN=1 .venv/bin/python -B \
  audit/verify_common_metric_tilted_rankone_complex_scale_t402_independent_audit.py
# exit 1: incomplete sign dependency set rejected
```

The candidate package manifest passed:

```text
shasum -a 256 -c \
  tmp/research/common_metric_tilted_rankone_complex_scale_t402_enlargement_manifest.sha256
# exit 0; all eleven entries OK
```

The global frozen checkpoint manifest is not clean in the current working
state:

```text
set -o pipefail; shasum -a 256 -c CHECKPOINT_MANIFEST.sha256 2>&1 \
  | rg 'FAILED|WARNING'
# exit 1
```

It reports pre-existing drift in `APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`,
`COUNTEREXAMPLE_DB.md`, and `research_state.json`.  Per the audit assignment,
none of those files was edited here.  This global drift does not affect the
separately hash-bound t402 dependency DAG, but it must not be described as a
clean frozen-checkpoint replay.

Development diagnostics, not theorem failures: system `python3` exited `1`
because it lacked SymPy; an overinclusive draft that replayed historical
`N_D` controls was manually stopped with exit `130` after the lower center
cell had passed, and was replaced by the final theorem-specific seven-sign
reconstruction; a pre-final audit assertion exited `1` because it attempted
to substitute the composite expression `g` as an independent symbol.  The
final verifier introduces an auxiliary independent `G`, reruns both center
cells, and passes.

## 8. Hashes and scientific scope

At audit freeze, the principal hashes are:

```text
1f3a41767f8a668d51d22edf4edbd0bf9daf4b87356179859aea1e1b93818a82  candidate statement
c7bdce41a0a55dc31c3ad14a113a8dffd14d4a323c264a875c1238ae3412b473  source verifier
57685250b623139e1b19361121b47c5b0a2f0215fa795ab681d52519b7966b2d  candidate manifest
a732faf7bfe2ea9ced372be87f9b29494b5b4f7a26faa3cd4c359979f08490ed  independent verifier
```

No proof assistant was used for this audit.

The passed result is one seven-real-parameter positivity island: six bounded
shape coordinates and every legal positive coupling scale.  It does not
cover arbitrary active blocks, arbitrary phase directions, the feasible-
center branch, unbalanced densities, higher rank, dimension greater than
three, arbitrary nodes, the full common-metric theorem, or the fixed
crossing-lens constant.  The scientifically honest status is therefore
**exact computer-assisted partial theorem**, not a solution of the general
problem.
