# Precise problem statement

## Objects and conventions

Let

\[
A=\mathbb Z/5\mathbb Z=\{0,1,2,3,4\},
\qquad b=01213101314310.
\]

All displayed letters are their residues modulo $5$.  Define the monoid
morphism $h:A^*\to A^*$ by

\[
h(r)_j=b_j+r\pmod 5\quad (r\in A,\ 0\le j<14).
\]

Thus every image has length $14$.  Since $h(0)$ begins with $0$, the
words $h^k(0)$ are nested prefixes.  Their one-sided limit

\[
w=h^\omega(0)=w_0w_1w_2\cdots
\]

is therefore well-defined and satisfies $h(w)=w$.  Positions are indexed
from $0$.

For a finite word $u\in A^*$, define its Parikh vector (with coordinates in
the fixed order $0,1,2,3,4$) by

\[
\Psi(u)=(|u|_0,|u|_1,|u|_2,|u|_3,|u|_4)\in\mathbb N^5.
\]

Division of a Parikh vector by a positive word length is coordinatewise in
\(\mathbb Q^5\).

## Frozen quantified claim

The question is whether the following universal statement is true:

\[
\tag{C}
\forall s\in\mathbb N_0\;\forall m,n\in\mathbb N_{>0},\qquad
 n\,\Psi(w_s\cdots w_{s+m-1})
 \ne
 m\,\Psi(w_{s+m}\cdots w_{s+m+n-1}).
\]

Equivalently, for the two blocks in this occurrence

\[
x=w_s\cdots w_{s+m-1},\qquad
y=w_{s+m}\cdots w_{s+m+n-1},
\]

claim (C) says

\[
\frac{\Psi(x)}{m}\ne\frac{\Psi(y)}{n}.
\]

The blocks must be consecutive in one occurrence of $w$, but their positive
lengths $m$ and $n$ are arbitrary and need not be equal.  The displayed
frequency condition is controlling if terminology for “weak abelian square”
varies elsewhere.

## Walk formulation

Let $e_0,\ldots,e_4$ be the standard basis of $\mathbb R^5$, and set

\[
S_0=0,\qquad S_t=\sum_{i=0}^{t-1}e_{w_i}\quad(t\ge1).
\]

For $0\le p<q<r$,

\[
S_q-S_p=\Psi(w_p\cdots w_{q-1}),\qquad
S_r-S_q=\Psi(w_q\cdots w_{r-1}).
\]

Because the coordinate sum of $S_t$ is $t$, all vertices are distinct and
these three vertices are collinear exactly when

\[
(r-q)(S_q-S_p)=(q-p)(S_r-S_q).
\]

Consequently, (C) is exactly the assertion that no three vertices of this
one-sided walk are collinear.

## Scope and resolution standard

Only the particular morphism, seed $0$, and one-sided fixed point above are
in scope.  No assertion is made about other seeds, shifts, morphisms, or
alphabet sizes.  Testing a finite prefix can disprove (C), but cannot prove it.
A disproof requires exact $s,m,n$, the two blocks (or a reproducibly bound
prefix), and their Parikh vectors.  A proof must cover every $s\ge0$ and all
$m,n\ge1$, including every alignment relative to substitution blocks.

## Triage target and source status

The immutable source identifies Shallit, *Avoiding Three Collinear Points in a
Unit-Step Lattice Walk*, arXiv:2609.05780v1, Proposition 1, Theorem 5, and
Section 5 (PDF pp. 2 and 6--8) as the nearest prior result: it reports a
proved construction on $16$ letters and presents the morphism above as an
unproved proposed five-letter construction.  The proposed delta is an exact
proof or counterexample for (C).  On this triage pass the original claim
remains unresolved and its current literature status remains
`status-uncertain`; neither the source description nor a finite computation is
a proof of open status.
