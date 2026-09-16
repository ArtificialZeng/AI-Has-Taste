# Precise reading

## Objects and conventions

For each integer \(c>5\) with \(c\ne 7\), let
\[
S_c=\{2,5,c\}.
\]
The normal-play subtraction game is played on one heap of size \(n\in
\mathbb Z_{\ge 0}\); a legal move replaces \(n\) by \(n-s\) for some
\(s\in S_c\) with \(s\le n\). Its Sprague--Grundy sequence is the unique
map \(g_c:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}\) satisfying
\[
g_c(n)=\operatorname{mex}\{g_c(n-s):s\in S_c,\ s\le n\},
\]
where \(\operatorname{mex}\) is the least nonnegative integer outside the
displayed finite set. In particular, the empty set at \(n=0\) has mex zero.

Write the sequence as the one-sided word
\(g_c(0)g_c(1)g_c(2)\cdots\). Concatenation is implicit, \(W^K\) is the
concatenation of \(K\) copies of a finite word \(W\), and \(W^\infty\) is
the right-infinite repetition of nonempty \(W\).

Define the minimal preperiod
\[
q_c=\min\{q\ge0:\text{ there is a }p\ge1\text{ such that }
g_c(n+p)=g_c(n)\text{ for every }n\ge q\}.
\]
Define \(p_c\) to be the least positive \(p\) satisfying the displayed
identity at \(q=q_c\). Thus “purely periodic” means \(q_c=0\), and
“positive minimal preperiod” means \(q_c>0\).

## Frozen claim and research scope

The source asks for Conjecture 50 of arXiv:2609.05358v1 to be decided for
every \(S_c\) above. The project source says that results already in that
paper cover the residue zones other than
\[
c\equiv0,4\pmod 7,
\]
subject to checking the cited theorem and all small boundary cases. Those
known zones are part of the whole-shape audit but need not be reproved unless
the check exposes a gap. The genuinely new obligations are:

1. for every \(K\ge1\) (so \(c=7K+4\ge11\)), decide whether \(q_c>0\);
2. for every \(K\ge2\) (so \(c=7K\ge14\); \(c=7\) is excluded), decide
   whether \(q_c>0\).

A universal proof or counterexample for those quantified families is needed;
verification of finitely many values of \(K\) does not decide the source
claim.

## Strong provisional formulas (not part of the frozen claim)

Let \(A=0011021\). The computational leads strengthen the required
positivity assertions to the following exact claims:
\[
g_{7K+4}=A^K\,0011223\,(021021\,A^K)^\infty\qquad(K\ge1),
\]
with proposed exact minima
\[
(q_{7K+4},p_{7K+4})=(7K+7,7K+6)=(c+3,c+2),
\]
and
\[
g_{7K}=A^K\,32203103\,(1\,A^{K-1}\,02102102)^\infty
\qquad(K\ge2),
\]
with proposed exact minima
\[
(q_{7K},p_{7K})=(7K+8,7K+2)=(c+8,c+2).
\]
Proving an infinite-word identity requires exact mex verification at all
block interiors and seams, uniformly in \(K\). Exactness of \(p_c\) further
requires ruling out every smaller eventual period, and exactness of \(q_c\)
requires ruling out periodicity beginning before the displayed prefix.
A mismatch at any index disproves only the corresponding provisional formula
unless it also settles Conjecture 50 itself.

## Source-status note

The local primary-source PDF was checked directly on 2026-09-07. It is
arXiv:2609.05358v1, Hikaru Manabe, *Purely Periodic Three-move Subtraction
Games*, submitted 2026-09-04. Theorem 32 and Table 1 (PDF pp. 21--22),
Conjecture 50 (PDF p. 33), Theorem 28, and Theorem 57 together verify the
specialization: for \((a,b)=(2,5)\), the proved purely periodic residues are
\(1,2,3,5,6\pmod7\), and the conjectured positive-preperiod residues are
exactly \(0,4\pmod7\). The checked copy is
`evidence/external/2609.05358v1.pdf`, SHA-256
`39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`.
This verifies the source statement but is not by itself a claim of broader
priority.
