# The \(t=16\) branch: singleton compression eliminates every pattern

Date: 2026-08-29  
Role: proof builder after the independently reconstructed \(t=15\) argument  
Scope: exact analysis of \(t=16\) only  
Verifier policy: no frozen verifier, runner, or fail-closed log is modified  
Novelty: not assessed here; this note is mathematical evidence for later
independent referee and novelty review

## Result ledger

| ID | Statement | Status |
|---|---|---|
| T16-1 | Only three coordinate gap-count partitions survive the spectral-deficit bounds | **PROVED** |
| T16-2 | A uniform cut decomposition cannot have between one and eight non-singleton cut copies | **PROVED** |
| T16-3 | Each of the three surviving \(t=16\) partitions has at most eight non-singleton copies | **PROVED** |
| T16-4 | Every putative eleven-point equilateral set in \(\ell_1^5\) has \(t\ge17\) | **PROVED**, conditional on the previously proved \(t\ge16\) endpoint |
| T16-C1 | Singleton compression alone will settle all later strata | **CANDIDATE / NOT USED** |

No floating-point or sampled assertion is used below.

## 1. Imported facts and notation

As in the earlier notes, a putative configuration gives

\[
 \sum_{a=1}^{t}g_av_{S_a}v_{S_a}^T=\frac12H,
 \qquad H=I_{11}-\frac1{11}J_{11},\quad
 v_S=H\mathbf1_S,\quad g_a>0.                           \tag{1}
\]

Let \(\ell_j\) be the number of positive gaps in coordinate \(j\).  At
\(t=16\),

\[
 \sum_{j=1}^5\ell_j=16,
 \qquad \sum_{j=1}^5\varepsilon_j=t-10=6,                \tag{2}
\]

where \(\varepsilon_j\) is the coordinate spectral deficit.  The Naimark
chain-length lemma gives \(0\le\ell_j\le7\).

For a chain of length \(\ell\), the proved rational deficit lower bounds are

\[
\begin{array}{c|cccccccc}
\ell&0&1&2&3&4&5&6&7\\ \hline
c_\ell&0&0&\frac2{11}&\frac{24}{25}&\frac{19}{10}&
\frac{23}{8}&\frac{193}{50}&\frac{243}{50}.
\end{array}                                               \tag{3}
\]

The entries through \(6\) were proved in the earlier notes.  For the last
entry, the general chain bound gives

\[
 \varepsilon_j\ge\frac{12}{\sqrt[6]{10}+1}>\frac{243}{50}; \tag{4}
\]

the strict rational comparison is exactly

\[
 119^6>10\,81^6.
\]

The successive increments of (3) are

\[
 0,\quad\frac2{11},\quad\frac{214}{275},\quad
 \frac{47}{50},\quad\frac{39}{40},\quad
 \frac{197}{200},\quad1,                                 \tag{5}
\]

so the sequence is discretely convex.

## 2. The only deficit-compatible partitions

### Lemma 1 (PROVED)

If \(t=16\), then the sorted gap-count multiset must be one of

\[
 (4,3,3,3,3),\qquad(4,4,3,3,2),\qquad(5,3,3,3,2).        \tag{6}
\]

#### Proof

Discrete convexity means that, at fixed sum, moving one unit from a smaller
entry to a larger entry cannot lower \(\sum_jc_{\ell_j}\).  If every entry
is at least three, sum sixteen forces the first partition in (6).

If the minimum is exactly two and occurs once, the other four entries are at
least three and sum fourteen.  Their excess above three is two, giving the
other two partitions in (6).  If the minimum two occurs at least twice, the
least expensive possibility is \((4,4,4,2,2)\), whose lower-bound sum is

\[
 3\frac{19}{10}+2\frac2{11}=\frac{667}{110}>6.            \tag{7}
\]

If the minimum is one, convexity makes \((4,4,4,3,1)\) cheapest; its cost is

\[
 3\frac{19}{10}+\frac{24}{25}=\frac{333}{50}>6.           \tag{8}
\]

A zero minimum is still more imbalanced and more expensive.  Finally, the
three partitions in (6) have lower-bound sums

\[
 \frac{287}{50},\qquad \frac{1623}{275},\qquad
 \frac{13061}{2200},                                     \tag{9}
\]

all below six, so deficit alone does not eliminate them. \(\square\)

## 3. Strong singleton-compression obstruction

Call a cut ray **singleton** if one side of its bipartition has one label.
Copies are counted separately when they arise from different positive
coordinate gaps.  Put \(s_r=He_r\).

### Lemma 2 (PROVED)

An exact uniform-metric decomposition (1) cannot contain between one and
eight non-singleton cut copies.

#### Proof

Suppose there are \(1\le R\le8\) non-singleton copies.  For every label
\(r\), let \(\alpha_r\) be the total positive coefficient of all singleton
cut copies on that label and set

\[
 c_r=\frac12-\alpha_r,
 \qquad Z=\{r:c_r=0\}.                                   \tag{10}
\]

After subtracting the singleton terms from (1), the remaining operator is

\[
 C=H\operatorname{diag}(c)H
  =\sum_{a=1}^{R}g_av_{S_a}v_{S_a}^T\succeq0,
 \qquad\operatorname{rank}C\le R\le8.                   \tag{11}
\]

If \(Z\) were empty, a vector \(u\in\mathbf1^\perp\) in \(\ker C\) would
have to satisfy \(c_ru_r=\lambda\) for every \(r\), leaving kernel dimension
at most one.  Then \(\operatorname{rank}C\ge9\), contrary to (11).  Hence
\(Z\ne\varnothing\).

With at least one zero \(c_r\), the same equations force \(\lambda=0\), and

\[
 \ker(C|_{\mathbf1^\perp})=K_Z
 =\{u:\operatorname{supp}u\subseteq Z,
                    \ \sum_{r\in Z}u_r=0\}.              \tag{12}
\]

Positivity of every \(g_a\) in (11) implies that each remaining cut vector
is orthogonal to \(K_Z\).  Equivalently, every indicator
\(\mathbf1_{S_a}\) is constant on \(Z\).  Complement the cut if necessary;
then it has an oriented side contained in \(W=[11]\setminus Z\).  Here
\(W\ne\varnothing\): if \(Z=[11]\), constancy on \(Z\) would make every
remaining cut trivial, contrary to \(R\ge1\).  Because every original cut is
proper, the oriented side is therefore a nonempty set
\(U_a\subseteq W\).

The vectors \((s_w)_{w\in W}\) are linearly independent.  If \(S\) is the
matrix with those columns, then

\[
 H\operatorname{diag}(c)H
 =S\operatorname{diag}(c_w:w\in W)S^T,
 \qquad v_{U_a}=S\mathbf1_{U_a}.
\]

Applying a left inverse of \(S\) to (11) yields

\[
 \operatorname{diag}(c_w:w\in W)
 =\sum_{a=1}^{R}g_a\mathbf1_{U_a}\mathbf1_{U_a}^T.       \tag{13}
\]

Every off-diagonal entry on the right is a sum of nonnegative terms.  Since
the left side is diagonal and every \(g_a>0\), no \(U_a\) can contain two
labels.  Each \(U_a\) is nonempty, so every remaining cut ray is singleton,
contradicting the definition of the \(R\) copies. \(\square\)

This strengthens the equality-only form of singleton compression used in
the \(t=15\) note: no equality between \(|Z|\) and \(11-R\) is required.

## 4. Endpoint deficit penalties

Call a chain **regular** when its first and last prefix sizes are \((1,10)\),
so it supplies two singleton endpoint cut copies.  A nonregular chain with
one of these endpoints supplies one singleton copy; with neither, it supplies
none.

The endpoint-correlation argument in `proof/t15_dense_branch.md` proves:

\[
\begin{array}{c|ccc}
\text{length}&\text{general}&\text{nonregular}&
\text{neither singleton endpoint}\\ \hline
2&\frac2{11}&>\frac14&\ge\frac4{11}\\
3&>\frac{24}{25}&>\frac{11}{10}&>\frac54\\
4&>\frac{19}{10}&>2&>\frac94.
\end{array}                                               \tag{14}
\]

For the last entry in the quadruple row: when neither endpoint is singleton,
the squared endpoint correlation is at least \(4/81\).  In the three-factor
Jensen bound put \(u=\theta^{1/3}\); then
\(u^6\ge4/81>(3/5)^6\), and so
\(6u/(1+u)>9/4\).

For a nonregular quintuple chain, the corresponding four-factor bound has
\(u^8\ge1/45>(3/5)^8\), hence

\[
 \varepsilon>\frac{8(3/5)}{1+3/5}=3.                    \tag{15}
\]

Every comparison in (14)--(15) is exact.

## 5. Eliminate the three partitions

### Proposition 3 (PROVED)

The pattern \((4,3,3,3,3)\) is impossible.

#### Proof

No triple can lack both singleton endpoints, since that would give

\[
 \sum_j\varepsilon_j>
 \frac54+3\frac{24}{25}+\frac{19}{10}>6.                 \tag{16}
\]

Nor can the quadruple lack both endpoints, since

\[
 \sum_j\varepsilon_j>
 \frac94+4\frac{24}{25}>6.                               \tag{17}
\]

At most two chains can be nonregular.  Indeed, three nonregular triples give
more than

\[
 3\frac{11}{10}+\frac{24}{25}+\frac{19}{10}>6,
\]

while a nonregular quadruple together with two nonregular triples gives more
than

\[
 2+2\frac{11}{10}+2\frac{24}{25}>6.
\]

Thus the five chains retain at least \(10-2=8\) singleton endpoint copies.
Among all sixteen copies, the number \(R\) of non-singleton copies satisfies
\(1\le R\le8\): it is nonzero because every triple or quadruple has internal
cuts.  Lemma 2 gives the contradiction. \(\square\)

### Proposition 4 (PROVED)

The pattern \((4,4,3,3,2)\) is impossible.

#### Proof

A nonregular quadruple would force

\[
 2+\frac{19}{10}+2\frac{24}{25}+\frac2{11}>6,
\]

and a nonregular triple would force

\[
 2\frac{19}{10}+\frac{11}{10}+\frac{24}{25}
 +\frac2{11}>6.
\]

Hence both quadruples and both triples are regular.  The double may be
regular or may retain exactly one singleton endpoint.  It cannot lack both,
because then (14) gives

\[
 2\frac{19}{10}+2\frac{24}{25}+\frac4{11}>6.
\]

There are therefore at least nine singleton endpoint copies, leaving at most
\(R=7\) non-singleton copies; internal quadruple and triple cuts make
\(R>0\).  Lemma 2 again contradicts the decomposition. \(\square\)

### Proposition 5 (PROVED)

The pattern \((5,3,3,3,2)\) is impossible.

#### Proof

The quintuple must be regular, since a nonregular one gives, by (15),

\[
 3+3\frac{24}{25}+\frac2{11}>6.
\]

Every triple must be regular, because one nonregular triple would give

\[
 \frac{23}{8}+\frac{11}{10}+2\frac{24}{25}
 +\frac2{11}>6.
\]

The double must also be regular, since otherwise

\[
 \frac{23}{8}+3\frac{24}{25}+\frac14>6.
\]

Thus all five chains give two singleton endpoint copies, leaving exactly six
non-singleton copies (three internal quintuple cuts and one from each triple).
Lemma 2 excludes \(R=6\). \(\square\)

## 6. Exact endpoint

### Theorem 6 (PROVED relative to earlier endpoints)

Every putative eleven-point equilateral set in \(\ell_1^5\) has at least
seventeen positive consecutive coordinate gaps:

\[
 \boxed{\displaystyle
 t=\sum_{j=1}^5(q_j-1)\ge17,
 \qquad\sum_{j=1}^5q_j\ge22.}                             \tag{18}
\]

The earlier notes prove \(t\ge16\); Lemma 1 lists every possible equality
pattern at \(t=16\), and Propositions 3--5 eliminate all of them.

This remains a partial theorem, not a proof of \(e(\ell_1^5)=10\).  No
claim about \(t\ge17\) is made here, and no proof assistant was used.
