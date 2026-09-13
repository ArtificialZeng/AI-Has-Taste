# Formal statement

## Ambient Coxeter system and conventions

For every integer \(n\ge 2\), let \(S_n\) be the symmetric group written in
one-line notation.  Products act on the right: \(ws_i\) is obtained from the
one-line word for \(w\) by interchanging the entries in positions \(i\) and
\(i+1\).  The identity is \(e=12\cdots n\), the simple reflections are
\(s_i=(i,i+1)\), and \(\ell(w)\) is the inversion number.

The (strong) Bruhat order is fixed by either of the equivalent conditions

1. a reduced word of \(u\) is a subword of a reduced word of \(v\); or
2. for every \(1\le p,r\le n\),
   \[
   \#\{i\le p:u(i)\le r\}\ge \#\{i\le p:v(i)\le r\}.
   \]

Set
\[
v_n=[3,4,\ldots,n,1,2].
\]
For \(n=2\), this means \(v_2=e=[1,2]\).  For \(n\ge3\), a fixed reduced
word is
\[
\Omega_n=s_2s_1s_3s_2\cdots s_{n-1}s_{n-2},
\qquad \ell(v_n)=2n-4.
\]
The symbol \(\Omega_n\) denotes this word, while \(v_n\) denotes its group
element; the original paper occasionally uses them interchangeably in an
order relation.

## Exact normalization of \(\widetilde R\)

For all \(u,v\in S_n\), set \(\widetilde R_{u,v}(q)=0\) if \(u\not\le v\)
and \(\widetilde R_{u,u}(q)=1\).  If \(u<v\) and
\(s\in D_R(v)=\{s_i:\ell(vs_i)<\ell(v)\}\), define recursively
\[
\widetilde R_{u,v}(q)=
\begin{cases}
\widetilde R_{us,vs}(q),&s\in D_R(u),\\
\widetilde R_{us,vs}(q)+q\widetilde R_{u,vs}(q),&s\notin D_R(u).
\end{cases}
\]
All coefficient arithmetic is in \(\mathbb Z[q]\).  For \(u\le v\), put
\(d(u,v)=\ell(v)-\ell(u)\).  The recurrence implies that
\(\widetilde R_{u,v}\) is monic of degree \(d(u,v)\) and only has powers
congruent to \(d(u,v)\pmod 2\).  Thus there is a unique
\(B_{u,v}(x)\in\mathbb Z[x]\) such that
\[
\widetilde R_{u,v}(q)=q^{d(u,v)}B_{u,v}(q^{-2}).
\]

## The allowed \(q\)-Fibonacci family

Define
\[
F_0(x)=F_1(x)=1,\qquad
F_h(x)=F_{h-1}(x)+xF_{h-2}(x)\quad(h\ge2).
\]
Factors \(F_0\) and \(F_1\) are units and carry no information.  We therefore
use the canonical convention that all displayed nonunit indices satisfy
\(h_i\ge2\), and allow the empty product to equal \(1\).

## Conjecture and finite \(n=10\) endpoint

The corrected quantified conjecture is:

> For every \(n\ge2\) and every \(u,v\in S_n\) with
> \(e\le u\le v\le v_n\), there exist \(k\ge0\) and integers
> \(h_1,\ldots,h_k\ge2\) such that
> \[
> \widetilde R_{u,v}(q)
> =q^{d(u,v)}\prod_{i=1}^kF_{h_i}(q^{-2}).
> \]

The exponent called \(g(u,v)\) in the source is not free: comparison of the
leading term forces \(g(u,v)=d(u,v)\).  Equivalently,
\[
B_{u,v}(x)\in\langle F_2(x),F_3(x),\ldots\rangle_{\rm mult}.
\]

The finite endpoint investigated here is the universal statement above with
\(n=10\).  A **certified finite result** must enumerate the complete lower
interval \([e,v_{10}]\), every comparable ordered pair \((u,v)\) inside it,
reconstruct \(\widetilde R_{u,v}\) by exact recurrence, and certify the stated
multiplicative-monoid membership for every pair.  A **disproof** needs only
one exact comparable pair for which membership fails.

## Edge and degenerate cases

- If \(u=v\), then \(d=0\), \(\widetilde R=1\), and the empty product is used.
- The case \(n=2\) consists only of \((e,e)\).
- Incomparable pairs are outside the conjecture and have
  \(\widetilde R_{u,v}=0\) only by the recurrence convention.
- “Remove the maximum \(q\)-power” is interpreted as factoring the unique
  top-degree term \(q^{d(u,v)}\) and changing variables to \(x=q^{-2}\), not
  as removing the largest common monomial divisor at the low-degree end.
- Exact polynomial equality, not numerical evaluation, modular coincidence,
  or a factorization over floating point, is required.
