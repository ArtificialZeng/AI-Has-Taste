# Formal statement

## Fixed finite endpoint

Let \(B_9=C_2\wr S_9\) be the group of signed permutations of
\(\{1,\ldots,9\}\), acting on \(\mathbb R^9\), and let

\[
D_9=\{w\in B_9:\text{the window of }w\text{ has an even number of negative entries}\}.
\]

Thus \(|D_9|=2^8 9!=92{,}897{,}280\).  Let \(T\) be the complete set of
reflections of \(D_9\): for every \(1\leq i<j\leq9\), it contains the two
signed transpositions

\[
(i\ j)(-i\ {-j})\quad\text{and}\quad(i\ {-j})(-i\ j).
\]

For \(w\in D_9\), define

\[
\ell_T(w)=\min\{k:w=t_1\cdots t_k,\ t_j\in T\}.
\]

The absolute order \(P=\operatorname{Abs}(D_9)\) is the finite ranked poset
whose order relation is

\[
u\leq_T v\iff \ell_T(u)+\ell_T(u^{-1}v)=\ell_T(v),
\]

with rank sets \(P_i=\{w:\ell_T(w)=i\}\), \(0\leq i\leq9\).  Equivalently,
\(u\lessdot v\) exactly when \(v=ut\) for some \(t\in T\) and
\(\ell_T(v)=\ell_T(u)+1\).

## Normalized-flow assertion

The finite claim to be proved or disproved is:

> There are rational numbers \(f_i(x,y)\geq0\), one for every cover
> \(x\lessdot y\) with \(x\in P_i\), \(y\in P_{i+1}\), such that, for every
> \(0\leq i<9\),
> \[
> \sum_{y:x\lessdot y} f_i(x,y)=\frac1{|P_i|}\quad(x\in P_i),
> \qquad
> \sum_{x:x\lessdot y} f_i(x,y)=\frac1{|P_{i+1}|}\quad(y\in P_{i+1}).
> \]

Every rank is nonempty, so no zero denominator or empty-layer convention is
needed.  The nonnegativity convention includes zero.  A flow is allowed to be
different on different adjacent-rank layers.  No rank-symmetry assumption is
made.

## Exact orbit quotient used by the certificate

The proof uses the action of \(B_9\) on its normal subgroup \(D_9\) by
conjugation.  A \(B_9\)-orbit is indexed by a signed cycle type
\((\lambda,\mu)\), where \(\lambda\) lists positive-cycle lengths, \(\mu\)
lists negative-cycle lengths,

\[
|\lambda|+|\mu|=9,\qquad \ell(\mu)\equiv0\pmod2.
\]

For an orbit \(C_{\lambda,\mu}\),

\[
\operatorname{rank}(C_{\lambda,\mu})=9-\ell(\lambda),\qquad
|C_{\lambda,\mu}|=
\frac{2^9 9!}{2^{\ell(\lambda)+\ell(\mu)}z_\lambda z_\mu},
\]

where \(z_\lambda=\prod_j j^{m_j(\lambda)}m_j(\lambda)!\).  There are 150
such orbits.  Their rank totals are

\[
(1,72,2220,38304,405174,2702448,11228300,27491616,34812945,16216200).
\]

For adjacent-rank orbits \(C,D\), let \(E(C,D)\) be the number of absolute
cover edges from \(C\) to \(D\).  It suffices to give rational totals
\(F(C,D)\geq0\) satisfying

\[
\sum_D F(C,D)=\frac{|C|}{|P_i|},\qquad
\sum_C F(C,D)=\frac{|D|}{|P_{i+1}|}.
\]

Indeed, conjugation makes every nonempty orbit-pair cover graph biregular.
Assigning \(f(x,y)=F(C,D)/E(C,D)\) to every cover edge from \(C\) to \(D\)
lifts the orbit totals to the vertex equations above.

## Scope and endpoints

The certified endpoint is only \(n=9\).  It does not assert a uniform formula
for all \(n\), a recurrence \(D_n\to D_{n+1}\), uniqueness, strict positivity
on every cover edge, or any converse to the normalized-flow implication for
the strong Sperner property.  The standard convention \(D_n\) for an
irreducible Coxeter group begins at \(n=4\); no degenerate \(D_1,D_2,D_3\)
cases are part of the claim.
