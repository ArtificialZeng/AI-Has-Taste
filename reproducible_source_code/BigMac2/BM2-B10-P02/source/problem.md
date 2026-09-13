# Precise reading of the problem

`source.md` is the immutable, normative statement.  This file fixes its
mathematical reading without changing or weakening it.

## Exact discrete-time model

For each integer \(N\ge 2\), let
\(X^{(t)}=(X_1^{(t)},\ldots,X_N^{(t)})\in\{0,1\}^N\).  Given the state at
integer time \(t\), independently sample

- an updating index \(V_t\) uniformly from \([N]=\{1,\ldots,N\}\), and
- three indices \(J_{t,1},J_{t,2},J_{t,3}\), independently and uniformly
  from \([N]\), independently also of \(V_t\).

All sampling is with replacement: every equality among these four indices is
allowed.  Set
\[
 X_{V_t}^{(t+1)}
 =X_{J_{t,1}}^{(t)}\mathbin{\mathrm{OR}}
   \bigl(X_{J_{t,2}}^{(t)}\mathbin{\mathrm{AND}}X_{J_{t,3}}^{(t)}\bigr),
\]
and leave every other coordinate unchanged.  Thus one unit of time is one
asynchronous update, not one sweep of \(N\) updates and not a continuous-time
unit.

Let
\[
 S_t=\sum_{i=1}^N X_i^{(t)},\qquad
 T_N=\inf\{t\ge0:S_t\in\{0,N\}\}.
\]
For \(0\le s\le N\), write
\[
 u_N(s)=\mathbb E[T_N\mid S_0=s].
\]
The law of \((S_t)\), hence this expectation, is the same for every initial
configuration having exactly \(s\) ones; no distribution on such
configurations is being added.  The notation \(E_s[T_N]\) in `source.md`
means \(u_N(s)\).

## Equivalent exact birth--death chain

If \(p=s/N\) and \(B_1,B_2,B_3\) are independent Bernoulli\((p)\) variables,
then the rule's mean-field polynomial is
\[
 g(p)=\mathbb P\{B_1\lor(B_2\land B_3)=1\}
     =p+(1-p)p^2=p+p^2-p^3.
\]
Consequently, conditional on \(S_t=s\), the only nonzero changes are
\[
\begin{aligned}
 \beta_{N,s}&=\mathbb P(S_{t+1}=s+1\mid S_t=s)
       =(1-p)g(p)=p(1-p)(1+p-p^2),\\
 \delta_{N,s}&=\mathbb P(S_{t+1}=s-1\mid S_t=s)
       =p(1-g(p))=p(1-p)(1-p^2),\\
 \mathbb P(S_{t+1}=s\mid S_t=s)&=1-\beta_{N,s}-\delta_{N,s}.
\end{aligned}
\]
States \(0,N\) are absorbing.  Equivalently, \(u_N\) is the unique solution
of the exact finite Poisson problem
\[
\begin{cases}
 \beta_{N,s}\bigl(u_N(s+1)-u_N(s)\bigr)
 +\delta_{N,s}\bigl(u_N(s-1)-u_N(s)\bigr)=-1,
       &1\le s\le N-1,\\
 u_N(0)=u_N(N)=0.
\end{cases}
\]
This recurrence (or the equivalent Green-function formula) is an exact
finite-\(N\) verifier, not an asymptotic approximation.

## Quantified target

Define the nonempty finite sets and numbers
\[
 M_N=\max_{1\le s<N}u_N(s),\qquad
 A_N=\operatorname*{arg\,max}_{1\le s<N}u_N(s).
\]
The limit is along integer \(N\to\infty\).  The tasks are:

1. Decide whether the finite real limit
   \[
   C_*=\lim_{N\to\infty}\frac{M_N}{N^{3/2}}
   \]
   exists.
2. If it exists, give \(C_*\) exactly as a convergent integral or in standard
   special functions (a decimal fit alone does not answer the question).
3. Determine, allowing for ties at every \(N\), the full subsequential limit
   set
   \[
   \mathcal L=
   \left\{a\in[0,\infty]:
   \begin{array}{l}
   \text{there are }N_k\to\infty\text{ and }s_k\in A_{N_k}\text{ with}\\[-2pt]
   s_k/\sqrt{N_k}\to a
   \end{array}\right\}.
   \]
   Here convergence is understood in the extended half-line; thus the answer
   must also say whether \(+\infty\in\mathcal L\).  The finite part is the
   ordinary real limit set.  In particular, uniqueness of a limiting
   maximizer may not be assumed.

The normalization and maximization are exactly those above.  The question does
not switch to synchronous or without-replacement sampling, does not rescale
time by \(N\), and does not ask merely for the exponent, absorption
probabilities, or a numerical candidate.  Passing a limit through the maximum
requires uniform control and optimizer tightness; pointwise asymptotics alone
are insufficient.

## Nearest prior result and proposed delta

Primary source inspected on 2026-09-07: Elchanan Mossel, *Consensus times for
monotone aggregation dynamics*, arXiv:2609.04468v1,
<https://arxiv.org/abs/2609.04468>.  The inspected local PDF has SHA-256
`97409d22628a2f5693a518d5ee5b17f675693c8d1ccac2e9d36e64e26073225b`,
matching `source.md`.

For this rule, \(D_0=1\), \(D_1=0\), the residual rule is
\(\widetilde f(x_2,x_3)=x_2\land x_3\), and its least minterm has size \(m=2\).
Theorem 1(iii) (PDF p. 2) and Theorem 22 together with Example 25 (PDF
pp. 30--31) therefore give only
\(M_N=\Theta(N^{3/2})\).  Proposition 13 (PDF p. 11) supplies the exact
Green-function formula.  Remark 23 (PDF p. 31) reports finite numerical values
and maximizers, but neither those observations nor the order theorem prove a
sharp limit or the optimizer limit set.

The target delta is therefore a uniform first-order asymptotic with an exact
constant and a complete classification of scaled maximizers.  A bounded
verification route is to specialize Proposition 13 using
\[
 \frac{\delta_{N,s}}{\beta_{N,s}}
 =\frac{1-(s/N)^2}{1+s/N-(s/N)^2},
\]
derive the scaled Green kernel on \(s,j=O(\sqrt N)\), and prove the tail and
uniform bounds needed to exchange scaling, summation, and maximization.  A
limited exact-assertion search on 2026-09-07 found no additional primary source
beyond the Mossel preprint; this is not a priority or novelty claim.  The source
status is best recorded as a newly posed sharp refinement whose broader
literature status remains unverified.
