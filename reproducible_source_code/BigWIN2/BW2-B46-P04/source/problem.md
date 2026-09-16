# Precise problem statement

## Frozen claim to be determined

Let
\[
\mathcal P(44)=\{(\nu_1,\ldots,\nu_r):r\geq 1,
\nu_1\geq\cdots\geq\nu_r\geq1,\ \sum_i\nu_i=44\}
\]
be the set of integer partitions of 44.  For each \(\lambda\in
\mathcal P(44)\), let \(\chi^\lambda\) be the ordinary irreducible complex
character of the symmetric group \(S_{44}\) afforded by the Specht module
indexed by \(\lambda\).  For \(\mu\in\mathcal P(44)\), \(\chi^\lambda(\mu)\)
means the (integer) value of this character on the conjugacy class whose cycle
length multiset is \(\mu\).

Determine, with no omitted partitions,
\[
ZF(44)=\{\mu\in\mathcal P(44):
          \forall\lambda\in\mathcal P(44),\ \chi^\lambda(\mu)\neq0\},
\qquad D(44)=|ZF(44)|.
\]
Thus a column is a survivor only after the universal quantifier over all
\(\lambda\vdash44\) has been checked.  To exclude a column it suffices to give
one explicit \(\lambda\vdash44\) with exact value zero.  Notation such as
\((3^a,2^b,1^c)\) denotes multiplicities, and requires
\(a,b,c\in\mathbb Z_{\geq0}\) and \(3a+2b+c=44\).

## Exact preliminary reduction

The cited primary paper proves for \(n\geq3\) that a zero-free cycle type must
have the form \((3^a,2^b,1^c)\) with \(b\) even (Proposition 3.1).  It defines
\[
s_2(n)=\min\{s\geq0:n-2s=u(u+1)/2\text{ for some }u\geq0\}
\]
and
\[
s_3(n)=\min\{s\geq0:n-3s\geq0\text{ and a 3-core partition of }
n-3s\text{ exists}\},
\]
and proves that zero-freeness implies \(b\leq s_2(n)\) and
\(a\leq s_3(n)\) (Corollaries 4.1 and 4.2).

For \(n=44\), \(s_2(44)=4\): none of \(44,42,40,38\) is triangular, while
\(44-2\cdot4=36=8\cdot9/2\).  Also \(s_3(44)=0\): the paper's 3-core
criterion says a 3-core of size \(m\) exists exactly when \(3m+1\) is of the
form \(x^2+xy+y^2\), and
\[
3\cdot44+1=133=9^2+9\cdot4+4^2.
\]
Consequently every member of \(ZF(44)\) lies in the exact three-element set
\[
\mathcal C_{44}=\{(1^{44}),\ (2^2,1^{40}),\ (2^4,1^{36})\}.
\]
The identity type \((1^{44})\) is certainly zero-free because
\(\chi^\lambda(1^{44})=\dim S^\lambda>0\).  The unresolved finite task is
therefore to classify the other two members of \(\mathcal C_{44}\).

## Scope and completion standard

The requested output is the exact finite layer at \(n=44\), not a claim about
the asymptotic conjecture for \(D(n)\).  A complete resolution must:

1. justify exhaustiveness of \(\mathcal C_{44}\);
2. give an exact zero witness \(\lambda\) for each rejected member of
   \(\mathcal C_{44}\);
3. check \(\chi^\lambda(\mu)\neq0\) for every \(\lambda\vdash44\) for each
   claimed survivor; and
4. independently verify the decisive computation, as well as reproduce the
   paper's published values through \(n=43\).

Floating-point calculations, a timeout, or output from a single unaudited
implementation do not meet this standard.

## Nearest prior result and proposed delta

Nearest prior result: Defant--Hariharan--Lau--Ono,
*Zero-free columns in the character tables of symmetric groups*,
[arXiv:2608.27718v1](https://arxiv.org/abs/2608.27718), submitted 2026-08-27.
Definition (3) gives \(D(n)\); Proposition 3.1 and Corollaries 4.1--4.2 give
the reduction above; Section 8.2 and Table 1 report a beta-number
Murnaghan--Nakayama computation only for \(1\leq n\leq43\), with \(D(43)=7\).
The PDF and arXiv metadata were inspected on 2026-09-06.  Exact web searches
for \(D(44)\), \(ZF(44)\), and the paper title with 44 found no primary source
answer; this limited negative search does not establish priority or open
status.

Proposed delta: compute and certify the exact set \(ZF(44)\) and its cardinality.
Verification route: exact memoized Murnaghan--Nakayama recurrence with
beta-number rim-hook enumeration, followed by a structurally independent
small verifier or comparison with a standard character-table system.  GAP and
Sage were not installed in the triage environment, so that comparison may
require a later environment or an independent local implementation.
