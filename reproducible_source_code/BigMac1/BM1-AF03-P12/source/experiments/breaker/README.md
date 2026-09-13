# Exact breaker/certifier for 3-packed plactic stability

## Outcome and exact limitation

No counterexample was found in any certified finite range below.  This is **not**
a proof that every 3-packed word is 3-stable.  The strongest single certified
box is exactly

\[
\begin{gathered}
u\in[3]^n\text{ is 3-packed},\quad 3\le n\le8,\\
w\in[3]^\ell,\quad0\le\ell\le16,\\
3\le k\le20,
\end{gathered}
\]

and, in that box, the exhaustive computation found

\[
  [w\in C(u^k)]=[w\in C(u^{k+1})]
\]

for every quantified triple.  A separate expansion permits letters 4 and 5
in `w`, but only through length 7.  Another separate expansion permits `u`
through length 10, but only takes `w` in `[3]` through length 10.  These boxes
must not be combined into an uncomputed rectangular range.

## Source baseline and numbering correction

The primary preprint is Bruce E. Sagan and Chenchen Zhao, *Properties of
plactic monoid centralizers*, arXiv:2512.21401v1 (24 December 2025), later
published with DOI `10.1007/s00233-026-10652-4`.  On pages 14--15 of the
preprint, the packed-word claim is **Conjecture 3.8**, not Conjecture 4.6.
Conjecture 4.6 is a different log-concavity conjecture.  The authors report
testing all `m=3,4` packed `u` of length at most 8, `w` over `[m]` of length at
most 10, and adjacent powers for `m <= k <= 14`.

Primary sources:

- <https://arxiv.org/abs/2512.21401>
- <https://doi.org/10.1007/s00233-026-10652-4>

Only the `m=3` part is reproduced here, because this project is specifically
the first new alphabet `m=3`.

## Why enumeration by tableaux is exhaustive

Knuth equivalence is a monoid congruence and `x` and `y` are Knuth equivalent
if and only if `P(x)=P(y)`.  Consequently:

1. replacing `u` by a word with the same insertion tableau does not change
   any power `u^k` in the plactic monoid;
2. replacing `w` by a word with the same insertion tableau does not change
   either `P(u^k w)` or `P(w u^k)`;
3. content, hence the 3-packed condition, is constant on a plactic class.

It is therefore sufficient and necessary, in each finite word-length and
alphabet box, to check one row-reading representative of every semistandard
Young tableau.  This is an exact quotient, not sampling.

For alphabet `[3]`, `coordinate_discovery.cpp` uses the explicit six-coordinate
normal form

```text
row 1: 1^a 2^b 3^c
row 2:     2^d 3^e
row 3:         3^f
```

where all coordinates are nonnegative and precisely

```text
d <= a,   d + e <= a + b,   f <= d.
```

The packed restriction is `a>0`, `b+d>0`, and `c+e+f>0`.  Thus the long-`w`
run enumerates integer six-tuples directly and never enumerates the `3^16`
raw words.

## Separation of discovery and certification

- `discovery.cpp` uses ordinary row bumping and discovers classes from all raw
  words in the requested finite box.
- `coordinate_discovery.cpp` uses row bumping but discovers `[3]` tableaux
  directly from the six integer coordinates.
- `verifier_core.cpp` shares no source with either discovery program.  It
  enumerates partitions and all valid SSYT fillings directly, and evaluates
  `P(x)` by **column insertion of the reversed word**.
- `verify_finite.py` parses the sealed JSON fail closed, checks all artifact
  hashes, compiles `verifier_core.cpp` in a fresh temporary directory, rebuilds
  every membership bit, and compares the SHA-256 of the entire bit stream.
- `verify_counterexample.py` is a small no-import witness verifier.  If a
  membership change is found, it checks the literal integer words, the
  3-packed condition, both exponents (at least 3), and both tableaux from
  scratch using reverse-word column insertion.

The trace stores every Boolean membership, not merely the number of failures.
Bits are ordered by `u` length/tableau key, then `w` length/tableau key, then
exponent, packed most-significant-bit first and padded with zeros in the last
byte.

## Certified runs

| Run | Exact range | Plactic class pairs | Adjacent comparisons | Changes | Discovery time | Result SHA-256 | Trace SHA-256 |
|---|---|---:|---:|---:|---:|---|---|
| Author `m=3` baseline | `3<=|u|<=8`, `u` 3-packed; `w in [3]^{<=10}`; `3<=k<=14` | 872,298 | 10,467,576 | 0 | 5.15 s | `4a85a72f0ed239f87b44605df11cf803d9010b03be546f01e31716c96e577df0` | `7d601f31b2abcb672dc034a9fc26a372029c7f088162d1e268c3975e2730be09` |
| Larger `w` alphabet | `3<=|u|<=8`; `w in [5]^{<=7}`; `3<=k<=20` | 3,724,896 | 67,048,128 | 0 | 28.80 s | `fe016215c0979cabc4155f8a9829d80120d0e98c6c48cb531c304b91ed7ea1d2` | `64ab2d93cd0fdabcc12a781a25accd2bbbd93deb8276f9538a9ea6df20a7ba16` |
| Longer `u` | `3<=|u|<=10`, `u` 3-packed; `w in [3]^{<=10}`; `3<=k<=20` | 2,447,130 | 44,048,340 | 0 | 25.98 s | `e2745b8638ba04e5dbb90c920a95141f842ec12a20db5a887ddf46a7e185bb03` | `75d55758438c1a8005b5579e1e8ee4bde80abacfa72018c8d492b97f9b6d185b` |
| Six-coordinate longer `w` | `3<=|u|<=8`; `w in [3]^{<=16}`; `3<=k<=20` | 6,869,709 | 123,654,762 | 0 | 62.13 s | `87bb4fc835f37ee7b562f091db62ac19df485afff883d5a03d0af276a3cad960` | `322df3942b69882f1092657ec2490fd34367ba4c1b8bc337b8eb7a17d68c52e6` |

Times are diagnostics from this machine and are not part of any certificate.
Each result JSON records the per-length class counts.  For example, the
six-coordinate run has 483 packed `u` classes and 14,223 `w` classes.

The raw-word and six-coordinate discovery programs were also run on the same
author-baseline box; `cmp` confirmed their 1,417,485-byte traces are identical.

## Reproduction

All commands start in this directory.

```bash
make test
```

Author baseline:

```bash
./discovery \
  --u-min-length 3 --u-max-length 8 \
  --w-alphabet 3 --w-max-length 10 \
  --k-first 3 --k-last 14 \
  --trace runs/baseline/trace.bin \
  --result runs/baseline/result.raw.json
python3 seal_run.py \
  --raw runs/baseline/result.raw.json \
  --trace runs/baseline/trace.bin \
  --discovery-source discovery.cpp \
  --output runs/baseline/result.json
python3 verify_finite.py runs/baseline/result.json --source-dir .
```

Six-coordinate long-`w` box:

```bash
./coordinate_discovery 3 8 16 3 20 \
  runs/coordinate_w16/trace.bin \
  runs/coordinate_w16/result.raw.json \
  coordinate_w16
python3 seal_run.py \
  --raw runs/coordinate_w16/result.raw.json \
  --trace runs/coordinate_w16/trace.bin \
  --discovery-source coordinate_discovery.cpp \
  --output runs/coordinate_w16/result.json
python3 verify_finite.py runs/coordinate_w16/result.json --source-dir .
```

Other exact commands are obtained from the baseline command by these argument
changes:

```text
extended_alpha: --u-max-length 8 --w-alphabet 5 --w-max-length 7 --k-last 20
extended_u:     --u-max-length 10 --w-alphabet 3 --w-max-length 10 --k-last 20
```

The four sealed results, traces, stdout logs, independent verification logs,
and `SHA256SUMS` files are under `runs/`.

## Unit and rejection tests

`make test` currently runs eleven tests.  They include:

- hand-computed tableaux and Knuth moves, including repeated-letter cases;
- exhaustive agreement of row insertion and reverse-word column insertion for
  all words over `[3]` of length at most 6;
- a small exhaustive finite result rebuilt by the no-import verifier;
- rejection of a falsified membership bit, a missing field, a non-packed `u`,
  a Boolean disguised as an exponent, an unexpected trusted tableau, and a
  tampered finite-trace digest.

The verifier accepts no discovery-supplied tableau or objective value as
trusted input.  Malformed, incomplete, extra-field, unsafe-path, hash-mismatch,
and recomputation-mismatch inputs are rejected with a nonzero exit code.

## Environment

The recorded runs used Apple command-line `c++` with
`-std=c++20 -O3 -Wall -Wextra -Wpedantic` and Python 3.9.6 for sealing and
verification orchestration.  All decisive objects and comparisons are finite
integer/combinatorial data; no floating point, random seed, heuristic cutoff,
SAT oracle, or proof assistant is used.  The reported wall times are the only
floating-point fields, are explicitly marked diagnostic, and do not enter the
claim.
