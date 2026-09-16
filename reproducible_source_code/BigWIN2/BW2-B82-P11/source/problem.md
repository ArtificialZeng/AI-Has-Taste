# Precise reading of the frozen problem

## Frozen target and scope

Let \(T=(t_0<t_1<t_2<t_3<t_4)\in\mathbb R^5\).  The frozen claim is

\[
\forall T\quad
\bigl(\operatorname{rank}_{\mathbb Q}\langle Z_3(T)\rangle_{\mathbb Q}=1
\text{ and the primitive generator has mass }3\bigr)
\Longrightarrow M_3(T)\le 33.
\]

The quantifier is over every strictly increasing real five-tuple satisfying
the displayed hypotheses.  An equality classification is optional and is
not part of the claim.  A disproof must exhibit a qualifying \(T\) (or its
exact zero profile) and prove \(M_3(T)\ge34\); failure to find a model is not a
disproof.

## Definitions

For \(a=(a_0,\ldots,a_4)\in\mathbb Z^5\):

- \(a\) is **balanced** when \(\sum_{i=0}^4a_i=0\).
- Its **mass** is
  \[
  m(a)=\sum_i\max(a_i,0)=\sum_i\max(-a_i,0)=\tfrac12\sum_i|a_i|.
  \]
- The mass-at-most-three zero profile is
  \[
  Z_3(T)=\{a\in\mathbb Z^5:\textstyle\sum_i a_i=0,
             \ m(a)\le3,\ \sum_i a_it_i=0\}.
  \]
  It records exactly the equalities between two equal-length sums of at most
  three letters, with repetitions allowed.

Write \(V_3(T)=\operatorname{span}_{\mathbb Q}Z_3(T)\).  Its rank means
\(\dim_{\mathbb Q}V_3(T)\).  If this dimension is one, the rank-one lattice
\(V_3(T)\cap\mathbb Z^5\) has a generator \(\delta\), unique up to sign, whose
coordinate gcd is one; this is the **primitive balanced generator**.  Under
the mass-three hypothesis, \(m(\delta)=3\) and in fact
\(Z_3(T)=\{0,\delta,-\delta\}\): any other integral vector on the line is an
integer multiple of \(\delta\), and a nontrivial multiple has mass at least
six.

An **order-preserving integer 3-model** of \(T\) is a strictly increasing
integer tuple \(S=(s_0<\cdots<s_4)\) such that, for every balanced
\(a\in\mathbb Z^5\) with \(m(a)\le3\),

\[
                         a\cdot T=0\quad\Longleftrightarrow\quad a\cdot S=0.
\]

Only equality/non-equality is preserved; the signs and relative order of
unequal three-term sums need not be preserved.  Its diameter is \(s_4-s_0\),
and \(M_3(T)\) is the minimum such diameter.  Translation permits \(s_0=0\),
and division by the coordinate gcd shows a minimum model may be taken
primitive.

## Why the numerical maximum would be 33

For rationally independent \(1,\theta,\eta\), with
\(0<\theta<\eta<1\), the cluster alphabet

\[
T_{\rm cl}=(0,2,2+\theta,2+\eta,3)
\]

has primitive relation \((1,-3,0,0,2)\), of mass three, and the inspected
source proves \(M_3(T_{\rm cl})=3L_4(3)=33\), where \(L_4(3)=11\).  It gives
the model \(\{0,22,23,29,33\}\).  Thus the frozen upper bound, if proved,
would make the maximum exactly 33.

## Nearest prior result and proposed delta

Zhang, Proposition 6.5, proves the general rank-one estimate
\(M_q(T)\le\mu q(q+1)\); at \((q,\mu)=(3,3)\) this is only \(M_3(T)\le36\).
Remark 10.1 covers only \(\mu\le\lfloor q/2\rfloor+1=2\) at \(q=3\), while
Corollary 9.2 supplies the lower value 33 and Question 12.3 explicitly leaves
the high-mass profiles open.  The proposed delta is therefore to close the
three-unit gap \(36\to33\) for every feasible primitive mass-three direction.

The bounded verification route is finite and exact.  Enumerate every
primitive balanced \(\delta\in\mathbb Z^5\) of mass three, modulo sign (and
optionally reflection).  If \(g_j=t_j-t_{j-1}>0\) and
\(A_j=\sum_{i=j}^4\delta_i\), then
\(\delta\cdot T=\sum_{j=1}^4A_jg_j\); hence the direction is feasible exactly
when the tail sums have both signs.  For every feasible direction, search
all \(0=s_0<s_1<\cdots<s_4\le33\) and certify directly that
\(Z_3(S)=\{0,\pm\delta\}\).  Completeness of both finite enumerations must be
replayable.  Any failure at diameter 33 should be extended through the known
ceiling 36 before deciding whether it is a counterexample lead.  The cluster
lower bound remains a separate exact obligation.

## Interpretation notes

No truth-affecting ambiguity was found.  The frozen source gives the paper
title as *Sharp Ordered Integer Models for Short Additive Equalities*; the
live arXiv v1 title is *Sharp order-preserving integer models for short
additive equalities*.  This is a bibliographic correction only and does not
alter the frozen question.
