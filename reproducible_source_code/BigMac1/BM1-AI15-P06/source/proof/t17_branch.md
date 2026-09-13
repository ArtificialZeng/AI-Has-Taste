# The \(t=17\) branch: the rank-nine singleton obstruction

Date: 2026-08-29  
Role: proof builder  
Scope: exact analysis of \(t=17\) only  
Freeze discipline: no earlier proof, verifier, frame, runner, or log is edited  
Novelty: not assessed here

## Result ledger

| ID | Statement | Status |
|---|---|---|
| T17-1 | Exactly five gap-count partitions survive the deficit budget | **PROVED** |
| T17-2 | A uniform cut decomposition cannot have \(1\le R\le9\) non-singleton copies | **PROVED** |
| T17-3 | Every surviving partition has at least eight singleton endpoint copies | **PROVED** |
| T17-4 | Every putative target configuration has \(t\ge18\) | **PROVED**, relative to the earlier \(t\ge17\) endpoint |
| T17-C1 | The rank-ten case \(R=10\) has an analogous sign obstruction | **CANDIDATE / NOT USED** |

All proved comparisons are rational or integer-power comparisons.  No
floating-point computation is used.

## 1. Deficit bounds through chain length eight

At \(t=17\), the exact total spectral deficit is

\[
 \sum_{j=1}^5\varepsilon_j=7,                             \tag{1}
\]

and the Naimark bound gives \(0\le\ell_j\le8\).  Use the
following rational lower bounds:

\[
\begin{array}{c|ccccccccc}
\ell&0&1&2&3&4&5&6&7&8\\ \hline
c_\ell&0&0&\frac2{11}&\frac{24}{25}&\frac{19}{10}&
\frac{23}{8}&\frac{193}{50}&\frac{97}{20}&\frac{146}{25}.
\end{array}                                               \tag{2}
\]

The entries through six were proved earlier.  The general chain bound gives

\[
 \varepsilon_7\ge\frac{12}{\sqrt[6]{10}+1}>\frac{97}{20},
 \qquad
 \varepsilon_8\ge\frac{14}{\sqrt[7]{10}+1}>\frac{146}{25}. \tag{3}
\]

These are exact because

\[
 143^6>10\,97^6,
 \qquad102^7>10\,73^7.                                   \tag{4}
\]

The successive increments of (2) are

\[
 0,\ \frac2{11},\ \frac{214}{275},\ \frac{47}{50},\
 \frac{39}{40},\ \frac{197}{200},\ \frac{99}{100},\
 \frac{99}{100},                                         \tag{5}
\]

so the lower-bound sequence is discretely convex.

### Lemma 1 (PROVED: partition list)

The only sorted five-tuples with sum seventeen whose lower-bound sum does not
exceed seven are

\[
\begin{aligned}
 &(4,4,3,3,3), &&(5,3,3,3,3),\\
 &(4,4,4,3,2), &&(5,4,3,3,2), &&(6,3,3,3,2).              \tag{6}
\end{aligned}
\]

#### Proof

If the minimum is at least three, distribute the two units above
\((3,3,3,3,3)\), giving the first line of (6).  If the minimum is exactly
two and occurs once, distribute three units above the remaining four threes,
giving the second line.  If at least two entries equal two, convexity makes
\((5,4,4,2,2)\) cheapest, and its cost is

\[
 \frac{23}{8}+2\frac{19}{10}+2\frac2{11}
 =\frac{3097}{440}>7.                                    \tag{7}
\]

If the minimum is one, \((4,4,4,4,1)\) is cheapest and already costs
\(4(19/10)>7\); a zero minimum is still more imbalanced.  Finally, the five
tuples in (6) have costs respectively

\[
 \frac{167}{25},\quad\frac{1343}{200},\quad
 \frac{3763}{550},\quad\frac{15129}{2200},\quad
 \frac{3807}{550},                                       \tag{8}
\]

all below seven. \(\square\)

## 2. Singleton compression through rank nine

As before, let \(R\) be the number of non-singleton cut copies, let
\(\alpha_r\) be the total coefficient of singleton copies on label \(r\),
and put

\[
 c_r=\frac12-\alpha_r,
 \qquad C=H\operatorname{diag}(c)H
 =\sum_{a=1}^{R}g_av_{S_a}v_{S_a}^T\succeq0.             \tag{9}
\]

### Lemma 2 (PROVED: \(R\le9\) obstruction)

No exact uniform cut decomposition can have \(1\le R\le9\).

#### Proof

For \(R\le8\), the proof in `proof/t16_branch.md` applies verbatim: rank at
most eight forces some \(c_r=0\); the non-singleton indicators are constant
on the zero set; orienting them into its complement and applying a left
inverse turns (9) into a diagonal matrix expressed as a positive sum
\(\sum g_a\mathbf1_{U_a}\mathbf1_{U_a}^T\).  Vanishing off-diagonal entries
force every \(U_a\) to be singleton, a contradiction.

It remains to consider \(R=9\).  If some \(c_r=0\), exactly the same
left-inverse argument gives the contradiction, with no rank-equality
assumption.  Suppose therefore that every \(c_r\ne0\).  On
\(V=\mathbf1^\perp\), a kernel vector of \(C\) satisfies

\[
 c_ru_r=\lambda\quad(1\le r\le11).                       \tag{10}
\]

With all \(c_r\ne0\), this kernel has dimension at most one.  Since
\(\operatorname{rank}C\le9\) on the ten-dimensional space \(V\), it must
have dimension exactly one, \(\operatorname{rank}C=9\), and

\[
 \sum_{r=1}^{11}\frac1{c_r}=0.                            \tag{11}
\]

The quadratic form of \(C\) on \(V\) is

\[
 u^TCu=\sum_{r=1}^{11}c_ru_r^2.                           \tag{12}
\]

There cannot be two negative \(c_r\)'s: their coordinate difference lies in
\(V\) and makes (12) negative.  All \(c_r\)'s cannot be positive because of
(11).  Hence exactly one \(c_r\) is negative and the other ten are positive.

The kernel vector \(u_r=1/c_r\) consequently has one negative entry, ten
positive entries, and total sum zero.  Such a vector has no nonempty proper
zero-sum subset.  A subset excluding the negative entry has positive sum; a
zero-sum subset containing it must contain all ten positive entries, because
their total is exactly the opposite of the unique negative entry.

On the other hand, positivity of every coefficient in the rank-one sum (9)
forces each \(v_{S_a}\) to be orthogonal to \(\ker C\).  Thus every
non-singleton proper cut would satisfy

\[
 \sum_{r\in S_a}u_r=0,
\]

which the preceding sign argument makes impossible.  This contradiction
excludes \(R=9\). \(\square\)

## 3. Exact endpoint-loss bounds

Call a coordinate chain regular if its endpoint prefix sizes are \((1,10)\).
It then contributes two singleton endpoint cut copies.  A nonregular chain
loses one such copy if it retains one endpoint, and two if it retains neither.

The exact endpoint-correlation estimates established in the earlier notes
are

\[
\begin{array}{c|ccc}
\ell&\text{general}&\text{nonregular}&\text{neither endpoint}\\ \hline
2&\frac2{11}&>\frac14&\ge\frac4{11}\\
3&>\frac{24}{25}&>\frac{11}{10}&>\frac54\\
4&>\frac{19}{10}&>2&>\frac94\\
5&>\frac{23}{8}&>3&>\frac{13}{4}\\
6&>\frac{193}{50}&>4&\text{not needed}.
\end{array}                                               \tag{13}
\]

Only the two last new comparisons require comment.  For a quintuple with
neither singleton endpoint, the four-factor endpoint bound has
\(u^8\ge4/81>(13/19)^8\), and
\(8u/(1+u)>13/4\).  The integer comparison is

\[
 4\,19^8>81\,13^8.
\]

For a nonregular sextuple, the five-factor endpoint bound has
\(u^{10}\ge1/45>(2/3)^{10}\), since
\(3^{10}>45\,2^{10}\); hence \(10u/(1+u)>4\).

## 4. Each partition retains at least eight singleton copies

### Proposition 3 (PROVED): \((4,4,3,3,3)\)

At most two singleton endpoints can be lost.

If a quadruple loses both endpoints, its deficit together with the general
bounds for the other chains is already

\[
 \frac94+\frac{19}{10}+3\frac{24}{25}>7.                 \tag{14}
\]

If a triple loses both and any further endpoint is lost, the cheapest two
possibilities give

\[
 \frac54+\frac{11}{10}+\frac{24}{25}+2\frac{19}{10}>7,
\]

or

\[
 \frac54+2+2\frac{24}{25}+\frac{19}{10}>7.               \tag{15}
\]

If every nonregular chain loses only one endpoint but at least three chains
are nonregular, let the number of nonregular quadruples be \(0,1,2\).  The
three respective lower bounds are

\[
 3\frac{11}{10}+2\frac{19}{10},\quad
 2+2\frac{11}{10}+\frac{19}{10}+\frac{24}{25},\quad
 2\cdot2+\frac{11}{10}+2\frac{24}{25},                   \tag{16}
\]

and all exceed seven.  Thus at least eight of the ten endpoint copies remain.

### Proposition 4 (PROVED): \((5,3,3,3,3)\)

Again at most two endpoints can be lost.  A quintuple losing both endpoints
already gives

\[
 \frac{13}{4}+4\frac{24}{25}>7.                          \tag{17}
\]

A triple losing both endpoints and any further loss gives at least

\[
 \frac{23}{8}+\frac54+\frac{11}{10}+2\frac{24}{25}>7
\]

if the extra loss is in another triple, and at least

\[
 3+\frac54+3\frac{24}{25}>7                              \tag{18}
\]

if it is in the quintuple.  Finally, three one-endpoint losses give either

\[
 \frac{23}{8}+3\frac{11}{10}+\frac{24}{25}>7,
\]

or

\[
 3+2\frac{11}{10}+2\frac{24}{25}>7.                      \tag{19}
\]

Thus at least eight singleton copies remain.

### Proposition 5 (PROVED): \((4,4,4,3,2)\)

In fact at most one endpoint can be lost.  Losing both endpoints in a double,
triple, or quadruple gives respectively

\[
 3\frac{19}{10}+\frac{24}{25}+\frac4{11},\quad
 3\frac{19}{10}+\frac54+\frac2{11},\quad
 \frac94+2\frac{19}{10}+\frac{24}{25}+\frac2{11},        \tag{20}
\]

all greater than seven.  Two one-endpoint losses have four possible length
pairs \((4,4),(4,3),(4,2),(3,2)\); their exact lower bounds are respectively

\[
 2\cdot2+\frac{19}{10}+\frac{24}{25}+\frac2{11},
\]

\[
 2+2\frac{19}{10}+\frac{11}{10}+\frac2{11},
\]

\[
 2+2\frac{19}{10}+\frac{24}{25}+\frac14,
\]

\[
 3\frac{19}{10}+\frac{11}{10}+\frac14,                  \tag{21}
\]

and all exceed seven.  Hence at least nine singleton copies remain.

### Proposition 6 (PROVED): \((5,4,3,3,2)\)

The quintuple and both triples must be regular:

\[
 3+\frac{19}{10}+2\frac{24}{25}+\frac2{11}>7,
\]

\[
 \frac{23}{8}+\frac{19}{10}+\frac{11}{10}
 +\frac{24}{25}+\frac2{11}>7.                            \tag{22}
\]

The quadruple or the double may separately lose one endpoint, but not both
together, since

\[
 \frac{23}{8}+2+2\frac{24}{25}+\frac14>7.                \tag{23}
\]

Neither can lose both endpoints, by replacing \(2\) with \(9/4\), or
\(1/4\) with \(4/11\), in the relevant general-budget sum.  Thus at most one
endpoint is lost and at least nine singleton copies remain.

### Proposition 7 (PROVED): \((6,3,3,3,2)\)

The sextuple and all triples are regular, because

\[
 4+3\frac{24}{25}+\frac2{11}>7,
\]

\[
 \frac{193}{50}+\frac{11}{10}+2\frac{24}{25}
 +\frac2{11}>7.                                          \tag{24}
\]

The double can lose one endpoint, but not both:

\[
 \frac{193}{50}+3\frac{24}{25}+\frac4{11}>7.             \tag{25}
\]

So at least nine singleton copies remain.

## 5. Exact endpoint

In every partition (6), Propositions 3--7 give at least eight singleton cut
copies among the seventeen gaps.  Thus

\[
 1\le R\le17-8=9;
\]

the lower inequality holds because five coordinate chains can contain at
most ten singleton endpoint cuts, while \(t=17\).  Lemma 2 now excludes every
partition.

### Theorem 8 (PROVED relative to earlier endpoints)

Every putative eleven-point equilateral set in \(\ell_1^5\) has

\[
 \boxed{\displaystyle
 t=\sum_{j=1}^5(q_j-1)\ge18,
 \qquad\sum_{j=1}^5q_j\ge23.}                             \tag{26}
\]

This is a partial theorem, not a proof of \(e(\ell_1^5)=10\).  The case
\(t\ge18\) is untouched, and no proof assistant was used.
