# Dense branch at \(t=15\): exact elimination of both surviving patterns

Date: 2026-08-29  
Role: proof builder, continuation after the frozen Gate-4 certificate  
Scope: only the two \(t=15\) patterns left by `proof/builder_notes.md`  
Verifier policy: this note does not modify or rely on any frozen verifier  
Novelty: not assessed here; every result below requires the separate
literature/novelty audit before being described as new

## Result ledger

| ID | Statement | Status in this note |
|---|---|---|
| D15-1 | A nonregular chain has a strictly larger endpoint-correlation deficit | **PROVED** in Lemma 1 |
| D15-2 | Singleton compression and its low-rank zero-set consequence | **PROVED** in Lemma 2 |
| D15-3 | The pattern \((3,3,3,3,3)\) is impossible | **PROVED** in Proposition 3 |
| D15-4 | The pattern \((4,3,3,3,2)\) is impossible | **PROVED** in Proposition 4 |
| D15-5 | Every putative eleven-point equilateral set in \(\ell_1^5\) has at least sixteen positive coordinate gaps | **PROVED**, conditional only on the already proved \(t\ge15\) theorem in `builder_notes.md` |
| D15-C1 | The same compression will eliminate all \(t\ge16\) strata | **CONJECTURE / NOT USED** |

No numerical observation is used in any proved item.

## 1. Imported exact setup

Let \(H=I_{11}-J_{11}/11\), let

\[
 v_S=H\mathbf1_S,
\]

and split every sorted coordinate into its positive consecutive gaps.  If
there are \(t\) positive gaps in total, the equilateral equations give

\[
 \sum_{a=1}^t g_a v_{S_a}v_{S_a}^T=\frac12H,
 \qquad g_a>0.                                            \tag{1}
\]

The frozen proof in `builder_notes.md` establishes:

1. \(t\ge15\);
2. at \(t=15\), the total spectral deficit is exactly \(t-10=5\); and
3. the only gap-count multisets not already contradicted by the deficit
   bound are

   \[
   (3,3,3,3,3),\qquad(4,3,3,3,2).                        \tag{2}
   \]

For a coordinate chain of length \(\ell\), let its selected prefix sizes be

\[
 1\le k_1<\cdots<k_\ell\le10.
\]

Call the chain **regular** if \((k_1,k_\ell)=(1,10)\).  Its first and last
cut rays are then singleton cut rays: the last prefix is the complement of
a singleton.  A nonregular chain need not lack both singleton endpoints; it
may have exactly one of them.

## 2. Exact endpoint-deficit separation

### Lemma 1 (PROVED)

Let \(\varepsilon\) be the spectral deficit of a positive-gap chain.  Then:

1. every triple chain satisfies \(\varepsilon>24/25\);
2. every nonregular triple chain satisfies \(\varepsilon>11/10\);
3. every triple chain with neither singleton endpoint satisfies
   \(\varepsilon>5/4\);
4. every quadruple chain satisfies \(\varepsilon>19/10\);
5. every nonregular quadruple chain satisfies \(\varepsilon>2\);
6. every double chain satisfies \(\varepsilon\ge2/11\); and
7. every nonregular double chain satisfies \(\varepsilon>1/4\).

#### Proof

For endpoint sizes \(a=k_1<b=k_\ell\), their normalized centered-cut
correlation is

\[
 \theta=\sqrt{\frac{a(11-b)}{b(11-a)}}.                  \tag{3}
\]

If \(r_1,\ldots,r_{\ell-1}\) are the adjacent normalized correlations in
the chain, then \(\prod_i r_i=\theta\).  The exact deficit inequality from
`builder_notes.md` is

\[
 \varepsilon\ge\sum_{i=1}^{\ell-1}\frac{2r_i}{1+r_i}.
\]

Convexity in \(\log r_i\) gives

\[
 \varepsilon\ge
 \frac{2(\ell-1)\theta^{1/(\ell-1)}}
 {1+\theta^{1/(\ell-1)}}.                                \tag{4}
\]

The general triple, quadruple, and double bounds in items 1, 4, and 6 are
the exact rational bounds already proved in `builder_notes.md`.

If \((a,b)\ne(1,10)\), then

\[
 \frac{a(11-b)}{b(11-a)}\ge\frac1{45}.                   \tag{5}
\]

Indeed, if \(a=1\), then \(b\le9\) and the ratio is minimized at \(b=9\);
if \(b=10\), it is minimized at \(a=2\); and if
\(a\ge2,b\le9\), the ratio is at least \(4/81>1/45\).

For a nonregular triple, put \(u=\sqrt\theta\).  Equations (4)--(5) give
\(u^4\ge1/45\), while

\[
 29^4>45\,11^4
\]

gives \(u>11/29\).  Hence

\[
 \varepsilon\ge\frac{4u}{1+u}>\frac{11}{10},
\]

proving item 2.

If the triple has neither singleton endpoint, then \(a\ge2,b\le9\), so the
ratio in (3) squared is at least \(4/81\).  Thus
\(u\ge\sqrt2/3>5/11\), where the last comparison follows from
\(2\cdot121>25\cdot9\).  Equation (4) now gives
\(\varepsilon>5/4\), proving item 3.

For a nonregular quadruple, put \(u=\theta^{1/3}\).  Then
\(u^6\ge1/45>1/64\), so \(u>1/2\), and (4) gives

\[
 \varepsilon\ge\frac{6u}{1+u}>2.
\]

For a nonregular double, (5) gives
\(\theta\ge1/\sqrt{45}>1/7\), and therefore

\[
 \varepsilon\ge\frac{2\theta}{1+\theta}>\frac14.
\]

This proves all seven items. \(\square\)

## 3. Singleton compression

Write

\[
 s_r=H e_r\qquad(1\le r\le11).
\]

The two sides of the singleton cut \(\{r\}\mid[11]\setminus\{r\}\) give
centered vectors \(s_r\) and \(-s_r\), so their rank-one outer product is
the same.

### Lemma 2 (PROVED: singleton compression)

Suppose exactly \(R\) columns in (1) are non-singleton cut rays.  For each
label \(r\), let \(\alpha_r\) be the sum of the positive gap weights on all
singleton cut copies with label \(r\), and put

\[
 c_r=\frac12-\alpha_r,
 \qquad Z=\{r:c_r=0\},\qquad h=|Z|.                       \tag{6}
\]

If \(R\le8\), then:

1. \(Z\ne\varnothing\) and \(h\ge11-R\);
2. every non-singleton cut indicator is constant on \(Z\); and
3. if equality \(h=11-R\) holds, then after orienting every remaining cut
   to a nonempty subset of \(W=[11]\setminus Z\), the exact identity

   \[
   \operatorname{diag}(c_w:w\in W)
   =\sum_{a=1}^{R}g_a\mathbf1_{U_a}\mathbf1_{U_a}^T       \tag{7}
   \]

   holds.  In particular, the right side of (7) can be diagonal only if
   every \(U_a\) is a singleton.

#### Proof

Subtract the singleton terms from (1).  Since

\[
 \sum_r\alpha_rs_rs_r^T=H\operatorname{diag}(\alpha)H,
\]

the sum \(C\) of the \(R\) non-singleton terms is

\[
 C=H\operatorname{diag}(c)H
  =\sum_{a=1}^{R}g_av_{S_a}v_{S_a}^T\succeq0,
 \qquad\operatorname{rank}C\le R.                        \tag{8}
\]

Work on \(V=\mathbf1^\perp\), which has dimension ten.  A vector
\(u\in V\) belongs to the kernel of the left side of (8) exactly when

\[
 H\operatorname{diag}(c)u=0,
\]

or equivalently \(c_ru_r=\lambda\) for a constant \(\lambda\).  If no
\(c_r\) vanishes, this kernel has dimension at most one, so
\(\operatorname{rank}C\ge9\), contrary to \(R\le8\).  Thus \(h>0\).
The equations at a zero entry force \(\lambda=0\), after which the kernel is
exactly

\[
 K_Z=\{u:\operatorname{supp}u\subseteq Z,\ \sum_{r\in Z}u_r=0\}.
\]

It has dimension \(h-1\), so

\[
 \operatorname{rank}C=10-(h-1)=11-h\le R,                \tag{9}
\]

which proves item 1.

Because every coefficient in the rank-one sum (8) is positive, every
\(v_{S_a}\) is orthogonal to \(\ker C=K_Z\).  Hence

\[
 0=\langle v_{S_a},u\rangle=\sum_{r\in S_a}u_r
 \quad(u\in K_Z).
\]

This holds for all zero-sum vectors supported on \(Z\) exactly when
\(\mathbf1_{S_a}\) is constant on \(Z\), proving item 2.

Assume now \(h=11-R\), let \(W=[11]\setminus Z\), and orient every cut to
a nonempty subset \(U_a\subseteq W\); complementing a cut only changes the
sign of its centered vector.  The vectors \((s_w)_{w\in W}\) are linearly
independent: if \(H\sum_{w\in W}d_we_w=0\), the vector supported on \(W\)
inside \(H\) would have to be constant on all eleven labels and hence zero.
Let \(S\) be the matrix with these \(s_w\) as columns.  Then

\[
 H\operatorname{diag}(c)H
 =S\operatorname{diag}(c_w:w\in W)S^T,
 \qquad
 v_{U_a}=S\mathbf1_{U_a}.
\]

Since \(S\) has full column rank, applying a left inverse to (8) gives (7).
Every off-diagonal entry on the right of (7) is a sum of nonnegative numbers
\(g_a\) over those \(U_a\) containing both labels.  It can vanish for every
pair only when no \(U_a\) contains two labels.  Every \(U_a\) is nonempty,
so each is a singleton. \(\square\)

## 4. Eliminate \((3,3,3,3,3)\)

### Proposition 3 (PROVED)

There is no \(t=15\) equilateral cut frame with coordinate gap-count pattern
\((3,3,3,3,3)\).

#### Proof

The total deficit is five.  If two triple chains were nonregular, Lemma 1
would give

\[
 \sum_j\varepsilon_j>
 2\frac{11}{10}+3\frac{24}{25}
 =\frac{127}{25}>5,                                      \tag{10}
\]

a contradiction.  Thus at most one chain is nonregular.  If that one chain
had neither singleton endpoint, then

\[
 \sum_j\varepsilon_j>
 \frac54+4\frac{24}{25}=\frac{509}{100}>5.               \tag{11}
\]

Therefore there are only two cases.

**Case A: all five chains are regular.**  There are ten singleton cut copies
and five non-singleton cuts, so Lemma 2 with \(R=5\) gives \(h\ge6\).  Every
label in \(Z\) has \(\alpha_r=1/2>0\), hence occurs as a singleton endpoint
of at least one coordinate.

In any regular triple coordinate, its internal prefix cut contains its
minimum endpoint and excludes its maximum endpoint.  Lemma 2 says that this
indicator is constant on \(Z\), so the two endpoints cannot both belong to
\(Z\).  Five coordinates can therefore contain at most five distinct
\(Z\)-labels among their endpoint slots.  This contradicts \(h\ge6\).

**Case B: exactly one chain is nonregular and has exactly one singleton
endpoint.**  The four regular chains contribute eight singleton copies and
the exceptional chain contributes one, leaving \(R=6\) non-singleton cuts.
Lemma 2 gives \(h\ge5\).  Each regular coordinate contains at most one
\(Z\)-endpoint as above.  The exceptional coordinate also contains a
non-singleton prefix cut which contains its minimum point and excludes its
maximum point, so those two endpoint labels cannot both lie in \(Z\).
Since every label of \(Z\) must occur as a singleton endpoint in some
coordinate, the union of \(Z\)-labels over the five endpoint pairs has size
at most five.  Hence \(h\le5\), and thus \(h=5=11-R\).

Apply item 3 of Lemma 2.  It says that all six remaining cut rays are
singleton rays on \(W=[11]\setminus Z\).  But they were defined to be the six
non-singleton cut rays (four internal cuts from the regular chains and two
from the exceptional chain).  This contradiction completes Case B and the
proof. \(\square\)

## 5. Eliminate \((4,3,3,3,2)\)

### Proposition 4 (PROVED)

There is no \(t=15\) equilateral cut frame with coordinate gap-count pattern
\((4,3,3,3,2)\).

#### Proof

Again the total deficit is five.  Lemma 1 shows that every chain must be
regular:

- a nonregular quadruple would give

  \[
  \sum_j\varepsilon_j>
  2+3\frac{24}{25}+\frac2{11}>5;
  \]

- a nonregular triple would give

  \[
  \sum_j\varepsilon_j>
  \frac{19}{10}+\frac{11}{10}
  +2\frac{24}{25}+\frac2{11}>5;
  \]

- a nonregular double would give

  \[
  \sum_j\varepsilon_j>
  \frac{19}{10}+3\frac{24}{25}+\frac14>5.
  \]

There are consequently ten singleton endpoint cut copies.  The quadruple
has two internal non-singleton cuts, the three triples have one each, and the
double has none.  Hence \(R=5\), and Lemma 2 gives \(h\ge6\).

Each of the quadruple and triple coordinates has an internal prefix cut, so
its two endpoints cannot both lie in \(Z\).  These four coordinates account
for at most four distinct \(Z\)-labels.  The double coordinate has no
internal cut and can account for at most its two endpoint labels.  Thus
\(h\le6\), and consequently \(h=6=11-R\).

Item 3 of Lemma 2 now says that all five internal non-singleton cut rays are
singleton rays on the five-label complement \(W\), contradicting their
definition.  Therefore the pattern is impossible. \(\square\)

## 6. Exact conclusion and remaining gap

### Theorem 5 (PROVED relative to the frozen \(t\ge15\) result)

Every putative eleven-point equilateral set in \(\ell_1^5\) has at least
sixteen positive consecutive coordinate gaps:

\[
 \boxed{\displaystyle
 t=\sum_{j=1}^5(q_j-1)\ge16,
 \qquad \sum_{j=1}^5q_j\ge21.}                            \tag{12}
\]

Indeed, `builder_notes.md` proves \(t\ge15\) and reduces equality to the two
patterns (2); Propositions 3--4 eliminate both exactly.

This does **not** prove \(e(\ell_1^5)=10\).  No claim is made here about any
stratum \(t\ge16\), and D15-C1 remains only a conjectural route.  No proof
assistant was used.
