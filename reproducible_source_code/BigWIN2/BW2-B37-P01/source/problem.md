# Precise problem: even periods for the RESOCA 115 family

## Frozen source claim

The immutable statement in `source.md` asks for a proof or disproof of
Formenti--Kamilya, Conjecture 3:

\[
P(2i)=\frac{2\,4^{2i+2}-7\,4^{i+1}+5}{3}
\qquad\text{for every integer }i\ge 0.
\]

An alleged counterexample qualifies only if its **least** positive period is
established.

## Definitions and quantifiers

Let \(A=\{0,1\}\), let \(X=A^{\mathbb Z}\), and write \(\oplus\) for addition
modulo 2.  Wolfram rule 115 is the radius-one map
\(\delta_{115}:A^3\to A\) whose outputs, for neighborhoods
\(111,110,101,100,011,010,001,000\), are respectively
\(0,1,1,1,0,0,1,1\).

The global RESOCA 115 map \(F:X^2\to X^2\) is

\[
F(b,c)=(c,d),\qquad
d_j=b_j\oplus\delta_{115}(c_{j-1},c_j,c_{j+1})
\quad(j\in\mathbb Z).
\]

Here the first component is the memory configuration and the second is the
current configuration.  Let \(u\in X\) be the singleton configuration
\(u_0=1\), \(u_j=0\) for \(j\ne0\).

For each integer \(k\ge0\), let \(w^{(k)}=1(01)^k\), a word of length
\(2k+1\), indexed from 0 through \(2k\).  Define the centered finite
configuration \(c^{(k)}\in X\) by

\[
c^{(k)}_{-k+j}=w^{(k)}_j\quad(0\le j\le2k),
\qquad c^{(k)}_r=0\quad(r\notin[-k,k]).
\]

Equivalently, its 1-sites are \(-k,-k+2,\ldots,k\).  Define

\[
P(k)=\min\{p\in\mathbb Z_{>0}:F^p(u,c^{(k)})=(u,c^{(k)})\}.
\]

Existence of this minimum follows from Theorem 1 of the cited paper.  Thus the
problem quantifies over every \(i\in\mathbb Z_{\ge0}\), uses family parameter
\(k=2i\), and asserts equality with the least period, not merely a return time.
For \(i=0\), the current word is `1` and the displayed formula asserts
\(P(0)=3\).

## Source convention note

Section 6 says to set \(c_{-k+i}=w_i\) for \(i\in[0,|w|]\), while also saying
that \(w\) has length \(|w|\).  Read literally with zero-based word indices,
the upper endpoint asks for the undefined symbol \(w_{|w|}\).  The reading
above records the evident endpoint correction \(0\le i<|w|\), centers the
entire odd word as the section requires, and does not alter the family or the
conjecture.  The paper also motivates the even formula from a base-4 pattern
reported for \(i>2\), but Conjecture 3 itself uses \(i\in\mathbb N\); the
project's frozen quantifier is explicitly every integer \(i\ge0\).

## Prior-result and status triage

Nearest prior result: Enrico Formenti and Supreeti Kamilya, *The Curious Case
of Reversible Elementary Second Order Cellular Automaton 115*, EPTCS 445
(2026), pp. 95--103, DOI
<https://doi.org/10.4204/EPTCS.445.12>, arXiv v1
<https://arxiv.org/abs/2606.13159> (submitted 2026-06-11; inspected
2026-09-06).  Its Theorem 1 proves periodicity for every finite initial pair,
Lemma 1 proves that every such least period is a multiple of 3, and Section
6.3 states the displayed formula as Conjecture 3 on p. 102 of the proceedings
(PDF page 8).

Exact-assertion, title, and equivalent-keyword searches on 2026-09-06 found no
separate primary paper proving or disproving Conjecture 3.  This is a bounded
search result, not a priority claim.  Source status is therefore
`open-supported` by the authors' explicit conjecture, subject to later
literature re-check.

## Triage target

Nearest prior result X: existence and divisibility by 3, plus the experimentally
proposed closed formula.  Proposed delta Y: prove the formula for all
\(i\ge0\), including leastness, or give one exact \(i\) whose rigorously
certified least period differs.  Verification route Z: exact finite-defect
evolution relative to the period-3 homogeneous background, followed by a
symbolic recurrence/block decomposition and an independent least-period
argument.  The target is precise, nontrivial, and has a reproducible exact
small-case verifier, so it advances to research.
