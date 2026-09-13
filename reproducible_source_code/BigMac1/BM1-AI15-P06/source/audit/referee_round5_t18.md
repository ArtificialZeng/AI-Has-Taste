# Gate 4, referee round 5: the \(t=18\) branch

Date: 2026-08-29  
Role: independent mathematical referee  
Audited proof: `proof/t18_branch.md`  
Frozen proof SHA-256: `2a50ff367e65652e43e58a44319a86fdff61e04ca41b106260e192c6ee3f20c9`  
Independent checker: `audit/referee_t18_check.py`  
Checker SHA-256: `90895d6fea54ff722c16c1d360d0ed8fd7cedeca8779fbbd3a549e9968975903`  
External matrix log: `logs/referee_t18_check_matrix.json`  
Log SHA-256: `de8252d3e184357d889bc68e9cfc3503c3b87aa2255a5dc14536fbb9e0810d16`

## Verdict

**PASS.**  I found no fatal, major, or local mathematical issue in the
frozen snapshot.  The 88-to-8 partition reduction is complete; every entry
and strictness convention in Tables (13)--(17) checks exactly; the eight loss
minima are exhaustive; and the \(R=10\) basis, positivity, inverse, antichain,
and chain-orientation arguments are valid.

Conditional on the previously audited endpoint \(t\ge18\) and the imported
rank-nine compression lemma, the proof establishes exactly

\[
\boxed{t\ge19}.
\]

It does not exclude any \(t\ge19\) stratum, construct eleven points, or prove
\(e(\ell_1^5)=10\).  The original problem therefore remains open.  This
limitation is stated accurately in the proof.

## 1. Chain costs and all 88 partitions

For \(t=18\), the Naimark chain bound gives \(0\le\ell_j\le9\).  The new
cost

\[
c_9=\frac{683}{100}
\]

is valid because, with all quantities positive,

\[
\frac{16}{10^{1/8}+1}>\frac{683}{100}
\iff 10^{1/8}<\frac{917}{683}
\iff917^8>10\,683^8.
\]

The exact difference is

\[
917^8-10\,683^8=26432594300827948436631>0.
\]

The complete cost-increment sequence is

\[
0,\ \frac2{11},\ \frac{214}{275},\ \frac{47}{50},\
\frac{39}{40},\ \frac{197}{200},\ \frac{99}{100},\
\frac{99}{100},\ \frac{99}{100},
\]

so discrete convexity has the claimed direction.

Independent enumeration of every nonincreasing five-tuple in
\(\{0,\ldots,9\}^5\) with sum eighteen gives exactly 88 distinct
partitions.  Exactly eight have lower-bound cost at most eight:

| Pattern | Exact cost |
|---|---:|
| \((4,4,4,3,3)\) | \(381/50\) |
| \((5,4,3,3,3)\) | \(1531/200\) |
| \((6,3,3,3,3)\) | \(77/10\) |
| \((4,4,4,4,2)\) | \(428/55\) |
| \((5,4,4,3,2)\) | \(17197/2200\) |
| \((5,5,3,3,2)\) | \(8637/1100\) |
| \((6,4,3,3,2)\) | \(2162/275\) |
| \((7,3,3,3,2)\) | \(8703/1100\) |

No partition has cost exactly eight.  The least expensive excluded partition
is \((5,5,4,2,2)\), at \(1763/220>8\).  The cheapest minimum-one and
minimum-zero cases are respectively \((5,4,4,4,1)\), at \(343/40\), and
\((5,5,4,4,0)\), at \(191/20\).  Thus the prose split by minimum entry and
multiplicity covers all boundary cases.

## 2. Endpoint Tables (13)--(17)

For endpoint sizes \(1\le a<b\le10\), direct centering gives

\[
\theta^2=\frac{a(11-b)}{b(11-a)}.
\]

The minimum among nonregular pairs is \(1/45\), and the minimum when neither
endpoint is singleton is \(4/81\).  For \(n=\ell-1\), comparing the Jensen
bound to a rational target \(L<2n\) is exactly equivalent to

\[
\theta^2\mathrel{\gtrless}
\left(\frac{L}{2n-L}\right)^{2n},
\]

with the same strict/non-strict relation.  This removes all radicals without
changing inequality direction.

The checker enumerates every increasing prefix-size tuple for lengths two
through seven: \(45,120,210,252,210,120\) tuples, respectively.  It verifies
all three endpoint-loss columns in Table (13), including the two non-strict
double-chain statements \(2/11\) and \(4/11\).

Direct integer recomputation gives Table (14):

\[
\begin{aligned}
289^4-45\,111^4&=144440596,\\
131^6-45\,69^6&=197595805636,\\
247^8-45\,153^8&=341257329895839316,\\
119^{10}-45\,81^{10}&=22373433354250690756,\\
139^{12}-45\,101^{12}&=1313742681350448050257876,
\end{aligned}
\]

and Table (15):

\[
7939,\quad3451,\quad1860063763,\quad
2410538918227,\quad8573882643.
\]

All are positive and exactly match the proof.  Subtracting the general
rational column from the one-loss and two-loss columns also reproduces every
entry in Table (17), with strictness retained exactly as displayed.

## 3. Exhaustiveness of the loss minima

For each of the eight patterns, the checker independently assigns every
coordinate a loss \(e\in\{0,1,2\}\), hence checks all \(3^5=243\) cases.
It preserves a separate strictness bit, so a rational lower sum of exactly
eight is rejected only when at least one constituent inequality is strict.
This matters for six assignments of pattern C; all six have strict actual
deficit greater than eight.

The exact reconstructed minima are:

| Pattern | General | Minimum for loss \(\ge2\) | Minimum for loss \(\ge3\) | Maximum compatible loss | Minimum singleton copies |
|---|---:|---:|---:|---:|---:|
| A | \(381/50\) | \(791/100\) | \(403/50\) | 2 | 8 |
| B | \(1531/200\) | \(1589/200\) | \(1619/200\) | 2 | 8 |
| C | \(77/10\) | \(799/100\) | \(407/50\) | 2 | 8 |
| D | \(428/55\) | \(438/55\) | \(8947/1100\) | 2 | 8 |
| E | \(17197/2200\) | \(17597/2200\) | \(17927/2200\) | 2 | 8 |
| F | \(8637/1100\) | \(8837/1100\) | \(4501/550\) | 1 | 9 |
| G | \(2162/275\) | \(2212/275\) | \(9013/1100\) | 1 | 9 |
| H | \(8703/1100\) | \(8903/1100\) | \(2267/275\) | 1 | 9 |

For A--C, a two-endpoint loss in a triple is cheapest; a third loss is
cheapest in another triple.  For D--H, the cheapest two losses lie in the
double, followed by a one-endpoint loss in the shortest remaining chain.
The proof's description is therefore exhaustive, including repeated chain
lengths and all ties.

Every surviving chain has length at least two.  A singleton prefix cut must
occur at a chain endpoint, so there are at most ten singleton copies and at
least eight.  Consequently

\[
8\le R=18-(\text{singleton copies})\le10.
\]

The imported rank-nine lemma excludes \(R=8,9\); the only new case is
\(R=10\).

## 4. The \(R=10\) basis identity

Fix a reference label \(p\), put \(W=[11]\setminus\{p\}\), and write
\(s_r=He_r\).  The ten vectors \((s_r)_{r\in W}\) form a basis of
\(V=\mathbf1^\perp\): if a vector supported on \(W\) is killed by \(H\),
it is constant on all eleven labels, while its \(p\)-coordinate is zero, so
it is zero.  Also \(s_p=-\sum_{r\in W}s_r\), since \(H\mathbf1=0\).

Therefore

\[
H\operatorname{diag}(c)H
=\sum_{r=1}^{11}c_rs_rs_r^T
=S(D_p+c_pJ)S^T,
\]

where \(S\) has the \(s_r\), \(r\in W\), as columns.  Orienting each
non-singleton cut away from \(p\) gives a side
\(U_a^{(p)}\subseteq W\).  Both sides of such a cut contain at least two
labels, so \(2\le|U_a^{(p)}|\le9\), and
\(v_{U_a}=S\mathbf1_{U_a}\).  Expressing both sides in this basis gives

\[
D_p+c_pJ=B_pGB_p^T.
\]

This derivation uses no orthonormality of the \(s_r\); full column rank of
\(S\) is sufficient.  The independent checker verifies all 121 symbolic
coefficient matrices for the eleven choices of \(p\) and all eleven
coefficients \(c_r\).

## 5. Positivity, invertibility, and determinant direction

For distinct \(i,j\in W\), the off-diagonal entry gives

\[
c_p=\sum_{a:i,j\in U_a^{(p)}}g_a\ge0.
\]

If \(c_p=0\), positivity of every \(g_a\) says that no binary column can
contain a pair of labels, so every column has size at most one.  This
contradicts \(|U_a^{(p)}|\ge2\).  Thus \(c_p>0\).  Since \(p\) was arbitrary,
all \(c_r>0\).

It follows that \(D_p+c_pJ\) is positive definite.  Since \(G\) is positive
diagonal and \(B_pGB_p^T\) has rank ten, the square matrix \(B_p\) is
invertible.  No circular use of invertibility occurs in the positivity step.

The matrix determinant lemma gives

\[
\det(D_p+c_pJ)
=\left(\prod_{r\ne p}c_r\right)
 \left(1+c_p\sum_{r\ne p}\frac1{c_r}\right)
=\left(\prod_{r=1}^{11}c_r\right)
 \left(\sum_{r=1}^{11}\frac1{c_r}\right).
\]

Taking determinants of the design identity therefore yields equation (23)
with the correct product and no missing sign.  Positivity makes the expression
independent of the reference label.

## 6. Sherman--Morrison and the antichain

Let

\[
s=\sum_{r\in W}\frac1{c_r},\qquad
\lambda=\frac{c_p}{1+c_ps}.
\]

Both are positive and

\[
0<\lambda s=\frac{c_ps}{1+c_ps}<1.
\]

Sherman--Morrison has the subtractive sign

\[
(D+c_pJ)^{-1}
=D^{-1}-\lambda D^{-1}JD^{-1}.
\]

From \(D+c_pJ=BGB^T\) and invertibility of \(B\), the correct congruence is

\[
G^{-1}=B^T(D+c_pJ)^{-1}B.
\]

Thus the off-diagonal \((a,b)\) entry, for two different cut copies, is

\[
0=x(U_a\cap U_b)-\lambda x(U_a)x(U_b),
\qquad x(X)=\sum_{r\in X}\frac1{c_r}.
\]

The right product is positive, so the blocks intersect.  If
\(U_a\subseteq U_b\), cancellation of \(x(U_a)>0\) gives
\(1=\lambda x(U_b)\le\lambda s<1\), a contradiction.  The reverse
containment is identical.  Hence every two indexed blocks intersect and are
incomparable.  Repeated block columns are included: equality would imply
both containments and is likewise impossible.

## 7. Chain orientation trichotomy

For two distinct prefix cuts \(P\subsetneq Q\) from one coordinate, the
reference label has exactly three possible positions:

1. If \(p\notin Q\), the oriented sides are \(P\subsetneq Q\).
2. If \(p\in P\), the oriented sides are
   \(Q^c\subsetneq P^c\).
3. If \(p\in Q\setminus P\), the oriented sides are \(P\) and \(Q^c\),
   which are disjoint.

These exhaust all possibilities.  Each conflicts with the intersecting
antichain conclusion, so a coordinate contributes at most one non-singleton
copy.  Five coordinates give \(R\le5\), contradicting \(R=10\).

The checker scans all \(3^{11}=177147\) ternary label assignments encoding
\(P\subseteq Q\), retains 171006 strict nontrivial nested pairs, and checks
all eleven reference labels, for 1881066 trichotomy cases.  It also checks
all 22264 non-singleton-cut/reference orientations and verifies the exact
size interval \([2,9]\).

## 8. Independent checker and tamper matrix

The checker uses only the Python standard library and exact integers/
`fractions.Fraction`.  It imports no project \(t=18\) verifier, manifest,
runner, frame checker, or cached result.  Its parsed AST contains zero
`ast.Assert` nodes; every failure uses an explicit exception and nonzero exit.

The checker and proof were copied to temporary directories under `/tmp` and
run in the following four modes:

```text
normal
python3 -O
python3 -I
python3 -O -I
```

The genuine frozen proof produced exit 0/PASS in all four modes.  A separate
copy with one newline appended to the proof produced exit 1/FAIL in all four
modes, with no PASS marker.  Thus all 8/8 expected outcomes were observed.
The tampered proof SHA-256 was
`422fb54aee5808a977488b50bbfcbe3097ffb48e733351548c8c0c839aea6b05`.

The JSON log records the actual commands, exit codes, and stdout/stderr hashes.
Its `external_workdir_inside_project` field is false.  Temporary paths are
ephemeral, but the frozen checker/proof hashes at the start of this report
make the run reproducible.

The program certifies the finite arithmetic, partition/loss enumeration,
symbolic basis coefficients, and set-orientation trichotomy.  The general
positive-definite, inverse, and antichain deductions were independently
reconstructed by hand in Sections 4--7 of this report and are not
misrepresented as formal machine verification.

## Issue ledger

| Severity | ID | Verdict |
|---|---|---|
| Fatal | -- | None in the frozen target. |
| Major | -- | None in the frozen target. |
| Local | -- | None in the frozen target. |
| Scope, not a defect | R5-T18-OPEN | The proof excludes only \(t=18\); every \(t\ge19\) branch remains open. |
| Dependency, not re-audited here | R5-T18-IMPORT | The conclusion \(t\ge19\) depends on the earlier audited \(t\ge18\) endpoint, frame reduction, deficit bounds, and rank-nine compression lemma. |

## Proof-assistant disclosure

No proof assistant (Lean, Coq, Isabelle, HOL, or comparable system) was used.
The accompanying Python program is an exact finite checker, not a
formalization of the real linear-algebra proof.
