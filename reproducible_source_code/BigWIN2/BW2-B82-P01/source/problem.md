# Precise problem: decide \(\mathsf E(8,4)\)

## Frozen interpretation

Write \([8]=\{1,\ldots,8\}\), let \(\binom{[8]}4\) be the set of all
four-element subsets of \([8]\), and put
\(N=\lvert\binom{[8]}4\rvert=\binom84=70\).  All time indices and all
additions below are in the cyclic group \(\mathbb Z_{70}=\mathbb Z/70\mathbb Z\).
For \(D\subseteq\mathbb Z_{70}\) and \(s\in\mathbb Z_{70}\),
\(D+s:=\{d+s:d\in D\}\).

The question is the truth value of the following existential statement:

\[
\exists e\;\exists D\;\exists(s_1,\ldots,s_8)\quad
\begin{cases}
e:\mathbb Z_{70}\to\binom{[8]}4\text{ is a bijection},\\
D\subseteq\mathbb Z_{70},\quad |D|=35,\\
s_v\in\mathbb Z_{70}\quad(v\in[8]),\\
\{t\in\mathbb Z_{70}:v\in e(t)\}=D+s_v\quad(v\in[8]).
\end{cases}
\]

The shifts are independently chosen; the definition imposes no ordering on the
vertices, no common step between their shifts, no action of a cyclic group on
the vertices, and no adjacency/Gray-code condition on consecutive values of
\(e\).  The eight shifts are not assumed distinct, although distinctness follows
from bijectivity: for \(u\ne v\), some four-set contains \(u\) but not \(v\), so
the two incidence supports differ.  The cardinality \(|D|=35\) is also forced by
counting, but is retained because it is explicit in the frozen question.

Equivalently, the seventy rows \(1_{e(t)}\in\{0,1\}^8\) must list the entire
weight-four layer exactly once, while the eight length-seventy coordinate
columns are cyclic shifts of one common binary column.

## Scope and source status

The requested output is either a definition-level witness \((e,D,(s_v))\),
checked to list every four-set exactly once, or a proof that no such data exist.
Conjecture 7.1 alone is not an answer.  Complementation does not change this
middle-layer instance.

The primary source is Junyu Zhou, *Cyclic Incidence Orderings of Complete
Graphs and 3-Uniform Hypergraphs*, arXiv:2609.06724v1 (submitted 2026-09-06),
<https://arxiv.org/abs/2609.06724>, inspected 2026-09-09.  Definition 1.1 gives
the definition; Lemma 2.2 gives the shift congruence; Theorems 1.3--1.4 settle
uniformities two and three; Conjecture 7.1 states the general coprimality
prediction and explicitly describes higher uniformities as open.  Thus the
source status at triage is **open-supported**, subject to the usual caveat that
the short current-literature search is not proof of priority.

Nearest prior result: Lemma 2.2 of that source.  Proposed delta: settle the first
uncovered case \((n,k)=(8,4)\).  Verification route: derive the quotient
\(\mathbb Z_{10}\) from Lemma 2.2, exhaust its slice factorizations, reconstruct
their four-element columns, and turn any obstruction into a self-contained
proof (with independent exact enumeration as a check).
