# Exact resolution of the frozen \(\Gamma_{34}\)-orbit assertion

## Scope and conclusion

Let \(A,B\), the Gray map, and \(\Gamma_{34}(A,B)\) be exactly as frozen in
`source.md` and interpreted in `problem.md`.  Then **no ordered pair in
\(\Gamma_{34}(A,B)\) has all four Gray rows reversible**.  This disproves the
frozen existential assertion.  It says nothing about operations outside the
displayed definition of \(\Gamma_{34}\), and nothing about other length-34
qLPs.

## Paper-checkable obstruction

For a quaternary symbol \(z\), write its Gray image as \(g(z)=(p(z),q(z))\).
On the four symbols \(1,i,-1,-i\), this is a bijection onto
\(\{\pm1\}^2\).  Consequently, for any quaternary word \(X\), both Gray rows
are reversible if and only if

\[
X_j=X_{-j}\qquad(j\in\mathbb Z_{34}). \tag{1}
\]

Every member of the frozen orbit, whether exchanged or not, contains as one
of its two coordinates a word

\[
Z=\alpha c_r d_k(A^\varepsilon).
\]

Suppose that (1) held for \(Z\).  Cancelling the nonzero phase and, when
needed, applying conjugation to both sides gives

\[
A_{(j-r)k^{-1}}=A_{(-j-r)k^{-1}}\qquad(j\in\mathbb Z_{34}).
\]

Set \(u=(j-r)k^{-1}\).  Since multiplication by the unit \(k^{-1}\) is a
bijection, the preceding identities are equivalent to

\[
A_u=A_{a-u}\qquad(u\in\mathbb Z_{34}),
\quad a=-2rk^{-1}\pmod {34}. \tag{2}
\]

The residue \(a\) is even.  The following table gives, for every even residue
\(a\), one exact failure of (2).  Entries are the literal Appendix-A digits;
different digits represent different fourth roots of unity.

| \(a\) | \(u\) | \(A_u\) | \(a-u\pmod {34}\) | \(A_{a-u}\) |
|---:|---:|---:|---:|---:|
| 0 | 1 | 2 | 33 | 0 |
| 2 | 0 | 2 | 2 | 0 |
| 4 | 10 | 0 | 28 | 2 |
| 6 | 1 | 2 | 5 | 0 |
| 8 | 0 | 2 | 8 | 0 |
| 10 | 0 | 2 | 10 | 0 |
| 12 | 3 | 2 | 9 | 0 |
| 14 | 1 | 2 | 13 | 0 |
| 16 | 1 | 2 | 15 | 0 |
| 18 | 2 | 0 | 16 | 2 |
| 20 | 0 | 2 | 20 | 0 |
| 22 | 0 | 2 | 22 | 0 |
| 24 | 0 | 2 | 24 | 0 |
| 26 | 3 | 2 | 23 | 0 |
| 28 | 1 | 2 | 27 | 0 |
| 30 | 0 | 2 | 30 | 0 |
| 32 | 1 | 2 | 31 | 0 |

Thus no permitted transform of \(A\) has both Gray rows reversible.  Pair
exchange only changes which coordinate contains that transform, so no orbit
pair can have all four rows reversible.  This proves the conclusion.

## Preservation of the qLP equations

For completeness, with
\(\operatorname{PAF}(X,h)=\sum_jX_j\overline{X_{j+h}}\), direct reindexing
gives

\[
\begin{aligned}
\operatorname{PAF}(\alpha X,h)&=\operatorname{PAF}(X,h),\\
\operatorname{PAF}(c_rX,h)&=\operatorname{PAF}(X,h),\\
\operatorname{PAF}(d_kX,h)&=\operatorname{PAF}(X,hk^{-1}),\\
\operatorname{PAF}(\overline X,h)&=
  \overline{\operatorname{PAF}(X,h)}.
\end{aligned}
\]

Independent phases and shifts therefore preserve each summand, common
decimation permutes the nonzero lags, simultaneous conjugation fixes the real
sum \(-2\), and exchange swaps the two summands.  Hence every displayed
generator preserves the qLP equations.  The exact checker also evaluates the
given \((A,B)\) over Gaussian integers at all 33 nonzero lags.

## Complete census and reproducible certificate

`orbit_census.py` is independent of the intake checker.  It represents fourth
roots by exponents modulo 4 and enumerates all

\[
4\cdot4\cdot34\cdot34\cdot16\cdot2\cdot2=1{,}183{,}744
\]

displayed parameter tuples, including exchange.  An ordered image is encoded
as 34 ASCII digits, `|`, 34 ASCII digits, and newline.  Lexicographically
sorting the distinct encodings gives:

- distinct ordered images: **1,183,744**;
- multiplicity: **1 for every image**;
- canonical orbit SHA-256:
  `633befce04711dc130f011ee6ede35e32347be63a53719933e625545d270817e`;
- fully Gray-reversible images: **0**.

For each canonical image,
`orbit_failure_witnesses.jsonl.gz` records the first failing row in the fixed
order `first.p`, `first.q`, `second.p`, `second.q`, followed by the least
\(j\in\{0,\ldots,33\}\) with unequal values at \(j\) and \(-j\).  It has
1,183,744 image records.  Its compressed SHA-256 is
`636a51bd42360d70e7b9d18805ce65ef2ac6e563df3ddfd9e1f5ceb5f1c38019`;
the uncompressed JSONL stream SHA-256 is
`95ee5c29a52d5d1974bc427532a9a45b006bf541f5394df6bd819a27f6f49be5`.

`verify_orbit_census.py` imports no census code.  It instead composes literal
string conjugation, decimation, shift, and phase operations, reconstructs the
full parameter domain, obtains the same sorted orbit and digest, and recomputes
and compares every one of the 1,183,744 witness records.  Its successful result
is in `orbit_census_verification.json`.

Reproduction from the project root:

```sh
python3 evidence/orbit_census.py
python3 evidence/verify_orbit_census.py
```

All decisive arithmetic is exact.  The proof above has no known mathematical
gap; candidate status still requests a fresh referee and is not acceptance.
