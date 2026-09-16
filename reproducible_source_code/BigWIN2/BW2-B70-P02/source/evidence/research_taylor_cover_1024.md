# Certified zero-free range through 1024

Research job: `win-00070-p02-research-5ae3369c8f92` (pass 3,
2026-09-08).

## Exact subsidiary theorem

For the measure and Fourier transform frozen in `source.md`,

\[
 F(x)\ne 0\qquad(27/25\le x\le 1024).
\]

Since `F(-x)=conj(F(x))`, the same holds when
`27/25 <= |x| <= 1024`.  Combining this certified annular range with the
source's Proposition 3.3 on `|x| <= 27/25` gives zero-freeness on
`[-1024,1024]`.  This is a strict subsidiary result: the frozen assertion
through `10^7` remains unresolved.

## Analytic inclusion argument

Put `A=4*pi/3`.  The invariant interval `[0,2/3]` contains the attractor,
so at every terminal real interval `t`,

\[
 |F(t)-1|\le A|t|,\qquad |F^{(n)}(t)|\le A^n\quad(1\le n\le3).
\]

Starting with the corresponding complex rectangles, the generator propagates
outward-rounded Arb balls through the differentiated exact functional equation

\[
F^{(n)}(x)=p2^{-n}F^{(n)}(x/2)+p^2e^{-\pi i x}
 \sum_{j=0}^n {n\choose j}(-\pi i)^{n-j}4^{-j}F^{(j)}(x/4).
\]

It then performs certified Taylor-series division for
`q(x)=F(x)/F(x/2)`.  Every point and interval denominator is required to
exclude complex zero.

For an exact leaf `[a,b]`, write `m=(a+b)/2`, `h=(b-a)/2`, and let `P(s)`
be the quadratic interpolating the certified values `q(a),q(m),q(b)` at
`s=-1,0,1`.  Separately for the real and imaginary components, the Lagrange
remainder is

\[
 |q(m+hs)-P(s)|_{\rm component}
 \le \sup_{[a,b]}|q'''|_{\rm component}
       {h^3\over9\sqrt3}.
\]

An exact dyadic cover of `[-1,1]` proves the interpolating quadratic farther
from zero than the Euclidean norm of these two componentwise errors.  Each
cover segment succeeds either by direct complex-ball separation or by a
certified fixed sign of `(abs(P)^2)'` and the appropriate endpoint value.
Thus `q` is defined and nonzero throughout the leaf, which implies `F` is
nonzero there.

## Exhaustive exact cover

The initial partition is

\[
[27/25+k/8,\,27/25+(k+1)/8]\quad(0\le k<8183)
\]

followed by `[204791/200,1024]`, of width `9/200`.  Hence all 8,184
initial cells have width at most `1/8`, meet exactly, and cover the claimed
closed interval.  Failed stencils were bisected at exact rational midpoints.
The final certificate contains 11,224 accepted leaves and 11,396 polynomial
cover segments.  Its Taylor-leaf depth histogram is

```text
0:6461, 1:2677, 2:1241, 3:437, 4:260, 5:97,
6:11, 7:12, 8:14, 9:10, 10:4.
```

The maximum normalized-polynomial cover depth is 7.  At the stored 256-bit
precision, the least interval-denominator absolute lower bound is greater than
`1.3651341245973564e-5`, and the least certified difference between quadratic
distance and remainder norm is greater than `3.5487297055146310e-5`.

## Independent replay and limitations

`research_taylor_cover_1024.py` generated the certificate with python-flint
0.9.0 at 256 bits and recursion depth 120.  The structural audit checks every
exact endpoint, adjacency, dyadic alignment, serialized denominator, and
polynomial witness.  `verify_research_taylor_cover_1024.py` then recomputes
all 11,224 leaves at 320 bits and depth 128 using the separately implemented
Taylor-coefficient recurrence in `verify_research_taylor_stencils.py`.  The
fresh replay accepts every leaf and has the same aggregate 11,396 polynomial
segments.  The 52 MB certificate has SHA-256
`3a83ce8c86d526ea5070bc407555355c6328d1c4f33add5d3123e257d0da0b21`.

Both evaluator paths use Arb through python-flint, so this is a distinct
precision, depth, and recurrence replay, not a cross-library formal audit.
No point above 1024 is covered, and successful certification here is not
evidence by itself for `(1024,10^7]`.

