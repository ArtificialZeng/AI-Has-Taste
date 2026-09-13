# Resolution dossier: `nu(4,4)=15`

## Exact statement

With the definitions frozen in `source.md` and `problem.md`,

\[
\nu(4,4)=15.
\]

Equivalently, every label `|4A|` arising from a four-element integer set has
a four-element representative in `[0,15]`, and 15 is the least endpoint with
that property. This assertion is only for `(h,k)=(4,4)`; it does not settle
the all-`h` question.

## Primary-source dependency and finite reduction

The downloaded primary record `evidence/2609.01690v1.html` is Henry Shin,
*Iterated-sumset spectra: The complete exponent law and its rank geometry*,
arXiv:2609.01690v1. Immediately before Corollary 10.5 it defines

\[
\nu(h,4)=\min\{D\geq0:\mathcal R(h,4)=\mathcal R_D(h,4)\}.
\]

Theorem 10.3 gives
`D_h^max=binom(h+2,2)+1_{2 does not divide h}`, and Corollary 10.5 gives

\[
D_h^{\max}\leq\nu(h,4)\leq\max\{h^2,D_h^{\max}\}.
\]

At `h=4`, these are the two independently needed bounds

\[
15\leq\nu(4,4)\leq16. \tag{1}
\]

The sets `R_D(4,4)` are monotone in `D` and are always contained in
`R(4,4)`. The upper bound in (1), together with the definition of `nu`,
therefore implies

\[
\mathcal R_{16}(4,4)=\mathcal R(4,4). \tag{2}
\]

Thus it remains only to decide whether `R_15(4,4)=R_16(4,4)`.

## Exhaustive coefficient-vector calculation

For an increasing alphabet `B=(b_0,b_1,b_2,b_3)`, every four-term sum from
`B`, with repetition allowed, has the form

\[
c_0b_0+c_1b_1+c_2b_2+c_3b_3,
\qquad c_i\in\mathbb Z_{\geq0},\quad \sum_i c_i=4,
\]

and every such coefficient vector gives a four-term sum. There are exactly
`binom(7,3)=35` vectors. Consequently the cardinality of the set of these 35
exact integer dot products is exactly `|4B|`.

`evidence/coefficient_vector_recheck.py` implements this description without
enumerating tuples of summands and without importing `itertools`. Four nested
strictly increasing loops enumerate every four-subset of `[0,D]` exactly once.
Their observed totals equal the theoretical coverage counts

\[
\binom{16}{4}=1820\quad(D=15),\qquad
\binom{17}{4}=2380\quad(D=16).
\]

The exact-integer output `evidence/coefficient_vector_recheck.json` records all
35 coefficient vectors, label frequencies whose totals are 1820 and 2380,
and a range-checked witness with recomputed label for every attained value. It
gives, for both endpoints, the same complete label set

\[
\{13,16,17,19,21,23,24,25,26,27,29,30,31,32,33,34,35\}. \tag{3}
\]

In particular, both set differences are empty. The output assertions
`equal_label_sets`, `all_coverage_checks`, and `all_witness_checks` are all
true. This recomputation is structurally distinct from
`evidence/triage_enumeration.py`, which enumerates nondecreasing tuples of
summands using `itertools.combinations_with_replacement`. The two separately
produced JSON records agree on both complete label lists.

By (2) and (3), `R_15(4,4)=R_16(4,4)=R(4,4)`, so `nu(4,4)<=15`. The lower
bound in (1) gives the reverse inequality. Hence `nu(4,4)=15`.

## Reproduction and integrity

Run the decisive certificate with the mandated interpreter:

```sh
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python \
  evidence/coefficient_vector_recheck.py \
  --output evidence/coefficient_vector_recheck.json
```

At the research handoff, SHA-256 digests were:

- `source.md`: `093883054c665b367e5363739e6d5a5563e0959b8a39c6d2b288fc3401932be6`
- coefficient program: `efeada981d1ea6a1aa564fe71f84c09d70af8ddb3a75e5fee46a27453b00944f`
- coefficient output: `5d6da4da9eeb1989ca67a1c99557f2660f0fd1f823cd8ede35662efa7591716d`
- Shin HTML: `453e39bc6fc2773e50582eed117b46986f75341010fea1abc1db3a18bd506d60`
- Zhang HTML: `def8da9ca7df2e381284f9fc175ffb5e0e372ce806d05927cf9643656c061a94`

## Literature/status boundary and gap list

Shin's current arXiv record was still v1 on 2026-09-09 and states the general
endpoint-sharp question immediately after Corollary 10.5. The downloaded
Enkai Zhang record `evidence/2609.08915v1.html`, Remark 5.2 and Question 12.5,
also states that the label-level question is not answered by the weak-type
result. Bounded exact-phrase searches of current arXiv records found no later
separate resolution of this instance. This search is not exhaustive and no
priority claim is made.

Known mathematical gaps in the stated `(4,4)` deduction: none. The result is
a researcher-proposed computational proof and still requires the workflow's
fresh mathematical referee; no audit acceptance is asserted here.
