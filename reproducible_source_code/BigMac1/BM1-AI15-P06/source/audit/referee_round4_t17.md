# Gate 4, referee round 4: the \(t=17\) branch

Date: 2026-08-29  
Role: independent mathematical referee  
Audited proof: `proof/t17_branch.md`  
Proof SHA-256: `5332a2acc28a5407b3837c28fe4d007fae64d8031ad18a64e6b8177e32e856a3`  
Independent checker: `audit/referee_t17_check.py`  
Checker SHA-256: `f7352bb8e590e163fe8d5c3d8af8b6917a52114dfdbfb868957079cdc58b17c3`

## Verdict

**PASS.**  I found no fatal, major, or local mathematical issue in the
audited snapshot.  In particular, the repaired cost sequence is discretely
convex, all 66 bounded partitions are covered, the \(R=9\) sign obstruction
is valid, and the loss cases in Propositions 3--7 are exhaustive.

Conditional on the earlier audited endpoint \(t\ge17\), the proof establishes

\[
t\ge18,
\qquad \sum_{j=1}^5q_j\ge23.
\]

This remains a partial theorem.  No \(t\ge18\) stratum is eliminated, and
the proof does not settle \(e(\ell_1^5)=10\).  The target states these
limitations accurately.

## 1. The repaired chain costs

The current cost vector is

\[
\left(0,0,\frac2{11},\frac{24}{25},\frac{19}{10},
\frac{23}{8},\frac{193}{50},\frac{97}{20},\frac{146}{25}\right).
\]

Its exact increments are

\[
0,\ \frac2{11},\ \frac{214}{275},\ \frac{47}{50},\
\frac{39}{40},\ \frac{197}{200},\ \frac{99}{100},\
\frac{99}{100}.
\]

They are nondecreasing.  Thus the nonconvexity defect in the superseded
draft is absent from the audited `5332a2...` snapshot, and every
majorization step in Lemma 1 has the required direction.

The two new radical comparisons are also exact.  Because every quantity is
positive,

\[
\frac{12}{10^{1/6}+1}>\frac{97}{20}
\iff 10^{1/6}<\frac{143}{97}
\iff 143^6>10\,97^6,
\]

and

\[
\frac{14}{10^{1/7}+1}>\frac{146}{25}
\iff 10^{1/7}<\frac{102}{73}
\iff 102^7>10\,73^7.
\]

Both terminal integer inequalities hold.  The checker performs the integer
comparisons directly; no floating-point approximation is used.

## 2. Completeness of the 66 partitions

Independent enumeration of every nonincreasing five-tuple in
\(\{0,\ldots,8\}^5\) with sum seventeen gives exactly 66 distinct
partitions.  Exactly five have cost at most seven:

\[
\begin{array}{c|c}
(4,4,3,3,3)&167/25\\
(5,3,3,3,3)&1343/200\\
(4,4,4,3,2)&3763/550\\
(5,4,3,3,2)&15129/2200\\
(6,3,3,3,2)&3807/550.
\end{array}
\]

No partition has lower-bound cost exactly seven.  The cheapest excluded
partition is

\[
(5,4,4,2,2),\qquad
\frac{23}{8}+2\frac{19}{10}+2\frac2{11}
=\frac{3097}{440}>7.
\]

Consequently there is no missed equality boundary.  The prose split into
minimum at least three, exactly one two, at least two twos, minimum one, and
minimum zero is exhaustive; the exact enumeration independently confirms
the convexity argument for every boundary case.

## 3. The \(R\le9\) singleton obstruction

The \(R\le8\) portion is the already audited, post-fix compression theorem
from `proof/t16_branch.md`.  Its left-inverse step does not use a rank-equality
hypothesis.

For \(R=9\), if any \(c_r=0\), that same zero-set argument applies.  Suppose
instead that every \(c_r\ne0\).  On
\(V=\mathbf1^\perp\), the kernel equations are

\[
c_ru_r=\lambda\quad(1\le r\le11).
\]

They give nullity at most one.  Since \(V\) has dimension ten and
\(\operatorname{rank}C\le9\), nullity is exactly one, rank is nine, and a
nonzero kernel vector exists.  Its multiplier \(\lambda\) cannot vanish, so

\[
\sum_{r=1}^{11}\frac1{c_r}=0,
\qquad u_r=\frac1{c_r}
\]

after rescaling.

On \(V\), the quadratic form is
\(u^TCu=\sum_rc_ru_r^2\).  If two entries \(c_i,c_j\) were negative, the
vector \(e_i-e_j\in V\) would have negative quadratic value
\(c_i+c_j\), contradicting positive semidefiniteness.  Thus at most one
\(c_r\) is negative.  They cannot all be positive because their reciprocal
sum is zero, so exactly one is negative and ten are positive.

The kernel vector consequently has one negative component, ten positive
components, and total sum zero.  A nonempty subset omitting the negative
component has positive sum.  A proper subset containing it omits at least
one positive component and has sum equal to minus the omitted positive sum,
hence is negative.  Therefore no nonempty proper subset has sum zero.

For a kernel vector, positivity of every rank-one coefficient gives

\[
0=u^TCu=\sum_{a=1}^9g_a\langle v_{S_a},u\rangle^2,
\]

so each remaining proper cut would require
\(\sum_{r\in S_a}u_r=0\), which is impossible.  Repeated or complementary
cut copies cannot cancel a positive sum of squares.  This completes the
rank-nine obstruction.

The finite checker separately enumerates all \(11\cdot2^{11}=22528\)
choices of the unique-negative label and subset type, confirming that only
the empty and full subsets belong to the symbolic zero class.  The rank and
quadratic-form argument above remains an independent human proof, not a
claim of machine formalization.

## 4. Endpoint penalties and all loss cases

For all increasing prefix-size tuples of lengths two through six, the
checker evaluates

\[
\theta^2=\frac{a(11-b)}{b(11-a)}
\]

and compares the Jensen endpoint bound to each rational target after raising
only positive quantities to integer powers.  It checks respectively
\(45,120,210,252,210\) tuples.  The minimum nonregular squared ratio is
\(1/45\), and the minimum with neither singleton endpoint is \(4/81\), in
every length where it is used.

The two new endpoint comparisons reduce to

\[
4\,19^8>81\,13^8,
\qquad 3^{10}>45\,2^{10},
\]

and both hold.  The non-strict double bounds \(2/11\) and \(4/11\) are kept
non-strict; all relevant displayed totals still exceed seven strictly.

For completeness, each chain was independently assigned one of the three
exhaustive endpoint-loss categories:

* regular: two singleton endpoint copies;
* nonregular with one singleton endpoint;
* nonregular with neither singleton endpoint.

All \(3^5=243\) assignments were checked for each surviving partition.
Exact results are:

| Proposition/pattern | Deficit-compatible assignments | Minimum singleton copies | Maximum \(R=17-s\) |
|---|---:|---:|---:|
| 3: \((4,4,3,3,3)\) | 19 | 8 | 9 |
| 4: \((5,3,3,3,3)\) | 16 | 8 | 9 |
| 5: \((4,4,4,3,2)\) | 6 | 9 | 8 |
| 6: \((5,4,3,3,2)\) | 3 | 9 | 8 |
| 7: \((6,3,3,3,2)\) | 2 | 9 | 8 |

This confirms every loss-case conclusion in Propositions 3--7, including:

* the three possible counts \(0,1,2\) of nonregular quadruples in
  Proposition 3;
* both locations of an additional loss after a no-endpoint triple in
  Propositions 3--4;
* all four possible two-loss length pairs
  \((4,4),(4,3),(4,2),(3,2)\) in Proposition 5;
* the separately allowed quadruple or double loss, but not both, in
  Proposition 6;
* the only surviving optional loss being in the double in Proposition 7.

For the two “neither endpoint” statements abbreviated in Proposition 6, the
exact cheapest sums are also above seven: replace the quadruple's general
\(19/10\) by \(9/4\), or the double's general \(2/11\) by \(4/11\), while
leaving every other chain at its general bound.  The exhaustive checker
includes these cheaper cases rather than retaining an unnecessary second
loss.

Every surviving partition has exactly
\(\sum_j(\ell_j-2)=17-10=7\) forced internal non-singleton copies, so
\(R\ge1\) (indeed \(R\ge7\)).  Together with the singleton minima above,
all five patterns satisfy \(R\le9\), precisely the range excluded by
Lemma 2.

## 5. Fail-closed checker matrix

The checker uses only the Python standard library, integers, and
`fractions.Fraction`.  It imports no project verifier, frame audit, runner,
log, or discovery result.  It pins the proof hash and has zero
`ast.Assert` nodes.  Every decisive condition raises an explicit exception
and exits nonzero on failure.

It was run from `/tmp`, outside the project directory, in four modes:

```bash
t17_script='/Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/06_kusner_l1_5_equilateral/audit/referee_t17_check.py'
cd /tmp
python3 "$t17_script"
python3 -O "$t17_script"
python3 -I "$t17_script"
python3 -O -I "$t17_script"
```

All four executions returned `status: PASS` with byte-identical JSON.  Each
reported 66 partitions, five survivors, 243 loss assignments per pattern,
22528 symbolic sign-subset cases, the pinned `5332a2...` proof hash, and zero
AST assert nodes.

## 6. Post-fix \(t=16\) checker

The original `audit/referee_t16_check.py` correctly fails closed because it
pins the superseded pre-fix proof hash.  Per the audit instruction, it was not
edited.  A new snapshot checker was created:

`audit/referee_t16_check_postfix.py`  
SHA-256: `12108c0614bf59e54403d7936821d0f23414927cc99fd1c4fe4a2b4008b66b69`

An exact textual diff against the old checker contains one changed line only:
the expected proof hash is updated from `2cdf4ec...` to the post-fix hash
`114d861529243e3eb96415e10f14920370b91f5085d1538fc0bb0f564e26d889`.

It too was run from `/tmp` in normal, `-O`, `-I`, and `-O -I` modes.  All
four outputs were byte-identical and returned `status: PASS`, including 48
partitions, the three expected \(t=16\) survivors, all endpoint-category
checks, and zero AST assert nodes.

## Issue ledger

| Severity | ID | Verdict |
|---|---|---|
| Fatal | -- | None in the audited snapshot. |
| Major | -- | None; the superseded nonconvex cost sequence is repaired. |
| Local | -- | None. |
| Scope, not a defect | R4-T17-OPEN | All \(t\ge18\) strata remain untreated. |
| Dependency, not re-audited here | R4-T17-IMPORT | The endpoint \(t\ge18\) is conditional on the earlier audited \(t\ge17\) result and imported chain-deficit machinery. |

## Proof-assistant disclosure

No proof assistant (Lean, Coq, Isabelle, HOL, or comparable system) was used.
The Python programs are exact finite arithmetic/enumeration checkers.  They do
not constitute a formal proof of the compression/rank lemma.
