# Exact result: `L_8 = 94`

## The target count

The number of primitive binary words of length eight is, by Möbius
inversion,

\[
 \sum_{d\mid 8}\mu(d)2^{8/d}=2^8-2^4=240.
\]

Every primitive rotation orbit has size eight and has one lexicographically
least representative. Hence there are `240/8 = 30` binary Lyndon words of
length eight. The certificate checkers also enumerate the 30 targets directly
from the locked definition.

## Occurrence-order lower bound

For distinct length-eight words `x,y`, let

\[
 \operatorname{ov}(x,y)=\max\{k\in\{0,\ldots,7\}:
       \operatorname{suf}_k(x)=\operatorname{pre}_k(y)\}.
\]

Let `W` be any common superstring. Choose one occurrence of every target and
sort the 30 chosen starting positions, obtaining distinct targets
`x_1,...,x_30` at positions `p_1<...<p_30`. (Equal starting positions would
give equal length-eight factors.) For each consecutive pair,

\[
 p_{r+1}-p_r \ge 8-\operatorname{ov}(x_r,x_{r+1}).
\]

This is immediate when the displacement is at least eight; for a smaller
displacement, the two overlapping occurrences force a suffix-prefix match of
length `8-(p_{r+1}-p_r)`. Since `|W| >= p_30-p_1+8`,

\[
 |W|\ge 240-\sum_{r=1}^{29}\operatorname{ov}(x_r,x_{r+1}). \tag{1}
\]

## Exact assignment-dual certificate

Adjoin a dummy node `*`, and give arcs incident with it weight zero. The arcs

\[
 *\to x_1,\quad x_1\to x_2,\ldots,x_{29}\to x_{30},\quad x_{30}\to *
\]

form a permutation assignment on the 31 nodes. Thus the overlap sum in (1)
is at most the maximum weight of the assignment relaxation.

In lexicographic target order followed by `*`, the following integer vectors
are a feasible dual assignment certificate:

```text
u = 6 6 6 6 6 1 6 1 4 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
v = 0 1 0 1 0 1 0 1 1 0 6 0 1 0 6 0 3 7 5 7 0 7 7 5 7 7 7 7 7 7 0
```

For every two distinct nodes `i,j`, direct suffix-prefix comparison gives

\[
 u_i+v_j\ge c_{ij},
\]

where `c_ij=ov(i,j)` for two real nodes and is zero for an arc incident with
the dummy. The two vector sums are 45 and 101. Summing the selected 31 dual
inequalities of any permutation assignment therefore bounds its weight by
`45+101=146`. This is a finite integer certificate: the primary verifier
checks all `31*30=930` inequalities, and the independent checker ignores these
vectors and recomputes the assignment optimum by an integer Hungarian
algorithm. Equation (1) yields

\[
 |W|\ge 240-146=94. \tag{2}
\]

## Matching word

The literal word

```text
0001100110101000010011110100011101100010101110000010111110000110111100100101101100000001111111
```

has length 94. Its 30 target occurrences begin at positions (zero based)

```text
80 81 45 82 13 46 57 83 14 35 47 0 58 26 84
68 15 36 71 48 5 59 27 18 85 37 72 49 60 86
```

when the targets are listed lexicographically. Direct substring/rolling-window
checks establish coverage. Together with (2), this proves

\[
 \boxed{L_8=94}.
\]

No floating-point result or solver status is used in the proof. The numerical
MILP run was only a discovery mechanism for the path and dual; certification
uses integer/string arithmetic.
