# Uniform proof for the two missing residue classes

All words below are words of decimal digits.  Put
\[
A=0011021,\quad B=0011223,\quad C=021021,
\quad D=32203103,\quad E=02102102.
\]
For a tuple of digits, `mex` means the mex of the set of its entries; repeated
entries therefore have no effect.

## Theorem

For every integer \(K\geq1\), the Sprague--Grundy word for
\(S=\{2,5,7K+4\}\) is
\[
 A^K B\,(C A^K)^\infty.
\]
Its minimal preperiod and least eventual period are respectively
\[
 q=7K+7=c+3,\qquad p=7K+6=c+2.
\]
For every integer \(K\geq2\), the Sprague--Grundy word for
\(S=\{2,5,7K\}\) is
\[
 A^K D\,(1 A^{K-1}E)^\infty,
\]
and its corresponding exact parameters are
\[
 q=7K+8=c+8,\qquad p=7K+2=c+2.
\]

Consequently, in both residue classes the minimal preperiod is positive.

## A finite certification lemma

Let \(X\) be a proposed word with prefix of length \(q\) followed by the
infinite repetition of a word \(P\) of length \(p=c+2\).  It is enough to
check the mex recurrence in the following three ranges:

1. \(0\leq n<c\);
2. \(n=c+m\), where \(0\leq m<q\);
3. cyclically on \(P\), using
   \[
   P_r=\operatorname{mex}\{P_{r-5},P_{r-2},P_{r+2}\}
   \quad(r\bmod p).
   \tag{1}
   \]

Indeed, the second range checks through \(n=q+c-1\).  If \(n\geq q+c\),
then all predecessors are in the periodic tail and
\(n-c=n+2-p\), so the third predecessor has the same letter as \(n+2\).
Thus (1) is precisely the recurrence in the remaining range.  A word passing
these checks equals the Sprague--Grundy word by forward uniqueness of the mex
recurrence.

The first range in both families is a prefix of \(A^\infty\).  For
\(0\leq n\leq4\), direct use of the legal predecessors gives `00110`.
At \(n=5,6\) it gives `21`.  Thereafter the following cyclic table proves the
two-move recurrence for \(A\).  Here \(i\) is the index in \(A\), and the
triple is \((A_{i-5},A_{i-2},A_{i+2})\); the last entry duplicates the first
because \(-5\equiv2\pmod7\).

| \(i\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 0 | 0 | 1 | 1 | 0 | 2 | 1 |
| triple | 121 | 111 | 000 | 202 | 111 | 010 | 000 |

In every table below, the current digit is the mex of its displayed triple.
Thus the tables are both the symbolic mex calculation and its certificate.

## The class \(c=7K+4\)

Here \(q=7K+7\), \(p=7K+6\), and \(P=CA^K\).  The cyclic check (1) consists
of the following seam rows:

| \(r\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | \(p-2\) | \(p-1\) |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 1 |
| triple | 121 | 110 | 002 | 221 | 110 | 000 | 221 | 111 | 000 | 202 | 111 | 010 | 002 |

All unlisted indices \(11\leq r\leq p-3\) (an empty range when \(K=1\))
are internal to the \(A\)-run and are rows of the seven-column base table,
with \(i\equiv r-6\pmod7\).  This proves (1) for every \(K\geq1\).

For the transient check, the triple displayed at \(m\) is
\[
 (X_{c+m-5},X_{c+m-2},X_m).
 \tag{2}
\]
When \(K=1\), the complete table is:

| \(m\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 2 | 2 | 3 | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 0 |
| triple | 110 | 010 | 021 | 121 | 130 | 202 | 221 | 310 | 000 | 221 | 111 | 002 | 202 | 113 |

For \(K\geq2\), the rows \(0\leq m\leq13\) are:

| \(m\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 2 | 2 | 3 | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 0 |
| triple | 110 | 010 | 021 | 121 | 130 | 202 | 221 | 310 | 000 | 221 | 111 | 000 | 202 | 111 |

The final seven rows, writing \(m=7K+t\), are:

| \(t\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 2 | 1 | 0 | 0 | 1 | 1 | 0 |
| triple | 010 | 000 | 121 | 111 | 002 | 202 | 113 |

The remaining range \(14\leq m\leq7K-1\) is empty for \(K=2\).  Otherwise
it is the base table with \(i\equiv m-2\pmod7\): the current tail letter is
\(A_{m-2}\), and the three entries of (2) become
\(A_{i-5},A_{i-2},A_{i+2}\).  This proves every transient row.

## The class \(c=7K\)

Now \(q=7K+8\), \(p=7K+2\), and \(P=1A^{K-1}E\).  For the cyclic check,
the first seam has the table

| \(r\) | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 1 | 0 | 0 | 1 | 1 | 0 |
| triple | 000 | 221 | 111 | 000 | 202 | 111 |

and, on writing \(r=c-8+t\), the final seam has

| \(t\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 2 | 1 | 0 | 2 | 1 | 0 | 2 | 1 | 0 | 2 |
| triple | 010 | 002 | 121 | 110 | 002 | 221 | 110 | 002 | 221 | 110 |

Every index in \(6\leq r\leq c-9\) is a base-table row with
\(i\equiv r-1\pmod7\).  This range is empty for \(K=2\), and the two seam
tables are then disjoint and exhaustive.  Hence (1) holds uniformly.

For the transient range, the first fourteen rows of (2) are

| \(m\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 3 | 2 | 2 | 0 | 3 | 1 | 0 | 3 | 1 | 0 | 0 | 1 | 1 | 0 |
| triple | 120 | 110 | 031 | 221 | 120 | 302 | 231 | 210 | 000 | 331 | 111 | 000 | 302 | 111 |

Writing \(m=c+t\), the final eight rows are

| \(t\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| current | 2 | 1 | 0 | 2 | 1 | 0 | 2 | 1 |
| triple | 013 | 002 | 122 | 110 | 003 | 221 | 110 | 003 |

The intervening range \(14\leq m\leq c-1\), empty for \(K=2\), again
reduces to the base table with \(i\equiv m-2\pmod7\).  This completes the
mex proof of both infinite words.

## Least periods and minimal preperiods

Both displayed period blocks are primitive.  A short uniform certificate is
given by the cyclic gaps between occurrences of the digit 2.

For \(P=CA^K\), the 2's are at positions
\(1,4,11,18,\ldots,7K+4\).  Their cyclic gap word is
\[
3\,7^K\,3,
\]
which, up to cyclic rotation, has one nonempty run of 3's and one nonempty
run of 7's.  For \(P=1A^{K-1}E\), the cyclic gap word is, up to rotation,
\[
7^{K-1}3^3.
\]
It has the same one-run property because \(K\geq2\).  A proper power
containing a 2 would make its cyclic 2-gap word the same proper power, which
would have at least two runs of each of its two gap symbols.  Therefore
neither period block is a proper power.

It follows that the periodic tail has least period \(p\).  Explicitly, any
period \(d\) of the tail makes rotation by \(d\bmod p\) fix \(P\); primitivity
forces \(p\mid d\), while \(p\) itself is a period.

Finally, for \(c=7K+4\), the prefix letter at \(q-1\) is the last letter of
\(B\), namely 3, whereas
\[
X_{q-1+p}=P_{p-1}=1.
\]
For \(c=7K\), the corresponding letters are the last letter 3 of \(D\) and
the last letter 2 of \(E\).  If periodicity began at some \(q'<q\) with
period \(d\), then its restriction to the tail would give \(p\mid d\), and
periodicity at \(q-1\) would equate exactly these unequal letters.  Thus no
smaller preperiod exists, proving the asserted exact \(q\)'s.

## Consequence for Conjecture 50 on the whole shape

The local primary source `evidence/external/2609.05358v1.pdf` has SHA-256
`39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`.
Its Theorem 32 and Table 1 (PDF pp. 21--22), together with Theorems 28 and 57,
give the following proved admissible zones for \((a,b)=(2,5)\):
\[
\rho\in\{2,5\}:p=7,\qquad
\rho=1:p=c+2,\qquad
\rho\in\{3,6\}:p=c+5.
\]
To see the last set directly from the source notation, here
\(\delta=3,\eta=1,\epsilon=1\), and Theorem 28 gives
\(C_{2,5}=\{3,6\}\).  Theorem 57 gives the new \(c+a\) angle
\(\delta-a=1\), while Lemma 14 gives the inert angles \(\{a,b\}=\{2,5\}\).
All these zones are purely periodic by Theorem 32.  The only remaining angles
are 0 and 4, and the theorem above proves positive minimal preperiod for every
admissible \(c\) in them (\(c=7K, K\ge2\), and \(c=7K+4,K\ge1\)).
The excluded value \(c=7\) is the additive point; the small value \(c=6\)
lies in the proved angle 6 zone.  Hence Conjecture 50 holds for every
\(c>5\), \(c\ne7\), in this entire shape.

## Literature-screening scope

The primary-source comparison above was checked directly in the cited v1 PDF.
An arXiv-focused exact-string search on 2026-09-07 for the family
\(\{2,5,c\}\) found that preprint but no separate source stating the two
parameterized words proved here.  This is a bounded search report, not a
claim of priority.
