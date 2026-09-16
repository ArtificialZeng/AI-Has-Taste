# Certified radius-1/16 cells at the two deepest reported valleys

Research job: `win-00070-p02-research-857391805db7` (pass 1,
2026-09-08).

## Exact partial result

For the Fourier transform `F` frozen in `source.md`, directed ball arithmetic
certifies

\[
 F(x)\ne 0
 \quad\text{on}\quad
 [6580077.12910276,6580077.25410276]
 \cup
 [5065070.54521886,5065070.67021886].
\]

The two centers are treated as the exact printed decimals
`6580077.19160276` and `5065070.60771886`; each interval has exact rational
radius `1/16`.  This is a bounded partial result, not a proof on
`[-10^7,10^7]`.

## Certification argument

The attractor is contained in `[0,2/3]`.  Hence, for every real `t`,

\[
 |F(t)-1|
 \le \int |e^{-2\pi i t y}-1|\,d\mu(y)
 \le 2\pi |t|\sup |y|
 \le \frac{4\pi}{3}|t|.
\]

For a rational interval `X`, the generator places `F(X/2^120)` and
`F(X/2^121)` in rectangular complex balls obtained from this bound.  It then
applies 120 outward-rounded Arb steps of

\[
 F(x)=pF(x/2)+p^2e^{-\pi i x}F(x/4),
 \qquad p=(\sqrt5-1)/2.
\]

Induction on the upward recursion shows that the final pair encloses
`F(X)` and `F(X/2)` for every `x` in `X`.  A leaf is accepted only after
`F(X/2)` excludes complex zero and either the real or imaginary component of
the quotient enclosure `F(X)/F(X/2)` excludes zero.  Thus `F(x)` cannot be
zero anywhere on that leaf.

Adaptive exact-rational bisection produced 78 leaves for the first cell and
148 for the second, 226 total, with maximum bisection depth 21.  The serialized
leaves are ordered and share exact endpoints, so their closed union is exactly
the two stated cells.  Every denominator and quotient enclosure is stored in
the certificate.

## Replay artifacts

- `research_valley_cells.py` generates the certificate at 256-bit precision
  with python-flint 0.9.0.
- `research_valley_cells_certificate.json` contains the 226 rational leaves
  and their decimal Arb enclosures.  Its SHA-256 is
  `1f05e8dce38e98e02665945029c351c813379bcd830135c278f20c9f68cbf417`.
- `verify_research_valley_cells.py` independently checks exact union coverage,
  parses every stored enclosure, and recomputes `F(X)` and `F(X/2)` in separate
  recursion calls rather than reusing the generator's paired recursion.
- `research_valley_cells_verification.txt` records the successful replay.

From the project directory, regenerate and replay with

```text
python3 evidence/research_valley_cells.py
python3 evidence/verify_research_valley_cells.py
```

## Scope and remaining obstacle

The certified union has total length `1/4`; almost all of `[1.08,10^7]`
remains uncovered.  Direct interval recursion loses enough dependency
information that the two whole cells do not certify as single leaves, although
adaptive subdivision resolves them.  The source's double-precision scan and
empirical third-derivative estimate still cannot certify the intervening
range.  A scalable proof needs a rigorous Taylor/derivative screen or another
compressed covering method, with direct subdivision reserved for flagged
valleys.
