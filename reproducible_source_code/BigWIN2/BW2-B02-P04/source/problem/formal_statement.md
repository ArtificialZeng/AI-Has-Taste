# Locked formal statement

Status: **target statement locked for certification** on 2026-08-29. Any
later change to the theorem below must be recorded as a new version rather
than made silently.

## Definitions and quantifiers

Let \(V=[7]=\{1,\ldots,7\}\), \(N=\binom72=21\), and order the edges of
\(K_7\) as

\[
(1,2),(1,3),\ldots,(1,7),(2,3),\ldots,(6,7).
\]

For \(1\le i<j\le7\), put

\[
\operatorname{idx}(i,j)=7(i-1)-\binom{i}{2}+(j-i)\in\{1,\ldots,21\}.
\]

For every real \(r\) with \(1<r<2\), the edge \((i,j)\) has weight
\(r^{21-\operatorname{idx}(i,j)}\). A cut is an unordered bipartition
\(S\mid(V\setminus S)\). To enumerate each cut once, use its unique
representative satisfying \(1\in S\); there are \(2^6=64\) such
representatives. Define

\[
W_S(r)=\sum_{\substack{1\le i<j\le7\\ |S\cap\{i,j\}|=1}}
r^{21-\operatorname{idx}(i,j)}.
\]

Thus complements define the same cut and have the same weight. Empty
crossing sets (in particular \(S=V\)) have weight zero. Let

\[
C_k=\{1,\ldots,k\}\mid\{k+1,\ldots,7\},\qquad k=1,2,3.
\]

Let \(\alpha\) and \(\beta\) be the unique positive roots, respectively, of

\[
q_2(x)=x^{13}+x^8-x^3-x^2-x-1,
\qquad
q_1(x)=x^{10}-x^4-x^3-x^2-x-1.
\]

Equivalently, \(\alpha=r_2(7)\) is the equality point of \(C_2,C_3\),
because

\[
W_{C_2}-W_{C_3}=x^6q_2(x),
\]

and \(\beta=r_1(7)\) is the equality point of \(C_1,C_2\), because

\[
W_{C_1}-W_{C_2}=x^{10}q_1(x).
\]

The intended exact isolations are

\[
\frac{539}{500}<\alpha<\frac{1079}{1000}
 <\frac{1229}{1000}<\beta<\frac{123}{100},
\]

to be proved, not assumed numerically.

## Theorem to prove (the \(n=7\) case of Conjecture 5.1)

For every real \(r\in(1,2)\) and every cut \(S\mid(V\setminus S)\),

\[
W_S(r)\le
\begin{cases}
W_{C_3}(r),&1<r\le\alpha,\\
W_{C_2}(r),&\alpha\le r\le\beta,\\
W_{C_1}(r),&\beta\le r<2.
\end{cases}
\]

The overlap at a threshold is intentional. Equality is to be classified:
up to complementation, the only maximizer is \(C_3\) on \((1,\alpha)\),
both \(C_3,C_2\) maximize at \(\alpha\), only \(C_2\) maximizes on
\((\alpha,\beta)\), both \(C_2,C_1\) maximize at \(\beta\), and only
\(C_1\) maximizes on \((\beta,2)\).

This endpoint formulation is a continuous closure of the open threshold
intervals in Conjecture 5.1; it does not add \(r=1\) or \(r=2\) to the
requested parameter domain.

## Corrections and clarifications relative to the source statement

1. The exponent in \(W_S\) is fixed explicitly as
   \(21-\operatorname{idx}(i,j)\); the source's shorthand \(r^j\) is
   otherwise ambiguous.
2. The cited paper reports exhaustive enumeration of all cuts for
   \(n\le21\) on the mesh \(0.001\), *and additionally* targeted
   near-isolated checks for \(n\le100\). Neither is a continuum proof.
3. Cuts are unordered bipartitions. The convention \(1\in S\) removes
   complement duplication and makes “only maximizer” precise.
