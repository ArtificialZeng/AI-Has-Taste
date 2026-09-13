# The \(t=18\) branch: a ten-block antichain obstruction

Date: 2026-08-29  
Role: proof builder  
Scope: exact analysis of \(t=18\) only  
Freeze discipline: no earlier proof, verifier, frame, runner, or log is edited  
Novelty: not assessed here

## Result ledger

| ID | Statement | Status |
|---|---|---|
| T18-1 | Exactly eight gap-count partitions survive the general spectral-deficit budget | **PROVED** |
| T18-2 | Every surviving partition has at least eight singleton endpoint copies | **PROVED** |
| T18-3 | A five-chain uniform-cut decomposition cannot have exactly ten non-singleton copies | **PROVED** |
| T18-4 | Every putative eleven-point equilateral set in \(\ell_1^5\) has \(t\ge19\) positive coordinate gaps | **PROVED**, relative to the previously proved \(t\ge18\) endpoint and rank-nine compression lemma |
| T18-C1 | The bound \(t\ge19\) alone implies \(e(\ell_1^5)\le10\) | **FALSE AS AN INFERENCE / NOT CLAIMED** |

Every comparison below is an equality of rationals or an integer-power
comparison.  No floating-point computation is used.  This note does **not**
settle the original equilateral-set conjecture: configurations with
\(t\ge19\) remain to be excluded or constructed.

## 1. Imported exact frame facts

Let the eleven labels be \([11]\), let

\[
 H=I_{11}-\frac1{11}J_{11},\qquad v_S=H\mathbf1_S,
\]

and let the positive coordinate gaps give cut copies \((S_a,g_a)\),
\(g_a>0\).  The uniform-distance identity is

\[
 \sum_{a=1}^{t}g_av_{S_a}v_{S_a}^{T}=\frac12H.          \tag{1}
\]

For coordinate \(j\), write \(\ell_j\) for its number of positive gaps and
\(\varepsilon_j\) for its spectral deficit.  The earlier exact reduction
gives

\[
 \sum_{j=1}^5\ell_j=t,\qquad
 \sum_{j=1}^5\varepsilon_j=t-10,\qquad
 \ell_j\le t-9.                                         \tag{2}
\]

The earlier rank-nine singleton-compression lemma says that (1) cannot have
between one and nine non-singleton cut copies.  We import that proved lemma
without changing its file.

We now assume \(t=18\).  Thus

\[
 \sum_j\ell_j=18,\qquad \sum_j\varepsilon_j=8,
 \qquad0\le\ell_j\le9.                                  \tag{3}
\]

## 2. Exact deficit-compatible gap partitions

For a chain of length \(\ell\), use the following rational lower bounds:

\[
\begin{array}{c|cccccccccc}
\ell&0&1&2&3&4&5&6&7&8&9\\ \hline
c_\ell&0&0&\frac2{11}&\frac{24}{25}&\frac{19}{10}&
\frac{23}{8}&\frac{193}{50}&\frac{97}{20}&
\frac{146}{25}&\frac{683}{100}.
\end{array}                                               \tag{4}
\]

The entries through eight were proved in the earlier branches.  The new
entry follows from the general chain bound:

\[
 \varepsilon_9\ge\frac{16}{\sqrt[8]{10}+1}
 >\frac{683}{100}.                                       \tag{5}
\]

Indeed, the last comparison is equivalent to

\[
 917^8>10\,683^8,
\]

and the integer difference is

\[
 917^8-10\,683^8=26432594300827948436631>0.              \tag{6}
\]

The successive increments of (4) are

\[
 0,\ \frac2{11},\ \frac{214}{275},\ \frac{47}{50},
 \ \frac{39}{40},\ \frac{197}{200},\ \frac{99}{100},
 \ \frac{99}{100},\ \frac{99}{100}.                   \tag{7}
\]

They are nondecreasing, so \((c_\ell)\) is discretely convex.

### Lemma 1 (PROVED: the eight partitions)

The only sorted five-tuples of nonnegative integers of sum eighteen whose
cost from (4) does not exceed eight are

\[
\begin{array}{lll}
A=(4,4,4,3,3),&B=(5,4,3,3,3),&C=(6,3,3,3,3),\\
D=(4,4,4,4,2),&E=(5,4,4,3,2),&F=(5,5,3,3,2),\\
G=(6,4,3,3,2),&H=(7,3,3,3,2).                           \tag{8}
\end{array}
\]

Their respective rational costs are

\[
 \frac{381}{50},\ \frac{1531}{200},\ \frac{77}{10},
 \ \frac{428}{55},\ \frac{17197}{2200},
 \ \frac{8637}{1100},\ \frac{2162}{275},
 \ \frac{8703}{1100}.                                  \tag{9}
\]

#### Proof

If the minimum entry is at least three, distribute the three excess units
above \((3,3,3,3,3)\).  The three integer partitions of that excess give
exactly \(A,B,C\).

If the minimum is exactly two and occurs once, the other four entries have
four excess units above three.  The five integer partitions of four give
exactly \(D,E,F,G,H\).  If at least two entries equal two, discrete
convexity makes \((5,5,4,2,2)\) cheapest, and

\[
 2\frac{23}{8}+\frac{19}{10}+2\frac2{11}
 =\frac{1763}{220}>8.                                   \tag{10}
\]

If the minimum is one, convexity makes \((5,4,4,4,1)\) cheapest, with cost

\[
 \frac{23}{8}+3\frac{19}{10}=\frac{343}{40}>8.          \tag{11}
\]

If the minimum is zero, \((5,5,4,4,0)\) is cheapest and costs
\(191/20>8\).  This proves completeness.  Direct substitution gives (9),
and every number in (9) is below eight. \(\square\)

## 3. Exact endpoint-loss penalties

For a chain with selected prefix sizes

\[
 1\le k_1<\cdots<k_\ell\le10,
\]

call an endpoint copy singleton when \(k_1=1\), respectively
\(k_\ell=10\).  A regular chain has both singleton endpoint copies.  Let
\(e\in\{0,1,2\}\) count the singleton endpoint copies lost by the chain.

Put \(a=k_1\), \(b=k_\ell\).  The endpoint correlation and the exact chain
bound are

\[
 \theta=\sqrt{\frac{a(11-b)}{b(11-a)}},\qquad
 \varepsilon\ge\frac{2(\ell-1)u}{1+u},\quad
 u=\theta^{1/(\ell-1)}.                                 \tag{12}
\]

For \(e\ge1\), one has \(\theta^2\ge1/45\).  For \(e=2\), one has the
stronger \(\theta^2\ge4/81\).  These follow by monotonicity of
\(a(11-b)/(b(11-a))\): a nonregular endpoint pair is no more extreme than
\((1,9)\) or \((2,10)\), while a pair with neither endpoint has
\(2\le a<b\le9\).

Substitution in (12) gives the following safe rational table:

\[
\begin{array}{c|ccc}
\ell& e=0\text{ (general)}&e\ge1&e=2\\ \hline
2&\frac2{11}&>\frac14&\ge\frac4{11}\\
3&>\frac{24}{25}&>\frac{111}{100}&>\frac54\\
4&>\frac{19}{10}&>\frac{207}{100}&>\frac94\\
5&>\frac{23}{8}&>\frac{153}{50}&>\frac{13}{4}\\
6&>\frac{193}{50}&>\frac{81}{20}&>\frac{17}{4}\\
7&>\frac{97}{20}&>\frac{101}{20}&>\frac{21}{4}.
\end{array}                                               \tag{13}
\]

Here the \(e=0\) column means the general bound, not that regularity makes
equality possible.

For completeness, all new radical comparisons in the middle column reduce
to

\[
\begin{array}{rcl}
289^4-45\,111^4&=&144440596,\\
131^6-45\,69^6&=&197595805636,\\
247^8-45\,153^8&=&341257329895839316,\\
119^{10}-45\,81^{10}&=&22373433354250690756,\\
139^{12}-45\,101^{12}&=&1313742681350448050257876,
\end{array}                                               \tag{14}
\]

all positive.  For example, in the \(\ell=5\) line, (14) gives
\(u>153/247\), and then \(8u/(1+u)>153/50\).

The corresponding comparisons for the last column are

\[
\begin{array}{rcl}
4\,11^4-81\,5^4&=&7939,\\
4\,5^6-81\,3^6&=&3451,\\
4\,19^8-81\,13^8&=&1860063763,\\
4\,23^{10}-81\,17^{10}&=&2410538918227,\\
4\,9^{12}-81\,7^{12}&=&8573882643,
\end{array}                                               \tag{15}
\]

again all positive.  The \(\ell=2\) middle entry follows from
\(1/\sqrt{45}>1/7\), and its last entry follows directly from
\(\theta\ge2/9\).  Thus (13) is proved without numerical approximation.

### Lemma 2 (PROVED: every survivor retains eight endpoints)

For every partition in (8), the total endpoint loss is at most two.  For
\(F,G,H\), it is in fact at most one.

#### Proof

Use the three entries in each row of (13) according as the loss in that
coordinate is zero, at least one, or two.  The exact minima of these rational
boundary sums, subject to total loss at least two and at least three, are as
follows (the actual deficit retains the strict inequalities in (13)):

\[
\begin{array}{c|c|c|c}
\text{pattern}&\text{general cost}&
\min(\text{loss}\ge2)&\min(\text{loss}\ge3)\\ \hline
A&381/50&791/100&403/50\\
B&1531/200&1589/200&1619/200\\
C&77/10&799/100&407/50\\
D&428/55&438/55&8947/1100\\
E&17197/2200&17597/2200&17927/2200\\
F&8637/1100&8837/1100&4501/550\\
G&2162/275&2212/275&9013/1100\\
H&8703/1100&8903/1100&2267/275.
\end{array}                                               \tag{16}
\]

This small table is also directly hand-checkable from the endpoint penalty
increments.  Relative to the general column of (13), the total penalties
for losing one endpoint and for losing both are respectively

\[
\begin{array}{c|cccccc}
\ell&2&3&4&5&6&7\\ \hline
e\ge1&>3/44&>3/20&>17/100&>37/200&>19/100&>1/5\\
e=2&\ge2/11&>29/100&>7/20&>3/8&>39/100&>2/5.
\end{array}                                               \tag{17}
\]

For \(A,B,C\), the cheapest two losses are both placed in a triple, and the
cheapest third loss is one endpoint of another triple.  For \(D,\ldots,H\),
the cheapest two losses are both placed in the double; the cheapest third
loss is one endpoint of a shortest remaining chain.  This gives (16).
All entries in the last column for \(A,\ldots,E\) exceed eight, and all
loss-at-least-two entries for \(F,G,H\) exceed eight.  The exact deficit
budget (3) proves the claim. \(\square\)

Every chain in (8) has length at least two, so it has at most two singleton
endpoint copies and there are at most ten such copies overall.  Lemma 2 gives
at least eight.  Hence, when \(t=18\), the number \(R\) of non-singleton
copies satisfies

\[
 8\le R=18-(\text{number of singleton copies})\le10.     \tag{18}
\]

If \(R\le9\), the imported rank-nine compression lemma already contradicts
(1).  It remains only to exclude \(R=10\).

## 4. The exact \(R=10\) design identity

Let \(R=10\) be the number of non-singleton cut copies.  For each label
\(r\), let \(\alpha_r\) be the total coefficient of singleton cut copies
on that label and set

\[
 c_r=\frac12-\alpha_r,\qquad s_r=He_r.
\]

After subtracting the singleton terms from (1),

\[
 C=H\operatorname{diag}(c)H
   =\sum_{a=1}^{10}g_av_{S_a}v_{S_a}^{T}.                \tag{19}
\]

Fix an arbitrary reference label \(p\).  Put \(W=[11]\setminus\{p\}\).
The ten vectors \((s_r)_{r\in W}\) form a basis of
\(V=\mathbf1^\perp\), and \(s_p=-\sum_{r\in W}s_r\).

Orient every non-singleton cut to the side \(U_a^{(p)}\) not containing
\(p\).  Because the cut is non-singleton, both sides have at least two
labels, so

\[
 2\le |U_a^{(p)}|\le9.                                  \tag{20}
\]

Let \(B_p\) be the \(10\times10\) zero-one matrix whose \(a\)-th column is
\(\mathbf1_{U_a^{(p)}}\), let
\(G=\operatorname{diag}(g_1,\ldots,g_{10})\), and let
\(D_p=\operatorname{diag}(c_r:r\in W)\).  Expressing (19) in the basis
\((s_r)_{r\in W}\) gives the exact design identity

\[
 \boxed{\quad D_p+c_pJ_{10}=B_pGB_p^T.\quad}             \tag{21}
\]

### Lemma 3 (PROVED: positivity and invertibility)

Every \(c_p\) is positive, and every \(B_p\) is invertible.

#### Proof

For distinct rows \(i,j\in W\), the \((i,j)\) entry of (21) is

\[
 c_p=\sum_{a:\ i,j\in U_a^{(p)}}g_a.                   \tag{22}
\]

The right side is nonnegative, so \(c_p\ge0\).  If \(c_p=0\), positivity
of all \(g_a\) makes every column of \(B_p\) contain at most one \(1\),
contrary to (20).  Thus \(c_p>0\).  Since \(p\) was arbitrary, every
\(c_r>0\).

Consequently, the left side of (21) is positive definite.  Its rank is ten,
and \(G\) is positive diagonal, so \(B_p\) has rank ten and is invertible.
\(\square\)

The determinant form of (21), useful as an independent check, is

\[
 (\det B_p)^2\prod_{a=1}^{10}g_a
 =\left(\prod_{r=1}^{11}c_r\right)
  \left(\sum_{r=1}^{11}\frac1{c_r}\right).              \tag{23}
\]

In particular, \(|\det B_p|\) is independent of the reference label.

## 5. The antichain obstruction

### Lemma 4 (PROVED: the oriented blocks cross pairwise)

For a fixed reference \(p\), any two distinct blocks
\(U_a^{(p)},U_b^{(p)}\) intersect, and neither contains the other.

#### Proof

Suppress the subscript \(p\), write

\[
 s=\sum_{r\in W}\frac1{c_r},\qquad
 \lambda=\frac{c_p}{1+c_ps},\qquad
 x(X)=\sum_{r\in X}\frac1{c_r}.
\]

All these quantities are positive, and

\[
 0<\lambda s=\frac{c_ps}{1+c_ps}<1.                     \tag{24}
\]

Sherman--Morrison applied to the left side of (21) gives

\[
 (D+c_pJ)^{-1}
 =D^{-1}-\lambda D^{-1}JD^{-1}.                         \tag{25}
\]

Because \(D+c_pJ=BGB^T\) and \(B\) is invertible,

\[
 G^{-1}=B^T(D+c_pJ)^{-1}B.                              \tag{26}
\]

The off-diagonal \((a,b)\) entry of (26) is zero.  Equations
(25)--(26) therefore give the exact intersection identity

\[
 x(U_a\cap U_b)=\lambda x(U_a)x(U_b).                   \tag{27}
\]

The right side is positive, so \(U_a\cap U_b\ne\varnothing\).  If, say,
\(U_a\subseteq U_b\), then (27) and \(x(U_a)>0\) give

\[
 1=\lambda x(U_b)\le\lambda s<1,
\]

a contradiction.  Interchanging \(a,b\) excludes the other containment.
\(\square\)

### Lemma 5 (PROVED: a coordinate contributes at most one block)

After orientation away from a fixed reference label, two cuts coming from
one coordinate chain are either nested or disjoint.

#### Proof

Let \(P\subset Q\) be two prefix sets from the same coordinate.  If the
reference \(p\) lies in neither, their oriented sides are \(P\subset Q\).
If it lies in both, their oriented sides are
\(Q^c\subset P^c\).  In the only remaining case,
\(p\notin P\) and \(p\in Q\), the oriented sides are \(P\) and \(Q^c\),
which are disjoint. \(\square\)

Lemmas 4 and 5 are incompatible for any two non-singleton copies from the
same coordinate.  Thus each of the five coordinates contributes at most one
non-singleton copy, and hence \(R\le5\).  This contradicts \(R=10\).

We have proved:

### Proposition 6 (PROVED: the ten-copy obstruction)

An exact uniform-cut decomposition arising from five coordinate chains
cannot have exactly ten non-singleton cut copies.

This is stronger than a bare pairwise-intersecting design condition.  The
inverse identity (27) is what also rules out containment; pairwise
intersection alone would not contradict a nested coordinate chain.

## 6. Conclusion and precise remaining gap

Under \(t=18\), Lemmas 1--2 leave at least eight singleton copies, so there
are at most ten non-singleton copies.  One through nine are excluded by the
earlier rank-nine compression lemma, while ten are excluded by Proposition
6.  Therefore \(t=18\) is impossible.  Combined with the earlier proved
endpoint \(t\ge18\), this yields

\[
 \boxed{\ t\ge19\ }                                     \tag{28}
\]

for every putative eleven-point equilateral set in \(\ell_1^5\).

The remaining gap to the original problem is substantial and explicit:
(28) is only a lower bound on the number of positive coordinate gaps in a
hypothetical configuration.  It neither constructs eleven points nor rules
out all strata \(t\ge19\).  No claim about the final value of
\(e(\ell_1^5)\) is made here.

No proof assistant was used.  The proof uses exact rational arithmetic,
integer-power comparisons, and hand-checkable finite partition and
endpoint-loss tables.
