# Breaker result: an exact length-10 counterexample

## Outcome

The corrected Ehrhart root-disk conjecture is false at word length 10.  The
regular snake word

\[
w=\varepsilon LRLRLRLRLR
\]

has Ehrhart roots outside the closed disk centered at \(-7\) with radius
\(6\).  This is an exact result, not an inference from the decimal roots.

The independent verifier is
`discovery/breaker_verify_counterexample.py`; its sole serialized input is
`experiments/breaker_counterexample_certificate.json`.

## Parameter repair

In arXiv v2, `sections/preliminaries.tex` lines 9--10 define length as the
number of letters in \(\{L,R\}\).  Line 270 gives dimension \(2m+4\) for
length \(m\), and lines 301--305 prove

\[
L(w;t)=L(w;-m-4-t).
\]

However, `sections/h_polynomials.tex` lines 569--573 state Conjecture 1 for a
word of “length \(n+1\),” put a positive number in the disk-center expression,
and simultaneously give the negative symmetry axis.  These statements cannot
all be literal.  The only reading consistent with the definition, the proved
symmetry, the fixed roots, and the “verified through length 9” sentence at
line 576 is:

\[
|t+(m+4)/2|\le (m+2)/2
\quad\text{for a word having exactly }m\text{ letters.}
\]

Thus length 10 means ten `L/R` letters, dimension 24, center \(-7\), and
radius 6.  This is the endpoint attacked here.

The v1 and v2 recurrence texts also differ.  V1 uses the final alternating
sub-snake (v1 lines 377--396), while v2 replaces it with the final constant
sub-ladder (v2 lines 382--401).  Discovery used v2.  The decisive candidate's
\(h^*\) was then rebuilt without either recurrence by enumerating linear
extensions of the poset from v2 `preliminaries.tex` lines 13--27.

## Exact polynomial

Direct enumeration of the 13,860 linear extensions gives

\[
h^*(w;z)=1+21z+181z^2+833z^3+2241z^4+3653z^5
+3653z^6+2241z^7+833z^8+181z^9+21z^{10}+z^{11}.
\]

Put \(x=t+7\) and \(y=x^2\).  Integer arithmetic in the binomial-basis
formula for the Ehrhart polynomial gives the identity

\[
24!L(w;x-7)
=36\prod_{k=0}^{6}(x^2-k^2)Q(x^2),
\]

where

\[
Q(y)=385y^5+25789y^4+923223y^3+10769815y^2
+70801492y+23924096.
\]

Every coefficient and the factorization are recomputed by the verifier from
the source-defined poset.

## Rational isolating disk

Let

\[
c=-\frac{53}{2}+29i,\qquad r=\frac16.
\]

Writing \(Q(c+u)=\sum_{j=0}^{5}a_j u^j\), the exact Gaussian-rational
coefficients are stored in the certificate and recomputed by the verifier.
They satisfy

\[
\begin{aligned}
|a_0|&<151000000,& |a_1|&>1060000000,\\
|a_2|&<103000000,& |a_3|&<3750000,\\
|a_4|&<61300,& |a_5|&\le385.
\end{aligned}
\]

Consequently, on \(|u|=1/6\),

\[
|a_1u|>
|a_0|+\sum_{j=2}^{5}|a_j u^j|,
\]

because the certified lower minus upper rational bound is

\[
\frac{177200631815}{7776}>0.
\]

Rouché's theorem therefore says that \(Q(c+u)\) and \(a_1u\) have the same
number of zeros in \(|u|<1/6\), counting multiplicity: exactly one.  Call the
isolated algebraic root \(y_0\).  The entire isolating disk lies strictly
outside \(|y|=36\), since

\[
|c|^2-\left(36+\frac16\right)^2
=\frac{2117}{9}>0.
\]

Hence \(|y_0|>36\).  Choose either square root \(x_0^2=y_0\) and put
\(t_0=x_0-7\).  The exact factorization proves \(L(w;t_0)=0\), while

\[
|t_0+7|=|x_0|=\sqrt{|y_0|}>6.
\]

This is the required strict algebraic counterexample.

For orientation only, one localized root is

\[
y_0\approx-26.4223522355+28.8791146449i,
\]

giving

\[
t_0\approx-4.4780703509+5.7255987801i,
\qquad |t_0+7|\approx6.2564055612.
\]

The decimals play no role in the certificate.

## Full length-10 search and symmetry audit

The discovery program visited all \(2^{10}=1024\) words without quotienting.
It found 272 orbits under complement and reversal (32 of size 2 and 240 of
size 4) and 272 distinct exact \(h^*\)-vectors.

Exact recurrence evaluation verified equality under complement and reversal
for all 1024 words.  Directed-cover-graph isomorphism checks found:

- complement: 1024/1024 pairs are isomorphic, agreeing with the paper;
- reversal: only 64/1024 pairs are isomorphic.

Thus reversal is an Ehrhart/\(h^*\) symmetry in this finite dataset, but it is
not generally a poset isomorphism.  The exhaustive result does not assume
reversal isomorphism.

Numerical localization flagged six words in two symmetry orbits.  The exact
certificate above covers the simpler regular-snake orbit
`LRLRLRLRLR`/`RLRLRLRLRL`; no assertion about the other orbit is needed to
disprove the conjecture.

All 1024 exact records, including \(h^*\), the 25 coefficients of \(24!L(t)\),
the shifted polynomial, the residual quintic, and coefficient hashes, are in
`experiments/breaker_length10_exact.jsonl`.  Numeric fields are explicitly
prefixed `numeric_`.

## Reproduction

Environment recorded by the run:

- Python 3.13.5;
- mpmath 1.3.0 (localization only);
- NetworkX 3.4.2 (symmetry audit only);
- macOS arm64.

Commands from the project root:

```bash
python discovery/breaker_exact_search.py --length 10 --dps 80
python -I discovery/breaker_verify_counterexample.py \
  experiments/breaker_counterexample_certificate.json
python discovery/breaker_test_rejections.py
```

Observed verifier status: `CERTIFIED_COUNTEREXAMPLE`.  All 8 deliberately
corrupted inputs were rejected.  No proof assistant (Lean, Coq, Isabelle, or
other) was used; the endpoint is certified by exact integer/rational arithmetic,
direct finite enumeration, and Rouché's theorem.

## Scope and files

This Breaker branch modified only files matching `discovery/breaker_*` and
`experiments/breaker_*`.  It did not modify status files, formal statements,
literature ledgers, manuscript files, or final-status files.
