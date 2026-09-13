# Exact resolution of the at-most-five-support layer of (HC4)

## Statement proved

Let (x=(x_v)_{v\in V_4}\in\mathbb R_{\geq 0}^{16}). If

\[
|\operatorname{supp}x|\leq 5,
\]

then

\[
P_4(x)\,\sigma(x)^3\leq Q_4(x).
\]

Within this at-most-five-support domain, equality holds exactly when
(\operatorname{supp}x) is contained in a facet of the 4-cube. This includes
the zero vector. This is a subsidiary result: no assertion is made here for
supports of size at least six, so the original 16-variable claim (HC4) remains
unresolved.

## Reduction to exact orbit polynomials

If the support has at most four elements, every five-fold squarefree monomial
in (P_4) vanishes. Suppose the support has exactly five elements
(T=\{v_0,\ldots,v_4\}), and write (y_j=x_{v_j}>0). Then only the term indexed
by (T) can survive in (P_4). Hence the restricted gap is

\[
D_T(y)=
\prod_{r=1}^4
 \left(\sum_{j:(v_j)_r=0}y_j\right)
 \left(\sum_{j:(v_j)_r=1}y_j\right)
-\operatorname{Vol}(T)y_0y_1y_2y_3y_4
 (y_0+y_1+y_2+y_3+y_4)^3. \tag{1}
\]

If (T) is affinely dependent, then (operatorname{Vol}(T)=0), so (1) is a
product of eight linear forms with nonnegative coefficients. It remains only
to treat affinely independent (T).

Let

\[
G=\{g_{\pi,e}:(g_{\pi,e}(v))_j=v_{\pi(j)}\mathbin\oplus e_j,
\ \pi\in S_4,\ e\in\{0,1\}^4\}.
\]

These are the (2^4 4!=384) cube symmetries. They permute the eight facets,
and their affine linear parts are signed permutation matrices. Therefore they
preserve the determinant absolute value and carry (1) to the corresponding
polynomial after merely relabelling variables. It is consequently enough to
check one representative of every (G)-orbit of five-subsets.

The exact enumeration uses the lexicographically least image under all 384
maps as the canonical representative. It produces the following complete
table. “Terms” and “range” refer to the nonzero coefficients after expanding
(D_T); a dash denotes an affinely dependent representative.

| no. | representative | orbit | stabilizer | Vol | terms | coefficient range |
|---:|:---|---:|---:|---:|---:|:---|
| 1 | `0000,0001,0010,0011,0100` | 192 | 2 | 0 | — | — |
| 2 | `0000,0001,0010,0011,1100` | 96 | 4 | 0 | — | — |
| 3 | `0000,0001,0010,0100,0111` | 64 | 6 | 0 | — | — |
| 4 | `0000,0001,0010,0100,1000` | 16 | 24 | 1 | 53 | 1–9 |
| 5 | `0000,0001,0010,0100,1001` | 192 | 2 | 1 | 79 | 1–13 |
| 6 | `0000,0001,0010,0100,1011` | 192 | 2 | 1 | 118 | 1–16 |
| 7 | `0000,0001,0010,0100,1111` | 64 | 6 | 1 | 165 | 1–18 |
| 8 | `0000,0001,0010,0101,0110` | 192 | 2 | 0 | — | — |
| 9 | `0000,0001,0010,0101,1010` | 192 | 2 | 1 | 108 | 1–16 |
| 10 | `0000,0001,0010,0101,1011` | 384 | 1 | 1 | 120 | 1–16 |
| 11 | `0000,0001,0010,0101,1110` | 384 | 1 | 1 | 162 | 1–20 |
| 12 | `0000,0001,0010,0111,1011` | 96 | 4 | 1 | 125 | 1–17 |
| 13 | `0000,0001,0010,0111,1100` | 192 | 2 | 1 | 174 | 1–18 |
| 14 | `0000,0001,0010,0111,1101` | 384 | 1 | 1 | 168 | 1–20 |
| 15 | `0000,0001,0010,0111,1111` | 192 | 2 | 1 | 157 | 1–23 |
| 16 | `0000,0001,0010,1100,1101` | 192 | 2 | 0 | — | — |
| 17 | `0000,0001,0010,1100,1111` | 96 | 4 | 0 | — | — |
| 18 | `0000,0001,0010,1101,1110` | 96 | 4 | 0 | — | — |
| 19 | `0000,0001,0010,1101,1111` | 192 | 2 | 0 | — | — |
| 20 | `0000,0001,0110,0111,1010` | 192 | 2 | 0 | — | — |
| 21 | `0000,0001,0110,1010,1100` | 64 | 6 | 2 | 173 | 1–12 |
| 22 | `0000,0001,0110,1010,1101` | 192 | 2 | 2 | 237 | 1–18 |
| 23 | `0000,0001,0110,1010,1111` | 192 | 2 | 1 | 235 | 1–24 |
| 24 | `0000,0001,0110,1011,1110` | 192 | 2 | 1 | 225 | 1–27 |
| 25 | `0000,0011,0101,0110,1001` | 64 | 6 | 2 | 180 | 1–12 |
| 26 | `0000,0011,0101,1001,1110` | 16 | 24 | 3 | 246 | 1–12 |
| 27 | `0000,0011,0101,1010,1100` | 48 | 8 | 0 | — | — |

The orbit sizes sum to (4368=\binom{16}{5}), and every row satisfies

\[
|G\cdot T|\,|G_T|=384.
\]

Thus the table covers every five-subset, rather than a sampled prefix. There
are 17 independent orbits (3008 individual supports) and 10 dependent orbits
(1360 supports). The normalized-volume census over all 4368 supports is

\[
\#\{\operatorname{Vol}=0,1,2,3\}=(1360,2672,320,16).
\]

For each of the 17 independent representatives, direct integer expansion gives

\[
D_T(y)=\sum_{\alpha\in\mathbb Z_{\geq0}^5, |\alpha|=8}
c_{T,\alpha}y^\alpha,
\qquad c_{T,\alpha}\in\mathbb Z_{\geq0}, \tag{2}
\]

and at least one coefficient is positive. In fact, every nonzero coefficient
has the positive range displayed in the table. Equation (2) proves
(D_T(y)\geq0) on the nonnegative orthant. The complete list of exponents and
integer coefficients—not just the displayed ranges—is serialized in
`five_support_certificate.json`.

## Equality classification

For a support of size at most four, or an affinely dependent support of size
five, (P_4(x)=0). Since all variables are nonnegative,

\[
Q_4(x)=0
\quad\Longleftrightarrow\quad
\sum_{v\in F}x_v=0\text{ for some facet }F
\quad\Longleftrightarrow\quad
\operatorname{supp}x\subseteq V_4\setminus F.
\]

The complement (V_4\setminus F) is the opposite cube facet. Thus equality in
these cases holds exactly when the support lies in a facet. If the support is
an affinely independent five-set, all five (y_j) are positive. Because (2)
has at least one positive coefficient, (D_T(y)>0), so equality is impossible.
This proves both the inequality and the stated equality classification.

## Reproducibility and limits

Run, from the project root,

```sh
python evidence/verify_five_supports.py \
  --check evidence/five_support_certificate.json
```

The verifier uses only exact integer arithmetic and Python's standard library.
It reconstructs the vertices, all group maps, all supports, each determinant by
the 120-term Leibniz formula, all eight linear factors, and every coefficient
in (2). It also checks orbit membership, orbit–stabilizer identities, volume
invariance on every orbit, coverage totals, and byte-for-byte agreement with
the stored certificate. The certificate SHA-256 is
`33e1aad46c7d3f20c2eb24e12a5969af20935311185f49c8dd883b1ece44cb93`.

No floating-point optimization, random sampling, or numerical volume is used.
The result supplies no compression or polarization argument for larger
supports; in particular, it neither proves nor disproves full (HC4).

## Literature scope

The primary source identified in `source.md` proves the (d=3) inequality and
states that (d\geq4) remains open; it proposes exact sparse-support analysis
as a useful local route. The bounded primary-source comparison already recorded
in `problem.md` found no separate resolution of this five-support classification
as of 2026-09-09. That search is not a priority or novelty guarantee, and the
present claim is submitted only as an exact subsidiary result for fresh review.
