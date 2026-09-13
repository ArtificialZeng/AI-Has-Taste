# Regular-slice obstructions for every mixed-sign case

Provenance: `bigMac-00011-p02-research-d67d5b979c71` (research pass 2,
2026-09-07).  All statements use the precise map and realization convention
of `problem.md`.  This note reconstructs the source obstruction for
`(1,-1,R)`, supplies the missing left-tie obstruction, and proves analogous
obstructions for `(1,-2,L/R)` and `(2,-1,L/R)`.

## A reusable regular-slice criterion

Let \(W_{m,n}\in\mathcal D\) be a family for which a deterministic two-way
finite-state transducer maps \(a^m\#b^n\) to \(W_{m,n}\), and suppose
\(|W_{m,n}|=O(m+n)\).  If a regular language \(K\) makes

\[
  \{a^m\#b^n:m,n\geq 1,\ \Phi_{u,d}^t(W_{m,n})\in K\}                 \tag{1}
\]

nonregular (allowing harmless fixed lower bounds on \(m,n\)), then
\(\Phi_{u,d}^t\!\upharpoonright_{\mathcal D}\) has no polyregular
realization.

Indeed, precompose a hypothetical realization with the stated 2DFT and
restrict to the regular parameter language.  The resulting polyregular map
has linear output growth because a level sort is length preserving.  The
linear-growth collapse makes it a deterministic MSO string transduction (or
2DFT), whose inverse image of \(K\) must be regular, contradicting (1).  This
is Proposition 5.6 of the primary source, with the same proof and with an
arbitrary 2DFT-generated Dyck slice in place of its two-pyramid slice.

We repeatedly use two elementary pumping facts.  For every fixed integer
\(c\geq0\),

\[
 \{a^m\#b^n:m,n\geq1,\ n\geq m+c\}                                  \tag{2}
\]

is nonregular: at the boundary word \(a^p\#b^{p+c}\), pumping a nonempty
piece of the initial \(a\)-block up violates the inequality.  Likewise
\(\{a^m\#b^n:n\leq m\}\) is nonregular, since pumping such a piece down in
\(a^p\#b^p\) violates that inequality.  Fixed lower bounds on the exponents
do not affect either argument.

## Weight `(1,-1)`: both tie orders

Put \(P_{m,n}=U^mD^mU^nD^n\).  Sorting the four run contributions one level
at a time gives, for the right tie order,

\[
\Phi_{1,-1}^{R}(P_{m,n})=
\begin{cases}
 UU(DU)^{2n-2}DD(UD)^{m-n},&n\leq m,\\
 UU(DU)^{2m-1}DD(UD)^{n-m-1},&n>m.
\end{cases}                                                         \tag{3}
\]

At level zero the two up-steps occur as \(UU\).  At every positive level at
which all four runs occur, decreasing input position gives \(DUDU\); after
one pyramid runs out, the remaining level blocks give exactly the displayed
central \(DD\) and tail.  Thus (3) is also a direct reconstruction of Lemma
6.3 in the primary source.

For the regular language

\[
 K_R=\{UU(DU)^{2q}DD(UD)^s:q,s\geq0\},
\]

the first exponent in (3) is even exactly when \(n\leq m\).  The first
\(DD\) fixes the factorization, so there is no alternative parse.  Hence
\(\Phi_{1,-1}^{R}(P_{m,n})\in K_R\) iff \(n\leq m\); (1) and the second
pumping fact prove non-polyregularity.

For the left tie order, the corresponding direct level calculation is

\[
\Phi_{1,-1}^{L}(P_{m,n})=
\begin{cases}
 UU(UD)^{2m-2}D(UD)^{n-m}D,&m\leq n,\\
 UU(UD)^{2n-2}UDD(UD)^{m-n-1}D,&m>n.
\end{cases}                                                         \tag{4}
\]

Here a four-run level contributes \(UDUD\), because positions increase
within a tie.  Restrict to \(m,n\geq2\) and set

\[
 K_L=\{UU(UD)^{2q+1}UDD(UD)^sD:q,s\geq0\}.
\]

In the first branch of (4), rewrite
\((UD)^{2m-2}D=(UD)^{2m-3}UDD\); the exponent before \(UDD\) is odd.  In
the second branch it is \(2n-2\), which is even.  The designated \(DD\) is
the first \(DD\) after the initial \(UU\), so again the parse is unique.
Consequently \(\Phi_{1,-1}^{L}(P_{m,n})\in K_L\) iff \(m\leq n\).  This is
(2) with \(c=0\), and (1) proves the missing left-tie lower bound.

## Weight `(1,-2)`: a zigzag followed by a mountain

Let

\[
 Z_{m,n}=(UD)^mU^nD^n\in\mathcal D,
 \qquad r=n-m.
\]

A sequential transducer outputs \(UD\) for each \(a\), then a 2DFT makes
one \(U\)-pass and one \(D\)-pass over the \(b\)-block, so this is an
admissible slice for (1).  The starting levels of its four kinds of steps are

\[
\begin{array}{c|c|c}
\text{step}&\text{index range}&\text{starting level}\\ \hline
U\text{ in }(UD)^m&1\leq j\leq m&1-j\\
D\text{ in }(UD)^m&1\leq j\leq m&2-j\\
U\text{ in }U^n&1\leq k\leq n&k-m-1\\
D\text{ in }D^n&1\leq k\leq n&r-2k+2.
\end{array}                                                         \tag{5}
\]

For left ties, (5) shows

\[
 \Phi_{1,-2}^{L}(Z_{m,n})\text{ ends in }UD
 \quad\Longleftrightarrow\quad r\geq2.                              \tag{6}
\]

If \(r\geq2\), the unique top-level step is the first mountain \(D\), at
level \(r\), and the preceding level ends in the last mountain \(U\), so the
suffix is \(UD\).  At the boundary \(r=2\), the old zigzag \(D\) tied at
level one precedes that \(U\), and the conclusion is unchanged.  If
\(r\leq1\), the top level is level one: it ends in the first zigzag \(D\)
(and also contains the mountain \(D\) when \(r=1\)).  The preceding level
ends in a \(D\), including the sole small case \(m=n=1\), so the suffix is
\(DD\), not \(UD\).

For right ties, the same table gives

\[
 \Phi_{1,-2}^{R}(Z_{m,n})\text{ ends in }UUD
 \quad\Longleftrightarrow\quad r\geq4.                              \tag{7}
\]

For \(r\geq4\), the top three level blocks (starting at level \(r-2\))
end as \(DU,U,D\), hence give \(UUD\).  If \(r=3\), level one ends in the
old zigzag \(D\), so the last three letters are \(DUD\); if \(r=2\) or
\(r=1\), they end in \(DD\).  For \(r\leq0\), level zero has right-tie
suffix \(DU\) (the mountain \(D\), when present, comes first), followed by
the top zigzag \(D\); its last three letters therefore are not \(UUD\).

Take respectively the regular suffix languages
\(\Sigma^*UD\) and \(\Sigma^*UUD\).  Equations (6)--(7) pull them back to
the nonregular languages (2) with \(c=2\) and \(c=4\).  Criterion (1) proves
both `(1,-2,L)` and `(1,-2,R)` non-polyregular.

## Weight `(2,-1)`: a mountain followed by a zigzag

Let

\[
 Y_{m,n}=U^mD^m(UD)^n\in\mathcal D,
 \qquad r=n-m.
\]

This slice is also generated by a 2DFT: make a \(U\)-pass and a \(D\)-pass
over the \(a\)-block, then output \(UD\) for every \(b\).  Its starting
levels are

\[
\begin{array}{c|c|c}
\text{step}&\text{index range}&\text{starting level}\\ \hline
U\text{ in }U^m&1\leq i\leq m&2(i-1)\\
D\text{ in }D^m&1\leq i\leq m&2m-i+1\\
U\text{ in }(UD)^n&1\leq j\leq n&m+j-1\\
D\text{ in }(UD)^n&1\leq j\leq n&m+j+1.
\end{array}                                                         \tag{8}
\]

For left ties, the top of (8) gives

\[
 \Phi_{2,-1}^{L}(Y_{m,n})\text{ ends in }DUDD
 \quad\Longleftrightarrow\quad r\geq1.                              \tag{9}
\]

When \(r\geq1\), the top two levels are singleton zigzag \(D\)'s.  The
preceding level ends in a zigzag \(D,U\) block; at \(r=1\), the original
mountain top supplies the \(D\) if the relevant earlier zigzag \(D\) is
absent.  Thus the suffix is \(DUDD\).  If \(r=0\), the last level is a
zigzag \(D\) and the preceding level consists only of \(D\)'s (apart from
the exceptional \(m=n=1\), whose whole output is \(UUDD\)).  If \(r<0\),
the top two or three original-mountain levels likewise end only in \(D\)'s.
None has the suffix in (9).

For right ties, a slightly longer fixed suffix removes the boundary ties:

\[
 \Phi_{2,-1}^{R}(Y_{m,n})\text{ ends in }DUDUDDD
 \quad\Longleftrightarrow\quad r\geq3.                              \tag{10}
\]

If \(r\geq3\), the top two blocks are singleton \(D\)'s, the next two are
right-tie \(UD\) blocks, and the preceding block ends in \(D\).  They give
exactly the asserted seven-letter suffix.  For \(r=2\), the next lower
boundary block is \(UDD\), so it cannot supply the required preceding
\(DUD\); when \((m,n)=(1,3)\), where one of those \(D\)'s is absent, the
output ends in \(UUDUDDD\), not the target suffix.  For \(r=1\) the
boundary block is again \(UDD\), with the small case \((1,2)\) giving
\(UUUDDD\).  For \(r=0\), at least three top letters are consecutive
\(D\)'s when \(m\geq2\), while \((1,1)\) gives \(UUDD\).  If \(r=-1\),
the top tie and the level below it are all \(D\)'s (the smallest case
\((2,1)\) gives \(UUUDDD\)).  For \(r=-2\) and \(m\geq4\), the final
level blocks have suffix \(DDU,DD,D\), hence end in \(DDUDDD\); the
remaining case \((3,1)\) ends in \(UUDUDDD\).  For \(r=-3\) the top
blocks end in \(DDU,D,D\), and for \(r\leq-4\) they end in \(DU,D,D\),
so these outputs have only two final consecutive \(D\)'s.  Thus none of
the cases \(r\leq2\) ends in \(DUDUDDD\).

The regular suffix languages \(\Sigma^*DUDD\) and
\(\Sigma^*DUDUDDD\) pull back, by (9)--(10), to (2) with \(c=1\) and
\(c=3\).  Criterion (1) proves both `(2,-1,L)` and `(2,-1,R)`
non-polyregular.

## Transport and complete table

For every word and tie order,

\[
 \Phi_{-u,-d}^{t}=\operatorname{rev}\circ\Phi_{u,d}^{\bar t}.        \tag{11}
\]

This follows because negating all levels reverses the order of the level
blocks, while reversing the output also reverses the within-block order.
Output reversal is an invertible regular transduction, so (11) transports
non-polyregularity as well as polyregularity.  Equations (3)--(10) therefore
settle all twelve mixed-sign labeled cases as non-polyregular.

Together with `evidence/nonnegative_cases.md`, the full classification is:

* **polyregular for both ties:** `(1,1)`, `(-1,-1)`, `(1,2)`,
  `(-1,-2)`, `(2,1)`, `(-2,-1)`, `(1,0)`, `(-1,0)`, `(0,1)`,
  `(0,-1)`;
* **non-polyregular for both ties:** `(1,-1)`, `(-1,1)`, `(1,-2)`,
  `(-1,2)`, `(2,-1)`, `(-2,1)`.

These are exactly the 32 labeled triples in `problem.md`.  The positive note
gives explicit one-copy MSO transductions, and the present note gives a
regular-slice pumping obstruction for every negative representative.
