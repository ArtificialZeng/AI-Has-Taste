# Exact computational cross-check at total positive-gap count t=15

Date: 2026-08-29.  This route did not assume the separate proposed exclusion
of the `t=15` stratum.  It used only the five-chain model, the already audited
Parseval deficit identity and one-chain deficit inequality, and the two
gap-count patterns supplied as the surviving input scope.

## Exact cardinality model

For a coordinate chain with strictly nested prefix-cut cardinalities

\[
1\le s_1<\cdots<s_\ell\le10,
\]

put

\[
r_i^2=\frac{s_i(11-s_{i+1})}{s_{i+1}(11-s_i)}.
\]

The exact one-chain spectral estimate gives

\[
\varepsilon\ge\Phi(s_1,\ldots,s_\ell)
=\sum_{i=1}^{\ell-1}\frac{2r_i}{1+r_i}.
\]

For every adjacent pair `(a,b)`, the certificate replaces its radical term
by the largest strict lower bound `N/10^9`.  The verifier checks this without
floating point using

\[
\frac{a(11-b)}{b(11-a)}>
\left(\frac{N}{2\cdot10^9-N}\right)^2
\]

and checks that `N+1` fails the same strict comparison.  Because the total
deficit at `t=15` is exactly five, a cardinality multiset is impossible when
the sum of these strict rational lower bounds is at least five.

Each chain is independently reversible, sending
`(s_1,...,s_l)` to `(11-s_l,...,11-s_1)`.  The enumeration retains the
lexicographically smaller representative.  Coordinates having equal chain
length may be permuted, so their cardinality types are enumerated as
multisets.  These are complete symmetry quotients: neither operation changes
any cut metric or gap feasibility.

The canonical type counts are 25, 60, and 110 for chain lengths two, three,
and four.  Exact reconstruction gives:

| gap-count pattern | cardinality multisets | survivors |
|---|---:|---:|
| `(3,3,3,3,3)` | 7,624,512 | 40 |
| `(4,3,3,3,2)` | 104,005,000 | 12 |

This is a necessary cut-cardinality reduction only.  Each of the 52 survivors
still contains many assignments of the eleven labels to coordinate levels.
No survivor is asserted feasible.

## Incidence/gap feasibility model

`t15_milp_feasibility.py` implements the original incidence equations for a
selected survivor.  Its variables are:

* binary prefix memberships `b[a,r]`, with exact cut cardinalities and chain
  nesting;
* binary pair separations `z[a,p] = b[a,i] XOR b[a,j]`;
* continuous gaps `g[a]` and products `w[a,p]=g[a]z[a,p]` using the exact
  binary-continuous product hull on `0<=g<=1`;
* the 55 exact distance equations `sum_a w[a,p]=1`.

Simultaneous label symmetry fixes the first coordinate's ordered blocks to
consecutive labels.  The positive-gap lower bound `epsilon` is only a MILP
discovery aid.  A returned binary incidence is never certified from the
floating MILP gaps: the script rebuilds its zero-one cut matrix, performs
`Fraction` Gaussian elimination on `A g = 1`, checks strict rational
positivity, and only then writes `t15_exact_candidate.json`.  The separate
`t15_verify_candidate.py` reconstructs both cut and direct-coordinate
distances from such a file.

The recorded run on balanced branch 0, whose five size sequences are all
`(1,5,10)`, used 1,830 variables, 5,988 constraints, `epsilon=10^-5`, and a
15-second HiGHS limit.  It returned no incumbent and status `time limit`.
The earlier same model at 120 seconds also returned no incumbent.  These are
not infeasibility results and do not conflict with either feasibility or the
separate proof route.

## Reproduction and audit

```bash
python3 experiments/t15_block_size_reduce.py
python3 certificate/t15_verify_block_size_reduction.py \
  certificate/t15_block_size_reduction.json

OPENBLAS_NUM_THREADS=1 experiments/.venv/bin/python \
  experiments/t15_milp_feasibility.py --pattern balanced --branch 0 \
  --time-limit 15 --output experiments/t15_milp_balanced0.json
```

The exact reduction verifier passed from outside the project under normal,
`-O`, `-I`, and explicitly invoked `-O -I`; a wrong-schema t16 certificate
failed with nonzero exit.  The first batched attempt at `-O -I` accidentally
passed the two flags as one zsh scalar and was rejected by Python; it was not
counted, and the explicit rerun passed.

Hashes:

* reduction input: `b65945cfc10c476971887f905b9dc2374cf7119cbb91a6f1a68ffa9750bdc5cc`;
* verifier: `febe7263a9e8687e932d868322e76f08349574de27b83ff2301b50ff58fc6aea`;
* recorded 15-second MILP diagnostic:
  `4b5ce5a52e08d017fa3001cc301ea24d416053827407f5d8764826dae0b988a2`.

No proof assistant was used.
