# Builder route: explicit 3-colorings and the four obstructions

## Result

For the graph on \(\mathbb Z/n\mathbb Z\) with edges of offsets \(1\) and
\(3\), and additionally offset \(n/2\) when \(n\) is even, the following
words are proper colorings with colors \(0,1,2\).  Put

\[
 A=01,\qquad B=21202.
\]

Reading a displayed word cyclically gives the colors of vertices
\(0,1,\ldots,n-1\).

\[
\begin{array}{c|c}
\text{orders} & \text{color word}\\ \hline
n\ge9\text{ odd} & A^{(n-5)/2}B\\
n\equiv2\pmod4 & A^{n/2}\\
n=20 & A^3BA^2B\\
n=4k\ge24 & A^{k-1}BA^{k-4}B.
\end{array}
\]

These four rows cover every \(n\ge6\) except \(7,8,12,16\).  The proof
below also shows directly that those four omitted graphs are not
3-colorable.  Thus the Builder route alone proves the full zero-set theorem;
no transfer matrix, recurrence, asymptotic estimate, or finite computation is
needed.

## 1. Increment-word reduction

Identify the three colors with \(\mathbb Z/3\mathbb Z\).  In any proper
coloring define

\[
 \epsilon_i=c_{i+1}-c_i\pmod3,
\]

and represent its two nonzero possibilities by the integers \(+1\) and
\(-1\).  The edge of offset \(3\) at \(i\) is proper precisely when

\[
 \epsilon_i+\epsilon_{i+1}+\epsilon_{i+2}\not\equiv0\pmod3.
\]

A sum of three signs is divisible by \(3\) exactly when all three signs are
equal.  Hence the offset-1 and offset-3 conditions are equivalent to a cyclic
sign word with no three cyclically consecutive equal signs.  Closing the
color word additionally says

\[
 \sum_{i=0}^{n-1}\epsilon_i\equiv0\pmod3. \tag{1}
\]

For \(n=2m\), the diametric edge from \(i\) to \(i+m\) is proper precisely
when

\[
 \sum_{j=0}^{m-1}\epsilon_{i+j}\not\equiv0\pmod3. \tag{2}
\]

All indices in (1)--(2) are cyclic.  Conversely, a sign word satisfying
these conditions reconstructs a coloring after choosing \(c_0\), so the
reduction loses no information.

## 2. Verification of the displayed constructions

First ignore diameters.  Inside any \(A\)-string the word alternates, so
colors at offsets \(1\) and \(3\) differ.  Inside \(B=21202\), adjacent
symbols differ and the two internal offset-3 comparisons are
\(2\ne0\) and \(1\ne2\).  It remains only to inspect a junction.  Its full
local context is one of

\[
 \cdots0101\mid21202\cdots,
 \qquad
 \cdots21202\mid0101\cdots.
\]

Across the first junction the three offset-3 comparisons are
\((1,2),(0,1),(1,2)\); across the second they are
\((2,0),(0,1),(2,0)\).  The adjacent symbols at the two junctions are also
different.  Consequently every cyclic word made from \(B\)'s separated by
blocks \(A^r\) with \(r\ge2\) satisfies all offset-1 and offset-3 edges.
This proves the required local conditions for the odd row and for both
\(0\pmod4\) rows.

For \(n\equiv2\pmod4\), the word \(A^{n/2}\) alternates.  The offsets \(1\)
and \(3\) are odd, and the diameter \(n/2\) is also odd, so all three types
of edge have differently colored endpoints.

It remains to check diameters in the two \(0\pmod4\) rows.  For \(n=20\),
split the word into its two length-10 halves:

\[
 A^3BA^2B
 =\underbrace{0101012120}_{X}\,
  \underbrace{2010121202}_{Y}.
\]

Every coordinate of \(X\) differs from the corresponding coordinate of
\(Y\), as is visible digit by digit.  These are exactly the ten diametric
pairs.

Now let \(n=4k\) with \(k\ge6\).  Splitting at the diameter gives

\[
 A^{k-1}BA^{k-4}B
 =\underbrace{A^{k-1}21}_{X}\,
  \underbrace{202A^{k-4}B}_{Y},
\]

where \(|X|=|Y|=2k\).  Number coordinates of the halves from \(0\) to
\(2k-1\).  On coordinates \(0,1,2\), their substrings are respectively
\(010\) and \(202\).  On coordinates \(3\le j\le2k-6\), both entries are
in alternating strings but with opposite parity, so \(X_j\ne Y_j\).  On the
last five coordinates their substrings are respectively

\[
 10121\qquad\text{and}\qquad21202.
\]

Again the entries differ coordinatewise.  Therefore all diametric edges are
proper.  This completes the construction proof.

## 3. Nonexistence at \(7,8,12,16\)

Suppose a coloring exists, let \(p\) be the number of \(+1\)'s in its
increment word, and use the reduction above.  Equation (1) gives

\[
 2p-n\equiv0\pmod3. \tag{3}
\]

Because no three cyclically consecutive signs are equal, whenever both signs
occur the number of occurrences of either sign is at most twice the number
of occurrences of the other: decompose the cyclic word into runs, each of
which has length at most two.

The one-sign cases are themselves impossible, since they contain a cyclic
run of three.  Thus the ratio bound applies to every remaining candidate.

For \(n=7\), (3) gives \(p\equiv2\pmod3\), hence \(p=2\) or \(5\).  In
either case the majority sign occurs five times and the minority sign twice,
contradicting \(5\le2\cdot2\).  Thus \(C_7^{(3)}\) is not 3-colorable.

For the remaining three orders, (3) and the run bound give

\[
\begin{array}{c|c|c}
n&\text{possibilities from (3)}&\text{sole possibility after the run bound}\\\hline
8&1,4,7&4\\
12&0,3,6,9,12&6\\
16&2,5,8,11,14&8.
\end{array}
\]

(For \(n=16\), for example, \(11>2\cdot5\); the more extreme cases are
immediate.)  Thus in every case \(n=2m\) and the increment word has exactly
\(m\) plus signs.

Let \(q_i\) be the number of plus signs in the length-\(m\) cyclic window
starting at \(i\).  The opposite window contains the remaining plus signs,
so

\[
 q_{i+m}=m-q_i.
\]

Here \(m=4,6,8\) is even.  Also
\(|q_{i+1}-q_i|\le1\), since moving a window one step deletes one sign and
adds one sign.  Along the successive windows from \(i\) to \(i+m\), the
integer values therefore pass through \(m/2\) (and if already
\(q_i=m/2\), there is nothing to prove).  For such a window the sum of its
\(m\) signs is

\[
 q_i-(m-q_i)=2q_i-m=0,
\]

contradicting the diametric condition (2).  Hence the graphs at
\(n=8,12,16\) are not 3-colorable.

Combining Sections 2 and 3 yields

\[
 a(n)=0\quad\Longleftrightarrow\quad n\in\{7,8,12,16\}
 \qquad(n\ge6).
\]

## 4. Provenance and independent diagnostic

The graph definition was checked against OEIS A383733 (accessed
2026-08-29), whose comment defines offset-3 chords and adds diametric edges
for even \(n\).  The proof above is elementary and does not depend on the
OEIS counts or on the SciNet computation to \(3000\).

The serialized pattern data are in
`certificates/builder_construction_spec.json`.  The independent diagnostic
`certificates/verify_builder_construction.py` reconstructs the displayed
words and checks graph edges directly; separately, it exhausts all
\(2^n\) increment words at \(n=7,8,12,16\).  A reproducible command is

```bash
python3 certificates/verify_builder_construction.py --max-n 10000
```

This computation is supplemental only.  Infinite coverage and the four
nonexistence statements are proved by the hand-checkable arguments above.
No proof assistant was used.
