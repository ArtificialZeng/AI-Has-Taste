# Independent referee: recentered inward-Z adjacent cell to X=19/20

Date: 2026-08-25  
Verdict: **PASS**  
Classification: **fatal 0 / major 0 / minor 0**

## Scope and independence

This audit concerns only

```text
0<S<=1/10000, 15/16<=X<=19/20,
|M|<=1/1000, |omega|,|nu|<=1/100,
Z=9/13-X^2+S*b-S^2*y0^2+2(X-83059/100000).
```

The frozen candidate source was treated as opaque bytes and used only for
SHA-256. It was not opened for specializations, coefficients, controls, or
helpers and was not parsed, imported, or executed. Its digest is
`a3097867b0e8a6644c13306e6b3c146839af2f1f0599f326294fee2b0aff355e`;
the source-manifest digest is
`32d9b3639ceddc0c5c76cf985df9a8d4e1ffae4c968d967c354408f23bbca34d`.
All five supplied hashes for the preceding audited cell were independently
bound before mathematical reconstruction.

The referee rebuilds the direct compression and a reversed signed-z Gram
sum, eliminates in the order `q`, signed `z`, `h`, forms `Q^2` with scalar
products ordered `(2,0,1)`, and performs a dense `u`-first Bernstein
transform. No candidate deterministic specialization is reused.

The exact reserve was first derived in an atomic scout run with no reserve
literal in the proof. That run stopped intentionally after printing the
fraction. Only afterward was the literal frozen for the formal normal run;
the derived fraction agreed digit for digit with a separately supplied
public comparison value.

## Exact gates

1. Direct compression equals the reversed Gram sum. The frame is
   orthonormal modulo `q^2=1-S`, `h^2=S`; `H` is Hermitian and even in signed
   `z`; and `det(C)=(5/9)SZ`.
2. All 9/9 entries of `Q^2` match matrix multiplication and are Hermitian.
3. The literal fully conjugated raw gate equals the cyclic vector gate. The
   result is real, radical-free, and has exact degree four in `Z`.
4. Clearing `36*Gate` by positive `25^8(1+M)^8S^3` is reversible. The exact
   counts are `34/34/1659`, with bidegree `(7,4)`.
5. All 40 centered rational Bernstein lower controls are strict. The unique
   weakest index is `(7,0)` with reserve

```text
15364004537485683830512016158976405126737501996882768005086777230415845013529148963
/59933944800018432000000000000000000000000000000000000000000000000000000.
```

   The complete weakest polynomial was independently reconstructed and its
   exact centered coefficient-l1 lower equals this reserve. The atomic normal
   log preserves that polynomial verbatim.
6. Parameters, cleared raw gate, and cleared core splice exactly at `X=15/16`.
7. Full-cell exact legality was independently recovered:

```text
Z_X >= 264199/2750000 > 0,
Z >= 386655427244434873/15857127000000000000 > 0,
Z < 1163/40625 < 1,
Tmax = -1588319/57200 < 0,
D >= 31767/650000 > 0,
det(C) >= [386655427244434873/28542828600000000000] S > 0.
```

   Thus `lambda>0`, strict danger, rank two, and both signed-z lifts hold on
   the entire cell.
8. All 72 exact diagnostic nodes are legal and raw-gate positive. Their
   minimum is

```text
7082552078348649207963879171615956200048566604623246551
/4181616010000000000000000000000000000000000
```

   at `(S,X,M,omega,nu)=(1/10000,15/16,-1/1000,-1/100,-1/100)`. These nodes
   are diagnostics only; the strict Bernstein tensor proves the continuum.

## Adversarial audit

Normal, optimized-Python, bad source hash, bad predecessor hash, bad sparse
normalization, deleted `Q^2`, flipped danger, and deleted-core runs were all
actually executed serially. Normal passed; every mutation failed closed at
its intended exact gate. The formal normal replay and every attack wrote
stdout/stderr and explicit exit codes through temporary files followed by
atomic renames.

No numerical result is used as a theorem. No chart obstruction is promoted
to a raw negative or maximality claim. The proof retains the complex phase,
uses no feasible-center absorption, no fixed `s=-2` allocation, and no
quadratic remainder anchored at `Z=0`; hence CE-046, CE-048, CE-059 and
CE-060 are not reused. The result remains one adjacent local cell, not a
full compact-ball, unrestricted common-metric, arbitrary-node/dimension, or
fixed crossing-lens theorem.

## Conclusion

No fatal, major, or minor finding was identified. The candidate passes as an
exact independently audited adjacent local theorem only. No protected
ledger, research-state/checkpoint file, manuscript, PDF/ZIP, predecessor, or
candidate source was modified.

Replay:

```sh
.venv/bin/python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x19_20_independent_referee.py
```
