# Formal statement

## Ambient superalgebra and field

Fix an integer \(n\ge 1\) and a field \(K\) of characteristic zero.  (The source works over \(K=\mathbb C\); every finite computation below is over \(\mathbb Q\), and scalar extension from \(\mathbb Q\) to \(\mathbb C\) preserves the ranks in question.)  Let
\[
A_n(K)=K[x_1,\ldots,x_n]\otimes_K
\Lambda_K(\theta_1,\ldots,\theta_n,\xi_1,\ldots,\xi_n).
\]
The \(x_i\) are even and commute with every variable.  All \(2n\) odd variables anticommute with one another, including across the two species; hence every odd variable squares to zero.  Canonical odd monomials are written
\[
\theta_T\xi_S=\theta_{t_1}\cdots\theta_{t_p}
\xi_{s_1}\cdots\xi_{s_q}
\quad(t_1<\cdots<t_p,\ s_1<\cdots<s_q).
\]

The symmetric group \(S_n\) acts by the even superalgebra automorphisms
\(\sigma(x_i)=x_{\sigma(i)}\), \(\sigma(\theta_i)=\theta_{\sigma(i)}\), and \(\sigma(\xi_i)=\xi_{\sigma(i)}\).  Let \(A_n(K)^{S_n}_+\) be the invariant elements whose scalar (multidegree-zero) term is zero, and set
\[
I_n=\langle A_n(K)^{S_n}_+\rangle_{A_n(K)},\qquad
R_n^{(1,2)}(K)=A_n(K)/I_n.
\]
The grading used for finite blocks is \((d,p,q)=(\deg_x,\deg_\theta,\deg_\xi)\), where \(d\in\mathbb Z_{\ge0}\) and \(0\le p,q\le n\).

## Candidate monomials

A modified Motzkin path of length \(n\) starts at height \(0\), has first step up to height \(1\), and thereafter never has height below \(1\).  At position \(i\), its four possible steps and weights are

- up, of increment \(+1\) and weight \(1\);
- horizontal, of increment \(0\) and weight \(\theta_i\);
- horizontal, of increment \(0\) and weight \(\xi_i\);
- down, of increment \(-1\) and weight \(\theta_i\xi_i\).

For its weight \(\theta_T\xi_S\), necessarily \(T,S\subseteq\{2,\ldots,n\}\).  Define the generalized \(\alpha\)-sequence by
\[
\alpha_1(T,S)=0,
\qquad
\alpha_i(T,S)=\alpha_{i-1}(T,S)-1+
\mathbf 1_{i\notin T}+\mathbf 1_{i\notin S}
\quad(2\le i\le n).
\]
The path condition makes every \(\alpha_i(T,S)\) nonnegative.  Lentfer's finite set is
\[
B_n^{(1,2)}=
\left\{
x_1^{a_1}\cdots x_n^{a_n}\theta_T\xi_S:
\begin{array}{l}
\theta_T\xi_S\text{ is the weight of a modified Motzkin path},\\
0\le a_i\le\alpha_i(T,S)\text{ for every }i
\end{array}
\right\}.
\]
There are no identifications between differently written elements because the displayed ordering is canonical.
If the odd step weights are first multiplied in path order, their canonical
species-ordered form can acquire a sign.  Replacing that vector by its negative
does not change the basis endpoint; the serialized candidate convention uses
the displayed canonical representative.

## Source conjecture and target endpoint

The source conjecture is
\[
\forall n\ge1,\qquad
\{b+I_n:b\in B_n^{(1,2)}\}
\text{ is a }K\text{-basis of }R_n^{(1,2)}(K).
\]

The present finite endpoint is the exact \(n=5\) proposition over \(\mathbb Q\), equivalently over every characteristic-zero field:
\[
\boxed{\{b+I_5:b\in B_5^{(1,2)}\}\text{ is a basis of }R_5^{(1,2)}.}
\]
Because \(|B_5^{(1,2)}|=2^4 5!=1920\), the endpoint is equivalent to the conjunction of:

1. \(\dim_K R_5^{(1,2)}=1920\);
2. the 1920 candidate residue classes are linearly independent.

It is **not** part of the source conjecture that these monomials are the standard monomials for every term order.  A Gröbner computation may use any explicitly declared admissible order; if the candidate normal forms form a nonsingular coordinate matrix in the resulting standard-monomial basis, that proves the basis claim even when some candidates themselves reduce.

## Exact finite generator reduction to be proved and audited

For \(U\in\{1,\theta,\xi,\theta\xi\}\), put
\[
p_{r,U}=\sum_{i=1}^n x_i^r U_i,
\quad U_i\in\{1,\theta_i,\xi_i,\theta_i\xi_i\}.
\]
The convention \(p_{0,1}=n\) is a nonzero scalar and is excluded.  The proposed structural lemma is the exact ideal equality
\[
I_n=\left\langle
p_{r,1}\ (1\le r\le n),\quad
p_{r,U}\ (0\le r<n,\ U\in\{\theta,\xi,\theta\xi\})
\right\rangle.
\]
This equality must be established independently of the \(n=5\) Gröbner output; otherwise a computation with the displayed \(4n\) invariants would only concern a possibly larger quotient and would not settle the source conjecture.

## Edge and degenerate cases

- For \(n=1\), the first Motzkin step is forced up and \(B_1^{(1,2)}=\{1\}\); the invariant ideal contains \(x_1,\theta_1,\xi_1\), so the quotient is \(K\).
- Empty subsets and empty odd products are permitted and have product \(1\).
- Fermionic degrees outside \(0\le p,q\le n\) are zero because odd variables square to zero.
- Polynomial degree is a nonnegative integer; finiteness of the quotient follows already from the ordinary symmetric invariants, since \(p_{1,1},\ldots,p_{n,1}\) generate the same characteristic-zero ideal as the elementary symmetric polynomials.
- No floating-point, genericity, limiting, or division-by-a-variable convention is used.
