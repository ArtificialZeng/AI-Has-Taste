# Precise problem reading

## Objects and definitions

For \(r,q,t\in\mathbb R_{>0}\), let

\[
P(r,q,t)=
\begin{pmatrix}
1&r&q&q&r&t&t\\
r&1&r&q&q&t&t\\
q&r&1&r&q&t&t\\
q&q&r&1&r&t&t\\
r&q&q&r&1&t&t\\
t&t&t&t&t&1&1\\
t&t&t&t&t&1&1
\end{pmatrix}.
\]

Here a **Lorentzian matrix** means a real symmetric matrix with nonnegative
entries and at most one positive eigenvalue, counted with multiplicity.  This
definition allows zero eigenvalues; in particular, the identical sixth and
seventh rows do not exclude this family.  Since all entries of \(P(r,q,t)\)
are positive, every such matrix has at least one positive eigenvalue, so on
this family “at most one” is equivalent to “exactly one.”

The reduced exponent vector is indexed by the \(21\) off-diagonal variables
\(x_{ij}\), \(1\le i<j\le7\).  Put

\[
z=x_{13}+x_{14}+x_{24}+x_{25}+x_{35}+x_{67}
  -\sum_{i=1}^{5}(x_{i6}+x_{i7}),\qquad \alpha=z/4.
\]

Thus \(\alpha_{ij}=1/4\) on the six displayed positive terms,
\(\alpha_{ij}=-1/4\) on the ten terms in the sum, and it is zero elsewhere.
Its coordinate sum is \((6-10)/4=-1\).  For a positive normalized matrix
\(P=(p_{ij})\),

\[
P^\alpha:=\prod_{1\le i<j\le7}p_{ij}^{\alpha_{ij}},
\]

and direct substitution on this family gives

\[
P(r,q,t)^\alpha=\left(\frac{q^5}{t^{10}}\right)^{1/4}
=\left(\frac q{t^2}\right)^{5/4}.
\]

## Feasible set and quantified task

Use the following exact characterization, whose equality cases are included:

\[
P(r,q,t)\text{ is Lorentzian}
\quad\Longleftrightarrow\quad
r+q-2\ge\sqrt5\,|r-q|,
\qquad
t^2\ge\frac{1+2r+2q}{5}.
\]

Accordingly, define

\[
\mathcal D=\left\{(r,q,t)\in\mathbb R_{>0}^3:
r+q-2\ge\sqrt5|r-q|,
t^2\ge\frac{1+2r+2q}{5}\right\}
\]

and the family constant

\[
C_{\rm fam}:=\sup_{(r,q,t)\in\mathcal D}
\left(\frac q{t^2}\right)^{5/4}.
\]

The task is to:

1. determine \(C_{\rm fam}\) exactly;
2. decide whether there exists a finite \((r,q,t)\in\mathcal D\) whose value
   equals \(C_{\rm fam}\); and
3. if not, give explicit exact sequences \((r_n,q_n,t_n)\in\mathcal D\) and
   prove their objective values converge to \(C_{\rm fam}\).

All three parameters remain strictly positive, while equality in either
Lorentzian inequality is permitted.  The diagonal normalization is fixed at
one.  The quantifier ranges only over this displayed three-parameter family;
no equality or upper bound involving the global bounded-ratio constant
\(f(\alpha)\) is part of the claim.

## Prior result and proposed delta

Baldi and Kummer, *A note on bounded ratios*, arXiv:2609.03934v1 (submitted
2026-09-03), equations (1)--(3) and Lemma 3.2, give the exponent, objective,
and feasibility characterization above.  They exhibit
\((r,q,t)=(284,701,20)\), with value
\((701/400)^{5/4}\approx2.01638>2\), but do not state a sharp optimization of
this family.  Primary source inspected 2026-09-07:
https://arxiv.org/html/2609.03934v1 (Section 3, especially Lemma 3.2).

Nearest prior result \(X\): that characterization and explicit witness.
Proposed delta \(Y\): the sharp family constant, attainment classification,
and exact extremal sequence.  Verification route \(Z\): eliminate \(t\) by
monotonicity, minimize admissible \(r\) for each \(q\) in the branches
\(r\le q\) and \(r\ge q\), and certify the resulting one-variable monotonicity
and limiting sequence exactly.

## Resolution submitted for independent audit

**Theorem.**  On the frozen three-parameter family,

\[
C_{\rm fam}=\left(\frac{5+\sqrt5}{4}\right)^{5/4}.
\]

No finite feasible triple attains this value.  For every integer \(n\ge1\),
the exact sequence

\[
q_n=n,\qquad
r_n=\frac{(\sqrt5-1)+(3-\sqrt5)n}{2},\qquad
t_n=\sqrt{\frac{\sqrt5+(5-\sqrt5)n}{5}}
\]

is feasible and its objective values converge to \(C_{\rm fam}\).

**Independent check of the feasibility characterization.**  Let
\(U=\langle e_6-e_7\rangle\), let \(V\) be spanned by
\(u=e_6+e_7\) and \(v=e_1+\cdots+e_5\), and let \(W\) be the subspace of
vectors supported on the first five coordinates whose coordinates sum to
zero.  These three spaces form a direct sum and are mutually orthogonal for
the bilinear form represented by \(P\).  The restriction to \(U\) is zero,
while the Gram matrix on \(V\), in the basis \((u,v)\), is

\[
\begin{pmatrix}4&10t\\10t&5+10r+10q\end{pmatrix}.
\]

It has one positive direction and at most one positive eigenvalue exactly
when its determinant is nonpositive, namely when
\(t^2\ge(1+2r+2q)/5\).  On \(W\), the two eigenvalues (each with multiplicity
two) are

\[
1-\frac{r+q}{2}\mathbin{\pm}\frac{\sqrt5}{2}(r-q).
\]

Their maximum is nonpositive exactly when
\(r+q-2\ge\sqrt5\lvert r-q\rvert\).  Since the restriction on \(V\) always
has a positive direction, this proves the stated characterization, including
all equality cases.

**Proof of the sharp bound.**  Put \(s=\sqrt5\).  The positive power
\(x\mapsto x^{5/4}\) is strictly increasing.  For every fixed feasible
\((r,q)\), the largest possible base \(q/t^2\) therefore occurs at

\[
t^2=\frac{1+2r+2q}{5},
\qquad
\frac q{t^2}=\frac{5q}{1+2r+2q}.
\]

It remains to minimize feasible \(r\) for a fixed \(q\).  There are two
branches.

If \(r\le q\), the first feasibility inequality is equivalent to

\[
r\ge a(q):=\frac{(s-1)q+2}{s+1}
=\frac{(3-s)q+(s-1)}2.
\]

The interval \(a(q)\le r\le q\) is nonempty exactly when \(q\ge1\).  Hence

\[
\frac q{t^2}\le
\frac{5q}{1+2a(q)+2q}
=\frac{5q}{s+(5-s)q}
<\frac5{5-s}.
\]

The last inequality is strict for every finite \(q>0\), because the
denominator on its left has the additional positive term \(s\).

If \(r\ge q\), feasibility is equivalent to

\[
(s-1)r\le(s+1)q-2.
\]

Together with \(r\ge q\), this again forces \(q\ge1\).  The objective base
decreases as \(r\) increases, so throughout this branch

\[
\frac q{t^2}\le\frac{5q}{1+4q}<\frac5{5-s};
\]

the strict inequality follows from \((5-s)q<1+4q\).  Thus every finite
feasible triple satisfies

\[
P(r,q,t)^\alpha
<\left(\frac5{5-s}\right)^{5/4}
=\left(\frac{5+s}{4}\right)^{5/4},
\]

where the last identity follows by rationalizing the denominator.  This also
proves nonattainment.

It remains to prove sharpness.  For the displayed sequence, \(q_n\ge r_n>0\)
and

\[
q_n-r_n=\frac{(s-1)(n-1)}2,
\qquad
r_n+q_n-2=\frac{(5-s)(n-1)}2
=s(q_n-r_n).
\]

Also \(t_n>0\) and direct substitution gives

\[
t_n^2=\frac{1+2r_n+2q_n}{5}.
\]

Both feasibility inequalities therefore hold with equality.  Finally,

\[
P(r_n,q_n,t_n)^\alpha
=\left(\frac{5n}{s+(5-s)n}\right)^{5/4}
\longrightarrow
\left(\frac5{5-s}\right)^{5/4}
=\left(\frac{5+s}{4}\right)^{5/4}.
\]

This supplies the matching lower bound and completes the resolution of the
frozen family problem.  It does not assert equality with the global constant
\(f(\alpha)\).
