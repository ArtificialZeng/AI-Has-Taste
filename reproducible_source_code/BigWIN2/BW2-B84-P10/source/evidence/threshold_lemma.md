# Sharp width gap for defective valid-extension sets

Proposer job: `win-00084-p10-research-674c4e058ca0`.

## Statement

Let (n\ge 3) and (S\in\mathcal G_n), with (K_S,C_S) and ordered
right anti-diagonal (e_1,\ldots,e_{n-1}) as fixed in `source.md` and
`problem.md`. Then

\[
K_S\ne C_S \quad\Longrightarrow\quad |K_S|\ge 10.
\]

The constant is sharp: (S=(2,3,5,9,15)) has
(K_S\ne C_S) and (|K_S|=10).

This is a subsidiary theorem. It does **not** classify all sequences of width
at most nine and does not resolve the frozen problem.

## Dependencies

Only the definitions and the following results of Muney,
*Holes in Valid-Extension Sets of Finite Gilbreath Sequences*,
arXiv:2606.23721v2, are used:

1. Proposition 18, equivalently the ordered reverse recurrence
   (T_{r-1}=P_{e_r}(T_r)), (T_{n-1}=\{1\}), with (D_S=T_0);
2. Theorem 20, which says that (K_S=C_S) exactly when
   (e_r\le 1+\sum_{j>r}e_j) for every (r\le n-2); and
3. the directly checkable first-hole example for sharpness.

No bounded computation is used in the proof.

## Proof

We first record two elementary constraints on a realizable right
anti-diagonal.

### Parity constraint

Every (s_j) with (j\ge2) is odd. Indeed, this holds for (s_2=3).
Inductively, reduce the bottom entry of the difference triangle of the prefix
((s_1,\ldots,s_j)) modulo two. Since absolute subtraction is addition
modulo two,

\[
1\equiv \sum_{a=1}^{j}\binom{j-1}{a-1}s_a\pmod2.
\]

Here (s_1=2\equiv0), while the contribution of the already-odd terms
(s_2,\ldots,s_{j-1}) is

\[
\sum_{a=2}^{j-1}\binom{j-1}{a-1}=2^{j-1}-2\equiv0\pmod2.
\]

Thus (s_j\equiv1\pmod2).

Consequently, the first positive row of the triangle has first entry (1)
and every later entry even. Induction down the triangle shows that every row
of length at least two has first entry (1) and all its later entries even:
the difference of two even entries is even, while the first entry is (1) by
the Gilbreath hypothesis. Therefore

\[
e_1,\ldots,e_{n-2}\text{ are even},\qquad e_{n-1}=1. \tag{1}
\]

### Zero-tail rigidity

For any (i\le n-2), if

\[
e_{i+1}=e_{i+2}=\cdots=e_{n-2}=0, \tag{2}
\]

then (e_i\in\{0,2\}). To see this, write row (i) as
((x_1,\ldots,x_L)). Its first entry is (x_1=1), its last entry is
(x_L=e_i), and (e_{i+r}) is the rightmost (r)-fold absolute difference
of this row. The consecutive zero values in (2) force
(x_2=\cdots=x_L). Formally, after the last (m) entries have been shown
equal to (c), the rightmost (m)-fold difference of
((x_{L-m},c,\ldots,c)) is (|x_{L-m}-c|), so the next zero extends the
constant suffix by one. Finally the first entry of row (i+1) is

\[
1=|x_2-x_1|=|e_i-1|,
\]

which gives (e_i=0) or (2).

Now suppose (K_S\ne C_S). By Theorem 20, at least one ordered inequality
fails. Let (i\) be the largest failing index and put

\[
q=\sum_{j=i+1}^{n-1}e_j.
\]

All inequalities strictly to the right of (i) hold. By (1), (q) is odd.
It cannot equal (1): in that case every even summand
(e_{i+1},\ldots,e_{n-2}) would vanish, zero-tail rigidity would give
(e_i\le2=1+q), contradicting the failure at (i). Hence

\[
q\ge3. \tag{3}
\]

Run the reverse recurrence only through the tail to the right of (i). The
holding inequalities there give, by a direct induction,

\[
T_i=\{0,2,4,\ldots,q+1\}. \tag{4}
\]

For completeness, the induction starts with
(P_1(\{1\})=\{0,2\}). If the current set is
(\{0,2,\ldots,R\}) and the next even entry (e) satisfies (e\le R),
then its two preimage branches have union
(\{0,2,\ldots,R+e\}).

The inequality at (i) fails, so (e_i>q+1). Applying (P_{e_i}) to (4)
therefore produces two reflected copies which meet only at (e_i):

\[
|T_{i-1}|=2|T_i|-1=q+2\ge5, \qquad 0\notin T_{i-1}. \tag{5}
\]

Every remaining outer preimage step is cardinality-nondecreasing, because
(P_e(T)) contains the injective translate (e+T). Thus
(|D_S|=|T_0|\ge5). If (0\notin D_S), reflection about (s_n) gives

\[
|K_S|=2|D_S|\ge10.
\]

If (0) enters during an outer step, consider the first such step. Just
before it, the set has at least five elements and does not contain zero. For
(0\in P_e(T)), necessarily (e\in T); hence (P_e(T)) contains both the
(|T|) positive, distinct elements of (e+T) and the additional element
(0). Its size is at least six, and subsequent steps cannot decrease it.
Therefore in this case

\[
|K_S|=2|D_S|-1\ge11.
\]

This proves the asserted lower bound. The exact reverse calculation for
((2,3,5,9,15)), reproduced in `threshold_census_n10.json`, gives width ten,
so the bound is sharp. \(\square\)

## Immediate reduction of the open classification

Write (e_i=2a_i) for (i<n-1). Since (e_1=s_n-s_{n-1}>0), the gap
theorem and Theorem 20 imply the exact reduction

\[
|K_S|\le9
\quad\Longleftrightarrow\quad
K_S=C_S\text{ and }A(S)\le7.
\]

Equivalently, the anti-diagonal must have exactly one of the following forms
(all unshown entries before the final (1) are zero):

1. (e_1=2);
2. (e_1=2) and one further (e_q=2), where (2\le q\le n-2);
3. (e_1=2) and two further entries (e_q=e_r=2), where
   (2\le q<r\le n-2); or
4. (e_1=4) and one further (e_q=2), where (2\le q\le n-2).

Indeed, (A=1+2\sum a_i\le7), so the positive integer (a_1) and the
other nonnegative (a_i)'s have total at most three. The normalized
completeness inequalities are
(a_i\le1+\sum_{j>i}a_j). Listing the partitions of totals one, two, and
three gives exactly the four displayed types. Conversely every displayed
type satisfies all the inequalities and has (A\le7).

This is a finite anti-diagonal reduction, not yet the explicit top-row
template classification required by the frozen problem: some displayed
anti-diagonals may be unrealizable, and a realizable anti-diagonal can come
from more than one top row.

## Exact computational attack

`enumerate_threshold.py` exhaustively generated both the ordered reverse-tree
frontier and an independently constructed direct difference-triangle frontier
through (n=10), comparing the two sets exactly at every length. It found no
defective sequence of width at most nine. The minimum defective width was ten
at each length (5\le n\le10), attained respectively by
(1,1,8,9,37,102) sequences. Every minimum-width hit was independently
rechecked by constructing the appended triangle for every integer in the
complete radius-(A(S)+1) range. See `threshold_census_n10.json`.

This census corroborates but is not needed for the all-length proof.

## Literature screen and scope

The local primary source `evidence/external/2606.23721v2.pdf` was inspected.
Its Section 16(5) asks for the width-at-most-nine classification, while its
Theorem 20 supplies the interval-completeness criterion used above; it does
not state the sharp defective-width gap proved here. On 2026-09-09, web
searches for the title together with “width nine”, “valid-extension”, and
“interval-completeness” found that preprint and bibliographic mirrors, but no
separate primary source claiming this lemma. This limited screen is not proof
of priority.

## Gap list

- No mathematical gap is presently known in the stated subsidiary theorem.
- The frozen original classification remains open: after the reduction, one
  must still classify all realizable ordered anti-diagonals with
  (A(S)\le7) (and translate that classification into explicit templates).
- Novelty has only the limited literature support described above and needs a
  fresh citation audit before release.
