# Gate 5 Breaker / Counterexample Hunter Report

## Outcome and scientific limitation

No tree with \(\Delta(T)>0\) was found in the exact search domains below.
This is **negative discovery evidence only**, not a proof of the conjecture and
not a certified extension of the published finite frontier.  In particular,
the grammar and mutation phases are not exhaustive over their vertex ranges.

Two natural proof shortcuts were refuted by exact small witnesses, and two
root-state synchronization hypotheses were refuted by actual rooted trees.
Thus a Builder proof cannot use bare unimodality closure or a naive rooted
mode/ratio interlacing assumption.

Discovery and verification are separated:

- `discovery/breaker_search.py` performs the search with exact integer rooted
  DP and serializes retained trees, edge lists, full coefficient sequences,
  exact \(\Delta\), and exact rational discovery scores.
- `discovery/breaker_verify.py` imports no discovery code.  It validates each
  serialized edge list as a simple tree, roots at a different vertex, rebuilds
  the two root states with sparse degree dictionaries, and recomputes
  \(\Delta\) by an exact suffix-max reformulation of its literal definition.
- `discovery/breaker_run.json` is the full run record.  Its SHA-256 is
  `00adaa9ec1b1773449a96c257d5ee676994c5f95ea3eda280c45b90ab60dea86`.
- `discovery/breaker_verify_output.json` records the independent PASS result.

No proof assistant was used.

## Exact conventions and self-tests

For a rooted tree, the discovery evaluator uses

\[
 A=\prod_j(A_j+B_j),\qquad B=x\prod_jA_j,\qquad I=A+B
\]

over Python arbitrary-precision integers.  Unimodality is decided only by
exact coefficient comparisons.  The decision statistic is

\[
 \Delta=\max_{k<\ell<m}\min(i_k-i_\ell,i_m-i_\ell),
\]

computed exactly.  A normalized local reversal score

\[
 \max_{r<s}\min\left(
   \frac{i_r-i_{r+1}}{i_r+i_{r+1}},
   \frac{i_{s+1}-i_s}{i_{s+1}+i_s}
 \right)
\]

was used only to guide retention; it is positive exactly for a descent
followed by a later ascent, but zero can also come from a plateau.  It is never
used as a certificate.

Hand checks in the executable cover \(K_1\), \(K_2\), \(P_3\), a deliberately
nonunimodal integer sequence, and the published-style 26-vertex
\((3,4,4)\) path-arm tree.  The latter was reconstructed as

\[
(1,26,300,2040,9142,28551,63933,103736,121376,100144,
55499,18683,2979,51,1).
\]

It is unimodal but fails log-concavity at \(k=13\), since

\[
51^2-2979\cdot1=-378<0.
\]

This provides a regression test that the structured search reaches the known
non-log-concave regime without confusing log-concavity failure with a valley.

## Exact search domains

All counts below are read from `discovery/breaker_run.json`; elapsed time is
recorded there as 148.516227 seconds under Python 3.14.7 on macOS arm64 with
seed `99320260829`.

1. **Small rooted-tree audit.**  Generated every unlabeled rooted tree through
   order 12 by the unique unordered child-multiset grammar.  Per-order counts
   were checked against
   \(1,1,2,4,9,20,48,115,286,719,1842,4766\), for 7,813 rooted types total.
   All resulting total independence sequences were unimodal.  This phase was
   used principally to attack rooted-state lemmas; it does not improve the
   already reported global finite frontier.

2. **Repeated hub--gadget family.**  For each of all 486 rooted types of order
   at most 9, attached \(m=2,\ldots,80\) identical copies to a new hub.  This
   is 38,394 exact parameter points, with orders up to 721.  No positive
   \(\Delta\) occurred.

3. **Galvin-style spherically symmetric family.**  Searched the full box
   \(1\le m,t\le50\) (2,500 points) using the exact formula
   \[
   I_{m,t}(x)=\big((1+2x)^t+x(1+x)^t\big)^m+x(1+2x)^{mt}.
   \]
   Orders range up to 5,051.  No positive \(\Delta\) occurred.

4. **Known-style three-arm family.**  Searched every
   \((3,k,k+d)\) with \(4\le k\le120\) and \(0\le d\le10\), 1,287 exact
   points.  Here each branch vertex supports the stated number of pendant
   length-two paths.  No positive \(\Delta\) occurred.

5. **Fixed-order subtree prune--regraft.**  At each of
   \(n\in\{31,40,60,100,150\}\), ran five fixed-seed restarts of 3,000 exact
   proposals, for 75,000 evaluated trees.  A move detaches a rooted subtree
   and reattaches it outside itself, preserving connectedness and acyclicity.
   No positive \(\Delta\) occurred.  The best tree at each order is serialized
   with its edge list and full coefficient sequence.

6. **Spherically symmetric grammar.**  Proposed 5,000 fixed-seed branching
   words of depth 2--9 over \(\{1,2,3,4,5\}\), augmented by the words
   \(2^m1^n\) for \(1\le m\le6\), \(1\le n\le12\).  After exact de-duplication
   and the size cutoff \(n\le600\), 1,570 trees remained.  No positive
   \(\Delta\) occurred.

The closest retained normalized local-reversal score was in the Galvin box at
\((m,t)=(49,50)\), order 4,950, at adjacent slopes 1633 and 1634.  Its score is
approximately \(-4.58926372045\times10^{-4}\); the exact numerator and
denominator, edge list, and all 2,500 coefficients are in
`discovery/breaker_run.json`.  Its exact global statistic is
\(\Delta=-4949\).  The negative sign means it is not a counterexample; the
decimal is only a navigation summary of the exact rational value.

## Refuted closure and rooted-state lemmas

### Bare sum closure is false

Both

\[
a=(1,1,2),\qquad b=(2,1,1)
\]

are positive unimodal sequences, while

\[
a+b=(3,2,3)
\]

has \(\Delta=1\), witnessed by \((k,\ell,m)=(0,1,2)\).  Therefore the
decomposition \(I=A+B\) cannot be closed using unimodality of the two summands
alone.

### Bare convolution closure is false

Both

\[
a=(1,1,2),\qquad b=(1,1,3)
\]

are positive unimodal sequences, while

\[
a*b=(1,2,6,5,6)
\]

has \(\Delta=1\), witnessed by \((2,3,4)\).  These two algebraic witnesses
are not asserted to be tree independence sequences; their precise force is
that unimodality by itself supplies no sum or product closure theorem.

### Root ratio monotonicity is false for an actual tree

Take the four-vertex star with edge list

```text
0 1
1 2
1 3
```

and root it at leaf 0.  Exact rooted states are

\[
A=(1,3,1),\qquad B=(0,1,2,1).
\]

Thus the positive-support ratios \(B_{k+1}/A_k\) are

\[
1,\quad 2/3,\quad 1,
\]

so the plausible claim that these ratios are nonincreasing fails between
\(k=1\) and \(k=2\).

### Root mode synchronization is false for an actual tree

Take \(K_{1,6}\) rooted at its center, with edges \(0j\), \(1\le j\le6\).
Then

\[
A=(1,6,15,20,15,6,1),\qquad B=(0,1).
\]

The leftmost modes are 3 and 1, respectively.  Hence even the weak assertion
that the two rooted-state modes always differ by at most one is false.

These witnesses do not refute a more carefully formulated total-positivity,
ratio, or synchronized-mode invariant.  They delimit what such an invariant
must add beyond raw unimodality and a naive one-step interlacing condition.

## Reproduction and independent verification

From the project root:

```bash
python3 -m py_compile discovery/breaker_search.py discovery/breaker_verify.py
python3 discovery/breaker_search.py --output discovery/breaker_run.json
python3 discovery/breaker_verify.py discovery/breaker_run.json
```

The verifier returned `PASS`, independently reconstructed nine retained
explicit trees of orders 26 through 4,950, and certified zero serialized
counterexamples.  The run/verifier hashes are recorded in
`discovery/breaker_verify_output.json`.

## Breaker handoff

The strongest actionable conclusion is adversarial rather than terminal:

- the conjecture survives the specified structured and mutation searches;
- parameter amplification of the tested non-log-concave path-arm families did
  not create a valley in the registered boxes;
- any positive proof route must use more than arbitrary unimodal sum/product
  closure and more than naive root-state mode or likelihood-ratio interlacing;
- no finite or infinite theorem, and no counterexample, is claimed here.
