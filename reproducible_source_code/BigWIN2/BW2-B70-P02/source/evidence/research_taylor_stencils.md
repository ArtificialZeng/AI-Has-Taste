# Certified adaptive order-3 Taylor stencils at the two deepest valleys

Research job: `win-00070-p02-research-7788cb2527f4` (pass 2,
2026-09-08).

## Scope and outcome

This pass independently re-certifies the same bounded partial fact established
in pass 1:

\[
F(x)\ne0\quad\text{on}\quad
[6580077.12910276,6580077.25410276]
\cup[5065070.54521886,5065070.67021886].
\]

Its new evidence is algorithmic compression, not a larger zero-free interval:
the order-3 Taylor certificate has respectively 8 and 10 exact-rational Taylor
leaves (18 total, maximum bisection depths 4 and 5), versus 78 and 148 leaves
in the direct interval-recursion certificate.  It therefore does not qualify
as a new mathematical result candidate, and the frozen assertion remains
unresolved.

## Certified jet construction

Put \(A=4\pi/3\).  Since `supp(mu) subset [0,2/3]`, at terminal scale

\[
 |F(t)-1|\le A|t|,\qquad |F^{(n)}(t)|\le A^n\quad(1\le n\le3).
\]

Starting with these complex rectangles at depths 120 and 121, the generator
differentiates the exact functional equation.  For \(0\le n\le3\),

\[
F^{(n)}(x)=p\,2^{-n}F^{(n)}(x/2)+p^2e^{-\pi ix}
 \sum_{j=0}^n {n\choose j}(-\pi i)^{n-j}4^{-j}F^{(j)}(x/4).
\]

It then divides the order-3 Taylor series for \(F(x)\) and \(F(x/2)\).
Every point and interval denominator is required to exclude complex zero
before the quotient \(q(x)=F(x)/F(x/2)\) is used.

On a leaf \([a,b]\), let \(m=(a+b)/2\), \(h=(b-a)/2\), and let \(P(s)\)
be the quadratic interpolating \(q(a),q(m),q(b)\) at \(s=-1,0,1\).  Applied
separately to real and imaginary parts, the Lagrange remainder gives

\[
 |\operatorname{component}(q(m+hs)-P(s))|
 \le \sup_{[a,b]}|\operatorname{component}(q''')|
       \frac{h^3}{9\sqrt3},\qquad -1\le s\le1.
\]

The certificate covers each normalized leaf by exact dyadic rational segments.
It either separates the complex ball `P(segment)` directly from the rectangular
remainder, or proves a fixed sign for
\((|P|^2)'=2\operatorname{Re}(\overline P P')\) and checks the minimizing
endpoint.  There are 24 such polynomial-cover segments; only one Taylor leaf
needs subdivision of its normalized polynomial domain (7 segments, depth 6).

## Whole-cell diagnostic

A single three-node stencil on either full radius-`1/16` cell is inconclusive.
For the first cell the certified full-cell component bounds are
`|Re q'''| <= 3076.903` and `|Im q'''| <= 3063.912`, giving a Euclidean
remainder bound about `6.789e-2`.  For the second they are
`|Re q'''| <= 1.210018e6` and `|Im q'''| <= 1.210022e6`, giving a remainder
bound about `2.659e1`.  In both cases the corresponding componentwise
remainder tube at the center contains zero.  These are dependency-inflated
derivative enclosures, not evidence that a zero exists.  Exact adaptive
bisection shrinks the decisive central leaf enough to certify it.

## Replay and limitations

`research_taylor_stencils.py` emits the 256-bit, depth-120 certificate.
`verify_research_taylor_stencils.py` checks its exact covers and stored
witnesses, then independently recomputes exponential Taylor coefficients at
320 bits and depth 128.  The replay succeeds with the same 18 Taylor leaves and
24 polynomial-cover segments.  The certificate SHA-256 is
`f48a0db352d9cf389783af8468b0dc53c98b961d9362b1d9c1785f80cdc7f6ba`.

Both paths use Arb through python-flint 0.9.0, so this is a distinct recurrence,
precision, and truncation replay but not a cross-library formal audit.  The
certified union still has total length only `1/4`; almost all of
`[1.08,10^7]` remains uncovered.
