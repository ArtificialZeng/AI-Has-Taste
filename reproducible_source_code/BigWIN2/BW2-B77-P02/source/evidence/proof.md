# Proof certificate: injectivity through weight eight

## Statement

With the definitions frozen in `source.md` and `problem.md`, the canonical map

\[
\bar Z:\mathcal Z_*^{\mathrm f}=H_*^0/I\longrightarrow\mathcal Z_{q,0}
\]

is injective on the induced filtered piece (W_8\mathcal Z_*^{\mathrm f}).
This is a computer-assisted exact proof.  It does not address weights above
eight.

## Two finite integer matrices

Let (V=W_8H^0).  Its ordered word basis consists of the empty word and all
(z_{s_1}\cdots z_{s_k}) with (s_1\geq1), later (s_i\geq0), and
(\sum_i\max(s_i,1)\leq8).  The exact-weight counts, starting at weight zero,
are

\[
1,1,3,8,21,55,144,377,987,
\]

so (\dim_{\mathbb Q}V=1597).

Define (J\subset V) to be the span of all nonzero vectors

\[
v*(\tau(u)-u),\qquad
u,v\text{ basis words},\quad \operatorname{wt}(u)+\operatorname{wt}(v)\leq8.
\tag{1}
\]

The quasi-shuffle recursion has integer coefficients.  Moreover

\[
\max(a+b,1)\leq\max(a,1)+\max(b,1)
\]

for nonnegative (a,b), so every vector in (1) is supported in (V).
It is visibly in the full quasi-shuffle ideal (I).  In the ordered word
basis, the 4636 nonzero vectors in (1) form the rows of an integer matrix
(R\) of size (4636\times1597).

For (0\leq n\leq164), define the second integer matrix by

\[
C_{n,w}=[q^n]Z(w).
\tag{2}
\]

Thus (C) has size (165\times1597).  These coefficients are integers.  To
compute them, put

\[
F_{s,m}(q)=
\begin{cases}
1,&s=0,\\
(q^m/(1-q^m))^s,&s>0,
\end{cases}
\]

and, also for suffixes whose first index may be zero, put

\[
H_{(s,t)}(M)=H_{(s,t)}(M-1)+F_{s,M}H_t(M-1),
\qquad H_{\varnothing}(M)=1.
\tag{3}
\]

Here (H_w(0)=0) for nonempty (w). All series in (3) are truncated after
(q^{164}). Formula (3) is simply the
partition according to whether the largest strict summation index is (M).
The nonzero coefficients of its factor are

\[
[q^{m\ell}]F_{s,m}=\binom{\ell-1}{s-1}
\quad(s>0,\ \ell\geq s).
\tag{4}
\]

For an admissible word the first index is positive, so a largest summation
index above 164 cannot affect a coefficient through degree 164.  Consequently
(3)--(4) compute (2) exactly, not numerically.

## Modular certificates

The script `evidence/weight8_certificate.py` constructs (R) and (C) over
the integers and reduces them modulo a user-selected prime.  It translates
(\tau) by expanding a word as the binary string
(1^{s_1}0\cdots1^{s_k}0), reversing the string, complementing its bits, and
parsing it back into indices.  It implements the defining three-term
quasi-shuffle recursion directly.

For (p=1000003), the serialized certificate gives

\[
\operatorname{rank}_{\mathbb F_p}(R)=1432,
\qquad
\operatorname{rank}_{\mathbb F_p}(C)=165.
\tag{5}
\]

It records the row and column indices of a (1432\times1432) minor of (R)
whose determinant is (795164\pmod p), and a (165\times165) minor of (C)
whose determinant is (372525\pmod p). Both are nonzero. The second-prime
repeat at (p=1000033) gives the same two ranks, with determinant residues
(221688) and (994554), respectively.  In both runs, all 4636 rows of (R)
were also checked against all 165 coefficient functionals and had zero image
modulo the prime.

The decisive files are:

- `evidence/full_certificate_p1000003.json`;
- `evidence/full_certificate_p1000033.json`;
- `evidence/weight8_certificate.py`.

They can be regenerated with

```sh
python3 evidence/weight8_certificate.py --stage full \
  --max-q-degree 164 --prime 1000003 \
  --output evidence/full_certificate_p1000003.json --quiet
python3 evidence/weight8_certificate.py --stage full \
  --max-q-degree 164 --prime 1000033 \
  --output evidence/full_certificate_p1000033.json --quiet
```

A determinant of an integer matrix which is nonzero modulo a prime is nonzero
over (\mathbb Q).  Hence (5) proves

\[
\operatorname{rank}_{\mathbb Q}(R)\geq1432,
\qquad
\operatorname{rank}_{\mathbb Q}(C)\geq165.
\tag{6}
\]

## Rank-nullity conclusion

Mozgovoy's Theorem 3.5 gives (Z(\tau(u)-u)=0), and (Z) is a
quasi-shuffle algebra map.  Therefore every row of (R) is killed by every
coefficient functional in (C), so

\[
J=\operatorname{rowspan}_{\mathbb Q}(R)\subseteq\ker C.
\]

Since (V) has dimension 1597, (6) and rank-nullity give

\[
1597\geq \dim J+\operatorname{rank}C\geq1432+165=1597.
\]

All inequalities are equalities.  In particular (\ker C=J\subseteq I).
If (a\in V) has (Z(a)=0) as a formal series, then its first 165
coefficients vanish, hence (Ca=0), hence (a\in J\subseteq I).  This is
exactly the quantified assertion in `problem.md`, and proves injectivity of
(\bar Z) on (W_8\mathcal Z_*^{\mathrm f}).

This argument deliberately does not assert in advance that the rows (1)
generate all of (I\cap V).  Possible filtered cancellations involving
higher-weight products are irrelevant: the explicit subspace (J\subseteq I)
already saturates the complementary coefficient-rank bound.
