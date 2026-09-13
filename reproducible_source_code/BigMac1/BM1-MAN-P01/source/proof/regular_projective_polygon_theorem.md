# Exact `F_A` spectrum for regular real projective polygons

## Theorem

Let `n >= 3`, let

\[
  v_j=(\cos(\pi j/n),\sin(\pi j/n))^T,\qquad 0\le j<n,
\]

and let `A_n=(v_i^T v_j)`.  Then `A_n` is a real correlation matrix of
rank two and

\[
  \operatorname{per}(A_n)=\frac{n!}{2^{n-1}}.
\]

If `F_n` has entries

\[
  (F_n)_{ij}=(A_n)_{ij}\operatorname{per}(A_n(i,j)),
\]

then its eigenvalues, indexed by `s=0,...,n-1`, are

\[
 \lambda_s=\frac{n!}{2^n}
 \left(
   \binom{n-1}{s}^{-1}+
   \binom{n-1}{s-1\pmod n}^{-1}
 \right).
\]

Consequently

\[
  \lambda_0=\operatorname{per}(A_n),\qquad
  \max_{1\le s<n}\lambda_s
   =\frac{n}{2(n-1)}\operatorname{per}(A_n)
   <\operatorname{per}(A_n).
\]

Thus the real Bapat--Sunder `F_A` inequality holds strictly away from the
constant eigenvector on this non-entrywise-nonnegative rank-two family in
every order.

## Proof

Put `theta_j=pi j/n`, `q_j=exp(2 i theta_j)`, and
`zeta=exp(2 pi i/n)`, so the `q_j` are all `n`th roots of unity.  We first
record a symmetric-tensor identity.  For two ordered lists of `m` real
two-vectors with angles `alpha_1,...,alpha_m` and
`beta_1,...,beta_m`, set `u_j=exp(2 i alpha_j)` and
`w_j=exp(2 i beta_j)`.  Expansion in the orthonormal complex basis of
`Sym^m(C^2)` gives

\[
 \operatorname{per}\bigl((x_{\alpha_p}^T x_{\beta_q})_{p,q=1}^m\bigr)
 =\frac{m!}{2^m}e^{i(\sum_p\alpha_p-\sum_q\beta_q)}
 \sum_{k=0}^m
 \frac{\overline{e_k(u_1,\ldots,u_m)}e_k(w_1,\ldots,w_m)}
      {\binom{m}{k}}. \tag{1}
\]

Indeed, the coefficient of the normalized symmetric basis vector with `k`
copies of the second complex basis vector is

\[
 2^{-m/2}e^{-i\sum_p\alpha_p}
 \frac{e_k(u_1,\ldots,u_m)}{\sqrt{\binom{m}{k}}},
\]

and the permanent is `m!` times the inner product of the two symmetrized
tensors.  This proves (1) directly from the definition.

For the full root set,

\[
 e_k(q_0,\ldots,q_{n-1})=0\quad(1\le k<n),
 \qquad |e_0|=|e_n|=1.
\]

Applying (1) with the same full list on both sides yields

\[
 \operatorname{per}(A_n)=\frac{n!}{2^n}(1+1)
 =\frac{n!}{2^{n-1}}. \tag{2}
\]

Now set `m=n-1`.  Removing `q_i` from the full root set gives, recursively,

\[
 e_k(q_0,\ldots,\widehat{q_i},\ldots,q_{n-1})=(-q_i)^k,
 \qquad 0\le k\le m. \tag{3}
\]

Let `d=j-i` modulo `n` and `delta=pi d/n`.  Substitution of (3) into (1)
gives

\[
 \operatorname{per}(A_n(i,j))
 =\frac{m!}{2^m}\sum_{k=0}^m
   \binom{m}{k}^{-1}\cos((2k+1)\delta). \tag{4}
\]

The apparently complex expression before taking real parts is already real:
pairing `k` with `m-k` uses `m=n-1` and `e^{2in\delta}=1`.

Write `c_k=binom(m,k)^{-1}`.  Since `(A_n)_{ij}=cos(delta)`, the elementary
product-to-sum identity turns (4) into

\[
 (F_n)_{ij}=\frac{m!}{2^{m+1}}
 \sum_{k=0}^{m}c_k
 \left[
  \cos\left(\frac{2\pi k d}{n}\right)+
  \cos\left(\frac{2\pi(k+1)d}{n}\right)
 \right]. \tag{5}
\]

Thus `F_n` is circulant.  With indices read modulo `n`, the coefficient of
the frequency `r` in (5) is `c_r+c_{r-1}`.  Since
`c_{n-1-k}=c_k`, the discrete Fourier transform gives

\[
 \lambda_s=\frac{(n-1)!}{2^n}n(c_s+c_{s-1}), \tag{6}
\]

which is the asserted spectrum.

For `s=0`, `c_0+c_{n-1}=2`, so (6) agrees with (2).  For
`1<=s<n`, both summands are at most one and they cannot both equal one.
More precisely, the largest nonconstant value occurs at `s=1,n-1` and is

\[
 \frac{1+1/(n-1)}{2}=\frac{n}{2(n-1)}<1
\]

after division by (2).  This proves the theorem.

## Why this family is nontrivial

For `n>=4`, the underlying unoriented lines wind around the entire real
projective circle.  No choice of signs places all pairwise inner products in
the nonnegative orthant, so the usual entrywise-nonnegative theorem does not
apply after diagonal sign switching.  The result is therefore not a disguised
instance of that standard sufficient condition.

## Scope

This theorem does not exclude a real counterexample elsewhere in order at
most 15 and does not prove the complete real rank-two conjecture.  It closes
one highly symmetric infinite family exactly.
