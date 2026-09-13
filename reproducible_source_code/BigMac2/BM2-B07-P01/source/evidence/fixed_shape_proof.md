# Exact resolution for the shape \((2,5)\)

This is the decisive mathematical dossier for the frozen statement in
`source.md`.  Word juxtaposition denotes concatenation, (X^m) denotes (m)
copies of a finite word, and (W^\omega) denotes infinite repetition.

Literature scope is recorded in `evidence/literature_screen.md`.  In
particular, an anonymous 2009 note already states (without proof) the same
zero/nonzero preperiod classification, while its displayed period for two
positive residue classes appears to contain a typo.  The contribution below
is therefore a complete proof and exact certificate, not a claim that the
classification was never previously stated.

## 1. The source predicates for this shape

In Manabe's notation, (a=2), (b=5), (a+b=7),
\(\delta=b-a=3=1\cdot a+1\), so \(\eta=1\) and \(\varepsilon=1\).
The shape is non-harmonic and (b>2a).  Lemma 14, Theorem 57, and
Theorem 28 of `literature/2609.05358v1.pdf` therefore give, respectively,

\[
 \Theta_7=\{2,5\},\qquad
 \Theta_{c+2}=\{\delta-a,b\}=\{1,5\},
\]

and, in the odd-(\eta) formula of Theorem 28,

\[
 C_{2,5}=[3,3]\mathbin\sqcup[6,6]=\{3,6\},\qquad
 \Theta_{c+5}=C_{2,5}\mathbin\sqcup\{a\}=\{2,3,6\}.
\]

Thus precisely the residues (1,2,3,5,6\pmod 7) are admissible.  Since
\(\gcd(2,5,c)=1\), (c>5), and (c\ne7), Manabe's Theorem 32 applies to
every such (c).  It proves pure periodicity and, by its minimality clause,
the least periods

\[
 \lambda(c)=
 \begin{cases}
 c+2,&c\equiv1\pmod7,\\
 7,&c\equiv2,5\pmod7,\\
 c+5,&c\equiv3,6\pmod7.
 \end{cases}
\]

There is no proper-divisor exception here: Theorem 32 and Proposition 46
give the displayed candidate itself as the least period for this primitive,
non-harmonic shape.  It remains only to exclude residues (0) and (4).

## 2. Exact nim words at the two non-admissible residues

Put

\[
\begin{array}{c|c}
B=0011021&E=0011223\\
A=0210210&C=0110210\\
D=011021&F=32203103\\
H=1001102&I=1021021\\
J=02.&
\end{array}
\]

The following identities are at the full nim-value level.

**Lemma 1 (residue 4).**  If (c=7k+4), (k\ge1), then

\[
 (G_c(n))_{n\ge0}=B^kE\bigl(AC^{k-1}D\bigr)^\omega.       \tag{1}
\]

The periodic tail in (1) begins at
\(q=7k+7=c+3\), and its displayed period has length
\(7+7(k-1)+6=7k+6=c+2\).

**Lemma 2 (residue 0).**  If (c=7k), (k\ge2), then

\[
 (G_c(n))_{n\ge0}=B^kF\bigl(H^{k-1}IJ\bigr)^\omega.       \tag{2}
\]

The periodic tail in (2) begins at
\(q=7k+8=c+8\), and its displayed period has length
\(7(k-1)+7+2=7k+2=c+2\).

### Proof of Lemmas 1 and 2

For a proposed word (x=(x_n)_{n\ge0}), define its padded recurrence
signature at (n) by

\[
 \sigma_c(n)=(x_{n-2}^*,x_{n-5}^*,x_{n-c}^*;x_n),
\]

where an entry is `*` when its index is negative and is then omitted from
the mex set.  Direct substitution of the finite words above gives the
following complete list of possible *sets* of available option values:

\[
\begin{array}{c|c|c}
\text{families}&\{x_{n-s}:s\in\{2,5,c\},\ s\le n\}&x_n\\ \hline
0,4&\varnothing&0\\
0,4&\{0\}&1\\
0,4&\{0,2\}&1\\
0,4&\{1\}&0\\
0,4&\{1,2\}&0\\
0,4&\{1,3\}&0\\
0,4&\{0,1\}&2\\
0,4&\{0,1,3\}&2\\
0,4&\{0,1,2\}&3\\
0&\{0,3\}&1\\
0&\{0,2,3\}&1\\
0&\{1,2,3\}&0
\end{array}                                                     \tag{3}
\]

Every last entry in (3) is the mex of the middle entry.  Here is a
finite, all-(k) audit of the substitution leading to (3).  Write the
candidate as (UW^\omega), with (q=|U|) and (p=|W|=c+2).
For (n\ge q+c), all four entries of a signature lie in the tail, and
the signature is (p)-periodic.  Moreover, within the tail the (c)-move
has offset

\[
 -c\equiv2\pmod p.                                             \tag{4}
\]

It is therefore enough to inspect (0\le n<q+c+p).  In the only long
transition range, (q\le n<q+c), the current length-(c) word and its
length-(c) string of (c)-predecessors are exactly

\[
\begin{array}{c|c|c}
c& (x_q,\ldots,x_{q+c-1})&(x_{q-c},\ldots,x_{q-1})\\ \hline
7k+4&AC^{k-1}D[0{:}4]&B[3{:}7]B^{k-1}E\\
7k&H^{k-1}I&B[1{:}7]B^{k-2}F.
\end{array}                                                     \tag{5}
\]

All full repeated pieces in (5) have length seven.  The other two moves
have lengths two and five, so expanding one copy of each displayed block,
each adjacent block boundary, and the fixed end fragments exhausts the
signatures; inserting another (B/C) pair in the first row or another
(B/H) pair in the second only repeats the same seven aligned checks.
In the cyclic range, (4) likewise makes the three inspected offsets
(-2,-5,+2), so one copy of each block and adjacent cyclic boundary
exhausts that range.  The expansion is precisely (3).  For complete
entry-by-entry audit, including the order of the three predecessors and
the wall entries, the constants `SIG4` (20 signatures) and `SIG0`
(25 signatures) in `evidence/fixed_shape_certificate.py` serialize this
same finite table.

Consequently the words in (1) and (2) satisfy the wall-convention mex
recurrence at every (n\).  That recurrence determines its sequence
uniquely by induction on (n), so the proposed words are (G_c).  This
proves both lemmas.  (The certificate script also recomputes the recurrence
directly for any requested finite collection of parameter values; that
sanity check is not used as the universal argument.)

## 3. An eventual period cannot hide a pure period

**Lemma 3.**  If a sequence (x) is periodic from (0) with some period
(d>0), and (p) is a period of (x) from some index (q) onward, then
(p) is already a period from (0).

Indeed, for any (n\ge0), choose (m\ge0) with (n+md\ge q).  Pure
(d)-periodicity and then tail (p)-periodicity give

\[
 x_{n+p}=x_{n+p+md}=x_{n+md}=x_n.
\]

In both (1) and (2), (p=c+2) is a tail period, but it is not a period
from zero.  Namely,

\[
\begin{array}{c|c|c}
c\bmod7&G_c(0)&G_c(c+2)\\ \hline
4&0&E[6]=3\\
0&0&F[2]=2.
\end{array}
\]

Lemma 3 therefore rules out pure periodicity with *any* period in both
non-admissible residue families.

## 4. Conclusion

For every integer (c>5), (c\ne7), the full Sprague--Grundy sequence
of \(\{2,5,c\}\) is purely periodic exactly for

\[
 c\bmod7\in\{1,2,3,5,6\}
 =\Theta_7\cup\Theta_{c+2}\cup\Theta_{c+5},
\]

and its least period in the positive cases is exactly the value displayed
in Section 1.  Thus the frozen original assertion is proved, not merely
verified over finitely many (c).

## Reproduction note

Run

```text
python3 evidence/fixed_shape_certificate.py --max-k 1000
```

to reproduce the exact finite sanity check used during discovery.  On
2026-09-08 it checked 1,999 parameter instances, reported the fixed
20/25-signature tables, and found no discrepancy.  The all-(k) proof is
the finite block/signature argument above.
