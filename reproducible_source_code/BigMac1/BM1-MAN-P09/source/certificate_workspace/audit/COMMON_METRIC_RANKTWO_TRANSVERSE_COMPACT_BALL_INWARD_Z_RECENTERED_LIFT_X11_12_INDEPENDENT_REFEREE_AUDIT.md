# Independent referee: recentered inward-Z adjacent cell to X=11/12

Date: 2026-08-25  
Verdict: **PASS**  
Classification: **fatal 0 / major 0 / minor 0**

## Scope and independence

This audit concerns only

```text
0<S<=1/10000, 9/10<=X<=11/12,
|M|<=1/1000, |omega|,|nu|<=1/100,
Z=9/13-X^2+S*b-S^2*y0^2+2(X-83059/100000).
```

The frozen candidate source was treated as opaque bytes and used only for
SHA-256. It was not opened for specializations, coefficients, controls, or
helpers and was not parsed, imported, or executed. Its digest is
`fdbf6e078e7d6beb20a5243ddcf80c4a5534027aa9f82283d327cb2361593dfe`;
the source-manifest digest is
`60e1bc22a58ac6ddd8023a0c5e325b6856adf39935c1b6ec526c2b02c602c404`.
All five supplied hashes for the preceding audited cell were independently
bound before mathematical reconstruction.

The referee rebuilds the direct compression and a reversed signed-z Gram
sum, eliminates in the order `q`, signed `z`, `h`, forms `Q^2` with scalar
products ordered `(2,0,1)`, and performs a dense `u`-first Bernstein
transform. No candidate deterministic specialization is reused.

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
49676024530556199202731766735542701752522753368441481977751511650694115571509875227
/239735779200073728000000000000000000000000000000000000000000000000000000.
```

   The complete weakest polynomial was independently reconstructed and its
   exact centered coefficient-l1 lower equals this reserve. The atomic normal
   log preserves that polynomial verbatim.
6. Parameters, cleared raw gate, and cleared core splice exactly at `X=9/10`.
7. Full-cell exact legality was independently recovered:

```text
Z_X >= 1342597/8250000 > 0,
Z >= 292361598161734873/15857127000000000000 > 0,
Z < 8842/365625 < 1,
Tmax = -1880089/71500 < 0,
D >= 199301/1950000 > 0,
det(C) >= [292361598161734873/28542828600000000000] S > 0.
```

   Thus `lambda>0`, strict danger, rank two, and both signed-z lifts hold on
   the entire cell.
8. All 72 exact diagnostic nodes are legal and raw-gate positive. Their
   minimum is

```text
22899826126753585223845316176910603875556251378493488079
/16726464040000000000000000000000000000000000
```

   at `(S,X,M,omega,nu)=(1/10000,9/10,-1/1000,-1/100,-1/100)`. These nodes
   are diagnostics only; the strict Bernstein tensor proves the continuum.

## Adversarial audit

Normal, optimized-Python, bad source hash, bad predecessor hash, bad sparse
normalization, deleted `Q^2`, flipped danger, and deleted-core runs were all
actually executed serially. Normal passed; every mutation failed closed at
its intended exact gate. The formal normal replay wrote stdout/stderr and
its exit code through temporary files followed by atomic renames.

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
.venv/bin/python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x11_12_independent_referee.py
```
