# Precise reading and triage

## Frozen statement

Let \(c\phi_{18}(N)\) be Andrews's 18-colored generalized Frobenius
partition function.  The frozen claim is the conjunction
\[
\begin{aligned}
&\forall n\in\mathbb Z_{\ge 0},\qquad
  c\phi_{18}(30n+19)\equiv0\pmod {16},\\
&\forall n\in\mathbb Z_{\ge 0},\qquad
  c\phi_{18}(30n+25)\equiv0\pmod {16}.
\end{aligned}
\]
Thus the variables in the conjecture are integers, both universal quantifiers
start at \(n=0\), and divisibility is in \(\mathbb Z\).  The first terms tested
by the assertions are therefore \(c\phi_{18}(19)\) and
\(c\phi_{18}(25)\).  Both progressions must be proved for a full proof.  One
exact failure in either progression disproves the conjunction; a result about
only one progression is partial and must be labeled as such.

## Exact definition

A combinatorial object has two rows of the same finite length \(r\ge0\), and
weight
\[
N=r+\sum_{j=1}^{r}(a_j+b_j).
\]
The entries come from 18 distinguished copies (colors) of each nonnegative
integer, and each row is put in Andrews's fixed size-then-color order with no
repetition of an identical colored entry in that row.  The empty array gives
\(c\phi_{18}(0)=1\).  The color names and their fixed order do not affect the
count.

For computation, and to remove any remaining ambiguity about the colored
ordering, the operative equivalent definition is the exact formal generating
series
\[
C\Phi_{18}(q):=\sum_{N\ge0}c\phi_{18}(N)q^N
=\frac{1}{(q;q)_\infty^{18}}
 \sum_{(m_1,\ldots,m_{17})\in\mathbb Z^{17}}q^{Q(m_1,\ldots,m_{17})},
\]
where
\[
(q;q)_\infty=\prod_{j\ge1}(1-q^j),\qquad
Q(m)=\sum_{i=1}^{17}m_i^2+
      \sum_{1\le i<j\le17}m_i m_j.
\]
This is interpreted in \(\mathbb Z[[q]]\), and \(c\phi_{18}(N)=[q^N]
C\Phi_{18}(q)\).  It is Andrews's cited generating function, not the
generating function for ordinary partitions or a free choice of coloring
convention.

## Scope and boundary audit

- The two exponent classes are \(19,25\pmod {30}\); both are \(1\pmod6\)
  and \(1\pmod3\).
- There are no negative arguments because \(n\ge0\).
- No normalization or division by another partition function is implicit.
- Finite coefficient agreement is evidence, not a proof of either universal
  assertion, unless accompanied by a theorem giving a valid finite bound.
- A computational disproof must use exact integer or modulo-16 arithmetic and
  independently reproduce the source-compatible coefficient sequence; the
  least failing \(n\) should be supplied when feasible.

## Source status and nearest prior results

The primary source is H. Das, H. Nath, and A. Sarma, *Proof of a Conjecture of
Cui, Gu and Tang on 18-Colored Generalized Frobenius Partitions*,
arXiv:2609.05302v1 (submitted 2026-09-04), Conjecture 5.1 on PDF page 21.
According to the immutable source record, the authors call these two
modulo-16 congruences numerically observed and leave their proofs open.  The
arXiv abstract and metadata were inspected on 2026-09-07 at
<https://arxiv.org/abs/2609.05302>; they confirm the paper, version, authors,
date, and its proved congruences for \(c\phi_{18}\) modulo 8, 81, and 2187.
Exact-assertion searches on 2026-09-07 found no separate primary paper settling
the two modulo-16 progressions; because this v1 is only three days old and the
full conjecture text was not independently retrieved during this bounded
triage, this is an `open-supported` lead rather than a priority claim.

The nearest recorded theorems in that paper are
\(c\phi_{18}(3n+1)\equiv0\pmod{81}\),
\(c\phi_{18}(3n+2)\equiv0\pmod{2187}\), and the separately recorded
\(c\phi_{18}(6n+5)\equiv0\pmod8\).  The first covers the same two classes
modulo 3 but concerns an odd modulus.  Importantly, \(30n+19\) and
\(30n+25\) are \(1\pmod6\), not \(5\pmod6\); hence the recorded
\(6n+5\pmod8\) theorem does **not** supply modulus 8 on these classes.  The
claim in `source.md` that the proposed delta is merely an "additional factor
of 2" over that theorem is arithmetically inconsistent and must be checked
against the primary PDF before any proof strategy relies on it.  This issue
does not make the frozen modulo-16 assertions themselves ambiguous.

## Triage target

Nearest prior result: the paper's exact generating series and its proved
congruences above.  Proposed delta: prove both specified modulo-16
progressions, or produce an exact least counterexample in either.  Verification
route: first independently confirm Conjecture 5.1 and Theorem 1.2 in the v1
PDF, then implement the displayed lattice-theta/product series exactly modulo
16 and compare it with an independent constant-term implementation over a
substantial prefix.  This is a precise, nontrivial target with a cheap
discriminating first test, so it is suitable to advance to research, with
novelty still subject to a fuller literature check.
